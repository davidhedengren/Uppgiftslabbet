'use strict';
const {test}=require('node:test');
const assert=require('node:assert/strict');
const fs=require('node:fs'),path=require('node:path'),vm=require('node:vm');
const c={window:{}};
for(const file of ['uppgiftermato1.js','strukturmato1.js'])vm.runInNewContext(fs.readFileSync(path.join(__dirname,'..',file),'utf8'),c);
const bank=JSON.parse(JSON.stringify(c.window.BANKMATO1));
const task=id=>bank.find(q=>q.id===id);

test('Varje område har en aktiv introduktionsuppgift för varje tillämpligt spår',()=>{
 let areas=0;
 for(const [kap,omr]of Object.entries(c.window.OMRMATO1))for(const area of Object.keys(omr)){
  areas++;
  const qs=bank.filter(q=>q.kap===+kap&&q.omr===area&&q.spel!==false);
  for(const track of c.window.SPARMATO1[kap][area]){
   assert.ok(qs.some(q=>q.kurs.includes(track)&&(q.spelDelning==='deluppgifter'&&q.spelDelar?.length?q.spelDelar.some(d=>(d.traningsniva??q.traningsniva)===1):q.traningsniva===1)),`${area}/${track}: nivå 1 saknas`);
  }
 }
 assert.equal(areas,50);
});
test('Den rationella ekvationens rot uppfyller originalekvationen',()=>{
 const x=task('1.129').rättSvar;
 assert.notEqual(x,-1);assert.equal(3*x/(x+1),2);
});
test('Exponentialkortets numeriska derivata hör till funktionen i frågan',()=>{
 const q=task('2.254'),f=x=>3*Math.exp(2*x)-5*Math.exp(-x),h=1e-5;
 assert.ok(Math.abs((f(h)-f(-h))/(2*h)-q.rättSvar[1])<1e-7);
 assert.match(q.spelDelar[0].t,/3e\^\{2x\}-5e\^\{-x\}/);
 assert.match(q.spelDelar[1].t,/6e\^\{2x\}\+5e\^\{-x\}/);
 assert.equal(q.rättSvar.length,2);assert.equal(q.svarFormat.length,2);
});
test('Tangentens båda svar har egna fält och ekvationen går genom rätt punkt',()=>{
 const q=task('2.309'),x=2,f=x=>x**3-3*x,k=3*x*x-3;
 assert.equal(q.rättSvar[0],k);
 const m=q.rättSvar[1].match(/^y=([\d.-]+)x([+-][\d.]+)$/);
 assert.ok(m);assert.equal(+m[1],k);assert.equal(+m[1]*x+(+m[2]),f(x));
 assert.equal(q.spelDelar.length,2);assert.equal(q.självrättning.length,2);
});
test('Integralens gräns och sträckan rättas var för sig utan extra självbedömning',()=>{
 const q=task('3.481');assert.deepEqual(q.rättSvar,[3,9.82*3**2/2]);
 assert.deepEqual(q.svarEnhet,['s','m']);assert.deepEqual(q.manuellKomplettering,[false,false]);
 assert.match(q.spelDelar[0].t,/övre gränsen/);assert.match(q.spelDelar[1].t,/9\{,\}82t/);
});
test('Rätvinkliga trianglar ritas med rätt katetförhållande och ger rätt hypotenusa',()=>{
 for(const [id,a,b]of [['4.446',6,8],['4.447',3,4],['4.461',8,15],['4.464',5,12]]){
  const q=task(id),lines=[...q.t.matchAll(/<line x1="([\d.]+)" y1="([\d.]+)" x2="([\d.]+)" y2="([\d.]+)"/g)].map(m=>m.slice(1).map(Number));
  assert.equal(lines[0][1],lines[0][3]);assert.equal(lines[1][0],lines[1][2]);
  const w=Math.abs(lines[0][2]-lines[0][0]),h=Math.abs(lines[1][3]-lines[1][1]);
  assert.ok(Math.abs(w/h-a/b)<1e-5);assert.equal(q.rättSvar,Math.hypot(a,b));
 }
});
test('De nya uppgifterna har kompletta, enkla kontrakt och ledtråd skiljer sig från facit',()=>{
 const ids=[...Array.from({length:8},(_,i)=>`1.${818+i}`),...Array.from({length:9},(_,i)=>`2.${1107+i}`),...Array.from({length:7},(_,i)=>`3.${1150+i}`),'4.493','4.494','4.495'];
 for(const id of ids){const q=task(id);assert.ok(q,id);assert.equal(q.traningsniva,1);assert.equal(q.niva,'E');assert.ok(q.spel&&q.självrättning);
  assert.notEqual(q.ledtrad,'<p>'+q.s.match(/<p>(.*?)<\/p>/)?.[1]+'</p>');
  if(q.svarstyp==='alternativ')assert.equal(q.alternativ.filter(a=>a.ratt).length,1);else assert.notEqual(q.rättSvar,null);
 }
});
