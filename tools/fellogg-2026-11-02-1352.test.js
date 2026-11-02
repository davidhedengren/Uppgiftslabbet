'use strict';
const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('node:fs'),vm=require('node:vm');
const ctx={window:{}};vm.runInNewContext(fs.readFileSync('uppgifterma1.js','utf8'),ctx);const bank=ctx.window.BANKMA1,q=id=>bank.find(q=>q.id===id);
const source=fs.readFileSync('index.html','utf8'),c={};for(const name of ['altVisas','uppgiftsText','altFacit']){const i=source.indexOf('function '+name+'(');vm.runInNewContext(source.slice(i,source.indexOf('\n}',i)+2),c)}c.altBokstav=i=>String.fromCharCode(65+i);
test('Efterfrågade alternativ syns i lärarunderlag och deras facit',()=>{
 for(const id of ['0.77','0.80','0.86','0.92','0.98','0.322','0.879']){let t=q(id);assert.match(t.t,/Välj ett alternativ/);assert.equal(c.altVisas(t),true,id);assert.equal((c.uppgiftsText(t).match(/class="ul-alt"/g)||[]).length,t.alternativ.length,id);assert.equal(t.alternativ.filter(x=>x.ratt).length,1,id);assert.ok(c.altFacit(t).includes(t.alternativ.find(x=>x.ratt).txt),id);assert.equal(t.miniräknare,false);assert.equal(t.geogebra,false)}
});
test('Rapporterad ifyllnad är entydig: en icke-noll faktor gånger noll är noll',()=>{
 const t=q('0.89');assert.equal(t.rättSvar,0);assert.ok(t.t.includes('square'));assert.ok(-4*0===0);for(const x of [-4,-1,1,4])assert.notEqual(-4*x,0);assert.equal(t.miniräknare,false);assert.equal(t.geogebra,false);
});
test('Alternativens korrekta matematik och den förbättrade förklaringen',()=>{
 const a=-3,values=[a**2,-(a**2),-(a**3),a**3];assert.deepEqual(values,[9,-9,27,-27]);assert.equal(q('0.879').alternativ.findIndex(x=>x.ratt),values.indexOf(Math.max(...values)));
 assert.equal(7-(-3),10);assert.match(q('0.80').alternativ.find(x=>x.ratt).txt,/10/);
 assert.equal(-6+(-4),-10);assert.equal(-4+(-6),-10);assert.match(q('0.77').alternativ[1].kommentar,/vänster/);
 assert.equal(-(4**2),-16);
 assert.match(q('0.98').s,/a&lt;b&lt;0/);assert.doesNotMatch(q('0.98').s,/a<b<0/);
});
