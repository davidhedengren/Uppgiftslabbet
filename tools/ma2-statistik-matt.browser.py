"""Real answer entry and mobile/desktop rendering for Ma2 #4.322–4.351.
Serve Kunskapsgymmet on 8083 and Uppgiftslabbet on 8085. No database/XP writes.
"""
import json,urllib.request,statistics,math
from pathlib import Path
from collections import Counter
from playwright.sync_api import sync_playwright
models=json.loads((Path(__file__).parent/'fixtures/ma2-statistik-matt.json').read_text());ids=[m['id'] for m in models]
def pair(v,sample=True):return [statistics.mean(v),statistics.stdev(v) if sample else statistics.pstdev(v)]
def mode(v):
 c=Counter(v);a=sorted(x for x in c if c[x]==max(c.values()));return a[0] if len(a)==1 else a
def iqr(v):
 a=sorted(v);return statistics.median(a[len(a)//2:])-statistics.median(a[:len(a)//2])
def answers(m):
 v=m.get('values');kind=m['type']
 if kind=='basic':return[statistics.mean(v),statistics.median(v),mode(v)]
 if kind=='categorical':return['Blå',13,600/13]
 if kind=='measures':return[statistics.median(v),mode(v),pair(v,m['sample']),iqr(v) if m['quartiles'] else max(v)-min(v)]
 if kind=='comparison':return[pair(m['A']),pair(m['B']),{'4.346':'A','4.348':0,'4.349':2,'4.350':'B'}[m['id']]]
 if kind=='outlier':return[statistics.median(v),mode(v),pair(v),'median']
 if kind=='weighted':return[pair(v),statistics.median(v),mode(v),iqr(v),'nej']
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
 tracks=page.evaluate("ids=>['2a','2b','2c'].map(track=>{state.track=track;const all=ids.flatMap(id=>expandGameTask(BANKMA2.find(q=>q.id===id))),pool=availableTasks();return{track,cards:all.length,missing:all.filter(q=>!pool.some(x=>x.id===q.id)).map(q=>q.id)};})",ids);assert all(t['cards']==111 and not t['missing'] for t in tracks),tracks
 page.evaluate('''()=>{finishAttempt=parts=>{state.answered=true;window.reviewOutcome=parts;};window.reviewCard=(q)=>{state.currentTask=q;state.answered=false;state.solutionShown=false;state.partResults=[];state.partIndex=0;state.altValda=new Set();state.altOrdningId=null;window.reviewOutcome=null;renderTraining();};}''')
 results=[]
 def check(id,part,inputs,want):
  r=page.evaluate('''([id,part,inputs])=>{const q=expandGameTask(BANKMA2.find(q=>q.id===id))[part];reviewCard(q);const fields=document.querySelectorAll('[id^="ans-"]');if(fields.length!==inputs.length)throw Error(id+' fields '+fields.length+'/'+inputs.length);inputs.forEach((text,i)=>{const el=document.getElementById('ans-'+i);if(el.disabled)throw Error(id+' disabled '+i);el.value=text;document.getElementById('kollaknapp').click();});return{id,part,inputs,actual:window.reviewOutcome||state.partResults};}''',[id,part,inputs]);assert r['actual']==want,(r,want);results.append(r)
 for m in models:
  for part,a in enumerate(answers(m)):
   aa=a if isinstance(a,list) else [a];full=[str(x).replace('.',',') for x in aa];check(m['id'],part,full,[True]*len(aa))
   rounded=[str(round(x,1 if m['id']=='4.327' and part==2 else 2)).replace('.',',') if isinstance(x,(int,float)) else x.upper() for x in aa];check(m['id'],part,rounded,[True]*len(aa))
   wrong=[str(x+1).replace('.',',') if isinstance(x,(int,float)) else 'felaktigt svar' for x in aa];check(m['id'],part,wrong,[False]*len(aa))
   if len(aa)==2:
    unordered=m['id'] in ['4.345','4.347'] and part==1
    check(m['id'],part,list(reversed(full)),[unordered]*2)
  if m['type']=='measures' and len(set(m['values']))>1:
   check(m['id'],2,[str(statistics.mean(m['values'])),str(statistics.pstdev(m['values']))],[True,False])
 # Explicit natural units, scalar fractions, zero spread, and near-miss rounding.
 for case in [('4.323',0,['5/6'],[True]),('4.328',2,['4 min','1,79 min'],[True,True]),('4.328',2,['4','1,78'],[True,False]),('4.339',0,['12,6 s'],[True]),('4.343',3,['0,6 mm'],[True]),('4.344',2,['2 kg','0 kg'],[True,True]),('4.345',1,['4','2'],[True,True]),('4.347',1,['30 kr','20 kr'],[True,True])]:check(*case)
 print('Answers checked:',len(results),flush=True)
 views=[];shots={'4.323':0,'4.326':0,'4.328':2,'4.330':3,'4.335':2,'4.338':2,'4.339':2,'4.343':2,'4.344':2,'4.345':1,'4.347':2,'4.350':2,'4.351':3}
 for width in [390,1280]:
  page.set_viewport_size({'width':width,'height':1100})
  for m in models:
   for part in range(len(answers(m))):
    page.evaluate('([id,part])=>{reviewCard(expandGameTask(BANKMA2.find(q=>q.id===id))[part]);showSolution();document.activeElement.blur();}',[m['id'],part]);page.evaluate('document.fonts.ready')
    metrics=page.evaluate('''()=>({katex:document.querySelectorAll('.task .katex-error').length,overflow:document.documentElement.scrollWidth>innerWidth+1,wideTables:[...document.querySelectorAll('.task table')].filter(t=>t.getBoundingClientRect().right>innerWidth+1).length,wideMath:[...document.querySelectorAll('.task .katex-display')].filter(e=>e.scrollWidth>e.clientWidth+2).length,mathNodes:document.querySelectorAll('.task .katex').length})''');assert not any(metrics[k] for k in ['katex','overflow','wideTables','wideMath']),(m['id'],part,width,metrics)
    if isinstance(answers(m)[part],list) and not(m['id'] in ['4.345','4.347'] and part==1):assert metrics['mathNodes']>0
    views.append({'app':'Kunskapsgymmet','id':m['id'],'part':part,'width':width,**metrics})
    if width==390 and shots.get(m['id'])==part:page.locator('.task').screenshot(path=f'/tmp/ma2-more-{m["id"]}-{part}.png')
  print('Student width checked:',width,flush=True)
 teacher=browser.new_page(viewport={'width':1280,'height':1100});configure(teacher,errors);teacher.goto('http://127.0.0.1:8085/index.html?kurs=ma2');teacher.wait_for_function('window.BANKMA2&&typeof renderMathInElement==="function"');teacher.evaluate('''()=>{document.body.classList.remove('password-locked');document.body.innerHTML='<main id="review-main" style="box-sizing:border-box;width:100%;padding:12px;color:#172b3a;background:white"></main>';}''')
 for width in [390,1280]:
  teacher.set_viewport_size({'width':width,'height':1100})
  for id in ids:
   r=teacher.evaluate(r'''id=>{const q=BANKMA2.find(q=>q.id===id);document.getElementById('review-main').innerHTML='<article style="max-width:720px;margin:auto">'+uppgiftsText(q)+q.s+'</article>';renderMathInElement(document.getElementById('review-main'),{delimiters:[{left:'\\[',right:'\\]',display:true},{left:'\\(',right:'\\)',display:false}],throwOnError:false});return{id,katex:document.querySelectorAll('.katex-error').length,overflow:document.documentElement.scrollWidth>innerWidth+1,mathNodes:document.querySelectorAll('.katex').length};}''',id);assert not r['katex'] and not r['overflow'],(id,width,r)
   if id!='4.327':assert r['mathNodes']>0,(id,width,r)
   views.append({'app':'Uppgiftslabbet','width':width,**r})
 teacher.set_viewport_size({'width':1500,'height':1200});teacher.evaluate(r'''ids=>{document.getElementById('review-main').innerHTML='<div style="display:grid;grid-template-columns:repeat(3,480px);gap:10px">'+ids.map(id=>{const q=BANKMA2.find(q=>q.id===id),fig=q.t.match(/<svg[\s\S]*?<\/svg>/)?.[0];return fig?'<section><b>'+id+'</b>'+fig+'</section>':'';}).join('')+'</div>';}''',ids);teacher.screenshot(path='/tmp/ma2-more-figures.png',full_page=True)
 assert not errors,errors
 Path('/tmp/ma2-more-browser.json').write_text(json.dumps({'answers':results,'views':views,'tracks':tracks,'javascriptErrors':errors},ensure_ascii=False,indent=2));print('PASS',len(results),'answer combinations,',len(views),'views');browser.close()
