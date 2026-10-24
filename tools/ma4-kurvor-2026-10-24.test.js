'use strict';
/* Ma4 2026-10-24: kap 2.1 trigonometriska kurvor (sinus/cosinus, förskjutna kurvor, sinusformad kurva, tan x, a sin x + b cos x).
   63 nya kort 2.656–2.718 med fokus på träningsnivå 1, variation och grafer där de passar. */
const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('node:fs'),vm=require('node:vm'),path=require('node:path');
const c={window:{}};vm.runInNewContext(fs.readFileSync(path.join(__dirname,'..','uppgiftermato2.js'),'utf8'),c);
const B=JSON.parse(JSON.stringify(c.window.BANKMATO2));const get=id=>{const t=B.find(x=>x.id===id);assert.ok(t,id);return t;};
const NYA=Array.from({length:63},(_,i)=>`2.${656+i}`);
const D=Math.PI/180,sin=x=>Math.sin(x*D),cos=x=>Math.cos(x*D),tan=x=>Math.tan(x*D);

test('63 nya kort fördelade på kap 2.1 med många kort på nivå 1',()=>{
  const per={},tn1={};
  for(const id of NYA){const t=get(id);per[t.omr]=(per[t.omr]||0)+1;if(t.traningsniva===1)tn1[t.omr]=(tn1[t.omr]||0)+1;
    assert.equal(t.kap,2,id);assert.deepEqual(t.kurs,['2c'],id);assert.ok([1,2,3].includes(t.traningsniva),id);assert.equal(t.geogebra,false,id);assert.equal(t.spel,true,id);}
  assert.deepEqual(per,{sinus_cosinuskurvor:12,forskjutna_kurvor:13,sinusformad_kurva:14,tan_kurvan:12,asinx_bcosx:12});
  assert.deepEqual(tn1,{sinus_cosinuskurvor:9,forskjutna_kurvor:6,sinusformad_kurva:8,tan_kurvan:7,asinx_bcosx:6});
  assert.equal(new Set(B.map(x=>x.id)).size,B.length,'dubblerade ID:n');
});

test('Nya delmoment har minst åtta uppgifter',()=>{
  for(const [omr,familj] of [['sinus_cosinuskurvor','Avläsa sinus- och cosinuskurvor i grafer'],['sinusformad_kurva','Sinusformade modeller i sammanhang'],['tan_kurvan','Tolka och använda tangenskurvan'],['asinx_bcosx','Summor av svängningar i grafer']])
    assert.ok(B.filter(x=>x.omr===omr&&x.familj===familj).length>=8,familj);
});

test('Inget nytt kort delar facit med ett annat kort i samma område',()=>{
  const v=x=>{const r=x.rättSvar,s=(Array.isArray(r)?JSON.stringify(r):String(r)).replace(/\s/g,''),n=Number(s);return isNaN(n)?s:String(Math.round(n*1e6)/1e6);};
  for(const id of NYA){const t=get(id);if(t.svarstyp==='alternativ')continue;
    const krock=B.filter(u=>u.omr===t.omr&&u.id!==id&&u.svarstyp!=='alternativ'&&u.rättSvar!=null&&v(u)===v(t)).map(u=>u.id);
    assert.deepEqual(krock,[],`${id} har samma facit som ${krock}`);}
});

test('Facit räknas om',()=>{
  const n=(id,x,tol=1e-9)=>assert.ok(Math.abs(Number(get(id).rättSvar)-x)<=tol,`${id}: ${get(id).rättSvar} ≠ ${x}`);const u=(id,s)=>assert.deepEqual(get(id).rättSvar,s,id);
  n('2.656',4);n('2.657',60);n('2.658',(4+1)/2);n('2.660',7);n('2.661',11-3);n('2.662',270);n('2.663',2);u('2.664',[-6,4]);n('2.665',180/4);n('2.666',30);
  n('2.668',2);n('2.669',90-70);n('2.671',25);n('2.672',-1);n('2.673',sin(120-30));u('2.674',[100,-2]);n('2.676',180);u('2.677',[60,3]);n('2.678',90+120);n('2.679',40);n('2.680',180-40);
  u('2.681',[3,-1]);n('2.682',(8+2)/2);n('2.683',(12+4)/2);n('2.684',150-30);n('2.685',360/60);n('2.686',1.5);n('2.688',(120-80)/2);n('2.689',4+1.5);n('2.690',360/29,0.05);u('2.691',[3,120,2]);n('2.692',(13+15)/2);n('2.693',360/4);n('2.694',360/120);
  n('2.695',tan(45),1e-12);n('2.697',135);n('2.698',0.6/0.8);n('2.699',2/5);n('2.700',90+2*180);n('2.701',1.5);n('2.702',180/6);n('2.703',100*tan(8),0.05);n('2.704',45);u('2.706',[120,300]);
  n('2.707',Math.hypot(5,12));n('2.709',-10);u('2.711','3sqrt(2)');n('2.712',Math.hypot(9,12));n('2.713',3);u('2.714',[5,-5]);n('2.715',45);n('2.716',90-Math.atan2(4,3)/D,0.05);n('2.717',0);u('2.718',['sqrt(3)',1]);
  // modellerna bakom graferna
  assert.ok(Math.abs(3*sin(3*20+30)+2-5)<1e-9&&Math.abs(3*sin(3*80+30)+2+1)<1e-9,'2.691 extrempunkter');
  assert.ok(Math.abs(-1+14*sin(30*(7-4))-13)<1e-9&&Math.abs(-1+14*sin(30*(1-4))+15)<1e-9,'2.692 extrempunkter');
  assert.ok(Math.abs(Math.sqrt(3)*sin(17)+cos(17)-2*sin(47))<1e-9,'2.718 identitet');
});

test('Flervalskort har rätt alternativ',()=>{
  const ratt=id=>get(id).alternativ.filter(a=>a.ratt).map(a=>a.txt).sort();
  assert.deepEqual(ratt('2.659'),['y = cos x']);assert.deepEqual(ratt('2.670'),['y = cos x − 3']);assert.deepEqual(ratt('2.687'),['y = 2 sin x + 3']);
  assert.deepEqual(ratt('2.696'),['90°']);assert.deepEqual(ratt('2.708'),['R = √(a² + b²)']);
  assert.deepEqual(ratt('2.675'),['y = sin(x + 360°)','y = sin(x − 360°)']);
  assert.deepEqual(ratt('2.667'),['Grafen går genom punkten (0°, 3).','Perioden är 360°.','Största värdet är 3.']);
  assert.deepEqual(ratt('2.705'),['Grafen går genom origo.','Grafen har en lodrät asymptot vid x = 45°.','Perioden är 90°.']);
});

test('Grafer: bredd, ofyllda kurvor och tangens bruten vid asymptoter',()=>{
  const figurer=NYA.filter(id=>/<svg/.test(get(id).t));assert.equal(figurer.length,28);
  for(const id of figurer){const t=get(id).t;assert.match(t,/style="width:100%;max-width:\d+px"/,id);assert.match(t,/role="img" aria-label="[^"]{20,}"/,id);
    for(const p of t.match(/<polyline[^>]*>/g)||[])assert.match(p,/fill="none"/,id);}
  // tangenskurvor: ingen polyline korsar en asymptot (FP85)
  for(const [id,asym] of [['2.695',[90]],['2.697',[90]],['2.701',[90]],['2.702',[15,45,75]]]){
    const t=get(id).t,vb=t.match(/viewBox="0 0 (\d+) (\d+)"/),W=+vb[1];
    const x0=id==='2.702'?0:-90,x1=id==='2.702'?90:270,xs=x=>48+(x-x0)/(x1-x0)*(W-70);
    for(const p of t.match(/points="[^"]*"/g).filter(s=>s.split(' ').length>20)){const xsv=p.slice(8,-1).split(' ').map(q=>+q.split(',')[0]);
      for(const a of asym)assert.ok(!(Math.min(...xsv)<xs(a)-0.5&&Math.max(...xsv)>xs(a)+0.5),`${id} korsar asymptoten ${a}°`);}
  }
});

test('Gradsvar har gradformat och verktygsbeslut är satta',()=>{
  for(const id of NYA){const t=get(id);const f=[].concat(t.svarFormat||[]);
    if(f.includes('grader'))assert.ok(t.svarEnhet,`${id} saknar svarEnhet`);
    assert.equal(typeof t.miniräknare,'boolean',id);}
  // exakta värden prövas utan räknare
  assert.equal(get('2.706').miniräknare,false);assert.equal(get('2.718').miniräknare,false);
});
