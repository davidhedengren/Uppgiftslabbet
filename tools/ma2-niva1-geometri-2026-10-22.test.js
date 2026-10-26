'use strict';
/* Påfyllnad 2026-10-22: 48 kort på träningsnivå 1 i Ma2 kap 3 (3.600–3.647). */
const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('node:fs'),vm=require('node:vm'),path=require('node:path');
const c={window:{}};vm.runInNewContext(fs.readFileSync(path.join(__dirname,'..','uppgifterma2.js'),'utf8'),c);
const bank=c.window.BANKMA2;
const nya=bank.filter(t=>{const n=+t.id.split('.')[1];return t.id.startsWith('3.')&&n>=600&&n<=647;});
const get=id=>nya.find(t=>t.id===id);
const nara=(a,b,tol=1e-9)=>assert.ok(Math.abs(a-b)<=tol,`${a} ≠ ${b}`);

test('48 nya kort på nivå 1, tolv per område, med figur',()=>{
  assert.equal(nya.length,48);
  const per={};for(const t of nya){per[t.omr]=(per[t.omr]||0)+1;
    assert.equal(t.traningsniva,1,t.id);assert.equal(t.niva,'E',t.id);assert.equal(t.spel,true,t.id);assert.equal(t.miniräknare,true,t.id);
    assert.match(t.t,/<svg/,t.id);
    if(t.svarstyp==='alternativ')assert.equal(t.alternativ.filter(a=>a.ratt).length,1,t.id);
    else assert.ok(Number.isFinite(t.rättSvar),t.id);}
  assert.deepEqual(per,{topptriangel_transversal:12,kordasatsen_biskarningssatsen:12,pythagoras:12,likformighet:12});
  assert.equal(new Set(nya.map(t=>t.t.replace(/<svg[\s\S]*?<\/svg>/g,''))).size,48);
});

test('Facit räknas om oberoende',()=>{
  const fall={
    '3.600':18/2,'3.601':1.2/2,'3.602':24/3,'3.604':5/20,'3.605':2/3*2.4,'3.606':7,'3.607':3*3,'3.609':2*4,'3.610':420,'3.611':5.5,
    '3.612':2*6/3,'3.613':4*5,'3.615':36/3,'3.616':2.5*4/2,'3.617':8*18/12,'3.618':20*45/30,'3.620':4*9/6,'3.621':10/2,'3.622':8*3/2,'3.623':30*50/25,
    '3.624':Math.hypot(9,40),'3.625':Math.sqrt(26**2-10**2),'3.628':Math.hypot(7,15),'3.629':Math.hypot(100,64),'3.630':Math.sqrt(50**2-30**2),
    '3.631':Math.hypot(3,4),'3.632':Math.hypot(9.6,0.8),// nya tal 2026-10-26: var samma som 3.2006'3.635':Math.hypot(80,45),
    '3.636':2*5,'3.637':20*21/100,'3.638':15*20/10,'3.639':12/4,'3.640':8*50/100,'3.641':5*6/2,'3.642':3*12,'3.643':16/2,'3.644':18/3*1.5,'3.646':2**2*7};
  for(const [id,v] of Object.entries(fall)){
    const t=get(id);assert.ok(t,id);
    nara(t.rättSvar,v,Math.max(1e-9,t.tolerans||0));
    if(t.tolerans>1e-6)assert.ok(t.tolerans<Math.abs(v)*0.01,id);
  }
});

test('Pythagoras omvändning: rätt alternativ stämmer med sidorna',()=>{
  assert.equal(8**2+15**2,17**2);assert.match(get('3.633').alternativ.find(a=>a.ratt).txt,/^Ja/);
  assert.notEqual(5**2+6**2,8**2);assert.match(get('3.634').alternativ.find(a=>a.ratt).txt,/^Nej/);
});
