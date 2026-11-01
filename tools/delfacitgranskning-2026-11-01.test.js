'use strict';
const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('node:fs'),path=require('node:path'),vm=require('node:vm');
function bank(file,key){let c={window:{}};vm.runInNewContext(fs.readFileSync(path.join(__dirname,'..',file),'utf8'),c);return c.window[key];}
const ma2=bank('uppgifterma2.js','BANKMA2'),ma4=bank('uppgiftermato2.js','BANKMATO2'),fy=bank('uppgifter.js','BANK');
const get=(b,id)=>{const q=b.find(q=>q.id===id);assert.ok(q,id);return q};
test('Derivatafacit behandlar aktuell del utan att avslöja senare slutsatser',()=>{
 const ids=['2.117','2.229','2.42','2.77','2.158','2.253','2.101'];
 for(const id of ids)assert.ok(get(ma4,id).spelDelar[0].s,id);
 assert.doesNotMatch(get(ma4,'2.117').spelDelar[0].s,/b\s*=\s*2/);
 assert.doesNotMatch(get(ma4,'2.229').spelDelar[0].s,/b\s*=\s*-2/);
 for(const id of ['2.42','2.77','2.253'])assert.doesNotMatch(get(ma4,id).spelDelar[0].s,/maximipunkt|minimipunkt/i);
 assert.doesNotMatch(get(ma4,'2.158').spelDelar[0].s,/sqrt/);
 assert.equal(5-2,3);assert.equal((8+12)/2,10);
 const second=x=>12*x*x-8,r=Math.sqrt(2/3);assert.ok(Math.abs(second(r))<1e-12);assert.ok(second(0)<0&&second(1)>0);
 const d=x=>(x-1)*(x-4);assert.ok(d(0)>0&&d(2)<0&&d(5)>0);
});
test('Frågor om volym, komplexa tal och exempel visar inte senare slutsvar',()=>{
 assert.doesNotMatch(get(ma4,'3.113').spelDelar[0].s,/243/);
 assert.doesNotMatch(get(ma4,'4.04').spelDelar[0].s,/75/);
 assert.doesNotMatch(get(ma4,'4.327').spelDelar[0].s,/\\sqrt3|area/i);
 assert.equal(3**5/5,243/5);assert.equal(30-(-45),75);assert.equal(Math.pow(64,1/6),2);
 const a=get(ma2,'1.313').spelDelar[0].s;assert.doesNotMatch(a,/\(1;0\{,\}5\)/);
 for(const [l,b] of [[1.8,.4],[2.6,.3]])assert.ok(Math.abs(l+8*b-5)<1e-12);
 assert.doesNotMatch(get(ma2,'3.462').spelDelar[1].s,/9 cm|12 cm|54/);
 assert.equal(5*(36/12),15);assert.equal(9*12/2,54);
 const speed=get(fy,'3.80').spelDelar[1].s;assert.doesNotMatch(speed,/6\s*m\/s|medelfart/i);assert.equal(2*24/4,12);
});
