'use strict';
const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('fs'),vm=require('vm');
const c={window:{}};vm.runInNewContext(fs.readFileSync(__dirname+'/../uppgiftermato2.js','utf8'),c);
const bank=JSON.parse(JSON.stringify(c.window.BANKMATO2)),q=id=>bank.find(t=>t.id===id);
test('Radianfacit är matematiskt korrekta och har rad på rätt del',()=>{
 for(const [id,expected]of [['1.166',['(pi)/(6)','(3*pi)/(4)','(5*pi)/(4)','(5*pi)/(3)']],['1.449','pi/12'],['1.451','5*pi/6'],['1.458','5*pi/12'],['1.46',['pi','3*pi/2','5*pi']]]){
  assert.deepEqual(q(id).rättSvar,expected);
  assert.deepEqual(q(id).svarEnhet,Array.isArray(expected)?expected.map(()=>'rad'):'rad');
 }
 assert.deepEqual(q('1.27').svarEnhet,['rad','rad','°','°']);
 assert.equal(q('1.27').rättSvar[3],1.4*180/Math.PI);assert.equal(q('1.27').tolerans[3],.05);
 assert.deepEqual(q('1.27').spelDelar.map(p=>p.miniräknare),[false,false,false,true]);
});
test('Avrundning utgår från räknat fullvärde med frågans noggrannhet',()=>{
 for(const [id,answer,tol,unit,precision]of [
  ['2.180',40/(16*Math.PI),.005,'m/min','två'],['2.182',1/(2*Math.PI),.005,'cm/min','två'],
  ['2.231',.5/(4*Math.PI),.00005,'m/min','fyra'],['2.249',500/(256*Math.PI),.0005,'cm/s','tre'],
  ['2.456',6*Math.PI,.05,'cm³/s','en']]){
   assert.equal(q(id).rättSvar,answer);assert.equal(q(id).tolerans,tol);assert.equal(q(id).svarEnhet,unit);
   assert.ok(q(id).t.includes(precision+' decimal'));assert.equal(q(id).miniräknare,true);
 }
 assert.deepEqual(q('2.188').rättSvar,[5/(2*Math.PI),20]);assert.deepEqual(q('2.188').tolerans,[.005,0]);
 assert.match(q('2.188').spelDelar[1].s,/5\/\(2\\pi\)/); // B-facit härleder sin egen radiehastighet.
 assert.deepEqual(q('2.187').rättSvar,[12*Math.PI,4.8*Math.PI]);
 for(const p of q('2.187').spelDelar)assert.match(p.fraga,/en decimal/);
});
test('Grafskärningarnas lösningar svarar på frågan och använder rätt modeller',()=>{
 assert.ok(Math.abs(Math.exp(q('2.420').rättSvar)-3)<1e-12);
 assert.equal(Math.log(q('2.421').rättSvar-2),0);
 for(const id of ['2.420','2.421']){
  assert.match(q(id).t,/punktens x-koordinat/);assert.doesNotMatch(q(id).s,/asymptot|polynomdivision/);
  assert.match(q(id).t,/<svg/);assert.deepEqual(q(id).svarEtiketter,['x']);
 }
 assert.equal(q('2.420').traningsniva,2);assert.equal(q('2.420').tolerans,.005);
 assert.equal(q('2.422').rättSvar,4);assert.equal(q('2.422').tolerans,0);
 // 2.407 och 2.408 är flervalskort sedan 2026-10-24; C är tredje alternativet i bankens ordning.
 for(const id of ['2.407','2.408']){assert.equal(q(id).rättSvar??'ABCD'[q(id).alternativ.findIndex(a=>a.ratt)],'C');assert.doesNotMatch(q(id).s,/polynomdivision|sned asymptot/);}
});
test('Granskningsspåret omfattar varje förändring och bevarar övriga bankobjekt',()=>{
 const report=JSON.parse(fs.readFileSync(__dirname+'/../agent/FELRAPPORTER_2026-10-19_2044.json','utf8'));
 assert.equal(report.reviewed.length,23);assert.equal(report.changes.length,18);assert.equal(report.unchanged.length,5);
 // Bokstavsuppgifter som gjordes till flervalskort 2026-10-24 (agent/FLERVAL_BOKSTAVSUPPGIFTER_2026-10-24.md)
 // jämförs utan de fält som omvandlingen ändrade.
 const FLERVAL=['t','s','svarstyp','rättSvar','tolerans','alternativ','svarFormat','svarEnhet','svarVardesiffror'];
 const utan=o=>Object.fromEntries(Object.entries(o).filter(([k])=>!FLERVAL.includes(k)));
 for(const item of report.changes){const t=q(item.id);if(t.svarstyp==='alternativ'&&item.after.svarstyp!=='alternativ')assert.deepEqual(utan(t),utan(item.after),item.id);else assert.deepEqual(t,item.after,item.id);}
 for(const id of report.reviewed){const t=q(id);assert.ok(!t.geogebra||t.miniräknare,id);
  for(const p of t.spelDelar||[])assert.ok(!(p.geogebra??t.geogebra)||(p.miniräknare??t.miniräknare),id);
 }
});
