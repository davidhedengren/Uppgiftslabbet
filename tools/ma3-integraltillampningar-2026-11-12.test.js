'use strict';
// Rättelser i Ma3 integral_tillampningar som hittades när facit skrevs om (FACIT_RUBRIKER_2026-10-27).
const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('node:fs'),vm=require('node:vm');
const c={window:{}};vm.runInNewContext(fs.readFileSync(__dirname+'/../uppgiftermato1.js','utf8'),c);
const q=id=>c.window.BANKMATO1.find(x=>x.id===id);

test('3.332: total sträcka för v(t)=3t²−6t på [0, 3] är 4 + 4 = 8 m',()=>{
 const F=t=>t**3-3*t**2;
 const s=Math.abs(F(2)-F(0))+Math.abs(F(3)-F(2));
 assert.equal(s,8);assert.equal(q('3.332').rättSvar,8);
 assert.match(q('3.332').s,/Svar:<\/strong> 8 m/);
});

test('3.24: enheten ml ligger i svarEnhet, inte i uttrycket',()=>{
 const t=q('3.24');assert.equal(t.rättSvar,'50-(50)/(e)');assert.equal(t.svarEnhet,'ml');
 // ∫0^10 5e^(−t/10) dt = 50 − 50/e
 let s=0;const n=100000;for(let i=0;i<n;i++){const u=(i+.5)*10/n;s+=5*Math.exp(-u/10)*10/n;}
 assert.ok(Math.abs(s-(50-50/Math.E))<1e-6);
});

test('Graf utan siffror på hastighetsaxeln: värdena står i frågan',()=>{
 assert.match(q('3.248').t,/högsta hastigheten är 6 m\/s/);
 assert.match(q('3.260').t,/2 vid start, 5 vid \\\(t=3\\\) och 2 vid \\\(t=6\\\)/);
 assert.equal(2*6/2+3*6+2*6/2,30);assert.equal(2*(2+5)/2*3/6,3.5);
});
