const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('fs'),vm=require('vm'),path=require('path');
const ctx={window:{}};vm.runInNewContext(fs.readFileSync(path.join(__dirname,'../uppgifter.js'),'utf8'),ctx);const q=id=>ctx.window.BANK.find(t=>t.id===id);

// Se agent/PAFYLLNAD_LOGG_2026-10-21.md, runda 71. Talsvaren kontrolleras även i fysik1-kapitel4.test.js.
test('Fjädrar: åtta nivå 1-kort i alla tre delmomenten, med figur och svarsruta',()=>{
 const fam=new Set();
 for(let n=853;n<=860;n++){const id='4.'+n,t=q(id);
  assert.equal(t.omr,'fjadrar',id);assert.equal(t.traningsniva,1,id);assert.match(t.t,/<svg/,id);
  assert.match(t.s,/<p class="facit-svar"><strong>Svar:<\/strong>/,id);fam.add(t.familj);
 }
 assert.equal(fam.size,3);
 assert.match(q('4.856').alternativ.find(a=>a.ratt).txt,/vänster/);
 assert.equal(q('4.857').alternativ.find(a=>a.ratt).txt,'Fjäder A');
 // 4.859: 5,0 cm ska räknas om till meter.
 assert.match(q('4.859').s,/0\{,\}050/);
});
