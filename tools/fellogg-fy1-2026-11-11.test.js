'use strict';
const{test}=require('node:test'),assert=require('node:assert/strict'),fs=require('node:fs'),vm=require('node:vm'),path=require('node:path');
const root=path.join(__dirname,'..'),c={window:{}};vm.runInNewContext(fs.readFileSync(path.join(root,'uppgifter.js'),'utf8'),c);
const q=id=>c.window.BANK.find(t=>t.id===id),plain=x=>JSON.parse(JSON.stringify(x));
const near=(a,b)=>assert.ok(Math.abs(a-b)<1e-11*Math.max(1,Math.abs(b)),`${a} ≠ ${b}`);
test('2.59 prövar vanliga hastighetsenheter, med tydliga självständiga kort',()=>{
 const t=q('2.59');assert.deepEqual(plain(t.rättSvar),[14*3600/1000,14*60]);assert.deepEqual(plain(t.svarEnhet),['km/h','m/min']);
 for(const p of t.spelDelar){assert.match(p.t,/14,0 m\/s/);assert.match(p.t,/en decimal/);assert.doesNotMatch(p.t+p.s,/knop|nautisk/i);assert.match(p.s,/facit-steglista/);}
});
test('Energiomvandlingar introduceras i energikapitlet utan nya ID eller svar',()=>{
 for(const id of ['2.19','2.29','2.33','2.36','2.209','2.217','2.220','2.362'])assert.equal(q(id).kap,5,id);
 for(const id of ['2.58','2.60','2.61','2.62','2.76'])assert.equal(q(id).kap,2,id);
});
test('8.294 är märkt fördjupning med given modell och visas inte i vanlig träning',()=>{
 const t=q('8.294');assert.equal(t.spel,false);assert.match(t.t,/Fördjupning.*potential från punktladdningar/);assert.match(t.t,/V=kq\/r/);near(t.rättSvar,8.99e9*(3e-6-1e-6)/.2);
 for(const id of ['8.280','8.281','8.282','8.283','8.284'])assert.notEqual(q(id).spel,false,id);
});
test('Vattnets alternativa densiteter räknas in i energibalansen, inte i toleransen',()=>{
 const t=q('7.221');assert.deepEqual(plain(t.tolerans),[.05,.0005,.005]);assert.equal(t.svarTabell['1'],undefined);
 [.997,.998,.9982].forEach((rho,i)=>{
 const mass=5*rho,correct=(.05*2260+.05*4.18*100+mass*4.18*11)/(4.18*(mass+.05));near(t.svarTabell[0][i],correct);
 const wm=.25*rho,ice=.04,energyToMelt=ice*(2.2*18+334);near(q('7.220').svarTabell[0][i],(wm*4.18*18-energyToMelt)/(4.18*(wm+ice)));
 });
 near(t.rättSvar[1],.5*334/(2260+4.18*100));near(t.rättSvar[2],(2260+4.18*50)/(334+4.18*50));
 for(const p of t.spelDelar)assert.match(p.s,/facit-steglista/);
});
test('Gaskonstantens tabellalternativ är separat beräknade i rätt enhet',()=>{
 const rs=[8.314,8.314421,8.31446261815324];rs.forEach((r,i)=>{near(q('6.338').svarTabell[0][i],.25*r*300/1e5*1000);near(q('6.337').svarTabell[0][i],.5*r*300/.012/1000);
 [283.15,283].forEach((T,j)=>near(q('6.201').svarTabell[0][i*2+j],16*r*T/35000));});
 assert.equal(q('6.338').tolerans,.005);assert.equal(q('6.337').tolerans,.05);assert.equal(q('6.201').svarTabell[1],undefined);
});
test('Alla berörda huvuduppgifter och delkort tillåter miniräknare',()=>{
 for(const id of ['2.59','2.19','2.29','2.33','2.36','2.209','2.217','2.220','2.362','8.294','7.221','7.220','6.201','6.337','6.338','2.76']){
 const t=q(id);assert.equal(t.miniräknare,true,id);assert.equal(t.geogebra,false,id);for(const p of t.spelDelar||[])assert.notEqual(p.miniräknare,false,id);
 }
});
