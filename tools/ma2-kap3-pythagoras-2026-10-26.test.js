'use strict';
/* Ma2 kap 3, etapp 4: Pythagoras (lärarbeslut 2026-10-25). Figurerna följer måtten: den långa kateten är ritad
   lång. Dubbletter har fått nya tal och sammanhang, och facit har en rubrik per steg. */
const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('node:fs'),vm=require('node:vm'),path=require('node:path');
const c={window:{}};vm.runInNewContext(fs.readFileSync(path.join(__dirname,'..','uppgifterma2.js'),'utf8'),c);
const B=JSON.parse(JSON.stringify(c.window.BANKMA2)),get=id=>{const t=B.find(x=>x.id===id);assert.ok(t,id);return t;};
// Sidförhållanden ur polygonens hörn (rätvinklig triangel): kvoten mellan kateterna i figuren ska stämma med måtten.
const katetkvot=(id)=>{const s=get(id).t.match(/<svg[\s\S]*?<\/svg>/)[0],pts=s.match(/<polygon points="([^"]+)"/)[1].trim().split(/\s+/).map(p=>p.split(',').map(Number));
  const L=[0,1,2].map(i=>Math.hypot(pts[i][0]-pts[(i+1)%3][0],pts[i][1]-pts[(i+1)%3][1])).sort((a,b)=>a-b);return L[0]/L[1];};
test('Figurerna följer måtten',()=>{
  for(const[id,kvot]of Object.entries({'3.142':8/15,'3.310':12/35,'3.333':6/8,'3.624':9/40,'3.625':10/24,'3.353':20/21}))assert.ok(Math.abs(katetkvot(id)-kvot)<0.02,`${id}: ${katetkvot(id).toFixed(3)} ≠ ${kvot.toFixed(3)}`);
  for(const id of ['3.04','3.34','3.145','3.187','3.630','3.632','3.240','3.200'])assert.match(get(id).t,/<svg/,id);
});
test('Dubbletterna har nya tal och svar',()=>{
  const svar={'3.310':35,'3.240':2.5,'3.353':29,'3.302':45,'3.200':2.4};for(const[id,v]of Object.entries(svar))assert.equal(get(id).rättSvar,v,id);
  assert.ok(Math.abs(get('3.632').rättSvar-Math.sqrt(0.64+92.16))<1e-12);assert.notEqual(get('3.632').rättSvar,get('3.2006').rättSvar);
  for(const id of ['3.240','3.200','3.632'])assert.match(get(id).t,/decimal/,id);
  const t=id=>get(id).t.replace(/<svg[\s\S]*?<\/svg>/g,'');assert.notEqual(t('3.240'),t('3.129'));assert.notEqual(t('3.353'),t('3.309'));assert.notEqual(t('3.302'),t('3.241'));
});
test('Facit har rubriker, och 3.145 behåller sina fristående delkort',()=>{
  for(const id of ['3.04','3.34','3.142','3.145','3.187','3.310','3.333','3.624','3.625','3.630','3.632','3.240','3.353','3.302','3.200']){const s=get(id).s;assert.ok((s.match(/facit-rubrik/g)||[]).length>=(s.match(/<li>/g)||[]).length,id);}
  const q=get('3.145');assert.equal(q.spelDelar.length,2);assert.match(q.spelIntro,/<svg/);for(const d of q.spelDelar)assert.match(d.s,/facit-rubrik/);
});
