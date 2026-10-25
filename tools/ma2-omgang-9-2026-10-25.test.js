'use strict';
/* Ma2 2026-10-25 omgång 9: ekvationssystem (grafisk lösning, tre obekanta, linjära system, tillämpningar, substitution,
   speciella system) och konjugatregeln på nivå 1–3. Varje systemlösning prövas i sina ekvationer. */
const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('node:fs'),vm=require('node:vm'),path=require('node:path');
const c={window:{}};vm.runInNewContext(fs.readFileSync(path.join(__dirname,'..','uppgifterma2.js'),'utf8'),c);
const B=JSON.parse(JSON.stringify(Object.values(c.window).find(Array.isArray)));const get=id=>{const t=B.find(x=>x.id===id);assert.ok(t,id);return t;};
const NYA=Array.from({length:55},(_,i)=>`1.${1174+i}`);
const n=(id,x)=>assert.ok(Math.abs(Number(get(id).rättSvar)-x)<1e-9,`${id}: ${get(id).rättSvar} ≠ ${x}`);
// sys: varje ekvation skrivs som funktion av lösningen och ska bli 0
const sys=(id,...ekv)=>{const v=get(id).rättSvar.map(Number);for(const f of ekv)assert.ok(Math.abs(f(...v))<1e-9,`${id}: ${v} uppfyller inte ${f}`);};

test('55 nya kort i Ma2 kap 1 på nivå 1–3, utan dubblettfacit',()=>{
  const per={},niv={1:0,2:0,3:0};
  for(const id of NYA){const t=get(id);per[t.omr]=(per[t.omr]||0)+1;niv[t.traningsniva]++;assert.equal(t.kap,1,id);if(t.traningsniva===3)assert.equal(t.niva,'C',id);}
  assert.deepEqual(per,{grafisk_losning_ekvationssystem:8,ekvationssystem_tre_obekanta:9,linjara_ekvationssystem:9,ekvationssystem_tillampningar:8,substitutionsmetoden:7,konjugatregeln:8,speciella_ekvationssystem:6});
  assert.deepEqual(niv,{1:10,2:26,3:19});
  for(const id of NYA){const t=get(id);assert.deepEqual(t.kurs,t.omr==='ekvationssystem_tre_obekanta'?['2c']:['2a','2b','2c'],id);}
  const v=x=>{const r=x.rättSvar,s=(Array.isArray(r)?JSON.stringify(r):String(r)).replace(/\s|\\\(|\\\)/g,''),m=Number(s);return isNaN(m)?s:String(Math.round(m*1e6)/1e6);};
  for(const id of NYA){const t=get(id);if(t.svarstyp==='alternativ')continue;
    const krock=B.filter(w=>w.omr===t.omr&&w.id!==id&&w.svarstyp!=='alternativ'&&w.rättSvar!=null&&v(w)===v(t)).map(w=>w.id);assert.deepEqual(krock,[],`${id}: ${krock}`);}
  for(const id of NYA.filter(id=>get(id).svarstyp==='alternativ')){const a=get(id).alternativ;assert.equal(a.filter(x=>x.ratt).length,1,id);
    if(!a.every(x=>/^[A-H]$/.test(x.txt)))assert.ok(!a[0].ratt,id);}
  // triangelfiguren: ingen linje korsar y-axeln vid en skalsiffra
  assert.match(get('1.1181').t,/y = 2x − 2/);
});

test('Facit räknas om och systemlösningar prövas',()=>{
  // grafisk lösning
  sys('1.1174',(x,y)=>y-(0.5*x+1),(x,y)=>y-(-x+5.5));sys('1.1175',(t,s)=>s-12*t,(t,s)=>s-(9+6*t));n('1.1178',(200-50)/(5-2));assert.equal(get('1.1179').rättSvar,'8/3');
  n('1.1180',(-2+7-1)/2);n('1.1181',(7-1)*4/2);
  // tre obekanta
  sys('1.1182',(x,y,z)=>x-2,(x,y,z)=>y-(x+3),(x,y,z)=>z-(x+y));n('1.1183',12-3-4);sys('1.1184',(x,y,z)=>x+y+z-12,(x,y,z)=>x-y+z-2,(x,y,z)=>x+y-z-4);
  sys('1.1185',(a,b,c)=>a+b+c-30,(a,b)=>b-a-2,(a,b,c)=>c-b-2);sys('1.1186',(k,b)=>2*k+b-50,(k,b)=>k+2*b-46,(k,b,c)=>k+b+c-52);
  sys('1.1187',(a,b,c)=>c-3,(a,b,c)=>a+b+c-4,(a,b,c)=>4*a+2*b+c-9);sys('1.1188',(a,m,y)=>a+m+y-36,(a,m,y)=>a-2*y,(a,m,y)=>m-y-4);
  sys('1.1189',(x,y,z)=>2*x+y+z-7,(x,y,z)=>x+2*y+z-8,(x,y,z)=>x+y+2*z-9);sys('1.1190',(e,f,t)=>e+f+t-24,(e,f,t)=>f-t,(e,f,t)=>e+5*f+10*t-115);
  // linjära ekvationssystem
  sys('1.1191',(x,y)=>0.5*x+y-7,(x,y)=>x-0.5*y-1);sys('1.1192',(x,y)=>x/2+y/3-4,(x,y)=>x-y-3);sys('1.1193',(x,y)=>x+y-50,(x,y)=>120*x+70*y-4600);
  sys('1.1194',(x,y)=>3*x-2*y-12,(x,y)=>5*x+2*y-20);sys('1.1195',(x,y)=>x+y-1,(x,y)=>5*x-y-23);sys('1.1196',(a,b)=>2*a+b-7,(a,b)=>2*a-b-1);
  n('1.1197',38);assert.equal(3+8,11);assert.equal(83-38,45);sys('1.1198',(l,b)=>2*(l+b)-34,(l,b)=>(l+3)*(b-2)-l*b);n('1.1199',(14-4)/2);
  // tillämpningar
  n('1.1200',(400-250)/(3-2));sys('1.1201',(x,y)=>x+y-6,(x,y)=>0.4*x+0.1*y-1.2);sys('1.1203',(s,j)=>3*s+2*j-165,(s,j)=>2*s+3*j-145);
  sys('1.1204',(v,u)=>1.5*(v+u)-30,(v,u)=>2.5*(v-u)-30);sys('1.1205',(x,y)=>x+y-50000,(x,y)=>0.02*x+0.03*y-1300);sys('1.1206',(v,b)=>2*v+3*b-700,(v,b)=>2.2*v+3.6*b-800);
  sys('1.1207',(a,b)=>2*(a+b)-360,(a,b)=>a-b-20);
  // substitution
  sys('1.1208',(x,y)=>y-(3*x-5),(x,y)=>2*x+3*y-7);sys('1.1209',(x,y)=>x-(2*y+1),(x,y)=>3*x-4*y-7);
  for(const x of get('1.1210').rättSvar)assert.equal(x*x,x+2);n('1.1211',2-2*2);const [p,q]=get('1.1212').rättSvar;assert.equal(p+q,10);assert.equal(p*q,21);
  // konjugatregeln
  n('1.1215',49-9);n('1.1217',7);n('1.1219',1.1*0.9);n('1.1221',(36-25)-(36-9));for(const x of get('1.1222').rättSvar)assert.equal((x+4)*(x-4),9);
  // speciella system
  n('1.1224',-4);n('1.1226',2/4);n('1.1228',4*2);
});
