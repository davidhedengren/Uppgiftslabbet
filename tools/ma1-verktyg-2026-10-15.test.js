'use strict';
const {test}=require('node:test');
const assert=require('node:assert/strict'),fs=require('node:fs'),vm=require('node:vm'),path=require('node:path');
const root=path.join(__dirname,'..'),context={window:{}};
vm.runInNewContext(fs.readFileSync(path.join(root,'uppgifterma1.js'),'utf8'),context);
const bank=JSON.parse(JSON.stringify(context.window.BANKMA1));
const review=JSON.parse(fs.readFileSync(path.join(root,'agent/MA1_VERKTYG_2026-10-15.json'),'utf8'));
const q=id=>{const found=bank.find(q=>q.id===id);assert.ok(found,id);return found;};
// Senare dokumenterade verktygsbeslut: 1.116 miniräknare tillåten (FELRAPPORTER_2026-10-23_1345).
const SENARE={'1.116':[true,false]};
const tools=(parent,part)=>[part?.miniräknare??parent.miniräknare,part?.geogebra??parent.geogebra];
test('Hela Ma1 motsvarar de manuellt bedömda verktygsbesluten, inklusive egna delkort',()=>{
 // Nya uppgifter får tillkomma utan att en daterad granskningslogg skrivs om.
 assert.equal(review.reviewed.length,3968);assert.ok(bank.length>=review.reviewed.length);
 const ids=new Set();let parts=0;
 for(const r of review.reviewed){assert.ok(!ids.has(r.id),r.id);ids.add(r.id);const task=q(r.id);assert.equal(task.omr,r.area);assert.ok(r.reason.length>30);assert.deepEqual(tools(task),SENARE[r.id]??r.tools,r.id);
  assert.equal(task.spelDelar?.length??0,r.parts.length,r.id);
  r.parts.forEach((p,i)=>{parts++;assert.deepEqual(tools(task,task.spelDelar[i]),p.tools,r.id+p.label);assert.ok(!p.tools[1]||p.tools[0],r.id+p.label);});
  assert.ok(!r.tools[1]||r.tools[0],r.id);
 }assert.equal(parts,954);
});
test('Digital undersökning tillåts, men direkt insättning och potensskalning behöver inte GeoGebra',()=>{
 for(const id of ['2.548','2.547','6.77','6.81','6.88','6.419'])assert.deepEqual(tools(q(id)),[true,true],id);
 for(const id of ['2.41','2.43','2.193','2.413','3.07','3.39','3.88','6.38','6.76'])assert.deepEqual(tools(q(id)),[true,false],id);
});
test('Metodundantag för överslag och exakta potenslagar bevaras, numeriska kontroller tillåts',()=>{
 for(const id of ['0.285','0.855','0.1064','3.118','3.177','4.555','7.112'])assert.deepEqual(tools(q(id)),[false,false],id);
 for(const id of ['0.928','7.104','7.105','7.541'])assert.deepEqual(tools(q(id)),[true,false],id);
});
test('Blandade uppgifter får olika behörigheter för sina olika lärandemål',()=>{
 for(const [id,expected]of [['6.69',[[true,true],[true,true],[false,false]]],['2.36',[[true,false],[true,true]]],['2.194',[[false,false],[true,false],[false,false]]],['7.113',[[true,false],[false,false],[false,false]]]]){
  assert.deepEqual(q(id).spelDelar.map(d=>tools(q(id),d)),expected,id);
 }
});
