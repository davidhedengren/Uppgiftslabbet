'use strict';
const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('fs'),vm=require('vm');
const c={window:{}};vm.runInNewContext(fs.readFileSync(__dirname+'/../uppgifter.js','utf8'),c);const bank=Object.values(c.window)[0],q=id=>bank.find(x=>x.id===id);
test('Rörelse: sträcka, förflyttning och tid i varje sammanhang',()=>{
 const values=[(180-100)/40,600/(180+60+240),(50-20)/30,(20+20)/25,(100-40)/(12-6),8/.4,(120+180)/(54/3.6),540/(1/6+1/4)];
 values.forEach((v,i)=>assert.ok(Math.abs(q('2.'+(335+i)).rättSvar-v)<1e-9));
 assert.equal(q('2.342').rättSvar/6+60+q('2.342').rättSvar/4,600);
 assert.equal(q('3.260').rättSvar,50/3.6);assert.equal(q('3.262').rättSvar,650/150);
});
test('Diagrammens punkter motsvarar uppgifternas rörelser',()=>{
 assert.ok(q('2.335').t.includes('0 s: 100 m, 40 s: 180 m'));
 assert.ok(q('2.338').t.includes('0 s: 0 m, 10 s: 20 m, 15 s: 20 m, 25 s: 0 m'));
 for(let i=335;i<=342;i++){const x=q('2.'+i);assert.equal(bank.filter(t=>t.id===x.id).length,1);assert.ok(x.t.includes('<svg'));assert.equal(x.miniräknare,true);assert.equal(x.geogebra,false);assert.equal(x.spel,true);assert.equal(x.självrättning,true);assert.ok(x.t.includes('(Svara'));assert.ok(x.ledtrad);}
});
