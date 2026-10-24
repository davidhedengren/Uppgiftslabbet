'use strict';
/* Ma2 2026-10-24 omgång 2: nivå 1 och variation i kap 2 (kvadratkomplettering, pq-formeln, rötter och koefficienter,
   mer om andragradsekvationer, från graf till formel, symmetrilinje och extrempunkt samt tillämpningar). */
const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('node:fs'),vm=require('node:vm'),path=require('node:path');
const c={window:{}};vm.runInNewContext(fs.readFileSync(path.join(__dirname,'..','uppgifterma2.js'),'utf8'),c);
const B=JSON.parse(JSON.stringify(Object.values(c.window).find(Array.isArray)));const get=id=>{const t=B.find(x=>x.id===id);assert.ok(t,id);return t;};
const NYA=Array.from({length:97},(_,i)=>`2.${1000+i}`);

const fn=(s,vars=['x'])=>{let e=String(s).replace(/^[a-zA-Z](\([a-z]\))?=/,'').replace(/=0$/,'').replace(/sqrt/g,'Q').replace(/\^/g,'**')
  .replace(/(\d|\))\s*(?=[a-zA-Z(Q])/g,'$1*').replace(/([a-zA-Z])(?=[a-zA-Z(Q])/g,'$1*').replace(/Q\*?/g,'Math.sqrt').replace(/(^|\()-/g,'$1-1*');
  return new Function(...vars,`return ${e};`);};
const samma=(id,ratt)=>{const f=fn(get(id).rättSvar),g=fn(ratt);
  for(const x of [-2.5,0.5,3,7])assert.ok(Math.abs(f(x)-g(x))<1e-9,`${id}: ${get(id).rättSvar} ≠ ${ratt}`);};
const pq=(p,q)=>{const d=p*p/4-q;return d<0?[]:[...new Set([-p/2-Math.sqrt(d),-p/2+Math.sqrt(d)])].sort((a,b)=>a-b);};
const lika=(id,v,tol=1e-9)=>{const r=[].concat(get(id).rättSvar).map(Number).sort((a,b)=>a-b),w=[].concat(v).sort((a,b)=>a-b);
  assert.equal(r.length,w.length,id);r.forEach((x,i)=>assert.ok(Math.abs(x-w[i])<=tol,`${id}: ${r} ≠ ${w}`));};
const n=(id,x)=>assert.ok(Math.abs(Number(get(id).rättSvar)-x)<1e-9,`${id}: ${get(id).rättSvar} ≠ ${x}`);
const u=(id,s)=>assert.deepEqual(get(id).rättSvar,s,id);

test('97 nya kort i åtta områden i Ma2 kap 2 utan dubblettfacit och med rätt kurstaggar',()=>{
  const per={};for(const id of NYA){const t=get(id);per[t.omr]=(per[t.omr]||0)+1;assert.equal(t.kap,2,id);assert.ok([1,2].includes(t.traningsniva),id);}
  assert.deepEqual(per,{kvadratkomplettering:12,losningsformel_andragrad:12,samband_roter_koefficienter:12,mer_om_andragradsekvationer:13,
    fran_graf_till_formel:12,symmetrilinje_extrempunkt:12,andragradsekvationer_tillampningar:12,andragradsfunktioner_tillampningar:12});
  assert.ok(NYA.filter(id=>get(id).traningsniva===1).length>=60);
  const kurs={kvadratkomplettering:['2c'],samband_roter_koefficienter:['2b','2c'],mer_om_andragradsekvationer:['2b','2c']};
  for(const id of NYA){const t=get(id);assert.deepEqual(t.kurs,kurs[t.omr]||['2a','2b','2c'],id);}
  const v=x=>{const r=x.rättSvar,s=(Array.isArray(r)?JSON.stringify(r):String(r)).replace(/\s|\\\(|\\\)/g,''),m=Number(s);return isNaN(m)?s:String(Math.round(m*1e6)/1e6);};
  for(const id of NYA){const t=get(id);if(t.svarstyp==='alternativ')continue;
    const krock=B.filter(w=>w.omr===t.omr&&w.id!==id&&w.svarstyp!=='alternativ'&&w.rättSvar!=null&&v(w)===v(t)).map(w=>w.id);
    assert.deepEqual(krock,[],`${id} har samma facit som ${krock}`);}
  for(const id of NYA.filter(id=>get(id).svarstyp==='alternativ'))assert.equal(get(id).alternativ.filter(a=>a.ratt).length,1,id);
  for(const id of NYA.filter(id=>get(id).svarstyp==='mängd'))assert.equal(get(id).svarsstruktur,'mängd',id);
});

test('Facit räknas om',()=>{
  // kvadratkomplettering
  n('2.1000',(8/2)**2);n('2.1001',3*3);n('2.1002',(10/2)**2);samma('2.1003','x^2+2x+5');samma('2.1004','x^2-4x+7');samma('2.1005','x^2+6x');samma('2.1006','x^2-12x+30');
  u('2.1007',[-1,-6]);lika('2.1008',pq(-6,-7));lika('2.1010',pq(4,-5));n('2.1011',8-1);
  // pq-formeln
  u('2.1012',[-6,5]);u('2.1013',[4,16-7]);lika('2.1015',pq(2,-15));lika('2.1016',pq(-10,16));n('2.1017',pq(6,9)[0]);assert.equal(pq(2,5).length,0);
  assert.deepEqual(get('2.1019').rättSvar.map(s=>fn(s,[])()).sort((a,b)=>a-b).map(x=>x.toFixed(12)),pq(-4,-1).map(x=>x.toFixed(12)));
  lika('2.1020',pq(3,-2).map(x=>Math.round(x*100)/100));lika('2.1021',pq(-4,3));lika('2.1022',pq(-4,-12));assert.deepEqual(pq(6,-16),[-8,2]);
  // rötter och koefficienter
  const rotOk=(id,r)=>{const f=fn(get(id).rättSvar);for(const x of r)assert.ok(Math.abs(f(x))<1e-9,`${id}: ${x}`);assert.equal(fn(get(id).rättSvar)(0),r.reduce((a,b)=>a*b,1),id);};
  rotOk('2.1024',[2,3]);rotOk('2.1025',[-1,4]);rotOk('2.1026',[0,6]);rotOk('2.1027',[3,3]);
  n('2.1028',pq(3,-10).reduce((a,b)=>a*b));n('2.1029',pq(5,2).reduce((a,b)=>a+b));n('2.1030',pq(-11,24).reduce((a,b)=>a*b));n('2.1032',10-3);u('2.1033',[-(-1+3),-1*3]);n('2.1034',1*6);
  // mer om andragradsekvationer
  n('2.1036',pq(-4,4).length);n('2.1038',pq(-4,1-2).length);lika('2.1039',pq(-4,0));lika('2.1040',[-2,-1,1,2]);for(const x of get('2.1040').rättSvar)assert.equal(x**4-5*x*x+4,0);
  lika('2.1041',[-2-5,-2+5]);lika('2.1042',[0.5,-3]);lika('2.1043',pq(-5,-6));n('2.1044',(10-4)/2);n('2.1045',25);lika('2.1047',[-4,4]);lika('2.1048',pq(-6,8));
  // från graf till formel
  n('2.1049',3);samma('2.1051','(x-2)*(x-5)');samma('2.1052','x*x-2*x-3');samma('2.1053','(x+3)*(x-1)');n('2.1054',-2*3);n('2.1055',6-2);samma('2.1056','-x*(x-4)');
  n('2.1058',-2);samma('2.1059','8-2*x*x');lika('2.1060',pq(-1,-6));
  // symmetrilinje och extrempunkt
  n('2.1061',(-4+2)/2);u('2.1062',[-3,2]);u('2.1063',[4,7]);u('2.1065',[5,(5-2)*(5-8)]);n('2.1066',3);n('2.1067',16-32+10);n('2.1068',-4+8+5);n('2.1069',(-3+5)/2);n('2.1070',(-2+6)/2);u('2.1071',[2,1]);n('2.1072',6);
  // tillämpningar
  n('2.1073',Math.sqrt(81));n('2.1074',pq(2,-63)[1]);lika('2.1075',[-9,9]);lika('2.1076',pq(3,-40));n('2.1077',6);n('2.1078',pq(1,-420)[1]);
  lika('2.1080',pq(-10,24));lika('2.1081',pq(-3,-10));n('2.1082',pq(2,-120)[1]);lika('2.1083',[pq(1,-56)[1],pq(1,-56)[1]+1]);n('2.1084',1.5);
  const h=t=>-5*t*t+25*t;n('2.1085',h(2));n('2.1086',15);u('2.1087',[3,-5*9+30*3]);n('2.1088',15/5);n('2.1089',5*5);n('2.1090',40/2);n('2.1093',6*6);
  n('2.1094',4/0.5);u('2.1095',pq(-4,3));n('2.1096',Math.sqrt(180/5));
});
