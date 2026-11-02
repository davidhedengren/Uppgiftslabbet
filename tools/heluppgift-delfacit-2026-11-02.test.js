const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('fs'),vm=require('vm'),path=require('path');
function bank(file,name){const c={window:{}};vm.runInNewContext(fs.readFileSync(path.join(__dirname,'..',file),'utf8'),c);return JSON.parse(JSON.stringify(c.window[name]));}
const ma1=bank('uppgifterma1.js','BANKMA1'),matf1=bank('uppgiftermatf1.js','BANKMATF1');
const q=(b,id)=>{const t=b.find(x=>x.id===id);assert.ok(t,id);return t};
test('Tabelluppgiftens tre delfacit förklarar var sin del utan att föregripa nästa',()=>{
 const t=q(ma1,'2.201');assert.equal(t.delfacit.length,3);
 assert.match(t.delfacit[0],/10/);assert.doesNotMatch(t.delfacit[0],/exponentiell|förändringsfaktor/i);
 assert.match(t.delfacit[1],/faktor.*3/i);assert.doesNotMatch(t.delfacit[1],/y\s*=\s*5/);
 assert.match(t.delfacit[2],/5\\cdot3\^x/);assert.equal(15/5,45/15);assert.equal(45/15,135/45);
});
test('Vinkelräta vektorers summa och differens motiveras var för sig',()=>{
 const t=q(ma1,'4.22');assert.equal(t.delfacit.length,2);assert.doesNotMatch(t.delfacit[0],/differens|\\vec u-\\vec v/i);
 for(const s of t.delfacit)assert.match(s,/13/);assert.equal(Math.hypot(5,12),13);
});
test('Differentialekvationens jämvikter och två gränsbeteenden hålls isär',()=>{
 const t=q(matf1,'4.138');assert.equal(t.delfacit.length,3);assert.match(t.delfacit[0],/y=0/);assert.match(t.delfacit[0],/y=2/);
 assert.match(t.delfacit[1],/underifrån/);assert.doesNotMatch(t.delfacit[1],/ovanifrån/);assert.match(t.delfacit[2],/ovanifrån/);
 assert.ok(.5*(2-.5)>0);assert.ok(3*(2-3)<0);
});
