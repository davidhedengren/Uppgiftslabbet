'use strict';
/* Påfyllnad 2026-10-22: 30 kort på nivå 1 i Fy2 kap 6 (6.320–6.349). */
const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('node:fs'),vm=require('node:vm'),path=require('node:path');
const c={window:{}};vm.runInNewContext(fs.readFileSync(path.join(__dirname,'..','uppgifter2.js'),'utf8'),c);
const nya=c.window.BANK2.filter(t=>{const [k,n]=t.id.split('.').map(Number);return k===6&&n>=320&&n<=349;});
const get=id=>nya.find(t=>t.id===id);
const C=299792458,ME=9.1093837e-31,MP=1.67262192e-27,g=b=>1/Math.sqrt(1-b*b);
const utanSvg=h=>h.replace(/<svg[\s\S]*?<\/svg>/g,'');

test('30 kort på nivå 1 med figur, miniräknare och fysikformat',()=>{
  assert.equal(nya.length,30);const per={};
  for(const t of nya){per[t.omr]=(per[t.omr]||0)+1;
    assert.equal(t.traningsniva,1,t.id);assert.equal(t.miniräknare,true,t.id);assert.match(t.poang,/^\(\d\/\d\/\d\)$/,t.id);assert.match(t.t,/<svg/,t.id);
    // Inga standardkonstanter eller formler i frågan (formelsamlingsregeln 2026-10-12).
    assert.doesNotMatch(utanSvg(t.t),/2,998|299\s?792|9,109|1,67\d|0,511|γ\s*=\s*1\/|\\dfrac\{1\}\{\\sqrt/,t.id);
    if(t.svarstyp==='alternativ')assert.equal(t.alternativ.filter(a=>a.ratt).length,1,t.id);
    if(t.svarVardesiffror!=null){assert.ok(Number.isInteger(t.svarVardesiffror),t.id);assert.ok(t.svarEnhet!==undefined||/gamma|γ/.test(t.t),t.id);
      assert.doesNotMatch(utanSvg(t.t),/decimal|avrund|värdesiffr/i,t.id);}
  }
  assert.deepEqual(per,{tidsdilatation:10,langdkontraktion:10,relativistisk_energi:10});
});

test('Facit räknas om med formelsamlingens konstanter',()=>{
  const fall={'6.320':g(.6),'6.321':g(.8),'6.322':g(.99),'6.323':2.0*g(.6),'6.324':2.2*g(.98),'6.327':g(.9),'6.328':10,'6.329':g(.8),
    '6.330':100/g(.6),'6.331':2/g(.8),'6.332':4.2/g(.9),'6.335':50/2.5,'6.336':15/g(.995),'6.337':300/g(.5),'6.338':100/g(.6),
    '6.340':1e-3*C*C,'6.341':2*C*C,'6.342':4.5e16/C/C,'6.343':g(.8)*MP*C*C,'6.344':(g(.6)-1)*ME*C*C,'6.346':3,'6.348':0.9e-3*C*C,'6.349':0.511};
  for(const [id,v] of Object.entries(fall)){const t=get(id);assert.ok(t,id);assert.ok(Math.abs(t.rättSvar-v)<=Math.abs(v)*1e-6+(id==='6.327'?0:1e-12),`${id}: ${t.rättSvar} ≠ ${v}`);}
});
