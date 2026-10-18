'use strict';
const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('node:fs'),vm=require('node:vm');
const c={window:{}};vm.runInNewContext(fs.readFileSync(__dirname+'/../uppgifterma2.js','utf8'),c);
const bank=JSON.parse(JSON.stringify(c.window.BANKMA2));
const models=[
 ['1.33',[[1,1,1,12],[1,1,0,7],[0,1,1,8]]],
 ['1.65',[[1,1,1,12],[1,-1,1,4],[2,1,-1,7]]],
 ['1.74',[[1,1,1,12],[2,1,1,17],[1,-1,1,8]]],
 ['1.75',[[1,1,1,15],[1,0,1,9],[1,1,0,11]]],
 ['1.78',[[1,1,1,6],[2,-1,1,6],[1,3,-2,-1]]],
 ['1.163',[[1,1,1,10],[1,-1,0,2],[0,-1,1,-1]]],
 ['1.164',[[1,1,1,15],[1,1,0,9],[0,1,1,11]]],
 ['1.166',[[1,1,1,6],[2,-1,1,6],[1,2,-1,1]]],
 ['1.167',[[1,1,1,9],[2,-1,1,8],[1,2,-1,3]]],
 ['1.168',[[1,1,1,9],[1,-1,0,1],[0,1,-1,1]]],
 ['1.268',[[2,1,1,11],[1,2,1,12],[1,1,2,13]]],
 ['1.272',[[1,1,1,15],[2,-1,1,13],[1,2,-1,2]]]
];
test('Systemens tre svar hör till x, y och z och uppfyller alla ekvationer',()=>{
 for(const [id,equations] of models){
  const q=bank.find(q=>q.id===id);assert.deepEqual(q.svarEtiketter,['x','y','z']);assert.equal(q.svarsstruktur,'ordnad');assert.equal(q.svarstyp,'flera_delar');
  assert.equal(q.rättSvar.length,3);assert.deepEqual(q.självrättning,[true,true,true]);
  const values=q.rättSvar.map(v=>{const [a,b=1]=String(v).split('/').map(Number);return a/b;});
  for(const [a,b,c,d] of equations)assert.ok(Math.abs(a*values[0]+b*values[1]+c*values[2]-d)<1e-10,id);
  assert.equal(q.geogebra,false);assert.equal(q.miniräknare,false);
 }
});
test('Namngivna antal matportioner och biljetter får inte byta plats',()=>{
 const a=bank.find(q=>q.id==='1.165'),b=bank.find(q=>q.id==='1.269');
 for(const q of [a,b])assert.equal(q.svarsstruktur,'ordnad');
 const [m,s,p]=a.rättSvar.map(Number);assert.equal(m+s+p,90);assert.equal(55*m+70*s+45*p,5200);assert.equal(s-p,10);
 const [u,v,f]=b.rättSvar.map(Number);assert.equal(u+v+f,120);assert.equal(90*u+150*v+240*f,19500);assert.equal(v-u,10);
});
