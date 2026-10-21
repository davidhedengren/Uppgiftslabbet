'use strict';
// Skydd för FP84: Ma2 grafisk lösning (1.675–1.683) och standardavvikelse (4.384–4.395).
const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('fs'),vm=require('vm');
const c={window:{}};vm.runInNewContext(fs.readFileSync(__dirname+'/../uppgifterma2.js','utf8'),c);
const b=Object.values(c.window).find(v=>Array.isArray(v)),q=id=>b.find(x=>x.id===id);
const ratt=id=>Array.from(q(id).alternativ.filter(a=>a.ratt),a=>a.txt);
const mean=a=>a.reduce((s,x)=>s+x,0)/a.length;
const Sx=a=>{const m=mean(a);return Math.sqrt(a.reduce((s,x)=>s+(x-m)**2,0)/(a.length-1));};

test('Grafisk lösning: skärningspunkter och parametrar stämmer',()=>{
 assert.equal(q('1.675').rättSvar,200);assert.equal(150+0.25*200,50+0.75*200);
 assert.deepEqual(Array.from(q('1.676').rättSvar),[4,1]);assert.equal(-4+5,0.5*4-1);
 assert.deepEqual(Array.from(q('1.677').rättSvar),[2.5,4]);assert.equal(2*2.5-1,-2.5+6.5);
 assert.deepEqual(Array.from(q('1.678').rättSvar),[6,8]);assert.equal(20-2*6,14-6);
 assert.equal(q('1.683').rättSvar,1);assert.equal(-3+8,1*3+2);
 assert.match(ratt('1.679')[0],/y = 2x − 2 och y = −0,5x \+ 3/);
 assert.deepEqual(ratt('1.680'),['Ingen lösning']);
 assert.deepEqual(ratt('1.682'),['y = 2x + 1']);
});

test('Standardavvikelse: Sx (n−1) och GeoGebra där data beräknas',()=>{
 const TA=[14,16,15,17,18,16,15,17,16,16],TB=[9,14,20,12,22,18,11,21,17,16];
 assert.deepEqual(Array.from(q('4.390').rättSvar),[Math.round(Sx(TA)*10)/10,Math.round(Sx(TB)*10)/10]);
 const H=[48,52,55,57,58,60,61,62,63,65,70,75],m=mean(H),s=Sx(H);
 assert.equal(q('4.391').rättSvar,H.filter(x=>x>=m-s&&x<=m+s).length);
 const V=[498.2,501.5,503.1,497.4,500.8,495.9,502.6,499.0,504.2,497.3];
 assert.ok(Sx(V)>2.0);assert.match(ratt('4.393')[0],/^Nej/);
 assert.match(ratt('4.392')[0],/Spelare B/);
 assert.equal(q('4.388').rättSvar,0);
 for(const id of ['4.390','4.391','4.392','4.393'])assert.equal(q(id).geogebra,true,id);
 for(let i=384;i<=395;i++){const t=q('4.'+i);assert.equal(t.omr,'standardavvikelse');assert.equal(t.miniräknare,true);
  assert.ok(!/SD\(/.test(JSON.stringify(t)),'4.'+i);}
 for(let i=384;i<=389;i++)assert.ok(q('4.'+i).t.includes('<svg'),'figur 4.'+i);
});

test('Ombyggda upprepningar: varierade typer med kontrollerade svar',()=>{
 const FEL=[5.2,5.6,4.9,5.8,55,5.1,5.4,5.0],RATT=[5.2,5.6,4.9,5.8,5.5,5.1,5.4,5.0];
 assert.deepEqual(Array.from(q('4.235').rättSvar),[Math.round(Sx(FEL)*100)/100,Math.round(Sx(RATT)*100)/100]);
 const MA=[24.3,24.6,24.1,24.5,24.4,24.7],MB=[24.40,24.46,24.43,24.48,24.41,24.45];
 assert.deepEqual(Array.from(q('4.174').rättSvar),[Math.round(Sx(MA)*100)/100,Math.round(Sx(MB)*100)/100]);
 assert.equal(q('4.236').rättSvar,(190-170)/8);
 assert.equal(ratt('4.211').length,3);
 assert.deepEqual(ratt('4.212'),['X']);assert.deepEqual(ratt('4.14'),['24']);assert.deepEqual(ratt('4.65'),['Q']);
 assert.deepEqual(ratt('4.173'),['5, 5, 5, 5']);assert.deepEqual(ratt('4.195'),['27']);
 assert.match(ratt('4.201')[0],/^Bea/);assert.match(ratt('4.114')[0],/Betydligt större/);
 for(const id of ['4.235','4.174'])assert.equal(q(id).geogebra,true,id);
 // Ingen ombyggd uppgift är längre en ren "alla värden ökas/multipliceras"-omvandling.
 for(const id of ['4.102','4.114','4.201','4.211','4.212','4.235','4.236','4.174'])
  assert.doesNotMatch(q(id).t,/Alla värden (ökas|multipliceras)/,id);
});
