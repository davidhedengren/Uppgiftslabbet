'use strict';
const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('fs'),vm=require('vm');const c={window:{}};vm.runInNewContext(fs.readFileSync(__dirname+'/../uppgifter.js','utf8'),c);const bank=c.window.BANK,q=id=>bank.find(q=>q.id===id),ids=Array.from({length:8},(_,i)=>'9.'+(444+i));
test('Standardmodellen: åtta självständiga figuruppgifter och verktyg/metadata',()=>{
 const svgs=new Set();for(const id of ids){const p=q(id);assert.equal(bank.filter(q=>q.id===id).length,1,id);assert.equal(p.omr,'standardmodellen');assert.equal(p.miniräknare,true);assert.equal(p.geogebra,false);assert.equal(p.spel,true);assert.equal(p.självrättning,true);assert.match(p.t,/<svg/);assert.match(p.t,/\((?:Välj|Svara)/);assert.ok(p.ledtrad);assert.doesNotMatch(p.s,/facit-steglista|[\u0000-\u0008\u000b\u000c\u000e-\u001f]/);svgs.add(p.t.match(/<svg[\s\S]*?<\/svg>/)[0]);}assert.equal(svgs.size,8);assert.equal(bank.filter(q=>q.omr==='standardmodellen').length,31/* 24 + 7 kort från omgång 5 (2026-10-25, 9.524–9.530) */);
});
test('Kvarkladdning och motsatta laddningar räknas oberoende',()=>{
 const charges={u:2/3,d:-1/3,'anti-u':-2/3,'anti-d':1/3},charge=labels=>labels.reduce((sum,x)=>sum+charges[x],0);
 assert.ok(Math.abs(charge(['u','d','d']))<1e-12);assert.ok(Math.abs(charge(['anti-u','anti-d','anti-d']))<1e-12);
 const pairs=[['A',['u','u','d'],['u','u','d']],['B',['u','d','d'],['u','u','d']],['C',['u','u','d'],['anti-u','anti-u','anti-d']],['D',['u','d','d'],['anti-u','anti-u','anti-d']]];
 assert.deepEqual(pairs.filter(([,a,b])=>Math.abs(charge(a)+charge(b))<1e-12).map(([p])=>p),['C']);assert.equal(q('9.451').alternativ.find(a=>a.ratt).txt,'Par C');
 assert.equal(q('9.448').rättSvar,(3+4)*3);assert.equal(q('9.448').svarFormat,'antal_satt');assert.equal(q('9.451').traningsniva,3);
});
test('Begreppsval och förklaringar följer den markerade bilden',()=>{
 const answers={'9.444':'A','9.445':'Bild B','9.446':'En d-kvark omvandlas till en u-kvark.','9.447':'Den är oladdad och består av antikvarkar.','9.449':'Neutronen','9.450':'En positron','9.451':'Par C'},positions=[];
 for(const[id,answer]of Object.entries(answers)){const p=q(id);assert.equal(p.alternativ.filter(a=>a.ratt).length,1,id);assert.equal(p.alternativ.find(a=>a.ratt).txt,answer);assert.ok(p.alternativ.every(a=>a.kommentar));positions.push(p.alternativ.findIndex(a=>a.ratt));}assert.equal(new Set(positions).size,4);
 assert.match(q('9.450').t,/proton i en atomkärna/);assert.match(q('9.446').s,/elektronen har laddningen −e/);
});
test('Kvarkladdningar finns i facit men inte som formelsamlingsledningar i frågorna',()=>{
 for(const id of ['GY25-FY1-STD-02','9.261','9.262','9.263','9.264','9.265','9.329']){const p=q(id);for(const text of [p.t,p.spelIntro||'',...(p.spelDelar||[]).map(d=>d.t)])assert.doesNotMatch(text,/laddningen [+-]?[−+]?2\/3|laddningen [−-]1\/3|\\frac\{?2\}?\{?3/);assert.match(p.s,/(2\/3|\\frac23)/);}
 for(const p of q('9.329').spelDelar){assert.match(p.t,/tre kvarkar av typerna u och d/);assert.match(p.t,/laddningen/);assert.doesNotMatch(p.t,/heltal/);assert.doesNotMatch(p.t,/föregående|svaret ovan/);}
});
