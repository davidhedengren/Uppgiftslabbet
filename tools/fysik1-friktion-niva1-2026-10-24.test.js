const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('fs'),vm=require('vm'),path=require('path');
const ctx={window:{}};vm.runInNewContext(fs.readFileSync(path.join(__dirname,'../uppgifter.js'),'utf8'),ctx);const q=id=>ctx.window.BANK.find(t=>t.id===id);

// Se agent/PAFYLLNAD_LOGG_2026-10-21.md, runda 72. Talsvaren kontrolleras även i fysik1-kapitel4.test.js.
test('Friktion: åtta nivå 1-kort i alla tre delmomenten, med figur och svarsruta',()=>{
 const fam=new Set();
 for(let n=861;n<=868;n++){const id='4.'+n,t=q(id);
  assert.equal(t.omr,'friktion',id);assert.equal(t.traningsniva,1,id);assert.match(t.t,/<svg/,id);
  assert.match(t.s,/<p class="facit-svar"><strong>Svar:<\/strong>/,id);fam.add(t.familj);
 }
 assert.equal(fam.size,3);
 assert.equal(q('4.863').alternativ.find(a=>a.ratt).txt,'A, framåt');
 assert.equal(q('4.868').alternativ.find(a=>a.ratt).txt,'A');
 // 4.864: diagrammets topp vid 45 N följs av glidfriktionen 30 N.
 assert.match(q('4.864').t,/upp till 45 N/);assert.match(q('4.864').s,/30 N/);
});
