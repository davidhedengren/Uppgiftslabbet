'use strict';
/* Felrapporter 2026-10-27 10:04 (Ma1). Se agent/FELRAPPORTER_2026-10-27_1004.md. */
const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('node:fs'),vm=require('node:vm'),path=require('node:path');
const c={window:{}};vm.runInNewContext(fs.readFileSync(path.join(__dirname,'..','uppgifterma1.js'),'utf8'),c);
const B=JSON.parse(JSON.stringify(Object.values(c.window).find(Array.isArray)));const q=id=>{const t=B.find(x=>x.id===id);assert.ok(t,id);return t;};
const matte=s=>[...String(s||'').matchAll(/\\\(([\s\S]*?)\\\)|\\\[([\s\S]*?)\\\]/g)].map(m=>m[1]??m[2]).join(' ');
test('Inga hakparenteser som grupperingstecken i de åtta uppgifterna (elevrapport 0.282)',()=>{
  for(const id of ['0.265','0.266','0.282','1.1387','1.1390','1.1392','1.1397','1.1399']){const t=q(id);
    for(const f of [t.t,t.s,t.ledtrad])assert.doesNotMatch(matte(f),/(?<!\\)\[|(?<!\\)\]|\\bigl\[/,id);
    assert.doesNotMatch(JSON.stringify(t),/hakparentes/,id);}
  assert.equal(3*(8-2*(5-3)),q('0.282').rättSvar);
});
test('2.410 anger enheterna kronor och timmar',()=>{
  const t=q('2.410');assert.match(t.t,/kr att hyra en släpvagn i \\\(x\\\) timmar/);
  assert.equal(t.alternativ.find(a=>a.ratt).txt,'Kostnaden ökar med 12 kr för varje timme.');assert.ok(!t.alternativ[0].ratt);
  for(const a of t.alternativ)if(!a.ratt)assert.ok(a.kommentar);
});
test('2.254 och 2.109 är delkort där a):s facit inte innehåller b):s svar',()=>{
  const a=q('2.254');assert.equal(a.spelDelning,'deluppgifter');assert.equal(a.spelDelar.length,2);
  const b=a.spelDelar[1];assert.equal(b.svarstyp,'alternativ');assert.equal(b.alternativ.filter(x=>x.ratt).length,1);assert.ok(!b.alternativ[0].ratt);
  assert.match(b.alternativ.find(x=>x.ratt).txt,/k=16.*priset per kilometer.*m=55.*startavgiften/);
  const t=q('2.109');assert.equal(t.spelDelning,'deluppgifter');assert.deepEqual(t.rättSvar,[0,1]);
  assert.doesNotMatch(t.spelDelar[0].s,/=\s*1\b|ska vara/);assert.match(t.spelDelar[1].s,/f\(4\)=7\+3\\cdot\(-2\)=1/);
  assert.equal(7+3*((7-13)/3),1);assert.equal(1+3*((7-13)/3),-5);
});
