const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('fs'),vm=require('vm'),path=require('path');
const ctx={window:{}};vm.runInNewContext(fs.readFileSync(path.join(__dirname,'../uppgiftermato1.js'),'utf8'),ctx);
const bank=ctx.window.BANKMATO1,q=id=>bank.find(q=>q.id===id),ids=Array.from({length:6},(_,i)=>'2.'+(1144+i));
test('h, konstant derivata och tvåsidigt gränsvärde räknas oberoende',()=>{
 assert.ok(Math.abs(q('2.1144').rättSvar-(4.2-4))<1e-12);assert.ok(Math.abs(q('2.1145').rättSvar-(4.7-5))<1e-12);assert.equal(q('2.1146').rättSvar,0);assert.equal(q('2.1148').rättSvar,2.5);
 const f=x=>x*x-1.5*x;for(const h of [-.1,-.01,-.001,.001,.01,.1])assert.ok(Math.abs((f(2+h)-f(2))/h-(2.5+h))<1e-10);
 const correct=q('2.1147').alternativ.find(a=>a.ratt);assert.match(correct.txt,/2\(1\+h\)\^2-2/);assert.match(q('2.1149').alternativ.find(a=>a.ratt).txt,/Derivatan är 2,/);
 for(const h of [-.5,-.01,.01,.5]){assert.ok(Math.abs((2*(1+h)**2-2)/h-(4+2*h))<1e-10);assert.ok(Math.abs((2*h+h*h)/h-(2+h))<1e-10);}
});
test('Självbärande begreppskort, nivåer och figurkontrakt',()=>{
 const levels={1:0,2:0,3:0};for(const id of ids){const t=q(id);assert.ok(t);levels[t.traningsniva]++;assert.equal(t.omr,'derivatans_definition');assert.deepEqual(Array.from(t.kurs),['1b','1c']);assert.equal(t.spel,true);assert.equal(t.självrättning,true);assert.equal(t.miniräknare,true);assert.equal(t.geogebra,false);assert.equal(t.spelDelning,undefined);assert.match(t.s,/facit-svar/);assert.doesNotMatch(t.t+t.s,/[\u0000-\u0008\u000b-\u001f]|<p><\/p>/);if(id==='2.1148')assert.match(t.t,/<table/);else assert.equal((t.t.match(/<svg /g)||[]).length,1);if(t.alternativ)assert.equal(t.alternativ.filter(a=>a.ratt).length,1);}
 assert.deepEqual(levels,{1:4,2:1,3:1});assert.equal(new Set(bank.map(q=>q.id)).size,bank.length);
});
