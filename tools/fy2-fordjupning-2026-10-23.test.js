const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('fs'),vm=require('vm'),path=require('path');
const c={window:{}};vm.runInNewContext(fs.readFileSync(path.join(__dirname,'../uppgifter2.js'),'utf8'),c);const bank=c.window.BANK2,get=n=>bank.find(q=>q.id==='3.'+n),near=(a,b,t=1e-10)=>assert.ok(Math.abs(a-b)<=t*Math.max(1,Math.abs(b)),`${a} != ${b}`);
test('Sex fristående problemlösningar med verktyg, nivå och figurer',()=>{
 const levels={};for(let n=532;n<=537;n++){const q=get(n);assert.ok(q);assert.match(q.t,/<svg/);assert.match(q.s,/facit-svar/);assert.equal(q.spel,true);assert.equal(q.självrättning,true);assert.equal(q.miniräknare,true);assert.equal(q.geogebra,false);assert.equal(q.svarVardesiffror,2);assert.ok(q.formaga.includes('problemlosning'));assert.doesNotMatch(q.t,/Använd .*?=|e=Blv|g\s*=\s*9/);levels[q.traningsniva]=(levels[q.traningsniva]||0)+1;}
 assert.deepEqual(levels,{4:3,5:3});assert.equal(new Set(bank.map(q=>q.id)).size,bank.length);
 assert.equal(get(534).familj,'Hastighetsfilter och masspektrometer');assert.equal(get(535).familj,'Transformatorn och kraftöverföring');
});
test('Kopplade kroppar: Newtons lag på båda kropparna återger uppmätt acceleration',()=>{
 const R=get(532).rättSvar,I=.6*.4*1.8/R,F=.6*.4*I;
 near((.08*9.82-F)/(.08+.12),1.2);near(.08*(9.82-1.2)-F,.12*1.2);
 // Alternativt vanligt g ger samma korrekt avrundade tvåsiffriga svar.
 near(Number(((.6*.4)**2*1.8/(.08*9.81-.20*1.2)).toPrecision(2)),.19);
});
test('Två fria stavar: rörelsemängd, numerisk rörelse och värme stämmer',()=>{
 const m1=.1,m2=.3,B=.5,l=.4,R=.2,dt=.0001;let v1=0,v2=4,Q=0;
 for(let i=0;i<100000;i++){const I=B*l*(v2-v1)/R,F=B*l*I;Q+=I*I*R*dt;v1+=F/m1*dt;v2-=F/m2*dt;}
 near(v1,3,1e-9);near(v2,3,1e-9);near(m1*v1+m2*v2,1.2);near(Q,get(533).rättSvar,.0001);
 near(get(533).rättSvar,.5*.3*4**2-.5*(.1+.3)*3**2);
});
test('Jonens massa återskapar rätt diameter och energin',()=>{
 const m=get(534).rättSvar*1.66053906660e-27,q=2*1.602176634e-19,U=1500,B=.30,v=Math.sqrt(2*q*U/m),r=m*v/(q*B);
 near(2*r,.166);near(q*v*B,m*v*v/r);assert.match(get(534).t,/M145 220 A95 95 0 0 1 335 220/);
});
test('Generatorns effekt inkluderar RMS, kablar och generatorförluster',()=>{
 const U1=34/Math.sqrt(2),U2=5*U1,I2=U2/128,I1=I2*5;
 near(get(535).rättSvar*.8,U1*I1);near(get(535).rättSvar*.8,I2*I2*120+I2*I2*8);
});
test('Batteriet laddas och energin går ihop',()=>{
 const emf=.8*.5*20,I=(emf-6)/2,F=.8*.5*I;assert.ok(I>0);near(F*20,6*I+I*I*2);near(100*6*I/(F*20),get(536).rättSvar);
});
test('Växande area och minskande fält: produktens maximum, inte fältets nollpunkt',()=>{
 const flux=t=>.2*(.1+.05*t)*(.8-.2*t),t=get(537).rättSvar;
 near(t,1);near(flux(t),.018);assert.ok(flux(t-.2)<flux(t)&&flux(t+.2)<flux(t));assert.ok(flux(.1)>flux(0));assert.ok(flux(2.1)<flux(2));near((flux(t+1e-4)-flux(t-1e-4))/(2e-4),0);
});
