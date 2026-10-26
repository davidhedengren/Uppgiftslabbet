'use strict';
/* Ma2 kap 1–2 nivå 3 i tunna områden (2026-10-26). Ett block per område. Kontrollerar nivå, format, facit enligt 1.116
   (rubrik i varje steg, svarsrad, inga råa < >), flervalskommentarer, dubblettfacit och räknar om svaren. */
const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('node:fs'),vm=require('node:vm'),path=require('node:path');
const c={window:{}};vm.runInNewContext(fs.readFileSync(path.join(__dirname,'..','uppgifterma2.js'),'utf8'),c);
const B=JSON.parse(JSON.stringify(Object.values(c.window).find(Array.isArray)));const get=id=>{const t=B.find(x=>x.id===id);assert.ok(t,id);return t;};
const r=(p,a,b)=>Array.from({length:b-a+1},(_,i)=>`${p}.${a+i}`);
const OMR={grafisk_losning_ekvationssystem:r(1,1229,1234)};
const v=x=>JSON.stringify(x.rättSvar);
for(const [omr,ids] of Object.entries(OMR))test(`${omr}: ${ids.length} nivå 3-kort med facitkraven uppfyllda`,()=>{
  for(const id of ids){const t=get(id);assert.equal(t.omr,omr,id);assert.equal(t.traningsniva,3,id);assert.equal(t.niva,'C',id);assert.equal(t.poang,'0/1/0',id);assert.equal(t.spel,true,id);
    const steg=[...t.s.matchAll(/<li>([\s\S]*?)<\/li>/g)];assert.ok(steg.length>=2,id);for(const m of steg)assert.match(m[1],/^<p class="facit-rubrik">/,id);
    assert.match(t.s,/class="facit-svar"/,id);assert.ok(String(t.ledtrad).replace(/<[^>]+>/g,'').trim().length>=15,id);
    for(const m of (t.t+t.s+t.ledtrad).matchAll(/\\\(([\s\S]*?)\\\)|\\\[([\s\S]*?)\\\]/g))assert.doesNotMatch(m[1]??m[2],/[<>]/,id);
    if(t.svarstyp==='alternativ'){assert.equal(t.alternativ.filter(a=>a.ratt).length,1,id);assert.ok(!t.alternativ[0].ratt,id);for(const a of t.alternativ)if(!a.ratt)assert.ok(a.kommentar,id);}
    else{const krock=B.filter(w=>w.omr===omr&&w.id!==id&&w.rättSvar!=null&&v(w)===v(t)).map(w=>w.id);assert.deepEqual(krock,[],id);}
    if(t.svarstyp==='flera_delar'){assert.equal(t.svarEtiketter.length,t.rättSvar.length,id);assert.deepEqual(t.självrättning,t.rättSvar.map(()=>true),id);}}
});
// sys: varje ekvation skrivs som funktion av lösningen och ska bli 0
const sys=(id,...ekv)=>{const x=get(id).rättSvar.map(Number);for(const f of ekv)assert.ok(Math.abs(f(...x))<1e-9,`${id}: ${x} uppfyller inte ${f}`);};
test('grafisk_losning_ekvationssystem: svaren räknas om',()=>{
  sys('1.1229',(x,y)=>2*x-1-y,(x,y)=>-0.5*x+5-y);
  // a och b ger samma linje som 6x − 2y = 4 för två olika x
  sys('1.1230',(a,b)=>6*0-2*(a*0+b)-4,(a,b)=>6*1-2*(a*1+b)-4);
  sys('1.1231',(t,V)=>200-8*t-V,(t,V)=>50+4*t-V);
  const m=get('1.1232').rättSvar;assert.equal(-8+8,0);assert.equal(2*8+m,0);
  sys('1.1233',(x,y)=>0.5*x+1-y,(x,y)=>0.6*x-1-y);
  assert.equal(get('1.1234').alternativ.find(a=>a.ratt).txt,'Om c = 10 har systemet oändligt många lösningar');
});
