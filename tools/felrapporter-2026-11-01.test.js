'use strict';
const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('node:fs'),vm=require('node:vm'),path=require('node:path');
function bank(file,key){const c={window:{}};vm.runInNewContext(fs.readFileSync(path.join(__dirname,'..',file),'utf8'),c);return c.window[key];}
const ma1=bank('uppgifterma1.js','BANKMA1'),ma2=bank('uppgifterma2.js','BANKMA2'),ma3=bank('uppgiftermato1.js','BANKMATO1'),ma4=bank('uppgiftermato2.js','BANKMATO2');
const q=(b,id)=>{const x=b.find(x=>x.id===id);assert.ok(x,id);return x};
test('Definitionsmängd är mängden tillåtna värden och korten har egna lösningar',()=>{
 for(const [id,n] of [['1.93',2],['1.98',3]]){
  const t=q(ma3,id);assert.equal(t.rättSvar[1],`x≠${n}`);assert.equal(t.svarFormat[1],'definitionsmangd_utom');
  assert.match(t.spelDelar[1].s,/alla andra reella tal/);assert.match(t.spelDelar[0].s,/Faktorisera/);assert.match(t.spelDelar[2].s,/Sätt in/);
 }
 for(const x of [-4,0,3,4]) assert.ok(Math.abs(((x*x-4)/(x*x-x-2))/((x+2)/(x-1))-(x-1)/(x+1))<1e-10);
 for(const x of [-4,0,3,4]) assert.ok(Math.abs(2/(x-1)+3/(x+2)-(5*x+1)/((x-1)*(x+2)))<1e-10);
 for(const id of ['1.135','1.211'])assert.match(q(ma3,id).t,/x-värden som inte ingår/);
});
test('Nivåer, radianvinkel och trigonometrisk avrundning motsvarar uppgifterna',()=>{
 assert.equal(q(ma3,'1.66').traningsniva,4);assert.equal(q(ma3,'1.216').traningsniva,5);
 for(const x of [-3,-2,3])assert.equal(x**3+2*x*x-9*x-18,0);
 const c=(Math.sqrt(3)-1)/2,v=Math.acos(c),area=200*Math.sin(v)+100*Math.sin(v)*Math.cos(v);
 assert.ok(Math.abs(v-1.196)<.001);assert.ok(Math.abs(area-220.18)<.02);assert.match(q(ma4,'2.269').t,/radianer/);
 assert.equal(Math.round(10*9*Math.sin(32*Math.PI/180))/10,4.8);assert.match(q(ma1,'4.50').t,/en decimal/);assert.equal(q(ma1,'4.50').tolerans,.05);
 assert.deepEqual(Array.from(q(ma1,'4.514').rättSvar),[6,12]);
});
test('Figurer och svarsfält ger inte svaret eller bristande kontrast',()=>{
 for(const id of ['4.429','4.434','4.442','4.465','4.466','4.469','4.470','4.471','4.472']){
  assert.doesNotMatch(q(ma3,id).t,/currentColor/);assert.match(q(ma3,id).t,/#243447/);
 }
 assert.equal(q(ma2,'3.263').svarFormat,'punkt');assert.equal(q(ma2,'3.295').rättSvar,5);
 const t=q(ma4,'2.106');assert.doesNotMatch(t.spelDelar[0].s,/minimipunkt|maximipunkt|avtagande/);
});
