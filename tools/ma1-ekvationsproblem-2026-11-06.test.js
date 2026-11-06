'use strict';
const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('node:fs'),vm=require('node:vm');
const c={window:{}};vm.runInNewContext(fs.readFileSync('uppgifterma1.js','utf8'),c);
const ids=Array.from({length:10},(_,i)=>`1.${1675+i}`),bank=c.window.BANKMA1;
const qs=ids.map(id=>bank.find(q=>q.id===id));
const near=(a,b)=>assert.ok(Math.abs(a-b)<1e-8,`${a} ≠ ${b}`);
test('Tio kompletta, självrättande Ma1-problem på nivå 4–5',()=>{
 assert.equal(new Set(bank.map(q=>q.id)).size,bank.length);
 for(const q of qs){assert.ok(q);assert.equal(q.omr,'ekv_problemlosning');assert.deepEqual(Array.from(q.kurs),['1a','1b','1c']);
 assert.equal(q.miniräknare,true);assert.equal(q.geogebra,false);assert.equal(q.spel,true);assert.equal(q.självrättning,true);
 assert.equal(q.svarFormat,'numeriskt');assert.equal(typeof q.rättSvar,'number');assert.ok(q.traningsniva>=4);
 assert.match(q.t,/<svg/);assert.match(q.t,/<title>/);assert.match(q.s,/facit-steglista/);assert.match(q.s,/facit-svar/);
 assert.ok((q.s.match(/facit-rubrik/g)||[]).length>=4);assert.match(q.s,/<p class="facit-rubrik">[^<]*\\\(/);
 assert.ok(q.ledtrad.length>80);assert.ok(!q.alternativ);assert.ok(!q.spelDelar);}
 assert.equal(qs.filter(q=>q.traningsniva===5).length,2);
});
test('Blandningarna uppfyller rätt andel av den färdiga volymen eller massan',()=>{
 const [gas,juice,ut,socker]=qs.map(q=>q.rättSvar);
 assert.match(qs[0].t,/4,5 liter olja/);assert.match(qs[0].t,/2,0 % av volymen/);
 near(4.5/(gas+4.5),.02);near(gas,220.5);assert.notEqual(gas,225);
 assert.match(qs[1].t,/12 %/);assert.match(qs[1].t,/30 %/);assert.match(qs[1].t,/20 %/);
 near((8*.12+juice*.30)/(8+juice),.20);near(juice,6.4);
 assert.match(qs[2].t,/väl omblandad/);assert.match(qs[2].t,/lika många liter rent vatten/);
 near(.40*(18-ut)/18,.25);assert.ok(ut>0&&ut<18);near(ut,6.75);
 assert.match(qs[3].t,/3,0 kg vatten avdunstar/);assert.match(qs[3].t,/Inget socker försvinner/);
 near((10*.30+socker)/(10-3+socker),.50);near(socker,1);
});
test('Kassor och rabatter: återinsättning i alla villkor',()=>{
 const k=qs[4].rättSvar,j=qs[5].rättSvar;
 assert.match(qs[4].t,/5 000 kr/);assert.match(qs[4].t,/25 %/);assert.match(qs[4].t,/600 kr/);
 near(.75*k,5000-k+600);near(k,3200);
 assert.match(qs[5].t,/240 kr mer/);assert.match(qs[5].t,/redan rabatterade totalsumman/);
 near(.8*j+.9*(j-240)-150,1164);near(j,900);
});
test('Hage och kabel: kontrollera hela och delar, inte bara ekvationens rot',()=>{
 const length=qs[6].rättSvar,breadth=(length-4)/2;
 assert.match(qs[6].t,/inklusive mellanstängslet/);assert.match(qs[6].t,/Mellanstängslet har ingen grind/);
 near(2*length+3*breadth-2,90);near(length,28);near(breadth,12);
 const roll=qs[7].rättSvar,long=roll/4,short=long-1.5;
 assert.match(qs[7].t,/fem lika långa/);assert.ok(short>0);near(long+5*short+2,roll);near(roll,11);
});
test('Cykelmötet är det första och ligger under pausen',()=>{
 const time=qs[8].rättSvar;
 assert.match(qs[8].t,/09.20/);assert.match(qs[8].t,/30 minuters cykling/);assert.match(qs[8].t,/stannar hon i 10 minuter/);
 assert.ok(time>30&&time<40);near(24*(time-20)/60,15*.5);near(time,38.75);
 // Före Sams start är Nora framför; under 20–30 min minskar ett positivt avstånd.
 for(let t=20;t<=30;t+=.5)assert.ok(15*t/60>24*(t-20)/60);
 for(let t=30;t<time;t+=.125)assert.ok(7.5>24*(t-20)/60);
});
test('Ritblock: båda erbjudanden ger samma ordinarie pris och totalsumma',()=>{
 const n=qs[9].rättSvar,p=6*(n+3)/3;
 assert.match(qs[9].t,/tre extra/);assert.match(qs[9].t,/fem extra/);assert.match(qs[9].t,/samma totalsumma/);
 near(p,9*(n+5)/5);near(n*p/(n+3),p-6);near(n*p/(n+5),p-9);near(n,15);assert.ok(Number.isInteger(n));
 // Uppräknad kontroll ger bara ett positivt heltalsantal som uppfyller båda.
 assert.deepEqual(Array.from({length:500},(_,i)=>i+1).filter(n=>Math.abs(2*(n+3)-1.8*(n+5))<1e-8),[15]);
});
test('Bankvalidatorn hittar inga fel eller varningar i de nya objekten',()=>{
 const {granskaBank}=require('./granska-uppgifter');
 assert.deepEqual(granskaBank('uppgifterma1.js',qs,process.cwd()).fynd,[]);
});
