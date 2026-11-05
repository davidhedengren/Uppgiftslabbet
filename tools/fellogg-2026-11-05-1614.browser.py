"""Lokal testserver på 8312; KaTeX-filer i REVIEW_KATEX (dist-katalog)."""
import os
from pathlib import Path
from playwright.sync_api import sync_playwright

ids={'ma1':['0.06','0.305','0.306','0.401','0.402','0.782','0.941'],
     'ma2':['4.245','4.2082','4.2084','4.2143']}
deps=Path(os.environ.get('REVIEW_KATEX','/tmp/fy1-render-deps/package/dist'))
with sync_playwright() as pw:
    browser=pw.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox'])
    page=browser.new_page()
    page.route('https://*.supabase.co/**',lambda r:r.abort())
    page.route('https://fonts.googleapis.com/**',lambda r:r.fulfill(body=''))
    page.route('https://cdn.jsdelivr.net/npm/katex@*/dist/**',lambda r:r.fulfill(path=str(deps/r.request.url.split('/dist/')[1])))
    page.goto(os.environ.get('REVIEW_URL','http://127.0.0.1:8312'))
    page.wait_for_function("typeof väljKurs==='function' && typeof renderMathInElement==='function'")
    page.evaluate("()=>{document.body.classList.remove('password-locked');document.getElementById('passwordGate').hidden=true}")
    for course,course_ids in ids.items():
        assert page.evaluate("id=>väljKurs(KURSER.find(k=>k.id===id),document.querySelector('[data-kurs=\"'+id+'\"]'))",course)
        for width in [390,1280]:
            page.set_viewport_size({'width':width,'height':950})
            for id in course_ids:
                expected=page.evaluate("""({id,course})=>{
                    state.spår=course==='ma1'?'1a':'2c';byggTräd();
                    const q=variantBank().find(q=>q.id===id);state.omr=new Set([q.kap+':'+q.omr]);
                    const pos=urval().findIndex(q=>q.id===id);if(pos<0)throw Error('Uppgift saknas');
                    rita(Math.floor(pos/UPPGIFTER_PER_SIDA));return q.alternativ.length;
                }""",{'id':id,'course':course})
                card=page.locator(f'article.kort[data-id="{id}"]');card.scroll_into_view_if_needed()
                assert card.locator('.ul-alt').count()==expected,(course,id)
                card.locator('.facitknapp').click()
                page.wait_for_timeout(80)
                assert card.locator('.katex-error').count()==0,(course,id)
                if id!='0.06':assert card.locator('.katex').count()>0,(course,id,'KaTeX saknas')
                assert card.locator('.facit-steglista').count()>0
                overflow=card.evaluate("el=>[...el.querySelectorAll('.facit-matte,.ul-alt')].filter(e=>e.scrollWidth>e.clientWidth+3).length")
                assert overflow==0,(course,id,width,'överflöde')
                if id in ['0.305','0.306','4.2143']:
                    card.screenshot(path=f'/tmp/fellogg-1614-{course}-{id}-{width}.png')
    # Skriv ut det gemensamma exportunderlaget till en lokal PDF för kontroll.
    page.set_viewport_size({'width':900,'height':1000})
    page.evaluate("""()=>{
        const q=variantBank().find(x=>x.id==='4.2143');
        document.body.innerHTML='<main style="padding:20px;background:white;color:black">'+uppgiftsText(q)+q.s+altFacit(q)+'</main>';
        renderMathInElement(document.body,{throwOnError:true});
    }""")
    assert page.locator('.ul-alt').count()==4
    page.pdf(path='/tmp/fellogg-1614-export.pdf',format='A4',print_background=True)
    browser.close()
print('11 uppgifter: synliga alternativ och facit i lärarvyn vid 390/1280 px; exportunderlag med alternativ verifierat.')
