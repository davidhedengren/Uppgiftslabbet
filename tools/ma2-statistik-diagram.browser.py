"""Verify the new Ma2 graphs/tables in both apps; no XP or database writes."""
import json,urllib.request
from pathlib import Path
from playwright.sync_api import sync_playwright
cache={}
def cdn(route):
 u=route.request.url
 if u not in cache:
  with urllib.request.urlopen(u,timeout=30) as r:cache[u]=(r.status,dict(r.headers),r.read())
 st,h,b=cache[u];route.fulfill(status=st,headers={k:v for k,v in h.items() if k.lower() not in ['content-encoding','content-length','transfer-encoding']},body=b)
ids=[f'4.{n}' for n in range(307,322)]
cases=[
 ['4.307',0,['5'],[True]],['4.307',0,['9'],[False]],['4.308',0,['18'],[True]],['4.308',0,['6'],[False]],
 ['4.310',0,['7 min'],[True]],['4.310',0,['6'],[False]],
 ['4.311',0,['1'],[True]],['4.311',0,['1.3'],[False]],['4.311',1,['1,3'],[True]],['4.311',1,['13/10'],[True]],['4.311',1,['1.3 böcker'],[True]],['4.311',1,['1'],[False]],
 ['4.312',0,['A'],[True]],['4.312',0,['a'],[True]],['4.312',0,['B'],[False]],['4.312',1,['20'],[True]],['4.312',1,['20 procentenheter'],[True]],['4.312',1,['20%'],[False]],['4.312',1,['0.2'],[False]],
 ['4.313',0,['60'],[True]],['4.313',0,['240*0.25'],[True]],['4.313',0,['25'],[False]],['4.313',0,['60.1'],[False]],
 ['4.314',0,['16'],[True]],['4.314',0,['28'],[False]],['4.315',0,['40 min'],[True]],['4.315',0,['75'],[False]],
 ['4.316',0,['A'],[True]],['4.316',0,['B'],[False]],['4.316',1,['6 min'],[True]],['4.316',1,['360 s'],[True]],['4.316',1,['8'],[False]],['4.316',1,['14'],[False]],
 ['4.317',0,['5'],[True]],['4.317',0,['300 s'],[True]],['4.317',0,['4'],[False]],['4.317',0,['6'],[False]],
 ['4.319',0,['7'],[True]],['4.319',0,['x=7'],[True]],['4.319',0,['7.01'],[False]],['4.319',0,['15'],[False]],
 ['4.321',0,['5','9'],[True,True]],['4.321',0,['5 min','9 min'],[True,True]],['4.321',0,['9','5'],[False,False]],['4.321',0,['7','7'],[False,False]],['4.321',0,['5.1','9.1'],[False,False]]]
with sync_playwright() as p:
 browser=p.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox']);student=browser.new_page(viewport={'width':1280,'height':1100});errors=[];student.on('pageerror',lambda e:errors.append(str(e)))
 for page in [student]:
  page.route('https://cdn.jsdelivr.net/**',cdn);page.route('https://fonts.googleapis.com/**',lambda r:r.fulfill(status=200,content_type='text/css',body=''));page.route('https://*.supabase.co/**',lambda r:r.abort())
 student.add_init_script("localStorage.setItem('kunskapsgymmet-beta-info','2')");student.goto('http://127.0.0.1:8083/index.html');student.evaluate("selectCourse('ma2')");student.wait_for_function('window.BANKMA2&&typeof renderMathInElement==="function"&&typeof nerdamer==="function"')
 tracks=student.evaluate('''ids=>['2a','2b','2c'].map(track=>{state.track=track;const q=availableTasks().filter(q=>ids.includes(q.parentId||q._parentId||q.id.split('#')[0]));const all=ids.map(id=>expandGameTask(BANKMA2.find(q=>q.id===id))).flat();const pool=availableTasks();return{track,cards:all.length,missing:all.filter(q=>!pool.some(x=>x.id===q.id)).map(q=>q.id)};})''',ids)
 assert all(t['cards']==18 and not t['missing'] for t in tracks),tracks
 student.evaluate('''()=>{
 finishAttempt=parts=>{state.answered=true;window.reviewOutcome=parts;};
 window.reviewCard=(q)=>{state.currentTask=q;state.answered=false;state.solutionShown=false;state.partResults=[];state.partIndex=0;state.altValda=new Set();state.altOrdningId=null;window.reviewOutcome=null;renderTraining();};
 }''')
 results=[]
 for id,part,inputs,want in cases:
  r=student.evaluate('''([id,part,inputs])=>{
   const q=expandGameTask(BANKMA2.find(q=>q.id===id))[part];reviewCard(q);
   const n=document.querySelectorAll('[id^="ans-"]').length;if(n!==inputs.length)throw Error(id+' fields '+n+'/'+inputs.length);
   inputs.forEach((text,i)=>{const el=document.getElementById('ans-'+i);if(el.disabled)throw Error(id+' disabled '+i);el.value=text;document.getElementById('kollaknapp').click();});
   return{id,part,inputs,actual:window.reviewOutcome||state.partResults};
  }''',[id,part,inputs]);results.append(r);assert r['actual']==want,(r,want)
 choices=[]
 for id in ['4.309','4.318','4.320']:
  for original in range(4):
   r=student.evaluate('''([id,original])=>{const q=BANKMA2.find(q=>q.id===id);reviewCard(q);const display=state.altOrdning.indexOf(original);document.getElementById('alt-'+display).click();document.getElementById('altknapp').click();return{id,original,want:q.alternativ[original].ratt,actual:window.reviewOutcome?.every(Boolean)};}''',[id,original]);choices.append(r);assert r['actual']==r['want'],r
 views=[]
 for width in [390,1280]:
  student.set_viewport_size({'width':width,'height':1100})
  for id in ids:
   parts=student.evaluate('id=>expandGameTask(BANKMA2.find(q=>q.id===id)).length',id)
   for part in range(parts):
    student.evaluate('([id,part])=>{reviewCard(expandGameTask(BANKMA2.find(q=>q.id===id))[part]);showSolution();document.activeElement.blur();window.scrollTo(0,0);}',[id,part]);student.evaluate('document.fonts.ready')
    metrics=student.evaluate('''()=>({katex:document.querySelectorAll('.task .katex-error').length,overflow:document.documentElement.scrollWidth>innerWidth+1,wideTables:[...document.querySelectorAll('.task table')].filter(t=>t.getBoundingClientRect().right>innerWidth+1).length,wideMath:[...document.querySelectorAll('.task .katex-display')].filter(e=>e.scrollWidth>e.clientWidth+2).length,figures:document.querySelectorAll('.task svg').length})''');assert not metrics['katex'] and not metrics['overflow'] and not metrics['wideTables'] and not metrics['wideMath'],(id,part,width,metrics);views.append({'app':'Kunskapsgymmet','id':id,'part':part,'width':width,**metrics})
    if width==390:student.locator('.task').screenshot(path=f'/tmp/ma2-stat-{id}-{part}-390.png')
 teacher=browser.new_page(viewport={'width':1280,'height':1100});teacher.on('pageerror',lambda e:errors.append(str(e)))
 teacher.route('https://cdn.jsdelivr.net/**',cdn);teacher.route('https://fonts.googleapis.com/**',lambda r:r.fulfill(status=200,content_type='text/css',body=''));teacher.route('https://*.supabase.co/**',lambda r:r.abort())
 teacher.goto('http://127.0.0.1:8085/index.html?kurs=ma2');teacher.wait_for_function('window.BANKMA2&&typeof renderMathInElement==="function"')
 teacherAreas=teacher.evaluate('''()=>['2a','2b','2c'].map(track=>{state.spår=track;byggTräd();return{track,text:document.querySelector('[data-omr="4:tabeller_diagram"]')?.textContent};})''');assert all(x['text'] and 'Tabeller och diagram' in x['text'] for x in teacherAreas),teacherAreas
 teacher.evaluate('''()=>{document.body.classList.remove('password-locked');document.body.innerHTML='<main id="review-main" style="box-sizing:border-box;width:100%;padding:12px;color:#172b3a;background:white"></main>';}''')
 for width in [390,1280]:
  teacher.set_viewport_size({'width':width,'height':1100})
  for id in ids:
   r=teacher.evaluate(r'''id=>{const q=BANKMA2.find(q=>q.id===id);document.getElementById('review-main').innerHTML='<article style="max-width:720px;margin:auto">'+uppgiftsText(q)+q.s+'</article>';renderMathInElement(document.getElementById('review-main'),{delimiters:[{left:'\\[',right:'\\]',display:true},{left:'\\(',right:'\\)',display:false}],throwOnError:false});return{id,katex:document.querySelectorAll('.katex-error').length,overflow:document.documentElement.scrollWidth>innerWidth+1,mathNodes:document.querySelectorAll('.katex').length};}''',id)
   assert not r['katex'] and not r['overflow'],(id,width,r)
   if id in ['4.311','4.313','4.317','4.318','4.319','4.320','4.321']:assert r['mathNodes']>0,(id,width,r)
   if id in ['4.309','4.318','4.320']:assert teacher.locator('#review-main').inner_text().count('A.')>=1,id
   views.append({'app':'Uppgiftslabbet','width':width,**r})
 # Contact sheet for manual review of every unique figure.
 teacher.set_viewport_size({'width':1500,'height':1600});teacher.evaluate(r'''ids=>{document.getElementById('review-main').innerHTML='<div style="display:grid;grid-template-columns:repeat(3,480px);gap:10px">'+ids.map(id=>{const q=BANKMA2.find(q=>q.id===id),fig=q.t.match(/<svg[\s\S]*?<\/svg>/)?.[0];return fig?'<section><b>'+id+'</b>'+fig+'</section>':'';}).join('')+'</div>';}''',ids);teacher.screenshot(path='/tmp/ma2-statistik-all-figures.png',full_page=True)
 assert not errors,errors
 report={'numericCases':results,'choiceCases':choices,'views':views,'tracks':tracks,'teacherAreas':teacherAreas,'javascriptErrors':errors};Path('/tmp/ma2-statistik-browser.json').write_text(json.dumps(report,ensure_ascii=False,indent=2));print('PASS',len(results),'numeric combinations,',len(choices),'clicked choices,',len(views),'views, all three tracks; no JavaScript errors');browser.close()
