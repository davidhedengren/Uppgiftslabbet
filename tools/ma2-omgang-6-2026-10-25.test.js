'use strict';
/* Ma2 2026-10-25 omgång 6: varierade kort på nivå 2 och 3 i kap 2 (logaritmbegreppet, exponentialfunktioner, rotekvationer,
   enkla andragradsekvationer, nollproduktmetoden, potensekvationer). */
const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('node:fs'),vm=require('node:vm'),path=require('node:path');
const c={window:{}};vm.runInNewContext(fs.readFileSync(path.join(__dirname,'..','uppgifterma2.js'),'utf8'),c);
const B=JSON.parse(JSON.stringify(Object.values(c.window).find(Array.isArray)));const get=id=>{const t=B.find(x=>x.id===id);assert.ok(t,id);return t;};
const NYA=Array.from({length:62},(_,i)=>`2.${1097+i}`);
const val=s=>typeof s==='number'?s:Function(`return ${String(s).replace(/sqrt/g,'Math.sqrt')};`)();
const n=(id,x)=>assert.ok(Math.abs(val(get(id).rättSvar)-x)<1e-9,`${id}: ${get(id).rättSvar} ≠ ${x}`);
const u=(id,s)=>assert.deepEqual(get(id).rättSvar,s,id);
const rot=(id,f,antal)=>{const r=get(id).rättSvar.map(val);for(const x of r)assert.ok(Math.abs(f(x))<1e-9,`${id}: ${x}`);assert.equal(new Set(r).size,antal,id);};
const inom=(id,x)=>{const t=get(id);assert.ok(Math.abs(t.rättSvar-x)<1e-9,`${id}: ${t.rättSvar} ≠ ${x}`);};

test('62 nya kort på nivå 2 och 3 i Ma2 kap 2, utan dubblettfacit och med rätt kurstaggar',()=>{
  const per={},niv={2:0,3:0};
  for(const id of NYA){const t=get(id);per[t.omr]=(per[t.omr]||0)+1;niv[t.traningsniva]++;assert.equal(t.kap,2,id);assert.ok([2,3].includes(t.traningsniva),id);
    if(t.traningsniva===3){assert.equal(t.niva,'C',id);assert.equal(t.poang,'0/1/0',id);}}
  assert.deepEqual(per,{logaritmbegreppet:11,exponentialfunktioner:11,rotekvationer:10,enkla_andragradsekvationer:10,nollproduktmetoden:10,potensekvationer:10});
  assert.deepEqual(niv,{2:30,3:32});
  const kurs={logaritmbegreppet:['2b','2c'],rotekvationer:['2c']};
  for(const id of NYA){const t=get(id);assert.deepEqual(t.kurs,kurs[t.omr]||['2a','2b','2c'],id);}
  const v=x=>{const r=x.rättSvar,s=(Array.isArray(r)?JSON.stringify(r):String(r)).replace(/\s|\\\(|\\\)/g,''),m=Number(s);return isNaN(m)?s:String(Math.round(m*1e6)/1e6);};
  for(const id of NYA){const t=get(id);if(t.svarstyp==='alternativ')continue;
    const krock=B.filter(w=>w.omr===t.omr&&w.id!==id&&w.svarstyp!=='alternativ'&&w.rättSvar!=null&&v(w)===v(t)).map(w=>w.id);
    assert.deepEqual(krock,[],`${id} har samma facit som ${krock}`);}
  for(const id of NYA.filter(id=>get(id).svarstyp==='alternativ')){const a=get(id).alternativ;assert.equal(a.filter(x=>x.ratt).length,1,id);assert.ok(!a[0].ratt,id);}
  // decimalsvar: frågan anger precisionen och toleransen är högst ett halvt avrundningssteg
  for(const id of NYA){const t=get(id);if(t.svarstyp!=='numeriskt'||!t.tolerans)continue;assert.match(t.t,/\((Svara|svara)[^)]*(decimal|heltal|värdesiffror)[^)]*\)/,id);}
});

test('Facit räknas om',()=>{
  // logaritmer
  inom('2.1097',Math.log10(500));u('2.1098',[3,4]);inom('2.1099',Math.log10(60/3));n('2.1100',100-3);n('2.1101',2.5+1.5);n('2.1102',5);n('2.1103',4-1);
  inom('2.1104',10**-3.2);inom('2.1105',10*Math.log10(2));n('2.1106',1e6/1e4);n('2.1107',Math.sqrt(100));
  // exponentialfunktioner
  inom('2.1108',(1.03**10-1)*100);n('2.1109',Math.round((1-0.8*1.2)*100));n('2.1110',1000*0.5**3);n('2.1111',3*4**5);n('2.1112',50*0.8**3);inom('2.1113',(1.25**0.25-1)*100);
  n('2.1114',[1,2,3,4,5,6,7].find(k=>0.85**k<0.5));u('2.1115',[5,2]);n('2.1116',9/Math.log2(80/10));inom('2.1117',100/1.02**10);
  // rotekvationer: varje svar uppfyller den ursprungliga ekvationen
  const ok=(id,f)=>{for(const x of [].concat(get(id).rättSvar).map(val))assert.ok(Math.abs(f(x))<1e-9,`${id}: ${x}`);};
  ok('2.1119',x=>Math.sqrt(x)+3-7);ok('2.1120',x=>2*Math.sqrt(x-1)-6);rot('2.1121',x=>Math.sqrt(x*x+9)-5,2);ok('2.1122',x=>Math.sqrt(5*x+1)-Math.sqrt(2*x+7));
  ok('2.1124',x=>Math.sqrt(x+1)-(x-5));assert.notEqual(Math.sqrt(3+1),3-5);ok('2.1125',x=>x-Math.sqrt(3*x+10));ok('2.1126',x=>Math.sqrt(2*x+7)-(x+2));
  inom('2.1127',9.82*(2/(2*Math.PI))**2);inom('2.1128',3**2*9.82/2);
  // enkla andragradsekvationer
  rot('2.1129',x=>(2*x-1)**2-49,2);n('2.1130',Math.sqrt(50)-2);n('2.1131',10-2);inom('2.1132',Math.sqrt(20/4.91));rot('2.1133',x=>x*x-(2*x*x-8),2);
  n('2.1134',5);assert.deepEqual([5+4,5-4],[9,1]);n('2.1135',(Math.sqrt(1.21)-1)*100);n('2.1136',-5);inom('2.1137',Math.sqrt(50));rot('2.1138',x=>(x*x-3)**2-1,4);
  // nollproduktmetoden
  rot('2.1139',x=>x*x+6*x-7*x,2);rot('2.1140',x=>(3*x-6)*(x+2),2);rot('2.1141',x=>x**3-7*x*x,2);rot('2.1142',x=>(x-2)*(x+3)-(x-2)*(2*x-1),2);
  rot('2.1143',x=>x*(x-3)*(2*x+1),3);n('2.1144',20/5);n('2.1145',5);assert.equal(2*5*(5-3),4*5);u('2.1146',[4,-1]);rot('2.1147',x=>(x*x-4)*(x*x-9),4);
  // potensekvationer
  rot('2.1149',x=>x**4-81,2);n('2.1150',-2);n('2.1151',1+Math.cbrt(-8));inom('2.1152',Math.cbrt(3*1000/(4*Math.PI)));n('2.1153',36);n('2.1154',27**(2/3));
  inom('2.1155',Math.cbrt(2));inom('2.1156',1.2**0.25);rot('2.1157',x=>(x+2)**4-16,2);u('2.1158',[1,0]);
});
