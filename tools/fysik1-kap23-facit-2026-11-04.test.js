'use strict';
const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('node:fs'),vm=require('node:vm'),path=require('node:path');
const c={window:{}};vm.runInNewContext(fs.readFileSync(path.join(__dirname,'../uppgifter.js'),'utf8'),c);const bank=c.window.BANK,q=id=>bank.find(q=>q.id===id);
const headings=/<p class="facit-rubrik">[^<]*\\\([^<]*\\\)[^<]*<\/p>/;
test('Samtliga 71 enhetsuppgifter och 110 delfacit följer facitmallen',()=>{
 const tasks=bank.filter(q=>q.omr==='enheter');assert.equal(tasks.length,71);let cards=0;
 for(const t of tasks){for(const [id,s]of[[t.id,t.s],...(t.spelDelar||[]).map(d=>[t.id+d.etikett,d.s])]){
  assert.match(s,/facit-steglista/,id);assert.match(s,headings,id);assert.match(s,/<p class="facit-svar"><strong>Svar:<\/strong>/,id);
  assert.doesNotMatch(s,/None|null|undefined|facit-forklaring/,id);
 }
 assert.equal(t.miniräknare,true,t.id);for(const d of t.spelDelar||[]){assert.notEqual(d.miniräknare,false,t.id+d.etikett);cards++;}}
 assert.equal(cards,110);
});
test('Givna data och alla efterfrågade svar finns kvar',()=>{
 assert.match(q('2.10').t,/3\{,\}156/);assert.match(q('2.10').s,/536\\,520\\,000/);
 assert.match(q('2.227').s,/p=1/);assert.match(q('2.227').s,/q=2/);assert.match(q('2.227').s,/multipliceras med 18/);
 assert.match(q('2.12').s,/50,6/);assert.match(q('2.12').spelDelar[1].s,/50,5/);
 assert.equal(q('2.36').självrättning[2],false);assert.equal(q('2.36').spelDelar[2].rättSvar,56.26/18);
});
test('Oberoende värden för prefix, skala, flöden och tillämpningar',()=>{
 const cases={
 '2.5':[45/100,8.4/1000,.75*1000,3.2*10000,620e-9,15/10],
 '2.22':[2.4e9,88e6,37e3,12e6,150e-6,2.4e-3],
 '2.32':[2400,850e6,.045,1.5*735,600,12e9],
 '2.33':[45000,2.5e6,3*3.6e6,250*3600,.0015,500*4184],
 '2.57':[4500,.25,1.2e6,300000,250000,101300],
 '2.58':[2700,.998,13600,.00129,920,7.87],
 '2.60':[25*60,3.5*3600,2*86400,.480,25e-6,1.5*3.156e7],
 '2.61':[350e-4,4.2e-2,1200e-6,.25e6,3e4,45e-2],
 '2.66':[.25,45e-6,4700,2.2e6,.012,400000],
 '2.70':[30e-3/60,1.2*1000*60,18000/3600,.25*3600,2*86400/1000],
 '2.73':[.03**2,.03**3,2**2,2**3,10**3],
 '2.74':[250e-6,3.5e-3,12e-3,800e-9,250e-6,4*100*.001],
 '2.76':[250e-3,45e-6,2400,78,.60e-9,12],
 '2.204':3.6e-6,'2.205':.045*100**2,'2.206':.0028,'2.207':.75*3600,
 '2.208':63/3.6,'2.209':4.2e6,'2.210':350e-6,'2.211':5600,'2.212':18,'2.213':.47,
 '2.215':.120*.080,'2.216':.012/60,'2.218':18*50**3/1e6,'2.220':.45e6/.001,
 '2.223':23.5*1000/6000,'2.321':75e-6,'2.322':1.2*.8,'2.323':3.6*1000/60,
 '2.324':120/.150,'2.325':35*.012*1000,'2.326':(1.8-.6)*1000,
 '2.359':Math.PI*.035**2,'2.360':3e8*1e-9*100,
 '2.361':[1000/19.3,Math.cbrt(1000/19.3)],'2.362':[18*9000/1000,18*2.5/1000],
 '2.363':1e6/.5**3,'2.364':1000/270};
 for(const[id,expected] of Object.entries(cases)){const t=q(id),actual=[].concat(t.rättSvar),want=[].concat(expected),tol=[].concat(t.tolerans);assert.equal(actual.length,want.length,id);
 want.forEach((v,i)=>assert.ok(Math.abs(v-actual[i])<=Math.max(tol[i]||0,Math.abs(v)*1e-10),`${id} ${i}: ${v} vs ${actual[i]}`));}
});
