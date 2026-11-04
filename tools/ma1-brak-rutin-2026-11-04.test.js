'use strict';
const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('node:fs'),vm=require('node:vm'),path=require('node:path'),cp=require('node:child_process');
const root=path.join(__dirname,'..'),c={window:{}};
vm.runInNewContext(fs.readFileSync(path.join(root,'uppgifterma1.js'),'utf8'),c);
const bank=JSON.parse(JSON.stringify(c.window.BANKMA1)),ids=Array.from({length:56},(_,i)=>'1.'+(1567+i)),qs=ids.map(id=>bank.find(q=>q.id===id));
test('56 nya kort: progression, spår, verktyg och rättningsformat',()=>{
 assert.equal(new Set(bank.map(q=>q.id)).size,bank.length);
 const levels={};for(const q of qs){assert.ok(q);levels[q.traningsniva]=(levels[q.traningsniva]||0)+1;
  assert.equal(q.omr,'ekv_brak');assert.deepEqual(q.kurs,['1a','1b','1c']);assert.equal(q.spel,true);assert.equal(q.självrättning,true);
  assert.equal(q.miniräknare,false);assert.equal(q.geogebra,false);assert.equal(q.spelDelning,undefined);
  assert.ok(['förenklat_polynom','numeriskt'].includes(q.svarFormat));
  if(q.traningsniva>=4)assert.match(q.t,/\\frac\{[^}]*\}\{[^}]*x/);
  if(q.traningsniva<=2){assert.doesNotMatch(q.t,/[()]/);assert.doesNotMatch(q.t,/\\frac\{[^}]*[+−-][^}]*\}/);}
 }
 assert.deepEqual(levels,{1:8,2:30,3:7,4:8,5:3});
 assert.equal(qs.filter(q=>q.familj==='Bråk i uttryck').length,28);
 assert.equal(qs.filter(q=>q.familj==='Ekvationer med nämnare').length,28);
});
test('Varje facit har specifika rubriker, regel, steglista och svarsrad',()=>{
 for(const q of [...qs,...['1.1364','1.270'].map(id=>bank.find(q=>q.id===id))]){
  assert.match(q.s,/<ol class="facit-steglista" role="list">/);assert.match(q.s,/class="facit-svar"/);
  const steps=[...q.s.matchAll(/<li>([\s\S]*?)<\/li>/g)];assert.ok(steps.length);
  for(const [,step] of steps){assert.match(step,/<p class="facit-rubrik">/);assert.match(step,/class="facit-matte"/)}
  assert.match(q.s,/<p class="facit-rubrik">[^<]*\\\(/);
  assert.doesNotMatch(q.s,/>Steg \d|>Förenkla<|None|null/);assert.ok(q.ledtrad.length>30);
 }
});
test('Sympy verifierar identiteter och samtliga lösningar exakt, utan att skriva bankfilen',()=>{
 const result=cp.spawnSync('python3',['-c',"import runpy; m=runpy.run_path('tools/ma1-brak-rutin-2026-11-04.py'); assert len(m['build']())==56"],{cwd:root,encoding:'utf8'});
 assert.equal(result.status,0,result.stderr);
});
