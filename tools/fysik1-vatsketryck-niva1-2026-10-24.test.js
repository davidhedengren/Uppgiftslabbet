const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('fs'),vm=require('vm'),path=require('path');
const ctx={window:{}};vm.runInNewContext(fs.readFileSync(path.join(__dirname,'../uppgifter.js'),'utf8'),ctx);const q=id=>ctx.window.BANK.find(t=>t.id===id);

// Se agent/PAFYLLNAD_LOGG_2026-10-21.md, runda 75.
test('Vätsketryck: åtta nivå 1-kort i alla fyra delmomenten, med figur och svarsruta',()=>{
 const fam=new Set();
 for(let n=557;n<=564;n++){const id='6.'+n,t=q(id);
  assert.equal(t.omr,'vatsketryck',id);assert.equal(t.traningsniva,1,id);assert.match(t.t,/<svg/,id);
  assert.match(t.s,/<p class="facit-svar"><strong>Svar:<\/strong>/,id);assert.doesNotMatch(t.t,/använd[^<]{0,60}g\s*=/i,id);fam.add(t.familj);
 }
 assert.equal(fam.size,4);
});
test('Vätsketryck nivå 1: svaren stämmer med egen räkning',()=>{
 const g=9.82,r=id=>q(id).rättSvar;
 assert.ok(Math.abs(r('6.559')-1000*g*0.40/1000)<1e-12);assert.equal(r('6.560'),101+30);assert.equal(r('6.562'),2.5*100);
 assert.ok(Math.abs(r('6.563')-49000/(1000*g))<1e-12);assert.ok(Math.abs(r('6.564')-1000*g*(5.0-2.0)/1000)<1e-12);
 assert.equal(q('6.557').alternativ.find(a=>a.ratt).txt,'B');
 assert.match(q('6.558').alternativ.find(a=>a.ratt).txt,/Lika stort/);
 assert.match(q('6.561').alternativ.find(a=>a.ratt).txt,/^Högre/);
});
