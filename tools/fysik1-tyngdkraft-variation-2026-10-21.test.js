'use strict';
const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('fs'),vm=require('vm');const c={window:{}};vm.runInNewContext(fs.readFileSync(__dirname+'/../uppgifter.js','utf8'),c);const bank=c.window.BANK,q=id=>bank.find(q=>q.id===id),ids=Array.from({length:6},(_,i)=>'4.'+(758+i));
test('Massa och tyngd: sex skilda figuruppgifter för nivå 1–2 med verktyg och självständiga data',()=>{
 const figures=new Set(),types=new Set();for(const id of ids){const p=q(id);assert.equal(bank.filter(q=>q.id===id).length,1,id);assert.equal(p.kap,4);assert.equal(p.omr,'tyngdkraft');assert.equal(p.familj,'Massa och tyngd');assert.equal(p.miniräknare,true);assert.equal(p.geogebra,false);assert.equal(p.spel,true);assert.equal(p.självrättning,true);assert.ok(p.traningsniva<=2);assert.match(p.t,/\((Välj|Svara)/);assert.match(p.t,/<svg/);assert.doesNotMatch(p.t,/använd.*(?:formeln|konstant)|föregående del|svaret ovan/i);assert.doesNotMatch(p.s,/<ol|facit-steglista|[\u0000-\u0008\u000b\u000c\u000e-\u001f]/);assert.ok(p.ledtrad);figures.add(p.t.match(/<svg[\s\S]*?<\/svg>/)[0]);types.add(p.typ);}assert.equal(figures.size,6);assert.equal(types.size,6);assert.equal(bank.filter(q=>q.omr==='tyngdkraft').length,27);assert.equal(bank.filter(q=>q.omr==='tyngdkraft'&&q.spel!==false).length,25);
});
test('Diagram och mätare ger massa, kraft respektive en dimensionslös jämförelse',()=>{
 assert.equal(q('4.758').rättSvar,24/(40/10));assert.equal(q('4.758').svarEnhet,'kg');assert.match(q('4.758').t,/10 kg, 40 N/);
 assert.equal(q('4.760').rättSvar,15*4/2);assert.equal(q('4.760').svarEnhet,'N');assert.match(q('4.760').t,/hänger stilla/);
 assert.equal(q('4.761').rättSvar,20/8);assert.equal(q('4.761').svarFormat,'multipel');assert.match(q('4.761').t,/4 kg tyngdkraften 8 N/);assert.match(q('4.761').t,/4 kg tyngdkraften 20 N/);
});
test('Tyngdkraft och hastighet blandas inte ihop; kraftens storlek jämförs med massan',()=>{
 assert.equal(q('4.759').alternativ.find(a=>a.ratt).txt,'Bild C');assert.match(q('4.759').t,/luftmotståndet/);
 const a=2*9.82/2,b=6*9.82/6;assert.equal(a,b);assert.equal(q('4.762').alternativ.find(a=>a.ratt).txt,'De får lika stor acceleration.');
 assert.match(q('4.762').t,/M125 95L125 140/);assert.match(q('4.762').t,/M355 95L355 230/);assert.equal((230-95)/(140-95),3);
 assert.equal(q('4.763').alternativ.find(a=>a.ratt).txt,'Alla tre påverkas av lika stor tyngdkraft.');assert.match(q('4.763').t,/Pilarna visar deras hastigheter/);assert.match(q('4.763').t,/samma höjd/);
});
test('Felalternativ ger återkoppling och rätta alternativ har blandade positioner',()=>{
 const positions=[];for(const id of ['4.759','4.762','4.763']){const p=q(id);assert.equal(p.alternativ.filter(a=>a.ratt).length,1);assert.ok(p.alternativ.every(a=>a.kommentar));positions.push(p.alternativ.findIndex(a=>a.ratt));}assert.equal(new Set(positions).size,3);
});
