'use strict';
const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('node:fs'),vm=require('node:vm'),path=require('node:path');
const c={window:{}};vm.runInNewContext(fs.readFileSync(path.join(__dirname,'../uppgifterma1.js'),'utf8'),c);
const tasks=JSON.parse(JSON.stringify(c.window.BANKMA1)).filter(q=>q.kallaProv);
const q=(no,varnr=0)=>tasks.find(x=>x.kallaProv.uppgift===no&&x.kallaProv.variant===varnr);
const close=(a,b)=>assert.ok(Math.abs(a-b)<1e-9,`${a} != ${b}`);
test('Provets 30 uppgifter har två varianter var och unika ID:n',()=>{
 assert.equal(tasks.length,90);assert.equal(new Set(c.window.BANKMA1.map(x=>x.id)).size,c.window.BANKMA1.length);
 for(let no=1;no<=30;no++)assert.deepEqual(tasks.filter(x=>x.kallaProv.uppgift===no).map(x=>x.kallaProv.variant).sort(),[0,1,2]);
 assert.equal(tasks.filter(x=>x.kallaProv.variant===0).reduce((s,x)=>s+x.poang.split('/').map(Number).reduce((a,b)=>a+b),0),52);
 for(const x of tasks){assert.ok(x.kurs.includes('1a'));assert.ok(x.traningsniva>=1&&x.traningsniva<=4);assert.equal(x.självrättning,true);assert.equal(typeof x.miniräknare,'boolean');assert.equal(x.miniräknare,x.kallaProv.uppgift>=20);assert.equal(x.geogebra,false);assert.doesNotMatch(x.s,/facit-steglista|<ol\b/);}
});
test('Grundberäkningarna stämmer med provets uttryck, enheter och storleksordning',()=>{
 assert.deepEqual(q(1).rättSvar,[16-3*4,(-4)*(-5)-7,100-11+4*2,(-24)/(-6)-3]);
 close(q(2).rättSvar,-5+12-8);close(q(3).rättSvar,5.7);
 assert.deepEqual(q(4).rättSvar,[.07,.7,.707,.77]);close(q(5).rättSvar,60*30);
 assert.deepEqual(q(6).rättSvar,[3.5*100,750/100]);close(q(7).rättSvar,5.3*10**3);
 assert.deepEqual(q(8).rättSvar,[3.4*1000,6.2e-2*1000]);assert.deepEqual(q(9).rättSvar,['5/6','3/14']);
 close(q(10).rättSvar,15/60*100);close(q(11).rättSvar,6.2e-4);close(q(12).rättSvar,550*.2);close(q(13).rättSvar,6.35);assert.deepEqual(q(14).rättSvar,[.5,.07]);
 close(q(16).rättSvar,36*20/60);close(q(18).rättSvar,300/1.5*4);
});
test('Del B visar rätt jämförelsegrund, flöde och enhetsomvandling',()=>{
 close(q(20).rättSvar,3*2.4-5*.85);close(q(21).rättSvar,23/.355);close(q(22).rättSvar,(34750-25466)/34750*100);
 assert.deepEqual(q(23).rättSvar,['ja',180/(1.5/10)/60]);assert.deepEqual(q(23,2).rättSvar,['nej',(60-6)/((10-6)/20)/60]);
 close(q(24).rättSvar,84000-.3*22000);assert.deepEqual(q(25).rättSvar,[420/50,260/50]);close(q(26).rättSvar,14*3/(1+3));
 close(q(27).rättSvar,365*24*3600/2*.25/1000);assert.equal(q(28).rättSvar,'2/5');assert.deepEqual(q(29).rättSvar,[8,19]);close(q(30).rättSvar,1/(1/12+1/6));
 close(q(30,1).rättSvar,1/(1/12+1/8));close(q(30,2).rättSvar,1/(1/10+1/15-1/30));
});
test('Variationerna prövar även nya enheter, jämförelser och situationer',()=>{
 assert.deepEqual(q(1,1).rättSvar,[6,10,55,4]);assert.deepEqual(q(1,2).rättSvar,[4,15,82,2]);
 assert.deepEqual(q(6,2).rättSvar,[450,750]);assert.deepEqual(q(8,2).rättSvar,[450,7.5]);
 assert.deepEqual(q(9,1).rättSvar,['5/8','3/10']);assert.deepEqual(q(9,2).rättSvar,['7/12','2/5']);
 close(q(20,1).rättSvar,4*1.8-6*.75);close(q(20,2).rättSvar,3*2.5-7*.8);
 close(q(24,1).rättSvar,80000-.3*20000);close(q(24,2).rättSvar,65000-.2*15000);
 close(q(26,1).rättSvar,15*4/5);close(q(26,2).rättSvar,20*3/5);
 close(q(27,1).rättSvar,30*24*3600/3*.4/1000);close(q(27,2).rättSvar,7*24*3600/5*.2/1000);
 assert.equal(q(28,1).rättSvar,'1/4');assert.equal(q(28,2).rättSvar,'1/2');assert.deepEqual(q(29,1).rättSvar,[12,40]);close(q(29,2).rättSvar,3.84e8/3e8);
 assert.equal(q(30,2).traningsniva,4);assert.equal(q(29,2).traningsniva,2);
});
test('Öppna exempel har egna villkor och motiveringsfrågor har förklaringar i alternativen',()=>{
 for(let v=0;v<3;v++){
  assert.equal(q(15,v).svarFormat,'negativt_talpar');assert.ok(q(15,v).svarVillkor.skillnad>0);
  assert.equal(q(19,v).svarFormat,'brak_i_intervall');assert.ok(q(19,v).svarVillkor.min&&q(19,v).svarVillkor.max);
  assert.equal(q(11,v).svarFormat,'grundpotensform');assert.equal(q(28,v).svarFormat,'forkortat_brak');
  const alts=q(17,v).alternativ;assert.equal(alts.filter(a=>a.ratt).length,1);assert.ok(alts.every(a=>a.kommentar&&a.txt.length>60));
 }
});
test('Alla delkort har egen fråga, facit, ledtråd och kalibrerad nivå',()=>{
 for(const x of tasks.filter(x=>x.spelDelar)){
  assert.equal(x.spelDelning,'deluppgifter');assert.equal(x.spelDelar.length,x.rättSvar.length);
  for(const d of x.spelDelar){assert.ok(d.t.length>20&&d.s.length>50&&d.ledtrad.length>20);assert.doesNotMatch(d.t,/från (?:del|uppgift)|använd (?:ditt |)svar/);assert.ok(d.traningsniva>=1&&d.traningsniva<=3);assert.ok(['E','C'].includes(d.niva));}
 }
 for(const x of tasks.filter(x=>x.kallaProv.uppgift===23))assert.ok(x.spelDelar.every(d=>d.t.includes('<table')));
});
