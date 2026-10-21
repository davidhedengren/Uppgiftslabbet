'use strict';
// Skydd för FP85: Ma4 tan_kurvan 2.605–2.612 och Ma3c deriverbarhet 3.1157–3.1164.
const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('fs'),vm=require('vm');
const bank=f=>{const c={window:{}};vm.runInNewContext(fs.readFileSync(__dirname+'/../'+f,'utf8'),c);return Object.values(c.window).find(v=>Array.isArray(v));};
const m2=bank('uppgiftermato2.js'),m1=bank('uppgiftermato1.js');
const q=(b,id)=>b.find(x=>x.id===id),ratt=(b,id)=>Array.from(q(b,id).alternativ.filter(a=>a.ratt),a=>a.txt);
const tan=v=>Math.tan(v*Math.PI/180);

test('Ma4 tangenskurvan: svar stämmer med tan',()=>{
 assert.equal(q(m2,'2.606').rättSvar,180/90);
 assert.equal(q(m2,'2.607').rättSvar,Math.round(3/tan(45)));
 const v=Math.atan(2)*180/Math.PI;
 assert.deepEqual(Array.from(q(m2,'2.608').rättSvar),[Math.round(v*10)/10,Math.round((v+180)*10)/10]);
 assert.equal(q(m2,'2.609').rättSvar,120);
 assert.equal(q(m2,'2.611').rättSvar,Math.round(v*10)/10);
 assert.deepEqual(Array.from(q(m2,'2.612').rättSvar),[2,Math.round(2/tan(30)*100)/100]);
 assert.equal(ratt(m2,'2.610').length,3);
 for(let i=605;i<=612;i++){const t=q(m2,'2.'+i);assert.equal(t.omr,'tan_kurvan');assert.ok(t.t.includes('<svg'),'2.'+i);assert.deepEqual(Array.from(t.kurs),['2c']);}
});

test('Ma3c deriverbarhet: hörn, hopp, ensidiga lutningar och lodrät tangent',()=>{
 assert.equal(q(m1,'3.1157').rättSvar,2);
 assert.deepEqual(ratt(m1,'3.1159').sort(),['B','D']);
 assert.deepEqual(Array.from(q(m1,'3.1162').rättSvar),[2*1,3]);
 const [a,b]=q(m1,'3.1163').rättSvar;assert.equal(2*a*2,8);assert.equal(a*4,16+b);
 assert.match(ratt(m1,'3.1161')[0],/^Ja/);assert.match(ratt(m1,'3.1164')[0],/lodrät/);
 for(let i=1157;i<=1164;i++){const t=q(m1,'3.'+i);assert.equal(t.omr,'deriverbarhet');}
 for(let i=1157;i<=1162;i++)assert.ok(q(m1,'3.'+i).t.includes('<svg'),'3.'+i);
 assert.ok(q(m1,'3.1164').t.includes('<svg'));
});

test('Ma3c: extrempunktsuppgifter flyttade från deriverbarhet med bevarade gamla namn',()=>{
 const mal={'3.633':'extrempunkter','3.634':'extrempunkter','3.635':'extrempunkter','3.639':'extrempunkter','3.640':'extrempunkter',
  '3.637':'extrempunkter','3.638':'extrempunkter','2.278':'extrempunkter','2.673':'extrempunkter',
  '3.636':'derivatan_och_grafen','2.678':'derivatan_och_grafen','2.638':'andraderivatan','2.639':'andraderivatan'};
 for(const [id,omr] of Object.entries(mal)){const t=q(m1,id);assert.equal(t.omr,omr,id);
  assert.ok([].concat(t.omrTidigare).includes('deriverbarhet'),id);assert.ok([].concat(t.familjTidigare).includes('Deriverbarhet'),id);}
 const kvar=m1.filter(t=>t.omr==='deriverbarhet').map(t=>t.id);
 for(const id of ['3.1143','3.1149'])assert.ok(kvar.includes(id));
 assert.ok(kvar.every(id=>id==='3.1143'||id==='3.1149'||Number(id.split('.')[1])>=1157),kvar.join(','));
});
