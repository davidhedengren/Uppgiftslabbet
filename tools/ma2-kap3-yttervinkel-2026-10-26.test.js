'use strict';
/* Ma2 kap 3, etapp 3: yttervinkelsatsen (lärarbeslut 2026-10-25).
   22 kort hade samma mallfigur, där bågarna alltid var 44°, 86° och 129° oavsett uppgiftens värden. Texterna
   visade dessutom ”(x)” utan LaTeX-avgränsare. Korten har nu skalenliga figurer, varierade texter och facit
   med rubriker. Ledtrådarna i 1.261–2.40 har fått tillbaka sina \( \). */
const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('node:fs'),vm=require('node:vm'),path=require('node:path');
const c={window:{}};vm.runInNewContext(fs.readFileSync(path.join(__dirname,'..','uppgifterma2.js'),'utf8'),c);
const B=JSON.parse(JSON.stringify(c.window.BANKMA2)),get=id=>{const t=B.find(x=>x.id===id);assert.ok(t,id);return t;};
const FORV={'3.127':[49,79,128],'3.154':[52,43,95],'3.156':[35,48,83],'3.181':[75,55,130],'3.182':[28,26,54],'3.197':[45,50,95],'3.198':[40,70,110],'3.271':[61,77,138],
  '3.274':[62,62,124],'3.275':[50,100,150],'3.306':[42,63,105],'3.330':[42,58,100],'3.383':[51,73,124],'3.384':[37,48,85],'3.385':[48,48,96],'3.386':[28,85,67,113],
  '3.387':[33,68,101],'3.388':[58,72,130],'3.389':[48,90,138],'3.390':[42,42,84],'3.391':[67,44,111],'3.392':[45,55,100]};
const bagar=s=>[...s.matchAll(/<path d="M ([\d.-]+) ([\d.-]+) A ([\d.]+) [\d.]+ 0 0 [01] ([\d.-]+) ([\d.-]+)"/g)].map(m=>{const[sx,sy,r,ex,ey]=[1,2,3,4,5].map(i=>+m[i]);return 2*Math.asin(Math.min(1,Math.hypot(ex-sx,ey-sy)/(2*r)))*180/Math.PI;});
test('Bågarna har de storlekar som uppgiften anger',()=>{
  for(const[id,v]of Object.entries(FORV)){const s=get(id).t.match(/<svg[\s\S]*?<\/svg>/)[0],b=bagar(s);assert.equal(b.length,v.length,id);b.forEach((x,i)=>assert.ok(Math.abs(x-v[i])<1.2,`${id}: ${x.toFixed(1)} ≠ ${v[i]}`));}
});
// Kontrollen av LaTeX-avgränsare ligger i latex-avgransare-2026-10-26.test.js (regexarna här hade förstörts av skalet).
test('Svar, nivåer och delning',()=>{
  const svar={'3.181':[30,130],'3.197':[15,45,50,85],'3.386':[85,67],'3.389':[36,138],'3.392':[35,45,55,80],'3.383':73,'3.384':85,'3.385':48,'3.387':68};
  for(const[id,v]of Object.entries(svar))assert.deepEqual(get(id).rättSvar,v,id);
  // Delkort får ha ett givet mellanresultat i frågan (b: x = 30) så att de kan lösas fristående; facit får inte visa andra delars svar.
  assert.equal(get('3.181').spelDelar.length,2);assert.match(get('3.181').spelDelar[1].fraga,/x=30/);assert.ok(!get('3.181').spelDelar[1].s.includes('4x+10=(2x'));
  for(const id of Object.keys(FORV)){const q=get(id),[e,cc,a]=q.poang.split('/').map(Number);assert.equal(q.niva,a?'A':cc?'C':'E',id);
    assert.ok(q.niva==='E'?q.traningsniva<=2:q.niva==='C'?[3,4].includes(q.traningsniva):q.traningsniva>=4,id);}
});
test('Varierade texter och facit med rubriker',()=>{
  const borjan=new Set();
  for(const id of Object.keys(FORV)){const q=get(id),b=q.t.replace(/<[^>]+>/g,'').slice(0,40);assert.ok(!borjan.has(b),`${id}: samma inledning`);borjan.add(b);
    const li=(q.s.match(/<li>/g)||[]).length,r=(q.s.match(/facit-rubrik/g)||[]).length;assert.ok(li>0&&r>=li,id);assert.match(q.s,/facit-svar/,id);}
});
test('Geometriska begrepp: tre dubbletter varierade, med figurer som skiljer begreppen åt',()=>{
  const q291=get('3.291');assert.match(q291.t,/<svg/);assert.deepEqual(q291.alternativ.filter(a=>a.ratt).map(a=>a.txt),['AE']);assert.equal(q291.alternativ[0].ratt,false);
  const q303=get('3.303');assert.deepEqual(q303.alternativ.filter(a=>a.ratt).map(a=>a.txt),['Tangent']);assert.match(q303.t,/<circle/);
  assert.equal(get('3.347').rättSvar,62);const b=bagar(get('3.347').t);assert.ok(Math.abs(b[0]-118)<1&&Math.abs(b[1]-62)<1);
  for(const id of ['3.291','3.303','3.347'])assert.match(get(id).s,/facit-rubrik/,id);
});
