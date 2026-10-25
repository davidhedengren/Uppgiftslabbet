'use strict';
/* Ma2 kap 4 statistik, omgång S1 2026-10-25: 61 problemlösnings- och textkort 4.2000–4.2060 på nivå 1–3
   (tabeller och diagram, lägesmått, kvartiler, lådagram, normalfördelning, korrelation och regression). */
const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('node:fs'),vm=require('node:vm'),path=require('node:path');
const c={window:{}};vm.runInNewContext(fs.readFileSync(path.join(__dirname,'..','uppgifterma2.js'),'utf8'),c);
const B=JSON.parse(JSON.stringify(c.window.BANKMA2));const get=id=>{const t=B.find(x=>x.id===id);assert.ok(t,id);return t;};
const NYA=Array.from({length:61},(_,i)=>`4.${2000+i}`);
const s=id=>get(id).rättSvar;
const median=a=>{const v=[...a].sort((x,y)=>x-y),n=v.length;return n%2?v[(n-1)/2]:(v[n/2-1]+v[n/2])/2;};
const kv=a=>{const v=[...a].sort((x,y)=>x-y),h=Math.floor(v.length/2);return [median(v.slice(0,h)),median(v),median(v.slice(v.length-h))];};

test('61 kort i kap 4 med nivå 1–3 och rätt kursspår',()=>{
  const per={},niv={1:0,2:0,3:0};
  for(const id of NYA){const t=get(id);per[t.omr]=(per[t.omr]||0)+1;niv[t.traningsniva]++;assert.equal(t.kap,4,id);assert.equal(t.spel,true,id);
    assert.deepEqual(t.kurs,['korrelation_koefficient','linjar_regression'].includes(t.omr)?['2b','2c']:['2a','2b','2c'],id);
    if(t.traningsniva===3){assert.equal(t.niva,'C',id);assert.equal(t.poang,'0/1/0',id);}}
  assert.deepEqual(per,{tabeller_diagram:12,lagesmatt:11,kvartiler_percentiler:9,ladagram:10,normalfordelat_material:10,korrelation_koefficient:4,linjar_regression:5});
  assert.deepEqual(niv,{1:19,2:31,3:11});
  assert.equal(new Set(B.map(x=>x.id)).size,B.length,'dubblerade ID:n');
});

test('Inget nytt kort delar facit med ett annat kort i samma område',()=>{
  const v=x=>{const r=x.rättSvar,t=(Array.isArray(r)?JSON.stringify(r):String(r)).replace(/\s/g,''),n=Number(t);return isNaN(n)?t:String(Math.round(n*1e6)/1e6);};
  for(const id of NYA){const t=get(id);if(t.svarstyp==='alternativ')continue;
    const krock=B.filter(u=>u.omr===t.omr&&u.id!==id&&u.svarstyp!=='alternativ'&&u.rättSvar!=null&&v(u)===v(t)).map(u=>u.id);
    assert.deepEqual(krock,[],`${id} har samma facit som ${krock}`);}
});

test('Facit räknas om',()=>{
  assert.equal(s('4.2000'),420);assert.equal(s('4.2001'),Math.round((500/450-1)*1000)/10);assert.equal(s('4.2003'),72/360*600);
  assert.equal(s('4.2005'),2023);assert.equal(s('4.2006'),0.25*640-0.4*300);assert.ok(Math.abs(s('4.2008')-(0.45*0.6+0.55*0.4)*100)<1e-9);
  assert.equal(s('4.2009'),Math.round(14/30*1000)/10);assert.ok(Math.abs(s('4.2010')-7.2)<1e-12);assert.equal(s('4.2011'),25);
  assert.equal(s('4.2013'),6*8-5*7);assert.equal(s('4.2014'),(24*62+16*72)/40);assert.equal(s('4.2016'),37/20);
  assert.equal(s('4.2017'),(4+7+11+15)/4);assert.ok(Math.abs(s('4.2019')-(25*168-30)/25)<1e-9);assert.equal(s('4.2021'),400-316);assert.equal(s('4.2022'),11);
  assert.equal(s('4.2023'),kv([3,5,6,8,9,12,14,15,20,26])[0]);assert.equal(s('4.2024'),28);assert.deepEqual(s('4.2027'),[24,25]);
  const [q1,,q3]=kv([62,64,68,70,71,75,78,80,84,90]);assert.equal(s('4.2028'),q3-q1);assert.equal(s('4.2030'),120);
  assert.deepEqual(s('4.2036'),[2,8]);assert.deepEqual(kv([2,4,5,6,6,7,7,8,9,9,10,11,12,12,14,15]),[6,8.5,11.5]);
  const lang=[3.1,3.4,3.5,3.8,3.9,4.0,4.2,4.4,4.5,4.7,4.9,5.3],k=kv(lang);s('4.2038').forEach((x,i)=>assert.ok(Math.abs(x-[3.1,...k,5.3][i])<1e-9,'4.2038'));
  for(const a of get('4.2040').alternativ){const v=a.txt.split(',').map(Number),[a1,a2,a3]=kv(v);assert.equal(Math.min(...v)===2&&a1===4&&a2===5.5&&a3===8&&Math.max(...v)===10,a.ratt,a.txt);}
  assert.ok(Math.abs(s('4.2042')-0.682*2500)<1);assert.deepEqual(s('4.2043'),[165,193]);assert.equal(s('4.2046'),7);assert.ok(Math.abs(s('4.2047')-83.9)<1e-9);
  assert.ok(Math.abs(s('4.2049')-0.33)<1e-12);assert.equal(s('4.2051'),5);assert.equal(s('4.2056'),39);assert.ok(Math.abs(s('4.2058')-3.2)<1e-9);assert.equal(s('4.2059'),10);
});

test('Precision anges där ett avrundat heltal annars skulle godtas',()=>{
  for(const id of ['4.2010','4.2016','4.2017','4.2019','4.2049','4.2058'])assert.match(get(id).t,/decimal/,id);
});

test('Flerval: rätt alternativ står inte först och antalet rätta stämmer',()=>{
  for(const id of NYA.filter(id=>get(id).svarstyp==='alternativ')){const a=get(id).alternativ,r=a.filter(x=>x.ratt).length;
    assert.ok(r>=1&&a.length-r>=2,id);if(r===1)assert.equal(a[0].ratt,false,id);}
  assert.equal(get('4.2035').alternativ.filter(a=>a.ratt).length,3);
});

test('Figurer har bredd och beskrivning',()=>{
  const fig=NYA.filter(id=>/<svg/.test(get(id).t));assert.equal(fig.length,15);
  for(const id of fig)for(const svg of get(id).t.match(/<svg[^>]*>/g)){assert.match(svg,/max-width:\d+px/,id);assert.match(svg,/aria-label="[^"]{15,}"/,id);}
});
