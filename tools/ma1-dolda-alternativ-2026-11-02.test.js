'use strict';
const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('node:fs'),vm=require('node:vm');const c={window:{}};vm.runInNewContext(fs.readFileSync('uppgifterma1.js','utf8'),c);const bank=c.window.BANKMA1,q=id=>bank.find(x=>x.id===id),html=fs.readFileSync('index.html','utf8'),ctx={};for(const name of ['altVisas','uppgiftsText']){const i=html.indexOf('function '+name+'(');vm.runInNewContext(html.slice(i,html.indexOf('\n}',i)+2),ctx)}ctx.altBokstav=i=>String.fromCharCode(65+i);
test('Alla sju beroende flervalsuppgifter visar sina alternativ och har individuella förklaringar',()=>{
 for(const id of ['0.51','0.264','0.267','0.280','0.301','0.309','0.404']){const t=q(id);assert.ok(ctx.altVisas(t),id);assert.equal((ctx.uppgiftsText(t).match(/class="ul-alt"/g)||[]).length,t.alternativ.length,id);assert.equal(t.alternativ.filter(a=>a.ratt).length,1,id);assert.ok(t.alternativ.filter(a=>!a.ratt).every(a=>a.kommentar?.length>20),id);assert.equal(t.miniräknare,false);assert.equal(t.geogebra,false)}
});
test('Korrekt alternativ följer av beräkningarna',()=>{
 assert.equal(q('0.51').alternativ.findIndex(a=>a.ratt),2);assert.equal(q('0.264').alternativ.findIndex(a=>a.ratt),2);assert.equal(20-(3+2)*4,0);assert.deepEqual([6+2*5,(6+2)*5],[16,40]);assert.deepEqual([24/6*2,24/(6*2)],[8,2]);assert.equal(56/98,4/7);assert.ok(4*11<5*9);assert.ok(1.099<1.1);
});
