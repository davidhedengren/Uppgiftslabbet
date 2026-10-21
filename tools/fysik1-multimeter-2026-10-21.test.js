'use strict';
// Skydd för FP82: nya fy1-uppgifter om multimeter (8.530–8.549).
const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('fs'),vm=require('vm');
const c={window:{}};vm.runInNewContext(fs.readFileSync(__dirname+'/../uppgifter.js','utf8'),c);
vm.runInNewContext(fs.readFileSync(__dirname+'/../struktur.js','utf8'),c);
const b=c.window.BANK,q=id=>b.find(x=>x.id===id);
const ids=Array.from({length:20},(_,i)=>'8.'+(530+i));
const ratta=id=>Array.from(q(id).alternativ.filter(a=>a.ratt),a=>a.txt);

test('Området Mäta med multimeter finns i kap 8 efter Spänning och resistans',()=>{
 const keys=Object.keys(c.window.OMR['8']);
 assert.equal(c.window.OMR['8'].multimeter,'Mäta med multimeter');
 assert.equal(keys.indexOf('multimeter'),keys.indexOf('kretsar')+1);
});

test('Tjugo självständiga flervalskort med figur och kommentar till varje alternativ',()=>{
 for(const id of ids){
  const t=q(id);
  assert.equal(b.filter(x=>x.id===id).length,1,id);
  assert.equal(t.omr,'multimeter');assert.equal(t.svarstyp,'alternativ');
  assert.ok(t.t.includes('<svg'),id);assert.equal(t.spel,true);assert.equal(t.självrättning,true);
  assert.ok(t.alternativ.length>=3);assert.ok(t.alternativ.some(a=>a.ratt));
  assert.ok(t.alternativ.every(a=>a.kommentar),id);
  assert.ok(t.traningsniva>=1&&t.traningsniva<=4);
 }
 const fam=new Map();ids.forEach(id=>fam.set(q(id).familj,(fam.get(q(id).familj)||0)+1));
 assert.equal(fam.size,3);for(const n of fam.values())assert.ok(n>=6);
});

test('Uttag: COM alltid, mA-uttaget högst 400 mA, 10A för stora strömmar',()=>{
 assert.deepEqual(ratta('8.530').sort(),['COM','µA mA V Ω Hz'].sort());
 assert.deepEqual(ratta('8.531'),['COM']);
 assert.deepEqual(ratta('8.532').sort(),['COM','µA mA V Ω Hz'].sort()); // 0,15 A = 150 mA < 400 mA
 assert.deepEqual(ratta('8.533').sort(),['10A','COM']);                  // 2 A > 400 mA
 assert.match(ratta('8.535')[0],/10A och vredet på 10 A/);
});

test('Mätområden: minsta område som räcker, OL betyder för litet område',()=>{
 assert.deepEqual(ratta('8.536'),['V']);assert.deepEqual(ratta('8.537'),['Ω']);
 assert.deepEqual(ratta('8.538'),['400 mA']);   // 50 mA > 4 mA
 assert.deepEqual(ratta('8.539'),['4000 µA']);  // 1500 µA < 4000 µA
 assert.match(ratta('8.540')[0],/400 mA/);
 assert.match(ratta('8.541')[0],/Flytta sladden från 10A till µA mA V Ω Hz och vrid vredet till V/);
});

test('Inkoppling: amperemeter i serie, voltmeter parallellt',()=>{
 assert.match(ratta('8.542')[0],/Bryt kretsen/);
 assert.deepEqual(ratta('8.543'),['Mellan A och B.']);
 assert.deepEqual(ratta('8.544'),['B och C']);
 assert.deepEqual(ratta('8.545'),['Vid R']);
 assert.match(ratta('8.546')[0],/säkring/);
 assert.match(ratta('8.547')[0],/Lampan lyser inte/);
 assert.match(ratta('8.548')[0],/10A.*10 A.*vid Q/);
 assert.match(ratta('8.549')[0],/Koppla bort batteriet/);
});

test('Vredet avslöjar inte svaret i uttags-, läges- och växelspänningsfrågorna',()=>{
 // Visaren pekar mot OFF (200°) när vredets läge annars skulle ge en ledtråd.
 const OFF='x2="118.7" y2="267.0" stroke="#d9dde3"';
 for(const id of ['8.531','8.532','8.533','8.535','8.536','8.537','8.538','8.539'])assert.ok(q(id).t.includes(OFF),id);
 assert.ok(!q('8.540').t.includes(OFF)); // OL-uppgiften visar 4000 µA
});

test('Förslag B (8.550–8.565) och mindre multimeterfigurer',()=>{
 const nya=Array.from({length:16},(_,i)=>'8.'+(550+i));
 for(const id of nya){
  const t=q(id);assert.equal(b.filter(x=>x.id===id).length,1,id);
  assert.equal(t.omr,'multimeter');assert.equal(t.svarstyp,'alternativ');assert.ok(t.t.includes('<svg'),id);
  assert.equal(t.alternativ.filter(a=>a.ratt).length,1,id);
  assert.ok(!/µA mA \/ V/.test(JSON.stringify(t)),id);
  for(const m of t.t.matchAll(/max-width:(\d+)px/g))assert.ok(Number(m[1])<=440,id);
 }
 assert.deepEqual(ratta('8.550'),['B och C']);assert.deepEqual(ratta('8.551'),['A och C']);
 assert.deepEqual(ratta('8.558'),['COM och 10A']);           // 0,65 A > 400 mA
 assert.deepEqual(ratta('8.560'),['4000 µA']);               // 250 µA
 assert.deepEqual(ratta('8.561'),['0 V']);
 assert.match(ratta('8.564')[0],/400 mA; i serie/);           // 6 V / 300 Ω = 20 mA
 assert.equal(6/300,0.02);
 for(let i=530;i<=541;i++)assert.ok(q('8.'+i).t.includes('max-width:240px'),'8.'+i);
});

test('Förslag B:s regler: inga DC/AC-ord och sladdfärg avgör inte svaret',()=>{
 const ord=/\b(röd\w*|svart\w*|DC|AC|likspänning|likström|växel\w*)\b/i;
 for(const t of b.filter(x=>x.omr==='multimeter')){
  const utanFigur=JSON.stringify(t).replace(/<svg[\s\S]*?<\/svg>/g,'');
  assert.ok(!ord.test(utanFigur),t.id);
  assert.ok(!JSON.stringify(t).includes('DC/AC'),t.id);
 }
});
