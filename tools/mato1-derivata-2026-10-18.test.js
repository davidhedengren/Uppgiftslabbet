'use strict';
const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('fs'),vm=require('vm');
const c={window:{}};vm.runInNewContext(fs.readFileSync(__dirname+'/../uppgiftermato1.js','utf8'),c);const q=id=>c.window.BANKMATO1.find(q=>q.id===id);
test('Exponentialekvationerna har fullprecisionsmål och korrekt avrundning',()=>{
 for(const [id,a,k,b]of [['2.44',2,.4,7],['2.48',5,.2,12],['2.52',3,.5,20]]){const t=q(id);assert.ok(Math.abs(a*Math.exp(k*t.rättSvar)-b)<1e-12);assert.equal(t.tolerans,.005);assert.match(t.t,/två decimaler/);}
 assert.ok(Math.abs(q('2.08').rättSvar-Math.exp(.4))<1e-12);
 for(const [id,b]of [['2.509',1.05],['2.510',.8],['2.511',1.03],['2.512',.96]]){const t=q(id);assert.ok(Math.abs(Math.exp(t.rättSvar)-b)<1e-12);assert.equal(t.tolerans,.00005);assert.match(t.t,/fyra decimaler/);assert.doesNotMatch(t.ledtrad,/0\{,\}02956|0\{,\}04082/);}
 assert.match(q('2.511').t,/ökar/);assert.match(q('2.512').t,/minskar/);
});
test('Sekantpunkterna ligger på exponentialkurvan och tangentlutningen är samma',()=>{
 const t=q('2.547');assert.ok(Math.abs(2**t.rättSvar*Math.log(2)-7/6)<1e-12);
 const pts=t.t.match(/<polyline points="([^"]+)"/)[1].split(' ').map(p=>p.split(',').map(Number));
 for(const [X,Y]of pts)assert.ok(Math.abs((225-Y)/42-2**((X-130)/65))<.001);
 for(const [X,Y,x,y]of [[65,204,-1,.5],[260,57,2,4]]){assert.equal((X-130)/65,x);assert.equal((225-Y)/42,y);assert.equal(2**x,y);assert.ok(t.t.includes(`cx="${X}" cy="${Y}"`));}
});
test('Tolkning kräver komplettering; tidigare dubblett prövar en annan färdighet',()=>{
 assert.equal(q('2.753').manuellKomplettering,true);assert.equal(q('3.1149').manuellKomplettering,true);
 assert.notEqual(q('2.753').t,q('3.1079').t);assert.equal(-.2*q('3.1079').rättSvar,-3);assert.equal(q('3.1079').svarEnhet,'g');assert.equal(q('3.1079').miniräknare,false);
});
test('Alla 36 delkort har förklaringar och ämnesriktiga ledtrådar',()=>{
 for(const id of ['2.202','2.14','2.18','2.22','2.26','2.207','2.210','2.248','2.301','2.302','2.303','2.304']){
  const t=q(id);assert.equal(t.spelDelar.length,3);for(const p of t.spelDelar){assert.match(p.s,/<p>[^<]{40}/);assert.doesNotMatch(p.ledtrad,/En potensmodell/);assert.ok(t.s.includes(p.s));}
 }
});
