const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('fs'),vm=require('vm'),path=require('path');
const load=f=>{const c={window:{}};vm.runInNewContext(fs.readFileSync(path.join(__dirname,'..',f),'utf8'),c);return Object.values(c.window).find(Array.isArray);};
const ren=h=>String(h||'').replace(/<svg[\s\S]*?<\/svg>/g,'').replace(/<[^>]+>/g,' ');

// Se agent/FLERVAL_BOKSTAVSUPPGIFTER_2026-10-24.md.
const KONTROLL={'uppgifter2.js':['3.145','3.161','4.305','5.301']};
test('Omgjorda bokstavsuppgifter är flervalskort utan hårdkodade alternativ',()=>{
 for(const[f,ids]of Object.entries(KONTROLL)){const b=load(f);
  for(const id of ids){const t=b.find(x=>x.id===id);
   assert.equal(t.svarstyp,'alternativ',id);assert.equal(t.rättSvar,null,id);
   assert.equal(t.alternativ.filter(a=>a.ratt).length,1,id);
   assert.doesNotMatch(ren(t.t),/\bSvara\s+[A-H]\s*,|\bB\s*[.:)]\s/,id);
   const ratt=t.alternativ.find(a=>a.ratt).txt;
   assert.ok(t.s.includes('Svar:')&&t.s.includes(ratt),`${id}: facit ska nämna "${ratt}"`);
  }
 }
});
test('Inga kvarvarande bokstavssvar med alternativ i texten i omgjorda banker, utom handgranskade undantag',()=>{
 const b=load('uppgifter2.js');
 const kvar=b.filter(t=>typeof t.rättSvar==='string'&&/^[A-H]$/.test(t.rättSvar.trim())&&/<p>\s*(?:<strong>)?A(?:<\/strong>)?\s*[.:)]?\s/.test(t.t));
 assert.ok(kvar.length<=14,kvar.map(t=>t.id).join(' '));
});
