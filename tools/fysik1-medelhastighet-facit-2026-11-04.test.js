'use strict';
const {test}=require('node:test'),assert=require('node:assert/strict');
const fs=require('node:fs'),vm=require('node:vm'),path=require('node:path');
const c={window:{}};vm.runInNewContext(fs.readFileSync(path.join(__dirname,'../uppgifter.js'),'utf8'),c);
const tasks=c.window.BANK.filter(q=>q.omr==='medelhastighet'),q=id=>tasks.find(q=>q.id===id);

test('Alla 92 huvudfacit och 125 delkort har komplett facitstruktur',()=>{
 assert.equal(tasks.length,92);let cards=0;
 for(const t of tasks){
  assert.equal(t.miniräknare,true,t.id);
  for(const[id,s]of[[t.id,t.s],...(t.spelDelar||[]).map(d=>[t.id+d.etikett,d.s])]){
   assert.match(s,/<ol class="facit-steglista" role="list">/,id);
   assert.match(s,/<p class="facit-rubrik">/,id);
   assert.match(s,/<p class="facit-svar"><strong>Svar:<\/strong>/,id);
   assert.doesNotMatch(s,/undefined|None|facit-forklaring/,id);
  }
  const text=t.t.replace(/<svg[\s\S]*?<\/svg>/g,'');
  const n=(text.match(/<li>/g)||[]).length||(text.match(/<p>\s*[a-z]\)/g)||[]).length;
  if(n>1)assert.equal((t.s.match(/class="facit-del"/g)||[]).length,n,t.id);
  for(const d of t.spelDelar||[]){assert.notEqual(d.miniräknare,false,t.id);cards++;}
 }
 assert.equal(cards,125);
});

test('Icke-linjära fartproblem löses grafiskt och kontrolleras i ursprungsekvationen',()=>{
 const cases=[['2.301',2,60,v=>240/v-240/(v+20),1],
 ['2.303',0,6,v=>3/(v-3)+3/(v+3),4/3],
 ['2.303',1,200,v=>750/(v-50)+750/(v+50),8],
 ['2.303',2,8,v=>30/(v+2)+30/(v-2),8],
 ['2.315',0,30,v=>120/(v-10)-120/v,2],
 ['2.315',1,20,v=>150/v-150/(v+5),1.5],
 ['2.315',2,56,v=>140/v-152/(v+20),.5]];
 for(const[id,i,v,f,target]of cases){const t=q(id),d=t.spelDelar[i];
  assert.equal(t.geogebra,true,id);assert.notEqual(d.geogebra,false,id);
  assert.equal(t.rättSvar[i],v,id);assert.ok(Math.abs(f(v)-target)<1e-12,id);
  assert.match(d.s,/Lös ekvationen grafiskt/);assert.match(d.s,/<svg/);
  assert.match(d.s,/Fart \(km\/h\)/);assert.match(d.s,/<polyline/);
 }
 assert.equal((q('2.301').s.match(/<svg/g)||[]).length,1);
 assert.equal((q('2.303').s.match(/<svg/g)||[]).length,3);
 assert.equal((q('2.315').s.match(/<svg/g)||[]).length,3);
});

test('Oberoende kontroller av tidsstart, vägsträcka, relativ fart och modellgränser',()=>{
 // Equal distances and equal durations must not be averaged the same way.
 assert.equal(4/(2/12+2/28),16.8);assert.equal((4.2+5.6)/2,4.9);
 assert.equal(q('3.9').rättSvar,16.8);assert.equal(q('3.179').rättSvar,4.9);
 assert.equal(200/(100/80+100/120),96);assert.match(q('3.97').s,/96/);
 assert.ok(Math.abs(90/(1.2+.8)+90/(1.2-.8)-270)<1e-10);
 assert.match(q('3.234').s,/270/);assert.match(q('3.234').s,/v-u/);
 assert.match(q('3.229').s,/v_1\\gt V\/2/);
 assert.equal((340+2)*.600/2,102.6);assert.match(q('3.238').s,/102\{,\}6/);
 assert.ok(Math.abs((500/42.38)*.030-.35394053798961775)<1e-12);
 assert.match(q('3.237').s,/0\{,\}354/);
 assert.equal((4500/9.2/60).toFixed(1),'8.2');
 assert.equal((625/60).toFixed(1),'10.4');assert.equal((3125/60).toFixed(1),'52.1');
 for(const val of ['8{,}2','10{,}4','52{,}1'])assert.ok(q('2.307').s.includes(val));
 // Same-direction overtaking requires both train lengths, unlike a window observer.
 assert.equal((200+800)/((72-27)/3.6),80);assert.equal(q('2.318').rättSvar[3],80);
 assert.equal((72+32.4)/3.6*10,290);assert.equal(q('2.317').rättSvar[2],290);
 // The receiver moves towards successive pulses: reception interval is shorter than emission interval.
 const u=40/3.6,dt=1500*5/(1500+u);assert.ok(dt<5);
 assert.equal((u*dt).toFixed(1),'55.1');assert.equal(q('2.320').rättSvar,55.1);
});

test('Varje numerisk huvudnyckel i området kontrolleras från givna data',()=>{
 const cases={
 '3.1':[92*60,Math.round(4.25e7/(92*60)),Math.round(4.25e7/(92*60)*3.6)],
 '3.2':[380/9.5,9.5*3.6],'3.3':[2*3600+5*60,42195/7500,Math.round(7500/42.195)],
 '3.9':4/(2/12+2/28),'3.19':[11.2+10.4+10.8+10.6,400/43,100/10.4],
 '3.20':[340*.4/2,340*1.1/2,340*(.4+1.1)/2],'3.21':[1500*.8,1500*.8/2,1500*.2/2],
 '3.49':[8*30*86400,7e7/(8*30*86400),70000/(8*30*24)],
 '3.50':[1.8+.7,1.8-.7,500/(1.8+.7),Math.round(500/(1.8-.7))],
 '3.51':[(32+14)/24,(32-14)/24],'3.53':[11.5*32,470/32,820/15],
 '3.54':[1.5*3.6,54/3.6,90*3.6,72/3.6],'3.55':[12/1000,340*.012,340*.012/2],
 '3.96':[45/100,15*60,.45/900,.45/900*86400],'3.99':[150/(80/3.6),80/3.6*2.5],
 '3.101':[Math.round(2*Math.PI*7071/100)*100,2*Math.PI*7071/7.5/60],
 '3.102':660/30,'3.235':(5/12)/(1/75-1/200-1/240),
 '3.236':[90/(180/100-90/90-12/60),180/(90/90+12/60+90/120)],
 '3.126':340/(2+50/60),'3.127':[20200e3/3e8*1000,3e8*1e-6],
 '3.129':[(3+2)*1000,(15+20)*60,5000/2100],'3.130':2*85/.5,
 '3.131':[240/3,1.2*240/3,Math.asin(1.2/3)*180/Math.PI,240/Math.sqrt(3**2-1.2**2)],
 '3.132':[2.998e8*3.156e7,2.5e11/2.998e8/60],'3.134':[210/7,210/7*3.6,210/7*3.6/90],
 '3.178':60/(30/60+30/90),'3.179':(4.2+5.6)/2,'3.256':135/11,'3.257':6*15,
 '3.258':340/14,'3.259':10*3.6,'3.260':50/3.6,'3.261':20-20,'3.262':650/(2.5*60),
 '2.291':[25000/1.5/3600,25/18,25/70*60,25/.69],
 '2.292':[340*4.6,18000/.00013,340*.2/2,100/.0665],
 '2.293':[110*17/60,42.5/110*60],
 '2.294':[15/(145/3.6),7.32/(25/(100/3.6)),35/(28-16),20/.0075/60],
 '2.295':[10/18*60,10/(10/18-5/60)],'2.296':(35/60)/(1/12+1/9),'2.298':420*24/3600,
 '2.297':[186/(8/3.6),15*27/33,186/(163/3.6)],'2.299':[6.7*900+8.2*720,11934/2100],
 '2.300':[400/(12/3.6)-400/(15/3.6),400-(12/3.6)*400/(15/3.6)],
 '2.301':[(2/60)/(1/72-1/80),(80/90-80/95)*60,(-20+Math.sqrt(20**2+4*4800))/2,4*18],
 '2.302':.85*(1.25*5/(1.25-.85)),
 '2.303':[(9+Math.sqrt(81+4*2*18))/4,(187.5+Math.sqrt(187.5**2+10000))/2,(15+Math.sqrt(225+64))/4],
 '2.304':5/(5/340-.0137),'2.305':[(36/6-4)/(1/4-1/6),1500*.3/2],
 '2.306':[1/(2.4e5+6.7e6),(32*5/60)/(38-32)*60,38*(32*5/60)/(38-32)],
 '2.307':[4500/9.2/60,625/60,3125/60],'2.308':[10/12+10/8.5,3e8/(2*Math.PI*4200)],
 '2.309':(1+360/102-360/85)*60,'2.310':[(90-14)/(8/3),95/(95-85),(85/80-30/70-55/95)*60],
 '2.311':(1000/4.5e-4-1.2e6)/2*4.5e-4,
 '2.312':[343*.02332/2,2*3.99938/.02993,2*3.99938/1304],
 '2.313':1200/3.6+800/3.9-1500/4-500/3.1,
 '2.314':[(5/12-5/14.5)*60,8-11*8/14],
 '2.315':[(10+Math.sqrt(100+2400))/2,(-5+Math.sqrt(25+2000))/2,(-44+Math.sqrt(44**2+22400))/2],
 '2.316':[(115-15)/2.5*1.5+15,15*5/(25-15),255/(2+2.5*1.75),1/(1/60-1/80)],
 '2.317':[2/(1/8+1/12),2/(1/6-1/8),(72+32.4)/3.6*10,(42/1.4+42/1.68)/2],
 '2.318':[300/(1/3.65+1/2.35),24/((90+36)/3.6),(72-54)/3.6*60,(200+800)/((72-27)/3.6)],
 '2.319':[60*(40/6)/(60-40),5/610*3600],'2.320':(40/3.6)*(7500/(1500+40/3.6)),
 '2.335':(180-100)/40,'2.336':600/480,'2.337':(50-20)/30,'2.338':40/25,'2.339':60/6,
 '2.340':8/.4,'2.341':300/(54/3.6),'2.342':540/(1/6+1/4),'2.343':8/.5,'2.344':16/4,
 '2.346':90/3.6,'2.348':150/100,'2.349':600/120,'2.350':30/.5};
 const numerical=tasks.filter(t=>typeof t.rättSvar==='number'||Array.isArray(t.rättSvar));
 assert.deepEqual(Array.from(numerical,t=>t.id).sort(),Object.keys(cases).sort());
 for(const t of numerical){const values=[].concat(cases[t.id]),actual=[].concat(t.rättSvar);
  assert.equal(values.length,actual.length,t.id);
  values.forEach((v,i)=>{const precision=Array.isArray(t.svarVardesiffror)?t.svarVardesiffror[i]:t.svarVardesiffror;
   const rounding=precision&&v!==0?.500001*10**(Math.floor(Math.log10(Math.abs(v)))-precision+1):0;
   const tol=Array.isArray(t.tolerans)?t.tolerans[i]:t.tolerans;
   assert.ok(Math.abs(v-actual[i])<=Math.max(tol||0,rounding,Math.abs(v)*1e-12),`${t.id} ${i}: ${v} vs ${actual[i]}`);
  });
 }
});
