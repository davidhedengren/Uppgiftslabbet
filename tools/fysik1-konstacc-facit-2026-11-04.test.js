'use strict';
/* Fy1 konstacc: tydligare facit (användarbeslut 2026-11-04). Varje omskrivet facit är en numrerad steglista där
   en rubrik visar formeln, och andragradsekvationer har en grafisk lösning. Se agent/FY1_KONSTACC_FACIT_2026-11-04.md. */
const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('node:fs'),vm=require('node:vm'),path=require('node:path');
const c={window:{}};vm.runInNewContext(fs.readFileSync(path.join(__dirname,'..','uppgifter.js'),'utf8'),c);
const B=JSON.parse(JSON.stringify(c.window.BANK)),q=id=>{const t=B.find(x=>x.id===id);assert.ok(t,id);return t;};
const OMSKRIVNA=['3.48','3.64','3.74','3.88','3.93','3.124','3.152','3.370','3.377','3.379','3.118','3.171','3.399'];
const GRAFISKA={'3.74':['a'],'3.118':['c'],'3.171':['a'],'3.399':['a','b']};
const FORMEL=/<p class="facit-rubrik">[^<]*\\\((?:[^<]*)=(?:[^<]*)\\\)<\/p>/;
const facit=t=>t.spelDelar?.length?t.spelDelar.map(d=>[d.etikett,d.s]):[['',t.s]];

test('Omskrivna konstacc-facit: steglista, formel i rubrik och svarsrad',()=>{
  for(const id of OMSKRIVNA){const t=q(id);assert.match(t.s,/facit-steglista/,id);
    for(const [et,s] of facit(t)){assert.match(s,/facit-steglista/,id+et);assert.match(s,/facit-svar/,id+et);assert.doesNotMatch(s,/None/,id+et);
      if(!/^\s*<div class="facit-v2 facit-stegvis"><ol class="facit-steglista" role="list"><li><p class="facit-rubrik">Accelerationen från a\)/.test(s))
        assert.match(s,FORMEL,`${id}${et}: ingen rubrik med formel`);}}
});

test('Andragradsekvationer har grafisk lösning och tillåter GeoGebra',()=>{
  for(const [id,delar] of Object.entries(GRAFISKA)){const t=q(id);assert.equal(t.geogebra,true,id);
    for(const et of delar){const s=t.spelDelar.find(d=>d.etikett===et).s;assert.match(s,/Lös ekvationen grafiskt/,id+et);assert.match(s,/<svg[\s\S]*<polyline[\s\S]*<\/svg>/,id+et);assert.match(s,/Alternativ: lösningsformeln/,id+et);}}
});

test('Delfacit avslöjar inte svaret på en senare del',()=>{
  // 3.74 a och 3.171 a löser tiden utan att först räkna ut slutfarten (svaret på b).
  assert.doesNotMatch(q('3.74').spelDelar[0].s,/15\{,\}49|\\sqrt\{240\}/);
  assert.doesNotMatch(q('3.171').spelDelar[0].s,/22\{,\}52|\\sqrt\{507\}/);
  // 3.399 a markerar bara den första skärningen.
  assert.doesNotMatch(q('3.399').spelDelar[0].s,/t ≈ 2,47/);
});

test('rättSvar är oförändrade och stämmer med oberoende beräkningar',()=>{
  const near=(id,...x)=>{const r=q(id).rättSvar;x.forEach((v,i)=>assert.ok(Math.abs(r[i]-v)<=Math.max(q(id).tolerans[i]||0,1e-9)+1e-9,`${id}[${i}] ${r[i]}≠${v}`));};
  const v70=70/3.6;near('3.48',v70**2/110,110/v70);
  const r74=-10+Math.sqrt(100+40/0.6);near('3.74',r74,Math.sqrt(240));
  near('3.118',9/9.82,1.5+81/19.64,(9+Math.sqrt(81+4*4.91*1.5))/9.82);
  near('3.171',(-4+Math.sqrt(16+4*4.91*25))/9.82,Math.sqrt(16+2*9.82*25));
  const d=Math.sqrt(17**2-4*4.91*12);near('3.399',(17-d)/9.82,(17+d)/9.82);
});
