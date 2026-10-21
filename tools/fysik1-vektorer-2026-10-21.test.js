const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('fs'),vm=require('vm');const c={window:{}};vm.runInNewContext(fs.readFileSync(__dirname+'/../uppgifter.js','utf8'),c);const b=Object.values(c.window)[0],q=id=>b.find(x=>x.id===id);
test('Relativ rörelse, förflyttning och vektorskillnad',()=>{
 assert.equal(q('3.461').rättSvar,1.5-.5);
 assert.equal(q('3.462').rättSvar,Math.hypot(60-60,80));
 assert.equal(q('3.463').rättSvar,Math.hypot(0-6,8-0));
 const t=q('3.464').rättSvar;assert.equal((120/t)**2+3**2,5**2);
});
test('Fyra självständiga vektorkort med figurer',()=>{for(let i=461;i<=464;i++){const x=q('3.'+i);assert.equal(b.filter(y=>y.id===x.id).length,1);assert.equal(x.miniräknare,true);assert.equal(x.geogebra,false);assert.ok(x.t.includes('<svg'));assert.equal(x.spel,true);assert.equal(x.självrättning,true);assert.equal(x.omr,'vektorer');}});
