'use strict';
/* Ma2 2026-10-24 omgång 1: variation och nivå 1 i kap 1 (parenteser, kvadreringsregler, faktorisering, linjära representationer,
   bestämma linjära funktioner, räta linjens ekvation). Facit räknas om genom att jämföra uttryck i flera punkter. */
const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('node:fs'),vm=require('node:vm'),path=require('node:path');
const c={window:{}};vm.runInNewContext(fs.readFileSync(path.join(__dirname,'..','uppgifterma2.js'),'utf8'),c);
const B=JSON.parse(JSON.stringify(Object.values(c.window).find(Array.isArray)));const get=id=>{const t=B.find(x=>x.id===id);assert.ok(t,id);return t;};
const NYA=Array.from({length:90},(_,i)=>`1.${1000+i}`);

// Elevform (implicit multiplikation, ^) till JS-funktion av de angivna variablerna.
const fn=(s,vars)=>{let e=String(s).replace(/^[a-zA-Z](\([a-z]\))?=/,'').replace(/sqrt/g,'Q').replace(/\^/g,'**')
  .replace(/(\d|\))\s*(?=[a-zA-Z(Q])/g,'$1*').replace(/([a-zA-Z])(?=[a-zA-Z(Q])/g,'$1*').replace(/Q\*?/g,'Math.sqrt').replace(/(^|\()-/g,'$1-1*');
  return new Function(...vars,`return ${e};`);};
const samma=(id,ratt,vars=['x'])=>{const f=fn(get(id).rättSvar,vars),g=fn(ratt,vars);
  for(const p of [[-2.5,1.5],[0.5,-3],[3,2],[7,-1.25]]){const a=f(...p),b=g(...p);assert.ok(Math.abs(a-b)<1e-9,`${id}: ${get(id).rättSvar} ≠ ${ratt} vid ${p}`);}};

test('90 nya kort i sex områden i Ma2 kap 1 utan dubblettfacit',()=>{
  const per={};for(const id of NYA){const t=get(id);per[t.omr]=(per[t.omr]||0)+1;assert.equal(t.kap,1,id);assert.ok([1,2].includes(t.traningsniva),id);}
  assert.deepEqual(per,{multiplicera_parenteser:15,kvadreringsreglerna:16,faktorisering:17,linjara_representationer:13,bestamma_linjara_funktioner:15,rata_linjens_ekvation:14});
  assert.ok(NYA.filter(id=>get(id).traningsniva===1).length>=70);
  const v=x=>{const r=x.rättSvar,s=(Array.isArray(r)?JSON.stringify(r):String(r)).replace(/\s|\\\(|\\\)/g,''),n=Number(s);return isNaN(n)?s:String(Math.round(n*1e6)/1e6);};
  for(const id of NYA){const t=get(id);if(t.svarstyp==='alternativ')continue;
    const krock=B.filter(u=>u.omr===t.omr&&u.id!==id&&u.svarstyp!=='alternativ'&&u.rättSvar!=null&&v(u)===v(t)).map(u=>u.id);
    assert.deepEqual(krock,[],`${id} har samma facit som ${krock}`);}
  for(const id of NYA.filter(id=>get(id).svarstyp==='alternativ'))assert.equal(get(id).alternativ.filter(a=>a.ratt).length,1,id);
  for(const id of NYA.filter(id=>get(id).svarFormat==='faktoriserat'))assert.match(get(id).rättSvar,/\)/,id);
});

test('Facit räknas om',()=>{
  const n=(id,x)=>assert.ok(Math.abs(Number(get(id).rättSvar)-x)<1e-9,`${id}: ${get(id).rättSvar} ≠ ${x}`);const u=(id,s)=>assert.deepEqual(get(id).rättSvar,s,id);
  // multiplicera parenteser
  samma('1.1000','(x+2)*(x+5)');samma('1.1001','(x+4)*(x+3)');samma('1.1002','(a-6)*(a-2)',['a']);samma('1.1003','3*(x+2)*(x-1)');n('1.1005',-7*4);
  samma('1.1006','(5-x)*(2+x)');samma('1.1007','(2*x+1)*(x+2)');n('1.1008',3*2-1*4);n('1.1009',3);samma('1.1011','(2*a+b)*(a-3*b)',['a','b']);
  samma('1.1012','x*(x+4)+(x+1)*(x-2)');samma('1.1013','(x-4)*(x-9)');samma('1.1014','(x+1)*(x+2)*(x+3)');
  // kvadreringsregler
  samma('1.1015','(x-3)**2');samma('1.1016','(y+8)**2',['y']);samma('1.1017','(x+7)*(x-7)');samma('1.1018','(2*x+3)*(2*x-3)');samma('1.1019','(x+3)**2-x*x-9');
  n('1.1021',31*31);n('1.1022',49*51);n('1.1023',19*19);samma('1.1024','(x+7)**2-x*x-49');samma('1.1025','(x-0.5)**2');samma('1.1026','(a+2*b)**2',['a','b']);
  samma('1.1027','(6-x)**2');samma('1.1028','(x+2)**2-(x-2)**2');assert.ok(Math.abs(fn(get('1.1030').rättSvar,[])()-(Math.sqrt(3)+1)**2)<1e-12);
  // faktorisering
  samma('1.1031','5*x+15');samma('1.1032','x*x+8*x');samma('1.1033','7*x*x-14*x');samma('1.1034','x*x-81');samma('1.1035','16*x*x-1');samma('1.1036','x*x+10*x+25');
  samma('1.1037','4*x*x+12*x+9');samma('1.1038','2*x*x-50');samma('1.1039','x**3-4*x');samma('1.1044','10*x**3+15*x*x');n('1.1045',53*53-47*47);
  const rot=(id,f)=>{for(const r of get(id).rättSvar)assert.ok(Math.abs(f(r))<1e-9,`${id}: ${r}`);assert.equal(new Set(get(id).rättSvar).size,2,id);};
  rot('1.1040',x=>x*x-7*x);rot('1.1041',x=>(x-3)*(x+8));rot('1.1042',x=>x*x-36);rot('1.1046',x=>3*x*x-12*x);u('1.1047','4x');
  // linjer: kontrollera att ekvationen går genom givna punkter
  const genom=(id,pkt,vars=['x'])=>{const f=fn(get(id).rättSvar,vars);for(const [a,b] of pkt)assert.ok(Math.abs(f(a)-b)<1e-9,`${id}: (${a}, ${b})`);};
  genom('1.1048',[[0,5],[1,8],[2,11],[3,14]]);genom('1.1049',[[0,200],[1,250],[4,400]]);n('1.1050',(60-40)/4);n('1.1051',20);u('1.1052',[4*-1-3,-3,4*2-3]);
  genom('1.1055',[[0,1],[2,7],[4,13],[6,19]]);n('1.1057',(3-1)/0.5);genom('1.1058',[[1,20],[2,16],[3,12],[4,8]]);genom('1.1059',[[0,30],[5,20]],['t']);
  genom('1.1060',[[0,-3],[1,1]]);genom('1.1061',[[1,4],[3,10]]);n('1.1062',(13-5)/(6-2));genom('1.1063',[[-2,1],[2,9]]);genom('1.1064',[[0,-2],[3,10]]);
  genom('1.1065',[[1,2],[2,-1]]);genom('1.1066',[[0,4],[1,9]]);n('1.1067',170-5*(310-170)/7);n('1.1068',14-3*(24-14)/5);n('1.1069',6+500*(6-12)/1000);
  genom('1.1070',[[0,2],[4,4]]);genom('1.1071',[[1,7],[4,1]]);genom('1.1073',[[-3,5],[3,1]]);n('1.1074',(1100-560)/6);genom('1.1075',[[0,0],[4,10]]);
  u('1.1076',[-4,9]);genom('1.1077',[[0,6],[3,0]]);genom('1.1078',[[0,5],[1,7]]);n('1.1079',-8/2);n('1.1081',-1/4);u('1.1082',[2,4]);
  genom('1.1084',[[-3,4],[5,4]]);genom('1.1086',[[0,4],[4,0]]);n('1.1087',0.5*6);n('1.1089',(11-3)/2);
});
