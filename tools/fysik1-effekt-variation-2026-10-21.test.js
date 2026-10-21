'use strict';
const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('fs'),vm=require('vm');const c={window:{}};vm.runInNewContext(fs.readFileSync(__dirname+'/../uppgifter.js','utf8'),c);const bank=c.window.BANK,q=id=>bank.find(q=>q.id===id),ids=Array.from({length:6},(_,i)=>'5.'+(623+i));
test('Sex rutinuppgifter varierar diagram, tabell, energiflöde, dragkraft och mätarvärden',()=>{
 const figures=new Set(),types=new Set();for(const id of ids){const p=q(id);assert.equal(bank.filter(q=>q.id===id).length,1,id);assert.equal(p.kap,5);assert.equal(p.omr,'effekt');assert.equal(p.spel,true);assert.equal(p.självrättning,true);assert.equal(p.miniräknare,true);assert.equal(p.geogebra,false);assert.ok(p.traningsniva<=2);assert.match(p.t,/<svg/);assert.match(p.t,/\((Svara|Välj)/);assert.doesNotMatch(p.s,/facit-steglista|[\u0000-\u0008\u000b\u000c\u000e-\u001f]/);figures.add(p.t.match(/<svg[\s\S]*?<\/svg>/)[0]);types.add(p.typ);}assert.equal(figures.size,6);assert.equal(types.size,6);
});
test('Diagrammens skalor, tidsdelar och mätarnas startvärden ger rätt resultat',()=>{
 assert.equal(q('5.623').rättSvar,3e3/6);assert.match(q('5.623').t,/3 kJ vid 6 s/);
 assert.equal(q('5.625').rättSvar,600/800*100);assert.equal(600+200,800);
 assert.ok(Math.abs(q('5.626').rättSvar-(1.2*2/60+.3*(6-2)/60))<1e-12);assert.match(q('5.626').t,/0,3 kW under minut 2 till 6/);
 assert.ok(Math.abs(q('5.628').rättSvar-(12.7-12.4)/(15/60))<1e-12);
});
test('Kraft och rörelse har samma riktning vid positiv överförd effekt',()=>{
 assert.equal(q('5.627').rättSvar,60/.5);assert.match(q('5.627').t,/rör sig åt vänster/);assert.match(q('5.627').t,/M440 101L312 101/);assert.match(q('5.627').t,/M319.98 96.84L312 101L319.98 105.16/);assert.match(q('5.627').t,/M311 163L217 163/);
});
test('Både jämförelsemetod och felalternativ förklaras',()=>{
 const p=q('5.624');assert.equal(6000/12,500);assert.equal(9000/30,300);assert.equal(p.alternativ.filter(a=>a.ratt).length,1);assert.match(p.alternativ.find(a=>a.ratt).txt,/Band A/);assert.ok(p.alternativ.every(a=>a.kommentar));assert.match(p.s,/300/);
});
