'use strict';
const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('fs'),vm=require('vm');
const c={window:{}};vm.runInNewContext(fs.readFileSync(__dirname+'/../uppgiftermato2.js','utf8'),c);
const bank=c.window.BANKMATO2;
test('Derivatavärden stämmer med oberoende numerisk differens',()=>{
 for(const [id,f,x] of [['2.417',x=>Math.sin(3*x),0],['2.418',x=>Math.exp(2*x-1),0],['2.419',x=>Math.cos(x*x),1.25331],['2.423',x=>x**3-6*x*x+9*x,1],['2.424',x=>Math.log(x)+x,1],['2.425',x=>Math.PI*x*x,3]]){
  const q=bank.find(q=>q.id===id),h=1e-5,d=(f(x+h)-f(x-h))/(2*h);
  assert.ok(Math.abs(q.rättSvar-d)<1e-7,id);assert.match(q.s,/prime/);assert.doesNotMatch(q.s,/Varför metoden fungerar|Ett korrekt mellanled/);
  assert.equal(q.traningsniva,2);assert.equal(q.miniräknare,true);assert.equal(q.geogebra,false);
 }
});
test('Synlig exponent och angiven precision följs',()=>{
 const q=id=>bank.find(q=>q.id===id);
 assert.ok(q('2.418').t.includes('e^{2x-1}'));
 for(const id of ['2.418','2.419']){assert.match(q(id).t,/tre decimaler/);assert.equal(q(id).tolerans,.0005);}
 assert.equal(q('2.425').tolerans,.005);
 for(const id of ['2.417','2.423','2.424'])assert.equal(q(id).tolerans,0);
});
