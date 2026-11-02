const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('fs'),vm=require('vm'),path=require('path');
const c={window:{}};vm.runInNewContext(fs.readFileSync(path.join(__dirname,'../uppgifter.js'),'utf8'),c);const bank=JSON.parse(JSON.stringify(c.window.BANK));
test('Komponentfacit visar bara de efterfrågade x-komposanterna',()=>{
 const cases={'3.301':[-2,2,0],'3.302':[-5,5,0],'3.303':[4,-4,0],'3.304':[4,2,6],'3.305':[3,3,6],'3.306':[1,-4,-3],'3.307':[3,-1,2],'3.308':[-2,0,-2]};
 for(const [id,[a,b,sum]] of Object.entries(cases)){
  const q=bank.find(t=>t.id===id);assert.ok(q,id);assert.equal(a+b,sum,id);assert.equal(q.rättSvar[0],sum,id);
  const s=q.spelDelar[0].s;assert.match(s,/x-komposanter/,id);assert.doesNotMatch(s,/vektorform|F_\{Ry\}|y-komposant/,id);
  assert.ok(s.includes(`F_{Rx}=${a}+(${b})=${sum}`),id);assert.ok(q.spelDelar[1].s,id+' b');
 }
});
