"""Real inputs and figure layouts for Fy1 #8.518–8.529. Production RPCs are blocked."""
import json,urllib.request
from pathlib import Path
from playwright.sync_api import sync_playwright
models=json.loads((Path(__file__).parent/'fixtures/fysik1-elektricitet-fordjupning.json').read_text());ids=[m['id'] for m in models];cache={}
def cdn(route):
 u=route.request.url
 if u not in cache:
  with urllib.request.urlopen(u,timeout=30) as r:cache[u]=(r.status,r.read(),r.headers.get('Content-Type','application/javascript'))
 st,b,t=cache[u];route.fulfill(status=st,body=b,content_type=t)
def configure(page,errors):
 page.on('pageerror',lambda e:errors.append(str(e)));page.route('https://*.supabase.co/**',lambda r:r.abort());page.route('https://cdn.jsdelivr.net/**',cdn);page.route('https://fonts.googleapis.com/**',lambda r:r.fulfill(status=200,body=''))
with sync_playwright() as p:
 browser=p.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox']);page=browser.new_page(viewport={'width':1280,'height':1100});errors=[];configure(page,errors);page.add_init_script("localStorage.setItem('kunskapsgymmet-beta-info','2')");page.goto('http://127.0.0.1:8083/index.html');page.evaluate("selectCourse('fy1')");page.wait_for_function('window.BANK&&typeof nerdamer==="function"&&typeof renderMathInElement==="function"');
 missing=page.evaluate('ids=>ids.filter(id=>!availableTasks().some(q=>q.id===id))',ids);assert not missing,missing
 page.evaluate('''()=>{finishAttempt=parts=>{state.answered=true;window.outcome=parts;};window.review=q=>{state.currentTask=q;state.answered=false;state.solutionShown=false;state.partResults=[];state.partIndex=0;state.altValda=new Set();state.altOrdningId=null;window.outcome=null;renderTraining();};}''')
 cards=page.evaluate('ids=>ids.map(id=>{const q=BANK.find(q=>q.id===id);return{id,a:q.rättSvar,alts:q.alternativ,unit:q.svarEnhet};})',ids);answers=[];views=[]
 def check(id,inputs,want):
  r=page.evaluate('''([id,inputs])=>{review(BANK.find(q=>q.id===id));inputs.forEach((value,i)=>{const el=document.getElementById('ans-'+i);if(!el||el.disabled)throw Error(id+' input '+i);el.value=value;document.getElementById('kollaknapp').click();});return outcome||state.partResults;}''',[id,inputs]);assert r==want,(id,inputs,r,want);answers.append([id,inputs,r])
 for card in cards:
  id=card['id']
  if card.get('alts'):
   correct=[i for i,a in enumerate(card['alts']) if a['ratt']]
   for mask in range(1,2**len(card['alts'])):
    selected=[i for i in range(len(card['alts'])) if mask&(1<<i)];r=page.evaluate('''([id,selected])=>{review(BANK.find(q=>q.id===id));selected.forEach(i=>document.getElementById('alt-'+state.altOrdning.indexOf(i)).click());document.getElementById('altknapp').click();return outcome;}''',[id,selected]);assert r==[selected==correct],(id,selected,r);answers.append([id,selected,r])
   continue
  a=card['a'] if isinstance(card['a'],list) else [card['a']];full=[str(x).replace('.',',') for x in a];digits=3 if id=='8.523' else 1 if id in ['8.520','8.527'] else 2
  check(id,full,[True]*len(a));check(id,[str(round(x,digits)).replace('.',',') for x in a],[True]*len(a));check(id,[str(x+10) for x in a],[False]*len(a))
  if len(a)>1:check(id,full[1:]+full[:1],[a[(i+1)%len(a)]==a[i] for i in range(len(a))])
 for id,values,want in [('8.518',['3 nC','2 nC','3 nC'],[True]*3),('8.519',['-40 cm'],[True]),('8.519',['0,133333'],[False]),('8.520',['1,6 µN','30,7 grader'],[True,True]),('8.520',['1,5','30,6'],[False,False]),('8.523',['9/16'],[True]),('8.523',['0,563'],[True]),('8.523',['0,562'],[False]),('8.525',['12 V','1 Ω'],[True,True]),('8.526',['2 V','0,004 A'],[True,True]),('8.527',['12 V','83,3 %'],[True,True]),('8.528',['16/3','8/3'],[True,True]),('8.529',['8 Ω','7/3 A'],[True,True])]:check(id,values,want)
 for theme in ['dark','light']:
  page.evaluate('(t)=>document.documentElement.dataset.theme=t',theme)
  for width in [390,1280]:
   page.set_viewport_size({'width':width,'height':1200})
   for id in ids:
    page.evaluate('id=>{review(BANK.find(q=>q.id===id));showSolution();document.activeElement.blur();}',id);page.evaluate('document.fonts.ready');r=page.evaluate('''()=>({latex:document.querySelectorAll('.task .katex-error').length,overflow:document.documentElement.scrollWidth>innerWidth+1,wideMath:[...document.querySelectorAll('.task .katex-display')].filter(e=>e.scrollWidth>e.clientWidth+2).length,figures:document.querySelectorAll('.task svg[role="img"]').length})''');assert not r['latex'] and not r['overflow'] and not r['wideMath'],(id,theme,width,r);assert r['figures']>=1;views.append(['student',id,theme,width,r])
    if width==390 and theme=='dark' and id in ['8.519','8.520','8.524','8.525','8.529']:page.locator('.task').screenshot(path='/tmp/fy1-electric-mobile-'+id+'.png')
 teacher=browser.new_page(viewport={'width':1280,'height':1200});configure(teacher,errors);teacher.goto('http://127.0.0.1:8085/index.html?kurs=fy1');teacher.wait_for_function('window.BANK&&typeof renderMathInElement==="function"');teacher.evaluate("()=>{document.body.classList.remove('password-locked');document.body.innerHTML='<main id=review style=\"padding:12px;color:#173548;background:white\"></main>'}")
 for width in [390,1280]:
  teacher.set_viewport_size({'width':width,'height':1200})
  for id in ids:
   teacher.evaluate(r'''id=>{const q=BANK.find(q=>q.id===id),el=document.getElementById('review');el.innerHTML=uppgiftsText(q)+q.s;if(q.alternativ&&!q.alternativ.every(a=>uppgiftsText(q).includes(a.txt)))throw Error('Alternatives missing '+id);renderMathInElement(el,{delimiters:[{left:'\\[',right:'\\]',display:true},{left:'\\(',right:'\\)',display:false}],throwOnError:false});}''',id);teacher.evaluate('document.fonts.ready');r=teacher.evaluate('''()=>({latex:document.querySelectorAll('.katex-error').length,overflow:document.documentElement.scrollWidth>innerWidth+1})''');assert not r['latex'] and not r['overflow'],(id,width,r);views.append(['teacher',id,width,r])
 teacher.set_viewport_size({'width':1600,'height':2200});teacher.evaluate('''ids=>{document.getElementById('review').innerHTML='<div style="display:grid;grid-template-columns:repeat(3,520px);gap:8px">'+ids.map(id=>{const q=BANK.find(q=>q.id===id);return'<section><b>'+id+' · nivå '+q.traningsniva+'</b>'+q.t.match(/<svg[\\s\\S]*?<\\/svg>/)[0]+'</section>';}).join('')+'</div>';}''',ids);teacher.screenshot(path='/tmp/fy1-electric-figures.png',full_page=True)
 assert not errors,errors;Path('/tmp/fy1-electric-browser.json').write_text(json.dumps({'answers':answers,'views':views,'errors':errors},ensure_ascii=False,indent=2));print('PASS',len(answers),'answer combinations,',len(views),'views');browser.close()
