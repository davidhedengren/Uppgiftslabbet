const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('fs'),vm=require('vm'),path=require('path');
const ctx={window:{}};vm.runInNewContext(fs.readFileSync(path.join(__dirname,'../uppgifter.js'),'utf8'),ctx);const q=id=>ctx.window.BANK.find(t=>t.id===id);

// Se agent/PAFYLLNAD_LOGG_2026-10-21.md, runda 79. Avläsning och tolkning i stället för fler uttagsfrågor.
test('Multimeter: åtta nivå 1-kort om avläsning, med figur och svarsruta',()=>{
 let tal=0;
 for(let n=628;n<=635;n++){const id='8.'+n,t=q(id);
  assert.equal(t.omr,'multimeter',id);assert.equal(t.traningsniva,1,id);assert.match(t.t,/<svg/,id);
  assert.match(t.s,/<p class="facit-svar"><strong>Svar:<\/strong>/,id);if(t.svarstyp==='numeriskt')tal++;
 }
 assert.ok(tal>=5,'mest talsvar, inte bara flerval');
});
test('Multimeter nivå 1: svaren stämmer med egen räkning',()=>{
 const r=id=>q(id).rättSvar,nara=(a,b)=>assert.ok(Math.abs(a-b)<1e-9,`${a} ${b}`);
 nara(r('8.628'),0.235*1000);nara(r('8.629'),4.70*1000);nara(r('8.630'),0.01);
 nara(r('8.632'),6+2*0.2);assert.match(q('8.632').t,/fem smådelar/);
 nara(r('8.634'),6.0-2.5);nara(r('8.635'),0.20);
 assert.match(q('8.631').alternativ.find(a=>a.ratt).txt,/för stor/);assert.match(q('8.633').alternativ.find(a=>a.ratt).txt,/hel/);
});
