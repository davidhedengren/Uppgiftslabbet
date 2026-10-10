'use strict';
const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('node:fs'),vm=require('node:vm'),path=require('node:path');
const c={window:{}};vm.runInNewContext(fs.readFileSync(path.join(__dirname,'../uppgifter.js'),'utf8'),c);
const q=id=>c.window.BANK.find(q=>q.id===id),k=8.99e9;
test('Coulomb, laddningsutjämning och fält räknas från givna data',()=>{
 const cases=[
  ['8.21',1,k*4e-9*6e-9/.03**2*1000],['8.21',2,k*4e-9*6e-9/.06**2*1000],
  ['8.23',1,k*5e-9*5e-9/.04**2],['8.57',1,k*4e-9*6e-9/.05**2],
  ['8.67',0,(12-4)/2],['8.68',1,2*k*(6e-9)**2/.05**2*1e6],
  ['8.70',null,Math.sqrt(k*3e-9*4e-9/.0045)*1000],
  ['8.71',1,k*5e-9*3e-9/.04**2-k*5e-9*3e-9/.04**2],
  ['8.72',0,k*6e-9*9e-9/.03**2],['8.72',1,k*6e-9*9e-9/.06**2],['8.72',2,k*12e-9*18e-9/.03**2],
  ['8.74',1,k*5e-9*8e-9/.04**2],['8.321',null,.040/2e-6],['8.322',null,3e-6*4000],
  ['8.323',null,.028/6500*1e6],['8.326',null,.075/2.5e-6],['8.327',null,1.602e-19*2500],
  ['8.328',null,.050/16000*1e6],['8.329',null,3500*.080],['8.330',null,1.602e-19*2.5e6],['8.331',null,6e-9*1.2e5]
 ];
 for(const[id,index,value]of cases){
  const actual=index===null?q(id).rättSvar:q(id).rättSvar[index];
  assert.ok(Math.abs(actual-value)<=Math.max(Math.abs(value)*1e-10,1e-28),id);
 }
});
test('Symmetrikortets slutsvar gäller kraftsumman, inte en grannes kraft',()=>{
 const b=q('8.71').spelDelar[1];assert.match(b.s,/0\\,\\mathrm N/);
 assert.doesNotMatch(b.s,/84/);assert.equal(q('8.71').svarEnhet[1],'N');
 assert.equal(q('8.71').tolerans[1],0);
});
test('Förändringskort har egna givna startvärden och entydigt utgångsläge',()=>{
 for(const id of ['8.21','8.72'])for(const part of q(id).spelDelar.filter(p=>['b','c'].includes(p.etikett)&&p.t))
  assert.match(part.t,/Kraften mellan två/);
 assert.match(q('8.72').spelDelar[2].t,/Avståndet ändras inte/);
 assert.match(q('8.72').t,/ursprungliga/);
 assert.equal(q('8.21').spelDelar.length,3);assert.match(q('8.21').t,/d\)/);
 assert.match(q('8.21').s,/<strong>d\)/);
});
