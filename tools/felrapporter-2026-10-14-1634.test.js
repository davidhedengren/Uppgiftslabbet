'use strict';
const {test}=require('node:test'),assert=require('node:assert/strict');
const fs=require('node:fs'),vm=require('node:vm'),path=require('node:path');
const ctx={window:{}};vm.runInNewContext(fs.readFileSync(path.join(__dirname,'../uppgifter.js'),'utf8'),ctx);
const bank=ctx.window.BANK,by=id=>bank.find(t=>t.id===id);
test('Fristående accelerationskort anger en rörelse och ett eget slutvärde',()=>{
 for(const d of by('3.192').spelDelar){assert.match(d.t,/Ett föremål/);assert.doesNotMatch(d.t,/Rörelserna|varje fall/);}
 for(const [i,d] of by('3.197').spelDelar.entries()){
  assert.doesNotMatch(d.t,/vart och ett|slutvärdena/);
  assert.match(d.t,/27,0 m\/s/);assert.match(d.t,/5,0 s/);assert.match(d.t,/Bestäm medelaccelerationen/);
  assert.equal(by('3.197').rättSvar[i],([27,29,23,0,-10][i]-27)/5);
 }
});
test('Biluppgiften anger ordnade punkter och konstant acceleration utan partikelbyte',()=>{
 const q=by('3.386');assert.doesNotMatch(q.t,/Partikeln/);
 for(const i of [0,2]){assert.match(q.spelDelar[i].t,/konstant acceleration/);assert.match(q.spelDelar[i].t,/den ordningen/);assert.doesNotMatch(q.spelDelar[i].t,/Partikeln|annan bil/);}
 assert.ok(Math.abs(q.rättSvar[2]-(29**2-11**2)/(2*((15**2-11**2)/(2*28))))<.005);
 assert.ok(Math.abs(q.rättSvar[3]-(29-11)/((15**2-11**2)/(2*28)))<.005);
 for(const d of q.spelDelar)assert.doesNotMatch(d.ledtrad,/\\\\/);
});
test('Accelerationsgrafens fortsättning avslöjar inte stopptiden genom sin slutpunkt',()=>{
 const q=by('3.143');const stop=7+(3*4)/2;assert.equal(q.rättSvar[2],stop);
 for(const text of [q.t,q.spelIntro,...q.spelDelar.map(d=>d.t)]){
  const svg=text.match(/<svg[\s\S]*?<\/svg>/)[0];
  const dashed=svg.match(/<line[^>]*stroke-dasharray="7 5"[^>]*\/>/)[0];
  const val=k=>Number(dashed.match(new RegExp(k+'="([^"]+)"'))[1]);
  assert.equal(val('y1'),val('y2'));assert.equal(val('x1'),54+432*7/14);
  const endTime=(val('x2')-54)*14/432;assert.ok(endTime>stop);
  assert.match(text,/fortsätter accelerationen att vara konstant/);
 }
});
