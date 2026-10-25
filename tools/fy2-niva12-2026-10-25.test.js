'use strict';
/* Fy2 2026-10-25: 48 kort på nivå 1–2 utanför astronomin, i de sex tunnaste områdena enligt appens nivåräkning:
   växelström med spole och kondensator, kast i elfält och elektriska fält (3.544–3.567) samt de Broglie, atomstruktur
   och EM-vågor (4.518–4.541). Facit räknas om och facitkraven (metodtext, svarsrad, inga råa < >) kontrolleras. */
const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('node:fs'),vm=require('node:vm'),path=require('node:path');
const c={window:{}};vm.runInNewContext(fs.readFileSync(path.join(__dirname,'..','uppgifter2.js'),'utf8'),c);
const B=JSON.parse(JSON.stringify(Object.values(c.window).find(Array.isArray)));const get=id=>{const t=B.find(x=>x.id===id);assert.ok(t,id);return t;};
const NYA=[...Array.from({length:24},(_,i)=>`3.${544+i}`),...Array.from({length:24},(_,i)=>`4.${518+i}`)];
const h=6.626e-34,e=1.602e-19,me=9.109e-31,mp=1.673e-27,mn=1.675e-27,k=8.99e9,cl=2.998e8;
const n=(id,v)=>{const t=get(id);assert.ok(Math.abs(t.rättSvar-v)<=(t.tolerans||0)+1e-9*Math.abs(v),`${id}: ${t.rättSvar} ≠ ${v}`);};

test('48 spelbara kort på nivå 1–2 med facitkraven uppfyllda',()=>{
  const per={},niv={1:0,2:0};
  for(const id of NYA){const t=get(id);per[t.omr]=(per[t.omr]||0)+1;niv[t.traningsniva]++;assert.equal(t.spel,true,id);assert.equal(t.poang,'(1/0/0)',id);assert.equal(t.niva,'E',id);
    assert.match(t.s,/class="facit-metod"/,id);assert.match(t.s,/class="facit-svar"/,id);
    for(const m of (t.t+t.s+t.ledtrad).matchAll(/\\\(([\s\S]*?)\\\)|\\\[([\s\S]*?)\\\]/g))assert.doesNotMatch(m[1]??m[2],/[<>]/,id);
    if(t.svarstyp==='alternativ'){assert.equal(t.alternativ.filter(a=>a.ratt).length,1,id);assert.ok(!t.alternativ[0].ratt,id);for(const a of t.alternativ)if(!a.ratt)assert.ok(a.kommentar,id);}
    else assert.match(t.t,/\(Svara[^)]*\)/,id);}
  assert.deepEqual(per,{vaxelstrom_spole_kondensator:8,kast_elfalt:8,elektriska_falt:8,de_broglie:8,atomstruktur:8,em_vagor:8});
  assert.deepEqual(niv,{1:25,2:23});
  const v=x=>JSON.stringify(x.rättSvar);
  for(const id of NYA){const t=get(id);if(t.rättSvar==null)continue;
    const krock=B.filter(w=>w.omr===t.omr&&w.id!==id&&w.rättSvar!=null&&v(w)===v(t)).map(w=>w.id);assert.deepEqual(krock,[],`${id}: ${krock}`);}
});

test('Facit räknas om',()=>{
  n('3.544',12/40);n('3.545',100);n('3.546',90);n('3.547',314/(2*Math.PI*50));n('3.548',1/(2*Math.PI*1000*100)*1e6);n('3.549',1/((2*Math.PI*1000)**2*0.05)*1e6);
  n('3.552',200);n('3.553',e*1500);n('3.554',Math.sqrt(2*e*1500/me));n('3.555',e*2e3/me);n('3.556',0.05/2e7);n('3.557',4e14*(2.5e-9)**2/2*1000);n('3.559',10);
  n('3.560',6e-5/3e-9);n('3.561',k*5e-9/0.01);n('3.563',800/4);n('3.564',Math.sqrt(k*4e-12/3.6)*100);n('3.565',5e-6*120*1000);n('3.566',500*0.08);n('3.567',e*2e4/mp);
  n('4.518',h/(mp*1e5));n('4.519',h/2e-24);n('4.521',h/(mn*0.2e-9));n('4.522',h/Math.sqrt(2*me*e*100)*1e9);n('4.523',h/(me*530e-9));n('4.524',h**2/(2*me*(0.2e-9)**2)/e);
  n('4.526',1.51-0.85);n('4.527',3);n('4.528',h*cl/((13.6/4-13.6/25)*e)*1e9);n('4.530',1.51*e/h);n('4.531',-13.6/36);
  assert.equal(Math.round(Math.sqrt(13.6/(13.6-13.06))),5);n('4.532',5);n('4.533',h*6.2e14);
  n('4.534',cl*2e-3/2/1000);n('4.536',20200e3/cl*1000);n('4.537',h*cl/0.1e-9/e/1000);n('4.538',cl/1.5);n('4.539',600/1.5);n('4.540',9);n('4.541',cl/900e6/4*100);
});
