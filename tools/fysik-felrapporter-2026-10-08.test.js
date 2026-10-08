const test=require('node:test'),assert=require('node:assert/strict'),fs=require('node:fs'),path=require('node:path'),vm=require('node:vm');
const c={window:{}};vm.runInNewContext(fs.readFileSync(path.join(__dirname,'../uppgifter.js'),'utf8'),c);const get=id=>c.window.BANK.find(q=>q.id===id);
test('Massan ur rörelseenergin godtar två värdesiffror och avvisar nästa heltal',()=>{
 const q=get('5.142'),m=2*1900/6.8**2;
 assert.equal(q.rättSvar,82);assert.ok(Math.abs(m-q.rättSvar)<q.tolerans);assert.ok(Math.abs(83-q.rättSvar)>q.tolerans);
 assert.match(q.t,/två värdesiffror/);assert.match(q.s,/82 kg/);
});
test('Arbetet av en sned kraft avrundas konsekvent i text, facit och maskinsvar',()=>{
 const q=get('5.209'),w=100*5*Math.cos(Math.PI/6);
 assert.equal(q.rättSvar[1],433);assert.ok(Math.abs(w-433)<q.tolerans[1]);assert.ok(Math.abs(432-433)>q.tolerans[1]);
 assert.match(q.spelDelar[1].t,/tre värdesiffror/);assert.match(q.spelDelar[1].s,/433 J/);assert.equal(q.omr,'arbete');
});
test('Rörelsemängdskortet a innehåller bara sin egen vagn och tydlig teckenriktning',()=>{
 const q=get('5.160'),a=q.spelDelar[0];assert.equal(q.rättSvar[0],3*2.5);assert.equal(a.traningsniva,1);
 assert.match(a.t,/Höger räknas som positiv riktning/);assert.match(a.t,/med tecken/);assert.doesNotMatch(a.t,/stöten|4,0 kg|1,5 m\/s/);
});
