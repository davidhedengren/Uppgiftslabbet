const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('fs'),vm=require('vm'),path=require('path');
const ctx={window:{}};vm.runInNewContext(fs.readFileSync(path.join(__dirname,'../uppgiftermato1.js'),'utf8'),ctx);const bank=ctx.window.BANKMATO1,q=id=>bank.find(q=>q.id===id),ids=Array.from({length:7},(_,i)=>'2.'+(1158+i));
test('Tabeller, modellvärden och grafpunkter ger rätt lutningar',()=>{
 for(const [f,d] of [[4,10],[8,20],[12,30]])assert.equal(d/f,q('2.1158').rättSvar);
 const xp=Math.log(2)/.4;assert.ok(Math.abs(10*Math.exp(-.4*xp)-5)<1e-12);assert.equal(-.4*5,q('2.1159').rättSvar);assert.equal(-.2*50,q('2.1160').rättSvar);assert.equal(-2/4,q('2.1164').rättSvar);
 for(const f of [1,3,10])assert.equal(.08*(2*f),2*(.08*f));
 assert.equal(q('2.1161').alternativ.find(a=>a.ratt).txt,'Det fördubblas.');assert.match(q('2.1162').alternativ.find(a=>a.ratt).txt,/g\\\)/);assert.ok(6*.5>6*.2);
 assert.match(q('2.1163').alternativ.find(a=>a.ratt).txt,/f\(x\)-4/);
 const h=1e-5,F=x=>4+3*Math.exp(2*x);
 for(const x of [-1,0,.5,1])assert.ok(Math.abs((F(x+h)-F(x-h))/(2*h)-2*(F(x)-4))<1e-7);
});
test('Nivåer, tabell, figurer och verktyg följer frågornas krav',()=>{
 const levels={1:0,2:0,3:0};for(const id of ids){const t=q(id);levels[t.traningsniva]++;assert.equal(t.kap,2);assert.equal(t.omr,'derivata_exponential');assert.deepEqual(Array.from(t.kurs),['1b','1c']);assert.equal(t.spel,true);assert.equal(t.självrättning,true);assert.equal(t.miniräknare,true);assert.equal(t.geogebra,false);assert.equal(t.spelDelning,undefined);assert.match(t.s,/facit-svar/);assert.doesNotMatch(t.t+t.s,/[\u0000-\u0008\u000b-\u001f]|<p><\/p>/);}
 assert.deepEqual(levels,{1:5,2:1,3:1});assert.equal(q('2.1160').svarEnhet,'g/min');assert.match(q('2.1158').t,/<table/);for(const id of ['2.1159','2.1160','2.1162','2.1164'])assert.match(q(id).t,/<svg /);assert.equal(new Set(bank.map(q=>q.id)).size,bank.length);
});
