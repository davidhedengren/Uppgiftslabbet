'use strict';
const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('node:fs'),vm=require('node:vm');
const c={window:{}};vm.runInNewContext(fs.readFileSync(__dirname+'/../uppgiftermatf1.js','utf8'),c);const bank=Object.values(c.window)[0],q=id=>bank.find(x=>x.id===id);
test('Rapporterade hastigheter kontrolleras mot förändringen av den faktiska storheten',()=>{
 const h=1e-5;
 for(const [id,f]of [['3.248',t=>Math.PI*(10+3*t)**2],['3.261',t=>Math.PI*(60+30*t)**2],['3.263',t=>(3+4*t)**3],['3.66',t=>(8+2*t)*(5+t)],['3.47',t=>-Math.sqrt(100-(6+.5*t)**2)],['3.10',t=>Math.hypot(6*(4+t),18+1.5*(4+t))]]){
  const slope=(f(h)-f(-h))/(2*h);assert.ok(Math.abs(slope-q(id).rättSvar)<Math.max(1e-6,Math.abs(slope)*1e-8),id);
 }
 assert.ok(Math.abs(q('3.113').rättSvar*16*Math.PI-3)<1e-12);
});
test('Nya variationsuppgifters svar löser respektive villkor',()=>{
 assert.equal(q('3.330').rättSvar,2/(1+1));assert.equal(q('3.331').rättSvar,6*2-6);
 assert.equal(1-q('3.332').rättSvar,0);assert.equal(q('3.335').rättSvar+4,1);
 assert.equal(q('3.336').rättSvar,2**4-8*2**2);assert.equal(2*q('3.337').rättSvar,6);
 const x=q('3.338').rättSvar;assert.ok(Math.abs(Math.exp(x)-3*x)<1e-10);assert.ok(x>1);
 assert.equal(1/q('3.339').rättSvar-.5,0);
 assert.equal(q('4.569').rättSvar,3*2);assert.equal(q('4.570').rättSvar,4);assert.equal(q('4.571').rättSvar,2);
 assert.deepEqual(Array.from(q('4.572').rättSvar),[-1,1]);assert.equal(q('4.573').rättSvar,7);
 const [a,b]=q('4.574').rättSvar;assert.equal(1+a+b,0);assert.equal(2+a,0);
 assert.equal(q('4.575').rättSvar**2,25);assert.deepEqual(Array.from(q('4.576').rättSvar),[2,8]);
});
