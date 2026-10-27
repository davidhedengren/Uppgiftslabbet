'use strict';
/* Användarbeslut 2026-10-27: alla mattefacit ska ha en förklarande rubrik i varje steg (1.116), pedagogiskt och enkelt.
   Facit skrivs för hand område för område. Listan FÄRDIGA växer när ett område är klart; i dessa områden får
   inget facit sakna rubriker eller ha allmänna rubriker. Se agent/FACIT_RUBRIKER_2026-10-27.md. */
const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('node:fs'),vm=require('node:vm'),path=require('node:path');
const FÄRDIGA={
  'uppgifterma1.js':['tal_rakneordning'],
};
const GENERISK=/^(Steg \d+|Lös ekvationen|Lös|Förenkla|Beräkna|Svar|Derivera|Sätt in|Faktorisera|Multiplicera ut|Kontrollera|Metod)\.?$/i;
function brister(s){
  if(!s)return 'saknar facit';
  const steg=[...s.matchAll(/<li>([\s\S]*?)<\/li>/g)].map(m=>m[1]);
  if(!steg.length)return 'inga steg';
  if(steg.some(x=>!/^\s*<p class="facit-rubrik">/.test(x)))return 'steg utan rubrik';
  const rub=[...s.matchAll(/<p class="facit-rubrik">([\s\S]*?)<\/p>/g)].map(m=>m[1].replace(/<[^>]+>/g,'').trim());
  if(rub.some(r=>GENERISK.test(r)))return 'allmän rubrik';
  if(!/class="facit-svar"/.test(s))return 'svarsrad saknas';
  return null;
}
for(const [fil,omraden] of Object.entries(FÄRDIGA))test(`${fil}: varje facit i färdiga områden har rubrik i varje steg`,()=>{
  const c={window:{}};vm.runInNewContext(fs.readFileSync(path.join(__dirname,'..',fil),'utf8'),c);
  const B=Object.values(c.window).find(Array.isArray);const fel=[];
  for(const x of B){if(!omraden.includes(x.omr)||x.spel===false)continue;
    const facit=x.spelDelning==='deluppgifter'&&Array.isArray(x.spelDelar)?x.spelDelar.filter(d=>d.spel!==false).map(d=>[x.id+d.etikett,d.s||x.s]):[[x.id,x.s]];
    for(const [id,s] of facit){const b=brister(s);if(b)fel.push(`${id}: ${b}`);}}
  assert.deepEqual(fel,[]);
});
