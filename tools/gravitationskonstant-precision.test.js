'use strict';
const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('node:fs'),vm=require('node:vm'),path=require('node:path');
const c={window:{}};vm.runInNewContext(fs.readFileSync(path.join(__dirname,'../uppgifter.js'),'utf8'),c);
const q=id=>c.window.BANK.find(t=>t.id===id);
// Modeller beräknade direkt från frågornas massor, radier och densiteter.
const cases=[['4.346',0,G=>G*50*80/1.5**2*1e9,3],['4.9',0,G=>G*4e24/(5e6)**2,3],['4.9',1,G=>G*4e24/(5e6)**2*70,3],['4.363',0,G=>4*Math.PI*G*3200*240000/3,2],['4.364',0,G=>6.6*(3e6)**2/G,2],['4.367',0,G=>Math.sqrt(G*1.2e24/5)/1000,2],['4.372',0,G=>3*.21/(4*Math.PI*G*220000),2],['4.375',0,G=>4*Math.PI*G*4000*280000/3,2]];
test('Vanliga tabellvärden för G ger godtagbara svar med frågans precision',()=>{
 for(const [id,i,model,sf] of cases){const t=q(id),target=Array.isArray(t.rättSvar)?t.rättSvar[i]:t.rättSvar,tol=Array.isArray(t.tolerans)?t.tolerans[i]:t.tolerans;
  const good=v=>Math.abs(v-target)<=tol+Number.EPSILON*16*Math.max(v,target);
  for(const G of [6.67e-11,6.674e-11]){const value=model(G);assert.ok(good(value),id+' fullt värde');assert.ok(good(Number(value.toPrecision(sf))),id+' avrundat');assert.equal(good(2*value),false,id+' dubbelt');}
  assert.ok(good(model(6.674e-11)),id+' självständigt facit');
 }
 assert.match(q('4.346').t,/tre värdesiffror/);
 for(const part of q('4.9').spelDelar){assert.match(part.t,/tre värdesiffror/);assert.match(part.fraga,/tre värdesiffror/);}
 assert.match(q('4.9').spelDelar[0].s,/Svar: 10,7 /);assert.match(q('4.9').spelDelar[1].s,/Svar: 747 /);
 assert.match(q('4.372').s,/3414/);
});
