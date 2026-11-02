const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('fs'),vm=require('vm'),path=require('path');
const c={window:{}};vm.runInNewContext(fs.readFileSync(path.join(__dirname,'../uppgiftermato1.js'),'utf8'),c);const bank=JSON.parse(JSON.stringify(c.window.BANKMATO1));const q=id=>{const t=bank.find(x=>x.id===id);assert.ok(t,id);return t};
test('Endast den verkliga nollaxeln är mörk och x-beteckningar följer den',()=>{
 for(const [id,y] of [['3.1201','200.667'],['3.1202','76.0'],['3.1203','89.6'],['3.1204','161.0'],['3.1205','200.667']]){
  const t=q(id).t;assert.doesNotMatch(t,/M60 280L443 280/);assert.ok(t.includes(`M60 ${y}L443 ${y}`),id);assert.match(t,/<text x="449"[^>]*>x<\/text>/,id);
  const labels=[...t.matchAll(/<text x="[\d.]+" y="([\d.]+)" font-family="Arial,sans-serif" font-size="16" text-anchor="middle" fill="#243447">[-\d]+<\/text>/g)];assert.equal(labels.length,5,id);assert.ok(labels.every(m=>Math.abs(+m[1]-Number(y)-21)<.002),id);
 }assert.match(q('3.1206').t,/M60 280L443 280/);
});
test('Avrundningsbara längder använder exakta beräkningsvärden och måttenhet',()=>{
 const cases={'4.104':6*Math.sin(68*Math.PI/180),'4.102':30*Math.tan(38*Math.PI/180),'4.114':120*Math.sin(35*Math.PI/180),'4.118':18*Math.sin(52*Math.PI/180)+1.5};
 for(const [id,v] of Object.entries(cases)){const t=q(id);assert.ok(Math.abs(t.rättSvar-v)<1e-12,id);assert.equal(t.svarFormat,'numeriskt');assert.equal(t.svarEnhet,'m');assert.equal(t.miniräknare,true);assert.equal(t.geogebra,false);}
});
test('Transformerad derivatagraf är nivå 4 och kräver en decimal',()=>{const t=q('3.1233');assert.equal(t.traningsniva,4);assert.equal(t.rättSvar,4.5);assert.match(t.t,/en decimal/);assert.equal(t.miniräknare,true);assert.equal(t.geogebra,false)});

test('Uttryckligt en decimal rättas till ett avrundat svar utan bred tolerans',()=>{for(const [id,v] of [['4.485',34],['4.486',16.3]]){const t=q(id);assert.equal(t.rättSvar,v,id);assert.equal(t.tolerans,0,id);assert.equal(t.svarFormat,'numeriskt',id);assert.match(t.t,/en decimal/i,id);}});
