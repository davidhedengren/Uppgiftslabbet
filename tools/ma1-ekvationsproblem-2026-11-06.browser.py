"""Lokala appvyer, självrättning och facit. Ingen Supabase-trafik eller inloggning."""
import json, mimetypes, os
from pathlib import Path
from urllib.parse import urlparse,unquote
from playwright.sync_api import sync_playwright
ROOT=Path(__file__).resolve().parents[1];KG=ROOT.parent/'kunskapsgymmet'
DEPS=Path(os.environ.get('REVIEW_KATEX','/tmp/fy1-render-deps/package/dist'))
IDS=[f'1.{n}' for n in range(1675,1685)]
VARIANTS={
'1.1675':(['220,5','220.5 liter','220500 ml'],['225','4,5','220,5 kg']),
'1.1676':(['6,4','6.4 L','6400 ml'],['1,6','8','6,4 kg']),
'1.1677':(['6,75','6.75 liter','675 cl'],['2,7','4,5','6,75 kg']),
'1.1678':(['1','1 kg','1000 g'],['2','3','1 liter']),
'1.1679':(['3200','3 200 kr'],['2400','1800','3200 m']),
'1.1680':(['900','900 kr'],['660','720','900 m']),
'1.1681':(['28','28 m','2800 cm'],['12','26','28 kg']),
'1.1682':(['11','11 m','1100 cm'],['2,75','1,25','11 kg']),
'1.1683':(['38,75','38.75 min','2325 s'],['18,75','38,45','38,75 km']),
'1.1684':(['15'],['18','20','36','15,5'])}

def route(r):
    u=urlparse(r.request.url)
    if u.hostname=='cdn.jsdelivr.net' and '/katex@' in u.path and '/dist/' in u.path:
        return r.fulfill(path=str(DEPS/u.path.split('/dist/')[1]))
    if u.hostname in ['ul.test','kg.test']:
        root=ROOT if u.hostname=='ul.test' else KG
        rel=unquote(u.path).lstrip('/') or 'index.html'
        # Testa masterbanken även innan den synkas till konsumenten.
        f=(ROOT if rel=='uppgifterma1.js' else root)/rel
        if f.is_file():return r.fulfill(path=str(f),content_type=mimetypes.guess_type(str(f))[0] or 'application/octet-stream')
        return r.fulfill(status=404,body='')
    return r.abort()

CHECK=r'''el=>({errors:el.querySelectorAll('.katex-error').length,
 wide:[...el.querySelectorAll('.facit-matte,.katex-display')].filter(e=>e.scrollWidth>e.clientWidth+3).map(e=>e.textContent.slice(0,90)),
 svg:[...el.querySelectorAll('svg[role="img"]')].flatMap(s=>{let v=s.viewBox.baseVal;return [...s.querySelectorAll('text')].filter(t=>{let b=t.getBBox();return b.x<v.x||b.y<v.y||b.x+b.width>v.width||b.y+b.height>v.height}).map(t=>t.textContent)})})'''
with sync_playwright() as pw:
    browser=pw.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox'])
    for app in ['ul','kg']:
        page=browser.new_page();page.route('**/*',route);page.goto(f'http://{app}.test/')
        if app=='ul':
            page.wait_for_function("typeof väljKurs==='function' && typeof renderMathInElement==='function'")
            page.evaluate("()=>{document.body.classList.remove('password-locked');document.getElementById('passwordGate').hidden=true}")
            assert page.evaluate("()=>väljKurs(KURSER.find(k=>k.id==='ma1'),document.querySelector('[data-kurs=\"ma1\"]'))")
        else:
            page.wait_for_function("typeof selectCourse==='function' && typeof renderMathInElement==='function'")
            assert page.evaluate("()=>selectCourse('ma1',{record:false,render:false})")
            result=page.evaluate('''variants=>Object.entries(variants).map(([id,[yes,no]])=>{
             const q=state.data.bank.find(q=>q.id===id),f=kvFacit(q);
             for(const [list,want] of [[yes,true],[no,false]])for(const a of list){const got=delSvarRatt(a,q.rättSvar,q.svarEnhet,q.tolerans,q,0,q.svarFormat);if(got!==want)f.push(a+' -> '+got)}
             return {id,fel:f};})''',VARIANTS)
            print('Rättning:',json.dumps(result,ensure_ascii=False),flush=True)
            assert all(not x['fel'] for x in result)
        for width in [390,1280]:
            page.set_viewport_size({'width':width,'height':950})
            for id in IDS:
                if app=='ul':
                    page.evaluate('''id=>{state.spår='1a';byggTräd();const q=variantBank().find(x=>x.id===id);state.omr=new Set([q.kap+':'+q.omr]);const n=urval().findIndex(x=>x.id===id);if(n<0)throw Error(id);rita(Math.floor(n/UPPGIFTER_PER_SIDA));}''',id)
                    card=page.locator(f'article.kort[data-id="{id}"]');card.locator('.facitknapp').click()
                    # Ledtråden hör till gymmets vy; samma lagrade sträng läses där.
                else:
                    page.evaluate('''id=>{state.currentTask=state.data.bank.find(q=>q.id===id);state.answered=false;state.solutionShown=false;state.noXp=true;state.hintVisible=true;state.partResults=[];state.partIndex=0;state.kedja=null;renderTraining();showSolution();}''',id)
                    card=page.locator('article.task');assert page.locator('#ans-0').count()==1
                    assert page.locator('#ans-1').count()==0
                page.wait_for_timeout(60)
                result=card.evaluate(CHECK)
                if any(result.values()):print(app,id,width,result,flush=True)
                card.screenshot(path=f'/tmp/ma1-ekv-{app}-{id}-{width}.png')
                assert not any(result.values()),(app,id,width,result)
        page.close()
    browser.close()
print('10 uppgifter: båda apparna, mobil/dator, facit, ledtrådar och rättning godkända.')
