'use strict';
const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('fs'),vm=require('vm');
const c={window:{}};vm.runInNewContext(fs.readFileSync(__dirname+'/../uppgiftermato1.js','utf8'),c);
const q=id=>c.window.BANKMATO1.find(q=>q.id===id);
test('Grafavläsningens numeriska svar bevarar grafens stationära punkter',()=>{
  const cases=[['2.85',[-1,1]],['2.90',[-1,1]],['2.95',[-Math.sqrt(2),0,Math.sqrt(2)]],['2.100',[-Math.sqrt(2),0,Math.sqrt(2)]],['2.105',[0,2]],['2.110',[-2,0]],['2.115',[2]],['2.120',[1]]];
  for(const [id,roots] of cases){const t=q(id),actual=[t.rättSvar[0]].flat();assert.equal(actual.length,roots.length);roots.forEach((r,i)=>assert.ok(Math.abs(actual[i]-r)<.001));assert.match(t.s,/tangenten är vågrät/);assert.match(t.s,/visade området/);assert.doesNotMatch(t.s,/f\(x\)=/);}
});
test('Derivatagrafen ger både konkreta intervall och rätt extrema',()=>{
  const t=q('2.380');assert.match(t.s,/x\\lt-1/);assert.match(t.s,/x\\gt1/);assert.match(t.s,/-1\\lt x\\lt1/);
  assert.match(t.s,/x=-1[\s\S]*maximipunkt/);assert.match(t.s,/x=1[\s\S]*minimipunkt/);
  // f′ = x² − 1 är positiv, negativ, positiv runt de två nollställena.
  assert.deepEqual([-2,0,2].map(x=>Math.sign(x*x-1)),[1,-1,1]);
});
test('Den nya resonemangsvarianten är förenlig med ett polynom och kräver motivering',()=>{
  const t=q('3.241');assert.notEqual(t.t,q('2.270').t);assert.equal(t.självrättning,false);
  // f = 3x²/8 − 2x uppfyller samtliga villkor och har minimum vid 8/3.
  const derivative=x=>.75*x-2;assert.equal(derivative(0),-2);assert.equal(derivative(4),1);assert.equal(derivative(8/3),0);
  assert.match(t.s,/kontinuerlig/);assert.match(t.s,/strikt växande/);assert.match(t.s,/exakt en extrempunkt/);assert.match(t.s,/minimipunkt/);
});
