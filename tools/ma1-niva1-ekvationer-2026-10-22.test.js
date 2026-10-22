'use strict';
/* Påfyllnad 2026-10-22: 86 kort på nivå 1 i Ma1:s ekvationsområden (1.1300–1.1385), som Ma1a läser v.43–46. */
const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('node:fs'),vm=require('node:vm'),path=require('node:path');
const c={window:{}};vm.runInNewContext(fs.readFileSync(path.join(__dirname,'..','uppgifterma1.js'),'utf8'),c);
const B=JSON.parse(JSON.stringify(Object.values(c.window).find(Array.isArray)));
const nya=B.filter(t=>{const [k,n]=t.id.split('.').map(Number);return k===1&&n>=1300&&n<=1385;});
const get=id=>{const t=nya.find(x=>x.id===id);assert.ok(t,id);return t;};

test('86 kort på nivå 1 fördelade på fyra ekvationsområden',()=>{
  assert.equal(nya.length,86);const per={};
  for(const t of nya){per[t.omr]=(per[t.omr]||0)+1;
    assert.equal(t.traningsniva,1,t.id);assert.deepEqual(t.kurs,['1a','1b','1c'],t.id);assert.equal(t.poang,'1/0/0',t.id);
    if(t.svarstyp==='alternativ')assert.equal(t.alternativ.filter(a=>a.ratt).length,1,t.id);
    if(/^<p>(Lös ekvationen|Förenkla)/.test(t.t))assert.equal(t.miniräknare,false,t.id);
  }
  assert.deepEqual(per,{ekv_flera_variabeltermer:24,ekv_parenteser:22,ekv_brak:20,ekv_problemlosning:20});
});

test('Facit löser ekvationerna',()=>{
  // id: [vänsterled, högerled] som funktioner av x
  const E={'1.1300':[x=>5*x,x=>2*x+12],'1.1301':[x=>4*x+3,x=>2*x+11],'1.1302':[x=>8*x-6,x=>5*x],'1.1305':[x=>3*x+5,x=>x+13],
    '1.1306':[x=>2*x+5,x=>4*x-1],'1.1307':[x=>2*x+1,x=>-x+7],'1.1310':[x=>10-x,x=>x+2],'1.1311':[x=>2*x+9,x=>5*x+15],'1.1312':[x=>3*x,x=>40+x],
    '1.1313':[x=>20-2*x,x=>14-x],'1.1314':[x=>1.5*x+2,x=>0.5*x+6],'1.1318':[x=>200+30*x,x=>500+10*x],'1.1319':[x=>120+15*x,x=>30+25*x],
    '1.1320':[x=>4*x,x=>2*x+12],'1.1321':[x=>x+11,x=>4*x+2],'1.1323':[x=>7*x-9,x=>4*x-3],
    '1.1324':[x=>2*(x+3),x=>14],'1.1325':[x=>3*(x-1),x=>2*x+5],'1.1326':[x=>-(x-4),x=>1],'1.1327':[x=>12-(x-3),x=>10],'1.1330':[x=>4*x,x=>3*(x+2)],
    '1.1331':[x=>4*(x+25),x=>380],'1.1332':[x=>3*(2*x-1),x=>15],'1.1333':[x=>6*(x+4),x=>42],'1.1335':[x=>2*(x+5),x=>3*(x+2)],'1.1336':[x=>-2*(x-3),x=>4],
    '1.1337':[x=>4*(x+3),x=>32],'1.1339':[x=>3*(x+2),x=>18],'1.1340':[x=>4*(x-2)+3,x=>11],'1.1341':[x=>2*(x-4),x=>x],'1.1342':[x=>2*(x+10),x=>32],
    '1.1343':[x=>3*x,x=>20-(x+4)],'1.1344':[x=>2*(x+1),x=>7],
    '1.1346':[x=>x/4,x=>6],'1.1347':[x=>x/5-2,x=>1],'1.1348':[x=>2*x/3,x=>8],'1.1349':[x=>(x+3)/2,x=>7],'1.1350':[x=>(x+10)/2,x=>8],'1.1351':[x=>x/3,x=>145],
    '1.1353':[x=>12/x,x=>3],'1.1355':[x=>x/3,x=>9],'1.1359':[x=>3*x/4,x=>9],'1.1360':[x=>(x-1)/3,x=>4],'1.1361':[x=>x/2+3,x=>10],'1.1363':[x=>x/4,x=>3],'1.1364':[x=>2*x/5,x=>4],
    '1.1366':[x=>3*x+5,x=>26],'1.1367':[x=>4*x+30,x=>230],'1.1369':[x=>45+12*x,x=>189],'1.1370':[x=>4*x,x=>48],'1.1371':[x=>3*x+60,x=>180],'1.1372':[x=>300+2*x,x=>100+4*x],
    '1.1373':[x=>3*x+3,x=>48],'1.1374':[x=>3*x,x=>27],'1.1375':[x=>5*x+3,x=>43],'1.1376':[x=>130*x+200,x=>2280],'1.1377':[x=>2*x-7,x=>25],'1.1378':[x=>2*x+10,x=>34],
    '1.1379':[x=>99*x,x=>594],'1.1381':[x=>2*x-8,x=>30],'1.1382':[x=>2*x+4,x=>20],'1.1383':[x=>4*x,x=>36],'1.1384':[x=>600+150*x,x=>2400],'1.1385':[x=>40*x,x=>60+25*x]};
  for(const [id,[v,h]] of Object.entries(E)){const x=get(id).rättSvar;assert.ok(Math.abs(v(x)-h(x))<1e-9,`${id}: x=${x}`);}
  assert.equal(get('1.1315').rättSvar,12-6);assert.equal(get('1.1316').rättSvar,25/5);assert.equal(get('1.1356').rättSvar,12/3+12/6);
  assert.deepEqual(['1.1352','1.1357','1.1358'].map(id=>get(id).rättSvar),['x','2x','x/2']);
  const ratt=id=>get(id).alternativ.find(a=>a.ratt).txt;
  assert.equal(ratt('1.1308'),'Ingen lösning');assert.equal(ratt('1.1309'),'Oändligt många lösningar');assert.equal(ratt('1.1322'),'3');assert.equal(ratt('1.1380'),'12');
});
