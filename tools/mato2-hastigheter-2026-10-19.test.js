'use strict';
const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('fs'),vm=require('vm');
const c={window:{}};vm.runInNewContext(fs.readFileSync(__dirname+'/../uppgiftermato2.js','utf8'),c);const q=id=>c.window.BANKMATO2.find(q=>q.id===id);
test('Volymökning och tid räknas med samma fullständiga modell',()=>{
 const r=10,h=1e-5,V=r=>4*Math.PI*r**3/3;
 assert.ok(Math.abs((V(r+h)-V(r-h))/(2*h)*.4-q('2.125').rättSvar[0])<1e-6);
 assert.equal(V(15)/q('2.125').rättSvar[0],q('2.125').rättSvar[1]);
 assert.equal(q('2.125').svarFormat[0],'numeriskt');
 assert.match(q('2.125').spelDelar[1].t,/160\\pi/);
 assert.doesNotMatch(q('2.125').spelDelar[1].t,/0,40|radien 10/);
 assert.equal(q('2.125').spelDelar[1].traningsniva,2);
});
test('Area- och radiehastighet har egna enheter och kompletta lösningar',()=>{
 assert.deepEqual(Array.from(q('2.184').svarEnhet),['m','m/s']);
 assert.equal(q('2.184').rättSvar[0],2*3);
 assert.equal(q('2.184').rättSvar[1],1.8/(2*3));
 assert.doesNotMatch(q('2.184').s,/parabel|nollställ|faktorform/);
 assert.equal(q('2.212').rättSvar,80*Math.PI/(2*Math.PI*10*4));
 assert.equal(q('2.212').svarEnhet,'cm/s');
 for(const id of ['2.125','2.184','2.212']){assert.equal(q(id).miniräknare,true);assert.equal(q(id).geogebra,false);}
});
