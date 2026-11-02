const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('fs'),vm=require('vm'),path=require('path');
const c={window:{}};vm.runInNewContext(fs.readFileSync(path.join(__dirname,'../uppgiftermato2.js'),'utf8'),c);const bank=JSON.parse(JSON.stringify(c.window.BANKMATO2));
test('Alla aktuella delfacit visar formel, mellanled och svar utan främmande malltext',()=>{
 for(const id of ['1.20','1.38','1.41','1.145']){const q=bank.find(q=>q.id===id);assert.ok(q,id);assert.doesNotMatch(q.s,/periodiciteten|olikheter|ekvivalenskedja/i,id);
  for(const d of q.spelDelar){assert.match(d.s,/facit-rubrik/,id+d.etikett);assert.match(d.s,/begin\{aligned\}/,id+d.etikett);assert.match(d.s,/Svar:/,id+d.etikett);assert.doesNotMatch(d.s,/periodiciteten|olikheter|ekvivalenskedja/i,id+d.etikett);}}
});
test('Mellanledens exakta värden och tecken stämmer',()=>{
 const r=Math.sqrt,rad=x=>x*Math.PI/180,eps=1e-12;
 assert.ok(Math.abs(Math.sin(rad(75))-(r(6)+r(2))/4)<eps);assert.ok(Math.abs(Math.cos(rad(75))-(r(6)-r(2))/4)<eps);
 assert.ok(Math.abs(Math.sin(rad(15))-(r(6)-r(2))/4)<eps);assert.ok(Math.abs(Math.cos(rad(15))-(r(6)+r(2))/4)<eps);
 assert.ok(Math.abs(Math.cos(rad(105))-(r(2)-r(6))/4)<eps);
 for(const x of [-2,-.1,.9,2.7]){
  assert.ok(Math.abs(Math.sin(x+rad(30))-(r(3)/2*Math.sin(x)+.5*Math.cos(x)))<eps);
  assert.ok(Math.abs(Math.sin(x-rad(45))-(r(2)/2*Math.sin(x)-r(2)/2*Math.cos(x)))<eps);
  assert.ok(Math.abs(Math.cos(x+rad(60))-(.5*Math.cos(x)-r(3)/2*Math.sin(x)))<eps);
  assert.ok(Math.abs(Math.cos(x-rad(30))-(r(3)/2*Math.cos(x)+.5*Math.sin(x)))<eps);
 }
});
