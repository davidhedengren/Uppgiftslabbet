"""Pröva vätsketrycksuppgifternas slutsvar och svarsalternativ med Kunskapsgymmets riktiga rättning."""
import argparse
import json
import math
import re
import subprocess
import urllib.request
from decimal import Decimal, ROUND_HALF_UP
from pathlib import Path
from playwright.sync_api import sync_playwright

parser = argparse.ArgumentParser()
parser.add_argument('--student-port', type=int, default=8072)
args = parser.parse_args()
root = Path(__file__).resolve().parent.parent
# De manuellt uppställda fysikrelationerna finns i kontraktstestet, inte i bankens facit.
script = r"""
const fs=require('node:fs'),vm=require('node:vm');
const file=process.argv[1];
let source=fs.readFileSync(file,'utf8');source=source.slice(0,source.indexOf("test('"));
const result=vm.runInNewContext(source+'\nJSON.stringify(cases.map(([id,f])=>[id,f(),f()]))',
 {require,__dirname:require('node:path').dirname(file)});
process.stdout.write(result);
"""
models = json.loads(subprocess.check_output(
    ['node', '-e', script, str(root / 'tools/fysik1-vatsketryck.test.js')], text=True))
cache = {}

def cdn(route):
    url = route.request.url
    if url not in cache:
        with urllib.request.urlopen(url, timeout=30) as response:
            cache[url] = (response.status, dict(response.headers), response.read())
    status, headers, body = cache[url]
    route.fulfill(status=status, headers={k: v for k, v in headers.items()
                  if k.lower() not in ['content-encoding', 'content-length', 'transfer-encoding']}, body=body)

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(executable_path='/usr/bin/chromium', args=['--no-sandbox'])
    page = browser.new_page()
    page.route('https://cdn.jsdelivr.net/**', cdn)
    page.goto(f'http://127.0.0.1:{args.student_port}/index.html?kurs=fy1')
    page.evaluate("selectCourse('fy1')")
    page.wait_for_function('window.BANK && typeof renderMathInElement === "function"')
    cards = page.evaluate('BANK.filter(q=>q.spel!==false).flatMap(expandGameTask)')
    by_id = {q['id']: q for q in cards}
    cases = []
    for task_id, exact, approximate in models:
        values = exact if isinstance(exact, list) else [exact]
        alternatives = approximate if isinstance(approximate, list) else [approximate]
        for index, (value, alternative) in enumerate(zip(values, alternatives)):
            card_id = task_id + chr(97 + index) if len(values) > 1 else task_id
            card = by_id[card_id]
            precision = re.search(r'(\d+|en|två|tre|fyra) decimal', card['t'])
            for target in [value]:
                if precision:
                    word = precision[1]
                    decimals = int(word) if word.isdigit() else {'en': 1, 'två': 2, 'tre': 3, 'fyra': 4}[word]
                    rounded = str(Decimal(str(target)).quantize(Decimal(10) ** -decimals, rounding=ROUND_HALF_UP))
                elif 'heltal' in card['t']:
                    rounded = str(Decimal(str(target)).quantize(Decimal(1), rounding=ROUND_HALF_UP))
                elif (sf := re.search(r'(två|tre|fyra|\d+) värdesiffror', card['t'])):
                    n = int(sf[1]) if sf[1].isdigit() else {'två':2,'tre':3,'fyra':4}[sf[1]]
                    rounded = f'{target:.{n}g}'
                else:
                    rounded = str(target)
                unit = card.get('svarEnhet') or ''
                cases.extend([[card_id, str(target), True], [card_id, rounded, True],
                              [card_id, rounded.replace('.', ',') + ' ' + unit, True]])
            margin = max((card.get('tolerans') or 0) * 3, abs(value) * 1e-5, 1e-12)
            cases.extend([[card_id, str(value + margin), False],
                          [card_id, str(value - margin), False]])
    cases.extend([
        ['6.354','9820 Pa',True],['6.354','9,82 Pa',False],
        ['6.443b','45,8 mm',True],['6.443b','45,75 mm',True],['6.443b','45,6 mm',False],
        ['6.442a','101000 Pa',True],['6.442a','102000 Pa',False],
        ['6.445b','1,6 N',True],['6.445b','1,61446692 N',True],['6.445b','3,2 N',False],
        ['6.445b',str(17200*.94e-4),True],['6.445b','1,62 N',True],['6.445b','1,7 N',False],
        ['6.436b','2,97e5 Pa',True],['6.437c','1,01e4 m',True],
        ['6.439a','1,9e6 Pa',True],['6.439b','189 m',True],
    ])
    page.evaluate('window.reviewCards=BANK.filter(q=>q.spel!==false).flatMap(expandGameTask)')
    results = page.evaluate('''cases=>cases.map(([id,input,want])=>{
      const q=reviewCards.find(q=>q.id===id);
      return {id,input,want,actual:delSvarRatt(input,q.rättSvar,q.svarEnhet,q.tolerans,q,0,q.svarFormat)};
    })''', cases)
    failures = [result for result in results if result['actual'] != result['want']]
    assert not failures, failures
    # Kör även det riktiga gränssnittet för djupfrågans tre svarsalternativ.
    choices = page.evaluate('''()=>{
      const checks=[];window.finishAttempt=delar=>{window.choiceTestResult=delar;};
      for(const id of ['6.355']){
        const q=BANK.find(q=>q.id===id);if(!arAlt(q))throw Error(id+' saknar alternativ');
        for(let k=0;k<q.alternativ.length;k++){
          state.currentTask=q;state.answered=false;state.altValda=new Set();
          state.altOrdningId=null;window.choiceTestResult=null;
          renderAltTask(q);const a=altLista(q),i=a.findIndex(x=>x.txt===q.alternativ[k].txt);
          vaxlaAlt(i);kollaAlt();checks.push({id,want:a[i].ratt,actual:window.choiceTestResult[0]});
        }
      }return checks;
    }''')
    assert all(result['want'] == result['actual'] for result in choices), choices
    render = page.evaluate(r'''()=>{
      const qs=BANK.filter(q=>q.omr==='vatsketryck');
      document.body.innerHTML=qs.flatMap(q=>[q,...(q.spel!==false?expandGameTask(q):[])]).map(q=>
        '<article><div class="tbody">'+q.t+'</div><div class="sol facit öppen">'+q.s+'</div></article>').join('');
      renderMathInElement(document.body,{delimiters:[{left:'\\[',right:'\\]',display:true},{left:'\\(',right:'\\)',display:false}],throwOnError:false});
      return {main:qs.length,math:document.querySelectorAll('.katex').length,errors:document.querySelectorAll('.katex-error').length,
        numberedSolutions:document.querySelectorAll('.facit-steglista').length};
    }''')
    assert render['main']==97 and render['math']>500 and render['errors']==0 and render['numberedSolutions']==0, render
    print(json.dumps({'numericChecks': len(results), 'choiceChecks': len(choices), 'render':render,'failures': failures}))
    browser.close()
