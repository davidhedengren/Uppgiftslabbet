'use strict';
const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('fs'),vm=require('vm');
const c={window:{}};vm.runInNewContext(fs.readFileSync(__dirname+'/../uppgifter.js','utf8'),c);
const all=c.window.BANK.filter(q=>q.omr==='multimeter'),q=id=>all.find(x=>x.id===id);
const wiring=['8.542','8.544','8.545','8.550','8.551','8.552','8.553'];
test('Inkoppling kräver både rätt kopplingssätt och rätt komponent eller gren',()=>{
 for(const id of wiring){const p=q(id),text=p.t.replace(/<svg[\s\S]*?<\/svg>/g,'');
  assert.equal(p.alternativ.length,4,id);assert.equal(p.alternativ.filter(a=>a.ratt).length,1,id);
  assert.ok(p.alternativ.some(a=>/serie/i.test(a.txt)),id);assert.ok(p.alternativ.some(a=>/parallellt/i.test(a.txt)),id);
  assert.ok(p.alternativ.every(a=>a.kommentar),id);
  assert.ok(!/ska.*bryta|ska ledningen brytas|Vid vilken markering/i.test(text),id);
  assert.match(text,/Hur ska multimetern kopplas/);assert.equal(p.traningsniva,2,id);
 }
 for(const id of ['8.542','8.545','8.552','8.553']){
  const p=q(id);assert.match(p.alternativ.find(a=>a.ratt).txt,/^I serie/);
  assert.ok(p.alternativ.some(a=>!a.ratt&&/^I serie/.test(a.txt)),id+' behöver också en felaktig serieplacering');
 }
 for(const id of ['8.544','8.550','8.551']){
  const p=q(id);assert.match(p.alternativ.find(a=>a.ratt).txt,/^Parallellt/);
  assert.ok(p.alternativ.some(a=>!a.ratt&&/^Parallellt/.test(a.txt)),id+' behöver också en felaktig parallellplacering');
 }
});
test('Fyra bildalternativ kräver både rätt mätartyp och rätt koppling',()=>{
 const p=q('8.554');assert.deepEqual(Array.from(p.alternativ,a=>a.txt).sort(),['Bild A','Bild B','Bild C','Bild D']);assert.equal(p.alternativ.find(a=>a.ratt).txt,'Bild B');
 const svg=p.t.match(/<svg[\s\S]*?<\/svg>/)[0];
 assert.match(svg,/A: amperemeter parallellt/);assert.match(svg,/B: amperemeter i serie/);assert.match(svg,/C: voltmeter parallellt/);assert.match(svg,/D: voltmeter i serie/);
 assert.equal((svg.match(/>Bild [A-D]<\/text>/g)||[]).length,4);assert.equal(p.traningsniva,1);
});
test('Kombinationsfrågor kan besvaras fel enbart genom fel inkoppling',()=>{
 const p=q('8.548');assert.ok(p.alternativ.some(a=>!a.ratt&&/COM och 10A.*10 A.*parallellt med L1/.test(a.txt)));
 assert.ok(p.alternativ.some(a=>a.ratt&&/COM och 10A.*10 A.*serie vid Q/.test(a.txt)));
 const r=q('8.564');assert.equal(6/300*1000,20);assert.ok(r.alternativ.some(a=>!a.ratt&&/400 mA; parallellt/.test(a.txt)));assert.ok(r.alternativ.some(a=>!a.ratt&&/4000 µA; i serie/.test(a.txt)));
 assert.match(r.alternativ.find(a=>a.ratt).txt,/400 mA; i serie/);
});
test('Alla 44 kort bevarar verktygsregler och blandade alternativ',()=>{
 assert.equal(all.length,52); // 44 + 8 avläsningskort 2026-10-24 (8.628-8.635), varav fem med talsvar
 for(const p of all){assert.equal(p.miniräknare,true,p.id);assert.equal(p.geogebra,false,p.id);assert.equal(p.spel,true,p.id);assert.equal(p.självrättning,true,p.id);assert.match(p.t,/<svg/);if(p.alternativ)assert.equal(new Set(p.alternativ.map(a=>a.txt)).size,p.alternativ.length,p.id);}
 assert.equal(q('8.539').traningsniva,2);assert.equal(q('8.548').traningsniva,3);
 assert.ok(q('8.559').alternativ.some(a=>a.txt==='4000 µA'&&!a.ratt));assert.equal(q('8.543').alternativ.find(a=>a.ratt).txt,'Mellan A och B.');
});
test('Mätområdets slutsats kräver en övre gräns; 10A är inte bara möjligt över 400 mA',()=>{
 assert.match(q('8.540').t,/mindre än 100 mA/);assert.match(q('8.540').s,/mindre än 100 mA/);
 assert.ok(!/används bara.*400 mA/.test(q('8.530').s));assert.ok(!/används bara.*400 mA/.test(q('8.532').s));
 assert.match(q('8.532').s,/10A-uttaget fungerar också/);
});
test('8.553 prövar missuppfattningen att val av gren inte spelar någon roll',()=>{
 const p=q('8.553'),anywhere=p.alternativ.find(a=>a.txt==='Det spelar ingen roll: bryt vid P, Q eller R.');
 assert.ok(anywhere);assert.equal(anywhere.ratt,false);assert.match(anywhere.kommentar,/Vid P går hela strömmen/);assert.match(anywhere.kommentar,/Vid Q eller R går bara/);
 assert.match(p.s,/vid R bara strömmen genom R₂/);assert.match(p.s,/spelar alltså roll/);
 assert.equal(p.alternativ.filter(a=>a.ratt).length,1);assert.match(p.alternativ.find(a=>a.ratt).txt,/huvudledningen.*vid P/);
});
test('Åtta nya kretsar prövar ström, spänning och olika topologier',()=>{
 const ids=Array.from({length:8},(_,i)=>'8.'+(566+i));const figures=new Set();
 for(const id of ids){const p=q(id);assert.ok(p,id);assert.equal(p.alternativ.filter(a=>a.ratt).length,1,id);assert.ok(p.alternativ.length>=4,id);assert.ok(p.alternativ.every(a=>a.kommentar),id);assert.ok(p.traningsniva>=1&&p.traningsniva<=3,id);figures.add(p.t.match(/<svg[\s\S]*?<\/svg>/)[0]);}
 assert.equal(figures.size,8);assert.equal(q('8.566').traningsniva,1);
 assert.equal(q('8.572').traningsniva,3);assert.equal(q('8.573').traningsniva,3);
});
test('Det spelar ingen roll är ibland rätt: begränsat till verkligt likvärdiga placeringar',()=>{
 for(const id of ['8.542','8.545','8.552','8.553','8.567','8.569','8.570','8.572']){
  const a=q(id).alternativ.find(a=>a.txt.startsWith('Det spelar ingen roll'));assert.ok(a,id);assert.equal(a.ratt,false,id);
 }
 for(const id of ['8.566','8.568'])assert.match(q(id).alternativ.find(a=>a.ratt).txt,/^Det spelar ingen roll/);
 assert.match(q('8.566').s,/ingen.*väg|bara en väg/);assert.match(q('8.568').s,/lika stor/);
 assert.match(q('8.570').alternativ.find(a=>a.ratt).txt,/P eller S/);
 assert.match(q('8.572').alternativ.find(a=>a.ratt).txt,/P eller Q/);assert.match(q('8.572').s,/Vid R.*0 A/);
});
test('Nya spänningsmätningar och dubbelmätning har rätt komponentgränser',()=>{
 assert.match(q('8.569').alternativ.find(a=>a.ratt).txt,/B och D/);
 assert.equal(q('8.571').alternativ.find(a=>a.ratt).txt,'Bild C');
 assert.match(q('8.573').alternativ.find(a=>a.ratt).txt,/serie vid P; voltmetern mellan A och B/);
 assert.ok(q('8.573').alternativ.some(a=>!a.ratt&&/serie vid P; voltmetern mellan C och D/.test(a.txt)));
});
