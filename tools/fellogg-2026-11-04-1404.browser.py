import json,re,base64,argparse,subprocess
from pathlib import Path
from playwright.sync_api import sync_playwright
parser=argparse.ArgumentParser();parser.add_argument('--deps',type=Path,default=Path('/tmp/fy1-render-deps'));parser.add_argument('--consumer',type=Path);args=parser.parse_args()
root=Path(__file__).resolve().parents[1];deps=args.deps
qs=json.loads((root/'uppgifter.js').read_text().removeprefix('window.BANK = ').strip().removesuffix(';'))
qs=[q for q in qs if q['id'] in ['3.73','3.88','3.93']]
# Use the actual renderer shared by the teacher view and export preparation.
ma=json.loads(subprocess.check_output(['node','-e',r"""
const fs=require('fs'),vm=require('vm'),c={window:{}};
vm.runInNewContext(fs.readFileSync('uppgifterma1.js','utf8'),c);
const s=fs.readFileSync('index.html','utf8');
for(const n of ['altVisas','uppgiftsText']){let i=s.indexOf('function '+n+'(');vm.runInNewContext(s.slice(i,s.indexOf('\n}',i)+2),c)}
c.altBokstav=i=>String.fromCharCode(65+i);
const q=c.window.BANKMA1.find(q=>q.id==='0.879');console.log(JSON.stringify({t:c.uppgiftsText(q),s:q.s}));
"""],cwd=root))
kcss=(deps/'package/dist/katex.min.css').read_text()
kcss=re.sub(r'url\((fonts/[^)]+)\)',lambda m:'url(data:font/woff2;base64,'+base64.b64encode((deps/'package/dist'/m[1]).read_bytes()).decode()+')',kcss)
with sync_playwright() as pw:
 b=pw.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox']);page=b.new_page()
 results=[]
 for approot in [root]+([args.consumer] if args.consumer else []):
  app=approot.name
  css='\n'.join(re.findall(r'<style[^>]*>([\s\S]*?)</style>',(approot/'index.html').read_text()))
  for mode,width in [('screen',390),('screen',1000),('print',794)]:
   page.set_viewport_size({'width':width,'height':1200});page.emulate_media(media=mode)
   page.set_content('<!doctype html><meta charset=utf-8><style>'+css+'\n'+kcss+'\nhtml,body{height:auto!important;overflow:visible!important}body{display:block;padding:16px;background:white;color:#172e43}#review{display:block;width:100%;max-width:720px;margin:auto}.facit{display:block!important} </style><main id=review></main>')
   page.add_script_tag(path=str(deps/'katex.min.js'));page.add_script_tag(path=str(deps/'auto-render.min.js'))
   for q in qs+[{'id':'ma1-0.879',**ma}]:
    for index,card in enumerate([q]+q.get('spelDelar',[])):
     html=card['t']+'<hr><div class="facit öppen">'+card['s']+'</div>'
     page.evaluate('(s)=>{let e=document.querySelector("#review");e.innerHTML=s;renderMathInElement(e,{throwOnError:false,strict:"ignore"})}',html)
     dims=page.evaluate('''()=>({katex:document.querySelectorAll('.katex').length,errors:document.querySelectorAll('.katex-error').length,overflow:document.documentElement.scrollWidth>innerWidth+3,figures:[...document.querySelectorAll('svg')].filter(e=>!e.closest('.katex')).map(e=>({width:e.getBoundingClientRect().width,height:e.getBoundingClientRect().height})),alts:document.querySelectorAll('.ul-alt').length})''')
     assert dims['katex']>0
     assert not dims['errors'],(q['id'],index,dims)
     assert not dims['overflow'],(q['id'],index,dims)
     assert all(x['width']>100 and x['height']>40 for x in dims['figures'])
     if q['id']=='ma1-0.879':assert dims['alts']==4
     results.append([app,mode,width,q['id'],index,dims])
     if index==0 and app=='Uppgiftslabbet' and (width==390 or mode=='print'):
      page.set_viewport_size({'width':width,'height':max(1200,page.evaluate('document.documentElement.scrollHeight'))});page.wait_for_timeout(200)
      page.screenshot(path=f'/tmp/final-{q["id"]}-{mode}-{width}.png',full_page=True)
   if app=='Uppgiftslabbet' and mode=='screen' and width==1000:
    html='<style>.figcard{padding:15px;border:1px solid #ccc;margin-bottom:15px}</style>'
    for q in qs:
     for i,c in enumerate([q]+q.get('spelDelar',[])):
      html+=f'<section class=figcard><h2>{q["id"]} {"huvud" if i==0 else chr(96+i)}</h2>'+''.join(re.findall(r'<svg[\s\S]*?</svg>',c['t']))+'</section>'
    page.evaluate('s=>document.querySelector("#review").innerHTML=s',html)
    page.set_viewport_size({'width':1000,'height':page.evaluate('document.documentElement.scrollHeight')});page.wait_for_timeout(500)
    page.screenshot(path='/tmp/all-flight-diagrams.png',full_page=True)
 Path('/tmp/flight-browser-results.json').write_text(json.dumps(results))
 print('Verified',len(results),'renders: mobile, desktop and print, both app styles; no overflow or KaTeX errors. Ma1: four alternatives.')
 b.close()
