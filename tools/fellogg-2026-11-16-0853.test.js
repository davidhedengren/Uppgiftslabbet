'use strict';
// Felrapporter 2026-11-16 08:53 (Ma5 2.626 c) och uppföljning av 08:16 (ledtrådar om fältkrafter i Fy2).
// Logg: agent/FELRAPPORTER_2026-11-16_0853.md.
const {test}=require('node:test'),a=require('node:assert/strict'),fs=require('node:fs'),vm=require('node:vm');
const las=(f,n)=>{const c={window:{}};vm.runInNewContext(fs.readFileSync(f,'utf8'),c);return c.window[n];};
const fy2=las('uppgifter2.js','BANK2'),ma5=las('uppgiftermatf1.js','BANKMATF1');
const ledtradar=u=>[u.ledtrad,...(u.spelDelar||[]).map(p=>p.ledtrad)].filter(Boolean);
const HASTIGHETSFILTER=['3.12','3.114','4.37','4.38','4.46','4.48','4.50'];

test('Fy2: ledtråden om F_E och F_B finns bara där det finns både elektriskt fält och magnetfält',()=>{
 const med=fy2.filter(u=>ledtradar(u).some(l=>/Skriv kraften från varje fält separat/.test(l))).map(u=>u.id).sort();
 a.equal(med.join(),[...HASTIGHETSFILTER].sort().join());
 for(const id of HASTIGHETSFILTER){const u=fy2.find(x=>x.id===id);a.match(u.t,/hastighets(filter|väljare)/i,id);}
});

test('Fy2: uppgifter med bara magnetfält har ingen ledtråd om elektrisk kraft eller balans',()=>{
 for(const u of fy2.filter(u=>['laddade_partiklar'].includes(u.omr)&&!HASTIGHETSFILTER.includes(u.id))){
  for(const l of ledtradar(u)){a.doesNotMatch(l,/F_E=qE/,u.id);a.doesNotMatch(l,/krafterna balansera/,u.id);}
 }
 for(const id of ['3.47','3.61','3.62','3.68','4.32'])a.match(fy2.find(x=>x.id===id).ledtrad,/högerhandsregeln/,id);
 for(const id of ['3.11','3.53','4.34','4.35','4.57'])a.match(fy2.find(x=>x.id===id).ledtrad,/centripetalkraft/,id);
});

test('Ma5 2.626 c: facit och frågetext oförändrade (”Svara exakt” räcker)',()=>{
 const u=ma5.find(x=>x.id==='2.626'),c=u.spelDelar[2];
 a.equal(u.rättSvar[2],'3145725*pi');a.equal(3*(4**10-1),3145725);
 for(const x of [u.t,c.fraga,c.t]){a.match(x,/alla tio cirklarna\. Svara exakt\./);a.doesNotMatch(x,/alltså med/);}
 a.ok(Math.abs(3145725*Math.PI-9882586.55)<0.01,'decimaltalet i rapporten är inte exakt');
});
