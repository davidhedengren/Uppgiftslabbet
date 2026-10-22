'use strict';
const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('node:fs'),vm=require('node:vm'),path=require('node:path');
const c={window:{}};vm.runInNewContext(fs.readFileSync(path.join(__dirname,'..','uppgifterma2.js'),'utf8'),c);
const get=id=>c.window.BANKMA2.find(t=>t.id===id&&t.omr==='standardavvikelse');
const IDS=Array.from({length:15},(_,i)=>`4.${450+i}`);
const medel=v=>v.reduce((a,b)=>a+b,0)/v.length;
const Sx=v=>{const m=medel(v);return Math.sqrt(v.reduce((a,x)=>a+(x-m)**2,0)/(v.length-1));};
const nara=(a,b)=>assert.ok(Math.abs(a-b)<1e-6,`${a} != ${b}`);
const tabellTal=t=>[...t.matchAll(/<td>(-?[\d,]+)<\/td>/g)].map(m=>Number(m[1].replace(',','.')));

test('15 nya uppgifter i standardavvikelse med Sx-regel och verktyg',()=>{
  for(const id of IDS){
    const t=get(id);assert.ok(t,id);
    assert.deepEqual([...t.kurs],['2a','2b','2c']);
    if(t.svarstyp==='alternativ'){assert.equal(t.alternativ.filter(a=>a.ratt).length,1,id);continue;}
    /* Beräkning av standardavvikelse: Sx står i frågan och både GeoGebra och miniräknare är tillåtna. */
    assert.match(t.t,/Sx|S_x/,id);assert.equal(t.geogebra,true,id);assert.equal(t.miniräknare,true,id);
  }
  const ber=IDS.filter(id=>get(id).svarstyp!=='alternativ');
  assert.equal(ber.length,10);assert.equal(IDS.length-ber.length,5);
});

test('Varje Sx-facit stämmer med datan som visas i uppgiften',()=>{
  nara(get('4.450').rättSvar,Sx([4,6,8]));
  nara(get('4.451').rättSvar,Sx([2,3,3,4,4,4,5,7]));
  const steg=tabellTal(get('4.452').t);nara(get('4.452').rättSvar,Sx(steg));
  const sko=tabellTal(get('4.453').t);const v=[];for(let i=0;i<sko.length;i+=2)for(let k=0;k<sko[i+1];k++)v.push(sko[i]);
  assert.equal(v.length,15);nara(get('4.453').rättSvar,Sx(v));
  const [sA,sB]=get('4.454').rättSvar;nara(sA,Sx([9,8,10,9,7,9]));nara(sB,Sx([10,6,10,9,7,10]));
  nara(medel([9,8,10,9,7,9]),medel([10,6,10,9,7,10]));
  nara(get('4.455').rättSvar,Sx([0,0,0,0,1,1,1,1,1,1,2,2,2,3,4]));
  const d=[12.4,13.1,11.8,12.9,13.5,12.2].map((x,i)=>x-[12.0,12.4,11.6,12.1,12.6,12.0][i]);nara(get('4.456').rättSvar,Sx(d));
  assert.deepEqual([...get('4.457').rättSvar],[13,4]);nara(Sx([5,9,13]),4);
  nara(Sx([2,4,get('4.458').rättSvar]),4);
  const agg=(get('4.459').t.match(/var ([\d, och]+)\./)[1]).split(/, | och /).map(Number);
  assert.equal(agg.length,8);nara(get('4.459').rättSvar[0],medel(agg));nara(get('4.459').rättSvar[1],Sx(agg));
});

test('Inget avrundat facit ligger nära en avrundningsgräns',()=>{
  for(const id of IDS){
    const t=get(id);const r=[].concat(t.rättSvar),tol=[].concat(t.tolerans);
    r.forEach((v,i)=>{const d={0.005:2,0.05:1}[tol[i]];if(typeof v!=='number'||d==null)return;
      const rest=Math.abs(v*10**d)%1;assert.ok(Math.abs(rest-0.5)>0.1,`${id}: ${v}`);});
  }
});

test('Flervalsfrågorna prövar innebörden, inte variationsbredd eller lägesmått',()=>{
  assert.match(get('4.460').alternativ.find(a=>a.ratt).txt,/medelvärdet/);
  assert.match(get('4.461').t,/samma variationsbredd/);
  assert.match(get('4.462').alternativ.find(a=>a.ratt).txt,/alla värden/);
  assert.match(get('4.463').alternativ.find(a=>a.ratt).txt,/n − 1/);
});
