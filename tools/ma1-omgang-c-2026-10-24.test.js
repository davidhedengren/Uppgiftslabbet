'use strict';
/* Ma1 2026-10-24 omgång C: proportionalitet, potensekvationer, potensfunktioner, index och upprepade förändringar med figurer. */
const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('node:fs'),vm=require('node:vm'),path=require('node:path');
const c={window:{}};vm.runInNewContext(fs.readFileSync(path.join(__dirname,'..','uppgifterma1.js'),'utf8'),c);
const B=JSON.parse(JSON.stringify(Object.values(c.window).find(Array.isArray)));const get=id=>{const t=B.find(x=>x.id===id);assert.ok(t,id);return t;};
const ids=(k,a,b)=>Array.from({length:b-a+1},(_,i)=>`${k}.${a+i}`);
const NYA=[...ids(7,720,732),...ids(3,620,655),...ids(2,600,611)];

test('61 nya kort, rätt områden, figurer och inga dubblettfacit',()=>{
  const per={};for(const id of NYA){const t=get(id);per[t.omr]=(per[t.omr]||0)+1;assert.ok([1,2,3,4].includes(t.traningsniva),id);}
  assert.deepEqual(per,{proportionalitet_yrke:13,potensekvationer:12,potensfunktioner:12,index:12,upprepade_forandringar:12});
  assert.ok(NYA.filter(id=>/<svg|<table/.test(get(id).t)).length>=40);
  const v=x=>{const s=String(x.rättSvar),n=Number(s);return isNaN(n)?s:String(Math.round(n*1e6)/1e6);};
  for(const id of NYA){const t=get(id);if(t.svarstyp==='alternativ')continue;
    const krock=B.filter(u=>u.omr===t.omr&&u.id!==id&&u.svarstyp!=='alternativ'&&u.rättSvar!=null&&!Array.isArray(u.rättSvar)&&v(u)===v(t)).map(u=>u.id);
    assert.deepEqual(krock,[],`${id} har samma facit som ${krock}`);}
});

test('Facit räknas om',()=>{
  const n=(id,x,tol=1e-6)=>assert.ok(Math.abs(Number(get(id).rättSvar)-x)<=tol,`${id}: ${get(id).rättSvar} ≠ ${x}`);
  n('7.720',2.5/4*10);n('7.721',90*5);n('7.722',54/9);n('7.723',360/2*8);n('7.724',15*18);n('7.725',3/5);n('7.727',216/2.4*3.5);n('7.728',35*(1200/8-1000/8));
  n('7.729',90/6*2);n('7.730',Math.ceil(4.5*4/5));n('7.731',45*60);n('7.732',4*6/3);
  n('3.620',14);n('3.621',11);n('3.622',(2**0.2-1)*100,1e-3);n('3.623',8);n('3.624',16);n('3.625',(1-Math.cbrt(245650/400000))*100,1e-6);n('3.626',(1-0.5**0.25)*100,1e-3);
  n('3.628',50);n('3.629',64);n('3.630',9);n('3.631',(1.25**0.25-1)*100,1e-3);
  n('2.600',12.5);n('2.602',5);n('2.603',2*Math.sqrt(1.44));n('2.604',27);n('2.605',0.006*90**2);n('2.606',135);n('2.607',75);n('2.608',16/9,1e-3);n('2.609',1.5**3);n('2.610',60/8);n('2.611',70*16**0.75);
  n('3.632',16);n('3.633',65);n('3.634',110*126/105);n('3.636',130);n('3.637',(140/125-1)*100);n('3.638',455/1.3);n('3.640',80);n('3.641',6400*128/112,1e-3);n('3.642',(1.125/1.1-1)*100,1e-3);n('3.643',1088/850*100);
  n('3.644',800*0.75*0.8);n('3.645',1.3*0.7);n('3.646',2000*1.08*1.05*0.9);n('3.647',10000*1.04**6,1e-3);n('3.649',5000*1.02**12,1e-3);n('3.651',935/(0.85*1.1));n('3.652',4500*0.97**5,1e-3);
  n('3.653',11);n('3.654',0.65);n('3.655',(1.17/0.9-1)*100);
  for(const id of NYA.filter(id=>get(id).svarstyp==='alternativ'))assert.equal(get(id).alternativ.filter(a=>a.ratt).length,1,id);
});
