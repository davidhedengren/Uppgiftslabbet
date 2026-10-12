"""Mottagna dokument, accepterade/avböjda inbjudningar och riktig öppning med isolerade RPC-fixturer."""
import argparse
import json
import urllib.request
from playwright.sync_api import sync_playwright

parser = argparse.ArgumentParser()
parser.add_argument('--port', type=int, default=8084)
args = parser.parse_args()
cache = {}


def cdn(route):
    url = route.request.url
    if url not in cache:
        with urllib.request.urlopen(url, timeout=30) as r:
            cache[url] = (r.status, dict(r.headers), r.read())
    status, headers, body = cache[url]
    route.fulfill(status=status, headers={k: v for k, v in headers.items()
                  if k.lower() not in ['content-encoding', 'content-length', 'transfer-encoding']}, body=body)


with sync_playwright() as p:
    browser = p.chromium.launch(executable_path='/usr/bin/chromium', args=['--no-sandbox'])
    page = browser.new_page(viewport={'width': 1280, 'height': 1000})
    errors, dialogs = [], []
    page.on('pageerror', lambda e: errors.append(str(e)))
    page.on('dialog', lambda d: (dialogs.append(d.message), d.accept()))
    page.route('https://cdn.jsdelivr.net/**', cdn)
    page.route('https://*.supabase.co/**', lambda r: r.abort())
    page.route('https://fonts.googleapis.com/**', lambda r: r.fulfill(status=200, content_type='text/css', body=''))
    page.goto(f'http://127.0.0.1:{args.port}/index.html')
    page.wait_for_function('typeof minaÖppna==="function" && typeof renderMathInElement==="function"')
    page.evaluate('''async()=>{
      const owned={id:'owned',namn:'Mitt eget prov',kurs:'ma2',spar:'2c',typ:'prov',roll:'agare',medlemmar:1,antal_uppgifter:1,uppdaterad:'2026-10-12T08:00:00Z'};
      const received={...owned,id:'received',namn:'Mottaget geometriprov',roll:'medlem',agare:'Testkollega',medlemmar:2,omraden:['Likformighet']};
      const exercise={...received,id:'exercise',typ:'ovning',namn:'Mottaget övningsblad'};
      const otherTrack={...owned,id:'other-track',namn:'Algebra 2b',spar:'2b',uppdaterad:'2026-10-11T08:00:00Z'};
      const physics={...owned,id:'physics',namn:'Arbete och energi',kurs:'fy1',spar:null,uppdaterad:'2026-10-13T08:00:00Z'};
      const newlyAccepted={...received,id:'accepted',namn:'Nytt delat prov'};
      const invitation=(id,name)=>({id,namn:name,kurs:'ma2',fran_namn:'Testkollega',antal_uppgifter:1,skapad:'2026-10-12T08:00:00Z'});
      window.sharedFixture={accepted:false,declined:false,calls:[],owned,received,exercise,newlyAccepted};
      ulRpc=async(name,args={})=>{
        const f=window.sharedFixture;f.calls.push({name,args});
        if(name==='ul_min_behorighet')return{larare:true,admin:false};
        if(name==='ul_mina')return[owned,received,exercise,otherTrack,physics,...(f.accepted?[newlyAccepted]:[])];
        if(name==='ul_mina_delninginbjudningar')return[
          ...(f.accepted?[]:[invitation('invite-accept','Nytt delat prov')]),
          ...(f.declined?[]:[invitation('invite-decline','Prov att avböja')]),invitation('invite-fail','Förfrågan med tillfälligt fel')];
        if(name==='ul_skolbank')return{skola:'Testskola',dokument:[{...owned,id:'published',namn:'Publicerad skolmall',egen:false,agare:'Testkollega'}]};
        if(name==='ul_svara_delninginbjudan'){
          if(args.p_inbjudan==='invite-fail')throw new Error('Tillfälligt testfel');
          if(args.p_inbjudan==='invite-accept')f.accepted=args.p_acceptera;
          if(args.p_inbjudan==='invite-decline')f.declined=!args.p_acceptera;
          return{ok:true};
        }
        if(name==='ul_hamta'){
          if(![received.id,exercise.id,...(f.accepted?[newlyAccepted.id]:[])].includes(args.p_id))throw new Error('Ej medlem');
          return{...([received,exercise,newlyAccepted].find(d=>d.id===args.p_id)),revision:1,data:f.data};
        }
        if(name==='ul_hamta_utkast')return null;
        if(name==='ul_spara_utkast')return{ok:true};
        throw new Error('Oväntad RPC i testet: '+name);
      };
      ulSession={access_token:'test-only',user:{id:'test-recipient',user_metadata:{full_name:'Testmottagare'}}};
      ulBehörighet={larare:true,admin:false};ulBehörighetTid=Date.now();grindÖppna('konto');
      await sparSakerstallKurs('ma2');
      const q=DB.bank.find(q=>q.id==='3.17');
      window.sharedFixture.data={version:1,kind:'prov',course:'ma2',track:'2c',settings:{documentType:'prov'},tasks:[{bankId:q.id,order:0,snapshot:sparSnapshotUppgift(q)}]};
      await minaÖppna();
    }''')
    assert page.locator('[data-mina-oppna="owned"]').is_visible()
    assert page.locator('[data-mina-oppna="received"]').is_visible()
    assert page.locator('[data-mina-oppna="exercise"]').is_visible()
    received_row = page.locator('.mina-post').filter(has=page.locator('[data-mina-oppna="received"]'))
    assert 'Delat av Testkollega' in received_row.inner_text()
    assert received_row.locator('[data-mina-radera]').inner_text() == 'Lämna'
    assert received_row.locator('[data-mina-skolbank]').count() == 0
    for term in ['geometri', 'likformighet']:
        page.locator('#minaSok').fill(term)
        assert page.locator('[data-mina-oppna="received"]').is_visible()
    page.locator('#minaSok').fill('')

    # Verkliga filter/sorteringskontroller med olika kurser och spår.
    page.locator('#minaKurs').select_option(json.dumps(['ma2', None], separators=(',', ':')))
    assert page.locator('[data-mina-oppna="other-track"]').is_visible()
    assert page.locator('[data-mina-oppna="physics"]').count() == 0
    page.locator('#minaKurs').select_option(json.dumps(['ma2', '2c'], separators=(',', ':')))
    assert page.locator('[data-mina-oppna="other-track"]').count() == 0
    page.locator('#minaSok').fill('ma2c likformighet testkollega')
    assert page.locator('[data-mina-oppna="received"]').is_visible()
    assert page.locator('#minaTraffar').inner_text() == 'Visar 2 av 5 dokument'
    page.locator('#minaSok').fill('saknas')
    assert 'Inga träffar' in page.locator('#minaInnehall').inner_text()
    page.locator('#minaSok').fill('')
    page.locator('#minaKurs').select_option('')
    page.locator('#minaSortering').select_option('senast')
    def prov_ids():
        return page.locator('.mina-kolumn[aria-label="Prov"] [data-mina-oppna]').evaluate_all('(nodes)=>nodes.map(n=>n.dataset.minaOppna)')
    assert prov_ids()[0] == 'physics'
    page.locator('#minaSortering').select_option('namn')
    assert prov_ids() == ['other-track', 'physics', 'owned', 'received']
    page.locator('#minaSortering').select_option('kurs')
    assert prov_ids() == ['physics', 'other-track', 'owned', 'received']
    page.evaluate('async()=>await minaHämta()')
    assert page.locator('#minaSortering').input_value() == 'kurs'

    # Acceptera via den riktiga knappen: byt till Mina prov, uppdatera och visa dokumentet.
    page.evaluate("async()=>await minaÖppna({lage:'inbjudningar'})")
    page.locator('[data-mina-inbjudan-svar="invite-accept"][data-svar="ja"]').click()
    page.wait_for_function("MINA.lage==='mina' && document.querySelector('[data-mina-oppna=accepted]')")
    assert page.locator('#minamodalTitel').inner_text() == 'Mina prov och övningsblad'
    assert page.locator('[data-mina-oppna="accepted"]').is_visible()
    assert page.locator('#minaKurs').input_value() == ''
    assert page.locator('#minaSok').input_value() == ''
    page.evaluate('async()=>await minaHämta()')
    assert page.locator('[data-mina-oppna="accepted"]').is_visible()

    page.evaluate("async()=>await minaÖppna({lage:'inbjudningar'})")
    page.locator('[data-mina-inbjudan-svar="invite-decline"][data-svar="nej"]').click()
    page.wait_for_function("sharedFixture.declined && !document.querySelector('[data-mina-inbjudan-svar=invite-decline]')")
    assert page.evaluate("MINA.lage==='inbjudningar'")
    fail = page.locator('[data-mina-inbjudan-svar="invite-fail"][data-svar="ja"]')
    fail.click()
    page.wait_for_function("!document.querySelector('[data-mina-inbjudan-svar=invite-fail]').disabled")
    assert dialogs == ['Tillfälligt testfel'], dialogs
    assert page.evaluate("MINA.lage==='inbjudningar'")

    page.evaluate("async()=>await minaÖppna({lage:'bank'})")
    assert 'Fysik' not in page.locator('#minaKurs').inner_text()
    assert 'Publicerad skolmall' in page.locator('#minaInnehall').inner_text()
    assert 'Mottaget geometriprov' not in page.locator('#minaInnehall').inner_text()
    page.evaluate('async()=>await minaÖppna()')
    views = []
    for width in [390, 1280]:
        page.set_viewport_size({'width': width, 'height': 1000})
        assert page.locator('[data-mina-oppna="received"]').is_visible()
        for control in ['minaKurs', 'minaSortering']:
            box = page.locator('#'+control).bounding_box()
            assert box['x'] >= 0 and box['x'] + box['width'] <= width
        page.locator('#minamodal').screenshot(path=f'/tmp/ul-delade-dokument-{width}.png')
        views.append(width)

    # Öppna genom riktig delningÖppna/sparLaddaDokument, med en syntetisk hämtad uppgift.
    page.locator('[data-mina-oppna="accepted"]').click()
    page.wait_for_function("DELNING.id==='accepted' && state.blad.length===1 && document.getElementById('minamodal').hidden")
    assert page.evaluate("state.blad[0].id==='3.17' && DELNING.roll==='medlem'")
    page.evaluate('delningKoppla(null,{tyst:true})')
    assert not errors, errors
    print(json.dumps({'courseTrackSearchSort': True, 'receivedVisible': True, 'acceptAndDecline': True, 'failureRetryEnabled': True,
                      'receivedDocumentOpened': True, 'views': views, 'javascriptErrors': errors}))
    browser.close()
