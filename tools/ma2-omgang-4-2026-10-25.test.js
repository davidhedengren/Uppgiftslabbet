'use strict';
/* Ma2 2026-10-25 omgång 4: varierade kort på nivå 2 och 3 i kap 1 (parenteser, kvadreringsregler, konjugatregeln,
   faktorisering, linjära representationer, bestämma linjära funktioner, räta linjens ekvation).
   Läraren: påfyllnaden ska vara varierad även på nivå 2 och 3, inte bara nivå 1. */
const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('node:fs'),vm=require('node:vm'),path=require('node:path');
const c={window:{}};vm.runInNewContext(fs.readFileSync(path.join(__dirname,'..','uppgifterma2.js'),'utf8'),c);
const B=JSON.parse(JSON.stringify(Object.values(c.window).find(Array.isArray)));const get=id=>{const t=B.find(x=>x.id===id);assert.ok(t,id);return t;};
const NYA=Array.from({length:73},(_,i)=>`1.${1090+i}`);

const fn=(s,vars=['x'])=>{let e=String(s).replace(/^[a-zA-Z](\([a-z]\))?=/,'').replace(/sqrt/g,'Q').replace(/\^/g,'**')
  .replace(/(\d|\))\s*(?=[a-zA-Z(Q])/g,'$1*').replace(/([a-zA-Z])(?=[a-zA-Z(Q])/g,'$1*').replace(/Q\*?/g,'Math.sqrt').replace(/(^|\()-/g,'$1-1*');
  return new Function(...vars,`return ${e};`);};
const samma=(id,ratt,vars=['x'])=>{const f=fn(get(id).rättSvar,vars),g=fn(ratt,vars);
  for(const p of [[-2.5,1.5],[0.5,-3],[3,2],[7,-1.25]])assert.ok(Math.abs(f(...p)-g(...p))<1e-9,`${id}: ${get(id).rättSvar} ≠ ${ratt}`);};
const genom=(id,pkt)=>{const f=fn(get(id).rättSvar);for(const [a,b] of pkt)assert.ok(Math.abs(f(a)-b)<1e-9,`${id}: (${a}, ${b})`);};
const n=(id,x)=>assert.ok(Math.abs(Number(get(id).rättSvar)-x)<1e-9,`${id}: ${get(id).rättSvar} ≠ ${x}`);
const u=(id,s)=>assert.deepEqual(get(id).rättSvar,s,id);
const rot=(id,f)=>{for(const r of get(id).rättSvar)assert.ok(Math.abs(f(r))<1e-9,`${id}: ${r}`);};

test('73 nya kort på nivå 2 och 3 i Ma2 kap 1, utan dubblettfacit',()=>{
  const per={},niv={2:0,3:0};
  for(const id of NYA){const t=get(id);per[t.omr]=(per[t.omr]||0)+1;niv[t.traningsniva]++;assert.equal(t.kap,1,id);
    assert.ok([2,3].includes(t.traningsniva),id);
    if(t.traningsniva===3){assert.equal(t.niva,'C',id);assert.equal(t.poang,'0/1/0',id);assert.equal(t.arbetsinsats,2,id);}else assert.equal(t.niva,'E',id);}
  assert.deepEqual(per,{multiplicera_parenteser:11,kvadreringsreglerna:11,konjugatregeln:11,faktorisering:9,linjara_representationer:10,bestamma_linjara_funktioner:11,rata_linjens_ekvation:10});
  assert.deepEqual(niv,{2:38,3:35});
  const v=x=>{const r=x.rättSvar,s=(Array.isArray(r)?JSON.stringify(r):String(r)).replace(/\s|\\\(|\\\)/g,''),m=Number(s);return isNaN(m)?s:String(Math.round(m*1e6)/1e6);};
  for(const id of NYA){const t=get(id);if(t.svarstyp==='alternativ')continue;
    const krock=B.filter(w=>w.omr===t.omr&&w.id!==id&&w.svarstyp!=='alternativ'&&w.rättSvar!=null&&v(w)===v(t)).map(w=>w.id);
    assert.deepEqual(krock,[],`${id} har samma facit som ${krock}`);}
  for(const id of NYA.filter(id=>get(id).svarstyp==='alternativ')){const a=get(id).alternativ;assert.equal(a.filter(x=>x.ratt).length,1,id);assert.ok(!a[0].ratt,`${id}: rätt svar först`);}
  // Nivåregeln för andragradsekvationer: koefficient eller bråkrot ger minst nivå 2.
  for(const id of ['2.1042','2.1047'])assert.equal(get(id).traningsniva,2,id);
});

test('Facit räknas om',()=>{
  // parenteser
  samma('1.1090','(x+3)*(x*x-2*x+1)');samma('1.1091','(2*x-1)*(x+3)-(x-2)*(2*x+5)');samma('1.1092','(8+2*x)*(5+2*x)');n('1.1093',12/2);
  samma('1.1094','(3*x-2*y)*(2*x+y)',['x','y']);n('1.1095',3/2);u('1.1096',[3,-5]);assert.equal(3+(-5),-2);assert.equal(3*-5,-15);
  n('1.1097',11);assert.equal((11+5)*(11-2),(11+1)**2);u('1.1099',[3,2]);samma('1.1100','(20+2*x)*(30+2*x)-600');
  // kvadreringsregler
  samma('1.1101','(x+3)**2+(x-3)**2');samma('1.1102','(3*a-2*b)**2',['a','b']);n('1.1103',3);assert.equal((3-7)**2,(3+1)**2);
  assert.ok(Math.abs(fn(get('1.1104').rättSvar,[])()-(Math.sqrt(2)+3)**2)<1e-12);samma('1.1105','(x/2+4)**2');n('1.1106',1001**2);
  u('1.1107',[-3,9]);n('1.1108',7*7-2*10);n('1.1109',(29-9)/2);n('1.1110',(75-9)/6);n('1.1111',24/4);
  // konjugatregeln
  samma('1.1112','(x*x+3)*(x*x-3)');samma('1.1113','(0.5*x+4)*(0.5*x-4)');samma('1.1114','49-x*x');n('1.1115',7.5*8.5);rot('1.1116',x=>x*x-0.25);
  n('1.1117',2026**2-2024**2);n('1.1119',25);u('1.1120',[7,4]);assert.equal(7*7-4*4,33);n('1.1121',12-1);rot('1.1122',x=>(2*x+1)**2-(x+2)**2);
  // faktorisering
  samma('1.1123','3*x*x+12*x+12');rot('1.1124',x=>4*x*x-9);samma('1.1125','12*x*x-27');samma('1.1126','5*x**3-20*x*x+20*x');rot('1.1127',x=>x**3-25*x);
  rot('1.1128',x=>(x-2)**2-3*(x-2));rot('1.1130',x=>2*x**3-8*x*x+8*x);n('1.1131',3*17**2-3*13**2);
  for(const [id,k] of [['1.1124',2],['1.1127',3],['1.1128',2],['1.1130',2],['1.1116',2],['1.1122',2]])assert.equal(new Set(get(id).rättSvar).size,k,id);
  // linjära representationer
  genom('1.1132',[[1,5],[3,11],[4,14],[7,23]]);samma('1.1133','2500-40*t',['t']);n('1.1134',(200-100)/250);n('1.1136',(22-1)/3);n('1.1137',2*10-4);n('1.1138',(70-10)/2.5);
  n('1.1139',(150-40)/(12-8));n('1.1140',32/(1-1.8));n('1.1141',-8/4);
  // bestämma linjära funktioner
  genom('1.1142',[[-4,6],[2,-3]]);genom('1.1143',[[3,2],[0,8]]);n('1.1144',7+(10-2)*(19-7)/4);genom('1.1145',[[1,4],[0,6]]);n('1.1146',279-12*(359-279)/8);
  genom('1.1147',[[1,7],[-6,0]]);n('1.1148',9);assert.equal(-2*9+9,-9);n('1.1149',2*-1+1);n('1.1150',5/((9+5)/3.5));genom('1.1151',[[1,3],[2,7],[4,15]]);n('1.1152',300/30);
  // räta linjens ekvation
  u('1.1153',[3,4]);u('1.1154',[-1.5,6]);n('1.1155',(10+5)/3);n('1.1156',4*8/2);genom('1.1157',[[0,0],[2,3]]);assert.equal(-2/3*1.5,-1);
  n('1.1158',3/2);n('1.1159',-2*4);n('1.1160',8+2*(6-4));genom('1.1161',[[6,0],[2,4]]);n('1.1162',(1-3)/2);
});
