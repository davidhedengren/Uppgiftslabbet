"""15 nya rörelseuppgifter i båda apparna, med isolerad rättning utan XP eller nätverksskrivningar."""
import argparse
import json
import urllib.request
from pathlib import Path
from playwright.sync_api import sync_playwright

parser=argparse.ArgumentParser()
parser.add_argument('--master-port',type=int,default=8084)
parser.add_argument('--student-port',type=int,default=8083)
args=parser.parse_args()
ids=[f'3.{i}' for i in range(410,425)]
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
 for(const svg of root.querySelectorAll('svg[viewBox="0 0 480 370"]')){
  const texts=[...svg.querySelectorAll('text')].map(t=>({text:t.textContent,b:t.getBBox()}));
  for(const {text,b} of texts)if(b.x<0||b.y<0||b.x+b.width>480||b.y+b.height>370)findings.push({text,error:'outside'});
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
    assert all(id in available for id in ids[:11])
    assert all(id not in available for id in ids[11:])
    student.evaluate('''()=>{
      finishAttempt=parts=>{window.reviewAttempt=parts;state.answered=true;};
      window.setReviewTask=id=>{state.currentTask=BANK.find(t=>t.id===id);state.answered=false;state.solutionShown=false;
        state.partIndex=0;state.partResults=[];state.altValda=new Set();window.reviewAttempt=null;renderTraining();};
    }''')
    cases=[]
    for id,value,unit in [('3.410',2,'m/s'),('3.411',-2,'m/s'),('3.412',0,'m/s'),('3.413',4,'m/s²'),
                          ('3.414',-4,'m/s²'),('3.416',3,'m/s'),('3.417',2,'m/s²'),('3.418',6,'m/s'),('3.419',-2.5,'m/s²')]:
        for value_text,want in [(str(value),True),(str(value).replace('.',',')+' '+unit,True),
                                (str(value+1),False),(str(value)+' kg',False)]:
            cases.append([id,value_text,want])
    cases += [['3.410','7,2 km/h',True],['3.411','2 m/s',False],['3.414','4 m/s²',False],['3.417','7,2 m/s²',False],['3.418','6,00 m/s',True]]
    results=student.evaluate('''rows=>rows.map(([id,input,want])=>{
      setReviewTask(id);document.getElementById('ans-0').value=input;checkAnswer();
      return{id,input,want,actual:window.reviewAttempt?.every(Boolean)};
    })''',cases)
    assert all(r['want']==r.get('actual') for r in results),[r for r in results if r['want']!=r.get('actual')]
    alternatives=student.evaluate('''()=>{
      const out=[];for(const id of ['3.415','3.420']){
        setReviewTask(id);const count=altLista(state.currentTask).length;
        for(let i=0;i<count;i++){setReviewTask(id);const want=altLista(state.currentTask)[i].ratt;
          document.getElementById('alt-'+i).click();document.getElementById('altknapp').click();
          out.push({id,i,want,actual:window.reviewAttempt?.every(Boolean)});
        }
      }return out;
    }''')
    assert all(r['want']==r.get('actual') for r in alternatives),alternatives
    views=[]
    for width in [390,1280]:
        student.set_viewport_size({'width':width,'height':1100})
        for id in ids[:11]:
            student.evaluate('(id)=>{setReviewTask(id);showSolution();}',id)
            result=student.locator('.task').evaluate(geometry)
            assert not result['katexErrors'] and not result['findings'],(id,result)
            assert student.locator('.tbody').evaluate('(e)=>e.scrollWidth<=e.clientWidth+2'),id
            student.evaluate('window.scrollTo(0,0)')
            student.locator('.task').screenshot(path=f'/tmp/momentan-kg-{id}-{width}.png')
            views.append(['kg',id,width])
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
            if id in ['3.415','3.420']:assert card.locator('.ul-alt').count()>=3,id
            card.locator('[data-facit]').click()
            result=card.evaluate(geometry)
            assert not result['katexErrors'] and not result['findings'],(id,result)
            assert card.locator('.kroppen').evaluate('(e)=>e.scrollWidth<=e.clientWidth+2'),id
            card.screenshot(path=f'/tmp/momentan-ul-{id}-{width}.png')
            views.append(['ul',id,width])
    assert not errors,errors
    # Contact sheet of question diagrams at readable resolution for manual inspection.
    sheet=browser.new_page(viewport={'width':1440,'height':1800})
    questions=master.evaluate('(ids)=>ids.map(id=>DB.bank.find(q=>q.id===id))',ids)
    sheet.set_content('<style>body{font:16px Arial;background:#e7ecf3}main{display:grid;grid-template-columns:repeat(3,1fr);gap:12px}article{background:white;padding:12px}p{margin:8px 0}svg{width:100%}</style><main>'+''.join('<article><h3>'+q['id']+'</h3>'+q['t']+'</article>' for q in questions if '<svg' in q['t'])+'</main>')
    sheet.screenshot(path='/tmp/momentan-diagram-oversikt.png',full_page=True)
    report={'numericChecks':len(results),'alternativeChecks':len(alternatives),'views':len(views),'available':ids[:11],
            'labOnly':ids[11:],'javascriptErrors':errors}
    Path('/tmp/fy1-momentan-browser.json').write_text(json.dumps(report,ensure_ascii=False,indent=2))
    print(json.dumps(report,ensure_ascii=False));browser.close()
