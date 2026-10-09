'use strict';
const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('node:fs'),vm=require('node:vm'),path=require('node:path');
const c={window:{}};vm.runInNewContext(fs.readFileSync(path.join(__dirname,'../uppgifter.js'),'utf8'),c);
const q=id=>c.window.BANK.find(x=>x.id===id),e=1.602e-19;
// Givna data lästa manuellt från frågorna; modellerna läser aldrig facitvärden.
const cases=[
 ['8.78',[.35*45,.35*45/e]],['8.79',[2.2/1.5,2.2*3600/1000]],
 ['8.197',.90*150],['8.199',.60*210],['8.140',[9/370*1000,9/370*150]],
 ['8.465',[90*3600,90/24,(2100/1000)/48]],
 ['8.49',[9/600*1000,[9/600*200,9/600*400],[9,9-9/600*200]]],
 ['8.103',[12/600*1000,[12/600*200,12/600*400],12,12-12/600*200]],
 ['8.117',[(14-12)/20,[14*.1,12*.1,20*.1**2]]],
 ['8.148',[9/900*1000,9-9/900*300,-9/900*300]],
 ['8.149',[12/300*1000,[12/300*100,12/300*200],[12/300*100,-12/300*200]]],
 ['8.143',[400,Math.sqrt(2*e*400/9.11e-31),Math.sqrt(1.67e-27/9.11e-31)]],
 ['8.146',[250,Math.sqrt(2*e*250/9.109e-31),100*9.38e6/2.998e8]],
 ['8.40',[550,11/550*1000,[220*(11/550)**2,330*(11/550)**2],11**2/550]],
 ['8.55',[400,6/400*1000,[6/400*280,6/400*120]]],
 ['8.128',[230/20,230**2/15/20]],
 ['8.131',[500,10/500*1000,[10/500*100,10/500*150,10/500*250],250/500*100]],
 ['8.135',[12/.05,12/.05-150,[150*.05**2,90*.05**2]]],
 ['8.392',10*(3000*3000/(3000+3000))/(2000+3000*3000/(3000+3000))],
 ['8.396',(230/19)**2/((230/20)**2/4.6)],['8.515',2e-6*(10-0)*1e6]
];
function compare(actual,expected,tol,id){
 if(Array.isArray(expected)){expected.forEach((v,i)=>compare(actual[i],v,Array.isArray(tol)?tol[i]:tol,id));return;}
 assert.equal(typeof actual,'number',id);
 assert.ok(Math.abs(actual-expected)<=Math.max(Math.abs(expected)*1e-8,Number(tol)||0),`${id}: ${actual}, modell ${expected}`);
}
test('Ström, kapacitet, potential, spänningsdelning och effekter följer oberoende modeller',()=>{
 for(const [id,expected] of cases){const task=q(id);assert.ok(task,id);compare(task.rättSvar,expected,task.tolerans,id);}
});
test('Batterisymbolen i 8.49 har pluspolen på den sida som uppgiftens potentialer kräver',()=>{
 const task=q('8.49');
 for(const text of [task.t,task.spelIntro]){
  assert.match(text,/x1="255" y1="45" x2="255" y2="75"/);
  assert.match(text,/x1="245" y1="52" x2="245" y2="68"/);
 }
});
test('Tre grundfigurer har ingen ledning genom batteriets två poler',()=>{
 for(const id of ['8.244','8.246','8.248']){
  assert.doesNotMatch(q(id).t,/x1="70" y1="165" x2="70" y2="55"/);
  assert.match(q(id).t,/x1="70" y1="165" x2="70" y2="118"/);
 }
});
