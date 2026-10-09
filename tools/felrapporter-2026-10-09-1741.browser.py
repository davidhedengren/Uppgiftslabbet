"""Granska rapporterade svar i faktiska spelkort, inklusive tecken och enheter."""
import json, math, urllib.request
from playwright.sync_api import sync_playwright
cache={}
def cdn(route):
 u=route.request.url
 if u not in cache:
  with urllib.request.urlopen(u,timeout=30) as r:cache[u]=(r.status,dict(r.headers),r.read())
 st,h,b=cache[u];route.fulfill(status=st,headers={k:v for k,v in h.items() if k.lower() not in ['content-encoding','content-length','transfer-encoding']},body=b)
# Oberoende fysikberäkningar; index avser det verkliga delkortet.
models=[('5.397',1,2*1/24,'s','0,0833'),('5.391',0,5.9*8.9/.018,'N','2920'),('5.412',0,.030*175/3,'m/s','1,75'),('5.423',0,12*8/75,'m/s','1,28'),('5.411',0,54*2.5/88,'m/s','1,5'),('6.315',0,30-18,'N','12'),('5.91',1,30000/25,'N','1200'),('5.108',2,12/(.025*9.82),'m','48,88')]
with sync_playwright() as p:
 browser=p.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox']);pg=browser.new_page();pg.add_init_script("localStorage.setItem('kunskapsgymmet-beta-info','2')");pg.route('https://cdn.jsdelivr.net/**',cdn);pg.route('https://fonts.googleapis.com/**',lambda r:r.fulfill(status=200,content_type='text/css',body=''));pg.route('https://*.supabase.co/**',lambda r:r.abort())
 pg.goto('http://127.0.0.1:8072/index.html?kurs=fy1');pg.evaluate("selectCourse('fy1')");pg.wait_for_function('window.BANK && typeof renderMathInElement==="function"')
 cases=[]
 for id,part,value,unit,rounded in models:
  q=pg.evaluate('''([id,part])=>expandGameTask(BANK.find(q=>q.id===id))[part]''',[id,part]);actual=q['rättSvar'][0] if isinstance(q['rättSvar'],list) else q['rättSvar'];assert math.isclose(actual,value,rel_tol=1e-12),(id,actual,value)
  for text in [str(value),rounded,rounded+' '+unit]:cases.append([id,part,0,text,True])
  for text in [str(-value),str(2*value),'0']:cases.append([id,part,0,text,False])
 cases += [['5.391',0,0,'2,92*10^3 N',True],['5.391',0,0,'2,92 kN',True],['5.397',1,0,'83,3 ms',True],['5.397',1,0,'0,0417',False],['5.91',1,0,'-1200N',False],['6.315',0,1,'uppåt',True],['6.315',0,1,'upp',True],['6.315',0,1,'nedåt',False],['6.315',0,1,'ner',False],['5.108',2,0,'49',False]]
 checks=pg.evaluate('''cases=>cases.map(([id,part,i,input,want])=>{const q=expandGameTask(BANK.find(q=>q.id===id))[part],a=Array.isArray(q.rättSvar)?q.rättSvar:[q.rättSvar];return{id,part,input,want,actual:delSvarRatt(input,a[i],metadataForDel(q.svarEnhet,i,a.length),metadataForDel(q.tolerans,i,a.length),q,i,metadataForDel(q.svarFormat,i,a.length))}})''',cases)
 assert all(x['want']==x['actual'] for x in checks),[x for x in checks if x['want']!=x['actual']]
 attempts=pg.evaluate('''models=>{finishAttempt=parts=>{window.__parts=parts;state.answered=true;};const out=[];for(const [id,part,,,rounded] of models){const q=expandGameTask(BANK.find(q=>q.id===id))[part];for(const want of [true,false]){state.currentTask=q;state.answered=false;state.solutionShown=false;state.partResults=[];state.partIndex=0;window.__parts=null;renderTraining();document.querySelector('#ans-0').value=want?rounded:'999999';if(id==='6.315')document.querySelector('#ans-1').value='uppåt';checkAnswer();if(id==='6.315')checkAnswer();out.push({id,want,actual:window.__parts?.every(Boolean)});}}return out;}''',models)
 assert all(x['want']==x['actual'] for x in attempts),attempts
 for width in [390,1174]:
  pg.set_viewport_size({'width':width,'height':1000})
  for id,part,*_ in models:
   pg.evaluate('''([id,part])=>{state.currentTask=expandGameTask(BANK.find(q=>q.id===id))[part];state.answered=false;state.solutionShown=false;state.partResults=[];state.partIndex=0;renderTraining();showSolution();}''',[id,part]);pg.evaluate('document.fonts.ready');pg.wait_for_timeout(100)
   r=pg.evaluate('''()=>({overflow:document.documentElement.scrollWidth>innerWidth,errors:document.querySelectorAll('.katex-error').length,wide:[...document.querySelectorAll('.sol .katex-display')].filter(e=>e.scrollWidth>e.clientWidth+2).map(e=>e.querySelector('annotation').textContent),fields:document.querySelectorAll('input[id^=ans-]').length})''');assert not r['overflow'] and not r['errors'] and not r['wide'] and r['fields']==(2 if id=='6.315' else 1),(id,width,r)
   pg.evaluate('document.activeElement.blur();window.scrollTo(0,0)');pg.screenshot(full_page=True,path=f'/tmp/reported-1741-{id}-{width}.png')
 print(json.dumps({'gradingChecks':len(checks),'uiAttempts':len(attempts),'views':16,'failures':[]}));browser.close()
