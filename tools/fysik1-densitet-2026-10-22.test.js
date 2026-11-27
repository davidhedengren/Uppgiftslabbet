'use strict';
// Zink 7,13 g/cm³ enligt formelsamlingen (felrapport 2026-11-23 18:07).
const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('fs'),vm=require('vm');
const c={window:{}};vm.runInNewContext(fs.readFileSync(__dirname+'/../uppgifter.js','utf8'),c);
const bank=Object.values(c.window)[0],q=id=>bank.find(x=>x.id===id);
test('Densitet: full precision i fem avrundade maskinfacit',()=>{
 const gold=1/19.3/5000*1e7,lead=15000/11.3;
 const rows=[['2.18',[300/(200/8.96+100/7.13)],[.005]],['2.27',[gold,gold/.29],[.5,.5]],['2.274',[4*Math.PI/3*(2.7*8+7.8*(27-8))],[.05]],['2.52',[lead,Math.cbrt(3*lead/(4*Math.PI)),Math.cbrt(6*lead/(4*Math.PI))],[5,.005,.005]],['2.54',[450/8.96,8.96*27],[.05,.5]]];
 for(const[id,values,tolerances]of rows){const x=q(id);const ans=[].concat(x.rättSvar),tol=[].concat(x.tolerans);
  values.forEach((v,i)=>{assert.ok(Math.abs(ans[i]-v)<1e-10,id);assert.equal(tol[i],tolerances[i],id);});
  assert.ok(/med (två decimaler|en decimal|tre värdesiffror)/.test(x.t)||[].concat(x.svarVardesiffror).some(v=>v>=1));
 }
});
test('Delkorten har gemensam inledning, egna frågor och egna ledtrådar',()=>{
 // 2026-11-27: deluppgiftskedjan (felrapport 2.52). Alla delkort börjar med samma inledning; tidigare krävde testet
 // att a-korten bara hade sina egna data. Det som ändras i en del står i delens fråga.
 for(const id of ['2.17','2.26','2.52'])for(const d of q(id).spelDelar)assert.ok(d.t.startsWith(q(id).spelIntro),id+d.etikett);
 assert.match(q('2.27').spelDelar[1].t,/0,29/);
 assert.match(q('2.52').spelDelar[2].fraga,/30 kg/);assert.doesNotMatch(q('2.52').spelDelar[2].t,/massan 30 kg\.<\/p>/);
 for(const id of ['2.17','2.26','2.54'])assert.equal(new Set(q(id).spelDelar.map(d=>d.ledtrad)).size,q(id).spelDelar.length);
});
test('Granskad mätprecision, nivå och verktyg på samtliga fjorton uppgifter',()=>{
 assert.deepEqual(Array.from(q('2.26').svarVardesiffror),[2,null,2,2]);
 assert.deepEqual(Array.from(q('2.38').svarVardesiffror),[2,2]);
 assert.deepEqual(Array.from(q('2.42').spelDelar,d=>d.traningsniva),[1,1,1,2]);
 for(const id of ['2.2','2.8','2.17','2.18','2.26','2.27','2.31','2.38','2.39','2.42','2.274','2.52','2.53','2.54']){
  const x=q(id);for(const card of [x,...(x.spelDelar||[]).map(d=>({...x,...d}))]){assert.equal(card.miniräknare,true,id);assert.equal(card.geogebra,false,id);assert.ok(card.s,id);assert.ok(card.ledtrad,id);}
 }
 assert.match(q('2.274').t,/<svg/);assert.match(q('2.274').t,/Genomskärning/);
 assert.equal(q('2.53').svarEnhet,'kg/m³');
});
