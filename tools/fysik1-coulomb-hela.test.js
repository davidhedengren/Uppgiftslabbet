'use strict';
const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('node:fs'),vm=require('node:vm'),path=require('node:path');
const c={window:{}};vm.runInNewContext(fs.readFileSync(path.join(__dirname,'../uppgifter.js'),'utf8'),c);const q=id=>c.window.BANK.find(x=>x.id===id);
const k=8.99e9,e=1.602e-19,g=9.82,force=(a,b,r)=>k*Math.abs(a*b)/r**2;
const f33x=force(3e-9,5e-9,.04),f33y=force(3e-9,5e-9,.03),f160x=force(5e-9,4e-9,.03),f160y=force(5e-9,-6e-9,.04);
const q58=Math.sqrt(.0005*.06**2/k)*1e9,f121a=force(5e-9,2e-9,.03)*1e6,f121b=force(4e-9,2e-9,.05)*1e6;
const prod488=.00054*.05**2/k*1e18,large488=(25+Math.sqrt(25**2-4*prod488))/2;
const cases=[
 ['8.22',[force(e,e,.01),6.674e-11*(1.673e-27)**2/.01**2,force(e,e,.01)/(6.674e-11*(1.673e-27)**2/.01**2)]],
 ['8.24',[null,force(7e-9,5e-9,.06)]],['8.32',[10*Math.sqrt(9)/(Math.sqrt(9)+Math.sqrt(4)),null]],
 ['8.33',[f33x,f33y,[Math.hypot(f33x,f33y)*1e6,Math.atan2(f33y,f33x)*180/Math.PI]]],['8.34',[12*Math.sqrt(8)/(Math.sqrt(8)+Math.sqrt(2)),null]],
 ['8.58',[null,null,q58,q58*1e-9/e]],['8.119',[(12-8)/2,force(2e-9,2e-9,.04)]],
 ['8.311',Math.sqrt(k*(2e-6)**2/.9)],['8.312',force(2e-6,1e-6,.2)+force(3e-6,1e-6,.3)],
 ['8.121',[null,[f121a,f121b],f121a+f121b]],['8.313',0],['8.159',[force(6e-9,5e-9,.08),null,force(6e-9,5e-9,.16)]],['8.314',.75*2/3],
 ['8.160',[f160x,f160y,[Math.hypot(f160x,f160y)*1e6,Math.atan2(f160y,f160x)*180/Math.PI]]],
 ['8.161',[force(8e-6,2e-6,.05),(8+2)/2,force(5e-6,5e-6,.05)]],
 ['8.316',force(4e-6,1e-9,.32)-force(8e-6,1e-9,.32)],['8.317',4*.20**2/.40**2],['8.318',force(3e-6,3e-6,.3)],['8.174',-2.5e8*e*1e12],['8.320',.65*3/5],
 ['8.476',-(1.6+6.2-4.8-9.4)/4*1e-6/e],['8.477',-3.4*.26**2/(k*3.5e-6)*1e6],
 ['8.478',[force(20e-6,50e-6,.025),Math.sqrt(k*15e-6*30e-6/6)]],['8.479',[Math.sqrt(1.6*.03**2/(10*k))*1e6,Math.sqrt(1.6*.03**2/(10*k))*1e7]],
 ['8.480',force(3*e,e,150e-12)],['8.481',force(1.3e9*e,1.3e9*e,.05)],
 ['8.482',[.0075*g+force(32e-9,58e-9,.02),Math.sqrt(k*45e-9*78e-9/(.15-.0045*g))]],
 ['8.483',[force(.8e-6,.6e-6,.05)/.035,force(2.7e-6,8.6e-6,.09)/.005]],
 ['8.484',1.5*Math.sqrt(3)/(1+Math.sqrt(3))],['8.485',[force(1e-6,1e-6,1),force(1e-6,1e-6,1)/1]],
 ['8.486',[force(50e-9,50e-9,.02),force(50e-9,50e-9,.02)/(.002*g)]],['8.487',Math.sqrt(k*5e-9*12e-9/8.2e-4)],
 ['8.488',[large488,25-large488]],['8.489',.018*.01**2/(k*20e-9)*1e9],['8.490',force(10e-9,20e-9,.02)],
 ['8.491',[force(20e-9,e,.01)/9.11e-31,force(20e-9,e,.01)/1.673e-27]],
 ['8.492',Math.sqrt(.001*225*.02**2/k)*1e9],['8.493',[Math.sqrt(.45*.1**2/(2*k))*1e6,2*Math.sqrt(.45*.1**2/(2*k))*1e6]],
 ['8.494',.045*Math.sqrt((.001*g/.01)*.005/k)*1e9]
];
function near(a,b,id){if(b===null)return;if(Array.isArray(b)){b.forEach((v,i)=>near(a[i],v,id));return;}assert.equal(typeof a,'number',id);assert.ok(Math.abs(a-b)<=Math.abs(b)*1e-10+(b===0?1e-30:0),`${id}: ${a} vs ${b}`);}
test('Alla återstående Coulombsvar följer oberoende beräkningar från givna data',()=>{for(const[id,v]of cases)near(q(id).rättSvar,v,id);});
test('Fristående kort rättas från sina egna mellanresultat',()=>{
 near(q('8.58').spelDelar[0].rättSvar,Math.sqrt(2e-16)*1e9,'8.58 c');near(q('8.58').spelDelar[1].rättSvar,14e-9/e,'8.58 d');
 near(q('8.485').spelDelar[1].rättSvar,.009/1,'8.485 b');near(q('8.486').spelDelar[1].rättSvar,.056/(.002*g),'8.486 b');
 near(q('8.488').spelDelar[1].rättSvar,25-15,'8.488 b');near(q('8.493').spelDelar[1].rättSvar,2*.5,'8.493 b');
 for(const[id,x,y]of[['8.33',84.3,150],['8.160',200,169]])near(q(id).spelDelar[2].rättSvar,[Math.hypot(x,y),Math.atan2(y,x)*180/Math.PI],id+' c');
});
test('Avrundning till två värdesiffror är möjlig utan tolerans som överstiger en liten kraft',()=>{
 for(const[id,i,v]of[['8.22',2,1.2e36],['8.159',2,11e-6],['8.479',0,.13],['8.479',1,1.3]])assert.ok(Math.abs(q(id).rättSvar[i]-v)<=q(id).tolerans[i],id);
 assert.ok(Math.abs(q('8.481').rättSvar-1.6e-7)<=q('8.481').tolerans);
 assert.ok(q('8.22').tolerans[1]<q('8.22').rättSvar[1]); // noll/tiodubbelt får inte accepteras
});
test('Flera efterfrågade krafter eller olika enheter har ordnade namngivna fält',()=>{
 for(const[id,i]of[['8.33',2],['8.160',2],['8.121',1]]){const p=q(id).spelDelar[i];assert.equal(p.svarsstruktur,'ordnad');assert.equal(p.svarEtiketter.length,2);assert.equal(p.rättSvar.length,2);}
 assert.deepEqual(Array.from(q('8.33').spelDelar[2].svarEnhet),['µN','°']);assert.match(q('8.119').t,/likadana metallkulor/);
 for(const id of ['8.120','8.122','8.174','8.476'])assert.equal(q(id).omr,'laddning');
 for(const id of ['8.120','8.122'])assert.equal(q(id).spelDelar.length,3);
});

test('Större-laddningskortet visar inte den mindre laddningens svar',()=>{const a=q('8.488').spelDelar[0];assert.doesNotMatch(a.s,/Rötterna är|15 och 10|25\\pm/);assert.match(a.s,/större roten/);});
