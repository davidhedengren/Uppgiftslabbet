'use strict';
/* Fy1 omgång 11 (2026-10-25): 25 kort på nivå 3 i s-t-diagram (3.739–3.745), Newtons tredje lag (4.891–4.896),
   laddning (8.649–8.654) och seriekoppling (8.655–8.660). Facit räknas om oberoende. */
const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('node:fs'),vm=require('node:vm'),path=require('node:path');
const c={window:{}};vm.runInNewContext(fs.readFileSync(path.join(__dirname,'..','uppgifter.js'),'utf8'),c);
const B=JSON.parse(JSON.stringify(c.window.BANK));const get=id=>{const t=B.find(x=>x.id===id);assert.ok(t,id);return t;};
const NYA=[...Array.from({length:7},(_,i)=>`3.${739+i}`),...Array.from({length:6},(_,i)=>`4.${891+i}`),...Array.from({length:12},(_,i)=>`8.${649+i}`)];
const nära=(id,...x)=>{const r=get(id).rättSvar,a=Array.isArray(r)?r:[r],tol=get(id).tolerans,t=Array.isArray(tol)?tol:[tol];assert.equal(a.length,x.length,id);
  x.forEach((v,i)=>assert.ok(Math.abs(a[i]-v)<=(t[i]||0)+1e-9*Math.max(1,Math.abs(v)),`${id}[${i}]: ${a[i]} ≠ ${v}`));};
const e=1.602e-19,me=9.11e-31;

test('25 spelbara nivå 3-kort i fyra områden, fysikformat och inga dubblettfacit',()=>{
  const per={};
  for(const id of NYA){const t=get(id);per[t.omr]=(per[t.omr]||0)+1;assert.equal(t.traningsniva,3,id);assert.equal(t.niva,'C',id);assert.equal(t.poang,'(0/1/0)',id);
    assert.equal(t.spel,true,id);assert.equal(t.miniräknare,true,id);
    if(t.svarstyp==='alternativ'){assert.equal(t.alternativ.filter(a=>a.ratt).length,1,id);assert.ok(!t.alternativ[0].ratt,id);assert.match(t.t,/Välj ett alternativ/,id);}
    else assert.ok(/\(Svara[^)]*\)\s*(<\/p>)?$/.test(t.t)||t.svarEnhet||t.svarVardesiffror!=null,id);}
  assert.deepEqual(per,{st_diagram:7,newton3:6,laddning:6,seriekoppling:6});
  const v=x=>JSON.stringify(x.rättSvar);
  for(const id of NYA){const t=get(id);if(t.rättSvar==null)continue;
    const krock=B.filter(w=>w.omr===t.omr&&w.id!==id&&w.rättSvar!=null&&v(w)===v(t)).map(w=>w.id);assert.deepEqual(krock,[],`${id}: ${krock}`);}
  // B startar 5 s efter A, vilket står i texten och inte bara syns i figuren
  assert.match(get('3.739').t,/5 s senare/);
});

test('Facit räknas om',()=>{
  // s-t-diagram: A s=4t, B s=6(t−5)
  const tA=30/(6-4);nära('3.739',tA,4*tA);nära('3.740',(12+8)/10,4/10);
  const s=t=>20*t-2*t*t,h=1e-6;nära('3.742',(s(2+h)-s(2-h))/(2*h),s(5)/5);assert.ok(Math.abs(s(2)-(12*2+8))<1e-12);
  nära('3.743',6*20-4*15,(6*20-4*15)/45,(6*20+4*15)/45);nära('3.744',300/40,25*300/40);nära('3.745',(11-2)/12*60);
  // tredje lagen
  nära('4.891',120/60*0.5,120/80*0.5);nära('4.892',20000*0.3/1000);nära('4.894',60000/12000,60000/1200);nära('4.896',10*90/30);
  // laddning
  nära('8.649',2*5-(-2));nära('8.650',4.8e-9/e,4.8e-9/e*me);nära('8.651',7/2);nära('8.653',(-2-(8-2)/2)*-1e-9/e);
  // seriekoppling
  nära('8.655',(9-2)/0.02);nära('8.656',(5-2)/(2/10));nära('8.657',4/(2/40),(9-2-4)/(2/40));nära('8.658',36*36/(24+48),36*36/24);
  nära('8.659',Math.min(Math.sqrt(0.25/100),Math.sqrt(0.5/400))*500);
});
