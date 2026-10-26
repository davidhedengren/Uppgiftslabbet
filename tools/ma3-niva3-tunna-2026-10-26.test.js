'use strict';
/* Ma3 nivå 3 i tunna områden (2026-10-26). Ett block per område. Kontrollerar nivå, format, facit enligt 1.116
   (rubrik i varje steg, svarsrad, inga råa < >), flervalskommentarer, dubblettfacit och räknar om svaren. */
const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('node:fs'),vm=require('node:vm'),path=require('node:path');
const c={window:{}};vm.runInNewContext(fs.readFileSync(path.join(__dirname,'..','uppgiftermato1.js'),'utf8'),c);
const B=JSON.parse(JSON.stringify(c.window.BANKMATO1));const get=id=>{const t=B.find(x=>x.id===id);assert.ok(t,id);return t;};
const r=(p,a,b)=>Array.from({length:b-a+1},(_,i)=>`${p}.${a+i}`);
const OMR={deriveringsregler:r(2,1259,1264)};
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
const d=(f,x,h=1e-5)=>(f(x+h)-f(x-h))/(2*h);
const nara=(a,b,id)=>assert.ok(Math.abs(a-b)<1e-6,`${id}: ${a} ≠ ${b}`);
test('deriveringsregler: derivatorna räknas om numeriskt',()=>{
  for(const x of get('2.1259').rättSvar)nara(d(x=>x**3-3*x*x+2,x),9,'2.1259');
  nara(d(x=>(x*x+4)/Math.sqrt(x),4),get('2.1260').rättSvar,'2.1260');
  const [x3,y3]=get('2.1261').rättSvar,f3=x=>x*x-4*x+1;nara(d(f3,x3),2,'2.1261');assert.equal(f3(x3),y3);
  const [v5,tt]=get('2.1262').rättSvar,V=t=>200+30*t-t*t;nara(d(V,5),v5,'2.1262');nara(d(V,tt),0,'2.1262');
  assert.equal(get('2.1263').alternativ.find(a=>a.ratt).txt,'f(x) = x³ − 12x');nara(d(x=>x**3-12*x,2),0,'2.1263');
  nara(d(x=>(x**3-4*x)/(x*x),2),get('2.1264').rättSvar,'2.1264');
});
