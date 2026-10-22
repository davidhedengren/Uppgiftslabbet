'use strict';
const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('node:fs'),vm=require('node:vm'),path=require('node:path');
const root=path.join(__dirname,'..'),ctx={window:{}};vm.runInNewContext(fs.readFileSync(path.join(root,'uppgifter.js'),'utf8'),ctx);
const bank=ctx.window.BANK,q=id=>bank.find(x=>x.id===id),ids=Array.from({length:40},(_,i)=>'8.'+(580+i));
const near=(actual,expected,id)=>{if(Array.isArray(expected)){assert.equal(actual.length,expected.length,id);expected.forEach((v,i)=>near(actual[i],v,id));return;}assert.ok(Math.abs(actual-expected)<1e-9*Math.max(1,Math.abs(expected)),`${id}: ${actual} / ${expected}`);};
// Independent calculations from the supplied values. No expected result is read from the bank.
const cases=[
 ['8.580',120*2.5],['8.581',3/.95],['8.582',24/3200*1000],['8.583',60/230],['8.584',8.5/.145],['8.585',24*1.25],
 ['8.586',6**2/11],['8.587',.345**2*12.5],['8.588',8.5**2/5400*1000],['8.589',.86**2*370],['8.590',12.7/.045],['8.591',4.5*.12],
 ['8.592',(3/24)*550],['8.593',[2300*.64,1800*.64]],['8.594',[6*1.55,12*1.55]],['8.595',(30/680)**2*82],['8.596',Math.min(Math.sqrt(.5/220),Math.sqrt(.5/470))*1000],['8.597',10/(6.3+8.6)],['8.598',1.2/.56+.56*15],['8.599',42*1.2/4.9],['8.600',[Math.sqrt(5*55),8.4/Math.sqrt(5/55)]],['8.601',6/4.5*15],['8.602',5/(10/15)],['8.603',.25/.045**2],
 ['8.604',42*4.9/1.2],['8.605',[5/Math.sqrt(8.4/55),Math.sqrt(8.4*55)]],['8.606',6/15*4.5],['8.607',5**2/10],['8.608',(12/60+12/120)*1000],['8.609',1.8/6+6/60],['8.610',9/(.09-9/150)],['8.611',4.4/220*(330+220)],['8.612',12/600*500],['8.613',.3/(1/120+1/240+1/80)],['8.614',12/(100+200)*200],['8.615',(9/300+9/600)*1000],['8.616',(2.4+3.6+6)/12],['8.617',[6/300*1000,6/100*1000]],['8.618',(12-6)/(3/6)],['8.619',(12/40)**2*20]
];
test('Alla 24 källfrågor och 16 varianter har oberoende omräknade svar',()=>{assert.equal(cases.length,40);for(const [id,v]of cases)near(q(id).rättSvar,v,id);assert.equal(new Set(bank.map(q=>q.id)).size,bank.length);});
test('Sammansatta nät löses även med Kirchhoffs strömlag i noderna',()=>{
 // Single internal node: R1 connects U to x; R2 and R3 connect x to zero.
 const branchVoltage=(U,R1,R2,R3)=>(U/R1)/(1/R1+1/R2+1/R3);
 const u614=branchVoltage(12,100,300,600),u619=branchVoltage(12,20,30,60);
 near(q('8.614').rättSvar,u614,'8.614 nod');near(q('8.619').rättSvar,(12-u619)**2/20,'8.619 nod');
 assert.ok(Math.abs((12-u614)/100-u614/300-u614/600)<1e-12);
 assert.ok(Math.abs((12-u619)/20-u619/30-u619/60)<1e-12);
 near((12-u619)**2/20+u619**2/30+u619**2/60,12*(12-u619)/20,'effektbalans');
});
test('Nivåer, verktyg, precision och namngivna fält följer själva frågan',()=>{
 const levels={1:0,2:0,3:0};
 for(const id of ids){const p=q(id);assert.ok(p,id);levels[p.traningsniva]++;assert.equal(p.kap,8);assert.equal(p.spel,true);assert.equal(p.självrättning,true);assert.equal(p.miniräknare,true);assert.equal(p.geogebra,false);assert.ok(p.ledtrad.length>35);assert.match(p.t,/\(Svara i [^<]+\)\<\/p\>/);assert.doesNotMatch(p.t,/använd \w+=|från [abc]\)|föregående del|^steg/i);assert.doesNotMatch(p.s,/facit-stegvis|Steg \d/);assert.doesNotMatch(p.t+p.s,/[\u0000-\u0008\u000b-\u001f]/);assert.equal(p.niva,p.traningsniva<3?'E':'C');
 if(Array.isArray(p.rättSvar)){assert.equal(p.svarsstruktur,'ordnad');assert.equal(p.rättSvar.length,p.svarEtiketter.length);assert.equal(p.rättSvar.length,p.svarEnhet.length);assert.equal(p.rättSvar.length,p.tolerans.length);assert.equal(p.rättSvar.length,p.svarFormat.length);assert.notDeepEqual(Array.from(p.svarEtiketter),['a','b']);}
 }
 assert.deepEqual(levels,{1:6,2:30,3:4});
 assert.match(q('8.599').t,/över R₂ är 42/);assert.match(q('8.604').t,/över R₁ är 42/);
 assert.match(q('8.602').t,/lampan är 15,0 V och dess effekt är 10,0 W/);assert.match(q('8.607').t,/resistorn är 5,00 V och dess effekt är 10,0 W/);
 assert.doesNotMatch(q('8.603').t,/9,0 W/);
});
test('Varje uppgift har en läsbar sluten krets; mätare och komponenter har egen symbol',()=>{
 for(const id of ids){const p=q(id),figs=[...p.t.matchAll(/<svg[\s\S]*?<\/svg>/g)];assert.equal(figs.length,1,id);assert.match(figs[0][0],/role="img"/);assert.match(figs[0][0],/max-width:480px/);assert.doesNotMatch(figs[0][0],/font-size="(?:[1-9]|1[0-4])"/);assert.match(figs[0][0],/aria-label=/);}
 for(const id of ['8.608','8.609','8.610','8.613','8.616']){const t=q(id).t;assert.match(t,/>A<\/text>/);assert.match(t,/M65 45L65 149/);assert.match(t,/M65 191L65 (295|330)/);assert.doesNotMatch(t,/M65 45L65 (295|330)/);}
 for(const id of ['8.614','8.619']){assert.match(q(id).t,/M270 120L320 120/);assert.match(q(id).t,/M380 120L435 120/);assert.doesNotMatch(q(id).t,/M270 120L435 120/);}
 assert.match(q('8.612').t,/M210 90L210 185/);assert.match(q('8.617').t,/M330 180L360 160/);
});
test('Liknande tidigare rättningar behåller sina korrekta resultat',()=>{
 for(const [id,v]of [['8.183',230*1.8],['8.184',12*4.5],['8.203',12**2/7],['8.214',2.6**2*.35],['8.226',1.4**2*1.1],['8.188',6/4.7],['8.189',5.6*1.8],['8.190',12/2.6],['8.192',10/.45],['8.208',.8*.25]])near(q(id).rättSvar,v,id);
});
