const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('fs'),vm=require('vm'),path=require('path');
const ctx={window:{}};vm.runInNewContext(fs.readFileSync(path.join(__dirname,'../uppgifter.js'),'utf8'),ctx);const q=id=>ctx.window.BANK.find(t=>t.id===id);

// Se agent/PAFYLLNAD_LOGG_2026-10-21.md, runda 70. Talsvaren kontrolleras även i fysik1-kollisioner.test.js.
const IDS=['5.629','5.630','5.631','5.632','5.633','5.634','5.635','5.636'];
test('Kollisioner: åtta nivå 1-kort i alla tre delmomenten, med figur och svarsruta',()=>{
 const fam=new Set();
 for(const id of IDS){const t=q(id);
  assert.equal(t.omr,'kollisioner',id);assert.equal(t.traningsniva,1,id);assert.match(t.t,/<svg/,id);
  assert.match(t.s,/<p class="facit-svar"><strong>Svar:<\/strong>/,id);assert.doesNotMatch(t.s,/facit-steglista/,id);fam.add(t.familj);
 }
 assert.equal(fam.size,3);
 // 5.630: rörelsemängden 1,0·4,0 fördelas på 2,0 kg.
 assert.equal(1.0*4.0/2.0,2.0);assert.equal(q('5.630').alternativ.find(a=>a.ratt).txt,'2,0 m/s');
 assert.match(q('5.634').alternativ.find(a=>a.ratt).txt,/noll före skottet/);
 // 5.636: 10 J före och 7 J efter, alltså inte elastisk.
 assert.match(q('5.636').t,/>10 J</);assert.match(q('5.636').t,/>7 J</);assert.match(q('5.636').alternativ.find(a=>a.ratt).txt,/^Nej/);
});
