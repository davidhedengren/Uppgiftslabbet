'use strict';
/* Fy1 konstacc: tydligare facit (användarbeslut 2026-11-04). Varje omskrivet facit är en numrerad steglista där
   rubrikerna visar formlerna, och andragradsekvationer har en grafisk lösning. Se agent/FY1_KONSTACC_FACIT_2026-11-04.md. */
const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('node:fs'),vm=require('node:vm'),path=require('node:path');
const c={window:{}};vm.runInNewContext(fs.readFileSync(path.join(__dirname,'..','uppgifter.js'),'utf8'),c);
const B=JSON.parse(JSON.stringify(c.window.BANK)),q=id=>{const t=B.find(x=>x.id===id);assert.ok(t,id);return t;};
// Omgångar: pilot (tidlösa formeln + tre andragradskort) och omgång 2 (möte och ikapp, konstant acceleration).
const OMSKRIVNA=['3.48','3.64','3.74','3.88','3.93','3.124','3.152','3.370','3.377','3.379','3.118','3.171','3.399',
  '3.39','3.169','3.170','3.176','3.177','3.371','3.389','3.390','3.391','3.446','3.448'];
// Delar ('' = hela uppgiften) där en andragradsekvation löses och facit ska ha en graf.
const GRAFISKA={'3.74':['a'],'3.118':['c'],'3.171':['a'],'3.399':['a','b'],'3.39':['b'],'3.169':['c'],'3.176':[''],'3.177':[''],
  '3.389':['a','b','c'],'3.391':['a'],'3.448':['']};
const RUBRIK_MED_FORMEL=/<p class="facit-rubrik">[^<]*\\\([^<]*\\\)[^<]*<\/p>/;
const facit=t=>t.spelDelar?.length?t.spelDelar.map(d=>[d.etikett,d.s]):[['',t.s]];
const del=(t,et)=>et?t.spelDelar.find(d=>d.etikett===et).s:t.s;

test('Omskrivna konstacc-facit: steglista, formel i en rubrik och svarsrad',()=>{
  for(const id of OMSKRIVNA){const t=q(id);assert.match(t.s,/facit-steglista/,id);
    for(const [et,s] of facit(t)){assert.match(s,/facit-steglista/,id+et);assert.match(s,/facit-svar/,id+et);assert.doesNotMatch(s,/None/,id+et);
      assert.match(s,RUBRIK_MED_FORMEL,`${id}${et}: ingen rubrik med formel`);}}
  // Alla konstacc-kort som har steglista har också formelrubriker (gäller kommande omgångar).
  for(const t of B.filter(x=>x.omr==='konstacc'&&/facit-steglista/.test(x.s)))for(const [et,s] of facit(t))assert.match(s,RUBRIK_MED_FORMEL,t.id+et);
});

test('Andragradsekvationer har grafisk lösning och tillåter GeoGebra',()=>{
  for(const [id,delar] of Object.entries(GRAFISKA)){const t=q(id);assert.equal(t.geogebra,true,id);
    for(const et of delar){const s=del(t,et);assert.match(s,/grafiskt/,id+et);assert.match(s,/<svg[\s\S]*<polyline[\s\S]*<\/svg>/,id+et);}}
});

test('Delfacit avslöjar inte svaret på en senare del',()=>{
  assert.doesNotMatch(q('3.74').spelDelar[0].s,/15\{,\}49|\\sqrt\{240\}/);
  assert.doesNotMatch(q('3.171').spelDelar[0].s,/22\{,\}52|\\sqrt\{507\}/);
  assert.doesNotMatch(q('3.399').spelDelar[0].s,/t ≈ 2,47/);
  assert.doesNotMatch(q('3.39').spelDelar[0].s,/12\ \\mathrm s|t = 12/);
  assert.doesNotMatch(q('3.169').spelDelar[1].s,/10\ \\mathrm s|200/);
});

test('rättSvar är oförändrade och stämmer med oberoende beräkningar',()=>{
  const near=(id,...x)=>{const t=q(id),r=[].concat(t.rättSvar),tol=[].concat(t.tolerans);x.forEach((v,i)=>assert.ok(Math.abs(r[i]-v)<=Math.max(tol[i]||0,1e-9)+1e-9,`${id}[${i}] ${r[i]}≠${v}`));};
  const v70=70/3.6;near('3.48',v70**2/110,110/v70);
  near('3.74',-10+Math.sqrt(100+40/0.6),Math.sqrt(240));
  near('3.118',9/9.82,1.5+81/19.64,(9+Math.sqrt(81+4*4.91*1.5))/9.82);
  near('3.171',(-4+Math.sqrt(16+4*4.91*25))/9.82,Math.sqrt(16+2*9.82*25));
  const d=Math.sqrt(17**2-4*4.91*12);near('3.399',(17-d)/9.82,(17+d)/9.82);
  near('3.39',45,12);near('3.169',4,5,10,200);near('3.170',2.5,45-4.91*6.25);near('3.176',13/1.4);near('3.177',4+Math.sqrt(56));
  near('3.371',2600/(1200/33.4)**2);near('3.390',0.4,2*270/15.625-15);near('3.448',2+Math.sqrt(28));near('3.446',-64/24);
  const ta=(-9+Math.sqrt(81+375))/0.75,tb=40+Math.sqrt(6200),tc=(31-Math.sqrt(97))/2;near('3.389',4*ta+0.375*ta*ta,24+0.2*tb,tc);
  const tau=(18-Math.sqrt(52))/4;near('3.391',18-4*tau);
});
