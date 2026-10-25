'use strict';
/* Ma1 2026-10-25: 26 kort på nivå 3 i de tunnaste områdena enligt NIVAINVENTERING_2026-10-25 (urval, felkällor/signifikans,
   korrelation/kausalitet och intervall), 5.665–5.684 och 1.1551–1.1556. Facit räknas om. */
const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('node:fs'),vm=require('node:vm'),path=require('node:path');
const c={window:{}};vm.runInNewContext(fs.readFileSync(path.join(__dirname,'..','uppgifterma1.js'),'utf8'),c);
const B=JSON.parse(JSON.stringify(Object.values(c.window).find(Array.isArray)));const get=id=>{const t=B.find(x=>x.id===id);assert.ok(t,id);return t;};
const NYA=[...Array.from({length:20},(_,i)=>`5.${665+i}`),...Array.from({length:6},(_,i)=>`1.${1551+i}`)];
const n=(id,x)=>assert.ok(Math.abs(Number(get(id).rättSvar)-x)<1e-9,`${id}: ${get(id).rättSvar} ≠ ${x}`);
const d=(id,...x)=>{const r=get(id).rättSvar;assert.equal(r.length,x.length,id);x.forEach((v,i)=>assert.ok(Math.abs(r[i]-v)<1e-9,`${id}[${i}]: ${r[i]} ≠ ${v}`));};
const r=p=>{const m=p.length,mx=p.reduce((s,q)=>s+q[0],0)/m,my=p.reduce((s,q)=>s+q[1],0)/m;let a=0,b=0,e=0;for(const [x,y] of p){a+=(x-mx)*(y-my);b+=(x-mx)**2;e+=(y-my)**2;}return a/Math.sqrt(b*e);};

test('26 spelbara nivå 3-kort i rätt områden utan dubblettfacit',()=>{
  const per={};
  for(const id of NYA){const t=get(id);per[t.omr]=(per[t.omr]||0)+1;assert.equal(t.traningsniva,3,id);assert.equal(t.niva,'C',id);assert.equal(t.spel,true,id);
    assert.deepEqual(t.kurs,t.omr==='intervall'?['1b','1c']:['1a','1b','1c'],id);
    if(t.svarstyp==='alternativ'){assert.equal(t.alternativ.filter(a=>a.ratt).length,1,id);assert.ok(!t.alternativ[0].ratt,id);}}
  assert.deepEqual(per,{urvalsmetoder:7,signifikans:6,korrelation:7,intervall:6});
  const v=x=>JSON.stringify(x.rättSvar);
  for(const id of NYA){const t=get(id);if(t.rättSvar==null)continue;
    const krock=B.filter(w=>w.omr===t.omr&&w.id!==id&&w.rättSvar!=null&&v(w)===v(t)).map(w=>w.id);assert.deepEqual(krock,[],`${id}: ${krock}`);}
});

test('Facit räknas om',()=>{
  // urval
  n('5.665',(75-30-27)*1500/75);d('5.666',150/400*100,(150+150)/400*100);n('5.667',7+49*2400/120);
  d('5.668',(120+70)/400*100,0.7*60+0.3*35);n('5.670',(600*0.15+400*0.30)/1000*100);n('5.671',12/0.08);
  // signifikans: minsta heltal x med x−2 > 21+2
  n('5.672',[...Array(40).keys()].find(x=>x-2>21+2));n('5.673',400*(5/2)**2-400);n('5.674',(1014+1006+998+1021+1001)/5-12);
  let p=0;for(let k=14;k<=20;k++){let c=1;for(let j=0;j<k;j++)c=c*(20-j)/(j+1);p+=c;}p/=2**20;assert.ok(Math.abs(p-0.058)<0.001);
  d('5.676',Math.round(0.323*48000),Math.round(0.377*48000));
  // korrelation: koefficienterna i figuren stämmer med texten
  assert.match(get('5.678').t,/0,97, −0,75 och 0,02/);
  d('5.679',(80+20)/200*100,(18+54)/200*100);assert.ok(18/20>80/100&&54/180>20/100);
  n('5.681',0.72);const pts=[[2,34],[3,31],[5,25],[7,19],[10,10]];assert.ok(Math.abs(r(pts)+1)<1e-12);n('5.684',-1);
  // intervall
  assert.equal(get('1.1551').rättSvar,'41<=F<77');assert.equal(1.8*5+32,41);assert.equal(1.8*25+32,77);
  assert.equal(get('1.1552').rättSvar,'5<=x<=17');assert.equal(45+15*17,300);
  assert.equal(get('1.1553').rättSvar,'79.7<=L<=80.5');
  assert.equal(get('1.1554').rättSvar,'-2<=x<=2');assert.equal(3-0.5*2,2);
  assert.equal(get('1.1555').rättSvar,'-3<x<6');
  n('1.1556',[...Array(30).keys()].map(k=>k-10).filter(k=>-2.5<k&&k<=6&&1<=k&&k<9).length);
});
