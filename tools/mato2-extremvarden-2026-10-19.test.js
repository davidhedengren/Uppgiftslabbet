'use strict';
const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('fs'),vm=require('vm');
const c={window:{}};vm.runInNewContext(fs.readFileSync(__dirname+'/../uppgiftermato2.js','utf8'),c);const q=id=>c.window.BANKMATO2.find(q=>q.id===id);
test('Skärningarnas fullprecisionsvärden löser originalekvationerna',()=>{
 for(const [id,part,f,target] of [['2.265',2,x=>Math.log(x-1)+2/(x-1),2],['2.266',1,x=>Math.exp(-x)+x/2,1],['2.268',1,x=>3*x+2+2/(x-1)**2,10]]){
  for(const x of q(id).rättSvar[part])assert.ok(Math.abs(f(x)-target)<1e-12,id);
  assert.equal(q(id).spelDelar[part].svarsstruktur,'mängd');
  assert.ok(q(id).tolerans[part].every(x=>x===.0005));
 }
});
test('Minimivärden och derivatans tecken stämmer',()=>{
 const cases=[['2.265',3,x=>Math.log(x-1)+2/(x-1),x=>(x-3)/(x-1)**2,1],['2.268',1+Math.cbrt(4/3),x=>3*x+2+2/(x-1)**2,x=>3-4/(x-1)**3,0]];
 for(const [id,x,f,df,part] of cases){assert.ok(Math.abs(df(x))<1e-12);assert.ok(df(x-.01)<0&&df(x+.01)>0);assert.ok(Math.abs(f(x)-q(id).rättSvar[part])<1e-12);}
 assert.equal(q('2.266').rättSvar[0][0],Math.log(2));assert.equal(q('2.266').rättSvar[0][1],(1+Math.log(2))/2);
 assert.deepEqual(Array.from(q('2.266').spelDelar[0].svarEtiketter),['x','y']);assert.equal(q('2.266').spelDelar[0].svarsstruktur,'ordnad');
 for(const id of ['2.571','2.582']){assert.equal(q(id).miniräknare,true);assert.equal(q(id).geogebra,false);assert.equal(q(id).traningsniva,3);}
});
