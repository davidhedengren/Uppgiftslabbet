'use strict';
/* Ämnesplanen (Matematik fortsättning) lägger trigonometriska ekvationer, radianer, trigonometriska identiteter,
   trigonometriska funktioners derivator och integraler samt produkt- och kedjeregeln på nivå 2 (Ma4).
   2026-10-26 flyttades sådana kort från Ma3 (BANKMATO1) till Ma4 (BANKMATO2) med idTidigare 'mato1 <id>'. */
const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('node:fs'),vm=require('node:vm'),path=require('node:path');
const las=(f,g)=>{const c={window:{}};vm.runInNewContext(fs.readFileSync(path.join(__dirname,'..',f),'utf8'),c);return JSON.parse(JSON.stringify(c.window[g]));};
const A=las('uppgiftermato1.js','BANKMATO1'),B=las('uppgiftermato2.js','BANKMATO2'),OMR2=las('strukturmato2.js','OMRMATO2');
const FLYTT=[['4.71','1.699','trig_grundekvationer'],['4.177','1.700','trig_grundekvationer'],['4.583','1.701','trig_grundekvationer'],['4.410','1.702','trig_grundekvationer'],
 ['4.476','1.703','trig_ekv_formler'],['4.484','1.704','trig_ekv_formler'],['4.573','1.705','trig_identiteter'],['4.584','2.719','sinus_cosinuskurvor'],
 ['4.416','2.720','kurvor_radianer'],['4.417','2.721','kurvor_radianer'],['1.272','2.722','trig_problemlosning_2'],
 ['2.358','2.723','derivatan_sin_cos'],['2.365','2.724','derivatan_sin_cos'],['2.367','2.725','derivatan_sin_cos'],['2.372','2.726','derivatan_sin_cos'],
 ['2.356','2.727','derivata_sammansatta'],['2.361','2.728','derivata_sammansatta'],['2.366','2.729','derivata_sammansatta'],['3.1239','2.730','derivata_sammansatta'],
 ['2.368','3.531','produktregeln'],['2.370','3.532','produktregeln'],['3.519','3.533','produktregeln'],['3.520','3.534','produktregeln'],['3.530','3.535','produktregeln'],['3.577','3.536','produktregeln'],
 ['3.579','4.621','integraler_primitiva'],['3.531','4.622','integraler_primitiva'],['3.532','4.623','integraler_primitiva'],['3.534','4.624','integraler_primitiva'],
 ['3.535','4.625','integraler_primitiva'],['3.583','4.626','integraler_primitiva'],['3.585','4.627','integraler_primitiva'],['3.538','4.628','areor_mellan_kurvor'],
 ['3.589','4.629','integraler_storheter'],['3.547','4.630','integraler_storheter'],['3.548','4.631','integraler_storheter'],['3.610','4.632','integraler_storheter']];
const omrer2=new Set(Object.values(OMR2).flatMap(o=>Object.keys(o)));

test('De flyttade korten finns bara i Ma4, med spår till sitt gamla Ma3-id',()=>{
  assert.equal(new Set(B.map(x=>x.id)).size,B.length);
  for(const [gammal,ny,omr] of FLYTT){
    assert.ok(!A.some(x=>x.id===gammal),gammal+' ligger kvar i Ma3');
    const t=B.find(x=>x.id===ny);assert.ok(t,ny);
    assert.equal(t.idTidigare,'mato1 '+gammal);assert.equal(t.omr,omr);assert.ok(omrer2.has(omr),omr);
    assert.deepEqual(t.kurs,['2c']);assert.ok(B.some(x=>x!==t&&x.omr===omr&&x.familj===t.familj),ny+': okänd familj');
    assert.ok(t.omrTidigare.length>0,ny);
  }
});

const text=x=>[x.t,x.s,x.ledtrad,JSON.stringify(x.alternativ||''),JSON.stringify(x.spelDelar||'')].join(' ');
test('Ma3 innehåller inte längre nivå 2-innehåll som ämnesplanen lägger i Ma4',()=>{
  for(const x of A){const t=text(x);
    assert.doesNotMatch(t,/radian|trigonometriska ettan|produktregeln(?! för logaritmer| ger ln)|kedjeregeln|inre derivata/i,x.id);
    // sinus, cosinus och tangens hör bara hemma i Ma3c:s trigonometrikapitel, och där i grader
    if(/\\(sin|cos|tan)(?![a-z])/.test(x.t))assert.deepEqual(x.kurs,['1c'],x.id);
    if(x.kap!==4&&x.kap!==5)assert.doesNotMatch(x.t,/\\(sin|cos|tan)(?![a-z])/,x.id);
  }
});
