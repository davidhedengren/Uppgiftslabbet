'use strict';
/* Ma2 kap 3, etapp 8: problemlösning. Radien ska vara märkt på en radie och inte på diagonalen (3.2106, 3.2161).
   Hjulfiguren visar ett helt varv (3.2160), och 3.2052 är inte längre samma fråga som 3.659. */
const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('node:fs'),vm=require('node:vm'),path=require('node:path');
const c={window:{}};vm.runInNewContext(fs.readFileSync(path.join(__dirname,'..','uppgifterma2.js'),'utf8'),c);
const B=JSON.parse(JSON.stringify(c.window.BANKMA2)),get=id=>{const t=B.find(x=>x.id===id);assert.ok(t,id);return t;};
test('Radien går från medelpunkten till ett hörn och är lika lång som cirkelns radie',()=>{
  for(const id of ['3.2106','3.2161']){const s=get(id).t.match(/<svg[\s\S]*?<\/svg>/)[0];
    const [cx,cy,r]=s.match(/<circle cx="([\d.]+)" cy="([\d.]+)" r="([\d.]+)" fill="none"/).slice(1).map(Number);
    const l=s.match(/<line x1="([\d.-]+)" y1="([\d.-]+)" x2="([\d.-]+)" y2="([\d.-]+)"[^>]*stroke-dasharray/).slice(1).map(Number);
    assert.ok(Math.hypot(l[0]-cx,l[1]-cy)<1.5,id);assert.ok(Math.abs(Math.hypot(l[2]-l[0],l[3]-l[1])-r)<1.5,id);}
  assert.match(get('3.2160').t,/ett varv/);assert.doesNotMatch(get('3.2160').t,/halvt varv/);
});
test('3.2052 frågar efter yttervinkelsatsen och har figur och rubriker',()=>{
  const q=get('3.2052');assert.deepEqual(q.alternativ.filter(a=>a.ratt).map(a=>a.txt),['Yttervinkelsatsen']);assert.match(q.t,/<svg/);
  assert.doesNotMatch(q.s,/facit-steglista/);assert.match(q.s,/facit-rubrik/);
});
