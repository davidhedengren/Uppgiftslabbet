'use strict';
const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('fs'),vm=require('vm');const c={window:{}};vm.runInNewContext(fs.readFileSync(__dirname+'/../uppgifter.js','utf8'),c);const bank=c.window.BANK,q=id=>bank.find(q=>q.id===id),ids=Array.from({length:6},(_,i)=>'8.'+(574+i));
test('Sex strömkort har olika figurer och frågetyper med egna data',()=>{
 const figures=new Set(),types=new Set();for(const id of ids){const p=q(id);assert.equal(bank.filter(q=>q.id===id).length,1,id);assert.equal(p.kap,8);assert.equal(p.omr,'strom');assert.equal(p.familj,'Ström och laddning i kretsar');assert.equal(p.spel,true);assert.equal(p.självrättning,true);assert.equal(p.miniräknare,true);assert.equal(p.geogebra,false);assert.ok(p.traningsniva<=2);assert.match(p.t,/<svg/);assert.match(p.t,/\((Svara|Välj)/);assert.ok(p.ledtrad);assert.doesNotMatch(p.t,/föregående del|svaret ovan/);assert.doesNotMatch(p.s,/facit-steglista|[\u0000-\u0008\u000b\u000c\u000e-\u001f]/);figures.add(p.t.match(/<svg[\s\S]*?<\/svg>/)[0]);types.add(p.typ);}assert.equal(figures.size,6);assert.equal(types.size,6);
});
test('Laddningsdiagram, tabellskillnader och två strömlägen räknas från givna data',()=>{
 assert.equal(q('8.574').rättSvar,18/6);assert.match(q('8.574').t,/18 C vid 6 s/);
 assert.equal(q('8.575').rättSvar,(7-1)/(5-2));assert.notEqual(q('8.575').rättSvar,7/3);
 assert.equal(q('8.576').rättSvar,.4*10+.1*20);assert.notEqual(q('8.576').rättSvar,(.4+.1)/2*30);
});
test('Strömriktningar och hela pulsperioden ingår i beräkningarna',()=>{
 assert.equal(q('8.577').rättSvar,1.2-.45);assert.match(q('8.577').t,/går in i förgreningen/);assert.match(q('8.577').t,/I går ut i nedre/);
 assert.equal(q('8.578').rättSvar,.6*.2/2*1000);assert.match(q('8.578').t,/noll från 0,20 till 2,0 s/);assert.notEqual(q('8.578').rättSvar,.6*1000);
});
test('Konstant ström är konstant Q-t-lutning, inte en böjd eller knäckt graf',()=>{
 const p=q('8.579');assert.equal(p.alternativ.filter(a=>a.ratt).length,1);assert.equal(p.alternativ.find(a=>a.ratt).txt,'Diagram B');assert.equal(p.alternativ.findIndex(a=>a.ratt),3);assert.ok(p.alternativ.every(a=>a.kommentar));assert.match(p.s,/samma lutning hela tiden/);
 // Avsedda kurvor: B har samma ökning i alla lika långa intervall; A/C/D har det inte.
 const curves=[u=>u*u,u=>u,u=>u<=.5?.4*u:.2+1.6*(u-.5),u=>2*u-u*u];
 assert.deepEqual(curves.map(f=>{const slopes=Array.from({length:4},(_,i)=>(f((i+1)/4)-f(i/4))/.25);return slopes.every(v=>Math.abs(v-slopes[0])<1e-12);}),[false,true,false,false]);
});
