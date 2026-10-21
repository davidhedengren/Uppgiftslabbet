const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('fs'),vm=require('vm');const c={window:{}};vm.runInNewContext(fs.readFileSync(__dirname+'/../uppgifter.js','utf8'),c);const b=Object.values(c.window)[0],q=id=>b.find(x=>x.id===id);
test('Position, vila, möte, förflyttning och tangent',()=>{
 assert.equal(q('3.449').rättSvar,5+5*3);assert.equal(q('3.450').rättSvar,5-2);const t=q('3.451').rättSvar;assert.equal(3*t,20-2*t);assert.equal(q('3.452').rättSvar,(10-(-20))/6);assert.equal(q('3.453').rättSvar,Math.abs(8-0)+Math.abs(-4-8));const h=.00001;assert.ok(Math.abs(q('3.454').rättSvar-(((4+h)**2/2-(4-h)**2/2)/(2*h)))<1e-8);
});
test('Alla nya kort har figurer och rätt verktyg',()=>{for(let i=449;i<=454;i++){const x=q('3.'+i);assert.equal(b.filter(y=>y.id===x.id).length,1);assert.equal(x.miniräknare,true);assert.equal(x.geogebra,false);assert.ok(x.t.includes('<svg'));assert.equal(x.spel,true);assert.equal(x.självrättning,true);}});
