'use strict';
const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('fs'),vm=require('vm');
const load=f=>{const c={window:{}};vm.runInNewContext(fs.readFileSync(__dirname+'/../'+f,'utf8'),c);return Object.values(c.window)[0];};
const fy1=load('uppgifter.js'),fy2=load('uppgifter2.js'),matf=load('uppgiftermatf1.js');
const q=(b,id)=>b.find(x=>x.id===id),near=(a,b,t=1e-10)=>assert.ok(Math.abs(a-b)<=Math.abs(b)*t,`${a} ≠ ${b}`);
test('Mikroampere som distraktor; varierad grundordning utan att förlora svar',()=>{
 const p=q(fy1,'8.559');assert.ok(p.alternativ.some(a=>a.txt==='4000 µA'&&!a.ratt));assert.equal(p.alternativ.find(a=>a.ratt).txt,'V');
 const counts=[0,0,0,0,0],byLength={};for(const p of fy1.filter(x=>x.omr==='multimeter'&&x.alternativ)){
  assert.equal(new Set(p.alternativ.map(a=>a.txt)).size,p.alternativ.length,p.id);
  if(p.alternativ.filter(a=>a.ratt).length===1){const n=p.alternativ.length,i=p.alternativ.findIndex(a=>a.ratt);counts[i]++;(byLength[n] ||= Array(n).fill(0))[i]++;}
 }
 assert.ok(counts.slice(0,4).every(n=>n>0),counts);assert.ok(counts[0]<counts.reduce((a,b)=>a+b)*.4,counts);for(const c of Object.values(byLength))assert.ok(Math.max(...c)-Math.min(...c)<=1,c);
});
test('Figurerna ger inte räknealgoritmen; permutationernas facit oförändrade',()=>{
 for(const [id,word,result] of [['1.137','ANANAS',60],['1.40','MATEMATIK',45360],['1.73','STATISTIK',15120]]){
  const p=q(matf,id),svg=p.t.match(/<svg[\s\S]*?<\/svg>/)[0];assert.ok(!/gånger|brickor med|förekommer/.test(svg));assert.equal(p.rättSvar,result);
  assert.equal([...svg.matchAll(/<text[^>]*>([^<]+)<\/text>/g)].map(m=>m[1]).join(''),word);
 }
 const p=q(matf,'1.152'),svg=p.t.match(/<svg[\s\S]*?<\/svg>/)[0];assert.ok(!/fixer|<text/.test(svg));assert.equal((svg.match(/<circle/g)||[]).length,7);assert.equal(p.rättSvar,120);
 assert.ok(!/Blocken kan byta plats|ett block/.test(q(matf,'1.26').t));
});
test('Bläckdroppens krafttecken och fullständiga självständiga delkort',()=>{
 const p=q(fy2,'3.346'),a=1.5e-13*1.4e6/1.3e-10-9.82,t=.016/18;
 near(p.rättSvar[0],a*t*t/2);near(p.rättSvar[1],Math.atan(a*t/18)*180/Math.PI);
 for(const d of p.spelDelar){assert.match(d.t,/fältet är riktat nedåt/);assert.match(d.t,/tyngdkraften/);assert.match(d.t,/<svg/);assert.match(d.s,/1606/);assert.match(d.s,/8\{,\}89/);assert.ok(!/facit-steglista/.test(d.s));assert.equal(d.miniräknare,true);}
 assert.ok(!/försumbar/.test(JSON.stringify(p)));assert.equal(p.spelDelar[1].traningsniva,4);
});
test('Oljedroppens tyngd behövs; b använder samma data och mål som facit',()=>{
 const p=q(fy2,'3.354'),m=820*4*Math.PI*(.5e-6)**3/3,e=1.602176634e-19;
 near(p.rättSvar[0],m*9.82/(5*e));near(p.rättSvar[1],m*9.82*.0225/(5*e));assert.equal(p.rättSvar[2],8);
 for(const d of p.spelDelar){assert.match(d.t,/1,00 µm/);assert.match(d.t,/0,820 g\/cm³/);assert.match(d.s,/820/);assert.match(d.t,/<svg/);assert.ok(!/elektroner och protoner|5\{,\}3/.test(d.t));}
 assert.match(p.spelDelar[1].t,/5 överskottselektroner/);assert.match(p.spelDelar[1].s,/118\{,\}42/);assert.equal(p.spelDelar[1].traningsniva,3);
 assert.ok(p.svarTabell[1].some(n=>Math.abs(n-118.43333653448713)<1e-9));
 assert.ok(!/tyngdkraften på elektroner och protoner/.test(JSON.stringify(q(fy2,'3.353'))));
});
test('Fem jämförelser: partikel, inträdesriktning och talvärden',()=>{
 for(const id of ['3.337','3.338','3.339','3.340','3.341'])assert.ok(!/elektroner och protoner/.test(JSON.stringify(q(fy2,id))),id);
 const e=1.602e-19,me=9.109e-31,mp=1.673e-27;
 const t=.0225/5.4e6,a=2*.00618/t**2;
 near(q(fy2,'3.337').rättSvar[0],me*a/e,.001);near(q(fy2,'3.337').rättSvar[1],Math.hypot(5.4e6,a*t),.001);
 near(q(fy2,'3.338').rättSvar[0],.5*e*(90/.02)/me*(.05/1e7)**2,.001);
 near(q(fy2,'3.339').rättSvar[0],.5*e*4e5/mp*(.12/1.5e7)**2,.001);
 near(q(fy2,'3.340').rättSvar,me*(3e6)**2*Math.tan(10*Math.PI/180)/(e*2),.001);
 near(q(fy2,'3.341').rättSvar,.5*e*1000/me*(.03/2.7e6)**2,.001);
 assert.match(q(fy2,'3.339').t,/vinkelrätt/);assert.match(q(fy2,'3.341').t,/vinkelrätt/);assert.equal(q(fy2,'3.341').traningsniva,3);
});
test('Kondensatorer: enheter, prefix, svar och tillåten miniräknare',()=>{
 const expected={'3.115':22*9,'3.116':100*5,'3.117':470*12,'3.118':360/12,'3.119':150/25,'3.120':.5*220e-6*12**2*1000,'3.121':.5*47e-6*24**2*1000,'3.122':Math.sqrt(2*.020/100e-6)};
 for(const [id,value] of Object.entries(expected)){const p=q(fy2,id);near(p.rättSvar,value);assert.equal(p.miniräknare,true);assert.equal(p.geogebra,false);assert.match(p.t,/\(Svara i /);assert.match(p.t,/<svg/);assert.ok(!/facit-steglista/.test(p.s));}
});
test('Avancerad resonans förblir tillgänglig för lärare men väljs inte i elevträning',()=>{
 for(const id of ['4.30','4.153','4.32','4.34','4.490']){const p=q(matf,id);assert.equal(p.spel,false);assert.equal(p.traningsniva,5);assert.match(p.t,/Fördjupning utanför/);assert.equal(p.geogebra,true);assert.equal(p.miniräknare,true);}
 for(const id of ['4.81','4.106','4.386'])assert.equal(q(matf,id).spel,false);
});
