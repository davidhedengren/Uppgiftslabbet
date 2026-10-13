'use strict';
const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('node:fs'),vm=require('node:vm'),path=require('node:path');
const c={window:{}};vm.runInNewContext(fs.readFileSync(path.join(__dirname,'../uppgiftermatf1.js'),'utf8'),c);const qs=new Map(c.window.BANKMATF1.map(q=>[q.id,q]));
const factorial=n=>n<2?1:n*factorial(n-1);
test('Sex personer ger 720 olika köordningar genom direkt uppräkning',()=>{
 const permutations=[];const visit=(used,row)=>{if(row.length===6){permutations.push(row.join(''));return;}for(let n=1;n<=6;n++)if(!used.has(n)){used.add(n);visit(used,row.concat(n));used.delete(n);}};visit(new Set(),[]);
 assert.equal(new Set(permutations).size,720);assert.equal(qs.get('1.136').rättSvar,permutations.length);
});
test('Alla fem jämförelseuppgifter har korrekta heltalsfacit och samma avgränsade rättningskontrakt',()=>{
 for(const [id,expected]of [['1.136',factorial(6)],['1.509',factorial(5)],['1.510',factorial(6)],['1.511',factorial(7)],['1.70',factorial(7)],['1.72',2*factorial(8)]]){
  const q=qs.get(id);assert.ok(q,id);assert.equal(q.rättSvar,expected);assert.equal(q.svarFormat,'antal_satt');assert.equal(q.svarEnhet,undefined);assert.equal(q.tolerans,0);assert.equal(q.självrättning,true);
 }
});
test('Rapportuppgiftens lösning förklarar antalet val utan ledning i frågan',()=>{
 const q=qs.get('1.136');assert.match(q.s,/6\\cdot5\\cdot4\\cdot3\\cdot2\\cdot1=6!=720/);assert.match(q.s,/5 personer kvar/);assert.doesNotMatch(q.t,/720|6!/);assert.equal(q.niva,'E');assert.equal(q.traningsniva,1);assert.equal(q.miniräknare,false);
});
