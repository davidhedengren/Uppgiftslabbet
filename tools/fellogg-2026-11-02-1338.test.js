'use strict';
const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('node:fs'),vm=require('node:vm');
const c={window:{}};vm.runInNewContext(fs.readFileSync('uppgiftermato1.js','utf8'),c);const bank=c.window.BANKMATO1,q=id=>bank.find(x=>x.id===id);
test('Huvuduppgift och separata hastighetsdelar har rätt mål för sina olika givna data',()=>{
 const t=q('3.132');assert.deepEqual(Array.from(t.rättSvar),[1.3333333333,4]);assert.deepEqual(Array.from(t.spelDelar,x=>x.rättSvar),[5,13]);
 const F=t=>t*t-4*t;assert.equal(F(5)-F(0),5);assert.equal(-(F(2)-F(0))+(F(5)-F(2)),13);
 assert.equal(t.miniräknare,true);assert.equal(t.geogebra,false);assert.ok(t.spelDelar.every(d=>d.miniräknare!==false&&d.geogebra!==true));
});
test('Tolkning och jämförelsefacit finns för varje manuell del utan kommande svar',()=>{
 const t=q('3.731');assert.match(t.delfacit[1],/sträcka stenen faller/);assert.match(t.delfacit[1],/15 m/);assert.equal(t.rättSvar[0],15);
 for(const id of ['2.85','2.90','2.95','2.100','2.105','2.110','2.115','2.120'])assert.ok(q(id).delfacit[1].includes('visade området'),id);
 for(const id of ['3.359','3.365','3.369']){assert.match(q(id).delfacit[1],/derivat/i,id);assert.match(q(id).delfacit[2],/minimipunkt/i,id);}
 assert.doesNotMatch(q('3.369').delfacit[1],/minimipunkt|extrempunkt/i);
});
test('Sammanlagda kostnader får korrekt enhet och full precision',()=>{
 const a=q('3.500'),b=q('3.486');assert.match(a.t,/Svara i tusen kronor/);assert.equal(a.svarEnhet,'tkr');assert.ok(Math.abs(a.rättSvar-176/3)<1e-12);assert.equal(a.tolerans,null);
 assert.match(b.t,/Svara i miljoner kronor/);assert.equal(b.svarEnhet,'Mkr');assert.ok(Math.abs(b.rättSvar-30*(1.03**8-1)/Math.log(1.03))<1e-10);assert.equal(b.tolerans,null);
 for(const t of [a,b]){assert.equal(t.miniräknare,true);assert.equal(t.geogebra,false);assert.match(t.s,/facit-svar/);}
});
