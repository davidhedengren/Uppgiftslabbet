'use strict';
const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('fs'),vm=require('vm');const c={window:{}};vm.runInNewContext(fs.readFileSync(__dirname+'/../uppgifter.js','utf8'),c);const bank=c.window.BANK,q=id=>bank.find(q=>q.id===id),ids=Array.from({length:6},(_,i)=>'7.'+(225+i));
test('Värmeöverföring: sex olika självständiga figurer, enkla nivåer och rätt verktyg',()=>{
 const figures=new Set(),types=new Set();for(const id of ids){const p=q(id);assert.equal(bank.filter(q=>q.id===id).length,1,id);assert.equal(p.kap,7);assert.equal(p.omr,'varme');assert.equal(p.familj,'Värmeledning och strålning');assert.equal(p.miniräknare,true);assert.equal(p.geogebra,false);assert.equal(p.spel,true);assert.equal(p.självrättning,true);assert.ok(p.traningsniva<=2);assert.match(p.t,/\((Välj|Svara)/);assert.match(p.t,/<svg/);assert.doesNotMatch(p.t,/använd.*(?:formeln|konstant)|föregående del|svaret ovan/i);assert.doesNotMatch(p.s,/<ol|facit-steglista|[\u0000-\u0008\u000b\u000c\u000e-\u001f]/);assert.ok(p.ledtrad);figures.add(p.t.match(/<svg[\s\S]*?<\/svg>/)[0]);types.add(p.typ);}assert.equal(figures.size,6);assert.equal(types.size,6);assert.equal(bank.filter(q=>q.familj==='Värmeledning och strålning').length,12);
});
test('Avkylningsjämförelsen gäller lika massor, samma ämne och temperatursänkningar',()=>{
 const p=q('7.228');assert.match(p.t,/lika stor massa vatten/);assert.match(p.t,/70 grader/);assert.match(p.t,/40 grader/);assert.match(p.t,/55 grader/);assert.equal(p.rättSvar,(70-40)/(70-55));assert.equal(p.svarFormat,'multipel');assert.equal(p.traningsniva,2);
 // Samma svar fås med vilka lika vattenmassor som helst; temperaturerna i sig ska inte divideras.
 for(const mass of [.1,.5,2])assert.equal(mass*4180*(70-40)/(mass*4180*(70-55)),2);assert.notEqual(p.rättSvar,40/55);
});
test('Reflekterad strålningsenergi är inte samma sak som absorberad energi',()=>{
 const p=q('7.229');assert.equal(p.rättSvar,1200-300);assert.equal(p.svarEnhet,'J');assert.match(p.t,/Ingen strålning passerar genom plattan/);assert.match(p.s,/900 J/);
});
test('Ledning, strömning, strålning och termisk jämvikt skiljs åt med förklarade felalternativ',()=>{
 const answers={'7.225':'Stav A, eftersom aluminium leder värme bättre.','7.226':'Värmeströmning (konvektion)','7.227':'Värmestrålning','7.230':'Ingen av bitarna värmer den andra eftersom temperaturen är lika.'},positions=[];
 for(const[id,answer]of Object.entries(answers)){const p=q(id);assert.equal(p.alternativ.filter(a=>a.ratt).length,1);assert.equal(p.alternativ.find(a=>a.ratt).txt,answer);assert.ok(p.alternativ.every(a=>a.kommentar));positions.push(p.alternativ.findIndex(a=>a.ratt));}assert.equal(new Set(positions).size,4);
 assert.match(q('7.230').s,/samma temperatur/);assert.match(q('7.230').s,/inte ha lika stor inre energi/);assert.match(q('7.227').t,/Inget material förbinder/);
});
