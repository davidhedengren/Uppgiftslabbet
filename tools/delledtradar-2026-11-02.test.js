const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('fs'),vm=require('vm'),path=require('path');
function bank(file,name){const c={window:{}};vm.runInNewContext(fs.readFileSync(path.join(__dirname,'..',file),'utf8'),c);return JSON.parse(JSON.stringify(c.window[name]));}
const ma2=bank('uppgifterma2.js','BANKMA2'),mato1=bank('uppgiftermato1.js','BANKMATO1');
const q=(bank,id)=>{const q=bank.find(x=>x.id===id);assert.ok(q,id);return q;};
test('Delledtrådar till modeller och tabeller hjälper utan att ange efterfrågade koefficienter',()=>{
 const model=q(ma2,'1.76');assert.doesNotMatch(model.spelDelar[0].ledtrad,/850|32/);assert.match(model.spelDelar[1].ledtrad,/530/);
 const table=q(ma2,'1.104');assert.doesNotMatch(table.spelDelar[0].ledtrad,/-2|−2|k=|m=/);assert.match(table.spelDelar[1].ledtrad,/riktningskoefficienten/);assert.match(table.spelDelar[0].s,/-1-4=-5/);assert.doesNotMatch(table.spelDelar[0].s,/y=-2x\+3/);
 const bike=q(ma2,'1.234');assert.doesNotMatch(bike.spelDelar[0].ledtrad,/konstantterm|fast avgift|oberoende/i);assert.match(bike.spelDelar[1].ledtrad,/oberoende/);
});
test('Derivata får en egen ledtråd och tangentdelen behåller sin ledtråd',()=>{
 const t=q(mato1,'2.20');assert.match(t.spelDelar[0].ledtrad,/multiplicerar/);assert.doesNotMatch(t.spelDelar[0].ledtrad,/tangent/);assert.match(t.ledtrad,/tangentpunkten/);assert.equal(t.spelDelar[1].ledtrad,undefined);
});
