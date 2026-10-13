"""Real answer entry and mobile/desktop rendering for Ma2 #4.352–4.375 och elva varierade kvartil-/percentiluppgifter.
Serve Kunskapsgymmet on 8083 and Uppgiftslabbet on 8085. No database/XP writes.
"""
import json,urllib.request
from pathlib import Path
from playwright.sync_api import sync_playwright
models=json.loads((Path(__file__).parent/'fixtures/ma2-statistik-referenser.json').read_text());ids=[m['id'] for m in models]
cache={}
def cdn(route):
 u=route.request.url
 if u not in cache:
  with urllib.request.urlopen(u,timeout=30) as r:cache[u]=(r.status,dict(r.headers),r.read())
 st,h,b=cache[u];route.fulfill(status=st,headers={k:v for k,v in h.items() if k.lower() not in ['content-encoding','content-length','transfer-encoding']},body=b)
def configure(page,errors):
 page.on('pageerror',lambda e:errors.append(str(e)));page.route('https://cdn.jsdelivr.net/**',cdn);page.route('https://fonts.googleapis.com/**',lambda r:r.fulfill(status=200,content_type='text/css',body=''));page.route('https://*.supabase.co/**',lambda r:r.abort())
with sync_playwright() as p:
 browser=p.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox']);page=browser.new_page(viewport={'width':1280,'height':1100});errors=[];configure(page,errors)
 page.add_init_script("localStorage.setItem('kunskapsgymmet-beta-info','2')");page.goto('http://127.0.0.1:8083/index.html');page.evaluate("selectCourse('ma2')");page.wait_for_function('window.BANKMA2&&typeof renderMathInElement==="function"&&typeof nerdamer==="function"')
 tracks=page.evaluate("ids=>['2a','2b','2c'].map(track=>{state.track=track;const all=ids.filter(id=>id!=='4.359').flatMap(id=>expandGameTask(BANKMA2.find(q=>q.id===id))),pool=availableTasks();return{track,manualExcluded:!pool.some(q=>q.id==='4.359'||q.id.startsWith('4.359:')),cards:all.length,missing:all.filter(q=>!pool.some(x=>x.id===q.id)).map(q=>q.id)};})",ids);assert all(t['cards']==60 and not t['missing'] and t['manualExcluded'] for t in tracks),tracks
 page.evaluate('''()=>{finishAttempt=parts=>{state.answered=true;window.reviewOutcome=parts;};window.reviewCard=(q)=>{state.currentTask=q;state.answered=false;state.solutionShown=false;state.partResults=[];state.partIndex=0;state.altValda=new Set();state.altOrdningId=null;window.reviewOutcome=null;renderTraining();};}''')
 results=[]
 def check(id,part,inputs,want):
  r=page.evaluate('''([id,part,inputs])=>{const q=expandGameTask(BANKMA2.find(q=>q.id===id))[part];reviewCard(q);const fields=document.querySelectorAll('[id^="ans-"]');if(fields.length!==inputs.length)throw Error(id+' fields '+fields.length+'/'+inputs.length);inputs.forEach((text,i)=>{const el=document.getElementById('ans-'+i);if(el.disabled)throw Error(id+' disabled '+i);el.value=text;document.getElementById('kollaknapp').click();});return{id,part,inputs,actual:window.reviewOutcome||state.partResults};}''',[id,part,inputs]);assert r['actual']==want,(r,want);results.append(r)
 cards=page.evaluate("ids=>ids.filter(id=>id!=='4.359').flatMap(id=>expandGameTask(BANKMA2.find(q=>q.id===id)).map((q,part)=>({id,part,answer:q.rättSvar,structure:q.svarsstruktur,format:q.svarFormat,alternatives:q.alternativ})))",ids)
 for card in cards:
  id,part=card['id'],card['part']
  if card.get('alternatives'):
   correct=[i for i,x in enumerate(card['alternatives']) if x.get('ratt')];n=len(card['alternatives'])
   for mask in range(1,2**n):
    selected=[i for i in range(n) if mask&(1<<i)]
    r=page.evaluate('''([id,selected])=>{reviewCard(expandGameTask(BANKMA2.find(q=>q.id===id))[0]);selected.forEach(i=>document.getElementById('alt-'+state.altOrdning.indexOf(i)).click());document.getElementById('altknapp').click();return reviewOutcome;}''',[id,selected]);want=max(0,len(set(selected)&set(correct))-len(set(selected)-set(correct)))
    assert sum(r)==want,(id,selected,r,want);results.append({'id':id,'selected':selected,'actual':r})
   continue
  a=card['answer'];aa=a if isinstance(a,list) else [a]
  full=[str(x).replace('.',',') for x in aa];check(id,part,full,[True]*len(aa))
  rounded=[str(round(x,1 if id in ['4.365','4.366'] and part==0 else 2)).replace('.',',') if isinstance(x,(int,float)) else x.upper() for x in aa];check(id,part,rounded,[True]*len(aa))
  wrong=[str(x+100).replace('.',',') if isinstance(x,(int,float)) else 'felaktigt svar' for x in aa];check(id,part,wrong,[False]*len(aa))
  if len(aa)>1:
   want=[True]*len(aa) if card['structure']=='mängd' else [aa[i]==aa[-i-1] for i in range(len(aa))]
   check(id,part,list(reversed(full)),want)
 for case in [('4.360',0,['37/5'],[True]),('4.362',0,['5','4'],[True,True]),('4.365',0,['60,3 kg','8,8 kg'],[True,True]),('4.369',0,['28 år'],[True]),('4.372',2,['22/3'],[True]),('4.352',0,['34000 kr'],[True])]:check(*case)
 print('Answers checked:',len(results),flush=True)
 views=[];shots={'4.356':0,'4.360':0,'4.362':0,'4.364':2,'4.365':0,'4.366':0,'4.374':0,'4.71':1}
 for width in [390,1280]:
  page.set_viewport_size({'width':width,'height':1100})
  for card in cards:
    id,part=card['id'],card['part']
    page.evaluate('([id,part])=>{reviewCard(expandGameTask(BANKMA2.find(q=>q.id===id))[part]);showSolution();document.activeElement.blur();}',[id,part]);page.evaluate('document.fonts.ready')
    metrics=page.evaluate('''()=>({katex:document.querySelectorAll('.task .katex-error').length,overflow:document.documentElement.scrollWidth>innerWidth+1,wideTables:[...document.querySelectorAll('.task table')].filter(t=>t.getBoundingClientRect().right>innerWidth+1).length,wideMath:[...document.querySelectorAll('.task .katex-display')].filter(e=>e.scrollWidth>e.clientWidth+2).length,mathNodes:document.querySelectorAll('.task .katex').length})''');assert not any(metrics[k] for k in ['katex','overflow','wideTables','wideMath']),(id,part,width,metrics)
    views.append({'app':'Kunskapsgymmet','id':id,'part':part,'width':width,**metrics})
    if width==390 and shots.get(id)==part:page.locator('.task').screenshot(path=f'/tmp/ma2-ref-{id}-{part}.png')
  print('Student width checked:',width,flush=True)
 teacher=browser.new_page(viewport={'width':1280,'height':1100});configure(teacher,errors);teacher.goto('http://127.0.0.1:8085/index.html?kurs=ma2');teacher.wait_for_function('window.BANKMA2&&typeof renderMathInElement==="function"');teacher.evaluate('''()=>{document.body.classList.remove('password-locked');document.body.innerHTML='<main id="review-main" style="box-sizing:border-box;width:100%;padding:12px;color:#172b3a;background:white"></main>';}''')
 for width in [390,1280]:
  teacher.set_viewport_size({'width':width,'height':1100})
  for id in ids:
   r=teacher.evaluate(r'''id=>{const q=BANKMA2.find(q=>q.id===id);if(q.alternativ&&!q.alternativ.every(a=>uppgiftsText(q).includes(a.txt)))throw Error(id+' alternatives missing in teacher export');document.getElementById('review-main').innerHTML='<article style="max-width:720px;margin:auto">'+uppgiftsText(q)+q.s+'</article>';renderMathInElement(document.getElementById('review-main'),{delimiters:[{left:'\\[',right:'\\]',display:true},{left:'\\(',right:'\\)',display:false}],throwOnError:false});return{id,katex:document.querySelectorAll('.katex-error').length,overflow:document.documentElement.scrollWidth>innerWidth+1,mathNodes:document.querySelectorAll('.katex').length};}''',id);assert not r['katex'] and not r['overflow'],(id,width,r)
   if id in ['4.364','4.365','4.366','4.371','4.373']:assert r['mathNodes']>0,(id,width,r)
   views.append({'app':'Uppgiftslabbet','width':width,**r})
 teacher.set_viewport_size({'width':1500,'height':1200});teacher.evaluate(r'''ids=>{document.getElementById('review-main').innerHTML='<div style="display:grid;grid-template-columns:repeat(3,480px);gap:10px">'+ids.map(id=>{const q=BANKMA2.find(q=>q.id===id),fig=(q.t+q.s).match(/<svg[\s\S]*?<\/svg>/)?.[0];return fig?'<section><b>'+id+'</b>'+fig+'</section>':'';}).join('')+'</div>';}''',ids);teacher.screenshot(path='/tmp/ma2-ref-figures.png',full_page=True)
 assert not errors,errors
 Path('/tmp/ma2-ref-browser.json').write_text(json.dumps({'answers':results,'views':views,'tracks':tracks,'javascriptErrors':errors},ensure_ascii=False,indent=2));print('PASS',len(results),'answer combinations,',len(views),'views');browser.close()
