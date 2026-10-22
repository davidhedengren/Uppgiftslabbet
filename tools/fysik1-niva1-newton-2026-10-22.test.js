'use strict';
/* Påfyllnad 2026-10-22: 37 kort på nivå 1 i normalkraft (4.800–4.818) och newton3 (4.819–4.836). Facit räknas om i fysik1-kapitel4.test.js. */
const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('node:fs'),vm=require('node:vm'),path=require('node:path');
const c={window:{}};vm.runInNewContext(fs.readFileSync(path.join(__dirname,'..','uppgifter.js'),'utf8'),c);
const nya=JSON.parse(JSON.stringify(c.window.BANK.filter(t=>{const [k,n]=t.id.split('.').map(Number);return k===4&&n>=800&&n<=836;})));
const utanSvg=h=>h.replace(/<svg[\s\S]*?<\/svg>/g,'');

test('37 kort på nivå 1 i fysikformat utan konstanter i frågan',()=>{
  assert.equal(nya.length,37);const per={};
  for(const t of nya){per[t.omr]=(per[t.omr]||0)+1;
    assert.equal(t.traningsniva,1,t.id);assert.equal(t.miniräknare,true,t.id);assert.equal(t.poang,'(1/0/0)',t.id);
    assert.doesNotMatch(utanSvg(t.t),/9,8|1,62|m\/s²/,t.id);
    if(t.svarstyp==='alternativ')assert.equal(t.alternativ.filter(a=>a.ratt).length,1,t.id);
    else{assert.ok(t.svarEnhet,t.id);assert.ok(t.svarVardesiffror,t.id);assert.match(utanSvg(t.t),/\(Svara i [^)]*\.\)<\/p>$/,t.id);}
  }
  assert.deepEqual(per,{normalkraft:19,newton3:18});
});
