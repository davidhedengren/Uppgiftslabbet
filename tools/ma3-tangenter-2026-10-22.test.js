const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('fs'),vm=require('vm'),path=require('path');
const ctx={window:{}};vm.runInNewContext(fs.readFileSync(path.join(__dirname,'../uppgiftermato1.js'),'utf8'),ctx);
const bank=ctx.window.BANKMATO1,q=id=>bank.find(q=>q.id===id),ids=Array.from({length:6},(_,i)=>'1.'+(862+i));
test('Lutningar och omvänt funktionsvärde följer de givna koordinaterna',()=>{
 for(const [id,value] of [['1.862',(5-5)/(5-1)],['1.863',(0-6)/(4-0)],['1.864',(100-40)/(6-2)],['1.866',.8],['1.867',2+2*(4-1)]])assert.equal(q(id).rättSvar,value,id);
 const c=q('1.865');assert.equal(c.alternativ.filter(a=>a.ratt).length,1);assert.match(c.alternativ.find(a=>a.ratt).txt,/samma lutning/);
 // Cubic crosses the tangent but its secant slope tends to zero from both sides.
 for(const h of [-.1,.1,-.01,.01])assert.ok(Math.abs((h**3/4)/h-h*h/4)<1e-12);
});
test('Nivå, verktyg, självständiga kort och läsbara figurer',()=>{
 const levels={1:0,2:0,3:0};for(const id of ids){const t=q(id);assert.ok(t);levels[t.traningsniva]++;assert.equal(t.omr,'tangent_sekant');assert.deepEqual(Array.from(t.kurs),['1b','1c']);assert.equal(t.miniräknare,true);assert.equal(t.geogebra,false);assert.equal(t.spel,true);assert.equal(t.självrättning,true);assert.equal(t.spelDelning,undefined);assert.equal((t.t.match(/<svg /g)||[]).length,1);assert.match(t.t,/role="img"/);assert.match(t.s,/facit-svar/);assert.doesNotMatch(t.t+t.s,/[\u0000-\u0008\u000b-\u001f]/);}
 assert.deepEqual(levels,{1:4,2:1,3:1});assert.equal(new Set(bank.map(q=>q.id)).size,bank.length);
 // No y tick labels in the inverse problem: calculate the missing y-coordinate.
 assert.doesNotMatch(q('1.867').t,/<text x="49"/);
});
