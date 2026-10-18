'use strict';
const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('fs'),vm=require('vm');
const c={window:{}};vm.runInNewContext(fs.readFileSync(__dirname+'/../uppgiftermato1.js','utf8'),c);const bank=JSON.parse(JSON.stringify(c.window.BANKMATO1)),q=id=>bank.find(q=>q.id===id);
test('Definitionsvillkor och uttryck kräver separata svar',()=>{
 for(const [id,bad] of [['1.43',[1,-4]],['1.48',[-1,2]],['1.53',[0,3]]]){assert.deepEqual(q(id).rättSvar[1],bad);assert.equal(q(id).svarsstruktur,'ordnad');}
 const a=q('1.539');assert.equal(a.rättSvar,'C');assert.match(a.s,/inte definierad/);
 assert.equal(q('1.45').svarFormat,'intervall');assert.equal(q('1.45').rättSvar,'x<1 eller x>5');
});
test('Gränstider och kontinuitet kontrolleras matematiskt',()=>{
 const a=12*Math.asin(4/7)/Math.PI,b=12-a,T=t=>18+7*Math.sin(Math.PI*t/12);
 assert.ok(Math.abs(T(a)-22)<1e-12);assert.ok(Math.abs(T(b)-22)<1e-12);assert.ok(T(6)>22&&T(12)<22);
 assert.equal(a.toFixed(2),'2.32');assert.equal(b.toFixed(2),'9.68');assert.match(q('1.272').s,/2\{,\}32/);assert.match(q('1.187').t,/kontinuerliga/);assert.match(q('1.435').t,/miljarder/);
});
test('Faktoriseringens fyra rötter och sekantens gränsvärde',()=>{
 for(const x of q('1.580').rättSvar[1])assert.equal(x**4-5*x*x+4,0);
 for(const h of [-.2,.1,.5])assert.ok(Math.abs((3*(1+h)**2-3)/h-(6+3*h))<1e-10);
 assert.deepEqual(q('1.571').rättSvar,['6+3h',6]);
});
test('Studsfigurer når marken och topphöjderna följer rätt kvot',()=>{
 for(const [id,ratio,n,height]of [['4.179',.6,4,3],['4.229',.8,3,2.5]]){
 const curves=[...q(id).t.matchAll(/Q([\d.]+) (-?[\d.]+) ([\d.]+) (190)/g)];assert.equal(curves.length,n);
 curves.forEach((m,k)=>assert.ok(Math.abs((190-Number(m[2]))/2-150*ratio**(k+1))<.01));
 const distance=height+2*height*Array.from({length:n},(_,k)=>ratio**(k+1)).reduce((a,b)=>a+b,0);assert.ok(Math.abs(q(id).rättSvar-distance)<1e-10);
 }
});
test('Fontänkurvan följer modellen och spegelns hörn ligger på snittlinjen',()=>{
 const points=q('3.377').t.match(/<polyline points="([^"]+)"/)[1].split(' ').map(p=>p.split(',').map(Number));
 for(const [X,Y]of points){const x=(X-50)/32,h=(220-Y)/36;assert.ok(Math.abs(h-(-.25*x*x+2*x+.5))<.001);assert.ok(h>=-.001);}
 assert.match(q('3.390').t,/cy="79.2"/);assert.equal(35+(260-195)*85/125,79.2);
 assert.equal(q('3.390').rättSvar,15/(2*(5/7)));
});
test('Variation i linjär optimering har självständigt kontrollerade svar',()=>{
 assert.equal(q('4.452').rättSvar,(8-2)/2);assert.equal(q('4.454').rättSvar,(4*3+3)-(4*2+6));assert.equal(q('4.458').rättSvar,3-5);
 assert.equal(q('4.453').rättSvar,Math.max(0,2*3,2*5));assert.equal(q('4.455').rättSvar,Math.max(0,5*3,4*6));
 for(const id of ['4.432','4.437','4.444','4.452','4.454','4.458'])assert.doesNotMatch(q(id).t,/<polygon/);
});
test('Verktyg och avrundningskontrakt gäller också blandade delkort',()=>{
 assert.equal(q('4.158').spelDelar[0].miniräknare,false);assert.equal(q('4.158').spelDelar[1].miniräknare,true);
 for(const id of ['4.241','1.272'])assert.ok(q(id).geogebra&&q(id).miniräknare);
 for(const [id,exact,rounded,wrong]of [['3.819',16/3,5.33,5.34],['3.820',4/3,1.33,1.34]]){const t=q(id);assert.equal(t.rättSvar,exact);assert.ok(Math.abs(rounded-exact)<t.tolerans);assert.ok(Math.abs(wrong-exact)>t.tolerans);assert.equal(t.miniräknare,true);}
});
