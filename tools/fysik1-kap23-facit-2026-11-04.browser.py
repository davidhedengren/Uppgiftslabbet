import json,re,base64,argparse
from pathlib import Path
from playwright.sync_api import sync_playwright
parser=argparse.ArgumentParser()
parser.add_argument('--deps',default='/tmp/fy1-render-deps')
parser.add_argument('--css-from',type=Path)
parser.add_argument('--areas',nargs='+',default=['enheter'])
args=parser.parse_args()
root=Path(__file__).resolve().parents[1]
deps=Path(args.deps)
cssroot=args.css_from or root
bank=json.loads((root/'uppgifter.js').read_text().removeprefix('window.BANK = ').strip().removesuffix(';'))
qs=[q for q in bank if q['omr'] in args.areas]
css='\n'.join(re.findall(r'<style[^>]*>([\s\S]*?)</style>',(cssroot/'index.html').read_text()))
kcss=(deps/'package/dist/katex.min.css').read_text()
def font(m):
 f=(deps/'package/dist')/m[1]
 return 'url(data:font/woff2;base64,'+base64.b64encode(f.read_bytes()).decode()+')'
kcss=re.sub(r'url\((fonts/[^)]+)\)',font,kcss)
with sync_playwright() as pw:
 b=pw.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox'])
 page=b.new_page(viewport={'width':390,'height':1000})
 page.set_content('<!doctype html><meta charset="utf-8"><style>'+css+'\n'+kcss+'\nbody{display:block;overflow:auto;padding:10px} .facit{display:block;width:100%;box-sizing:border-box} </style><main id="review"></main>')
 page.add_script_tag(path=str(deps/'katex.min.js'));page.add_script_tag(path=str(deps/'auto-render.min.js'))
 errors=[];overflow=[];count=0
 for q in qs:
  for id,s in [(q['id'],q['s'])]+[(q['id']+d['etikett'],d['s']) for d in q.get('spelDelar',[])]:
   page.evaluate(r's=>{const el=document.querySelector("#review");el.innerHTML="<div class=\"facit öppen\">"+s+"</div>";renderMathInElement(el,{throwOnError:false,strict:"ignore"});}',s)
   count+=1
   dims=page.evaluate('''()=>({errors:document.querySelectorAll('.katex-error').length,katex:document.querySelectorAll('.katex').length,pageOverflow:document.documentElement.scrollWidth>innerWidth+3,overflow:[...document.querySelectorAll('.facit-matte,.facit-rubrik,.facit-svar')].filter(x=>x.scrollWidth>x.clientWidth+3).map(x=>({cls:x.className,text:x.textContent.slice(0,120),extra:x.scrollWidth-x.clientWidth}))})''')
   if dims['errors'] or (('\\(' in s or '\\[' in s) and not dims['katex']):errors.append(id)
   if dims['overflow'] or dims['pageOverflow']:overflow.append({'id':id,**dims})
   if id in ['2.12b','2.227','2.63','2.5a','2.361','2.46','2.13','2.47','2.354','2.253']:page.screenshot(path='/tmp/fy1-'+id+'.png',full_page=True)
 print(json.dumps({'count':count,'errors':errors,'overflow':overflow},ensure_ascii=False))
 Path('/tmp/fy1-render-result.json').write_text(json.dumps({'count':count,'errors':errors,'overflow':overflow},ensure_ascii=False))
 b.close()

if errors or overflow: raise SystemExit(1)
