const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('fs'),vm=require('vm'),path=require('path');
const ctx={window:{}};vm.runInNewContext(fs.readFileSync(path.join(__dirname,'../uppgifter.js'),'utf8'),ctx);const q=id=>ctx.window.BANK.find(t=>t.id===id);

// Se agent/PAFYLLNAD_LOGG_2026-10-21.md, runda 73. Talsvaren kontrolleras även i fysik1-moment.test.js.
test('Kraftmoment: åtta nivå 1-kort i alla fyra delmomenten, med figur och svarsruta',()=>{
 const fam=new Set();
 for(let n=869;n<=876;n++){const id='4.'+n,t=q(id);
  assert.equal(t.omr,'moment',id);assert.equal(t.traningsniva,1,id);assert.match(t.t,/<svg/,id);
  assert.match(t.s,/<p class="facit-svar"><strong>Svar:<\/strong>/,id);fam.add(t.familj);
 }
 assert.equal(fam.size,4);
 assert.equal(q('4.870').alternativ.find(a=>a.ratt).txt,'C');
 assert.equal(q('4.871').alternativ.find(a=>a.ratt).txt,'Medurs');
 assert.equal(q('4.874').alternativ.find(a=>a.ratt).txt,'C');
 // 4.874: lådan 50 x 100 välter när lutningen passerar atan(50/100) ≈ 26,6°; A 6°, B 15°, C 42°.
 const grans=Math.atan(0.5)*180/Math.PI;assert.ok(6<grans&&15<grans&&42>grans);
});
