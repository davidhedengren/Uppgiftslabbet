'use strict';
/* Påfyllnad 2026-10-22: 20 kort på nivå 1 i at_diagram (3.600–3.619). Facit räknas om i fysik1-kapitel3.test.js. */
const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('node:fs'),vm=require('node:vm'),path=require('node:path');
const c={window:{}};vm.runInNewContext(fs.readFileSync(path.join(__dirname,'..','uppgifter.js'),'utf8'),c);
const nya=JSON.parse(JSON.stringify(c.window.BANK.filter(t=>{const [k,n]=t.id.split('.').map(Number);return k===3&&n>=600&&n<=619;})));
const utanSvg=h=>h.replace(/<svg[\s\S]*?<\/svg>/g,'');

test('20 at-diagramkort på nivå 1 i fysikformat',()=>{
  assert.equal(nya.length,20);
  for(const t of nya){
    assert.equal(t.omr,'at_diagram',t.id);assert.equal(t.traningsniva,1,t.id);assert.equal(t.miniräknare,true,t.id);assert.equal(t.poang,'(1/0/0)',t.id);
    assert.doesNotMatch(t.t,/[Ss]amma .* som ovan/,t.id);
    if(t.svarstyp==='alternativ')assert.equal(t.alternativ.filter(a=>a.ratt).length,1,t.id);
    else{assert.ok(t.svarEnhet,t.id);assert.ok(/\(Svara i [^)]*\.\)<\/p>$/.test(utanSvg(t.t))||t.svarEnhet,t.id);}
  }
  assert.ok(nya.filter(t=>/<svg/.test(t.t)).length>=18);
});
