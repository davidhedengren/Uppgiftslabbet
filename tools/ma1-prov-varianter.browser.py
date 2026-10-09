"""Läsprov av nya Ma1-uppgifter, verklig rättning och alla självständiga elevkort.
Starta repona på 8071/8072. Inga elevförsök skrivs till servern.
"""
import json,urllib.request,os
from pathlib import Path
from playwright.sync_api import sync_playwright
cache={}
def cdn(route):
 u=route.request.url
 if u not in cache:
  with urllib.request.urlopen(u,timeout=30) as r:cache[u]=(r.status,dict(r.headers),r.read())
 st,h,b=cache[u];route.fulfill(status=st,headers={k:v for k,v in h.items() if k.lower() not in ['content-encoding','content-length','transfer-encoding']},body=b)
with sync_playwright() as p:
 browser=p.chromium.launch(executable_path=os.environ.get('CHROMIUM_PATH','/usr/bin/chromium'),args=['--no-sandbox'])
 pg=browser.new_page();pg.add_init_script("localStorage.setItem('kunskapsgymmet-beta-info','2')")
 pg.route('https://cdn.jsdelivr.net/**',cdn);pg.route('https://fonts.googleapis.com/**',lambda r:r.fulfill(status=200,content_type='text/css',body=''));pg.route('https://*.supabase.co/**',lambda r:r.abort())
 errors=[];pg.on('pageerror',lambda e:errors.append(str(e)))
 pg.goto('http://127.0.0.1:8072/index.html?kurs=ma1');pg.evaluate("selectCourse('ma1')");pg.wait_for_function('window.BANKMA1 && typeof renderMathInElement==="function"')
 quality=pg.evaluate('BANKMA1.filter(q=>q.kallaProv).flatMap(expandGameTask).map(q=>({id:q.id,findings:kvFacit(q)})).filter(x=>x.findings.length)')
 assert not quality,quality
 # Tester med rätt och fel värde i den faktiska appens grader, även per svarsdel.
 checks=pg.evaluate(r'''()=>{
 const out=[],questions=BANKMA1.filter(q=>q.kallaProv).flatMap(expandGameTask);
 for(const q of questions){
  if(arAlt(q))continue;
  const plan=svarsPlan(q);
  for(const [i,r] of plan.rutor.entries()){
   const d=plan.delar[r.del],facit=d.svar[r.plats],fmt=d.format[r.plats],unit=d.enhet[r.plats],tol=d.tol[r.plats];
   let good=String(facit),bad='999999';
   if(fmt==='grundpotensform'){let exp=Math.floor(Math.log10(Math.abs(Number(facit))));good=String(Number(facit)/10**exp)+'e'+exp;bad=String(Number(facit)*10);}
   if(fmt==='negativt_talpar')bad='(1;-5)';
   if(fmt==='brak_i_intervall')bad=q.svarVillkor.min;
   if(fmt==='forkortat_brak')bad='0';
   for(const [input,want] of [[good,true],[good.replace(/\./g,','),true],[bad,false]]){
    out.push({id:q.id,input,want,actual:delSvarRatt(input,facit,unit,tol,q,i,fmt)});
   }
  }
 }
 return out;
 }''')
 assert all(x['want']==x['actual'] for x in checks),[x for x in checks if x['want']!=x['actual']]
 # Alternativens egen motor körs med en lokal avslutshanterare, utan XP eller serveranrop.
 clicks=pg.evaluate('''()=>{
 finishAttempt=parts=>{window.__testParts=parts;state.answered=true;};
 const out=[];
 for(const q of BANKMA1.filter(q=>q.kallaProv).flatMap(expandGameTask).filter(arAlt)){
  altLista(q).forEach((a,i)=>{
   state.currentTask=q;state.answered=false;state.solutionShown=false;state.altValda=new Set();renderTraining();vaxlaAlt(i);kollaAlt();
   out.push({id:q.id,choice:i,want:!!a.ratt,actual:window.__testParts?.every(Boolean)});
  });
 }
 return out;
 }''')
 assert len(clicks)==18,clicks
 assert all(x['want']==x['actual'] for x in clicks),clicks
 # Kontrollera även hela knappen Kontrollera med verkliga svarsfält och återkoppling.
 attempts=pg.evaluate(r'''()=>{
 const out=[];
 for(const q of BANKMA1.filter(q=>q.kallaProv).flatMap(expandGameTask).filter(q=>!arAlt(q))){
  for(const correct of [true,false]){
   state.currentTask=q;state.answered=false;state.solutionShown=false;state.partResults=[];state.partIndex=0;state.altValda=new Set();window.__testParts=null;renderTraining();
   const plan=svarsPlan(q);
   for(const [i,r] of plan.rutor.entries()){
    const d=plan.delar[r.del],v=d.svar[r.plats],fmt=d.format[r.plats];
    let answer=String(v);
    if(fmt==='grundpotensform'){const e=Math.floor(Math.log10(Math.abs(Number(v))));answer=String(Number((Number(v)/10**e).toPrecision(12)))+'e'+e;}
    document.getElementById('ans-'+i).value=correct?answer:'999999';
   }
   for(let i=0;i<plan.rutor.length&&!state.answered;i++)checkAnswer();
   const parts=window.__testParts;
   out.push({id:q.id,want:correct,actual:parts?.every(Boolean),parts,feedback:[...document.querySelectorAll('[id^=corr-]')].map(e=>e.textContent)});
  }
 }
 return out;
 }''')
 assert len(attempts)==216,attempts
 assert all(x['want']==x['actual'] for x in attempts),[x for x in attempts if x['want']!=x['actual']]
 science=next(x for x in attempts if x['id']=='0.1109' and not x['want']);assert any('10' in text and '0,0006' not in text for text in science['feedback']),science
 # Enhetsnotation, värdesiffror och flera möjliga rätta exempel utöver kanonsvaret.
 cases=[['0.1121','(-1;-7)',True],['0.1121','(-0,5;-6,5)',True],['0.1121','(-8;-2)',False],['0.1133','13/20',True],['0.1133','3/5',False],['0.1133','2/3',False],['0.1133','0,65',True],['0.1109','6,2×10⁻⁴',True],['0.1109','0.00062',False],['0.1109','62e-5',False],['0.1139','64,79 kr/l',True],['0.1139','64,8',False],['3.547','26,7%',True],['3.547','26.8',False]]
 extra=pg.evaluate('''cases=>cases.map(([id,input,want])=>{const q=BANKMA1.find(q=>q.id===id);return {id,input,want,actual:delSvarRatt(input,q.rättSvar,q.svarEnhet,q.tolerans,q,0,q.svarFormat)};})''',cases)
 assert all(x['want']==x['actual'] for x in extra),[x for x in extra if x['want']!=x['actual']]
 ids=pg.evaluate('BANKMA1.filter(q=>q.kallaProv).flatMap(expandGameTask).map(q=>q.id)')
 render=[]
 for width in [390,1174]:
  pg.set_viewport_size({'width':width,'height':1000})
  for id in ids:
   pg.evaluate('''id=>{const q=BANKMA1.filter(q=>q.kallaProv).flatMap(expandGameTask).find(q=>q.id===id);state.currentTask=q;state.answered=false;state.solutionShown=false;state.partResults=[];state.partIndex=0;state.altValda=new Set();renderTraining();showSolution();}''',id)
   pg.evaluate('document.fonts.ready');pg.wait_for_timeout(20)
   check=pg.evaluate('''()=>({id:state.currentTask.id,overflow:document.documentElement.scrollWidth>innerWidth,errors:document.querySelectorAll('.katex-error').length,numbered:document.querySelectorAll('.facit-steglista').length,inputs:document.querySelectorAll('input[id^=ans-]').length,expected:arAlt(state.currentTask)?0:expectedAnswersForTask(state.currentTask).answers.length,wide:[...document.querySelectorAll('.sol .katex-display')].filter(e=>e.scrollWidth>e.clientWidth+2).map(e=>e.querySelector('annotation')?.textContent)})''')
   assert not check['overflow'] and not check['errors'] and not check['wide'] and not check['numbered'] and check['inputs']==check['expected'],(id,width,check)
   if id in ['0.1127','0.1128','2.550a','2.552a','0.1121','0.1133','0.1109','0.1136','0.1148','0.1151','0.1156','2.550a','2.550b','2.552b','7.544']:
    pg.evaluate('document.activeElement.blur();window.scrollTo(0,0)');pg.screenshot(full_page=True,path=f'/tmp/ma1-prov-{id}-{width}.png')
   render.append(check)
 # Lärarbankens samtliga nya texter och facit i båda bredderna.
 teacher=browser.new_page();teacher.route('https://cdn.jsdelivr.net/**',cdn);teacher.route('https://fonts.googleapis.com/**',lambda r:r.fulfill(status=200,content_type='text/css',body=''));teacher.route('https://*.supabase.co/**',lambda r:r.abort())
 teacher.goto('http://127.0.0.1:8071/index.html?kurs=ma1');teacher.wait_for_function('window.BANKMA1 && typeof renderMathInElement==="function"')
 parentids=teacher.evaluate('BANKMA1.filter(q=>q.kallaProv).map(q=>q.id)');assert len(parentids)==90
 for width in [390,1174]:
  teacher.set_viewport_size({'width':width,'height':1000})
  for id in parentids:
   teacher.evaluate('''id=>{const q=BANKMA1.find(q=>q.id===id);document.body.classList.remove('password-locked');document.body.innerHTML='<article class="tbody" style="max-width:850px;margin:16px;padding:12px">'+uppgiftsText(q)+LOS(q.s)+altFacit(q)+'</article>';renderMathInElement(document.body,{delimiters:[{left:"\\\\[",right:"\\\\]",display:true},{left:"\\\\(",right:"\\\\)",display:false}],throwOnError:false});}''',id)
   c=teacher.evaluate('''()=>({errors:document.querySelectorAll('.katex-error').length,overflow:document.documentElement.scrollWidth>innerWidth,wide:[...document.querySelectorAll('.katex-display')].filter(e=>e.scrollWidth>e.clientWidth+2).map(e=>e.querySelector('annotation')?.textContent)})''')
   assert not c['errors'] and not c['overflow'] and not c['wide'],(id,width,c)
 assert not errors,errors
 print(json.dumps({'numericChecks':len(checks)+len(extra),'choiceChecks':len(clicks),'uiAttempts':len(attempts),'studentCards':len(ids),'studentViews':len(render),'teacherViews':180,'failures':[]},ensure_ascii=False))
 browser.close()
