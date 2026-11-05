'use strict';
const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('fs'),vm=require('vm');
const c={window:{}};
for(const bank of ['ma1','ma2'])vm.runInNewContext(fs.readFileSync(`uppgifter${bank}.js`,'utf8'),c);
const q=(bank,id)=>c.window['BANK'+bank.toUpperCase()].find(q=>q.id===id);
const ids={ma1:['0.06','0.305','0.306','0.401','0.402','0.782','0.941'],ma2:['4.245','4.2082','4.2084','4.2143']};
const html=fs.readFileSync('index.html','utf8'),ctx={};
for(const name of ['altVisas','uppgiftsText','altFacit']){const i=html.indexOf('function '+name+'(');vm.runInNewContext(html.slice(i,html.indexOf('\n}',i)+2),ctx)}
ctx.altBokstav=i=>String.fromCharCode(65+i);
test('Alla elva frågor visar alternativen en gång i lärar- och exportunderlaget',()=>{
 for(const [bank,list] of Object.entries(ids))for(const id of list){
  const x=q(bank,id);assert.ok(ctx.altVisas(x),bank+' '+id);
  assert.equal((ctx.uppgiftsText(x).match(/class="ul-alt"/g)||[]).length,x.alternativ.length,id);
  for(const a of x.alternativ){assert.ok(ctx.uppgiftsText(x).includes(a.txt));assert.ok(a.kommentar?.length>15,id);if(a.ratt)assert.ok(ctx.altFacit(x).includes(a.txt),id)}
  assert.match(x.s,/facit-steglista/);assert.match(x.s,/facit-rubrik/);assert.match(x.s,/facit-svar/);
  assert.equal(x.geogebra,false);assert.equal(x.miniräknare,bank==='ma2'||id==='0.782');
 }
 // Öppna, fullständiga frågor ska inte göras om till flerval i lärarvyn.
 for(const [bank,id] of [['ma1','0.36'],['ma2','4.52'],['ma2','4.103']])assert.equal(ctx.altVisas(q(bank,id)),false);
 // Samma presenter används i kort, PDF och Word.
 assert.match(html,/class="kroppen">\$\{uppgiftsText\(x\)/);
 assert.match(html,/uppgiftsHTML=\(x,visaVerktyg=true,text=uppgiftsText\(x\)\)/);
 assert.match(html,/taskHTML=gemensam\?[^\n]*:uppgiftsText\(x\)/);
});
test('Bråk- och decimaltalsjämförelsernas rätta alternativ verifieras oberoende',()=>{
 const numeric={'0.305':[5/8,3/5,2/3],'0.306':[5/8,7/10,2/3],'0.401':[.507,.57,.509,.55],'0.402':[1.08,1.018,1.080,1.008],'0.782':[5/12,.42],'0.941':[5/8,.6,.65,2/3]};
 for(const [id,values] of Object.entries(numeric)){
  const ranked=id==='0.306'?values.map(v=>Math.abs(1-v)):values;
  const wanted=['0.306','0.402'].includes(id)?Math.min(...ranked):Math.max(...ranked);
  assert.deepEqual(Array.from(q('ma1',id).alternativ,a=>a.ratt),ranked.map(v=>v===wanted),id);
 }
 // Åtta olika positiva bitstorlekar; tre kan ge mindre/lika/mer än 3/8.
 const slices=[1,2,3,4,5,6,7,12],sum=slices.reduce((a,b)=>a+b,0);
 assert.equal(sum,40);assert.ok((1+2+3)/sum<3/8);assert.equal((3+5+7)/sum,3/8);assert.ok((6+7+12)/sum>3/8);
 assert.equal(q('ma1','0.06').alternativ[0].ratt,true);
});
test('Lådagram: rätta påståenden, korrekt spridning och inga obestyrkta slutsatser',()=>{
 for(const id of ['4.2082','4.2143'])assert.deepEqual(Array.from(q('ma2',id).alternativ,a=>a.ratt),[false,true,true,false]);
 assert.equal(4-2.5,1.5);assert.equal(5.5-2,3.5);assert.ok((5.5-2)>(4-2.5));
 assert.doesNotMatch(q('ma2','4.2143').s,/nästan ingen/);
 assert.deepEqual([36-18,52-15,31-24,38-22],[18,37,7,16]);
 assert.match(q('ma2','4.245').t,/mittersta hälften/);
 assert.deepEqual(Array.from(q('ma2','4.245').alternativ,a=>a.ratt),[true,false,false,false]);
 assert.ok(62>58&&10<25);
});
test('4.2084 säkrar placeringen innan median och kvartiler förklaras oförändrade',()=>{
 const x=q('ma2','4.2084');assert.match(x.t,/Det rättade värdet är fortfarande störst/);
 assert.doesNotMatch(x.s,/större än övre kvartilen/);
 assert.deepEqual(Array.from(x.alternativ,a=>a.ratt),[false,true,false,true]);
 const before=[12,14,16,18,19,21,22,23,24,25,27,28,29,29.5,30,32,33,34,35,48];
 const after=[...before.slice(0,-1),38];
 const stats=a=>[(a[9]+a[10])/2,(a[4]+a[5])/2,(a[14]+a[15])/2,a.at(-1),a.reduce((s,v)=>s+v,0)/20];
 const b=stats(before),a=stats(after);assert.deepEqual(b.slice(0,3),[26,20,31]);assert.deepEqual(a.slice(0,3),b.slice(0,3));assert.equal(b[3]-a[3],10);assert.equal(b[4]-a[4],.5);
 // Motexempel: Q3=31 räcker inte ensamt för att 38 ska vara det största värdet.
 const underSpecified=[12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,36,40,42,44,48];
 assert.equal(stats(underSpecified)[2],31);
 const corrected=[...underSpecified.slice(0,-1),38].sort((a,b)=>a-b);
 assert.equal(corrected.at(-1),44); // Inte 38, utan det nya villkoret.
});
