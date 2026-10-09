"""Pröva gaslagens slutsvar och svarsalternativ med Kunskapsgymmets riktiga rättning."""
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
const result=vm.runInNewContext(source+'\nJSON.stringify(cases.map(([id,f])=>[id,f(273.15),f(273)]))',
 {require,__dirname:require('node:path').dirname(file)});
process.stdout.write(result);
"""
models = json.loads(subprocess.check_output(
    ['node', '-e', script, str(root / 'tools/fysik1-gaslagen.test.js')], text=True))
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
            for target in [value, alternative]:
                if precision:
                    word = precision[1]
                    decimals = int(word) if word.isdigit() else {'en': 1, 'två': 2, 'tre': 3, 'fyra': 4}[word]
                    rounded = str(Decimal(str(target)).quantize(Decimal(10) ** -decimals, rounding=ROUND_HALF_UP))
                elif 'heltal' in card['t']:
                    rounded = str(Decimal(str(target)).quantize(Decimal(1), rounding=ROUND_HALF_UP))
                elif 'tre värdesiffror' in card['t']:
                    rounded = f'{target:.3g}'
                else:
                    rounded = str(target)
                unit = card.get('svarEnhet') or ''
                cases.extend([[card_id, str(target), True], [card_id, rounded, True],
                              [card_id, rounded + ' ' + unit, True]])
            margin = max((card.get('tolerans') or 0) * 3, abs(value) * 1e-5, 1e-5)
            cases.extend([[card_id, str(max(value, alternative) + margin), False],
                          [card_id, str(min(value, alternative) - margin), False]])
    cases.extend([
        ['6.145', '298 K', False], ['6.146', '77 °C', False],
        ['6.524', '0,294 m', True], ['6.524', '0,29 m', False],
        ['6.529', '0,0713 kg', True], ['6.529', '0,071 kg', False],
        ['6.542', '0,0667 m', True], ['6.542', '0,067 m', False],
        ['6.535b', '5,46 h', True], ['6.535b', '5,48 h', False],
        ['6.537a', '27,2 min', True], ['6.537a', '27,6 min', False],
        ['6.537b', '10,9 min', True], ['6.537b', '11,2 min', False],
    ])
    page.evaluate('window.reviewCards=BANK.filter(q=>q.spel!==false).flatMap(expandGameTask)')
    results = page.evaluate('''cases=>cases.map(([id,input,want])=>{
      const q=reviewCards.find(q=>q.id===id);
      return {id,input,want,actual:delSvarRatt(input,q.rättSvar,q.svarEnhet,q.tolerans,q,0,q.svarFormat)};
    })''', cases)
    failures = [result for result in results if result['actual'] != result['want']]
    assert not failures, failures
    # Kör även det riktiga gränssnittet för alla fyra flervalsuppgifters alternativ.
    choices = page.evaluate('''()=>{
      const checks=[];window.finishAttempt=delar=>{window.choiceTestResult=delar;};
      for(const id of ['6.147','6.289','6.516','6.518']){
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
    print(json.dumps({'numericChecks': len(results), 'choiceChecks': len(choices), 'failures': failures}))
    browser.close()
