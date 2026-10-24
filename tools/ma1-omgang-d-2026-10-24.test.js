'use strict';
/* Ma1 2026-10-24 omgång D: programmering, kostnadsberäkningar, linjära ekvationer, bestämma linjär funktion, spill och svinn. */
const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('node:fs'),vm=require('node:vm'),path=require('node:path');
const c={window:{}};vm.runInNewContext(fs.readFileSync(path.join(__dirname,'..','uppgifterma1.js'),'utf8'),c);
const B=JSON.parse(JSON.stringify(Object.values(c.window).find(Array.isArray)));const get=id=>{const t=B.find(x=>x.id===id);assert.ok(t,id);return t;};
const ids=(k,a,b)=>Array.from({length:b-a+1},(_,i)=>`${k}.${a+i}`);
const NYA=[...ids(6,430,441),...ids(7,740,751),...ids(1,1520,1531),...ids(2,620,631),...ids(7,752,763)];

test('60 nya kort, rätt områden, figurer och inga dubblettfacit',()=>{
  const per={};for(const id of NYA){const t=get(id);per[t.omr]=(per[t.omr]||0)+1;assert.ok([1,2,3,4].includes(t.traningsniva),id);}
  assert.deepEqual(per,{programmering:12,kostnadsberakningar:12,linjara_ekvationer:12,bestamma_linjar_funktion:12,spill_svinnostnad:12});
  assert.ok(NYA.filter(id=>/<svg|<table|<code>/.test(get(id).t)).length>=43);
  const v=x=>{const s=String(x.rättSvar).replace(/\s/g,''),n=Number(s);return isNaN(n)?s:String(Math.round(n*1e6)/1e6);};
  for(const id of NYA){const t=get(id);if(t.svarstyp==='alternativ')continue;
    const krock=B.filter(u=>u.omr===t.omr&&u.id!==id&&u.svarstyp!=='alternativ'&&u.rättSvar!=null&&!Array.isArray(u.rättSvar)&&v(u)===v(t)).map(u=>u.id);
    assert.deepEqual(krock,[],`${id} har samma facit som ${krock}`);}
  for(const id of NYA)for(const s of get(id).t.match(/<svg[\s\S]*?<\/svg>/g)||[])assert.doesNotMatch(s,/font-family="[^"]*"[^>]*font-family=/,id+' dubbla attribut');
});

test('Facit räknas om',()=>{
  const n=(id,x,tol=1e-6)=>assert.ok(Math.abs(Number(get(id).rättSvar)-x)<=tol,`${id}: ${get(id).rättSvar} ≠ ${x}`);const u=(id,s)=>assert.equal(get(id).rättSvar,s,id);
  n('6.430',3*4+5);n('6.431',(10+6)*3);n('6.432',2+4*3);n('6.433',2*23+1);n('6.435',4);n('6.436',22);n('6.438',45);n('6.439',10.5);n('6.440',6);
  let s=0;for(let i=0;i<3;i++)s=(s+500)*1.05;n('6.441',s,0.006);
  n('7.740',4*560+1950);n('7.741',1250-1250/1.25);n('7.743',8);n('7.744',200*1.4*1.25);n('7.745',1499*0.8);n('7.746',3*2*30*1.8);n('7.747',45.3*19.4,1e-6);n('7.748',(7*600+2400)*1.25);n('7.749',Math.ceil(1500/45));n('7.751',240*1.12);
  n('1.1520',10);n('1.1521',11);n('1.1522',40);n('1.1523',6);n('1.1524',15);n('1.1525',16);n('1.1526',19);n('1.1527',18);n('1.1529',17);n('1.1530',20);n('1.1531',9.5);
  n('2.620',1);n('2.621',-0.5);u('2.622','y=2*x+1');u('2.623','y=16*x+40');n('2.624',15);u('2.625','y=4*x-3');u('2.626','y=3*x-5');n('2.627',300);n('2.628',-1.5);n('2.629',12);n('2.631',77);
  n('7.752',5*4.5*1.1);n('7.753',6);n('7.754',Math.ceil(48/Math.floor(3.6/0.7)));n('7.755',40);n('7.756',Math.ceil(4.2*2.5*1.1/5));n('7.757',20);n('7.758',18*1.1*249);n('7.760',Math.ceil(24*1.08/2.2));n('7.761',12/96*100);n('7.762',126);n('7.763',60);
  for(const id of NYA.filter(id=>get(id).svarstyp==='alternativ'))assert.equal(get(id).alternativ.filter(a=>a.ratt).length,1,id);
});
