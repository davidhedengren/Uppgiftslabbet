const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('fs'),vm=require('vm'),path=require('path');
const ctx={window:{}};vm.runInNewContext(fs.readFileSync(path.join(__dirname,'../uppgifter.js'),'utf8'),ctx);const q=id=>ctx.window.BANK.find(t=>t.id===id);

// Se agent/PAFYLLNAD_LOGG_2026-10-21.md, runda 74.
test('Medelhastighet: åtta nivå 1-kort med figur eller tabell och svarsruta',()=>{
 const fam=new Set();
 for(let n=343;n<=350;n++){const id='2.'+n,t=q(id);
  assert.equal(t.omr,'medelhastighet',id);assert.equal(t.kap,2,id);assert.equal(t.traningsniva,1,id);assert.match(t.t,/<svg|<table/,id);
  assert.match(t.s,/<p class="facit-svar"><strong>Svar:<\/strong>/,id);assert.doesNotMatch(t.t,/föregående/,id);fam.add(t.familj);
 }
 assert.equal(fam.size,2);
});
test('Medelhastighet nivå 1: svaren stämmer med egen räkning',()=>{
 const r=id=>q(id).rättSvar;
 assert.equal(r('2.343'),(3.0+5.0)/0.50);assert.equal(r('2.344'),16/4);assert.equal(r('2.346'),90/3.6);
 assert.equal(r('2.348'),150/100);assert.equal(r('2.349'),600/120);assert.equal(r('2.350'),30/0.5);
 assert.match(q('2.345').alternativ.find(a=>a.ratt).txt,/medelhastigheten är 0/);assert.equal(400/80,5);
 assert.match(q('2.347').alternativ.find(a=>a.ratt).txt,/just i det ögonblicket/);
});
