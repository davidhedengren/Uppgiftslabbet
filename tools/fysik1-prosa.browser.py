import argparse,json,urllib.request
from pathlib import Path
from playwright.sync_api import sync_playwright
args=argparse.ArgumentParser();args.add_argument("--teacher-port",type=int,default=8063);args.add_argument("--student-port",type=int,default=8062);args=args.parse_args()
cache={}
def cdn(route):
 u=route.request.url
 if u not in cache:
  with urllib.request.urlopen(u,timeout=30) as r:cache[u]=(r.status,dict(r.headers),r.read())
 st,h,b=cache[u];route.fulfill(status=st,headers={k:v for k,v in h.items() if k.lower() not in ['content-encoding','content-length','transfer-encoding']},body=b)
with sync_playwright() as p:
 b=p.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox','--disable-dev-shm-usage'],env={'PATH':'/usr/bin:/bin','XDG_CONFIG_HOME':'/tmp/phys-prosa-config','XDG_CACHE_HOME':'/tmp/phys-prosa-cache'})
 results=[]
 for port in [args.teacher_port,args.student_port]:
  page=b.new_page();page.add_init_script("localStorage.setItem('kunskapsgymmet-beta-info','2')");page.route('https://cdn.jsdelivr.net/**',cdn);page.route('https://fonts.googleapis.com/**',lambda r:r.fulfill(status=200,content_type='text/css',body=''));page.goto(f'http://127.0.0.1:{port}/index.html?kurs=fy1')
  if port==args.student_port:page.evaluate("selectCourse('fy1')")
  page.wait_for_function('window.BANK&&typeof renderMathInElement==="function"')
  r=page.evaluate(r'''port=>{
   let formulas=0;const errors=[],issues=[];
   function visit(x,id){if(typeof x==='string'){
     const d=document.createElement('div');d.innerHTML=x;
     renderMathInElement(d,{delimiters:[{left:'\\[',right:'\\]',display:true},{left:'\\(',right:'\\)',display:false}],throwOnError:false,errorCallback:m=>errors.push({id,error:String(m)})});formulas+=d.querySelectorAll('.katex').length;
     if(d.querySelector('.facit-steglista'))issues.push({id,issue:'numbered steps'});
    }else if(Array.isArray(x))x.forEach(v=>visit(v,id));else if(x&&typeof x==='object')for(const[k,v]of Object.entries(x))if(['t','s','fraga','spelDelar','spelIntro','ledtrad','alternativ','txt'].includes(k))visit(v,id);
   }
   // Teacher-only tasks, such as 3.172, must also render correctly.
   BANK.forEach(q=>visit(q,q.id));
   return {port,mainTasks:BANK.length,formulas,errors,issues};
  }''',port);assert not r['errors'] and not r['issues'],r;results.append(r)
  if port==args.teacher_port:
   for width in [1174,390]:
    page.set_viewport_size({'width':width,'height':1000})
    page.evaluate(r'''()=>{const q=BANK.find(q=>q.id==='3.172');document.body.classList.remove('password-locked');document.body.innerHTML='<main style="padding:20px;max-width:1050px;margin:auto"><article class="uppgift"><div class="ut">'+q.t+'</div><div class="facit öppen">'+LOS(q.s)+'</div></article></main>';renderMathInElement(document.body,{delimiters:[{left:'\\[',right:'\\]',display:true},{left:'\\(',right:'\\)',display:false}],throwOnError:false});}''');page.wait_for_timeout(200)
    dom=page.evaluate('''()=>{const p=[...document.querySelectorAll('.ut p')],a=p.find(e=>e.textContent.startsWith('a)')),b=p.find(e=>e.textContent.startsWith('b)'));return {aY:a.getBoundingClientRect().top,bY:b.getBoundingClientRect().top,numbers:document.querySelectorAll('.stegnr,.facit-steglista').length,bodyOverflow:document.documentElement.scrollWidth>innerWidth};}''');assert dom['aY']<dom['bY'] and dom['numbers']==0 and not dom['bodyOverflow'],dom;page.screenshot(path=f'/tmp/fy1-prosa-3.172-{width}.png',full_page=True);results.append({'width':width,**dom})
  else:
   page.evaluate('''()=>{window.prosaCards=BANK.filter(q=>q.spel!==false).flatMap(expandGameTask);}''')
   cases=[['2.291c','21,4 min',True],['2.291c','21 min',False],['2.306a','1.4e-7 s',True],['2.307b','10,4 min',True],['2.307b','3,97 min',False],['2.308b','11400',True],['2.320','55,1 m',True],['2.320','55,6 m',False],['2.299b','5.7 m/s',True],['2.293b','23.2 min',True],['2.304','4.97e3 m/s',True],['2.16','2',False]]
   cases=cases[:-1]
   tests=page.evaluate('''cases=>cases.map(([id,input,want])=>{const q=prosaCards.find(q=>q.id===id);if(!q)return{id,input,want,error:'missing card'};return{id,input,want,actual:delSvarRatt(input,q.rättSvar,q.svarEnhet,q.tolerans,q,0,q.svarFormat)}})''',cases);assert all(t.get('actual')==t['want'] for t in tests),tests;results.append({'checks':tests})
  page.close()
 Path('/tmp/fy1-prosa-render.json').write_text(json.dumps(results,ensure_ascii=False,indent=2));print(json.dumps(results,ensure_ascii=False));b.close()
