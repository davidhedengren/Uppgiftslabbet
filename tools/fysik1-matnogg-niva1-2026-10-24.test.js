const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('fs'),vm=require('vm'),path=require('path');
const ctx={window:{}};vm.runInNewContext(fs.readFileSync(path.join(__dirname,'../uppgifter.js'),'utf8'),ctx);const q=id=>ctx.window.BANK.find(t=>t.id===id);

// Se agent/PAFYLLNAD_LOGG_2026-10-21.md, runda 77.
test('Mätnoggrannhet: åtta nivå 1-kort med figur och svarsruta i båda delmomenten',()=>{
 const fam=new Set();
 for(let n=351;n<=358;n++){const id='2.'+n,t=q(id);
  assert.equal(t.omr,'matnogg',id);assert.equal(t.traningsniva,1,id);assert.match(t.t,/<svg/,id);
  assert.match(t.s,/<p class="facit-svar"><strong>Svar:<\/strong>/,id);fam.add(t.familj);
 }
 assert.equal(fam.size,2);
});
test('Mätnoggrannhet nivå 1: svaren stämmer med egen räkning',()=>{
 const r=id=>q(id).rättSvar;
 assert.equal(r('2.351'),7.4);assert.ok(Math.abs(r('2.352')-(8.5-2.0))<1e-12);
 assert.ok(Math.abs(r('2.354')-[2.4,2.6,2.5,2.7,2.3].reduce((a,b)=>a+b)/5)<1e-12);
 assert.ok(Math.abs(r('2.356')-0.5/50.0*100)<1e-12);assert.equal(r('2.357'),21.5-0.5);
 assert.match(q('2.353').alternativ.find(a=>a.ratt).txt,/systematiskt/);
 assert.equal(q('2.355').alternativ.find(a=>a.ratt).txt,'4,0 s');assert.equal(q('2.358').alternativ.find(a=>a.ratt).txt,'B');
});
