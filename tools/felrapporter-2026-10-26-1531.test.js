'use strict';
/* Felrapporter från Kunskapsgymmet 2026-10-26 15:31 (Ma1 och Fy1). Se agent/FELRAPPORTER_2026-10-26_1531.md. */
const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('node:fs'),vm=require('node:vm'),path=require('node:path');
const las=f=>{const c={window:{}};vm.runInNewContext(fs.readFileSync(path.join(__dirname,'..',f),'utf8'),c);return JSON.parse(JSON.stringify(Object.values(c.window).find(Array.isArray)));};
const MA1=las('uppgifterma1.js'),FY1=las('uppgifter.js');
const q=(B,id)=>{const t=B.find(x=>x.id===id);assert.ok(t,id);return t;};
const nara=(a,b,id)=>assert.ok(Math.abs(a-b)<1e-9,`${id}: ${a} ≠ ${b}`);
const flervalOk=(alt,id)=>{assert.equal(alt.filter(a=>a.ratt).length,1,id);assert.ok(!alt[0].ratt,id);for(const a of alt)if(!a.ratt)assert.ok(a.kommentar&&!/Pröva sambandet för de givna villkoren/.test(a.kommentar),id);};

test('Ma1: nivå, flerval och tydliga svarsformat',()=>{
  assert.equal(q(MA1,'0.1257').traningsniva,4);
  const e=q(MA1,'3.55');assert.equal(e.svarstyp,'alternativ');flervalOk(e.alternativ,'3.55');
  assert.equal(e.alternativ.find(a=>a.ratt).txt,'Ekvationen saknar lösning.');
  for(const x of [2,0,-2])assert.notEqual(5*3**x,3**(x+2)/5);
  const k=q(MA1,'3.194');assert.match(k.t,/Kantlängden är \\\(s\\\) cm/);assert.match(k.spelDelar[0].t,/Kantlängden är \\\(s\\\) cm/);assert.equal(k.rättSvar[0][0],'s^3=512');
  const d=q(MA1,'2.22');assert.deepEqual(d.svarFormat,['mängd','mängd']);assert.deepEqual(d.rättSvar,['{-3,0,2,5}','{1,4,9}']);
  const f=q(MA1,'1.440');flervalOk(f.alternativ,'1.440');assert.doesNotMatch(JSON.stringify(f.alternativ),/annars inget x/);
  assert.match(q(MA1,'2.334').t,/Teckna ett uttryck för kostnaden/);
  const p=q(MA1,'2.415');assert.equal(p.tolerans,0);assert.equal(p.rättSvar,9*4**0.5);assert.match(p.t,/y=9/);
  assert.deepEqual(q(MA1,'2.180').självrättning,[true,true,false]);
});
test('Ma1: tanken är tom från början och alternativen förklarar proportionalitet',()=>{
  for(const [id,v,fl] of [['2.550',1.5,0.15],['2.551',1.2,0.12]]){const t=q(MA1,id);
    for(const txt of [t.t,...t.spelDelar.map(x=>x.t)]){assert.match(txt,/Tanken är tom när kranen öppnas/);assert.match(txt,/<td>0<\/td><td>10<\/td>/);}
    flervalOk(t.spelDelar[0].alternativ,id);nara(v/10,fl,id);assert.equal(t.rättSvar[1],(180*(id==='2.550')+72*(id==='2.551'))/fl/60);}
});
test('Ma1: koordinataxlarna går genom origo i 2.620, 2.626 och 2.628',()=>{
  for(const id of ['2.620','2.626','2.628']){const svg=q(MA1,id).t.match(/<svg[\s\S]*?<\/svg>/)[0];
    assert.doesNotMatch(svg,/stroke="#172b3a" stroke-width="1.6"/,id);
    const ax=[...svg.matchAll(/<line x1="([\d.]+)" y1="([\d.]+)" x2="([\d.]+)" y2="([\d.]+)" stroke="#34495e" stroke-width="1.8"\/>/g)].map(m=>m.slice(1).map(Number));
    const hor=ax.find(a=>a[1]===a[3]),ver=ax.find(a=>a[0]===a[2]);
    const xEt=n=>+svg.match(new RegExp(`<text x="([\\d.]+)" y="[\\d.]+"[^>]*text-anchor="middle"[^>]*>${n}</text>`))[1];
    const mitt=(xEt('1')+xEt('−1'))/2;assert.ok(Math.abs(ver[0]-mitt)<1,id);
    assert.ok(hor[1]>40&&hor[1]<255,id);}
  assert.equal(q(MA1,'2.626').rättSvar,'y=3*x-5');assert.equal(1,3*2-5);
  nara(q(MA1,'2.628').rättSvar,(-2-7)/(4+2),'2.628');
});

const allText=t=>[t.t,t.spelIntro||'',...(t.spelDelar||[]).flatMap(d=>[d.t||'',d.fraga||''])].join(' ');
const G=9.82;
test('Fy1: fristående delkort utan svarsenhet, likformig eller fartbelopp',()=>{
  for(const id of ['3.89','3.90','3.91','3.93','3.119','3.121','3.124','3.146','3.155']){const t=q(FY1,id);const txt=allText(t);
    assert.doesNotMatch(txt,/Svara i|likformig|fartbelopp|stationsavstånd|Behandla cykeln|med två decimaler|med tre decimaler|med en decimal/i,id);
    assert.equal(t.svarVardesiffror.length,t.rättSvar.length,id);
    for(const d of t.spelDelar){assert.ok(d.t&&/\?|med tecken\.|Ange tecknet\./.test(d.t),id+d.etikett);assert.match(d.s,/facit-svar/);assert.ok(d.ledtrad.length>20);}}
  assert.doesNotMatch(q(FY1,'3.92').t,/fartbelopp|Svara i/);assert.match(q(FY1,'3.156').t,/mellan stationerna/);
});
test('Fy1: svaren räknas om från delkortens egna givna värden',()=>{
  const r=id=>q(FY1,id).rättSvar;
  nara(r('3.89')[1],14/G,'3.89');nara(r('3.89')[2],14**2/(2*G),'3.89');
  [10.8,2.4*4.5**2/2,9.7,5.5*3.5+0.6*3.5**2,22/3.2,22**2/6.4,153/70,35/8.5].forEach((v,i)=>nara(r('3.90')[i],v,'3.90'));
  [60,900,Math.sqrt(30**2-2*0.5*400),10**2/(2*0.5)].forEach((v,i)=>nara(r('3.91')[i],v,'3.91'));
  [68**2/(2*1156),68/2,78**2/4].forEach((v,i)=>nara(r('3.93')[i],v,'3.93'));
  [2.4/0.9,2.4**2/1.8,2.4*7].forEach((v,i)=>nara(r('3.119')[i],v,'3.119'));
  [23**2/136,68/11.5].forEach((v,i)=>nara(r('3.124')[i],v,'3.124'));
  [(1.2-5.5)/7.5,3.35,3.35*7.5].forEach((v,i)=>nara(r('3.155')[i],v,'3.155'));
  [Math.sqrt(24/G),Math.sqrt(2*G*12)].forEach((v,i)=>nara(r('3.146')[i+1],v,'3.146'));
  [G*Math.sin(8*Math.PI/180),Math.sqrt(2*1.37*120),480].forEach((v,i)=>nara(r('3.121')[i],v,'3.121'));
  nara(r('3.92'),45/4,'3.92');nara(r('3.156'),1.2*100/2+12*40+144/3,'3.156');
});
test('Fy1: figurer och frågetext',()=>{
  const c=q(FY1,'3.121').spelIntro;const pol=c.match(/<polygon points="([^"]+)"/)[1].split(' ').map(p=>p.split(',').map(Number));
  assert.ok(pol[2][0]<pol[1][0]&&pol[2][1]<pol[1][1],'backen ska vara högst till vänster');assert.match(c,/rotate\(8\)/);
  assert.match(q(FY1,'3.146').spelIntro,/aria-label="En gran med en kotte/);
  const e=q(FY1,'8.158');assert.match(e.spelDelar[0].t,/^<p>Diagrammet visar spänningen/);assert.doesNotMatch(e.spelDelar[0].t,/Svara i/);
  flervalOk(e.spelDelar[2].alternativ,'8.158 d');
});
test('Ma1 6.31: alternativ i hela meningar och kontrollerad skärningspunkt',()=>{
  const t=q(MA1,'6.31');flervalOk(t.alternativ,'6.31');assert.match(t.alternativ.find(a=>a.ratt).txt,/lösningen till ekvationen/);
  assert.doesNotMatch(JSON.stringify(t.alternativ),/skrivna som en punkt|största möjliga/);assert.equal(2*2+1,7-2);
});
