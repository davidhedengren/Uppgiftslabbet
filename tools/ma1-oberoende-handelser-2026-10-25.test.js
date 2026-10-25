'use strict';
/* Ma1 2026-10-25: oberoende händelser på nivå 1–3 (5.641–5.664). Området hade 28 kort på nivå 1–2 och 5 på nivå 3. */
const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('node:fs'),vm=require('node:vm'),path=require('node:path');
const c={window:{}};vm.runInNewContext(fs.readFileSync(path.join(__dirname,'..','uppgifterma1.js'),'utf8'),c);
const B=JSON.parse(JSON.stringify(Object.values(c.window).find(Array.isArray)));const get=id=>{const t=B.find(x=>x.id===id);assert.ok(t,id);return t;};
const NYA=Array.from({length:24},(_,i)=>`5.${641+i}`);
const fr=s=>{const [a,b]=String(s).split('/').map(Number);return a/b;};
const n=(id,x)=>{const t=get(id);const v=t.svarstyp==='bråk'?fr(t.rättSvar):Number(t.rättSvar);assert.ok(Math.abs(v-x)<1e-12,`${id}: ${t.rättSvar} ≠ ${x}`);};

test('24 nya kort om oberoende händelser på nivå 1–3, utan dubbletter',()=>{
  const niv={1:0,2:0,3:0};
  for(const id of NYA){const t=get(id);assert.equal(t.omr,'oberoende_handelser',id);niv[t.traningsniva]++;assert.deepEqual(t.kurs,['1a','1b','1c'],id);
    if(t.traningsniva===3)assert.equal(t.niva,'C',id);}
  assert.deepEqual(niv,{1:8,2:9,3:7});
  const v=x=>JSON.stringify(x.rättSvar);
  for(const id of NYA){const t=get(id);if(t.rättSvar==null)continue;
    const krock=B.filter(w=>w.omr===t.omr&&w.id!==id&&w.rättSvar!=null&&v(w)===v(t)).map(w=>w.id);assert.deepEqual(krock,[],`${id}: ${krock}`);}
  for(const id of NYA.filter(id=>get(id).svarstyp==='alternativ')){const a=get(id).alternativ;assert.equal(a.filter(x=>x.ratt).length,1,id);assert.ok(!a[0].ratt,id);}
  // träddiagrammen är stående med raka grenar (tradlib) och tärningstabellen har 36 rutor
  for(const id of ['5.641','5.647','5.651','5.656'])assert.match(get(id).t,/<line /,id);
  assert.equal((get('5.653').t.match(/<rect x="\d+" y="\d+" width="40" height="40"/g)||[]).length,36);
});

test('Facit räknas om',()=>{
  n('5.641',0.6*0.7);n('5.642',0.9*0.9);n('5.643',0.25);n('5.645',1/1000);n('5.646',1/16);n('5.647',1-0.7);n('5.648',1/9);
  n('5.649',1-(4/6)**2);n('5.650',2*0.6*0.4);n('5.651',0.8*0.3+0.2*0.7);n('5.652',1-1/8);n('5.653',2/36);n('5.654',1-0.1**3);n('5.656',0.42/0.6);n('5.657',1/343);
  assert.deepEqual(get('5.658').rättSvar.map(x=>Math.round(x*1e9)/1e9),[0.855,0.995]);n('5.659',3*0.4**2*0.6);
  assert.deepEqual(get('5.660').rättSvar,[0.3,0.65]);
  n('5.661',[1,2,3,4,5,6].find(k=>1-(5/6)**k>0.5));n('5.662',[...Array(20).keys()].find(k=>1-0.7**k>0.9));n('5.664',0.6**2+2*0.6*0.4*0.6);
  assert.notEqual(Math.round(0.6*0.3*100),24);
});
