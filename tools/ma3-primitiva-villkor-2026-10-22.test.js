const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('fs'),vm=require('vm'),path=require('path');
const c={window:{}};vm.runInNewContext(fs.readFileSync(path.join(__dirname,'../uppgiftermato1.js'),'utf8'),c);const bank=c.window.BANKMATO1,q=id=>bank.find(q=>q.id===id),ids=Array.from({length:6},(_,i)=>'3.'+(1195+i));
test('Punktvillkor, parameter och integralvillkor räknas oberoende',()=>{
 assert.equal(q('3.1195').alternativ.find(a=>a.ratt).txt,'Kurva B.');assert.equal(q('3.1196').rättSvar,10+2*(4-3));
 const f=x=>x**3+5,g=x=>x*x+2*x-1;assert.equal(f(-1),4);assert.equal(g(1),2);assert.equal(g(3),14);
 assert.equal(q('3.1197').rättSvar,'x^3+5');assert.equal(q('3.1198').rättSvar,'x^2+2x-1');assert.equal(q('3.1199').rättSvar,'x^2+1');assert.ok(Math.abs(2**3/3+2-14/3)<1e-12);
 for(const C of [-10,0,3,27])assert.equal((4+C)-C,4);assert.match(q('3.1200').alternativ.find(a=>a.ratt).txt,/alla funktioner/);
 const h=1e-5;for(const x of [-2,-1,0,1,2]){assert.ok(Math.abs((f(x+h)-f(x-h))/(2*h)-3*x*x)<1e-7);assert.ok(Math.abs((g(x+h)-g(x-h))/(2*h)-(2*x+2))<1e-7);}
});
test('Två nivå 1, en nivå 2 och tre nivå 3 med fristående svar och rätt verktyg',()=>{
 const levels={1:0,2:0,3:0};for(const id of ids){const t=q(id);levels[t.traningsniva]++;assert.equal(t.omr,'primitiva_villkor');assert.equal(t.kap,3);assert.deepEqual(Array.from(t.kurs),['1b','1c']);assert.equal(t.spel,true);assert.equal(t.självrättning,true);assert.equal(t.miniräknare,true);assert.equal(t.geogebra,false);assert.match(t.s,/facit-svar/);assert.ok(['Primitiv funktion genom en given punkt','Återskapa funktion från derivata'].includes(t.familj));assert.doesNotMatch(t.t+t.s,/[\u0000-\u0008\u000b-\u001f]|<p><\/p>/);}
 assert.deepEqual(levels,{1:2,2:1,3:3});for(const id of ids.slice(0,4))assert.match(q(id).t,/<svg /);assert.match(q('3.1200').t,/<table/);assert.equal(new Set(bank.map(q=>q.id)).size,bank.length);
});
test('Grafalternativens faktiska koordinater är rätt parabelfamilj',()=>{
 const curves=[...q('3.1195').t.matchAll(/<path d="([^"]+)"/g)].map(m=>m[1]).filter(d=>d.length>1000);assert.equal(curves.length,3);
 curves.forEach((d,i)=>{for(const pair of d.slice(1).split(' L')){const [px,py]=pair.split(' ').map(Number),x=-1.5+(px-60)*3/370,y=5-(py-42)*8/238;assert.ok(Math.abs(y-(x*x+[-2,2,0][i]))<.0001);}});
});
