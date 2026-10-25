'use strict';
/* Fy2 2026-10-25: 29 kort på nivå 2–3 i kosmologi, exoplaneter, stjärnornas utveckling, avståndsmätning och magnituder
   (5.464–5.486) samt jordens magnetfält (3.538–3.543). Enligt nivåinventeringen hade kosmologi 1 kort på nivå 3,
   jordens magnetfält 3 och exoplaneter 4. Facit räknas om; svar som beror på solens värden godtar T☉ 5 772–5 800 K. */
const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('node:fs'),vm=require('node:vm'),path=require('node:path');
const c={window:{}};vm.runInNewContext(fs.readFileSync(path.join(__dirname,'..','uppgifter2.js'),'utf8'),c);
const B=JSON.parse(JSON.stringify(Object.values(c.window).find(Array.isArray)));const get=id=>{const t=B.find(x=>x.id===id);assert.ok(t,id);return t;};
const NYA=[...Array.from({length:23},(_,i)=>`5.${464+i}`),...Array.from({length:6},(_,i)=>`3.${538+i}`)];
const n=(id,...x)=>{const t=get(id),r=Array.isArray(t.rättSvar)?t.rättSvar:[t.rättSvar],tol=Array.isArray(t.tolerans)?t.tolerans:[t.tolerans];assert.equal(r.length,x.length,id);
  x.forEach((v,i)=>assert.ok(Math.abs(r[i]-v)<=(tol[i]||0)+1e-9*Math.abs(v),`${id}[${i}]: ${r[i]} ≠ ${v}`));};
const lg=Math.log10,AU=1.496e11,PC=3.086e16,deg=Math.PI/180;

test('29 spelbara kort på nivå 2–3, fysikformat och inga dubblettfacit',()=>{
  const per={},niv={2:0,3:0};
  for(const id of NYA){const t=get(id);per[t.omr]=(per[t.omr]||0)+1;niv[t.traningsniva]++;assert.equal(t.spel,true,id);
    assert.equal(t.poang,t.traningsniva===3?'(0/1/0)':'(1/0/0)',id);assert.doesNotMatch(t.t+t.s,/\bAE\b|bolometrisk/,id);
    if(t.svarstyp==='alternativ'){assert.equal(t.alternativ.filter(a=>a.ratt).length,1,id);assert.ok(!t.alternativ[0].ratt,id);}}
  assert.deepEqual(per,{kosmologi:6,exoplaneter:6,stjarnornas_utveckling:3,avstandsmatning:4,magnituder:4,jordens_magnetfalt:6});
  assert.deepEqual(niv,{2:7,3:22});
  const v=x=>JSON.stringify(x.rättSvar);
  for(const id of NYA){const t=get(id);if(t.rättSvar==null)continue;
    const krock=B.filter(w=>w.omr===t.omr&&w.id!==id&&w.rättSvar!=null&&v(w)===v(t)).map(w=>w.id);assert.deepEqual(krock,[],`${id}: ${krock}`);}
  // inga solvärden i frågorna om stjärnorna
  for(const id of ['5.476','5.477','5.478'])assert.doesNotMatch(get(id).t,/5\s?7[78]\d|3,8\d·10|6,96|1,99/,id);
});

test('Facit räknas om',()=>{
  n('5.464',17000/250);n('5.465',0.035*3e5/70);const z=(682.5-656.3)/656.3;n('5.466',z,z*2.998e5,z*2.998e5/70);n('5.467',1/0.8-1,500/0.8);
  n('5.469',1.5e9/3.2616/1e6,70*1.5e9/3.2616/1e6);
  n('3.538',Math.round(Math.atan(48/16)/deg));n('3.539',15e-6*Math.tan(25*deg)*2*Math.PI*0.05/(4e-7*Math.PI));n('3.540',45e-6*800*250);
  n('3.541',48e-6*30*1.6*1000);n('3.543',1.6726e-27*4e5/(1.602e-19*30e-6));
  n('5.470',0.13**2*100);n('5.471',Math.sqrt(0.5**3/0.8)*365.25);n('5.472',16-4,Math.sqrt(0.01)*0.95*109.1);n('5.473',Math.cbrt(0.95*(12/365.25)**2));
  n('5.474',4.2,2*Math.PI*0.05*AU/(4.2*86400)/1000);
  for(const Ts of [5772,5800]){const T=2.898e-3/725e-9;n('5.476',Math.sqrt(0.15)*(Ts/T)**2);n('5.478',Math.sqrt(1e5)*(Ts/3600)**2,Math.sqrt(1e5)*(Ts/3600)**2*6.957e8/AU);}
  for(const L of [3.828e26,3.846e26])n('5.477',L/2.998e8**2,L/2.998e8**2*1e10*3.156e7/1.989e30*100);
  n('5.479',1/4.4e-3,1/3.6e-3);n('5.480',25e6*(3/60)*deg/1000);n('5.481',1.392e9/(1.52*AU)/deg);n('5.482',3.2616/0.768,PC/0.768/17e3/3.156e7);
  n('5.483',-2.5*lg(10**-0.8+10**-1.2));n('5.484',50*10**(-2.2/5));n('5.485',5*lg(4),16);
  const d=10**((16.2+19.3+5)/5)/1e6;n('5.486',d,70*d);
});
