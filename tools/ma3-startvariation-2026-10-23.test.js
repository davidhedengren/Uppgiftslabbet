const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('fs'),vm=require('vm'),path=require('path');
const c={window:{}};vm.runInNewContext(fs.readFileSync(path.join(__dirname,'../uppgiftermato1.js'),'utf8'),c);const bank=c.window.BANKMATO1,get=n=>bank.find(q=>q.id==='1.'+n),ids=Array.from({length:12},(_,i)=>888+i);
test('Tolv varierade uppgifter på nivå 1–3, rätt spår och verktyg',()=>{
 const levels={};for(const n of ids){const q=get(n);assert.ok(q);assert.deepEqual([...q.kurs],['1b','1c']);assert.equal(q.kap,1);assert.equal(q.spel,true);assert.equal(q.självrättning,true);assert.equal(q.miniräknare,true);assert.equal(q.geogebra,false);assert.match(q.s,/facit-svar/);assert.ok(q.ledtrad.length>30);assert.doesNotMatch(q.t+q.s,/[\u0000-\u0008\u000b-\u001f]/);levels[q.traningsniva]=(levels[q.traningsniva]||0)+1;}
 assert.deepEqual(levels,{1:4,2:3,3:5});assert.equal(ids.filter(n=>get(n).t.includes('<svg')).length,9);assert.equal(new Set(bank.map(q=>q.id)).size,bank.length);
});
test('Areor, omkrets och prisskillnad verifieras med hela modellen',()=>{
 assert.equal(get(888).rättSvar,3);assert.equal((get(888).t.match(/>x²<\/text>/g)||[]).length,3);
 for(const x of [3,4,5,12]){
  assert.equal(3*(x+2),3*x+6);
  const W=2*x+3,H=x+2,edges=[W-2,1,2,H-1,W,H];assert.equal(edges.reduce((a,b)=>a+b),6*x+10);
  assert.equal((15+4*x)-(8+x),3*x+7);
 }
 for(const [n,v]of [[889,'3x+6'],[890,'6x+10'],[891,'3x+7'],[893,'4n+7']]){assert.equal(get(n).rättSvar,v);assert.equal(get(n).svarFormat,'förenklat_polynom');}
});
test('Koefficientvillkor och kostnadsskillnad gäller generellt',()=>{
 const a=get(892).rättSvar;assert.equal(a-3,0);
 for(const x of [-3,-1,0,1,4])assert.equal((x*x+a*x+2)*(x-3)+0,x**3-7*x-6+0);
 const K=n=>2*n*n+5*n+30;for(let n=0;n<30;n++)assert.equal(K(n+1)-K(n),4*n+7);
});
test('Polynom, koefficientdiagram och parameterns grad',()=>{
 assert.match(get(894).alternativ.find(a=>a.ratt).txt,/x\^2/);assert.equal(get(894).alternativ.filter(a=>a.ratt).length,1);
 const coefficients=[-1,2,0,-2,0];assert.equal(coefficients.findLastIndex(c=>c!==0),get(895).rättSvar);
 const m=get(897).rättSvar;assert.equal(m-2,0);assert.notEqual(m+1,0);
});
test('Graf och tabeller ger de avsedda värdena, utan oriktig entydighet',()=>{
 const p=x=>(x+2)*(x-1)*(x-3);assert.equal(p(0),6);assert.equal(p(2),get(896).rättSvar);for(const x of [-2,1,3])assert.equal(p(x)+0,0);
 const f=x=>x*x+1,g=x=>x*x+1+x*(x-1)*(x-2);assert.deepEqual([0,1,2].map(f),[1,2,5]);assert.deepEqual([0,1,2].map(g),[1,2,5]);assert.notEqual(f(3),g(3));assert.match(get(898).alternativ.find(a=>a.ratt).txt,/Båda passar/);
 const h=x=>2*x*x-x+3;assert.deepEqual([-1,0,2].map(h),[6,3,9]);assert.equal(h(3),get(899).rättSvar);
});
