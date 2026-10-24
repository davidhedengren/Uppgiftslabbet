'use strict';
const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('fs'),vm=require('vm');
const c={window:{}};vm.runInNewContext(fs.readFileSync(__dirname+'/../uppgifter.js','utf8'),c);const bank=Object.values(c.window)[0],q=id=>bank.find(x=>x.id===id);
test('Fysikaliska svar och tecken verifieras oberoende',()=>{
 assert.equal(q('3.440').rättSvar,(8-2)/3);assert.equal(q('3.441').rättSvar,(-2-(-6))/2);
 assert.equal((10-2)/4,(14-6)/4);assert.match(q('3.442').alternativ.find(a=>a.ratt).txt,/lika stor acceleration/); // flervalskort sedan 2026-10-24
 assert.equal(q('3.443').rättSvar,12*4/2);assert.equal(-4+2*q('3.444').rättSvar,0);
 assert.equal(q('3.445').rättSvar,(-1.5-(-3))/3);assert.equal(64+2*q('3.446').rättSvar*12,0);
 assert.equal((3/2+4+2/2)*q('3.447').rättSvar,65);
 const t=q('3.448').rättSvar;assert.ok(t>0);assert.ok(Math.abs(2*t+.5*t*t-(12+4*t))<1e-10);assert.notEqual(t,2);
});
test('Kort har tydliga verktyg, nivå, figur och svarsinstruktion',()=>{
 for(let i=440;i<=448;i++){const x=q('3.'+i);assert.equal(bank.filter(y=>y.id===x.id).length,1);assert.equal(x.miniräknare,true);assert.equal(x.geogebra,false);assert.equal(x.spel,true);assert.equal(x.självrättning,true);assert.ok(x.t.includes('<svg'));assert.ok(x.svarstyp==='alternativ'||x.t.includes('(Svara'));assert.ok(x.ledtrad);}
 assert.equal(q('3.440').traningsniva,1);assert.equal(q('3.444').traningsniva,1);assert.equal(q('3.448').traningsniva,4);
 assert.equal(q('3.446').tolerans,.05);assert.equal(q('3.448').tolerans,.005);
});
