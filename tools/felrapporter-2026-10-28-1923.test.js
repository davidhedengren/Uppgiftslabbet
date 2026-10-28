const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('node:fs'),vm=require('node:vm');
function bank(file){const c={window:{}};vm.runInNewContext(fs.readFileSync(file,'utf8'),c);return Object.values(c.window).find(Array.isArray);}
test('Procentresultat kontrolleras före den manuella motiveringen',()=>{
 const a=bank('uppgifterma1.js');
 for(const [id,value] of [['3.06',-1.44],['3.58',-1],['3.190',55]]){
  const q=a.find(x=>x.id===id);assert.equal(q.rättSvar,value,id);
  assert.equal(q.självrättning,true,id);assert.equal(q.manuellKomplettering,true,id);
  assert.equal(q.svarEnhet,'%',id);assert.equal(q.miniräknare,true,id);assert.equal(q.geogebra,false,id);
 }
 assert.ok(Math.abs((1.12*.88-1)*100+1.44)<1e-10);
 assert.ok(Math.abs((1.1*.9-1)*100+1)<1e-10);
 assert.ok(Math.abs((1-.75*.6)*100-55)<1e-10);
});
test('Figurerna avslöjar inte resultatet och facit visar de nödvändiga stegen',()=>{
 const a=bank('uppgifterma2.js'),g=a.find(x=>x.id==='3.544'),q=a.find(x=>x.id==='3.669');
 assert.equal(g.rättSvar,12.5);assert.ok(!g.t.includes('M192.600 68.200 l8.800 6.600 l6.600 -8.800'));
 assert.ok(g.t.includes('M199.200 154.000 l11.000 0.000 l-0.000 11.000'));
 assert.match(g.s,/Bestäm vinkeln vid C/);assert.match(g.s,/Använd likformighet/);assert.match(g.s,/Bestäm radien/);
 for(const label of ['I','II','III','IV'])assert.ok(!new RegExp('>'+label+'</text>').test(q.t),label);
 assert.equal(q.alternativ.filter(x=>x.ratt).length,1);
});
