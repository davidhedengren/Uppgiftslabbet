const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('fs'),vm=require('vm'),path=require('path');
function load(file,name){const c={window:{}};vm.runInNewContext(fs.readFileSync(path.join(__dirname,'..',file),'utf8'),c);return JSON.parse(JSON.stringify(c.window[name]));}
const ma1=load('uppgifterma1.js','BANKMA1'),ma3=load('uppgiftermato1.js','BANKMATO1');const q=(b,id)=>{const v=b.find(x=>x.id===id);assert.ok(v,id);return v};
test('Riskuppgifter har konkret situation, relevant ledtråd och korrekta medelvärden',()=>{
 let t=q(ma1,'5.272');assert.match(t.t,/komponent/i);assert.doesNotMatch(t.t,/försök|händelse/i);assert.equal(t.rättSvar,24/.03);assert.equal(t.miniräknare,true);
 for(const [id,p,v,result] of [['5.485',.005,80000,400],['5.486',.03,12000,360]]){t=q(ma1,id);assert.equal(t.rättSvar,p*v);assert.equal(t.rättSvar,result);assert.equal(t.svarEnhet,'kr');assert.doesNotMatch(t.ledtrad,/absolut risk|relativ risk/i);assert.match(t.s,/facit-rubrik/);assert.equal(t.geogebra,false);}
 t=q(ma1,'5.490');assert.match(t.t,/oberoende/);assert.match(t.t,/fyra decimaler/);assert.equal(t.rättSvar,.0005);assert.equal(t.tolerans,0);assert.ok(Math.abs((1-(1-1e-6)**500)-.0005)<.00000013);
});
test('Rapporterade svårigheter följer lärarens nivåbedömning',()=>{
 for(const [id,n] of [['3.1227',5],['3.518',4],['2.308',2],['2.1206',4],['2.1233',4]]){const t=q(ma3,id);assert.equal(t.traningsniva,n,id);assert.equal(t.geogebra,false,id);if(id==='2.1206')assert.equal(t.miniräknare,false);}
 assert.match(q(ma3,'2.308').ledtrad,/en gång till/);assert.doesNotMatch(q(ma3,'2.308').ledtrad,/punkt|sätta in/i);assert.match(q(ma3,'3.518').t,/timmar efter att mätningen börjar/);
});
test('Minimi- och maximipunkt används konsekvent utan att ändra rättningssvar',()=>{
 const ids=['3.356','2.602','2.606','2.607','2.610','2.613','2.617','2.622','2.628','2.638','2.639','2.641','2.642','2.665','2.666','2.667','2.672','2.674','2.675','2.676','2.677','2.678','2.679'];
 for(const id of ids){const t=q(ma3,id);assert.doesNotMatch([t.t,t.s,t.ledtrad].join(' '),/\b(?:minpunkt|minpunkten|minpunkter|maxpunkt|maxpunkten|maxpunkter)\b/i,id);}
 assert.equal(q(ma3,'2.674').rättSvar,2);assert.match(q(ma3,'2.674').t,/minimipunkt/);
});
test('Derivatan i 2.302 visas och lagras utvecklad med samma värde som den faktoriserade formen',()=>{
 const t=q(ma3,'2.302');assert.match(t.spelDelar[0].s,/18x\^2-2x/);assert.equal(t.rättSvar[0],"f'(x)=18*x^2-2*x");assert.equal(t.miniräknare,true);assert.equal(t.geogebra,false);
 for(const x of [-3,-.4,0,1,4])assert.ok(Math.abs((18*x*x-2*x)-2*x*(9*x-1))<1e-12);
});
