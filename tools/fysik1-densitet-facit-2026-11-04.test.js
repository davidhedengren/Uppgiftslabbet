'use strict';
const {test}=require('node:test');
const assert=require('node:assert/strict');
const fs=require('node:fs'),vm=require('node:vm'),path=require('node:path');
const c={window:{}};
vm.runInNewContext(fs.readFileSync(path.join(__dirname,'../uppgifter.js'),'utf8'),c);
const tasks=c.window.BANK.filter(q=>q.omr==='densitet');
const q=id=>tasks.find(q=>q.id===id);

test('Alla 178 densitetsfacit och 53 delkort har steg, rubriker och slutsvar',()=>{
 assert.equal(tasks.length,178);let cards=0;
 for(const t of tasks){
  assert.equal(t.miniräknare,true,t.id);
  for(const [id,s] of [[t.id,t.s],...(t.spelDelar||[]).map(d=>[t.id+d.etikett,d.s])]){
   assert.match(s,/<ol class="facit-steglista" role="list">/,id);
   assert.match(s,/<p class="facit-rubrik">/,id);
   assert.match(s,/<p class="facit-svar"><strong>Svar:<\/strong>/,id);
   assert.doesNotMatch(s,/None|undefined|facit-forklaring/,id);
  }
  // The solution must have exactly the question's parts, even when no gym cards exist.
  const text=t.t.replace(/<svg[\s\S]*?<\/svg>/g,'');
  const parts=(text.match(/<li>/g)||[]).length||(text.match(/<p>\s*[a-z]\)/g)||[]).length;
  if(parts>1)assert.equal((t.s.match(/class="facit-del"/g)||[]).length,parts,t.id);
  for(const d of t.spelDelar||[]){assert.notEqual(d.miniräknare,false,t.id+d.etikett);cards++;}
 }
 assert.equal(cards,53);
});

test('Grafkonstruktion tillåter digitala verktyg och visar rätt diagramdata',()=>{
 for(const id of ['2.80','2.92','2.93','2.94','2.95','2.99','2.100','2.101','2.102','2.103','2.104','2.105','2.106','2.203']){
  assert.equal(q(id).geogebra,true,id);
  for(const d of q(id).spelDelar||[])assert.notEqual(d.geogebra,false,id+d.etikett);
 }
 assert.equal((q('2.80').s.match(/<svg/g)||[]).length,2);
 assert.match(q('2.80').s,/Massa \(g\)/);assert.match(q('2.80').s,/Volym \(cm³\)/);
 assert.match(q('2.99').s,/7 cm³, 59 g/); // Visible coordinates, not extrapolation beyond the graph.
 const m=[19.3*Math.PI*30,(19.3*30+2.70*40)*Math.PI,(19.3*30+2.70*40+10.5*30)*Math.PI];
 assert.deepEqual(m.map(Math.round),[1819,2158,3148]);
 for(const mass of m.map(Math.round))assert.ok(q('2.203').s.includes(String(mass)));
 assert.match(q('2.203').s,/<svg[^>]*style="max-width:100%/);
});

test('Flytgräns, blandningsantagande och mätfel förklaras utan fel slutsats',()=>{
 assert.ok(q('2.90').t.indexOf('volymer kan adderas')<q('2.90').t.indexOf('<ol'));
 assert.equal((q('2.90').s.match(/class="facit-del"/g)||[]).length,2);
 assert.match(q('2.91').s,/\\gt/);assert.match(q('2.91').s,/neutralt/);
 for(const id of ['2.102','2.174'])assert.match(q(id).s,/bubbl/i,id);
 // A bubble raises apparent V and lowers rho; it cannot explain a point above the m(V) line.
 assert.ok(100/(20+2)<100/20);
 assert.match(q('2.173').s,/700/);assert.match(q('2.173').s,/50/);
});

test('Oavrundade mellanled i hålkub, sammansatt kula och stålfat',()=>{
 const rho=750/(125-5*Math.PI),mass=rho*125;
 assert.equal(rho.toFixed(5),'6.86235');assert.equal(mass.toFixed(3),'857.794');
 assert.match(q('2.180').s,/857\{,\}794/);
 const solid=7.8*4*Math.PI*3.2**3/3,core=(solid-843.1)/(7.8-2.7);
 assert.equal(solid.toFixed(3),'1070.615');assert.equal(core.toFixed(4),'44.6107');
 assert.equal(Math.cbrt(core*3/(4*Math.PI)).toFixed(2),'2.20');
 assert.match(q('2.275').s,/1070\{,\}615/);
 const exact=7800*Math.PI*(.287**2*.854-.285**2*.85);
 const thin=7800*.002*(2*Math.PI*.285*.85+2*Math.PI*.285**2);
 assert.equal(exact.toFixed(1),'31.9');assert.equal(thin.toFixed(1),'31.7');
 assert.match(q('2.182').s,/31,9 respektive 31,7/);
 assert.equal((10*Math.cbrt(1-1000/7850)).toFixed(1),'9.6');
 assert.match(q('2.290').s,/9\{,\}6/);
});
