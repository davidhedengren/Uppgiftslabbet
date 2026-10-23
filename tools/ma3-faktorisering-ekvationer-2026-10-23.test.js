const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('fs'),vm=require('vm'),path=require('path');
const ctx={window:{}};vm.runInNewContext(fs.readFileSync(path.join(__dirname,'../uppgiftermato1.js'),'utf8'),ctx);const bank=ctx.window.BANKMATO1,get=n=>bank.find(q=>q.id==='1.'+n),ids=Array.from({length:13},(_,i)=>900+i);
test('Tretton egna uppgifter med korrekt spår, nivå och verktyg',()=>{
 const levels={};for(const n of ids){const q=get(n);assert.ok(q);assert.deepEqual([...q.kurs],['1b','1c']);assert.equal(q.kap,1);assert.equal(q.spel,true);assert.equal(q.självrättning,true);assert.equal(q.miniräknare,true);assert.equal(q.geogebra,n===911);assert.match(q.s,/facit-svar/);levels[q.traningsniva]=(levels[q.traningsniva]||0)+1;}
 assert.deepEqual(levels,{1:4,2:4,3:4,4:1});assert.equal(ids.filter(n=>get(n).t.includes('<svg')).length,9);assert.equal(new Set(bank.map(q=>q.id)).size,bank.length);
});
test('Faktorformerna är identiteter, inklusive upprepad och irreducibel faktor',()=>{
 for(const x of [-5,-2,-1,0,1,3,5]){
  assert.equal(3*(2*x+5),6*x+15);assert.equal((x-2)*(x-3)+0,x*x-5*x+6);
  assert.equal((x+4)*(x*x+3)+0,x**3+4*x*x+3*x+12);assert.equal((2*x-3)**2,4*x*x-12*x+9);
  assert.equal((x+1)**2*(x-2)+0,x**3-3*x-2+0);
 }
 for(const n of [902,904])assert.equal(get(n).svarFormat,'faktoriserat');
 assert.equal(get(900).rättSvar,'2x+5');assert.equal(get(902).rättSvar,'(x+4)(x^2+3)');assert.equal(get(904).rättSvar,'(x+1)^2(x-2)');
 assert.match(get(903).alternativ.find(a=>a.ratt).txt,/4x\^2-12x\+9/);
});
test('Två nollställen och konstanttermen ger rätt koefficient',()=>{
 const a=get(905).rättSvar,b=-5,p=x=>x**3+a*x*x+b*x+6;
 assert.equal(p(1),0);assert.equal(p(-2),0);assert.equal(p(3),0);assert.equal(p(0),6);assert.equal(a,-2);
});
test('Lösningsmängder har alla olika rötter, även nollroten och andra ordningar',()=>{
 const models={906:x=>x*(x+4),907:x=>(x+2)*(x-3),910:x=>x**3-3*x*x-4*x+12};
 for(const [n,f]of Object.entries(models)){const q=get(+n);assert.equal(q.svarsstruktur,'mängd');assert.equal(new Set(q.rättSvar).size,q.rättSvar.length);q.rättSvar.forEach(x=>assert.equal(f(x)+0,0));assert.equal(q.svarFormat.length,q.rättSvar.length);}
 assert.deepEqual([...get(906).rättSvar].sort((a,b)=>a-b),[-4,0]);assert.deepEqual([...get(907).rättSvar],[-2,3]);assert.deepEqual([...get(910).rättSvar],[-2,2,3]);assert.equal(get(908).rättSvar,0);
 assert.equal(get(909).rättSvar*(get(909).rättSvar+3),10);assert.ok(get(909).rättSvar>0);
});
test('Lådans modell: båda möjliga lådor, tredje algebraiska roten är omöjlig',()=>{
 const V=x=>x*(20-2*x)*(16-2*x),q=get(911);assert.deepEqual([...q.rättSvar],[2,4]);
 for(const x of [2,4,12])assert.equal(V(x),384);for(const x of q.rättSvar)assert.ok(x>0&&x<8);
 for(const x of [0,1,2,4,6,12])assert.equal(V(x)-384+0,4*(x-2)*(x-4)*(x-12)+0);
 assert.match(q.t,/GeoGebra/);assert.equal(q.svarsstruktur,'mängd');assert.deepEqual([...q.svarEnhet],['cm','cm']);
 // Sheet is drawn to a consistent 15 px/cm scale, including square cuts.
 assert.match(q.t,/x="80" y="55" width="300" height="240"/);assert.match(q.t,/width="45" height="45"/);
});
test('Exakt två olika nollställen kräver sammanfallande rötter',()=>{
 const q=get(912);assert.deepEqual([...q.rättSvar],[-2,4]);for(const a of q.rättSvar)assert.equal(new Set([a,-2,4]).size,2);for(const a of [-3,0,2,5])assert.equal(new Set([a,-2,4]).size,3);
});
