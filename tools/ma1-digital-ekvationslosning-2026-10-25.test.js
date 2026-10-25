'use strict';
/* Ma1 2026-10-25: grafisk/digital ekvationslösning med kaströrelser (s = v0t + at²/2), parabler och exponentialfunktioner (2.632–2.645).
   Lärarbeslut: sådana uppgifter hör till digitala hjälpmedel (grafisk_ekvationslosning, delmomentet ”Ekvationslösning med digitalt
   verktyg”), inte till Ma2:s ekvationssystem, där bara linjära system ska finnas. */
const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('node:fs'),vm=require('node:vm'),path=require('node:path');
const load=f=>{const c={window:{}};vm.runInNewContext(fs.readFileSync(path.join(__dirname,'..',f),'utf8'),c);return JSON.parse(JSON.stringify(Object.values(c.window).find(Array.isArray)));};
const B=load('uppgifterma1.js');const get=id=>{const t=B.find(x=>x.id===id);assert.ok(t,id);return t;};
const NYA=Array.from({length:14},(_,i)=>`2.${632+i}`);
const rot=(f,a,b)=>{for(let i=0;i<200;i++){const m=(a+b)/2;if((f(m)>0)===(f(a)>0))a=m;else b=m;}return (a+b)/2;};
const nära=(id,x)=>assert.ok(Math.abs(get(id).rättSvar-x)<1e-8,`${id}: ${get(id).rättSvar} ≠ ${x}`);

test('14 kort i digital ekvationslösning med icke-linjära funktioner',()=>{
  const niv={1:0,2:0,3:0};
  for(const id of NYA){const t=get(id);niv[t.traningsniva]++;assert.equal(t.omr,'grafisk_ekvationslosning',id);assert.equal(t.familj,'Ekvationslösning med digitalt verktyg',id);
    assert.equal(t.geogebra,true,id);assert.equal(t.miniräknare,true,id);assert.deepEqual(t.kurs,['1a','1b','1c'],id);
    if(t.svarstyp==='numeriskt'&&t.tolerans)assert.match(t.t,/\(Svara[^)]*decimal/,id);}
  assert.deepEqual(niv,{1:2,2:7,3:5});
  // innehållet är verkligen icke-linjärt: kvadrat- eller exponentialterm i varje kort
  for(const id of NYA)assert.match(get(id).t,/\^|²|ˣ/,id);
  const v=x=>JSON.stringify(x.rättSvar);
  for(const id of NYA){const t=get(id);if(t.rättSvar==null)continue;const krock=B.filter(w=>w.omr===t.omr&&w.id!==id&&w.rättSvar!=null&&v(w)===v(t)).map(w=>w.id);assert.deepEqual(krock,[],`${id}: ${krock}`);}
  // Ma2:s grafiska lösning av ekvationssystem innehåller inga sådana kort
  const M2=load('uppgifterma2.js').filter(t=>t.omr==='grafisk_losning_ekvationssystem'&&/1\.1[12]\d\d/.test(t.id));
  for(const t of M2)assert.doesNotMatch(t.t,/x\^2|x²|\^x|2ˣ|t\^2/,t.id);
});

test('Facit räknas om',()=>{
  for(const x of get('2.632').rättSvar)assert.equal(20*x-5*x*x,15);for(const x of get('2.633').rättSvar)assert.equal(x*x,x+6);
  nära('2.634',rot(t=>2*t+1.5*t*t-20,0,5));nära('2.635',rot(x=>2**x-x-3,1,4));
  assert.equal(get('2.636').rättSvar,[1,2,3,4,5,6,7,8,9].find(t=>100*1.2**t>200+20*t));nära('2.637',Math.log(0.25)/Math.log(0.8));
  for(const x of get('2.638').rättSvar)assert.equal(x*x-3,2*x+5);nära('2.639',Math.log(4)/Math.log(1.5));
  nära('2.641',5-Math.sqrt(5));assert.ok(5+Math.sqrt(5)>5);nära('2.642',15/10);nära('2.643',rot(t=>1.8+14*t-4.91*t*t,1,4));
  assert.equal(get('2.644').rättSvar,Math.ceil(Math.log(500/300)/Math.log(1.1/1.05)));nära('2.645',rot(x=>2**x-x*x,-2,0));
});
