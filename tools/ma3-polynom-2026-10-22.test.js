const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('fs'),vm=require('vm'),path=require('path');
const ctx={window:{}};vm.runInNewContext(fs.readFileSync(path.join(__dirname,'../uppgiftermato1.js'),'utf8'),ctx);
const bank=ctx.window.BANKMATO1,q=id=>bank.find(q=>q.id===id),ids=Array.from({length:6},(_,i)=>'1.'+(868+i));
test('Konstanttermer, grad och koefficient beräknas från egna modeller',()=>{
 const p=x=>2*x*x-5*x-3;assert.deepEqual([-1,0,1,2].map(p),[4,-3,-6,-5]);assert.equal(q('1.868').rättSvar,p(0));assert.equal(q('1.871').rättSvar,0**3/4-0-2);
 for(const x of [.5,1,2,3,5]){assert.equal((x+4)*(x+1),x*x+5*x+4);assert.equal(x*2*x*(x+1),2*x**3+2*x*x);assert.equal(3*x**4+2*x*x-3*x**4+x**3,x**3+2*x*x);}
 assert.equal(q('1.869').rättSvar,2);assert.equal(q('1.872').rättSvar,3);assert.equal(q('1.873').rättSvar,2);assert.match(q('1.870').alternativ.find(a=>a.ratt).txt,/π är en koefficient/);
});
test('Nivå, verktyg, figurer och tabell stödjer begreppsträningen',()=>{
 const levels={1:0,2:0};for(const id of ids){const t=q(id);levels[t.traningsniva]++;assert.equal(t.omr,'polynom');assert.deepEqual(Array.from(t.kurs),['1b','1c']);assert.equal(t.spel,true);assert.equal(t.självrättning,true);assert.equal(t.miniräknare,true);assert.equal(t.geogebra,false);assert.match(t.s,/facit-svar/);assert.doesNotMatch(t.t+t.s,/[\u0000-\u0008\u000b-\u001f]|<p><\/p>/);}
 assert.deepEqual(levels,{1:3,2:3});assert.match(q('1.868').t,/<table/);for(const id of ['1.869','1.870','1.871','1.873'])assert.equal((q(id).t.match(/<svg /g)||[]).length,1);assert.match(q('1.870').t,/<circle[^>]+r="90"[^>]+fill="none"/);assert.equal(new Set(bank.map(q=>q.id)).size,bank.length);
});
