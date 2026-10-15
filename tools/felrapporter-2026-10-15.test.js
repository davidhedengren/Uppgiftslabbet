'use strict';
const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('node:fs'),vm=require('node:vm'),path=require('node:path');
const read=f=>{const c={window:{}};vm.runInNewContext(fs.readFileSync(path.join(__dirname,'..',f),'utf8'),c);return Object.values(c.window).find(Array.isArray);};
const ma2=read('uppgifterma2.js'),mato2=read('uppgiftermato2.js'),fy1=read('uppgifter.js');
test('Quartilfrågan anger jämförelseriktning och Q1/Q3 har ordnade fält före ritjämförelsen',()=>{
 const q=ma2.find(t=>t.id==='4.52');assert.match(q.t,/minst spridning/);assert.equal(q.alternativ.filter(a=>a.ratt).length,1);assert.equal(q.alternativ[0].ratt,true);
 const b=ma2.find(t=>t.id==='4.296').spelDelar[1];
 assert.deepEqual(Array.from(b.svarEtiketter),['Nedre kvartil (Q₁)','Övre kvartil (Q₃)']);assert.deepEqual(Array.from(b.manuellKomplettering),[false,true]);
 const data=[14,12,9,7,6,8,11,12,10,13,15,9].sort((a,b)=>a-b),q1=(data[2]+data[3])/2,q3=(data[8]+data[9])/2;
 assert.deepEqual(Array.from(ma2.find(t=>t.id==='4.296').rättSvar[1]),[q1,q3]);
});
test('Ortslinjecirklar fyller inte cirkelskivan i vare sig huvudfråga eller delkortsintro',()=>{
 for(const id of ['4.06','4.10','4.18','4.21']){
  const q=mato2.find(t=>t.id===id);
  for(const text of [q.t,q.spelIntro,...(q.spelDelar||[]).map(d=>d.t)].filter(Boolean)){
   for(const circle of text.match(/<circle\b[^>]*>/g)||[]){const r=Number(circle.match(/\br="([^"]+)"/)[1]);if(r>10)assert.match(circle,/fill="none"/,id);}
  }
 }
});
test('Båtens hastighetspilar har längderna fem och två rutor med motsatt riktning',()=>{
 const q=fy1.find(t=>t.id==='3.298');assert.match(q.t,/>Båt<\/text>/);
 assert.match(q.t,/<line x1="190" y1="115" x2="340" y2="115"/);
 assert.match(q.t,/<line x1="130" y1="115" x2="70" y2="115"/);
 assert.equal((340-190)/30,5);assert.equal((70-130)/30,-2);assert.equal(q.rättSvar,5-2);
});
