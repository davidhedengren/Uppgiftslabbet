'use strict';
// Felrapporter 2026-11-23 13:45: Ma1 5.242, Ma2 2.453, Ma4 1.608 och 1.585. Se agent/FELRAPPORTER_2026-11-23_1345.md.
const {test}=require('node:test');
const assert=require('node:assert/strict');
const fs=require('node:fs'),vm=require('node:vm'),path=require('node:path');
const bank=(fil,v)=>{const c={window:{}};vm.runInNewContext(fs.readFileSync(path.join(__dirname,'..',fil),'utf8'),c);return c.window[v];};
const ma1=bank('uppgifterma1.js','BANKMA1'),ma2=bank('uppgifterma2.js','BANKMA2'),mato2=bank('uppgiftermato2.js','BANKMATO2');
const hit=(B,id)=>B.find(q=>q.id===id);

test('Ma1 5.242: konkret lyckohjul med figur, svaret 3 nya gula fält',()=>{
 const q=hit(ma1,'5.242');
 assert.match(q.t,/Ett fält är gult och de andra fyra är blå/);
 assert.match(q.t,/<svg[^>]*aria-label="Lyckohjul/);
 assert.match(q.t,/Hur många gula fält måste du lägga till/);
 assert.doesNotMatch(q.t,/Du ritar om hjulet|behåller alla fem/);
 // 1 gult av 5; x nya gula ger (1+x)/(5+x) = 1/2
 const x=[...Array(10).keys()].find(x=>2*(1+x)===5+x);
 assert.equal(x,3);assert.equal(q.rättSvar,3);assert.equal(q.svarFormat,'heltal');
 assert.match(q.s,/class="facit-rubrik">Sannolikhet: \\\(P/);
 assert.match(q.s,/Svar: 3 gula fält/);
});

test('Ma2 2.453: nollställena 70 ± √1300 kräver räknare',()=>{
 const q=hit(ma2,'2.453');
 assert.equal(q.miniräknare,true);
 const r=Math.sqrt(70*70-3600);
 assert.deepEqual([...q.rättSvar],[Math.ceil(70-r),Math.floor(70+r)]);
});

test('Ma4: perioder och argument utan gradintervall säger att svaret ska vara i grader',()=>{
 for(const id of ['1.608','1.619','1.622','1.660','2.657','2.684','2.702','2.558','4.482','4.483','4.484','1.585'])
  assert.equal(hit(mato2,id).kgInstruktion,'Svara i grader.',id);
 for(const id of ['1.610','1.611','2.691'])
  assert.equal(hit(mato2,id).kgInstruktion,'Ange perioden i grader.',id);
 assert.equal(hit(mato2,'1.608').rättSvar,180);
 assert.doesNotMatch(hit(mato2,'1.608').t,/Svara/); // instruktionen visas bara i Kunskapsgymmet
});
