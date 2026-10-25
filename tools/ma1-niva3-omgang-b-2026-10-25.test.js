'use strict';
/* Ma1 2026-10-25, nivå 3 omgång B: 35 kort i prefix (0.1261–0.1265), linjära olikheter och ekvationer (1.1557–1.1566),
   vektorer (4.820–4.823, 1c) och kap 7 för 1a (7.781–7.796). Facit räknas om. */
const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('node:fs'),vm=require('node:vm'),path=require('node:path');
const c={window:{}};vm.runInNewContext(fs.readFileSync(path.join(__dirname,'..','uppgifterma1.js'),'utf8'),c);
const B=JSON.parse(JSON.stringify(Object.values(c.window).find(Array.isArray)));const get=id=>{const t=B.find(x=>x.id===id);assert.ok(t,id);return t;};
const NYA=[...Array.from({length:5},(_,i)=>`0.${1261+i}`),...Array.from({length:10},(_,i)=>`1.${1557+i}`),...Array.from({length:4},(_,i)=>`4.${820+i}`),...Array.from({length:16},(_,i)=>`7.${781+i}`)];
const n=(id,...x)=>{const r=get(id).rättSvar,a=Array.isArray(r)?r:[r],t=get(id).tolerans,tt=Array.isArray(t)?t:[t];assert.equal(a.length,x.length,id);
  x.forEach((v,i)=>assert.ok(Math.abs(a[i]-v)<=(tt[i]||0)+1e-9*Math.max(1,Math.abs(v)),`${id}[${i}]: ${a[i]} ≠ ${v}`));};

test('35 spelbara nivå 3-kort med rätt kursspår och utan dubblettfacit',()=>{
  const per={};
  for(const id of NYA){const t=get(id);per[t.omr]=(per[t.omr]||0)+1;assert.equal(t.traningsniva,3,id);assert.equal(t.niva,'C',id);assert.equal(t.spel,true,id);
    assert.deepEqual(t.kurs,t.kap===7?['1a']:t.kap===4?['1c']:['1a','1b','1c'],id);
    if(t.svarstyp==='alternativ'){assert.equal(t.alternativ.filter(a=>a.ratt).length,1,id);assert.ok(!t.alternativ[0].ratt,id);}}
  assert.deepEqual(per,{prefix:5,linjara_olikheter:5,linjara_ekvationer:5,vektorer:4,matning_enheter:4,uppskattning_overslag:4,kostnadsberakningar:4,yrkesformler:4});
  const v=x=>JSON.stringify(x.rättSvar);
  for(const id of NYA){const t=get(id);if(t.rättSvar==null)continue;
    const krock=B.filter(w=>w.omr===t.omr&&w.id!==id&&w.rättSvar!=null&&v(w)===v(t)).map(w=>w.id);assert.deepEqual(krock,[],`${id}: ${krock}`);}
});

test('Facit räknas om',()=>{
  // prefix
  n('0.1261',Math.floor(2e12/4.5e6));n('0.1262',Math.floor(1e-3/120e-9));n('0.1263',Math.round(25e-6/(50e-9)**2));n('0.1264',3.6e6*2400/1e9);n('0.1265',3e9*8/250e6);
  // olikheter och ekvationer
  n('1.1557',Math.ceil((149-49)/2.5)-1);assert.equal(get('1.1558').rättSvar,'x<=3');for(const x of [3,2.9])assert.ok(-3*(x-2)>=2*x-9);assert.ok(!(-3*(3.1-2)>=2*3.1-9));
  n('1.1560',Math.floor(3600/90)+1);assert.equal(get('1.1561').rättSvar,'-4<x<=4');
  n('1.1562',(20+3-12)/2);n('1.1563',21);assert.equal(3*21+21,2*(21+21));n('1.1564',(4.4-3)/0.4);n('1.1566',(190*25-220*25)/(160-220));
  // vektorer
  n('4.820',-2+7,5-3);n('4.822',(13-1)/(5-1));n('4.823',Math.hypot(12-3,-5+9));
  // mätning
  n('7.781',8*4*1.4*1000/25/60);n('7.782',600*24*7.85/1000);n('7.783',500/4,500-500/4*2.25);n('7.784',10000/2910,10/(2910/3600));
  // överslag
  n('7.785',4.65*3.25);n('7.787',Math.ceil(2*(5.2+3.9)*2.4*2/8/3));n('7.788',70*60*24*365);
  // kostnader
  n('7.789',2250*0.8-2250*0.8/1.25);n('7.790',(3*7.5*520+4800)*1.25);n('7.791',1495/1.25/2.3);n('7.792',Math.ceil(18000/(25-3.5)));
  // yrkesformler
  n('7.793',3100/230);n('7.794',200*0.4/0.15-200);n('7.795',1.2/4.8*100,0.25*7.5);n('7.796',0.1*70/2*60);
});
