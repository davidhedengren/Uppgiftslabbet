'use strict';
// Felrapporter 2026-11-23 18:07 (agent/FELRAPPORTER_2026-11-23_1807.md): Fy1 3.63 cyklistfigur, zink 7,13 g/cm³.
const {test}=require('node:test');
const a=require('node:assert/strict');
const fs=require('node:fs'),vm=require('node:vm'),path=require('node:path');
const c={window:{}};vm.runInNewContext(fs.readFileSync(path.join(__dirname,'../uppgifter.js'),'utf8'),c);
const B=c.window.BANK;
const q=id=>B.find(u=>u.id===id);

test('3.63: figuren visar en cyklist (huvud, hjälm, ben) på cykeln',()=>{
 const t=q('3.63').t;
 a.equal((t.match(/<svg/g)||[]).length,1);
 a.match(t,/viewBox="0 0 460 200"/);
 a.ok((t.match(/<circle /g)||[]).length>=5,'två hjul, två nav och ett huvud');
 a.match(t,/stoppsträcka \?/);
});

test('Zink har densiteten 7,13 g/cm³ i hela Fy1-banken',()=>{
 for(const u of B){
  const s=JSON.stringify(u);
  if(/[Zz]ink/.test(s))a.doesNotMatch(s,/7,14|7\{,\}14/,u.id);
 }
 a.ok(Math.abs(q('2.18').rättSvar-300/(200/8.96+100/7.13))<1e-12);
 a.equal(q('2.156').rättSvar,4634.5);a.equal(q('2.156').tolerans,0.5);
 a.equal(q('2.200').rättSvar,36.1);
 for(const id of ['2.18','2.40','2.156','2.200'])a.match(JSON.stringify(q(id)),/7,13/,id);
});
