'use strict';
/* Ma1 2026-10-24: varierade kort med figurer i volym, omkrets och area, mönster samt skala, och figurer i äldre geometrikort. */
const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('node:fs'),vm=require('node:vm'),path=require('node:path');
const c={window:{}};vm.runInNewContext(fs.readFileSync(path.join(__dirname,'..','uppgifterma1.js'),'utf8'),c);
const B=JSON.parse(JSON.stringify(Object.values(c.window).find(Array.isArray)));const get=id=>{const t=B.find(x=>x.id===id);assert.ok(t,id);return t;};
const nya=(kap,a,b)=>Array.from({length:b-a+1},(_,i)=>`${kap}.${a+i}`);
const NYA=[...nya(4,700,733),...nya(1,1500,1516),...nya(7,700,713)];
const FIGTILL=['4.527','4.528','4.529','4.530','4.537','4.540','4.541','4.544','4.545','4.547','4.548','4.570','4.582','4.583','4.587','4.594','6.416','1.1103','1.1106','7.544','7.545','7.546'];
const st=h=>(h||'').replace(/<svg[\s\S]*?<\/svg>/g,' ').replace(/<[^>]+>/g,' ').replace(/\s+/g,' ').trim();

test('65 nya kort i rätt områden, med nivå och utan dubblettfacit inom området',()=>{
  const per={};for(const id of NYA){const t=get(id);per[t.omr]=(per[t.omr]||0)+1;assert.ok([1,2,3,4].includes(t.traningsniva),id);assert.equal(t.spel,true,id);}
  assert.deepEqual(per,{volym:17,omkrets_area:17,monster_samband:17,skala_likformighet:14});
  for(const o of Object.keys(per)){const svar=B.filter(t=>t.omr===o&&t.svarstyp!=='alternativ'&&t.rättSvar!=null&&!Array.isArray(t.rättSvar)).map(t=>[t.id,String(t.rättSvar)]);
    for(const id of NYA.filter(id=>get(id).omr===o&&get(id).svarstyp!=='alternativ')){const r=String(get(id).rättSvar);assert.deepEqual(svar.filter(([i,v])=>v===r&&i!==id).map(x=>x[0]),[],`${id} har samma facit ${r}`);}}
});

test('Figurer: nya kort har oftast figur, äldre geometrikort har fått figur',()=>{
  const med=NYA.filter(id=>/<svg/.test(get(id).t)).length;assert.ok(med>=45,`${med} av ${NYA.length}`);
  for(const id of FIGTILL){const t=get(id).t;assert.match(t,/<svg[\s\S]*role="img"[\s\S]*<\/svg>/,id);assert.doesNotMatch(t,/<p>\s*<\/p>/,id);}
  // ellipsbågar ritas med Bézierkurvor, inte A-kommandon som granskaren tar för vinkelbågar
  for(const id of [...NYA,...FIGTILL])assert.doesNotMatch(get(id).t,/d="[^"]*A\d/,id);
  assert.match(get('7.545').t,/5 m lång och 3 m bred/);
});

test('Facit räknas om',()=>{
  const n=(id,v,tol=1e-9)=>assert.ok(Math.abs(get(id).rättSvar-v)<=tol,`${id}: ${get(id).rättSvar} ≠ ${v}`);
  n('4.700',30);n('4.701',24);n('4.702',64);n('4.703',Math.PI*16*12);n('4.704',375);n('4.706',Math.PI*9*2/3);n('4.707',4/3*Math.PI*216);
  n('4.708',54);n('4.709',30*20+2*30*12+2*20*12);n('4.710',4*3.5/2*20);n('4.711',6*4*3+4*1.5/2*6);n('4.713',Math.PI*3.5**2*20/1000);n('4.714',30000/(50*30));
  n('4.715',Math.PI*3.8**2*2.5);n('4.716',Math.ceil(1.2*0.8*0.3*1000/30));
  n('4.717',40);n('4.718',34);n('4.719',35);n('4.720',14);n('4.721',25*Math.PI);n('4.722',26*Math.PI);n('4.723',28);n('4.724',81);n('4.725',6*3+6*2/2);
  n('4.726',8*Math.PI);n('4.727',(10+6)*4/2);n('4.728',2400-100*Math.PI);n('4.730',16*Math.PI);n('4.731',7140);n('4.732',7.5);n('4.733',280+40*Math.PI);
  n('1.1500',16);n('1.1501',17);n('1.1502',27);n('1.1504',81);n('1.1505',11);n('1.1506',15);n('1.1507',22);n('1.1508',12);n('1.1510',10);n('1.1512',7);n('1.1516',18);
  n('1.1509',51);assert.equal(get('1.1511').rättSvar,'blå');
  n('7.700',2.5);n('7.701',8);n('7.702',10);n('7.704',16);n('7.705',60);n('7.706',17*87/100,0.05);n('7.710',12.5);n('7.711',20000);n('7.713',0.005,1e-4);
  assert.equal(get('7.707').rättSvar,'1:50');assert.equal(get('7.707').svarFormat,'skala');
  for(const id of NYA.filter(id=>get(id).svarstyp==='alternativ'))assert.equal(get(id).alternativ.filter(a=>a.ratt).length,1,id);
});

test('Frågorna anger svarsform',()=>{
  for(const id of NYA){const t=get(id);if(t.svarstyp==='alternativ')continue;assert.match(st(t.t),/\((Svara|Svara med)[^)]*\.\)|Skriv ett uttryck/,id);}
});
