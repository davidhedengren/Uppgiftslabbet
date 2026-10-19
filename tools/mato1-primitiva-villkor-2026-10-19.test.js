'use strict';
const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('fs'),vm=require('vm');
const c={window:{}};vm.runInNewContext(fs.readFileSync(__dirname+'/../uppgiftermato1.js','utf8'),c);const q=id=>c.window.BANKMATO1.find(q=>q.id===id);
test('Kubikens minimum är lokalt och integrationen uppfyller villkoret',()=>{
 const t=q('3.313');assert.match(t.t,/lokala minimivärdet/);const F=x=>x**3-3*x*x+3,dF=x=>3*x*x-6*x;
 assert.equal(F(2),-1);assert.equal(dF(2),0);assert.ok(dF(1)<0&&dF(3)>0);assert.ok(F(-10)<F(2));assert.match(q('3.220').t,/lokala maximi- och minimivärdet/);
});
test('Rörelse och inflöde använder startvillkoret och rätt enhet',()=>{
 assert.match(q('3.898').t,/bort från/);assert.match(q('3.898').t,/sekunder/);assert.equal(q('3.898').rättSvar,2+3*3**2);assert.equal(q('3.898').svarEnhet,'m');
 assert.equal(q('3.899').rättSvar,10+2*3**2);assert.match(q('3.899').t,/minuter från start/);
 assert.equal(q('3.944').rättSvar,29-3**2);assert.match(q('3.944').t,/fanns från början/);assert.equal(q('3.944').svarEnhet,'liter');
});
test('Avrundning och exakt tangentvillkor har olika svarskontrakt',()=>{
 const t=q('3.1011');assert.equal(t.rättSvar,Math.E+3);assert.equal(t.tolerans,.005);assert.ok(Math.abs(t.rättSvar-5.72)<t.tolerans);assert.ok(Math.abs(t.rättSvar-5.71)>t.tolerans);assert.ok(Math.abs(t.rättSvar-5.73)>t.tolerans);
 const tang=q('3.1147');assert.equal(tang.svarFormat,'uttryck');assert.equal(tang.rättSvar,'4/3');assert.equal(tang.tolerans,null);assert.ok(Math.abs(3*(2/3)**2-4*(2/3)+4/3)<1e-12);assert.equal(6*(2/3)-4,0);
});
test('Tidigare variationssvar och uttrycksrättning bevaras',()=>{
 assert.equal(q('3.1074').rättSvar,6);for(const id of ['3.22','3.28','3.34','3.154','3.166','3.310','3.354']){assert.equal(q(id).svarFormat,'uttryck');assert.match(q(id).ledtrad,/Sätt sedan in villkoret/);assert.equal(q(id).miniräknare,true);assert.equal(q(id).geogebra,false);}
 assert.doesNotMatch(q('3.186').ledtrad,/x\^n|potens/);
});
