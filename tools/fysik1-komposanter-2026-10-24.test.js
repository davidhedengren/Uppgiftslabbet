'use strict';
/* Fy1 2026-10-24: mängdträning i komposanter (3.620–3.689) – grafiskt, med trigonometri, storlek/riktning ur komposanter och addition.
   Facit räknas om i fysik1-kapitel3.test.js; här kontrolleras omfång, variation och format. */
const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('node:fs'),vm=require('node:vm'),path=require('node:path');
const c={window:{}};vm.runInNewContext(fs.readFileSync(path.join(__dirname,'..','uppgifter.js'),'utf8'),c);
const B=c.window.BANK;const get=id=>{const t=B.find(x=>x.id===id);assert.ok(t,id);return t;};
const NYA=Array.from({length:113},(_,i)=>`3.${620+i}`);

test('113 komposantkort (två omgångar) i vektorer med varierade delmoment',()=>{
  for(const id of NYA){const t=get(id);assert.equal(t.omr,'vektorer',id);assert.equal(t.kap,3,id);assert.match(t.poang,/^\(\d\/\d\/\d\)$/,id);assert.equal(t.miniräknare,true,id);}
  const per={};for(const id of NYA){const k=get(id).familjNyckel;per[k]=(per[k]||0)+1;}
  assert.ok(per['vektorer__komposanter_utan_trigonometri']>=26,JSON.stringify(per));assert.ok(per['vektorer__komposanter_med_trigonometri']>=60,JSON.stringify(per));assert.ok(per['vektorer__addera']>=18,JSON.stringify(per));
  assert.ok(NYA.filter(id=>get(id).traningsniva===1).length>=25);
  // trigonometrikort är markerade
  for(const id of NYA){const t=get(id);if(t.familjNyckel==='vektorer__komposanter_med_trigonometri')assert.equal(t.trigonometri,true,id);}
  // frågor med decimalsvar anger precision i parentes
  for(const id of NYA){const t=get(id);const tol=[].concat(t.tolerans);if(tol.some(x=>x===0.05)&&[].concat(t.rättSvar).some(v=>!Number.isInteger(v)))assert.ok(/med en decimal\.\)/.test(t.t)||t.svarVardesiffror!=null,id);}
});

test('Rättelser: draksnöre och ledtråd i 3.285',()=>{
  assert.doesNotMatch(JSON.stringify(NYA.map(get)),/drakskap/);
  assert.match(get('3.285').ledtrad,/kateterna 5 och 7/);
});
