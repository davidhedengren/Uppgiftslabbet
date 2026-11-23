'use strict';
// Fy1 densitet 2026-11-23: språket i området efter lärarens korpus och sex nya blandningsuppgifter på A-nivå (2.371–2.376).
// Se agent/FY1_DENSITET_A_2026-11-23.md och tools/bygg-fy1-densitet-a-2026-11-23.py.
const {test}=require('node:test');
const assert=require('node:assert/strict');
const fs=require('node:fs'),vm=require('node:vm'),path=require('node:path');
const c={window:{}};
vm.runInNewContext(fs.readFileSync(path.join(__dirname,'../uppgifter.js'),'utf8'),c);
const tasks=c.window.BANK.filter(q=>q.omr==='densitet');
const q=id=>tasks.find(q=>q.id===id);
const synlig=h=>(h||'').replace(/<svg[\s\S]*?<\/svg>/g,'').replace(/<[^>]+>/g,' ');

test('Svaren räknas om oberoende',()=>{
 const silver=(15*12/19.3-12)/(1-15/10.5);
 assert.ok(Math.abs(q('2.371').rättSvar[0]-silver)<1e-9);
 assert.ok(Math.abs(q('2.371').rättSvar[1]-24*12/(12+silver))<1e-9);
 assert.equal(Math.round(24*12/18.2),16);
 const ag=(60-1000/19.3)/(1/10.5-1/19.3);
 assert.ok(Math.abs(q('2.372').rättSvar[1]-ag)<1e-9);assert.equal(Math.round(ag),189);
 assert.equal(q('2.373').rättSvar,600);assert.equal((480+600)/(400+600),1.08);
 assert.ok(Math.abs(q('2.374').rättSvar[0]-100*(1-6250/30000))<1e-9);
 assert.equal(q('2.374').rättSvar[1],(15000+0.3*23750)/30000);
 assert.equal(Math.round(100*(15000+0.3*0.79*30000)/30000),74);
 assert.ok(Math.abs(q('2.375').rättSvar-100*(0.917-0.8)/0.2)<1e-9);
 assert.equal(q('2.376').rättSvar,4);
});

test('Nya uppgifter: A-nivå, facit enligt mallen, självbärande delkort',()=>{
 for(const id of ['2.371','2.372','2.373','2.374','2.375','2.376']){
  const t=q(id);
  assert.equal(t.niva,'A',id);assert.equal(t.miniräknare,true,id);assert.equal(t.geogebra,false,id);
  assert.match(t.s,/Givet och sökt/,id);
  assert.match(t.s,/class="facit-rubrik">[^<]*\\\(/,id); // formeln står i en rubrik
  assert.doesNotMatch(synlig(t.t),/Antag att|[Rr]äkna med|Avrunda|\(Svara/,id);
  for(const d of t.spelDelar||[]){
   assert.ok(d.t.startsWith(t.spelIntro),id+d.etikett);
   assert.match(d.s,/class="facit-svar"/,id+d.etikett);
  }
 }
 // Mellanresultat som delkortet behöver står i dess fråga, inte i huvudtexten.
 assert.match(q('2.371').spelDelar[1].fraga,/6,2 g silver/);assert.doesNotMatch(q('2.371').t,/6,2 g/);
 assert.match(q('2.374').spelDelar[1].fraga,/79 %/);assert.doesNotMatch(q('2.374').t,/79 %/);
 for(const id of ['2.372','2.373','2.375'])assert.match(q(id).t,/<svg/,id);
});

test('Språket i området: inga konstlade antaganden, modellord eller metatext',()=>{
 for(const t of tasks){
  const s=synlig(t.t)+synlig(t.spelIntro)+(t.spelDelar||[]).map(d=>synlig(d.t)+' '+(d.fraga||'')).join(' ');
  assert.doesNotMatch(s,/Avrunda inte|redan anpassad|volymer tillsammans är|förenklad modell|samma material rakt igenom|samma träslag rakt igenom|Referensdensiteter|definieras som|antas ha/,t.id);
 }
 // A-uppgifterna om metallegeringar har inget antagande om att volymerna läggs ihop; vätskeblandningarna har det kvar kort.
 for(const id of ['2.146','2.200','2.365','2.371','2.372'])assert.doesNotMatch(synlig(q(id).t),/volymer/,id);
 for(const id of ['2.202','2.367','2.373','2.376'])assert.match(synlig(q(id).t),/Anta att vätskornas volymer kan adderas\./,id);
 assert.match(q('2.51').t,/Visa att ringens densitet kan skrivas/);
 assert.match(q('2.191').kgInstruktion,/negativt tal/);assert.doesNotMatch(q('2.191').t,/tecken/);
 assert.doesNotMatch(q('2.369').s,/\{\\,\}5\}/); // trasigt decimalkomma i facit rättat
});
