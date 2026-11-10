'use strict';
/* Fel som hittades när Ma4-facit skrevs om med förklarande rubriker (agent/FACIT_RUBRIKER_2026-10-27.md, Ma4-tabellen). */
const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('node:fs'),vm=require('node:vm'),path=require('node:path');
const c={window:{}};vm.runInNewContext(fs.readFileSync(path.join(__dirname,'..','uppgiftermato2.js'),'utf8'),c);
const B=c.window.BANKMATO2,q=id=>{const x=B.find(x=>x.id===id);assert.ok(x,id);return x;};
const rad=x=>x*Math.PI/180;

test('1.192: rättSvar hör till frågan sin 2x = 0, inte till tan x = √3',()=>{
  const x=q('1.192');assert.match(x.t,/\\sin 2x=0/);
  assert.deepEqual(Array.from(x.rättSvar,Number),[0,90,180,270]);
  for(const v of x.rättSvar.map(Number))assert.ok(Math.abs(Math.sin(rad(2*v)))<1e-12);
  assert.equal(x.tolerans.length,4);assert.equal(x.svarFormat.length,4);
  assert.doesNotMatch(x.ledtrad,/Tangens/);
});

test('1.199: intervallet är 0 ≤ x < 2π eftersom svaren är i radianer',()=>{
  const x=q('1.199');assert.match(x.t,/2\\pi/);assert.doesNotMatch(x.t,/360\^\\circ/);
  for(const v of x.rättSvar)assert.ok(Math.abs(3*Math.sin(v)-Math.cos(v))<0.002&&v>=0&&v<2*Math.PI);
});
