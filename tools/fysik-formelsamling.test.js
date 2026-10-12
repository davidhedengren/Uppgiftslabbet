'use strict';
const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('node:fs'),vm=require('node:vm'),path=require('node:path');
function bank(file){const c={window:{}};vm.runInNewContext(fs.readFileSync(path.join(__dirname,'..',file),'utf8'),c);return Object.values(c.window).find(Array.isArray);}
const fy1=bank('uppgifter.js'),fy2=bank('uppgifter2.js'),q=id=>fy1.find(q=>q.id===id);
function texts(q){return [q.t,q.spelIntro,...(q.spelDelar||[]).flatMap(p=>[p.t,p.fraga])].filter(x=>typeof x==='string');}
test('Båda fysikbankernas frågor och delkort saknar standardkonstanter och färdiga formeluppmaningar',()=>{
 for(const [course,items]of [['fy1',fy1],['fy2',fy2]])for(const task of items)for(const html of texts(task)){
  const text=html.replace(/<svg[\s\S]*?<\/svg>|<img[^>]*>/g,'');
  assert.doesNotMatch(text,/(?:använd|räkna med)[^<>.]{0,150}\b[gG]\s*=\s*9[.,]/i,course+' '+task.id);
  assert.doesNotMatch(text,/\banvänd\b[^<>]{0,150}(?:Coulombs konstant|Plancks konstant|\\\\?\([FEPWIU]=|\b[FPWIU]\s*=)/i,course+' '+task.id);
  assert.doesNotMatch(text,/(?:Coulombs|Plancks|Boltzmanns|Avogadros|gravitations)konstant(?:en)?[^<>]{0,130}\d/i,course+' '+task.id);
 }
});
test('Givna modellvärden, riktningar, sträckor och experimentdata finns kvar',()=>{
 assert.match(q('4.323').t,/k = 80 N\/m/);assert.match(q('4.350').t,/g = 5,7/);
 assert.match(q('4.53').t,/Uppåt är positiv riktning/);assert.match(q('4.392').t,/Nedför är positiv/);
 assert.match(q('4.378').t,/6370 km/);assert.match(q('4.9').t,/4,0 · 10²⁴ kg/);
 assert.match(q('4.19').t,/Bortse från energiförluster/);
 assert.match(q('9.71').t,/2,014102 u/);assert.match(q('9.71').t,/4,002603 u/);
 assert.match(q('4.368').t,/En elev skriver g = 9,82/); // själva felsökningsexemplet, inte en ledning
 assert.match(fy2.find(q=>q.id==='2.503').t,/9\{,\}788/); // lokala g-värden är själva jämförelsens data
 for(const id of ['8.22','9.12','6.347'])for(const t of texts(q(id)))assert.doesNotMatch(t,/6\{,\}674|8\{,\}99|R=8,31|Använd/);
});
test('Avgränsade alternativa tabellfacit följer oberoende fysikmodeller utan att ändra originalmålen',()=>{
 const cases=[['2.29',4,5e6*1.60e-19*1e12],['4.74',1,6.67e-11*5.97e24*1200/(6.771e6)**2/1000],
 ['4.74',2,6.67e-11*5.97e24*1200/(6.371e6)**2/1000],['4.740',0,6.674e-11*5.97e24*78/(6.732e6)**2],
 ['4.742',0,6.674e-11*7.35e22/(1.737e6)**2],['4.742',3,6.674e-11*1.9e27/(6.99e7)**2],
 ['5.498',2,Math.ceil(280*4184*.2/(20*.45))],['2.29',0,2000*4186],['2.29',1,2000*4186/3.6e6],['2.32',3,1.5*735.5],['2.33',5,500*4186],['5.562',1,18*735/(95/3.6)]];
 for(const[id,i,value]of cases){const alias=q(id).svarTabell[i][0];assert.ok(Math.abs(alias-value)<=Math.abs(value)*1e-13,id);}
 assert.equal(q('2.29').rättSvar[4],.801);assert.equal(q('5.498').rättSvar[2],26047);
 assert.equal(q('2.29').tolerans[4],0);assert.equal(q('5.498').tolerans[2],0);
 assert.equal(q('4.74').tolerans[1],.005);assert.equal(q('4.740').tolerans,.5);
 for(const task of fy1.filter(q=>q.svarTabell))for(const [i,values]of Object.entries(task.svarTabell)){
  const target=Array.isArray(task.rättSvar)?task.rättSvar[+i]:task.rättSvar;
  assert.equal(typeof target,'number');assert.ok(values.every(v=>typeof v==='number'&&Number.isFinite(v)));
 }
});
