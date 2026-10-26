'use strict';
const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('node:fs'),vm=require('node:vm');
const c={window:{}};vm.createContext(c);for(const f of ['uppgifterma2.js','uppgifter.js'])vm.runInContext(fs.readFileSync(require('node:path').join(__dirname,'..',f),'utf8'),c);
const ma=id=>c.window.BANKMA2.find(t=>t.id===id),fy=id=>c.window.BANK.find(t=>t.id===id);
const close=(x,y)=>assert.ok(Math.abs(x-y)<1e-9,`${x} != ${y}`);
function pearson(x,y){const mean=v=>v.reduce((a,b)=>a+b,0)/v.length,mx=mean(x),my=mean(y);return x.reduce((s,a,i)=>s+(a-mx)*(y[i]-my),0)/Math.sqrt(x.reduce((s,a)=>s+(a-mx)**2,0)*y.reduce((s,b)=>s+(b-my)**2,0));}
test('Biltabellens data bevaras i lodräta rader och r rättas till två decimaler',()=>{
 const q=ma('4.300');const pairs=[[1,262],[2,245],[3,208],[4,201],[5,168],[6,172],[8,131],[10,104]];
 for(const [a,b]of pairs)for(const text of [q.t,q.spelIntro])assert.ok(text.includes(`<tr><td>${a}</td><td>${b}</td></tr>`));
 const r=pearson(pairs.map(x=>x[0]),pairs.map(x=>x[1]));close(q.rättSvar[0],r);
 assert.ok(Math.abs(-.99-r)<=q.tolerans[0]);assert.ok(Math.abs(-.98-r)>q.tolerans[0]);
});
test('Breda kapitel 4-tabeller har högst tre kolumner utan dataförlust',()=>{
 for(const id of ['4.136','4.138','4.139','4.146','4.162','4.290','4.299','4.300','4.303','4.306']){
   const t=ma(id);assert.match(t.t,/<thead>/,id);
   for(const row of t.t.matchAll(/<tr[^>]*>([\s\S]*?)<\/tr>/g))assert.ok((row[1].match(/<t[hd]\b/g)||[]).length<=3,id);
 }
});
test('Normalfördelningens sökta värde har en egen etikett utan överlagring',()=>{
 for(const [id,mu,sigma,n] of [['4.50',72,5,2],['4.196',50,4,1],['4.214',80,6,1]]){
  const t=ma(id);assert.equal(t.rättSvar,mu+n*sigma);assert.match(t.t,/<text[^>]*y="245"[^>]*>\?<\/text>/);
  assert.doesNotMatch(t.t,/<text[^>]*y="218"[^>]*>\?<\/text>/);
 }
});
test('Percentilernas mittområde är ett självständigt nivå 1-kort',()=>{
 const t=ma('4.95'),d=t.spelDelar[2];assert.match(d.t,/<svg/);assert.match(d.t,/10 %/);
 assert.equal(d.traningsniva,1);assert.equal(d.niva,'E');assert.equal(t.rättSvar[2],100-10-10);
 assert.doesNotMatch(d.t.replace(/<[^>]*>/g,""),/59,0|91,0|80/);assert.match(d.s,/100-10-10/);
 close(75-12.5*1.2815515655446004,58.980605430692496);
 for(const id of ['4.72','4.87'])assert.match(ma(id).spelDelar.at(-1).fraga,/intervall/);
 assert.match(ma('4.26').spelDelar[1].t,/5,02 %/);
});
test('Namngivna värden har ordning och namngivna svarsfält även på splitkort',()=>{
 for(const [id,part,labels]of [['2.711',0,['a','b','c']],['2.711',1,['E(3)','Q(3)']],['2.407',0,['a','b']],
  ['2.436',2,['x-koordinat','y-koordinat']],['1.313',1,['Lådans vikt (kg)','Bokens vikt (kg)']],
  ['2.707',0,['Biljettpris (kr)','Biljettintäkt (kr)']],['2.718',0,['k','x-koordinat','y-koordinat']],
  ['4.299',1,['Alva (s)','Bea (s)']],['4.302',0,['Medelvärde','Standardavvikelse']]]){
   const d=ma(id).spelDelar[part];assert.equal(d.svarsstruktur,'ordnad',id);assert.deepEqual(Array.from(d.svarEtiketter),labels);
 }
 const [a,b,k]=ma('2.711').rättSvar[0];for(const [x,y]of [[0,1],[1,2],[2,4]])close(a*x*x+b*x+k,y);
 assert.deepEqual(Array.from(ma('2.711').rättSvar[1]),[2**3,a*9+b*3+k]);
 assert.doesNotMatch(ma('2.407').spelDelar[0].s,/29/);
 assert.doesNotMatch(ma('2.436').spelDelar[0].s,/x-koordinat/);
});
test('Spridningsfacit har korrekt avrundning och tar hänsyn till spridning noll',()=>{
 const a=[31.2,30.8,31.5,30.9,31.1,31.0],b=[30.4,31.9,30.6,32,30.5,31.1],sd=v=>{let m=v.reduce((s,x)=>s+x,0)/v.length;return Math.sqrt(v.reduce((s,x)=>s+(x-m)**2,0)/(v.length-1))};
 assert.equal(sd(b.filter(x=>x!==32)).toFixed(2),'0.62');assert.match(ma('4.299').spelDelar[3].s,/0\{,\}62/);
 assert.equal(sd(a).toFixed(2),'0.25');assert.equal(sd(b).toFixed(2),'0.71');
 const golf=[276,279,279,277,278,278,280,282,285,272,279,278];
 const sample=sd(golf);assert.equal(sample.toFixed(1),'3.1');assert.match(ma('4.306').s,/s\\approx3\{,\}15/);assert.match(ma('4.306').t,/Sx/);
 assert.match(ma('4.302').spelDelar[1].s,/redan är noll/);assert.doesNotMatch(ma('4.302').t,/alltid minskar/);
});
test('De två fysikrapporterna har oförändrade, oberoende verifierade facit',()=>{
 const q=fy('6.300');assert.equal(q.rättSvar,800*9.82*1);assert.equal(q.tolerans,0);assert.equal(q.svarVardesiffror,4); // avrundningskravet ersatt av svarVardesiffror 2026-10-26
 const v=.12*Math.sqrt(250/.8);close(fy('5.99').rättSvar[0],v);assert.equal(fy('5.99').spelDelar[0].traningsniva,2);
});
