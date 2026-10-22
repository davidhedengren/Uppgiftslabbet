'use strict';
const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('fs'),vm=require('vm'),path=require('path');
const banks={};for(const [b,file]of [['fy1','uppgifter.js'],['fy2','uppgifter2.js'],['ma2','uppgifterma2.js']]){const c={window:{}};vm.runInNewContext(fs.readFileSync(path.join(__dirname,'../'+file),'utf8'),c);banks[b]=Object.values(c.window)[0];}
const q=(id,b='fy1')=>banks[b].find(t=>t.id===id),near=(a,b)=>assert.ok(Math.abs(a-b)<=Math.max(Math.abs(b)*1e-12,1e-30),`${a} != ${b}`);
test('Fellogg: energier, krafter och kontakttid verifieras oberoende',()=>{
 const g=9.82,F=45*(9/(2*6)+g*Math.sin(Math.PI/12)+.25*g*Math.cos(Math.PI/12));
 near(q('5.123').rättSvar[0],F);near(q('5.225').rättSvar[0],(72*g*2/21+25)*5/1000);
 near(q('5.117').rättSvar[1],75*14/.02);near(q('5.95').rättSvar[0],80*g*12);
 near(q('5.97').rättSvar[0],500*.12**2/2);near(q('5.14').rättSvar[0],6*4);
 near(q('5.382').rättSvar[1],.420*(18+13)/650);
 near(q('5.396').rättSvar,.10*g*(2/.060+1));
 near(q('9.415').rättSvar[0],1.5*1.3806e-23*2e7);
 near(q('9.415').spelDelar[1].rättSvar,Math.sqrt(2*4.1e-16/1.6735e-27));
});
test('Rapporterade delkort har egna rätta nivåer och tydliga frågor',()=>{
 assert.equal(q('5.123').spelDelar[0].traningsniva,4);
 assert.equal(q('5.225').spelDelar[0].traningsniva,5);assert.equal(q('5.225').spelDelar[1].traningsniva,3);
 assert.equal(q('5.396').traningsniva,5);assert.match(q('5.117').spelDelar[1].t,/på passageraren under inbromsningen/);
 assert.equal(q('5.395').spelDelar[1].traningsniva,4);assert.equal(q('5.395').spelDelar[0].traningsniva,2);
 assert.match(q('5.97').spelDelar[0].t,/energi är lagrad/);
 assert.equal((q('5.382').spelDelar[1].t.match(/18 m\/s/g)||[]).length,1);
 assert.match(q('9.415').spelDelar[0].t,/för en proton/);assert.doesNotMatch(q('9.415').spelDelar[0].ledtrad,/givna formeln/);
 assert.match(q('4.117','ma2').spelIntro,/medelvärdet 70 och standardavvikelsen 8/);
 assert.match(q('4.117','ma2').spelDelar[1].s,/90:e percentilen/);
 assert.match(q('5.95').spelDelar[0].t,/två värdesiffror/);assert.equal(q('5.95').tolerans[0],50);
});
test('Kalibrerad precision använder oavrundade målvärden och ärvs på rätt kort',()=>{
 near(q('2.2').rättSvar[0],84/2**3);near(q('2.2').rättSvar[1],84*(4/2)**3);
 near(q('1.3','fy2').rättSvar[0],2*Math.PI*5.5);near(q('1.3','fy2').rättSvar[1],Math.PI);
 near(q('1.4','fy2').rättSvar[1],.18*7.2**2/.6);near(q('1.6','fy2').rättSvar,9**2/3.6);
 for(const [b,ids]of [['fy1',['2.2','9.415']],['fy2',['1.2','1.3','1.4','1.6']]])for(const id of ids){
  const t=q(id,b);for(const d of t.spelDelar||[t])assert.equal(d.svarVardesiffror,2);
  assert.equal(t.miniräknare,true);assert.equal(t.geogebra,false);
 }
});
