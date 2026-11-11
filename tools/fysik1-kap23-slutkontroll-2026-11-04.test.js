'use strict';
const {test}=require('node:test');
const assert=require('node:assert/strict');
const fs=require('node:fs'),path=require('node:path'),vm=require('node:vm');
const root=path.join(__dirname,'..'),ctx={window:{}};
vm.runInNewContext(fs.readFileSync(path.join(root,'uppgifter.js'),'utf8'),ctx);
const areas=['enheter','matnogg','densitet','medelhastighet','konstacc','acceleration','vektorer','st_diagram','vt_diagram','at_diagram'];
const tasks=ctx.window.BANK.filter(q=>areas.includes(q.omr));
const plan=JSON.parse(fs.readFileSync(path.join(__dirname,'fy1-facit-kap23/layout-plan.json'),'utf8'));
const tokens=s=>s.replace(/\\(?:begin|end)\{(?:aligned|gathered)\}/g,'').replace(/\\\\|\\quad|&|\s/g,'');
test('Hela kapitel 2–3: 932 huvudfacit och 734 explicita delfacit har steg och svar',()=>{
 assert.equal(tasks.length,932);
 assert.equal(tasks.reduce((n,q)=>n+(q.spelDelar||[]).length,0),734);
 for(const q of tasks){
  assert.equal(q.miniräknare,true,q.id);
  for(const part of [q,...(q.spelDelar||[])]){
   const id=q.id+(part.etikett||'');
   assert.match(part.s,/class="facit-steglista"/,id);
   assert.match(part.s,/class="facit-rubrik"/,id);
   assert.match(part.s,/class="facit-svar"/,id);
   assert.notEqual(part.miniräknare,false,id);
   // TeX-alignment followed by gt/lt can become an HTML entity before KaTeX runs.
   assert.doesNotMatch(part.s,/&(?:gt|lt)(?:[=;]|\\)/,id);
  }
 }
});
test('93 manuellt utvalda radbrytningar bevarar samtliga matematiska tecken',()=>{
 assert.equal(plan.length,93);
 assert.equal(new Set(plan.map(p=>p.id)).size,77);
 for(const p of plan){
  assert.equal(tokens(p.new),tokens(p.old),p.id);
  const q=tasks.find(q=>q.id===p.id);
  assert.ok([q,...(q.spelDelar||[])].some(part=>part.s.includes(p.new)),p.id);
 }
});
test('3.65: modellantagande före frågorna och fyra tydliga delar',()=>{
 const q=tasks.find(q=>q.id==='3.65');
 assert.ok(q.t.indexOf('Anta att kulan')<q.t.indexOf('<ol'));
 assert.equal((q.t.match(/<li>/g)||[]).length,4);
 assert.equal((q.s.match(/class="facit-del"/g)||[]).length,4);
 assert.match(q.t,/<li>Kan mätpunkterna bevisa/);
});
test('3.388: accelerationen bygger på det exakta resultatet från a)',()=>{
 const q=tasks.find(q=>q.id==='3.388');
 assert.ok(q.s.includes(String.raw`\frac{18-\frac{142}{11}}{11}`));
 assert.ok(Math.abs((18-142/11)/11-56/121)<1e-14);
});
