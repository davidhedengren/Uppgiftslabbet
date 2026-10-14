'use strict';
const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('node:fs'),vm=require('node:vm'),path=require('node:path');
const c={window:{}};vm.createContext(c);for(const f of ['uppgifterma2.js','uppgifter.js'])vm.runInContext(fs.readFileSync(path.join(__dirname,'..',f),'utf8'),c);
const ma=id=>c.window.BANKMA2.find(t=>t.id===id),fy=id=>c.window.BANK.find(t=>t.id===id);
const mean=v=>v.reduce((a,b)=>a+b,0)/v.length,sd=(v,sample=true)=>Math.sqrt(v.reduce((a,x)=>a+(x-mean(v))**2,0)/(v.length-(sample?1:0)));
const close=(a,b)=>assert.ok(Math.abs(a-b)<1e-9,`${a} != ${b}`);
test('Temperaturstickprovet använder n−1, Sx och korrekt tvådecimalsrättning',()=>{
 const t=ma('5.94'),v=[20.8,21.2,21,21.4,20.6];close(t.rättSvar[0],mean(v));close(t.rättSvar[1],sd(v,true));
 assert.match(t.t,/stickprov/);assert.match(t.t,/Sx/);assert.match(t.s,/0\{,\}40/);assert.match(t.s,/0\{,\}32/);
 assert.ok(Math.abs(.32-t.rättSvar[1])<=t.tolerans[1]);assert.ok(Math.abs(.28-t.rättSvar[1])>t.tolerans[1]);
});
test('Rumstemperaturernas s-beteckningar motsvarar verkligen Sx',()=>{
 const t=ma('5.71');close(t.rättSvar[1],sd([20,21,22,21,21],true));close(t.rättSvar[3],sd([19,21,23,21,21],true));
 assert.match(t.t,/Sx/);assert.match(t.s,/0\{,\}71/);assert.match(t.s,/1\{,\}41/);
});
test('Statistikuppgifter anger vilket spridningsmått som beräknas',()=>{
 for(const id of ['5.66','5.110','4.299'])assert.match(ma(id).t,/Sx/,id);
 close(ma('5.110').rättSvar[1],sd([4,5,5,6,5]));close(ma('5.110').rättSvar[3],sd([2,4,5,6,8]));
 const a=[12,13,13,14,14,15,15,16],b=[12,13,13,14,14,15,15,30];
 assert.equal(sd(a).toFixed(2),'1.31');assert.equal(sd(b).toFixed(2),'5.85');
 close(sd([31.2,30.8,31.5,30.9,31.1,31]),.248327740429189);
});
test('Golfstickprovets intervall använder Sx och innehåller fortfarande nio slagantal',()=>{
 const t=ma('4.306'),v=[276,279,279,277,278,278,280,282,285,272,279,278],m=mean(v),s=sd(v,true);
 assert.match(t.t,/Sx/);assert.match(t.spelDelar[0].fraga,/Sx/);assert.match(t.s,/275,44–281,73/);
 assert.equal(v.filter(x=>x>=m-s&&x<=m+s).length,9);assert.equal(t.rättSvar[0],9/12*100);
});
test('Värmekurvans variabler och enheter är definierade med oförändrat svar',()=>{
 for(const id of ['5.162','5.92']){assert.match(ma(id).t,/x utomhustemperaturen i °C/);assert.match(ma(id).t,/T\(x\).*temperaturen i °C/);}
 assert.equal(ma('5.162').rättSvar,-1.2*(-5)+36);assert.equal(ma('5.121').svarEnhet,'månader');assert.equal(5000*10**(.2*ma('5.121').rättSvar),50000);
 assert.match(ma('5.90').t,/pumpens effekt i W/);assert.equal(-4*(6-2)*(6-10),ma('5.90').rättSvar[1]);
});
test('Fysikfaciten är korrekta och oavrundade rättningsmål bevaras',()=>{
 assert.equal(fy('5.575').rättSvar[0],120/4);assert.match(fy('5.575').spelDelar[0].s,/30,0 N/);
 assert.equal(fy('5.497').rättSvar[1],10*150*9.82*1.2);assert.match(fy('5.497').spelDelar[1].s,/1\{,\}77/);
 for(const [id,part,value]of [['5.14',0,6*4],['5.20',1,5400/45],['5.42',0,450*9.82*18],['5.46',0,80*15],['5.145',0,5*9.82*30],['5.67',0,250*40/1000]])close(fy(id).rättSvar[part],value);
});
