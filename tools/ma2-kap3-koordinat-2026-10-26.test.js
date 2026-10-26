'use strict';
/* Ma2 kap 3, etapp 7: avstånd, mittpunkt och koordinatgeometri (lärarbeslut 2026-10-25).
   Rutnätsfigurerna var skalenliga. Dubbletter och nästan identiska texter har fått nya tal, sammanhang eller
   felresonemang, och facit har rubriker. */
const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('node:fs'),vm=require('node:vm'),path=require('node:path');
const c={window:{}};vm.runInNewContext(fs.readFileSync(path.join(__dirname,'..','uppgifterma2.js'),'utf8'),c);
const B=JSON.parse(JSON.stringify(c.window.BANKMA2)),get=id=>{const t=B.find(x=>x.id===id);assert.ok(t,id);return t;};
const text=id=>get(id).t.replace(/<svg[\s\S]*?<\/svg>/g,'').replace(/<[^>]+>/g,' ').replace(/\s+/g,' ').trim();
test('Dubbletterna har nya tal och svar',()=>{
  assert.equal(get('3.342').rättSvar,Math.hypot(7-(-2),9-(-3)));assert.deepEqual(get('3.341').rättSvar,[(-3+7)/2,(8+2)/2]);
  assert.equal(get('3.358').rättSvar,-3+8);assert.equal(get('3.319').rättSvar,(5+3)*(4+1));assert.equal(get('3.362').rättSvar,(6+2)*(8+1)/2);
  assert.notEqual(get('3.342').rättSvar,get('3.264').rättSvar);assert.notDeepEqual(text('3.319'),text('3.288'));
  assert.deepEqual(get('3.2036').alternativ.filter(a=>a.ratt).map(a=>a.txt),['Rätvinklig']);
  const [ab,bc,ac]=[[4,2],[3,6],[1,8]].map(([x,y])=>x*x+y*y);assert.equal(ab+bc,ac);
});
test('Varierade texter med figurer, felresonemang och facit med rubriker',()=>{
  assert.match(text('3.326'),/Elin/);assert.match(text('3.343'),/Hanna/);assert.match(text('3.128'),/fågel/);
  for(const id of ['3.342','3.341','3.358','3.128','3.319','3.362'])assert.match(get(id).t,/<svg/,id);
  for(const id of ['3.342','3.341','3.358','3.326','3.343','3.128','3.319','3.362','3.2036','3.2045']){const s=get(id).s;assert.ok((s.match(/facit-rubrik/g)||[]).length>=(s.match(/<li>/g)||[]).length,id);}
});
