'use strict';
/* Ma1 2026-10-24 omgång F: tunna områden (algebraiska uttryck, kalkylprogram, säkerhetsmarginaler, vektorer, arcus, koordinatgeometri).
   Figurer bara där de passar naturligt (lärarbeslut samma dag). */
const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('node:fs'),vm=require('node:vm'),path=require('node:path');
const c={window:{}};vm.runInNewContext(fs.readFileSync(path.join(__dirname,'..','uppgifterma1.js'),'utf8'),c);
const B=JSON.parse(JSON.stringify(Object.values(c.window).find(Array.isArray)));const get=id=>{const t=B.find(x=>x.id===id);assert.ok(t,id);return t;};
const ids=(k,a,b)=>Array.from({length:b-a+1},(_,i)=>`${k}.${a+i}`);
const NYA=[...ids(1,1540,1550),...ids(6,450,459),...ids(7,770,780),...ids(4,770,819)];

test('82 nya kort i tunna områden utan dubblettfacit',()=>{
  const per={};for(const id of NYA){const t=get(id);per[t.omr]=(per[t.omr]||0)+1;assert.ok([1,2,3,4].includes(t.traningsniva),id);}
  assert.deepEqual(per,{algebraiska_uttryck:11,kalkylprogram:10,sakerhetsmarginaler:11,vektorer:10,vektor_skalar:10,vektor_absolutbelopp:10,arcusfunktioner:10,koordinatgeometri:10});
  const v=x=>{const r=x.rättSvar,s=(Array.isArray(r)?JSON.stringify(r):String(r)).replace(/\s/g,''),n=Number(s);return isNaN(n)?s:String(Math.round(n*1e6)/1e6);};
  for(const id of NYA){const t=get(id);if(t.svarstyp==='alternativ')continue;
    const krock=B.filter(u=>u.omr===t.omr&&u.id!==id&&u.svarstyp!=='alternativ'&&u.rättSvar!=null&&v(u)===v(t)).map(u=>u.id);
    assert.deepEqual(krock,[],`${id} har samma facit som ${krock}`);}
  // låsta cellreferenser visas utan rå dollar-LaTeX i texten
  assert.doesNotMatch(get('6.457').t+get('6.457').s,/\$E\$1/);assert.equal(get('6.457').rättSvar,'=B3*(1+$E$1)');
});

test('Facit räknas om',()=>{
  const n=(id,x,tol=1e-6)=>assert.ok(Math.abs(Number(get(id).rättSvar)-x)<=tol,`${id}: ${get(id).rättSvar} ≠ ${x}`);const u=(id,s)=>assert.deepEqual(get(id).rättSvar,s,id);
  const deg=r=>Math.round(r*180/Math.PI*10)/10;
  n('1.1540',25);n('1.1541',8);u('1.1542','4s');u('1.1544','40n+150');n('1.1545',41);n('1.1546',14);u('1.1547','2x+4y');u('1.1548','3x+6');u('1.1549','4a+12');n('1.1550',2.5);
  u('6.450','=SUMMA(B2:B5)');n('6.451',420);u('6.452','=B2-C2');n('6.453',67);n('6.454',21);n('6.455',11);u('6.456','=A3*B3');n('6.458',1215.51,0.006);
  n('7.770',41);n('7.771',48);n('7.772',1500);n('7.773',10);n('7.774',3.2);n('7.775',80);n('7.776',15);n('7.777',2000);n('7.778',5);n('7.780',27);
  u('4.770',[3,2]);u('4.771',[-4,3]);u('4.772',[3,3]);u('4.774',[5,-6]);u('4.775',[-2,4]);u('4.777',[7,-3]);u('4.778',[6,3]);u('4.779',[-2,-3]);
  u('4.780',[6,3]);u('4.781',[4,-7]);u('4.782',[18,6]);n('4.783',-4);u('4.784',[5,1]);u('4.785',[2,5]);u('4.786',[4,-4]);n('4.788',9);n('4.789',-6);
  n('4.790',20);n('4.791',11);n('4.792',29);n('4.793',8.06,0.005);n('4.794',26);n('4.795',500);n('4.796',6);n('4.797',6.71,0.005);n('4.799',8.54,0.005);
  n('4.800',deg(Math.atan(0.4)));n('4.801',deg(Math.acos(0.9)));n('4.802',deg(Math.asin(0.25)));n('4.803',deg(Math.acos(0.3)));n('4.804',deg(Math.asin(0.64)));n('4.805',deg(Math.atan(1/12)));
  n('4.806',deg(Math.atan(8/11)));n('4.807',deg(Math.acos(5/6)));n('4.809',deg(Math.atan(0.15)));
  n('4.810',9);n('4.811',17);u('4.812',[2,4]);n('4.813',28);n('4.814',4);n('4.816',6.4,0.005);n('4.817',15);u('4.818',[5,3]);u('4.819',[7,-9]);
  for(const id of NYA.filter(id=>get(id).svarstyp==='alternativ'))assert.equal(get(id).alternativ.filter(a=>a.ratt).length,1,id);
});
