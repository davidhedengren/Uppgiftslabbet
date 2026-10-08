'use strict';
const {test}=require('node:test');
const assert=require('node:assert/strict');
const fs=require('node:fs');
const path=require('node:path');
const vm=require('node:vm');
const context={window:{}};
vm.runInNewContext(fs.readFileSync(path.join(__dirname,'../uppgifterma2.js'),'utf8'),context);
const bank=JSON.parse(JSON.stringify(context.window.BANKMA2));
const task=id=>bank.find(q=>q.id===id);

test('Likformighetsuppgifterna har möjliga areor och rätt kvadratisk areaskala',()=>{
  for(const [id,side1,side2,area,scale,answers] of [
    ['3.99',5,6,12,3,[18,108]],
    ['3.162',4,6,8,2.5,[6,50]],
    ['3.164',4,5,6,2.5,[12.5,37.5]],
  ]){
    assert.ok(area<=side1*side2/2,`${id}: arean måste vara geometriskt möjlig`);
    assert.equal(area*scale**2,answers[1]);
    assert.deepEqual(task(id).rättSvar,answers);
    assert.match(task(id).t,new RegExp(`är ${area}([ .<]| areaenheter)`));
  }
});
test('Motexemplet använder två rätvinkliga trianglar med samma area men olika hypotenusor',()=>{
  assert.equal(6*4/2,8*3/2);
  assert.notEqual(Math.hypot(6,4),Math.hypot(8,3));
  assert.match(task('3.427').t,/rätvinkliga/);
  assert.match(task('3.427').s,/sqrt\{52\}/);
  assert.match(task('3.427').s,/sqrt\{73\}/);
});
test('Heltalsavrundningen i pizzauppgiften stämmer med maskinsvaret',()=>{
  const q=task('3.512');
  assert.equal(q.rättSvar,Math.round(120*(40/30)**2));
  assert.ok(Math.abs(214-q.rättSvar)>q.tolerans);
});
test('Introduktionsnivån skiljer givna samband från proportioner i flera steg',()=>{
  assert.equal(task('3.17').traningsniva,1);
  for(const id of ['3.35','3.44','3.102','3.165'])assert.equal(task(id).traningsniva,2,id);
  assert.equal(task('3.43').spelDelar[1].traningsniva,1);
});
test('Bråkens nämnare omfattar hela sträckbeteckningen',()=>{
  for(const id of ['3.395','3.396','3.397','3.398','3.404','3.406','3.409','3.410']){
    const q=task(id);
    for(const s of [q.s,...(q.spelDelar||[]).map(p=>p.s)]){
      assert.doesNotMatch(s,/\\frac\{[A-Z ]+\}\{[A-Z]\}\s*[A-Z]/,id);
    }
  }
});
