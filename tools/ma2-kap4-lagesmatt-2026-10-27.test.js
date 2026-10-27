'use strict';
/* Ma2 kap 4 etapp 1: lägesmått (2026-10-27). Facit enligt Ma1 #1.116 med kortspecifika rubriker, delkort med eget facit
   och egen ledtråd, varierade texter i mallfamiljerna (saknat värde, två gruppers medelvärde, summa ur medelvärde) och
   kommentarer till flervalsalternativ. Se agent/MA2_KAP4_REVISION_2026-10-27.md. */
const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('node:fs'),vm=require('node:vm'),path=require('node:path');
const c={window:{}};vm.runInNewContext(fs.readFileSync(path.join(__dirname,'..','uppgifterma2.js'),'utf8'),c);
const L=c.window.BANKMA2.filter(q=>q.omr==='lagesmatt'&&q.kap===4);
const ren=s=>(s||'').replace(/<svg[\s\S]*?<\/svg>/g,' ').replace(/<[^>]+>/g,' ').replace(/\s+/g,' ').trim();
const rubriker=s=>[...(s||'').matchAll(/class="facit-rubrik">([\s\S]*?)<\/p>/g)].map(m=>ren(m[1]));
function facit(namn,s){
  assert.match(s,/facit-svar/,`${namn}: svarsrad saknas`);
  const steg=(s.match(/<li>/g)||[]).length+(s.match(/class="facit-stycke"/g)||[]).length,r=rubriker(s);
  assert.ok(steg>0&&r.length>=steg,`${namn}: ${steg} steg men ${r.length} rubriker`);
  for(const x of r)assert.doesNotMatch(x,/^(steg\s*\d|förenkla|lös ekvationen|beräkna|svar)$/i,`${namn}: generisk rubrik ”${x}”`);
}
test('Alla lägesmåttskort i kap 4 har facit med rubrik per steg, och delkort har eget facit och egen ledtråd',()=>{
  assert.ok(L.length>=70,L.length);
  for(const q of L){facit(q.id,q.s);assert.ok(ren(q.ledtrad).length>15,`${q.id}: ledtråd`);
    for(const d of q.spelDelar||[]){facit(`${q.id}${d.etikett}`,d.s);assert.ok(ren(d.ledtrad).length>10,`${q.id}${d.etikett}: ledtråd`);}}
});
test('Rubrikerna är skrivna för sitt kort och återanvänds inte mellan kort',()=>{
  const var_={};for(const q of L)for(const r of new Set([q.s,...(q.spelDelar||[]).map(d=>d.s)].flatMap(rubriker)))(var_[r]=var_[r]||new Set()).add(q.id);
  const delade=Object.entries(var_).filter(([,v])=>v.size>1).map(([r,v])=>`${r}: ${[...v]}`);
  assert.deepEqual(delade,[]);
});
test('Mallfamiljerna har varierade texter och egna ledtrådar',()=>{
  const b={},l={};for(const q of L){const k=ren(q.t).slice(0,45).toLowerCase();(b[k]=b[k]||[]).push(q.id);(l[q.ledtrad]=l[q.ledtrad]||[]).push(q.id);}
  assert.deepEqual(Object.values(b).filter(v=>v.length>1),[]);assert.deepEqual(Object.values(l).filter(v=>v.length>1),[]);
  const svar={'4.25':14,'4.60':23,'4.85':15,'4.111':18,'4.112':17,'4.200':17,'4.74':21,'4.101':20,'4.205':14,'4.31':27.1,'4.55':21.6,'4.77':26.4,'4.206':18,'4.76':140,'4.91':112,'4.119':19,'4.203':8,'4.204':6};
  for(const[id,v]of Object.entries(svar))assert.equal(L.find(q=>q.id===id).rättSvar,v,id);
});
test('Flervalsalternativ har kommentarer, och 4.16:s motexempel stämmer',()=>{
  for(const q of L.filter(q=>q.alternativ))for(const a of q.alternativ)assert.ok((a.kommentar||'').length>10,`${q.id}: ${a.txt}`);
  const A=[40,45,50,55,60],B=[1,2,50,57,200],med=v=>v.slice().sort((a,b)=>a-b)[2],mv=v=>v.reduce((a,b)=>a+b)/v.length;
  assert.deepEqual([med(A),mv(A),med(B),mv(B)],[50,50,50,62]);assert.match(L.find(q=>q.id==='4.16').s,/1, 2 och 50/);
});
