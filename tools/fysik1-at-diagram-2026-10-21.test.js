const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('fs'),vm=require('vm');const c={window:{}};vm.runInNewContext(fs.readFileSync(__dirname+'/../uppgifter.js','utf8'),c);const b=Object.values(c.window)[0],q=id=>b.find(x=>x.id===id);
test('Acceleration, riktningsbyte och integrerad rörelse',()=>{
 assert.equal(q('3.455').rättSvar,-2);
 assert.equal(q('3.456').rättSvar,(2+2*2)*(5-2));
 assert.equal(-6+2*q('3.457').rättSvar,0);
 assert.equal(q('3.458').rättSvar,Math.max(3,3+2*4,3+2*4-4*2));
 assert.equal(q('3.459').rättSvar,1+4*4/2);
 // Oberoende numerisk integration av två accelerationer; mittpunktsmetod.
 let v=2,x=0,dt=.001;for(let i=0;i<6000;i++){const a=i<3000?2:-1;x+=(v+a*dt/2)*dt;v+=a*dt;}
 assert.ok(Math.abs(q('3.460').rättSvar-x)<1e-8);assert.ok(v>0);
});
test('Självständiga kort med figurer och miniräknare',()=>{for(let i=455;i<=460;i++){const x=q('3.'+i);assert.equal(b.filter(y=>y.id===x.id).length,1);assert.equal(x.miniräknare,true);assert.equal(x.geogebra,false);assert.ok(x.t.includes('<svg'));assert.equal(x.spel,true);assert.equal(x.självrättning,true);assert.equal(x.omr,'at_diagram');}});
