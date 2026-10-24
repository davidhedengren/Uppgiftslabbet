'use strict';
/* Ma1 2026-10-24 omgång E: förhållanden, proportionalitet (grunder), amortering, bråkräkning, ränta, risk och säkerhet. */
const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('node:fs'),vm=require('node:vm'),path=require('node:path');
const c={window:{}};vm.runInNewContext(fs.readFileSync(path.join(__dirname,'..','uppgifterma1.js'),'utf8'),c);
const B=JSON.parse(JSON.stringify(Object.values(c.window).find(Array.isArray)));const get=id=>{const t=B.find(x=>x.id===id);assert.ok(t,id);return t;};
const ids=(k,a,b)=>Array.from({length:b-a+1},(_,i)=>`${k}.${a+i}`);
const NYA=[...ids(0,1220,1252),...ids(3,660,681),...ids(5,630,640)];

test('66 nya kort, rätt områden, figurer och inga dubblettfacit',()=>{
  const per={};for(const id of NYA){const t=get(id);per[t.omr]=(per[t.omr]||0)+1;assert.ok([1,2,3,4].includes(t.traningsniva),id);}
  assert.deepEqual(per,{forhallanden:11,proportionalitet_grunder:11,amortering:11,brakrakning:11,ranta:11,risk_sakerhet:11});
  assert.ok(NYA.filter(id=>/<svg|<table/.test(get(id).t)).length>=36);
  const v=x=>{const s=String(x.rättSvar).replace(/\s/g,''),n=Number(s);return isNaN(n)?s:String(Math.round(n*1e6)/1e6);};
  for(const id of NYA){const t=get(id);if(t.svarstyp==='alternativ')continue;
    const krock=B.filter(u=>u.omr===t.omr&&u.id!==id&&u.svarstyp!=='alternativ'&&u.rättSvar!=null&&!Array.isArray(u.rättSvar)&&v(u)===v(t)).map(u=>u.id);
    assert.deepEqual(krock,[],`${id} har samma facit som ${krock}`);}
});

test('Facit räknas om',()=>{
  const n=(id,x,tol=1e-6)=>assert.ok(Math.abs(Number(get(id).rättSvar)-x)<=tol,`${id}: ${get(id).rättSvar} ≠ ${x}`);const u=(id,s)=>assert.equal(get(id).rättSvar,s,id);
  const by=(omr,fr)=>NYA.filter(id=>get(id).omr===omr&&get(id).svarstyp!=='alternativ')[fr];
  u('0.1220','2:5');n('0.1221',72/9*5);n('0.1222',15);u('0.1223','2/5');n('0.1224',16/8*5);n('0.1225',21);n('0.1226',84/21*9);u('0.1227','18:17');n('0.1229',8*2/5);n('0.1230',27/3*7);
  n('0.1231',75);n('0.1232',120);n('0.1234',1.5);n('0.1235',18*35/60);n('0.1236',5);n('0.1237',40);n('0.1238',6*(170/5-130/5));n('0.1240',250/5);n('0.1241',145*0.62);
  u('0.1242','7/12');u('0.1243','1/6');u('0.1244','3/5');u('0.1245','8/3');n('0.1246',8);u('0.1247','3/10');n('0.1248',25);n('0.1249',40);u('0.1250','4/7');n('0.1252',28);
  n('3.660',12000);n('3.661',30);n('3.662',240);n('3.663',2750);n('3.664',5400);n('3.666',840);n('3.667',850);n('3.668',0.5);n('3.669',30000);n('3.670',3900);
  n('3.671',360);n('3.672',3.5);n('3.673',10816*1.04,1e-6);n('3.674',8000*1.05**10,1e-3);n('3.676',1050);n('3.678',7);n('3.679',8000);n('3.680',4.5);n('3.681',10000*1.03**2+10000*1.03);
  n('5.630',4);n('5.631',15);n('5.632',7.5);n('5.633',270);n('5.635',0.12);n('5.636',60);n('5.637',0.3);n('5.638',24);n('5.639',2);n('5.640',-5);
  for(const id of NYA.filter(id=>get(id).svarstyp==='alternativ'))assert.equal(get(id).alternativ.filter(a=>a.ratt).length,1,id);
});
