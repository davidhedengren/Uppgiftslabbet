const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('fs'),vm=require('vm'),path=require('path');
const ctx={window:{}};vm.runInNewContext(fs.readFileSync(path.join(__dirname,'../uppgiftermato1.js'),'utf8'),ctx);const bank=ctx.window.BANKMATO1,q=id=>bank.find(q=>q.id===id),ids=Array.from({length:8},(_,i)=>'2.'+(1150+i));
test('Naturlig logaritm, inverse funktioner och definitionsmängd',()=>{
 assert.equal(q('2.1150').rättSvar,'e^(-2)');assert.ok(Math.abs(Math.log(Math.exp(-2))+2)<1e-12);assert.equal(q('2.1151').rättSvar,Math.round(Math.exp(Math.log(8))));assert.equal(q('2.1153').rättSvar,Math.log(Math.exp(4)));assert.ok(Math.abs(q('2.1154').rättSvar-Math.log(3))<1e-12);
 assert.equal(q('2.1156').svarFormat,'en_logaritm');assert.equal(q('2.1156').rättSvar,'ln(14)');assert.ok(Math.abs(Math.log(2)+Math.log(7)-Math.log(14))<1e-12);assert.ok(Math.abs(Math.log(2)+Math.log(3)-Math.log(5))>.1);
 assert.match(q('2.1152').alternativ.find(a=>a.ratt).txt,/Negativt/);assert.deepEqual(Array.from(q('2.1155').alternativ.filter(a=>a.ratt),a=>a.txt),['0,5','3']);assert.match(q('2.1157').alternativ.find(a=>a.ratt).txt,/ln 6/);
});
test('Verktyg bedöms efter begreppet och metadata stämmer på varje nytt kort',()=>{
 const levels={1:0,2:0};for(const id of ids){const t=q(id);levels[t.traningsniva]++;assert.equal(t.omr,'naturliga_logaritmer');assert.deepEqual(Array.from(t.kurs),['1b','1c']);assert.equal(t.spel,true);assert.equal(t.självrättning,true);assert.equal(t.geogebra,false);assert.equal(t.miniräknare,!['2.1151','2.1153','2.1156'].includes(id));assert.equal(t.spelDelning,undefined);assert.match(t.s,/facit-svar/);assert.doesNotMatch(t.t+t.s,/[\u0000-\u0008\u000b-\u001f]|<p><\/p>/);}
 assert.deepEqual(levels,{1:7,2:1});for(const id of ['2.1150','2.1151','2.1152','2.1154'])assert.match(q(id).t,/<svg /);assert.equal(new Set(bank.map(q=>q.id)).size,bank.length);
});
test('Äldre ekvationers svar bevaras och ledtråd för ln x isolerar ingen osynlig exponentialterm',()=>{
 const expected={'2.124':'x=(ln12)/(ln5)','2.129':'x=ln7','2.134':'x=(ln10)/(ln2)','2.413':'x=ln12','2.414':'x=e^3'};
 for(const [id,value]of Object.entries(expected)){const t=q(id);assert.equal(t.rättSvar,value);assert.match(t.s,/facit-svar/);assert.doesNotMatch(t.s,/Skriv om med samma bas när det går|facit-steglista/);assert.equal(t.miniräknare,true);assert.equal(t.geogebra,false);}
 assert.doesNotMatch(q('2.414').ledtrad,/isolera|exponentialtermen|båda leden logaritmeras/);
 assert.ok(Math.abs(5**(Math.log(12)/Math.log(5))-12)<1e-12);assert.ok(Math.abs(4*2**(Math.log(10)/Math.log(2))-40)<1e-12);assert.deepEqual(Array.from(q('2.816').rättSvar),['ln(2)','ln(3)']);
 for(const x of [Math.log(2),Math.log(3)])assert.ok(Math.abs(Math.exp(2*x)-5*Math.exp(x)+6)<1e-12);
});
