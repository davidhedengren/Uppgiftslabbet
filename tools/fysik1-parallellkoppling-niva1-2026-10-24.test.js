const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('fs'),vm=require('vm'),path=require('path');
const ctx={window:{}};vm.runInNewContext(fs.readFileSync(path.join(__dirname,'../uppgifter.js'),'utf8'),ctx);const q=id=>ctx.window.BANK.find(t=>t.id===id);

// Se agent/PAFYLLNAD_LOGG_2026-10-21.md, runda 78.
test('Parallellkoppling: åtta nivå 1-kort med kretsfigur och svarsruta i båda delmomenten',()=>{
 const fam=new Set();
 for(let n=620;n<=627;n++){const id='8.'+n,t=q(id);
  assert.equal(t.omr,'parallellkoppling',id);assert.equal(t.traningsniva,1,id);assert.match(t.t,/<svg/,id);
  assert.match(t.s,/<p class="facit-svar"><strong>Svar:<\/strong>/,id);fam.add(t.familj);
 }
 assert.equal(fam.size,2);
});
test('Parallellkoppling nivå 1: svaren stämmer med egen räkning',()=>{
 const r=id=>q(id).rättSvar,nara=(a,b)=>assert.ok(Math.abs(a-b)<1e-12,`${a} ${b}`);
 nara(r('8.620'),0.90-0.40);assert.equal(r('8.621'),6.0);nara(r('8.622'),1.2-0.8);
 nara(r('8.624'),1/(1/6+1/3));nara(r('8.626'),9.0/0.30);nara(r('8.627'),1.5/3);
 assert.ok(1/(1/10+1/40)<10);assert.match(q('8.625').alternativ.find(a=>a.ratt).txt,/mindre än 10/);
 assert.match(q('8.623').alternativ.find(a=>a.ratt).txt,/Lika starkt/);
});
