'use strict';
const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('node:fs'),vm=require('node:vm');
const c={window:{}};vm.runInNewContext(fs.readFileSync(require('node:path').join(__dirname,'../uppgifter.js'),'utf8'),c);
const get=id=>c.window.BANK.find(t=>t.id===id);
test('Simmarens tre svar är korrekta och c-kortet har egen tid och riktningsfigur',()=>{
 const q=get('3.311');assert.deepEqual(Array.from(q.rättSvar),[Math.hypot(.9,1.2),60/1.2,.9*50]);
 for(const d of q.spelDelar){assert.match(d.t,/<svg/);assert.match(d.t,/data-vektor="simning"/);assert.match(d.t,/data-vektor="strom"/);assert.match(d.t,/data-vektor="land"/);}
 const d=q.spelDelar[2];assert.match(d.t,/50 s/);assert.match(d.t,/0,9 m\/s/);assert.doesNotMatch(d.t,/60 m|1,2 m\/s|45 m/);
 assert.doesNotMatch(JSON.stringify(q),/överfarten/i);assert.deepEqual(q.spelDelar.map(d=>d.traningsniva).join(','),'2,1,1');
});
test('Färjeuppgiften behåller fysiken med enklare språk',()=>{
 const q=get('3.131');assert.doesNotMatch(JSON.stringify(q),/överfarten|Tvärfarten/);
 assert.deepEqual(Array.from(q.rättSvar),[240/3,1.2*240/3,Math.round(Math.asin(1.2/3)*180/Math.PI*10)/10,Math.round(240/Math.sqrt(3**2-1.2**2)*10)/10]);
});
test('Influens har ett begripligt felalternativ om fastsittande elektroner',()=>{
 const q=get('8.503');assert.equal(q.alternativ.length,5);assert.equal(q.alternativ.filter(a=>a.ratt).length,1);
 const a=q.alternativ.find(a=>/sitter fast/.test(a.txt));assert.equal(a.ratt,false);assert.match(a.kommentar,/kan röra sig/);
 assert.match(q.s,/sammanlagda laddning är fortfarande noll/);
});
