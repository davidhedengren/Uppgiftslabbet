'use strict';
/* Fy1 nivå 3 i tunna områden (2026-10-25, lärarbeslut: fyll inte medicinska metoder, standardmodellen eller strålning möter materia).
   Ett block per område. Kontrollerar nivå, format, facitkrav (metodtext, svarsrad, svarsinstruktion, inga råa < >) och dubblettfacit. */
const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('node:fs'),vm=require('node:vm'),path=require('node:path');
const c={window:{}};vm.runInNewContext(fs.readFileSync(path.join(__dirname,'..','uppgifter.js'),'utf8'),c);
const B=JSON.parse(JSON.stringify(c.window.BANK));const get=id=>{const t=B.find(x=>x.id===id);assert.ok(t,id);return t;};
const OMR={em_stralning:['9.576','9.577','9.578','9.579','9.580','9.581']};
const v=x=>JSON.stringify(x.rättSvar);
for(const [omr,ids] of Object.entries(OMR))test(`${omr}: ${ids.length} nivå 3-kort med facitkraven uppfyllda`,()=>{
  for(const id of ids){const t=get(id);assert.equal(t.omr,omr,id);assert.equal(t.traningsniva,3,id);assert.equal(t.niva,'C',id);assert.equal(t.poang,'(0/1/0)',id);assert.equal(t.spel,true,id);
    assert.match(t.s,/class="facit-metod"/,id);assert.match(t.s,/class="facit-svar"/,id);assert.ok(String(t.ledtrad).replace(/<[^>]+>/g,'').trim().length>=15,id);
    for(const m of (t.t+t.s+t.ledtrad).matchAll(/\\\(([\s\S]*?)\\\)|\\\[([\s\S]*?)\\\]/g))assert.doesNotMatch(m[1]??m[2],/[<>]/,id);
    if(t.svarstyp==='alternativ'){assert.equal(t.alternativ.filter(a=>a.ratt).length,1,id);assert.ok(!t.alternativ[0].ratt,id);for(const a of t.alternativ)if(!a.ratt)assert.ok(a.kommentar,id);}
    else{assert.match(t.t,/\(Svara[^)]*\)/,id);const krock=B.filter(w=>w.omr===omr&&w.id!==id&&w.rättSvar!=null&&v(w)===v(t)).map(w=>w.id);assert.deepEqual(krock,[],id);}}
});
