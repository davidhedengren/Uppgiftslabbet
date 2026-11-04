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
test('Samtliga 68 mätnoggrannhetsfacit och nio delkort följer mallen',()=>{
 const tasks=bank.filter(q=>q.omr==='matnogg');assert.equal(tasks.length,68);let parts=0;
 const concept=new Set(['2.228','2.229','2.247','2.233','2.235','2.353','2.355','2.358','2.16','2.44a','2.44b']);
 for(const t of tasks){assert.equal(t.miniräknare,true,t.id);for(const[id,s]of[[t.id,t.s],...(t.spelDelar||[]).map(d=>[t.id+d.etikett,d.s])]){
  assert.match(s,/facit-steglista/,id);assert.match(s,/facit-rubrik/,id);assert.match(s,/facit-svar/,id);
  if(!concept.has(id))assert.match(s,headings,id);
  assert.doesNotMatch(s,/None|null|undefined|facit-forklaring/,id);
 } parts+=(t.spelDelar||[]).length;}assert.equal(parts,9);
 assert.equal(q('2.46').geogebra,true);assert.match(q('2.46').s,/<svg/);
 assert.doesNotMatch(q('2.250').t,/eftersom/);assert.doesNotMatch(q('2.251').t,/eftersom/);
});
test('Osäkerhet: oberoende beräkningar och rätt gränser',()=>{
 const cases={'2.230':7.85,'2.231':.0759,'2.232':7.8-1.2,'2.234':.01,'2.236':12.4+.1/2,'2.237':12.4-.1/2,'2.238':.3,
 '2.239':.5/45*100,'2.240':(5.12+5.15+5.14)/3,'2.241':2.17-2.11,'2.242':.06/2,'2.243':14.8/10,'2.245':72.40-.2,
 '2.246':(12-11.7)/12*100,'2.248':7.6,'2.249':15/2,'2.250':12.9,'2.251':7.2,'2.252':.2/20,
 '2.253':Math.ceil(.1/(.1*.01)),'2.254':12.1*8.1,'2.255':(2*.02/2.5+.1/10)*100,
 '2.256':(.1/85+.2/10)*8.5,'2.257':(9.84-9.77)/2,'2.258':(50.7-.8)/(100.6-.8)*100,
 '2.259':1/.05,'2.260':20,'2.262':124.8-.5,'2.263':Math.PI*25*(2*.05/5),'2.264':1000*(.1/20+.1/10+.1/5),
 '2.267':2.9,'2.268':100.5/11.8,'2.269':12.6/40,'2.272':(47.7-2.4)/(98.8-2.4)*100,'2.273':41,
 '2.351':7+.4,'2.352':8.5-2,'2.354':(2.3+2.4+2.5+2.6+2.7)/5,'2.356':.5/50*100,'2.357':21.5-.5};
 const decimals={'2.240':2,'2.256':2,'2.263':2,'2.268':2,'2.272':1};
 for(const[id,full]of Object.entries(cases)){const v=id in decimals?Number(full.toFixed(decimals[id])):full,t=q(id);assert.ok(Math.abs(t.rättSvar-v)<=Math.max(t.tolerans||0,Math.abs(v)*1e-10),`${id}: ${v} vs ${t.rättSvar}`);}
 // Strictly less, not less than or equal: 40 fails, 41 passes.
 assert.equal(.30/(40*1.5),.005);assert.ok(.30/(41*1.5)<.005);
 // Exact difference of extreme products: the mixed uncertainty term cancels.
 assert.equal((6+.2)*(300+10)-(6-.2)*(300-10),2*6*10+2*300*.2);
 const E=.450*12**2/2,u=.002/.450+2*.3/12;assert.ok(Math.abs(E*u-1.764)<1e-12);
 // Regression from independent covariance calculation, including the non-zero intercept.
 const x=[10,20,35,50,65],y=[90,174,300,426,550];const xm=36,ym=308;
 const k=x.reduce((s,v,i)=>s+(v-xm)*(y[i]-ym),0)/x.reduce((s,v)=>s+(v-xm)**2,0),b=ym-k*xm;
 assert.ok(Math.abs(k-8.370558375634518)<1e-12);assert.ok(Math.abs(b-6.6598984771573555)<1e-12);
 assert.match(q('2.46').s,/8\{,\}3706/);assert.match(q('2.46').s,/6\{,\}6599/);
});
