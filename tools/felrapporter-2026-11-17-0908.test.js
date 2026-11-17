'use strict';
// Felrapporter 2026-11-17 09:08. Logg: agent/FELRAPPORTER_2026-11-17_0908.md
const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('node:fs'),vm=require('node:vm'),path=require('node:path');
function bank(file,key){const c={window:{}};vm.runInNewContext(fs.readFileSync(path.join(__dirname,'..',file),'utf8'),c);return c.window[key];}
const ma1=bank('uppgifterma1.js','BANKMA1'),fy1=bank('uppgifter.js','BANK'),ma2=bank('uppgifterma2.js','BANKMA2');
const q=(b,id)=>{const x=b.find(x=>x.id===id);assert.ok(x,id);return x};

test('Ma1 1.100: talen sätts in direkt i V = lbh, utan basarea',()=>{
 const u=q(ma1,'1.100');
 assert.doesNotMatch(u.s+u.ledtrad,/[Bb]asarea|botten/);
 assert.match(u.s,/facit-steglista/);assert.match(u.s,/facit-rubrik">Sätt in de kända värdena i formeln \\\(V=lbh\\\)/);
 assert.match(u.s,/120=6\\cdot4\\cdot h/);assert.match(u.s,/120=24h/);assert.match(u.s,/\\frac\{120\}\{24\}=5/);
 assert.match(u.s,/Höjden är 5 cm/);assert.equal(u.rättSvar,5);assert.equal(120/(6*4),5);
 assert.match(u.ledtrad,/V=lbh/);
});

test('Uppgifter med en enda del markeras inte med a)',()=>{
 const fall=[[fy1,['2.226','2.227','8.2','9.55','KG-FY1-ALFA-04','9.402']],[ma2,['3.393','3.394','3.395','3.397','3.399','3.400']]];
 for(const [b,ids] of fall)for(const id of ids){
  const u=q(b,id);
  assert.doesNotMatch(u.t,/(^|>|\s)a\)\s/,id);assert.doesNotMatch(u.s,/facit-mark">a\)|<strong>a\)<\/strong>/,id);
  assert.ok(!u.spelDelar||u.spelDelar.length===1,id);
 }
 // Inga nya ensamma a-uppgifter i Fy1 och Ma2 (Ma2 3.2040 har två svar som båda heter a, alltså parametern a).
 for(const b of [fy1,ma2])for(const u of b){
  if(u.id==='3.4')continue; // hänvisning "svaret i a)" i en lista utan bokstäver
  if(/<p>a\) /.test(u.t))assert.match(u.t,/(^|>|\s)b\)/,u.id);
 }
});
