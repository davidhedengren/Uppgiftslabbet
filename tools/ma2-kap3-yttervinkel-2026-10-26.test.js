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
test('Ingen matematik utan LaTeX-avgränsare i Ma2',()=>{
  const re=/(^|[^\A-Za-zåäöÅÄÖ0-9_^{])\(([a-z](?:[′']|_\d)?)\)/,ENH=new Set(['m','s','h','g','l']);
  for(const q of B)for(const s of [q.t,q.s,q.ledtrad,q.spelIntro,...(q.spelDelar||[]).flatMap(d=>[d.t,d.s,d.ledtrad,d.fraga])]){if(typeof s!=='string')continue;
    const p=s.replace(/<svg[\s\S]*?<\/svg>/g,'').replace(/\\([\s\S]*?\\)/g,'M').replace(/\\[[\s\S]*?\\]/g,'M').replace(/<[^>]+>/g,' ');const m=p.match(re);assert.ok(!m||ENH.has(m[2]),`${q.id}: ${m&&m[0]}`);}
});
test('Svar, nivåer och delning',()=>{
  const svar={'3.181':[30,130],'3.197':[15,45,50,85],'3.386':[85,67],'3.389':[36,138],'3.392':[35,45,55,80],'3.383':73,'3.384':85,'3.385':48,'3.387':68};
  for(const[id,v]of Object.entries(svar))assert.deepEqual(get(id).rättSvar,v,id);
  assert.equal(get('3.181').spelDelar,undefined);// b-kortet gav tidigare svaret på a
  for(const id of Object.keys(FORV)){const q=get(id),[e,cc,a]=q.poang.split('/').map(Number);assert.equal(q.niva,a?'A':cc?'C':'E',id);
    assert.ok(q.niva==='E'?q.traningsniva<=2:q.niva==='C'?[3,4].includes(q.traningsniva):q.traningsniva>=4,id);}
});
test('Varierade texter och facit med rubriker',()=>{
  const borjan=new Set();
  for(const id of Object.keys(FORV)){const q=get(id),b=q.t.replace(/<[^>]+>/g,'').slice(0,40);assert.ok(!borjan.has(b),`${id}: samma inledning`);borjan.add(b);
    const li=(q.s.match(/<li>/g)||[]).length,r=(q.s.match(/facit-rubrik/g)||[]).length;assert.ok(li>0&&r>=li,id);assert.match(q.s,/facit-svar/,id);}
});
