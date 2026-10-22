const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('fs'),vm=require('vm'),path=require('path');
const ctx={window:{}};vm.runInNewContext(fs.readFileSync(path.join(__dirname,'../uppgiftermato1.js'),'utf8'),ctx);const bank=ctx.window.BANKMATO1,q=id=>bank.find(q=>q.id===id),ids=Array.from({length:8},(_,i)=>'1.'+(880+i));
test('Rationella samband och förbjudna värden räknas oberoende',()=>{
 for(const x of [0.5,1,2,3,7,12]){assert.ok(Math.abs(x*12/x-12)<1e-12);assert.equal(6*x/(2*x),3);assert.ok(Math.abs((x+4)/x/4-(x+4)/(4*x))<1e-12);assert.ok(Math.abs((x+3)/5*10/(x+3)-2)<1e-12);assert.ok(Math.abs((6/x)/(2/x**2)-3*x)<1e-12);assert.ok(Math.abs((x*8/x)/(x*3/x)-8/3)<1e-12);}
 assert.equal(q('1.880').rättSvar,12);assert.equal(q('1.882').rättSvar,3);assert.equal(q('1.884').rättSvar,2);assert.equal(q('1.886').rättSvar,'3x');assert.equal(q('1.887').rättSvar,'8/3');
 assert.match(q('1.881').alternativ.find(a=>a.ratt).txt,/frac\{3\}\{x\+2\}/);assert.match(q('1.883').alternativ.find(a=>a.ratt).txt,/4x/);
 for(const x of [-2,1,0,3]){const allowed=x+2!==0&&(x-3)/(x+2)!==0;const choice=q('1.885').alternativ.find(a=>a.txt===`\\(x=${x}\\)`);assert.equal(choice.ratt,!allowed);}
});
test('Nivå, självbärande kort, svarsenheter och bilder',()=>{
 const levels={1:0,2:0};for(const id of ids){const t=q(id);levels[t.traningsniva]++;assert.equal(t.kap,1);assert.equal(t.omr,'rakna_rationella');assert.deepEqual(Array.from(t.kurs),['1b','1c']);assert.equal(t.spel,true);assert.equal(t.självrättning,true);assert.equal(t.miniräknare,true);assert.equal(t.geogebra,false);assert.equal(t.spelDelning,undefined);assert.match(t.s,/facit-svar/);assert.doesNotMatch(t.t+t.s,/[\u0000-\u0008\u000b-\u001f]|<p><\/p>/);}
 assert.deepEqual(levels,{1:5,2:3});assert.equal(q('1.880').svarEnhet,'cm²');assert.equal(q('1.882').svarEnhet,'min');assert.equal(q('1.886').svarFormat,'förenklat_polynom');assert.match(q('1.887').t,/exakt/);
 for(const id of ['1.880','1.882','1.883','1.887'])assert.match(q(id).t,/<svg /);assert.equal(new Set(bank.map(q=>q.id)).size,bank.length);
});
