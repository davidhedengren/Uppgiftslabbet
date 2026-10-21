'use strict';
const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('fs'),vm=require('vm');const c={window:{}};vm.runInNewContext(fs.readFileSync(__dirname+'/../uppgifter.js','utf8'),c);const q=id=>c.window.BANK.find(q=>q.id===id);
test('5.386: fullständig kraftmodell bevaras men a blir nivå 5, b är nivå 2',()=>{
 const p=q('5.386');assert.equal(p.traningsniva,5);assert.equal(p.spelDelar[0].traningsniva,5);assert.equal(p.spelDelar[1].traningsniva,2);
 assert.ok(Math.abs(p.rättSvar[0]-(1.2*(2.1-(-5.2))+1.2*9.82*.0200))<1e-12);assert.equal(p.rättSvar[1],9/.0200);
 assert.match(p.spelDelar[0].t,/golvets kraft och tyngdkraften/);assert.match(p.spelDelar[0].t,/5,2 m\/s nedåt/);assert.match(p.spelDelar[0].t,/2,1 m\/s uppåt/);assert.match(p.spelDelar[0].s,/Normalkraft/);assert.match(p.spelDelar[0].s,/Tyngdkraft/);assert.match(p.spelDelar[0].s,/inte samma sak som den sammanlagda impulsen/);assert.match(p.spelDelar[0].s,/0\{,\}23568/);
 assert.doesNotMatch(p.spelDelar[0].s,/450/);assert.match(p.spelDelar[1].t,/9,00 Ns/);assert.doesNotMatch(p.spelDelar[1].s,/8\{,\}76/);
 for(const d of p.spelDelar){assert.equal(d.miniräknare,true);assert.equal(d.geogebra,false);}
});
test('8.150: tre potentialer beskriver en möjlig sluten seriekrets och ändrad nollnivå',()=>{
 const p=q('8.150'),v=[12,7,0],current=(v[0]-v[1])/250,r2=(v[1]-v[2])/current;
 assert.equal(current,.020);assert.equal(r2,350);assert.equal(12/(250+r2),current);
 assert.deepEqual(Array.from(p.rättSvar[3]),v.map(x=>x-v[0]));assert.equal(p.rättSvar[0],v[0]-v[1]);assert.equal(p.rättSvar[1],v[1]-v[2]);assert.equal(p.spelDelar[2].alternativ.filter(a=>a.ratt).length,1);assert.match(p.spelDelar[2].alternativ.find(a=>a.ratt).txt,/20 mA, från A till B/);
 for(const text of [p.t,p.spelIntro,...p.spelDelar.map(d=>d.t)]){
  assert.match(text,/C är ansluten till batteriets minuspol/);assert.match(text,/M380 80L380 130/);assert.match(text,/<rect x="370" y="130" width="20" height="60"/);assert.match(text,/M380 190L380 230/);assert.match(text,/M380 230L110 230/);
  assert.match(text,/M110 80L110 145/);assert.match(text,/M110 165L110 230/);assert.doesNotMatch(text,/M110 145L110 165/);assert.match(text,/max-width:480px/);
 }
 for(const d of p.spelDelar){assert.equal(d.miniräknare,true);assert.equal(d.geogebra,false);assert.equal((d.t.match(/<svg/g)||[]).length,1);assert.ok(d.ledtrad);}
 assert.deepEqual(Array.from(p.spelDelar[3].svarEtiketter),['A','B','C']);assert.equal(p.spelDelar[3].svarsstruktur,'ordnad');assert.match(p.spelDelar[3].fraga,/i stället för C/);assert.match(p.spelDelar[3].s,/Bara nollnivån ändras/);
});
test('Fem impulsjämförelser använder rätt kraftmodell och fem eljämförelser rätt nollnivå',()=>{
 assert.ok(Math.abs(q('5.381').rättSvar[0]-.35*(-3.1-5))<=q('5.381').tolerans[0]+1e-12);
 assert.ok(Math.abs(q('5.394').rättSvar-.150*(Math.sqrt(2*9.82*1.25)+Math.sqrt(2*9.82*.960)))<1e-12);assert.match(q('5.394').t,/från tyngdkraftens impuls/);
 assert.ok(Math.abs(q('5.395').rättSvar[1]-(.050*Math.sqrt(2*9.82*1)/.010+.050*9.82))<1e-12);
 assert.ok(Math.abs(q('5.396').rättSvar-.10*((2*9.82*2)/(2*.060)+9.82))<1e-12);
 assert.ok(Math.abs(q('5.397').rättSvar[2]-(75*24/.0833+75*9.82))<1e-8);
 assert.deepEqual(Array.from(q('8.49').rättSvar[2]),[9,6]);assert.deepEqual(Array.from(q('8.149').rättSvar[2]),[4,-8]);assert.equal(q('8.148').rättSvar[2],-3);
 assert.match(q('8.144').spelDelar[2].s,/V_A=7\{,\}5\+2\{,\}5=10/);for(const [i,p] of [1.4,1.2,.2].entries())assert.ok(Math.abs(q('8.117').rättSvar[1][i]-p)<1e-12);
});
