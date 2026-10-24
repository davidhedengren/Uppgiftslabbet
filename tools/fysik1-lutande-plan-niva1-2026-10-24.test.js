const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('fs'),vm=require('vm'),path=require('path');
const ctx={window:{}};vm.runInNewContext(fs.readFileSync(path.join(__dirname,'../uppgifter.js'),'utf8'),ctx);const q=id=>ctx.window.BANK.find(t=>t.id===id);

// Se agent/PAFYLLNAD_LOGG_2026-10-21.md, runda 69. Talsvaren kontrolleras även i fysik1-lutande-plan.test.js.
const IDS=['4.845','4.846','4.847','4.848','4.849','4.850','4.851','4.852'];
test('Lutande plan: åtta nivå 1-kort i alla tre delmomenten, med figur och svarsruta',()=>{
 const fam=new Set();
 for(const id of IDS){const t=q(id);
  assert.equal(t.omr,'lutande_plan',id);assert.equal(t.traningsniva,1,id);assert.match(t.t,/<svg/,id);
  assert.match(t.s,/<p class="facit-svar"><strong>Svar:<\/strong>/,id);assert.doesNotMatch(t.s,/facit-steglista/,id);fam.add(t.familj);
 }
 assert.equal(fam.size,3);
 assert.equal(q('4.845').alternativ.find(a=>a.ratt).txt,'A');
 assert.equal(q('4.848').alternativ.find(a=>a.ratt).txt,'Större');
 // Pulkans etikett 36 N ska inte ligga ovanpå vinkelns etikett 18°.
 assert.doesNotMatch(q('4.851').t,/>låda</);
});
