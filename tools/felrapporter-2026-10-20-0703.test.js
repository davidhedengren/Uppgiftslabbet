'use strict';
const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('fs'),vm=require('vm');
function bank(n){const c={window:{}};vm.runInNewContext(fs.readFileSync(__dirname+'/../uppgifter'+n+'.js','utf8'),c);return JSON.parse(JSON.stringify(Object.values(c.window)[0]));}
const b=bank('mato2'),q=id=>b.find(q=>q.id===id);
function integral(f,a,b){const n=2000,h=(b-a)/n;let s=f(a)+f(b);for(let j=1;j<n;j++)s+=(j%2?4:2)*f(a+j*h);return s*h/3;}
test('Den varierade rotationsuppgiften använder den nya radien',()=>{
 assert.ok(Math.abs(integral(x=>(x+1)**2,0,2)-26/3)<1e-10);assert.equal(q('3.116').rättSvar[0],'26*pi/3');assert.match(q('3.116').spelDelar[0].fraga,/y=x\+1/);assert.match(q('3.116').spelDelar[0].fraga,/<svg/);assert.equal(q('3.116').spelDelar[0].traningsniva,2);
});
test('Tätheterna är icke-negativa och har total area 1',()=>{
 const cases=[['3.77',x=>3/16*(4-x*x),0,2],['3.450',x=>(1+x)*q('3.450').rättSvar,1,3],['3.508',x=>x*x*q('3.508').rättSvar,1,2]];
 for(const [id,f,a,b]of cases){assert.ok(Math.abs(integral(f,a,b)-1)<1e-10,id);for(let j=0;j<=100;j++)assert.ok(f(a+(b-a)*j/100)>=0);}
 assert.ok(Math.abs(integral(x=>3/16*(4-x*x),.5,1.5)-q('3.77').rättSvar)<1e-10);
});
test('Energin och sannolikheterna lagras före avrundning',()=>{
 const e=integral(t=>2.5+1.2*Math.sin(Math.PI*t/6)+.08*t*t,0,8);assert.ok(Math.abs(e-q('3.245').rättSvar)<1e-10);assert.equal(q('3.245').svarEnhet,'kWh');
 assert.equal(q('3.132').rättSvar[0],1-Math.exp(-1.25));assert.equal(q('3.132').rättSvar[1],Math.exp(-1.5));assert.deepEqual(q('3.132').svarFormat,['sannolikhet','sannolikhet']);assert.deepEqual(q('3.132').tolerans,[null,null]);
});
test('B-kortet för symmetrilinjen spärrar räknare oberoende av huvuduppgiften',()=>{
 const q=bank('ma2').find(q=>q.id==='2.88');assert.equal(q.spelDelar[1].miniräknare,false);assert.equal(q.spelDelar[1].geogebra,false);assert.equal(q.rättSvar[1],2);assert.match(q.spelDelar[1].t,/2\(x-2\)\^2-5/);
});
test('Fem analoga energifrågor har rätt enhet och fullprecisionsmål',()=>{
 for(const [id,power,hours]of [['3.69',600,12],['3.84',600,12],['3.125',600,6],['3.137',1200,6]]){assert.ok(Math.abs(integral(t=>power*Math.sin(Math.PI*t/hours),0,hours)/1000-q(id).rättSvar)<1e-10);assert.equal(q(id).svarEnhet,'kWh');}
 assert.ok(Math.abs(integral(t=>.8*t-.05*t*t,0,8)-q('3.210').rättSvar)<1e-10);assert.equal(q('3.210').svarEnhet,'kWh');
 for(const id of ['3.69','3.84'])assert.equal(q(id).tolerans,.005);
});
