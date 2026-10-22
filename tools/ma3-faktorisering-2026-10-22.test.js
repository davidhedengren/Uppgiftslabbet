const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('fs'),vm=require('vm'),path=require('path');
const ctx={window:{}};vm.runInNewContext(fs.readFileSync(path.join(__dirname,'../uppgiftermato1.js'),'utf8'),ctx);const bank=ctx.window.BANKMATO1,q=id=>bank.find(q=>q.id===id),ids=Array.from({length:6},(_,i)=>'1.'+(874+i));
test('Areaformer, koefficienter och faktorprodukter stämmer oberoende',()=>{
 for(const x of [-4,-1,0,1,3,5,10]){assert.ok(3*(x+4)===3*x+12);assert.ok(x*(x+5)===x*x+5*x);assert.ok((x-4)*(x+4)===x*x-16);assert.ok((x-3)*(x+5)===x*x+2*x-15);assert.ok((x+3)**2===x*x+6*x+9);assert.ok((x+1)*(x+2)===2*(x+1)+x*(x+1));}
 assert.equal(q('1.874').rättSvar,'3(x+4)');assert.equal(q('1.875').rättSvar,'x(x+5)');assert.equal(q('1.876').rättSvar,'(x-4)(x+4)');assert.equal(q('1.877').rättSvar,5);assert.equal(q('1.879').rättSvar,'(x+1)(x+2)');assert.equal(q('1.878').alternativ.filter(a=>a.ratt).length,1);assert.match(q('1.878').alternativ.find(a=>a.ratt).txt,/\(x\+3\)\^2/);
});
test('Begärd produktform, nivåer, verktyg och figurkontrakt',()=>{
 const levels={1:0,2:0};for(const id of ids){const t=q(id);levels[t.traningsniva]++;assert.equal(t.omr,'faktorisera_polynom');assert.deepEqual(Array.from(t.kurs),['1b','1c']);assert.equal(t.spel,true);assert.equal(t.självrättning,true);assert.equal(t.miniräknare,true);assert.equal(t.geogebra,false);assert.equal(t.spelDelning,undefined);assert.match(t.s,/facit-svar/);assert.doesNotMatch(t.t+t.s,/[\u0000-\u0008\u000b-\u001f]|<p><\/p>/);}
 assert.deepEqual(levels,{1:4,2:2});for(const id of ['1.874','1.875','1.876','1.879'])assert.equal(q(id).svarFormat,'faktoriserat');for(const id of ['1.874','1.875','1.876','1.878'])assert.match(q(id).t,/<svg /);assert.equal(new Set(bank.map(q=>q.id)).size,bank.length);
});
