"""Egna tangenter: 15 läraruppgifter, isolerad visning och kontroll av spelfilter."""
import argparse
import json
import urllib.request
from pathlib import Path
from playwright.sync_api import sync_playwright

parser=argparse.ArgumentParser()
parser.add_argument('--master-port',type=int,default=8085)
parser.add_argument('--student-port',type=int,default=8083)
args=parser.parse_args()
ids=[f'3.{i}' for i in range(425,440)]
cache={}
def cdn(route):
    url=route.request.url
    if url not in cache:
        with urllib.request.urlopen(url,timeout=30) as r:cache[url]=(r.status,dict(r.headers),r.read())
    status,headers,body=cache[url]
    route.fulfill(status=status,headers={k:v for k,v in headers.items() if k.lower() not in ['content-encoding','content-length','transfer-encoding']},body=body)

def setup(page):
    page.route('https://cdn.jsdelivr.net/**',cdn)
    page.route('https://fonts.googleapis.com/**',lambda r:r.fulfill(status=200,content_type='text/css',body=''))
    page.route('https://*.supabase.co/**',lambda r:r.abort())

geometry=r'''root=>{
 const findings=[];
 for(const svg of root.querySelectorAll('svg[viewBox="0 0 600 432"]')){
  const texts=[...svg.querySelectorAll('text')].map(t=>({text:t.textContent,b:t.getBBox()}));
  for(const {text,b} of texts)if(b.x<0||b.y<0||b.x+b.width>600||b.y+b.height>432)findings.push({text,error:'outside'});
  for(let i=0;i<texts.length;i++)for(let j=i+1;j<texts.length;j++){
   const a=texts[i].b,b=texts[j].b;
   if(a.x<b.x+b.width&&a.x+a.width>b.x&&a.y<b.y+b.height&&a.y+a.height>b.y)findings.push({text:texts[i].text+' / '+texts[j].text,error:'overlap'});
  }
 }
 return {katexErrors:root.querySelectorAll('.katex-error').length,findings};
}'''

with sync_playwright() as p:
    browser=p.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox'])
    student=browser.new_page(viewport={'width':1280,'height':1000})
    setup(student);errors=[]
    student.on('pageerror',lambda e:errors.append(str(e)))
    student.add_init_script("localStorage.setItem('kunskapsgymmet-beta-info','2')")
    student.goto(f'http://127.0.0.1:{args.student_port}/index.html?kurs=fy1')
    student.evaluate("selectCourse('fy1')")
    student.wait_for_function('window.BANK && typeof window.nerdamer==="function"')
    available=student.evaluate('availableTasks().map(t=>t.id)')
    assert all(id not in available for id in ids)
    views=[]
    master=browser.new_page(viewport={'width':1280,'height':1100});setup(master)
    master.on('pageerror',lambda e:errors.append(str(e)))
    master.goto(f'http://127.0.0.1:{args.master_port}/index.html')
    master.wait_for_function('typeof sparSakerstallKurs==="function" && typeof renderMathInElement==="function"')
    master.evaluate('''async()=>{
      await UL_KLAR;
      ulRpc=async name=>name==='ul_min_behorighet'?{larare:true,admin:false}:null;
      ulHämtaBehörighet=async()=>({larare:true,admin:false});
      ulSession={access_token:'test-only',user:{id:'test-only'}};grindÖppna('konto');
      await sparSakerstallKurs('fy1');

    }''')
    for width in [390,1280]:
        master.set_viewport_size({'width':width,'height':1100})
        for id in ids:
            master.evaluate('(id)=>{state.sök=id;state.omr.clear();rita();}',id)
            card=master.locator(f'article.kort[data-id="{id}"]')
            assert card.count()==1,id
            assert card.is_visible(),id
            card.locator('[data-facit]').click()
            result=card.evaluate(geometry)
            assert not result['katexErrors'] and not result['findings'],(id,result)
            assert card.locator('.kroppen').evaluate('(e)=>e.scrollWidth<=e.clientWidth+2'),id
            card.screenshot(path=f'/tmp/egna-tangenter-ul-{id}-{width}.png')
            views.append(['ul',id,width])
    assert not errors,errors
    # Contact sheet of question diagrams at readable resolution for manual inspection.
    sheet=browser.new_page(viewport={'width':1440,'height':1800})
    questions=master.evaluate('(ids)=>ids.map(id=>DB.bank.find(q=>q.id===id))',ids)
    for start in range(0,15,5):
        group=questions[start:start+5]
        for field in ['t','s']:
            import re
            sheet.set_content('<style>body{font:16px Arial;background:#e7ecf3}main{display:grid;grid-template-columns:repeat(2,1fr);gap:12px}article{background:white;padding:12px}svg{width:100%}</style><main>'+''.join('<article><h3>'+q['id']+'</h3>'+''.join(re.findall(r'<svg[\s\S]*?</svg>',q[field]))+'</article>' for q in group)+'</main>')
            sheet.screenshot(path=f'/tmp/egna-tangenter-{field}-{start}.png',full_page=True)
    report={'views':len(views),'labOnly':ids,'javascriptErrors':errors}
    Path('/tmp/fy1-egna-tangenter-browser.json').write_text(json.dumps(report,ensure_ascii=False,indent=2))
    print(json.dumps(report,ensure_ascii=False));browser.close()
