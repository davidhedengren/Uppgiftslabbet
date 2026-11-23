'use strict';
// Felrapporter 2026-11-23 14:31 (AI): minimax som fristående kort i Kunskapsgymmet och 3.79 utan del c.
// Se agent/FELRAPPORTER_2026-11-23_1431.md.
const {test}=require('node:test');
const assert=require('node:assert/strict');
const fs=require('node:fs'),vm=require('node:vm'),path=require('node:path');
const c={window:{}};vm.runInNewContext(fs.readFileSync(path.join(__dirname,'../uppgifterai.js'),'utf8'),c);
const B=c.window.BANKAI;
const strip=h=>(h||'').replace(/<svg[\s\S]*?<\/svg>/g,'').replace(/<[^>]+>/g,' ');

test('Alla minimaxuppgifter med flera delar visas som fristående kort i Kunskapsgymmet',()=>{
 const mm=B.filter(q=>q.omr==='minimax');
 assert.ok(mm.length>=35);
 for(const q of mm){
  if((q.spelDelar||[]).length>=2) assert.equal(q.kgFristaendeDelar,true,q.id);
  // Varje delkort bär sig självt: inledningen finns och frågan hänvisar inte till andra delar.
  for(const d of q.spelDelar||[]){
   assert.ok(d.t||(q.spelIntro&&d.fraga),q.id+d.etikett);
   assert.doesNotMatch(strip(d.fraga)+strip(d.t),/\b[a-e]\)|föregående|i del [a-e]/,q.id+d.etikett);
  }
 }
 assert.equal(B.filter(q=>q.omr!=='minimax'&&q.kgFristaendeDelar).length,0);
 const kg=fs.readFileSync(path.join(__dirname,'../../kunskapsgymmet/index.html'),'utf8');
 assert.match(kg,/foralder\.kgFristaendeDelar===true\) return \[\]/);
});

test('3.79 har bara delarna a och b',()=>{
 const q=B.find(x=>x.id==='3.79');
 assert.equal(q.spelDelar.map(d=>d.etikett).join(''),'ab');
 assert.doesNotMatch(q.t,/<p>c\)|Varför försöker den inte vinna/);
 assert.doesNotMatch(q.s,/facit-mark">c\)/);
 assert.equal(q.rättSvar.length,2);assert.equal(q.svarEtiketter.length,2);
 assert.equal(q.niva,'E');assert.equal(q.poang,'2/0/0');
 assert.equal((q.s.match(/<div/g)||[]).length,(q.s.match(/<\/div>/g)||[]).length);
});
