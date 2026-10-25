'use strict';
/* Fy1 nivå 3 i tunna områden (2026-10-25, lärarbeslut: fyll inte medicinska metoder, standardmodellen eller strålning möter materia).
   Ett block per område. Kontrollerar nivå, format, facitkrav (metodtext, svarsrad, svarsinstruktion, inga råa < >) och dubblettfacit. */
const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('node:fs'),vm=require('node:vm'),path=require('node:path');
const c={window:{}};vm.runInNewContext(fs.readFileSync(path.join(__dirname,'..','uppgifter.js'),'utf8'),c);
const B=JSON.parse(JSON.stringify(c.window.BANK));const get=id=>{const t=B.find(x=>x.id===id);assert.ok(t,id);return t;};
const OMR={em_stralning:['9.576','9.577','9.578','9.579','9.580','9.581'],enheter:['2.359','2.360','2.361','2.362','2.363','2.364'],tyngdkraft:['4.897','4.898','4.899','4.900','4.901'],falt:['8.661','8.662','8.663','8.664','8.665','8.666'],strom:['8.667','8.668','8.669','8.670','8.671'],parallellkoppling:['8.672','8.673','8.674','8.675','8.676','8.677'],potential:['8.678','8.679','8.680','8.681','8.682','8.683'],sonderfall:['9.582','9.583','9.584','9.585','9.586']};
const v=x=>JSON.stringify(x.rättSvar);
// Lärarbeslut 2026-10-25: naturkonstanter slås upp i formelsamlingen och skrivs inte i frågor eller ledtrådar.
const KONST=/6,6[23]\d*·10|[23],99?8?·10\^?\{?8|3,00·10\^?\{?8|3,00·10⁸|1,602·10|9,1[01]9?·10|8,99·10|6,02·10|931,5|0,511 MeV/;
test('Inga naturkonstanter i frågor eller ledtrådar',()=>{
  for(const id of [...Object.values(OMR).flat(),'9.526','9.527','9.532','9.537','9.539','9.542','8.638','8.650','9.557']){const t=get(id);
    const txt=(t.t+' '+t.ledtrad).replace(/<svg[\s\S]*?<\/svg>/g,'').replace(/\{,\}/g,',').replace(/\\cdot/g,'·').replace(/\s*·\s*/g,'·');
    assert.doesNotMatch(txt,KONST,id);}
  assert.equal(get('9.539').tolerans,1);
});
for(const [omr,ids] of Object.entries(OMR))test(`${omr}: ${ids.length} nivå 3-kort med facitkraven uppfyllda`,()=>{
  for(const id of ids){const t=get(id);assert.equal(t.omr,omr,id);assert.equal(t.traningsniva,3,id);assert.equal(t.niva,'C',id);assert.equal(t.poang,'(0/1/0)',id);assert.equal(t.spel,true,id);
    assert.match(t.s,/class="facit-metod"/,id);assert.match(t.s,/class="facit-svar"/,id);assert.ok(String(t.ledtrad).replace(/<[^>]+>/g,'').trim().length>=15,id);
    for(const m of (t.t+t.s+t.ledtrad).matchAll(/\\\(([\s\S]*?)\\\)|\\\[([\s\S]*?)\\\]/g))assert.doesNotMatch(m[1]??m[2],/[<>]/,id);
    if(t.svarstyp==='alternativ'){assert.equal(t.alternativ.filter(a=>a.ratt).length,1,id);assert.ok(!t.alternativ[0].ratt,id);for(const a of t.alternativ)if(!a.ratt)assert.ok(a.kommentar,id);}
    else{assert.match(t.t,/\(Svara[^)]*\)/,id);const krock=B.filter(w=>w.omr===omr&&w.id!==id&&w.rättSvar!=null&&v(w)===v(t)).map(w=>w.id);assert.deepEqual(krock,[],id);}}
});
