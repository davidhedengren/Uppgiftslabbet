"""Startar lokal testserver; KaTeX-filer i REVIEW_KATEX (dist-katalog)."""
import os
from pathlib import Path
from playwright.sync_api import sync_playwright

import runpy, threading
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
ids=runpy.run_path(str(Path(__file__).with_name('saknat-underlag-2026-11-06.py')))['IDS']
ids['fy1'].append('3.32')
server=ThreadingHTTPServer(('127.0.0.1',0),SimpleHTTPRequestHandler)
threading.Thread(target=server.serve_forever,daemon=True).start()
deps=Path(os.environ.get('REVIEW_KATEX','/tmp/fy1-render-deps/package/dist'))
with sync_playwright() as pw:
    browser=pw.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox'])
    page=browser.new_page()
    page.route('https://*.supabase.co/**',lambda r:r.abort())
    page.route('https://fonts.googleapis.com/**',lambda r:r.fulfill(body=''))
    page.route('https://cdn.jsdelivr.net/npm/katex@*/dist/**',lambda r:r.fulfill(path=str(deps/r.request.url.split('/dist/')[1])))
    page.goto('http://127.0.0.1:'+str(server.server_port))
    page.wait_for_function("typeof väljKurs==='function' && typeof renderMathInElement==='function'")
    page.evaluate("()=>{document.body.classList.remove('password-locked');document.getElementById('passwordGate').hidden=true}")
    for course,course_ids in ids.items():
        assert page.evaluate("id=>väljKurs(KURSER.find(k=>k.id===id),document.querySelector('[data-kurs=\"'+id+'\"]'))",course)
        for width in [390,1280]:
            page.set_viewport_size({'width':width,'height':950})
            for id in course_ids:
                print(course,id,width,flush=True)
                expected=page.evaluate("""({id,course})=>{
                    state.spår=course==='ma1'?(id==='6.405'?'1c':'1a'):course==='mato1'?'1c':['ma2','mato2'].includes(course)?'2c':null;byggTräd();
                    const q=variantBank().find(q=>q.id===id);state.omr=new Set([q.kap+':'+q.omr]);
                    const pos=urval().findIndex(q=>q.id===id);if(pos<0)throw Error('Uppgift saknas');
                    rita(Math.floor(pos/UPPGIFTER_PER_SIDA));return q.alternativ?.length||0;
                }""",{'id':id,'course':course})
                card=page.locator(f'article.kort[data-id="{id}"]');card.scroll_into_view_if_needed()
                assert card.locator('.ul-alt').count()==expected,(course,id)
                card.locator('.facitknapp').click()
                page.wait_for_timeout(80)
                assert card.locator('.katex-error').count()==0,(course,id)
                if id not in ['3.328','4.828','4.824','3.521','7.437']:assert card.locator('.katex').count()>0,(course,id,'KaTeX saknas')
                assert card.locator('.facit-steglista').count()>0
                overflow=card.evaluate("el=>[...el.querySelectorAll('.facit-matte,.ul-alt')].filter(e=>e.scrollWidth>e.clientWidth+3).length")
                if overflow:
                    card.screenshot(path='/tmp/saknat-overflow.png')
                    print(card.evaluate("el=>[...el.querySelectorAll('.facit-matte,.ul-alt')].filter(e=>e.scrollWidth>e.clientWidth+3).map(e=>({html:e.innerHTML,w:e.clientWidth,sw:e.scrollWidth}))"),flush=True)
                assert overflow==0,(course,id,width,'överflöde')
                if id in ['3.104','1.1187','2.800','4.513','4.305','3.32']:
                    card.screenshot(path=f'/tmp/saknat-underlag-20261106-{course}-{id}-{width}.png')
    # Skriv ut det gemensamma exportunderlaget till en lokal PDF för kontroll.
    page.set_viewport_size({'width':900,'height':1000})
    page.evaluate("""()=>{
        const q=variantBank().find(x=>x.id==='4.305');
        document.body.innerHTML='<main style="padding:20px;background:white;color:black">'+uppgiftsText(q)+q.s+altFacit(q)+'</main>';
        renderMathInElement(document.body,{throwOnError:true});
    }""")
    assert page.locator('.ul-alt').count()==4
    page.pdf(path='/tmp/saknat-underlag-20261106-export.pdf',format='A4',print_background=True)
    browser.close()
server.shutdown()
print('28 uppgifter: synliga alternativ och facit i lärarvyn vid 390/1280 px; exportunderlag verifierat.')
