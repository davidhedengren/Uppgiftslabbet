'use strict';
const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('fs'),vm=require('vm');
const bank=f=>{const c={window:{}};vm.runInNewContext(fs.readFileSync(__dirname+'/../'+f,'utf8'),c);return Object.values(c.window)[0];};
const phy=bank('uppgifter.js'),mat=bank('uppgiftermatf1.js'),q=id=>phy.find(q=>q.id===id);
test('Fullständiga beräkningsvärden och kopplingsscheman',()=>{
 assert.equal(q('3.165').rättSvar[0],9.82*2.5**2/2);assert.equal(q('3.221').rättSvar[1],7/9.82);assert.equal(q('3.222').rättSvar,10/3);
 for(const[id,answer] of [['8.382','A'],['8.383','B']]){assert.equal(q(id).alternativ.find(a=>a.ratt).txt,answer);assert.equal((q(id).t.match(/<svg/g)||[]).length,3);assert.equal(q(id).svarstyp,'alternativ');} // bokstavsknappar sedan 2026-10-24
 assert.equal(mat.find(q=>q.id==='3.309').miniräknare,true);
});
test('Sex varierade enhetsuppgifter: beräkning, verktyg och figur',()=>{
 const answers=[75e-6,1.2*.8,3.6*1000/60,120/.15,35*.012*1000,1200];
 answers.forEach((v,i)=>{const x=q('2.'+(321+i));assert.ok(Math.abs(x.rättSvar-v)<1e-10);assert.equal(x.miniräknare,true);assert.equal(x.geogebra,false);assert.ok(x.t.includes('<svg'));assert.ok(x.t.includes('(Svara'));});
});
test('Omformatering bevarar samtliga ord, tal och matematiska tecken',()=>{
 const r=JSON.parse(fs.readFileSync(__dirname+'/../agent/FYSIK_SVARSINSTRUKTIONER_2026-10-21.json'));
 const tokens=s=>(s.replace(/<[^>]*>/g,' ').match(/[\p{L}\p{N}_]+|[−+*/=<>²³µ]/gu)||[]).sort();
 for(const x of r)assert.deepEqual(tokens(x.before),tokens(x.after),x.bank+' '+x.id+' '+x.field);
});
