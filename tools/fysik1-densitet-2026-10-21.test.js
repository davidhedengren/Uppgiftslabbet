'use strict';
const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('fs'),vm=require('vm');
const c={window:{}};vm.runInNewContext(fs.readFileSync(__dirname+'/../uppgifter.js','utf8'),c);const b=Object.values(c.window)[0],q=id=>b.find(x=>x.id===id);
test('Densitet: oberoende fysikaliska beräkningar',()=>{
 assert.equal(q('2.327').rättSvar??'ABC'[q('2.327').alternativ.findIndex(a=>a.ratt)],['A','B','C'][[25,80,60].indexOf(Math.max(25,80,60))]);
 assert.equal(q('2.328').rättSvar,(330-90)/200);assert.equal(q('2.329').rättSvar,(1/200)/(1/300));
 assert.equal(q('2.330').rättSvar,96/1.2/200*100);assert.equal(q('2.331').alternativ.find(a=>a.ratt).txt,'C');
 assert.deepEqual([27/10,54/20,108/40],[2.7,2.7,2.7]);assert.notEqual(108/30,2.7);
 assert.equal(q('2.332').rättSvar,(500-(700-400))/500*100);
 assert.ok(Math.abs(q('2.333').rättSvar-(1.296-1.200)/1200/.8*1e6)<1e-9);
 assert.equal(q('2.334').rättSvar,48/2.4-48/3);
});
test('Självbärande kort med nivå, figur och verktyg',()=>{
 const ids=Array.from({length:8},(_,i)=>'2.'+(327+i));
 for(const id of ids){const x=q(id);assert.equal(b.filter(q=>q.id===id).length,1);assert.ok(x.t.includes('<svg'));assert.ok(x.svarstyp==='alternativ'||x.t.includes('(Svara')); // bokstavsknappar sedan 2026-10-24
 assert.equal(x.miniräknare,true);assert.equal(x.geogebra,false);assert.equal(x.spel,true);assert.equal(x.självrättning,true);assert.ok(x.ledtrad);}
 assert.equal(q('2.327').traningsniva,1);assert.equal(q('2.333').traningsniva,4);
});
test('Avrundningsfacit lagrar fullvärden och precision för sex äldre uppgifter',()=>{
 const rows=[['2.176',45*19.3/2.7,.5],['2.177',3.4*11.3/8.96,.005],['2.178',86.28/28.32*4*Math.PI*.91**3/3,.005],['2.179',8.96*Math.PI*(1.75**2-1.25**2)*150/1000,.005],['2.190',(89.22-35)/(98.44-35)*.998,.0005],['2.194',80/850000*1e6,.05]];
 for(const[id,value,tolerance]of rows){assert.ok(Math.abs(q(id).rättSvar-value)<1e-10);assert.equal(q(id).tolerans,tolerance);}
});
