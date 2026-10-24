const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('fs'),vm=require('vm'),path=require('path');
const load=f=>{const c={window:{}};vm.runInNewContext(fs.readFileSync(path.join(__dirname,'..',f),'utf8'),c);return Object.values(c.window).find(Array.isArray);};
const ren=h=>String(h||'').replace(/<svg[\s\S]*?<\/svg>/g,'').replace(/<[^>]+>/g,' ');

// Se agent/FLERVAL_BOKSTAVSUPPGIFTER_2026-10-24.md.
const KONTROLL={'uppgifter2.js':['3.145','3.161','4.305','5.301','2.301'],'uppgiftermato1.js':['1.401','1.539','3.636'],'uppgiftermato2.js':['1.410','1.401'],'uppgiftermatf1.js':['2.301','2.572']};
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
test('Svarsraden upprepar inte innehållet och börjar inte med skiljetecken',()=>{
 for(const f of Object.keys(KONTROLL))for(const t of load(f).filter(t=>t.svarstyp==='alternativ'&&/facit-svar/.test(t.s||''))){
  const r=(t.s.match(/<p class="facit-svar">([\s\S]*?)<\/p>/)||[])[1]||'';
  assert.doesNotMatch(r,/Svar:\s*(?:<\/strong>)?\s*[,.;:]|\.\.|\.,/,`${f} ${t.id}`);
  const txt=t.alternativ.find(a=>a.ratt).txt.replace(/<[^>]+>/g,'').toLowerCase().replace(/[.\s]+$/,'');
  // "Svar: Infraljud., infraljud." är fel; "Svar: Oförändrat. Magnetfältet är oförändrat." är en förklaring.
  const p=r.replace(/<[^>]+>/g,'').toLowerCase().replace(/^\s*svar:\s*/,''),esc=x=>x.replace(/[.*+?^${}()|[\]\\]/g,'\\$&');
  if(txt.length>3)assert.doesNotMatch(p,new RegExp('^'+esc(txt)+'[.,\\s]+'+esc(txt)),`${f} ${t.id}: dubblerat svar`);
 }
});
