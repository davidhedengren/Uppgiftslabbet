'use strict';
const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('node:fs'),path=require('node:path'),vm=require('node:vm');
function read(file,key){const c={window:{}};vm.runInNewContext(fs.readFileSync(path.join(__dirname,'..',file),'utf8'),c);return c.window[key]}
const ma2=read('uppgifterma2.js','BANKMA2'),ma4=read('uppgiftermato2.js','BANKMATO2');
test('Tabellavläsning bygger på samma tabell för varje del och punkten är ordnad',()=>{
 const q=ma2.find(x=>x.id==='2.436'),table=q.t.match(/<table\b[\s\S]*?<\/table>/)[0];
 for(const d of q.spelDelar)assert.ok(d.t.includes(table));
 assert.doesNotMatch(q.spelDelar[0].t,/f\(2\)\s*=\s*-3/);
 assert.deepEqual(JSON.parse(JSON.stringify(q.rättSvar)),[-3,0,[-3,6]]);assert.equal(q.spelDelar[2].svarsstruktur,'ordnad');
 assert.deepEqual(Array.from(q.spelDelar[2].svarEtiketter),['x-koordinat','y-koordinat']);
});
test('Rotationsfiguren är uttryckligt kopplad till a och alla volymer är korrekta',()=>{
 const q=ma4.find(x=>x.id==='3.116');assert.match(q.spelDelar[0].fraga,/Figuren hör till del a/);
 assert.deepEqual(Array.from(q.rättSvar),['26*pi/3','8*pi','12*pi']);
 assert.equal((3**3-1)/3,26/3);assert.equal((4**2)/2,8);assert.equal(2**2*3,12);
});
