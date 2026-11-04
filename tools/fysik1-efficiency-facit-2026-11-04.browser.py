import json,re,base64,argparse
from pathlib import Path
from playwright.sync_api import sync_playwright
parser=argparse.ArgumentParser()
parser.add_argument('--deps',default='/tmp/fy1-render-deps')
parser.add_argument('--css-from',type=Path)
parser.add_argument('--areas',nargs='+',default=['kopplingar'])
args=parser.parse_args()
root=Path(__file__).resolve().parents[1]
deps=Path(args.deps)
cssroot=args.css_from or root
bank=json.loads((root/'uppgifter.js').read_text().removeprefix('window.BANK = ').strip().removesuffix(';'))
qs=[q for q in bank if q['omr']=='kopplingar' and q.get('familj')=='Effekt och verkningsgrad med inre resistans']
css='\n'.join(re.findall(r'<style[^>]*>([\s\S]*?)</style>',(cssroot/'index.html').read_text()))
kcss=(deps/'package/dist/katex.min.css').read_text()
def font(m):
 f=(deps/'package/dist')/m[1]
 return 'url(data:font/woff2;base64,'+base64.b64encode(f.read_bytes()).decode()+')'
kcss=re.sub(r'url\((fonts/[^)]+)\)',font,kcss)
with sync_playwright() as pw:
 b=pw.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox'])
 page=b.new_page(viewport={'width':390,'height':1000})
 page.set_content('<!doctype html><meta charset="utf-8"><style>'+css+'\n'+kcss+'\nhtml,body{height:auto!important;overflow:visible!important}body{display:block;padding:10px}#review{height:auto!important;overflow:visible!important} .facit{display:block;width:100%;box-sizing:border-box} </style><main id="review"></main>')
 page.add_script_tag(path=str(deps/'katex.min.js'));page.add_script_tag(path=str(deps/'auto-render.min.js'))
 errors=[];overflow=[];count=0
 for q in qs:
  for id,s in [(q['id']+str(d.get('etikett','')),d['s']+'<hr>'+d.get('ledtrad','')) for d in [q]+q.get('spelDelar',[])]:
   page.evaluate(r's=>{const el=document.querySelector("#review");el.innerHTML="<div class=\"facit öppen\">"+s+"</div>";renderMathInElement(el,{throwOnError:false,strict:"ignore"});}',s)
   count+=1
   dims=page.evaluate('''()=>({errors:document.querySelectorAll('.katex-error').length,katex:document.querySelectorAll('.katex').length,pageOverflow:document.documentElement.scrollWidth>innerWidth+3,overflow:[...document.querySelectorAll('.facit-matte,.facit-rubrik,.facit-svar')].filter(x=>x.scrollWidth>x.clientWidth+3).map(x=>({cls:x.className,text:x.textContent.slice(0,120),tex:x.querySelector('annotation')?.textContent,extra:x.scrollWidth-x.clientWidth}))})''')
   if dims['errors'] or (('\\(' in s or '\\[' in s) and not dims['katex']):errors.append(id)
   if dims['overflow'] or dims['pageOverflow']:overflow.append({'id':id,**dims})
   if id in ['8.45','8.237','8.243','8.729','8.731','8.732','8.735','8.736']:
    page.evaluate('scrollTo(0,0)');page.wait_for_timeout(800);page.screenshot(path='/tmp/efficiency-'+id+'.png',full_page=True)
 print(json.dumps({'count':count,'errors':errors,'overflow':overflow},ensure_ascii=False))
 Path('/tmp/fy1-render-result.json').write_text(json.dumps({'count':count,'errors':errors,'overflow':overflow},ensure_ascii=False))
 # Review all question diagrams on independent, readable sheets.
 page.set_viewport_size({'width':1280,'height':1000})
 qs=[q for q in qs if '<svg' in q['t']]
 for start in range(0,len(qs),6):
  html='<style>.sheet{display:grid;grid-template-columns:1fr 1fr;gap:18px}.tile{background:white;color:#111;padding:15px;border:1px solid #888}.tile svg{width:100%;height:auto;max-height:400px}.tile .fig{display:block}</style><div class="sheet">'+''.join('<section class="tile"><h2>'+q['id']+'</h2>'+q['t']+'</section>' for q in qs[start:start+6])+'</div>'
  page.evaluate(r's=>{document.querySelector("#review").innerHTML=s;renderMathInElement(document.querySelector("#review"),{throwOnError:false});}',html)
  page.evaluate('scrollTo(0,0)');page.wait_for_timeout(800)
  page.set_viewport_size({'width':1280,'height':max(1000,page.evaluate('document.documentElement.scrollHeight'))})
  page.wait_for_timeout(300)
  page.screenshot(path='/tmp/efficiency-questions-'+str(start//6+1)+'.png',full_page=True)
 b.close()

if errors or overflow: raise SystemExit(1)
