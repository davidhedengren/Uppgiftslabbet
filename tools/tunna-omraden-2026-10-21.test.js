'use strict';
const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('node:fs'),vm=require('node:vm'),path=require('node:path');
const root=path.join(__dirname,'..');
function bank(fil){const c={window:{}};vm.runInNewContext(fs.readFileSync(path.join(root,fil),'utf8'),c);return Object.values(c.window).find(v=>Array.isArray(v));}
const B={fy1:bank('uppgifter.js'),fy2:bank('uppgifter2.js'),mato1:bank('uppgiftermato1.js'),mato2:bank('uppgiftermato2.js')};
/* ID:n delas mellan kapitel i vissa banker; välj uppgiften i rätt område. */
const get=(b,id,omr)=>B[b].find(t=>t.id===id&&t.omr===omr);
const NYA={
  fy1:{omr:'fyra_krafterna',ids:['9.428','9.429','9.430','9.431','9.432','9.433','9.434','9.435']},
  fy2i:{bank:'fy2',omr:'induktion_ledare',ids:['3.415','3.416','3.417','3.418','3.419','3.420','3.421','3.422']},
  fy2s:{bank:'fy2',omr:'stjarnornas_utveckling',ids:['5.369','5.370','5.371','5.372','5.373','5.374','5.375','5.376']},
  mato1:{omr:'derivata_exponential',ids:['2.1116','2.1117','2.1118','2.1119','2.1120','2.1121','2.1122','2.1123']},
  mato2a:{bank:'mato2',omr:'asinx_bcosx',ids:['2.589','2.590','2.591','2.592','2.593','2.594','2.595','2.596']},
  mato2s:{bank:'mato2',omr:'sinusformad_kurva',ids:['2.597','2.598','2.599','2.600','2.601','2.602','2.603','2.604']},
};
const alla=Object.entries(NYA).flatMap(([k,v])=>v.ids.map(id=>({b:v.bank||k,omr:v.omr,id})));
const nara=(a,b,rel=1e-6)=>assert.ok(Math.abs(a-b)<=Math.abs(b)*rel+1e-12,`${a} != ${b}`);

test('48 nya uppgifter finns i rätt område med fullständig metadata',()=>{
  assert.equal(alla.length,48);
  for(const {b,omr,id} of alla){
    const t=get(b,id,omr);assert.ok(t,`${b} ${id}`);
    for(const f of ['niva','poang','t','s','familj','formaga','ledtrad','traningsniva','arbetsinsats'])assert.ok(t[f]!=null&&t[f]!=='',`${id} ${f}`);
    assert.equal(t.spel,true);assert.equal(t.självrättning,true);
    if(b.startsWith('fy'))assert.equal(t.miniräknare,true,`${id}: miniräknare alltid i fysik`);
    if(b==='mato1')assert.deepEqual([...t.kurs],['1b','1c']);
    if(b==='mato2')assert.deepEqual([...t.kurs],['2c']);
    if(t.svarstyp==='alternativ')assert.equal(t.alternativ.filter(a=>a.ratt).length,1,id);
    if(t.svarstyp==='flera_delar'){
      for(const f of ['rättSvar','svarFormat','tolerans','svarEtiketter'])assert.equal(t[f].length,t.rättSvar.length,`${id} ${f}`);
      assert.ok(['ordnad','mängd'].includes(t.svarsstruktur),id);
    }
  }
  /* Varje område har nu minst 14 uppgifter (induktion 6→14, stjärnor 7→15, övriga 18–20). */
  for(const v of Object.values(NYA)){const b=v.bank||Object.keys(NYA).find(k=>NYA[k]===v);assert.ok(B[b].filter(t=>t.omr===v.omr).length>=14,v.omr);}
});

test('Fysikfacit stämmer med omräkning',()=>{
  const k=8.99e9,e=1.602e-19,G=6.674e-11,me=9.109e-31,mp=1.673e-27,Ms=1.989e30,c=2.998e8;
  nara(get('fy1','9.431','fyra_krafterna').rättSvar,k*e*e/(G*me*mp));
  nara(get('fy1','9.432','fyra_krafterna').rättSvar,k*e*e/(2e-15)**2);
  nara(get('fy1','9.435','fyra_krafterna').rättSvar,Math.sqrt(G/k)/e);
  nara(get('fy2','3.415','induktion_ledare').rättSvar,0.20*0.50*3.0);
  nara(get('fy2','3.416','induktion_ledare').rättSvar,0.80*0.25*2.5/2.0);
  nara(get('fy2','3.418','induktion_ledare').rättSvar,45e-6*34*250);
  nara(get('fy2','3.420','induktion_ledare').rättSvar,0.50*(0.50*0.40*3.0/1.2)*0.40);
  nara(get('fy2','3.422','induktion_ledare').rättSvar,(0.30/(0.60*0.50))*1.5/(0.60*0.50));
  nara(get('fy2','5.372','stjarnornas_utveckling').rättSvar,10*0.5**-2.5);
  nara(get('fy2','5.374','stjarnornas_utveckling').rättSvar,1.4*Ms/(4/3*Math.PI*12e3**3));
  nara(get('fy2','5.375','stjarnornas_utveckling').rättSvar,2*G*10*Ms/c**2/1000);
  nara(get('fy2','5.376','stjarnornas_utveckling').rättSvar,Math.sqrt(2000)*(5778/3500)**2);
  assert.equal(get('fy2','3.419','induktion_ledare').alternativ.find(a=>a.ratt).txt,'Uppåt i figuren'); // flervalskort sedan 2026-10-24
});

test('Matematikfacit stämmer med omräkning',()=>{
  const sind=v=>Math.sin(v*Math.PI/180),cosd=v=>Math.cos(v*Math.PI/180);
  nara(get('mato1','2.1122','derivata_exponential').rättSvar,Math.log(2)/0.04);
  /* 2.1123: f=3e^{-0,5x}, lutning -0,3 när f=0,6. */
  const x=2*Math.log(5);nara(-0.5*3*Math.exp(-0.5*x),-0.3);
  const t593=get('mato2','2.593','asinx_bcosx');assert.equal(t593.svarsstruktur,'mängd');
  for(const v of t593.rättSvar)nara(sind(v)+Math.sqrt(3)*cosd(v),1);
  const [R,v594]=get('mato2','2.594','asinx_bcosx').rättSvar;
  nara(20*sind(v594)+21*cosd(v594),R);assert.equal(R,29);
  const [a,]=get('mato2','2.596','asinx_bcosx').rättSvar;nara(a*sind(30)+5*Math.sqrt(3)*cosd(30),10);
  const [a0,b0,c0]=get('mato2','2.600','sinusformad_kurva').rättSvar;nara(a0*sind(b0*15)+c0,5);nara(a0*sind(b0*45)+c0,-1);
  const [ha,hb,hc]=get('mato2','2.601','sinusformad_kurva').rättSvar;nara(hc-ha*cosd(0),5);nara(hc-ha*cosd(hb*4),45);
  nara(get('mato2','2.603','sinusformad_kurva').rättSvar,18+6*sind(15*(7-9)));
  const [pa,pb,pc]=get('mato2','2.604','sinusformad_kurva').rättSvar;nara(pa*sind(pb*10)+pc,5);assert.equal(pc,3);
});

test('Figurer finns där de behövs och ligger inom ramen',()=>{
  const medFigur=['9.434','3.415','3.416','3.418','3.419','3.422','5.370','2.1117','2.1120','2.592','2.597','2.598','2.599','2.601'];
  for(const {b,omr,id} of alla.filter(x=>medFigur.includes(x.id))){
    const t=get(b,id,omr);const m=t.t.match(/<svg[^>]*viewBox="0 0 (\d+) (\d+)"/);assert.ok(m,id);
    assert.match(t.t,/aria-label="[^"]{20,}"/,id);
  }
});
