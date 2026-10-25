'use strict';
/* Ma2 kap 3–4, omgång S6 2026-10-25: 49 text- och problemlösningskort på nivå 1–3
   (3.2122–3.2161: sats och bevis, randvinklar, topptriangel/transversal, Pythagoras, geometrisk problemlösning;
    4.2139–4.2147: lådagram). */
const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('node:fs'),vm=require('node:vm'),path=require('node:path');
const c={window:{}};vm.runInNewContext(fs.readFileSync(path.join(__dirname,'..','uppgifterma2.js'),'utf8'),c);
const B=JSON.parse(JSON.stringify(c.window.BANKMA2));const get=id=>{const t=B.find(x=>x.id===id);assert.ok(t,id);return t;};
const NYA=[...Array.from({length:40},(_,i)=>`3.${2122+i}`),...Array.from({length:9},(_,i)=>`4.${2139+i}`)];
const s=id=>get(id).rättSvar,nara=(a,b,t)=>Math.abs(a-b)<=t,ratt=id=>get(id).alternativ.filter(a=>a.ratt).map(a=>a.txt);

test('49 kort med nivå 1–3, rätt kapitel och kursspår',()=>{
  const per={},niv={1:0,2:0,3:0};
  for(const id of NYA){const t=get(id);per[t.omr]=(per[t.omr]||0)+1;niv[t.traningsniva]++;assert.equal(t.kap,t.omr==='ladagram'?4:3,id);assert.equal(t.spel,true,id);assert.equal(t.geogebra,false,id);
    assert.deepEqual(t.kurs,['pythagoras','ladagram'].includes(t.omr)?['2a','2b','2c']:['2b','2c'],id);if(t.traningsniva===3){assert.equal(t.niva,'C',id);assert.equal(t.poang,'0/1/0',id);}}
  assert.deepEqual(per,{sats_bevis:9,randvinkel_medelpunkt:9,topptriangel_transversal:8,pythagoras:8,ladagram:9,geometri_problemlosning:6});
  assert.deepEqual(niv,{1:14,2:25,3:10});
  assert.equal(new Set(B.map(x=>x.id)).size,B.length,'dubblerade ID:n');
});

test('Inget nytt kort delar facit med ett annat kort i samma område',()=>{
  const v=x=>{const r=x.rättSvar,t=(Array.isArray(r)?JSON.stringify(r):String(r)).replace(/\s/g,''),n=Number(t);return isNaN(n)?t:String(Math.round(n*1e6)/1e6);};
  for(const id of NYA){const t=get(id);if(t.svarstyp==='alternativ')continue;
    const krock=B.filter(u=>u.omr===t.omr&&u.id!==id&&u.svarstyp!=='alternativ'&&u.rättSvar!=null&&v(u)===v(t)).map(u=>u.id);
    assert.deepEqual(krock,[],`${id} har samma facit som ${krock}`);}
});

test('Sats och bevis: rätt alternativ',()=>{
  assert.deepEqual(ratt('3.2122'),['2']);assert.match(ratt('3.2123')[0],/Om gatan är blöt, så regnar det/);assert.match(ratt('3.2124')[0],/drake/);
  assert.match(ratt('3.2125')[0],/3\(n \+ 1\)/);assert.match(ratt('3.2126')[0],/2\(m \+ n \+ 1\)/);assert.deepEqual(ratt('3.2127'),['Nödvändigt men inte tillräckligt']);
  assert.equal(s('3.2128'),720);assert.match(ratt('3.2129')[0],/udda, så är n² udda/);assert.match(ratt('3.2130')[0],/a − b, som är 0/);
});

test('Facit räknas om',()=>{
  assert.equal(s('3.2131'),34);assert.equal(s('3.2132'),45);assert.equal(5*s('3.2133')+20,180);assert.equal(s('3.2134'),35);assert.equal(s('3.2136'),130);assert.equal(s('3.2137'),96);assert.equal(s('3.2138'),22.5);assert.equal(s('3.2139'),73);
  assert.equal(s('3.2140'),18);assert.equal(s('3.2141'),6.5);assert.ok(nara(s('3.2142'),3*1.2/8,1e-12));assert.ok(nara(s('3.2143'),7*14/10,1e-12));assert.equal(s('3.2144'),30/8);assert.equal(s('3.2146'),20);assert.equal(s('3.2147'),9*5-4*5);
  assert.equal(s('3.2148'),13);assert.ok(nara(s('3.2149'),2,1e-12));assert.equal(s('3.2150'),3);assert.equal(s('3.2151'),210-150);assert.equal(s('3.2152'),1250);assert.ok(nara(s('3.2153'),Math.sqrt(152),0.005));
  assert.ok(nara(s('3.2154'),Math.sqrt(6371.003**2-6371**2),0.05));assert.ok(nara(s('3.2155'),2*Math.hypot(6,0.5),0.005));
  assert.equal(s('4.2139'),23);assert.equal(s('4.2140'),16);assert.equal(s('4.2141'),20);assert.equal(s('4.2142'),27);assert.equal(s('4.2145'),2.5);assert.equal(s('4.2146'),60);assert.equal(s('4.2147'),52);
  assert.equal(s('3.2156'),96-45);assert.equal(s('3.2157'),150);assert.ok(nara(s('3.2158'),0.6*Math.SQRT2-0.6,0.005));assert.equal(s('3.2159'),60);assert.ok(nara(s('3.2160'),6*Math.PI,0.005));assert.equal(s('3.2161'),98);
  for(const[a,b,c]of[[8,5,5],[10,13,13]])assert.ok(a<b+c&&b<a+c&&c<a+b);
});

test('Figurer: vinkelbågar, områdesregler, precision och flerval',()=>{
  const bagar=id=>(get(id).t.match(/<path d="M [^"]+"/g)||[]).map(p=>{const[,sx,sy,r,ex,ey]=p.match(/M ([\d.-]+) ([\d.-]+) A ([\d.]+) [\d.]+ 0 0 [01] ([\d.-]+) ([\d.-]+)/).map(Number);
    return 2*Math.asin(Math.min(1,Math.hypot(ex-sx,ey-sy)/(2*r)))*180/Math.PI;});
  const forv={'3.2131':[34,34],'3.2132':[45],'3.2133':[96,84],'3.2134':[110,35],'3.2136':[50,130],'3.2137':[48,96],'3.2138':[22.5],'3.2139':[146,73],'3.2157':[150]};
  for(const[id,v]of Object.entries(forv)){const b=bagar(id);assert.equal(b.length,v.length,id);b.forEach((x,i)=>assert.ok(Math.abs(x-v[i])<1,`${id}: ${x} ≠ ${v[i]}`));}
  for(const id of NYA.filter(id=>get(id).omr==='geometri_problemlosning')){assert.match(get(id).t,/<svg/,id);assert.doesNotMatch(get(id).s,/facit-steglista/,id);}
  for(const id of NYA){const t=get(id);if(typeof t.rättSvar==='number'&&!Number.isInteger(t.rättSvar))assert.match(t.t,/decimal|exakt/,id);}
  for(const id of NYA.filter(id=>get(id).svarstyp==='alternativ')){const a=get(id).alternativ,r=a.filter(x=>x.ratt).length;assert.ok(r>=1&&a.length-r>=2,id);if(r===1)assert.equal(a[0].ratt,false,id);}
  const fig=NYA.filter(id=>/<svg/.test(get(id).t));assert.equal(fig.length,36);
  // Lärarbeslut 2026-10-25 (andra beslutet): logik- och begreppskort i sats och bevis har ingen figur.
  // Bara 3.2128 behåller sin figur, eftersom texten beskriver sexhörningens uppdelning i trianglar.
  for(let i=2122;i<=2130;i++)(i===2128?assert.match:assert.doesNotMatch)(get(`3.${i}`).t,/<svg/,`3.${i}`);
  for(const id of fig)for(const svg of get(id).t.match(/<svg[^>]*>/g))assert.match(svg,/aria-label="[^"]{20,}"/,id);
  assert.match(get('3.2154').t,/inte skalenlig/);
});
