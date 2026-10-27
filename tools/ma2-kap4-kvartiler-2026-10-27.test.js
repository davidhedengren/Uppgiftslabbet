'use strict';
/* Ma2 kap 4 etapp 2: kvartiler och percentiler (2026-10-27). Facit enligt Ma1 #1.116 med kortspecifika rubriker,
   delkort med eget facit och egen ledtråd, kommentarer till alla flervalsalternativ och varierade percentilfrågor.
   Talbrickorna i 4.512, 4.513 och 4.517 markerade svaret (medianrutan i annan färg, ”nedre halvan”) och är nu neutrala. */
const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('node:fs'),vm=require('node:vm'),path=require('node:path');
const c={window:{}};vm.runInNewContext(fs.readFileSync(path.join(__dirname,'..','uppgifterma2.js'),'utf8'),c);
const L=c.window.BANKMA2.filter(q=>q.omr==='kvartiler_percentiler'&&q.kap===4),get=id=>L.find(q=>q.id===id);
const ren=s=>(s||'').replace(/<svg[\s\S]*?<\/svg>/g,' ').replace(/<[^>]+>/g,' ').replace(/\s+/g,' ').trim();
const rubriker=s=>[...(s||'').matchAll(/class="facit-rubrik">([\s\S]*?)<\/p>/g)].map(m=>ren(m[1]));
function facit(namn,s){assert.match(s,/facit-svar/,`${namn}: svarsrad`);const st=(s.match(/<li>/g)||[]).length+(s.match(/class="facit-stycke"/g)||[]).length,r=rubriker(s);
  assert.ok(st>0&&r.length>=st,`${namn}: ${st} steg men ${r.length} rubriker`);}
test('Facit med rubrik per steg, delkort med eget facit och ledtråd, inga delade rubriker eller ledtrådar',()=>{
  assert.ok(L.length>=59);const rub={},led={};
  for(const q of L){facit(q.id,q.s);(led[q.ledtrad]=led[q.ledtrad]||[]).push(q.id);
    for(const d of q.spelDelar||[]){facit(q.id+d.etikett,d.s);assert.ok(ren(d.ledtrad).length>10,q.id+d.etikett);}
    for(const r of new Set([q.s,...(q.spelDelar||[]).map(d=>d.s)].flatMap(rubriker)))(rub[r]=rub[r]||new Set()).add(q.id);}
  assert.deepEqual(Object.entries(rub).filter(([,v])=>v.size>1).map(([r])=>r),[]);
  assert.deepEqual(Object.values(led).filter(v=>v.length>1),[]);
  for(const q of L)assert.doesNotMatch(ren(q.ledtrad),/Vilken information i tabellen|Skilj på det som går att läsa av|Tänk på vad percentilen eller kvartilen betyder/,q.id);
});
test('Alla flervalsalternativ har kommentarer och passar sitt sammanhang',()=>{
  for(const q of L.filter(q=>q.alternativ)){assert.equal(q.alternativ.filter(a=>a.ratt).length,1,q.id);for(const a of q.alternativ)assert.ok((a.kommentar||'').length>10,`${q.id}: ${a.txt}`);}
  assert.doesNotMatch(get('4.22').alternativ.map(a=>a.txt).join(),/maxpoäng/);assert.doesNotMatch(get('4.193').alternativ.map(a=>a.txt).join(),/maxpoäng|resultaten/);
});
test('Figurerna avslöjar inte svaret',()=>{
  for(const id of ['4.512','4.513','4.517']){const s=get(id).t.match(/<svg[\s\S]*?<\/svg>/)[0];
    const fills=[...s.matchAll(/<rect x="\d+" y="20" width="\d+" height="46" rx="6" fill="([^"]+)"/g)].map(m=>m[1]);
    assert.ok(fills.length>=6&&new Set(fills).size===1,`${id}: ${[...new Set(fills)]}`);assert.doesNotMatch(s,/markera|nedre halvan|mittersta/i,id);}
  assert.deepEqual([get('4.512').rättSvar,get('4.513').rättSvar,get('4.517').rättSvar],[11,20,3]);
});
test('4.164 är osorterad och ger samma kvartiler',()=>{
  const v=[18,4,11,7,2,13,9,5].sort((a,b)=>a-b),md=a=>(a[(a.length-1)>>1]+a[a.length>>1])/2;
  assert.deepEqual([md(v.slice(0,4)),md(v),md(v.slice(4))],JSON.parse(JSON.stringify(get('4.164').rättSvar)));assert.match(get('4.164').t,/18, 4, 11/);
});
