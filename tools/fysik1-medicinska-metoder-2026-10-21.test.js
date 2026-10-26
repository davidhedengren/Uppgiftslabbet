'use strict';
const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('fs'),vm=require('vm');const c={window:{}};vm.runInNewContext(fs.readFileSync(__dirname+'/../uppgifter.js','utf8'),c);const bank=c.window.BANK,q=id=>bank.find(q=>q.id===id),ids=Array.from({length:8},(_,i)=>'9.'+(436+i));
test('Åtta olika figurkort i den tidigare tunna medicindelen',()=>{
 const svgs=new Set();for(const id of ids){const p=q(id);assert.equal(bank.filter(q=>q.id===id).length,1,id);assert.equal(p.omr,'medicinska_metoder');assert.equal(p.familj,'Strålning i medicin');assert.equal(p.miniräknare,true);assert.equal(p.geogebra,false);assert.equal(p.spel,true);assert.equal(p.självrättning,true);assert.match(p.t,/<svg/);assert.ok(/\((?:Välj|Svara)/.test(p.t)||p.svarEnhet);assert.ok(!/facit-steglista/.test(p.s));assert.ok(p.ledtrad);svgs.add(p.t.match(/<svg[\s\S]*?<\/svg>/)[0]);}assert.equal(svgs.size,8);assert.equal(bank.filter(q=>q.omr==='medicinska_metoder').length,38); // 21 + 10 kort från omgång 3 (9.504–9.513) + 7 från omgång 5 (9.550–9.556)
});
test('Dosbidrag, ursprungligt signalvärde, bakgrund och transport beräknas från givna data',()=>{
 assert.equal(q('9.437').rättSvar,(800-300)/800*100);assert.equal(q('9.438').rättSvar,4*.8);
 assert.equal(q('9.440').rättSvar*.5**(220/110),180);assert.equal(q('9.441').rättSvar+60,180);assert.equal(q('9.441').svarFormat,'antal_satt');
 const doseA=.002/.010,doseB=.002/.020;assert.equal(doseA/doseB,2);assert.match(q('9.442').alternativ.find(a=>a.ratt).txt,/^A,/);
});
test('Aktivitetsgrafens halveringstid och val av två tidskrav',()=>{
 assert.equal(160*2**(-q('9.439').rättSvar/3),80);assert.match(q('9.439').t,/80 MBq vid 3 h/);
 const eligible=[['A',20],['B',120],['C',10*24*60]].filter(([,half])=>2**(-120/half)>=.25&&2**(-1440/half)<=.01).map(([name])=>name);
 assert.deepEqual(eligible,['B']);assert.equal(q('9.443').alternativ.find(a=>a.ratt).txt,'Ämne B');
 assert.equal(q('9.443').traningsniva,3);for(const id of ['9.436','9.438','9.439','9.441'])assert.equal(q(id).traningsniva,1);
});
test('Bildval, rimliga felalternativ och kommentarer är kopplade till hela alternativet',()=>{
 assert.equal(q('9.436').alternativ.find(a=>a.ratt).txt,'Bild B');const positions=[];
 for(const id of ['9.436','9.442','9.443']){const p=q(id);assert.equal(p.alternativ.filter(a=>a.ratt).length,1);assert.ok(p.alternativ.every(a=>a.kommentar));positions.push(p.alternativ.findIndex(a=>a.ratt));}
 assert.equal(new Set(positions).size,3);
});
