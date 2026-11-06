'use strict';
/* Fy1 kapitel 3 (Rörelse): övriga områden än konstacc får facit enligt agent/FACITMALL.md (användarbeslut 2026-11-04).
   FÄRDIGA växer område för område. Alla uppgifter räknas, även de som bara visas i Uppgiftslabbet (spel:false).
   Se agent/FY1_RORELSE_FACIT_2026-11-04.md. */
const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('node:fs'),vm=require('node:vm'),path=require('node:path');
const c={window:{}};vm.runInNewContext(fs.readFileSync(path.join(__dirname,'..','uppgifter.js'),'utf8'),c);
const B=JSON.parse(JSON.stringify(c.window.BANK));
// Kapitel 3 och 4 klara 2026-11-04; kapitel 5 fylls på område för område (arbete 2026-11-06).
const FÄRDIGA=['konstacc','st_diagram','acceleration','vt_diagram','at_diagram','vektorer','tyngdkraft','newton1','newton2','newton3','normalkraft','gravitation','fjadrar','friktion','lutande_plan','moment','blandat_kraft','arbete','effekt','rorelseenergi','blandat_energi'];
// KaTeX visar inte tankstreck inne i \text{} (”0 2 s”): skriv ”0 till 2 s”.
test('Inga tankstreck i text-block i färdiga områden',()=>{for(const x of B.filter(x=>FÄRDIGA.includes(x.omr)))assert.doesNotMatch(JSON.stringify(x),/\\text\{–\}/,x.id);});
const RUBRIK_MED_FORMEL=/<p class="facit-rubrik">[^<]*\\\([^<]*\\\)[^<]*<\/p>/;
const GENERISK=/<p class="facit-rubrik">(Steg \d+|Beräkna|Förenkla|Svar|Lösning)\.?<\/p>/;
function brister(s,alt){
  if(!s)return 'saknar facit';
  if(!/facit-steglista/.test(s))return 'ingen steglista';
  const steg=[...s.matchAll(/<li>([\s\S]*?)<\/li>/g)].map(m=>m[1]);
  if(steg.some(x=>!/^\s*<p class="facit-rubrik">/.test(x)))return 'steg utan rubrik';
  if(GENERISK.test(s))return 'allmän rubrik';
  if(!alt&&!RUBRIK_MED_FORMEL.test(s))return 'ingen rubrik med formel';
  if(!/class="facit-svar"/.test(s))return 'svarsrad saknas';
  if(/None|undefined/.test(s.replace(/<svg[\s\S]*?<\/svg>/g,'')))return 'teknisk rest';
  return null;
}
test('Fy1 kapitel 3: färdiga områden följer facitmallen, även delfacit och UL-uppgifter',()=>{
  const fel=[];
  for(const x of B.filter(x=>FÄRDIGA.includes(x.omr))){const alt=x.svarstyp==='alternativ';
    const delar=x.spelDelning==='deluppgifter'?(x.spelDelar||[]).filter(d=>d.spel!==false).map(d=>[x.id+d.etikett,d.s]):[];
    for(const [id,s] of [[x.id,x.s],...delar]){const b=brister(s,alt);if(b)fel.push(`${id}: ${b}`);}}
  assert.deepEqual(fel,[]);
});
test('st_diagram: delfacit avslöjar inte senare delars svar',()=>{
  const q=id=>B.find(x=>x.id===id),d=(id,i)=>q(id).spelDelar[i].s;
  assert.doesNotMatch(d('3.13',3),/60\\ \\mathrm m|60 m/);
  assert.doesNotMatch(d('3.138',2),/100/);
  assert.doesNotMatch(d('3.36',1),/4\{,\}8/);
});
test('acceleration: andragradsekvationen i 3.360 löses grafiskt och tillåter GeoGebra',()=>{
  const t=B.find(x=>x.id==='3.360');assert.equal(t.geogebra,true);assert.match(t.s,/grafiskt/);assert.match(t.s,/<svg[\s\S]*<polyline[\s\S]*<\/svg>/);
  const r=8+Math.sqrt(96);assert.ok(Math.abs(t.rättSvar[0]-r)<1e-9&&Math.abs(t.rättSvar[1]-(40+20*r))<1e-9);
});
