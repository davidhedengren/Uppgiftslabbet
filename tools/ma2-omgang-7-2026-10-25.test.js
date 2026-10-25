'use strict';
/* Ma2 2026-10-25 omgång 7: de tunnaste områdena (under 20 kort på nivå 1–2) fylls på med nivå 1, 2 och 3:
   andragradsfunktioner, potensfunktioner, jämföra exponential/potens, exponentialgrafer, rotekvationer och speciella ekvationssystem. */
const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('node:fs'),vm=require('node:vm'),path=require('node:path');
const c={window:{}};vm.runInNewContext(fs.readFileSync(path.join(__dirname,'..','uppgifterma2.js'),'utf8'),c);
const B=JSON.parse(JSON.stringify(Object.values(c.window).find(Array.isArray)));const get=id=>{const t=B.find(x=>x.id===id);assert.ok(t,id);return t;};
const NYA=[...Array.from({length:58},(_,i)=>`2.${1159+i}`),...Array.from({length:11},(_,i)=>`1.${1163+i}`)];
const n=(id,x)=>assert.ok(Math.abs(Number(get(id).rättSvar)-x)<1e-9,`${id}: ${get(id).rättSvar} ≠ ${x}`);
const u=(id,s)=>assert.deepEqual(get(id).rättSvar,s,id);
const rot=(id,f,k)=>{const r=get(id).rättSvar;for(const x of r)assert.ok(Math.abs(f(x))<1e-9,`${id}: ${x}`);assert.equal(new Set(r).size,k,id);};
const poly=(id,f)=>{const e=String(get(id).rättSvar).replace(/\^/g,'**').replace(/(\d)(?=x)/g,'$1*').replace(/^-x/,'-1*x');const g=Function('x',`return ${e};`);
  for(const x of [-2,0.5,3,7])assert.ok(Math.abs(g(x)-f(x))<1e-9,`${id}: ${get(id).rättSvar}`);};

test('69 nya kort på nivå 1–3 i de tunnaste Ma2-områdena',()=>{
  const per={},niv={1:0,2:0,3:0};
  for(const id of NYA){const t=get(id);per[t.omr]=(per[t.omr]||0)+1;niv[t.traningsniva]++;if(t.traningsniva===3)assert.equal(t.niva,'C',id);}
  assert.deepEqual(per,{andragradsfunktioner:12,potensfunktioner:12,jamfora_exponential_potens:12,exponentialgraf:12,rotekvationer:10,speciella_ekvationssystem:11});
  assert.deepEqual(niv,{1:29,2:23,3:17});
  const kurs={potensfunktioner:['2a'],jamfora_exponential_potens:['2b','2c'],rotekvationer:['2c']};
  for(const id of NYA){const t=get(id);assert.deepEqual(t.kurs,kurs[t.omr]||['2a','2b','2c'],id);}
  const v=x=>{const r=x.rättSvar,s=(Array.isArray(r)?JSON.stringify(r):String(r)).replace(/\s|\\\(|\\\)/g,''),m=Number(s);return isNaN(m)?s:String(Math.round(m*1e6)/1e6);};
  for(const id of NYA){const t=get(id);if(t.svarstyp==='alternativ')continue;
    const krock=B.filter(w=>w.omr===t.omr&&w.id!==id&&w.svarstyp!=='alternativ'&&w.rättSvar!=null&&v(w)===v(t)).map(w=>w.id);
    assert.deepEqual(krock,[],`${id} har samma facit som ${krock}`);}
  for(const id of NYA.filter(id=>get(id).svarstyp==='alternativ')){const a=get(id).alternativ;assert.equal(a.filter(x=>x.ratt).length,1,id);
    if(!a.every(x=>/^[A-H]$/.test(x.txt)))assert.ok(!a[0].ratt,`${id}: rätt svar först`);}
});

test('Facit räknas om',()=>{
  // andragradsfunktioner
  n('2.1159',1+3+2);n('2.1161',-7);rot('2.1162',x=>(x-1)*(x+6),2);rot('2.1164',x=>2*x*x-8,2);rot('2.1165',x=>x*x-4*x-5,2);n('2.1166',(13+3)/4);
  poly('2.1167',x=>-(x-1)*(x-5));rot('2.1168',k=>(k/2)**2-9,2);n('2.1169',2+9);poly('2.1170',x=>x*x-4*x+3);assert.equal(0*0-4*0+3,3);assert.equal(1-4+3,0);
  // potensfunktioner
  n('2.1171',5*9);n('2.1172',2*(-2)**3);n('2.1174',0.5*3**4);n('2.1175',Math.sqrt(50/2));n('2.1176',3**2);n('2.1177',Math.round((1.1**3-1)*1000)/10);n('2.1178',56/8);
  u('2.1179',[0.5,3]);assert.equal(0.5*3**3,13.5);n('2.1180',25/4);n('2.1181',1/4);u('2.1182',[3,3]);assert.equal(3*4**3,192);
  // jämföra exponential och potens
  u('2.1185',[3**2,2**3]);u('2.1187',[Math.cbrt(64),Math.log(64)/Math.log(4)].map(Math.round));n('2.1189',4);assert.equal(4**2,2**4);
  const t=[...Array(30).keys()].slice(1).find(t=>1000*1.05**t>1000+65*t);n('2.1190',t);u('2.1192',[(8/4)**3,3**4]);
  for(const x of [1,2,3,4,5])assert.ok(!(x**3>3**x),x);
  // exponentialgrafer
  u('2.1195',[5,10]);n('2.1196',40*0.5**2);n('2.1198',3*2**4);n('2.1199',0);n('2.1200',Math.log2(48/1.5));n('2.1201',(1-35/50)*100);n('2.1202',6);assert.equal(80*0.5**(12/6),20);
  n('2.1203',Math.log(32)/Math.log(4));assert.equal(get('2.1204').rättSvar,'3*2^x');assert.equal(3*2**1,6);assert.equal(3*2**3,24);n('2.1205',50/0.5**2);
  // rotekvationer
  n('2.1207',81);n('2.1208',25+3);n('2.1209',100/5);n('2.1212',(49+2)/3);n('2.1213',16-5);rot('2.1214',x=>Math.sqrt(x*x-16)-3,2);n('2.1215',25);
  assert.equal(Math.sqrt(25),25-20);assert.notEqual(Math.sqrt(16),16-20);assert.ok(Math.abs(get('2.1216').rättSvar-196/19.64)<1e-9);
  // speciella ekvationssystem
  n('1.1165',-2);n('1.1166',-3);n('1.1168',2*5);u('1.1171',[2,6]);n('1.1172',10/2);n('1.1173',3+1);
});
