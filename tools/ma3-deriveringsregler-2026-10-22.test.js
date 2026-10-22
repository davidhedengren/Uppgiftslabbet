const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('fs'),vm=require('vm'),path=require('path');
const c={window:{}};vm.runInNewContext(fs.readFileSync(path.join(__dirname,'../uppgiftermato1.js'),'utf8'),c);const bank=c.window.BANKMATO1,q=id=>bank.find(q=>q.id===id),ids=Array.from({length:11},(_,i)=>'2.'+(1165+i));
test('Derivator och parameter räknas oberoende',()=>{
 const h=1e-5;for(const x of [.5,1,2,3])for(const [f,d] of [[()=>7,()=>0],[x=>-3*x+5,()=>-3],[x=>x*x,x=>2*x],[x=>4*x**3,x=>12*x*x],[x=>x*x+4,x=>2*x],[x=>x*(x+4),x=>2*x+4]])assert.ok(Math.abs((f(x+h)-f(x-h))/(2*h)-d(x))<1e-7);
 assert.equal(q('2.1165').rättSvar,'0');assert.equal(q('2.1166').rättSvar,'-3');assert.equal(q('2.1167').rättSvar,'2x');assert.equal(q('2.1170').rättSvar,3*(-2)**2);assert.equal(2*q('2.1171').rättSvar,6);assert.equal(q('2.1172').rättSvar,'2x+4');
 assert.equal(q('2.1168').alternativ.find(a=>a.ratt).txt,'Exponenten 3 ska bytas mot 2.');assert.match(q('2.1169').alternativ.find(a=>a.ratt).txt,/=f/);
});
test('Grundregler får tydlig progression, figurer och rätt verktyg',()=>{
 const levels={1:0,2:0,3:0};for(const id of ids){const t=q(id);levels[t.traningsniva]++;assert.equal(t.omr,'deriveringsregler');assert.equal(t.kap,2);assert.deepEqual(Array.from(t.kurs),['1b','1c']);assert.equal(t.spel,true);assert.ok([t.självrättning].flat().every(x=>x===true));assert.equal(t.miniräknare,true);assert.equal(t.geogebra,false);assert.match(t.s,/facit-svar/);assert.doesNotMatch(t.t+t.s,/[\u0000-\u0008\u000b-\u001f]|<p><\/p>/);}
 assert.deepEqual(levels,{1:6,2:2,3:3});for(const id of ['2.1165','2.1166','2.1167','2.1169','2.1171','2.1172','2.1173','2.1174'])assert.match(q(id).t,/<svg /);assert.match(q('2.1170').t,/<table/);assert.equal(new Set(bank.map(q=>q.id)).size,bank.length);
});
test('Nivå 3: tangentvillkor, lika hastighet och olika polynomgrader',()=>{
 const [a,b]=q('2.1173').rättSvar;assert.equal(1+a+b,2);assert.equal(2+a,(10-2)/(3-1));assert.equal(q('2.1173').svarsstruktur,'ordnad');
 assert.deepEqual(Array.from(q('2.1174').rättSvar),[0,4]);for(const t of q('2.1174').rättSvar)assert.equal(3*t*t,12*t);for(const t of [1,2,3,5])assert.notEqual(3*t*t,12*t);assert.equal(q('2.1174').svarsstruktur,'mängd');
 assert.equal(q('2.1175').alternativ.filter(a=>a.ratt).length,1);assert.match(q('2.1175').alternativ.find(a=>a.ratt).txt,/linjär.*grad 2/);
 for(const id of ['2.1173','2.1174','2.1175']){assert.equal(q(id).niva,'C');assert.equal(q(id).traningsniva,3);}
});
test('Fem äldre jämförelser har rätt derivatavärden och tillåter miniräknare',()=>{
 const h=1e-5;
 for(const [id,f,x] of [['2.30',x=>2*x**3-5*x,2],['2.34',x=>x**4-2*x*x,-1],['2.38',x=>3*x*x+4*x-1,3],['2.142',x=>2*x**5+x,-1],['2.177',x=>5*x**3-7,-2]]){
  assert.ok(Math.abs((f(x+h)-f(x-h))/(2*h)-q(id).rättSvar)<1e-6,id);assert.equal(q(id).miniräknare,true);assert.equal(q(id).geogebra,false);assert.equal(q(id).traningsniva,2);
 }
});
test('De nya nivå 3-grafernas faktiska koordinater följer givna samband',()=>{
 for(const [id,xmax,ymin,ymax,fs] of [['2.1173',3.5,-2,12,[x=>4*x-2]],['2.1174',5,0,160,[x=>x**3,x=>6*x*x]]]){
  const curves=[...q(id).t.matchAll(/<path d="([^"]+)"/g)].map(m=>m[1]).filter(d=>d.length>1000);assert.equal(curves.length,fs.length);
  curves.forEach((d,i)=>{for(const pair of d.slice(1).split(' L')){const [px,py]=pair.split(' ').map(Number),x=(px-60)*xmax/370,y=ymax-(py-42)*(ymax-ymin)/238;assert.ok(Math.abs(y-fs[i](x))<.002,id);}});
 }
});
