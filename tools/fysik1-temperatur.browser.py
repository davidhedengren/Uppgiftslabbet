"""Pröva verklig självrättning, enheter och fristående kort i Kunskapsgymmet."""
import argparse,json,urllib.request
from playwright.sync_api import sync_playwright
args=argparse.ArgumentParser();args.add_argument('--student-port',type=int,default=8062);args=args.parse_args()
cache={}
def cdn(route):
 url=route.request.url
 if url not in cache:
  with urllib.request.urlopen(url,timeout=30) as r:cache[url]=(r.status,dict(r.headers),r.read())
 status,headers,body=cache[url];route.fulfill(status=status,headers={k:v for k,v in headers.items() if k.lower() not in ['content-encoding','content-length','transfer-encoding']},body=body)
cases=[
 ['2.20d','-273,15 °C',True],['2.20d','-273 °C',True],['2.20d','-273,10 °C',False],['2.20d','-273,20 °C',False],['2.20d','0 °C',False],['2.20d','273 K',False],
 ['6.38a','310 K',True],['6.38a','310,15 K',True],['6.38a','310,10 K',False],['6.362','300 K',True],['6.362','300,15 K',True],['6.362','300,10 K',False],
 ['6.201b','131,3 °C',True],['6.201b','131,4 °C',True],['6.201b','131,5 °C',False],
 ['6.203','-167,3 °C',True],['6.203','-167,1 °C',True],['6.203','-167,2 °C',False],
 ['6.180','1302 K',True],['6.180','1303 K',True],['6.180','1304 K',False],
 ['6.341','2,76 liter',True],['6.341','2,77 liter',True],['6.341','2,78 liter',False],
 ['6.548a','1,36 %',True],['6.548a','1,37 %',True],['6.548a','1,38 %',False],
 ['6.539b','2,10 mm',True],['6.539b','0,00210 m',True],['6.539b','2,10 m',False],
 ['6.42a','30',True],['6.42a','29',False],['6.42b','18',True],['6.42b','17',False],['6.42b','1800',False],
 ['6.73a','12 cm',True],['6.73b','60 %',True],['6.73c','598,8 kg/m³',True],['6.73c','0,5988 g/cm³',True],['6.73c','599 kg/m³',False],
]
with sync_playwright() as p:
 browser=p.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox']);page=browser.new_page();page.route('https://cdn.jsdelivr.net/**',cdn);page.goto(f'http://127.0.0.1:{args.student_port}/index.html?kurs=fy1');page.evaluate("selectCourse('fy1')");page.wait_for_function('window.BANK&&typeof renderMathInElement==="function"');page.evaluate('window.reviewCards=BANK.filter(q=>q.spel!==false).flatMap(expandGameTask)')
 results=page.evaluate('cases=>cases.map(([id,input,want])=>{const q=reviewCards.find(q=>q.id===id);return{id,input,want,actual:delSvarRatt(input,q.rättSvar,q.svarEnhet,q.tolerans,q,0,q.svarFormat)}})',cases)
 failures=[r for r in results if r['actual']!=r['want']];assert not failures,failures
 assert page.evaluate("reviewCards.filter(q=>q.ursprungsId==='6.42').map(q=>q.id)")==['6.42a','6.42b']
 print(json.dumps({'checks':len(results),'failures':failures},ensure_ascii=False));browser.close()
