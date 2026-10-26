'use strict';
const {test}=require('node:test'),assert=require('node:assert/strict');
const fs=require('node:fs'),vm=require('node:vm'),path=require('node:path');
const c={window:{}};
for(const file of ['uppgifterma1.js','uppgifter.js'])vm.runInNewContext(fs.readFileSync(path.join(__dirname,'..',file),'utf8'),c);
const q=id=>c.window.BANKMA1.find(q=>q.id===id);
// Oberoende modeller: tal och samband från uppgiftstexterna, aldrig hämtade från facit.
const models=[
 ['7.01',[1.8/12,1.8/12*30]],['7.03',[2.45*100,1250/1000,32/10]],
 ['7.06',[36*1.08]],['7.07',[780+1250,(780+1250)*.06,(780+1250)*1.06]],
 ['7.08',[120*.75]],['7.10',[2.5/10*18]],
 ['3.81',[5000*.04]],['3.85',[18000*.03]],['3.87',[20000*1.02*.02]],['3.112',[900000*.04/12]],
 ['3.39',[16439.38/1.055**3]],['3.08',[(10500-10000)/10000*100]],
 ['3.126',[((11255.09/10000)**.25-1)*100]],['3.80',[(27208.48/((20000*1.02+5000)*1.04)-1)*100]],
 ['3.82',[(Math.sqrt(1.21275/1.05)-1)*100]],['3.89',[384/12000*100]],
 ['3.07',[(1-(178000/260000)**.2)*100]],
 ['3.40',[1+.024,'12000*1.024^5',12000*1.024**5]],
 ['3.127',[1350*10*12,1350*10*12-120000,780/1350*100]],
 ['3.25',[75*150/100,(135-75*150/100)/(75*150/100)*100]],
 ['3.26',[143-100,250*143/100,480*100/160]],
 ['3.28',[2400*1.25,1875/1.25,1875-1875/1.25]],
 ['3.38',[99000/.18,((680000/(99000/.18))**.25-1)*100]],
 ['3.88',[1+.028,8200*1.028**3,8200*1.028**3-8200]],
 ['3.223',[7500*1.018**2]],['3.203',[10000*1.025**5]],['3.217',[8000*1.03**2]],
 ['3.518',[10000*1.03**5]],['3.519',[25000*1.02**10]],['3.520',[4000*1.045**3]],
 ['3.84',[Math.ceil(120/(.032-.025))]],
];
test('Matematik: rättningsmål följer oberoende beräkningar i 31 uppgifter',()=>{
 for(const[id,values]of models){const t=q(id),answers=Array.isArray(t.rättSvar)?t.rättSvar:[t.rättSvar];assert.equal(answers.length,values.length,id);
 values.forEach((value,i)=>typeof value==='string'?assert.equal(answers[i],value,id):assert.ok(Math.abs(Number(answers[i])-value)<1e-8,id+' del '+i));}
});
test('Enheter, precisionskrav och givna belopp följer med fristående delkort',()=>{
 assert.deepEqual(Array.from(q('7.01').svarEnhet),['kg','kg']);
 assert.deepEqual(Array.from(q('7.03').svarFormat),['decimalform','decimalform','decimalform']);
 for(const id of ['3.08','3.126','3.80','3.82','3.89','3.07'])assert.equal(q(id).svarEnhet,'%',id);
 assert.match(q('3.40').spelDelar[2].t,/12 000 kr/);
 assert.match(q('3.40').spelDelar[2].t,/två decimaler/);
 assert.match(q('3.28').spelDelar[2].t,/cykel kostar 1 875 kr med moms/);
 assert.match(q('3.88').spelDelar[1].t,/två decimaler/);
 assert.match(q('3.88').spelDelar[2].t,/två decimaler/);
 assert.doesNotMatch(q('3.127').spelDelar[2].t,/10 år|120 000/);
});
test('Avrundning använder fullprecision och halva steget, inte ett allmänt procentintervall',()=>{
 for(const id of ['3.223','3.203','3.217','3.518','3.519','3.520','3.39']){assert.equal(q(id).tolerans,.5);assert.match(q(id).t,/hela kronor/);}
 assert.equal(q('3.40').tolerans[2],.005);assert.equal(q('3.88').tolerans[1],.005);assert.equal(q('3.88').tolerans[2],.005);
 assert.equal(q('3.126').tolerans,.05);assert.equal(q('3.82').tolerans,.005);
});
test('Avgiftens tidpunkt och nettobehovets spillpåslag har uttryckligt angiven jämförelsegrund',()=>{
 for(const id of ['3.258','3.256','3.84'])assert.match(q(id).t,/efter att räntan lagts till/,id);
 assert.match(q('3.86').t,/startavgift dras direkt/);
 assert.equal(2000*1.018-50,1986);assert.equal(2000*1.016,2032);assert.equal(q('3.258').alternativ.find(a=>a.ratt).txt,'B'); // flervalskort sedan 2026-10-24
 
 assert.equal(10000*1.03,10300);assert.equal(10000*1.035-100,10250);assert.equal(q('3.256').alternativ.find(a=>a.ratt).txt,'Konto A');
 assert.equal(Math.ceil(120/(.032-.025)),17143);assert.equal(q('3.84').rättSvar,17143);
 const a=1.03**5,b=1.045**2*1.022**3,bound=300*b/(b-a);
 assert.ok(bound>54456&&bound<54457);assert.match(q('3.86').t,/300 kr/);
 assert.match(q('7.06').t,/8 % mer än den mängden/);
});
test('Två värdesiffror i fysik: 6.470 c har korrekt mål, precision och självständiga givna data',()=>{
 const t=c.window.BANK.find(q=>q.id==='6.470');assert.equal(t.rättSvar[2],70*9.82);assert.equal(t.tolerans[2],5);
 assert.ok(Math.abs(690-t.rättSvar[2])<t.tolerans[2]);assert.match(t.spelDelar[2].t,/70 kg/);assert.equal(t.svarVardesiffror[2],2);assert.doesNotMatch(t.spelDelar[2].t,/värdesiffror/);assert.equal(t.spelDelar[2].traningsniva,1);
});
