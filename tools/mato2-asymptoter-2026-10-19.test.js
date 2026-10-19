'use strict';
const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('fs'),vm=require('vm');
const c={window:{}};vm.runInNewContext(fs.readFileSync(__dirname+'/../uppgiftermato2.js','utf8'),c);const q=id=>c.window.BANKMATO2.find(q=>q.id===id);
test('Extrempunkterna ligger på originalgraferna och har rätt teckenbyte',()=>{
 for(const [id,f,df]of [['2.264',x=>2*x-1+4/(x+1),x=>2-4/(x+1)**2],['2.267',x=>(x*x+1)/(x-2),x=>1-5/(x-2)**2]]){
  const [x,y,u,v]=q(id).rättSvar[1];assert.ok(Math.abs(f(x)-y)<1e-12);assert.ok(Math.abs(f(u)-v)<1e-12);
  assert.ok(Math.abs(df(x))<1e-12&&Math.abs(df(u))<1e-12);
  assert.ok(df(x-.01)>0&&df(x+.01)<0);assert.ok(df(u-.01)<0&&df(u+.01)>0);
  assert.equal(q(id).spelDelar[1].svarsstruktur,'ordnad');assert.equal(q(id).spelDelar[1].svarEtiketter.length,4);
  assert.ok(q(id).självrättning.every(Boolean));assert.ok(q(id).tolerans[1].every(t=>t===.0005));
 }
});
test('Skissfrågor förblir lärarbedömda och delkort får egna lösningar',()=>{
 for(const id of ['2.14','2.103']){assert.equal(q(id).spel,false);assert.equal(q(id).självrättning,false);}
 assert.equal(q('2.264').rättSvar[2],'nej');assert.ok(1-4*2*3<0);
 assert.match(q('2.267').spelDelar[1].s,/x\+2/);
 assert.doesNotMatch(q('2.264').spelDelar[0].s,/8\{,\}657/);
 assert.equal(q('2.488').rättSvar,'1/e');assert.equal(q('2.486').rättSvar,'nedåt');
});
