'use strict';
/* Fy1 2026-11-02: varierade serie- och parallellkopplingskort med kopplingsscheman (8.684–8.726)
   och kopplingsscheman i 17 äldre kort utan figur. Inga kort i områdena handlar om effekt. Facit räknas om oberoende. */
const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('node:fs'),vm=require('node:vm'),path=require('node:path');
const c={window:{}};vm.runInNewContext(fs.readFileSync(path.join(__dirname,'..','uppgifter.js'),'utf8'),c);
const B=JSON.parse(JSON.stringify(c.window.BANK));const get=id=>{const t=B.find(x=>x.id===id);assert.ok(t,id);return t;};
const NYA=Array.from({length:43},(_,i)=>`8.${684+i}`);
const utanFig=x=>String(x||'').replace(/<svg[\s\S]*?<\/svg>/g,'').replace(/<[^>]+>/g,' ');

const FACIT={
  '8.684':3.0/2,'8.685':0.25,'8.686':47+22+10,'8.687':2.4+3.6,'8.689':12/(680+320)*1000,'8.690':100-33,'8.691':33*0.20,'8.692':24/10,
  '8.693':220*12/500,'8.694':(330+230)*0.025,'8.695':9.0,'8.696':4/(1+4)*10,'8.697':9.0/1.2e-3/1000-4.7,'8.698':[9.0-1.8-3.0,(9.0-1.8-3.0)/0.060],
  '8.699':18*6.0/30,'8.700':100*0.090/150*1000,'8.702':(5.0-2.0)/180*1000,'8.703':12-8.0,'8.704':(6.0-1.5)/(1.5/200),'8.705':15/2,
  '8.707':4.5,'8.708':0.45+0.40,'8.709':1/(2/220),'8.711':9.4/47,'8.712':2.6-1.2-0.7,'8.714':1/(1/8+2/24),'8.715':12/24+12/40,
  '8.716':6.0/(0.45-0.20),'8.717':9.0/(4*0.18),'8.718':0.30+9.0/36,'8.719':1/(1/10+1/1000),'8.720':3*0.17,'8.721':12/(0.48-12/40),
  '8.722':9.0/30,'8.723':2.0*3/4,'8.724':9.0,'8.725':Math.floor(2.0/0.25+1e-9),'8.726':1/(1/20-1/28)};

test('43 nya kort: områden, nivåer, figurer och inga effektfrågor',()=>{
  const per={},niv={1:0,2:0,3:0};let fig=0;
  for(const id of NYA){const t=get(id);per[t.omr]=(per[t.omr]||0)+1;niv[t.traningsniva]++;
    assert.equal(t.spel,true,id);assert.equal(t.miniräknare,true,id);assert.ok(t.ledtrad&&t.ledtrad.length>20,id);
    assert.match(t.s,/facit-svar/,id);if(/<svg/.test(t.t))fig++;
    assert.doesNotMatch(utanFig(t.t),/effekt|watt|\d\s*W\b|energi|joule|kWh/i,id);
    if(t.svarstyp==='alternativ'){assert.equal(t.alternativ.filter(a=>a.ratt).length,1,id);
      for(const a of t.alternativ)if(!a.ratt)assert.ok(a.kommentar,`${id}: ${a.txt}`);}}
  assert.deepEqual(per,{seriekoppling:23,parallellkoppling:20});
  assert.deepEqual(niv,{1:16,2:16,3:11});
  assert.equal(fig,41);
});

test('Facit räknas om',()=>{
  for(const [id,v] of Object.entries(FACIT)){const t=get(id),r=t.rättSvar,a=Array.isArray(r)?r:[r],f=Array.isArray(v)?v:[v];
    assert.equal(a.length,f.length,id);
    f.forEach((x,i)=>{const tol=Array.isArray(t.tolerans)?t.tolerans[i]:t.tolerans;assert.ok(Math.abs(a[i]-x)<=(tol||0)+1e-9*Math.max(1,Math.abs(x)),`${id}[${i}]: ${a[i]} ≠ ${x}`);});}
});

test('Inga identiska facit inom områdena',()=>{
  const v=x=>JSON.stringify(x.rättSvar);
  for(const id of NYA){const t=get(id);if(t.rättSvar==null)continue;
    const krock=B.filter(w=>w.omr===t.omr&&w.id!==id&&w.rättSvar!=null&&v(w)===v(t)).map(w=>w.id);assert.deepEqual(krock,[],`${id}: ${krock}`);}
});

test('Kopplingsscheman i äldre kort utan figur',()=>{
  for(const id of ['8.361','8.363','8.365','8.369','8.392','8.362','8.364','8.366','8.367','8.368','8.642','8.643','8.644','8.645','8.672','8.673','8.676'])
    assert.match(get(id).t,/<svg[\s\S]*<\/svg>/,id);
  // Figuren ger inte bort svaret: 8.369 visar den okända resistorn som R₂ = ?
  assert.match(get('8.369').t,/R₂ = \?/);
});

test('Seriekoppling och parallellkoppling: amperemetrar i serie och voltmetrar som egen gren',()=>{
  // I seriekretsar sitter voltmetern mellan två noder (prickar) på huvudledningen, aldrig i själva slingan.
  for(const id of ['8.691','8.693','8.695','8.696','8.703','8.704','8.706']){const s=get(id).t;assert.match(s,/>V[₁₂]?<\/text>/,id);assert.match(s,/r="3\.5"/,id);}
});
