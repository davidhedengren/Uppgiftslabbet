const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('fs'),vm=require('vm'),path=require('path');
const ctx={window:{}};vm.runInNewContext(fs.readFileSync(path.join(__dirname,'../uppgifter.js'),'utf8'),ctx);const q=id=>ctx.window.BANK.find(t=>t.id===id);

// Se agent/PAFYLLNAD_LOGG_2026-10-21.md, runda 76. Talsvaren kontrolleras även i fysik1-kapitel4.test.js.
test('Tyngdkraft: åtta nivå 1-kort med figur och svarsruta',()=>{
 for(let n=877;n<=884;n++){const id='4.'+n,t=q(id);
  assert.equal(t.omr,'tyngdkraft',id);assert.equal(t.traningsniva,1,id);assert.match(t.t,/<svg/,id);
  assert.match(t.s,/<p class="facit-svar"><strong>Svar:<\/strong>/,id);assert.doesNotMatch(t.t,/F_g/,id);
 }
 assert.equal(q('4.877').alternativ.find(a=>a.ratt).txt,'B');
 assert.match(q('4.879').alternativ.find(a=>a.ratt).txt,/1,0 kg/);
 assert.match(q('4.882').alternativ.find(a=>a.ratt).txt,/^Nästan lika stor/);
 // 4.882: (6400/6410)² ≈ 0,997, alltså under en procent mindre.
 assert.ok((6400/6410)**2>0.99);
});
