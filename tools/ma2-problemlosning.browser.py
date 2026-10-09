"""Kontrollera det blandade geometriområdets verkliga val, figurer och rättning."""
import json,urllib.request
from pathlib import Path
from playwright.sync_api import sync_playwright
cache={}
def cdn(route):
 u=route.request.url
 if u not in cache:
  with urllib.request.urlopen(u,timeout=30) as r:cache[u]=(r.status,dict(r.headers),r.read())
 st,h,b=cache[u];route.fulfill(status=st,headers={k:v for k,v in h.items() if k.lower() not in ['content-encoding','content-length','transfer-encoding']},body=b)
with sync_playwright() as p:
 browser=p.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox'])
 student=browser.new_page();student.add_init_script("localStorage.setItem('kunskapsgymmet-beta-info','2')")
 for page in [student]:
  page.route('https://cdn.jsdelivr.net/**',cdn);page.route('https://fonts.googleapis.com/**',lambda r:r.fulfill(status=200,content_type='text/css',body=''));page.route('https://*.supabase.co/**',lambda r:r.abort())
 student.goto('http://127.0.0.1:8072/index.html?kurs=ma2');student.evaluate("selectCourse('ma2')");student.wait_for_function('window.BANKMA2 && typeof renderMathInElement==="function"')
 tracks=student.evaluate('''()=>{const out=[];for(const track of ['2a','2b','2c']){state.track=track;out.push({track,count:availableTasks().filter(q=>q.omr==='geometri_problemlosning').length});}state.track='2c';return out;}''')
 assert tracks==[{'track':'2a','count':0},{'track':'2b','count':15},{'track':'2c','count':15}],tracks
 values=[['3.478',20,'cm²'],['3.484',3.6,'m'],['3.485',4.8,'m'],['3.486',9.5,'m'],['3.531',8,'cm'],['3.532',80,'°'],['3.533',12,'cm²'],['3.534',12,'cm'],['3.535',30/7,'cm'],['3.536',2.4,'cm'],['3.537',55,'°'],['3.538',24,'cm²'],['3.539',90,'°']]
 cases=[]
 for id,val,unit in values:
  for text in [str(val),str(val).replace('.',','),f'{val} {unit}']:
   cases.append([id,text,True])
  for wrong in [str(val/2),str(val*2),str(-val)]:cases.append([id,wrong,False])
 # Alternativa uttryck, koordinatnotation och svar med efterfrågad avrundning.
 cases += [['3.479',s,True] for s in ['24sqrt(2)','24*sqrt(2)','12sqrt(8)']]+[['3.479','24',False],['3.479','-24sqrt(2)',False],['3.530','(5.25,0.75)',True],['3.530','(5,25;0,75)',True],['3.530','(0.75,5.25)',False],['3.535','4,29 cm',True],['3.535','4.28',False]]
 results=student.evaluate('''cases=>cases.map(([id,input,want])=>{const q=BANKMA2.find(q=>q.id===id);return {id,input,want,actual:delSvarRatt(input,q.rättSvar,q.svarEnhet,q.tolerans,q,0,q.svarFormat)}})''',cases)
 assert all(x['want']==x['actual'] for x in results),[x for x in results if x['want']!=x['actual']]
 # Rendera varje verkligt kort i mobil- och datorbredd, utan att spara elevförsök.
 ids=student.evaluate("BANKMA2.filter(q=>q.omr==='geometri_problemlosning').map(q=>q.id)")
 render=[]
 for width in [390,1174]:
  student.set_viewport_size({'width':width,'height':1000})
  for id in ids:
   student.evaluate('''id=>{state.currentTask=expandGameTask(BANKMA2.find(q=>q.id===id))[0];state.answered=false;state.solutionShown=false;state.partResults=[];state.partIndex=0;renderTraining();showSolution();}''',id)
   student.evaluate('document.fonts.ready');student.wait_for_timeout(60)
   check=student.evaluate('''()=>({overflow:document.documentElement.scrollWidth>innerWidth,errors:document.querySelectorAll('.katex-error').length,numbered:document.querySelectorAll('.facit-steglista').length,inputs:document.querySelectorAll('input[id^=ans-]').length,wide:[...document.querySelectorAll('.sol .katex-display')].filter(e=>e.scrollWidth>e.clientWidth+2).map(e=>e.querySelector('annotation').textContent)})''')
   assert not check['overflow'] and not check['errors'] and not check['wide'] and not check['numbered'] and check['inputs']==1,(id,width,check)
   student.evaluate('document.activeElement.blur();window.scrollTo(0,0)');student.screenshot(path=f'/tmp/ma2-mixed-{id}-{width}.png',full_page=True)
   render.append({'id':id,'width':width,**check})
 teacher=browser.new_page();teacher.route('https://cdn.jsdelivr.net/**',cdn);teacher.route('https://fonts.googleapis.com/**',lambda r:r.fulfill(status=200,content_type='text/css',body=''));teacher.route('https://*.supabase.co/**',lambda r:r.abort())
 teacher.goto('http://127.0.0.1:8071/index.html?kurs=ma2');teacher.wait_for_function('window.BANKMA2 && typeof renderMathInElement==="function"')
 visible=teacher.evaluate('''()=>{state.spår='2c';byggTräd();const b=document.querySelector('[data-omr="3:geometri_problemlosning"]');return {text:b?.textContent,ids:BANKMA2.filter(q=>q.omr==='geometri_problemlosning').map(q=>q.id)};}''')
 assert 'Problemlösning' in visible['text'] and '15' in visible['text'] and visible['ids']==ids,visible
 # Separat figuröversikt för manuell visuell granskning.
 teacher.evaluate('''()=>{document.body.classList.remove('password-locked');document.body.innerHTML='<main style="display:grid;grid-template-columns:repeat(3,460px);gap:10px;background:#fff">'+BANKMA2.filter(q=>q.omr==='geometri_problemlosning').map(q=>'<div style="color:#123;padding:5px"><b>'+q.id+'</b>'+q.t.match(/<svg[\\s\\S]*?<\\/svg>/)[0]+'</div>').join('')+'</main>';}''')
 teacher.set_viewport_size({'width':1440,'height':1800});teacher.screenshot(path='/tmp/ma2-mixed-figures.png',full_page=True)
 print(json.dumps({'gradingChecks':len(results),'tracks':tracks,'renderedCards':len(render),'teacherArea':visible['text'],'failures':[]}))
 browser.close()
