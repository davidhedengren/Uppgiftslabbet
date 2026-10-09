"""Kontrollera tidigare felrapporter i den faktiska elevvyn och graderingen."""
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
 b=p.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox']);pg=b.new_page();pg.add_init_script("localStorage.setItem('kunskapsgymmet-beta-info','2')");pg.route('https://cdn.jsdelivr.net/**',cdn);pg.route('https://fonts.googleapis.com/**',lambda r:r.fulfill(status=200,content_type='text/css',body=''));pg.route('https://*.supabase.co/**',lambda r:r.abort())
 result=[]
 for course,key,ids in [('ma1','BANKMA1',['0.1047','4.514']),('fy2','BANK2',['1.84'])]:
  pg.goto('http://127.0.0.1:8072/index.html?kurs='+course);pg.evaluate('c=>selectCourse(c)',course);pg.wait_for_function('key=>window[key]&&typeof renderMathInElement==="function"',arg=key)
  checks=[]
  if course=='ma1':
   checks=[['0.1047','0,707',True,0],['0.1047','0.707',True,0],['0.1047','0.7070',True,0],['0.1047','0.77',False,0],['0.1047','0.7',False,0],['0.1047','0.07',False,0],['4.514','6',True,0],['4.514','12',True,1],['4.514','-6',False,0],['4.514','12',False,0],['4.514','6',False,1],['4.514','-12',False,1]]
  else:checks=[['1.84','36,2',True,0],['1.84','36.2°',True,0],['1.84','36.24877850747886',True,0],['1.84','36.25',True,0],['1.84','36.3',True,0],['1.84','36.4',False,0],['1.84','36',False,0],['1.84','0.7332',False,0],['1.84','-36.2',False,0]]
  r=pg.evaluate('''([key,checks])=>checks.map(([id,input,want,i])=>{const q=window[key].find(q=>q.id===id),a=Array.isArray(q.rättSvar)?q.rättSvar:[q.rättSvar];return{id,input,want,actual:delSvarRatt(input,a[i],metadataForDel(q.svarEnhet,i,a.length),metadataForDel(q.tolerans,i,a.length),q,i,metadataForDel(q.svarFormat,i,a.length))}})''',[key,checks]);assert all(x['want']==x['actual'] for x in r),r;result+=r
  for width in [390,1174]:
   pg.set_viewport_size({'width':width,'height':1000})
   for id in ids:
    pg.evaluate('''([key,id])=>{state.currentTask=expandGameTask(window[key].find(q=>q.id===id))[0];state.answered=false;state.solutionShown=false;state.partResults=[];state.partIndex=0;renderTraining();showSolution();}''',[key,id]);pg.evaluate('document.fonts.ready');pg.wait_for_timeout(150)
    r=pg.evaluate('''()=>({overflow:document.documentElement.scrollWidth>innerWidth,errors:document.querySelectorAll('.katex-error').length,wide:[...document.querySelectorAll('.sol .katex-display')].filter(e=>e.scrollWidth>e.clientWidth+2).map(e=>e.querySelector('annotation').textContent),fields:document.querySelectorAll('input[id^=ans-]').length})''');assert not r['overflow'] and not r['errors'] and not r['wide'] and r['fields']==(2 if id=='4.514' else 1),(id,width,r)
    pg.evaluate('document.activeElement.blur();window.scrollTo(0,0)');pg.screenshot(full_page=True,path=f'/tmp/reported-{id}-{width}.png')
 print(json.dumps({'checks':len(result),'failures':[]}));b.close()
