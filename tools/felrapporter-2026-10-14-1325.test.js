'use strict';
const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('node:fs'),vm=require('node:vm'),path=require('node:path');
function bank(file){const c={window:{}};vm.runInNewContext(fs.readFileSync(path.join(__dirname,'..',file),'utf8'),c);return new Map(Object.values(c.window).find(Array.isArray).map(q=>[q.id,q]));}
const fy1=bank('uppgifter.js'),ma1=bank('uppgifterma1.js'),ma2=bank('uppgifterma2.js'),ma4=bank('uppgiftermato2.js'),ma5=bank('uppgiftermatf1.js');
test('Planetmassan efterfrågas och följer gravitationslagen med tidigare precision',()=>{
 const q=fy1.get('4.364'),mass=6.6*(3e6)**2/6.674e-11;
 assert.match(q.t,/Bestäm planetens massa/);assert.doesNotMatch(q.t,/Använd|G\s*=/);
 assert.ok(Math.abs(q.rättSvar-mass)<mass*1e-14);assert.ok(Math.abs(8.9e23-mass)<=q.tolerans);
 assert.equal(q.svarEnhet,'kg');assert.equal(q.miniräknare,true);
});
test('Parentesernas gruppering ger samma oberoende aritmetiska resultat',()=>{
 for(const[id,value]of [['0.265',2*(3+(8-5))],['0.266',36/(2*(3+3))],['0.282',3*(8-2*(5-3))]]){
  assert.equal(ma1.get(id).rättSvar,value);assert.match(ma1.get(id).t,/\\cdot/);
 }
});
test('Koordinater är ordnade också när punkten är ett separat delkort',()=>{
 for(const[id,value]of [['3.341',[(-3+7)/2,(8+2)/2]]/* nya tal 2026-10-26: var en dubblett av 3.263 */,['3.134',[2*2-(-3),2*1-5]]]){
  const q=ma2.get(id);assert.deepEqual(Array.from(q.rättSvar),value);assert.equal(q.svarsstruktur,'ordnad');assert.equal(q.svarEtiketter.length,2);
 }
 const q=ma2.get('3.201');assert.deepEqual(Array.from(q.rättSvar[0]),[2*2-7,2*5-(-1)]);assert.equal(q.spelDelar[0].svarEtiketter.length,2);
 assert.match(q.spelDelar[1].s,/MB=/); // delen kan använda givna M och B direkt
});
test('Amplitud, period och medellinje har en ledtråd om varje efterfrågad egenskap',()=>{
 const q=ma4.get('1.611');assert.deepEqual(Array.from(q.rättSvar),[Math.abs(-2),360/.5,1]);
 for(const word of ['Amplitud','Period','Medellinje'])assert.ok(q.ledtrad.includes(word));
});
test('Återläggning och ordnade drag ger rätt sannolikheter utan ändrade facit',()=>{
 const q=ma5.get('1.680');const expected=[5/9*5/9,5/9*4/8,5/9*4/8];
 q.rättSvar.forEach((answer,i)=>{const[n,d]=answer.split('/').map(Number);assert.ok(Math.abs(n/d-expected[i])<1e-14);});
 assert.ok(q.spelDelar[0].t.includes('läggs tillbaka'));assert.ok(q.spelDelar[1].t.includes('läggs inte tillbaka'));
});
