'use strict';
/* Ma2 kap 3 geometri, omgång S2 2026-10-25: 53 problemlösnings- och textkort 3.2000–3.2052 på nivå 1–3
   (Pythagoras, likformighet, topptriangel- och transversalsatsen, kordor, randvinklar, avstånd, koordinatgeometri, problemlösning). */
const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('node:fs'),vm=require('node:vm'),path=require('node:path');
const c={window:{}};vm.runInNewContext(fs.readFileSync(path.join(__dirname,'..','uppgifterma2.js'),'utf8'),c);
const B=JSON.parse(JSON.stringify(c.window.BANKMA2));const get=id=>{const t=B.find(x=>x.id===id);assert.ok(t,id);return t;};
const NYA=Array.from({length:53},(_,i)=>`3.${2000+i}`);
const s=id=>get(id).rättSvar,nara=(a,b,t=1e-9)=>Math.abs(a-b)<=t;

test('53 kort i kap 3 med nivå 1–3 och rätt kursspår',()=>{
  const per={},niv={1:0,2:0,3:0},alla=['pythagoras','avstandsformeln_mittpunktsformeln','koordinatgeometri_problemlosning'];
  for(const id of NYA){const t=get(id);per[t.omr]=(per[t.omr]||0)+1;niv[t.traningsniva]++;assert.equal(t.kap,3,id);assert.equal(t.spel,true,id);
    assert.deepEqual(t.kurs,alla.includes(t.omr)?['2a','2b','2c']:['2b','2c'],id);if(t.traningsniva===3){assert.equal(t.niva,'C',id);assert.equal(t.poang,'0/1/0',id);}}
  assert.deepEqual(per,{pythagoras:9,likformighet:8,topptriangel_transversal:6,kordasatsen_biskarningssatsen:6,randvinkel_medelpunkt:6,avstandsformeln_mittpunktsformeln:6,koordinatgeometri_problemlosning:6,geometri_problemlosning:6});
  assert.deepEqual(niv,{1:14,2:21,3:18});
  assert.equal(new Set(B.map(x=>x.id)).size,B.length,'dubblerade ID:n');
});

test('Inget nytt kort delar facit med ett annat kort i samma område',()=>{
  const v=x=>{const r=x.rättSvar,t=(Array.isArray(r)?JSON.stringify(r):String(r)).replace(/\s/g,''),n=Number(t);return isNaN(n)?t:String(Math.round(n*1e6)/1e6);};
  for(const id of NYA){const t=get(id);if(t.svarstyp==='alternativ')continue;
    const krock=B.filter(u=>u.omr===t.omr&&u.id!==id&&u.svarstyp!=='alternativ'&&u.rättSvar!=null&&v(u)===v(t)).map(u=>u.id);
    assert.deepEqual(krock,[],`${id} har samma facit som ${krock}`);}
});

test('Facit räknas om',()=>{
  assert.ok(nara(s('3.2000'),Math.sqrt(25-1.96),1e-12));assert.ok(nara(s('3.2001'),Math.hypot(2.4,7),1e-12));assert.equal(s('3.2002'),Math.round(16*Math.sqrt(3025/337)*10)/10);
  assert.equal(s('3.2004'),Math.round(Math.hypot(4,3,2.5)*100)/100);assert.equal(s('3.2005'),48);assert.equal(s('3.2007'),Math.sqrt(196));
  assert.ok(nara(s('3.2009'),11*1.2/1.5,1e-12));assert.ok(nara(s('3.2010'),8*25000**2/1e10,1e-12));assert.equal(s('3.2011'),8*13.5/6);assert.equal(s('3.2012'),25);
  assert.ok(nara(s('3.2013'),14*1.6/2,1e-12));assert.ok(nara(s('3.2014'),90*1.5**2,1e-12));assert.ok(nara(s('3.2016'),4.4*2.5,1e-12));
  assert.equal(s('3.2017'),7*10/4);assert.equal(s('3.2018'),7.5*4/6);assert.ok(nara(s('3.2019'),1.8*8.1/2.7,1e-12));assert.ok(nara(s('3.2020'),8*1.8/3,1e-12));assert.equal(s('3.2021'),2);
  assert.equal(s('3.2023'),7*9/6);assert.equal(s('3.2024'),(64+4)/4);assert.equal(s('3.2025'),15);assert.equal(s('3.2026'),11);assert.equal(11*16,8*22);
  assert.equal(s('3.2027'),12.5*12/20);assert.ok(nara(s('3.2028'),4*4.5/4.8,1e-12));
  assert.equal(s('3.2029'),65);assert.equal(s('3.2030'),55);assert.equal(s('3.2031'),11);assert.equal(s('3.2032'),76);assert.equal(s('3.2033'),58);assert.equal(s('3.2034'),12);
  assert.equal(s('3.2035'),3);assert.deepEqual(s('3.2037'),[2,0,5]);assert.deepEqual(s('3.2038'),[9,-1]);assert.equal(s('3.2039'),25);assert.deepEqual(s('3.2040'),[-1,5]);
  assert.equal(s('3.2041'),27);assert.deepEqual(s('3.2042'),[3,5]);assert.equal(s('3.2043'),13.5);assert.equal(s('3.2044'),28);assert.equal(s('3.2045'),22);assert.equal(s('3.2046'),9);
  assert.equal(s('3.2047'),36);assert.equal(s('3.2048'),Math.round((Math.SQRT2-1)*1000)/100);assert.equal(s('3.2049'),Math.round((64-16*Math.PI)*10)/10);assert.equal(s('3.2050'),200);assert.equal(s('3.2051'),26);
});

test('Exakta decimalsvar kräver exakthet i frågan',()=>{
  for(const id of ['3.2017','3.2023','3.2027','3.2028','3.2043'])assert.match(get(id).t,/exakt/,id);
});

test('Flerval och figurer',()=>{
  for(const id of NYA.filter(id=>get(id).svarstyp==='alternativ')){const a=get(id).alternativ,r=a.filter(x=>x.ratt).length;assert.ok(r>=1&&a.length-r>=2,id);if(r===1)assert.equal(a[0].ratt,false,id);}
  const fig=NYA.filter(id=>/<svg/.test(get(id).t));assert.equal(fig.length,29);
  for(const id of fig)for(const svg of get(id).t.match(/<svg[^>]*>/g)){assert.match(svg,/max-width:\d+px/,id);assert.match(svg,/aria-label="[^"]{20,}"/,id);}
  // cirklar ritas ofyllda
  for(const id of fig)for(const c of get(id).t.match(/<circle[^>]*r="(?:[2-9]\d|\d{3})[^>]*>/g)||[])assert.match(c,/fill="none"/,id);
});
