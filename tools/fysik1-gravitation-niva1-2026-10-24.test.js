const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('fs'),vm=require('vm'),path=require('path');
const ctx={window:{}};vm.runInNewContext(fs.readFileSync(path.join(__dirname,'../uppgifter.js'),'utf8'),ctx);const q=id=>ctx.window.BANK.find(t=>t.id===id);

// Se agent/PAFYLLNAD_LOGG_2026-10-21.md, runda 68.
const IDS=['4.837','4.838','4.839','4.840','4.841','4.842','4.843','4.844'];
test('Gravitation: åtta nivå 1-kort med figur, svarsruta och självrättning',()=>{
 for(const id of IDS){const t=q(id);
  assert.equal(t.omr,'gravitation',id);assert.equal(t.traningsniva,1,id);assert.match(t.t,/<svg/,id);
  assert.match(t.s,/<p class="facit-svar"><strong>Svar:<\/strong>/,id);assert.doesNotMatch(t.s,/facit-steglista/,id);
  assert.equal(t.självrättning,true,id);
 }
});
test('Gravitation nivå 1: svaren stämmer med egen räkning',()=>{
 const G=6.67e-11;
 assert.ok(Math.abs(G*30*40/0.20**2-q('4.837').rättSvar)<1e-12);
 assert.equal(q('4.838').alternativ.find(a=>a.ratt).txt,'En fjärdedel så stor');
 assert.equal(q('4.839').rättSvar,3*2.0);
 assert.ok(Math.abs(q('4.840').rättSvar-120*1.62)<1e-9);
 assert.ok(Math.abs(q('4.841').rättSvar-250*3.7)<1e-9);assert.match(q('4.841').t,/>3,7</);
 assert.equal(q('4.842').alternativ.find(a=>a.ratt).txt,'A');
 assert.ok(Math.abs(q('4.843').rättSvar-(0.10+0.25+0.15))<1e-12);
 assert.ok(Math.abs(q('4.844').rättSvar-9.82/4)<1e-12);
});
