'use strict';
/* Ma2 kap 3 geometri, omgång S4 2026-10-25: 43 kort 3.2053–3.2095 på nivå 1–3 i yttervinkelsatsen,
   geometriska begrepp och bevis med likformighet. */
const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('node:fs'),vm=require('node:vm'),path=require('node:path');
const c={window:{}};vm.runInNewContext(fs.readFileSync(path.join(__dirname,'..','uppgifterma2.js'),'utf8'),c);
const B=JSON.parse(JSON.stringify(c.window.BANKMA2));const get=id=>{const t=B.find(x=>x.id===id);assert.ok(t,id);return t;};
const NYA=Array.from({length:43},(_,i)=>`3.${2053+i}`);
const s=id=>get(id).rättSvar;

test('43 kort i kap 3 med nivå 1–3 och områdenas kursspår',()=>{
  const per={},niv={1:0,2:0,3:0};
  for(const id of NYA){const t=get(id);per[t.omr]=(per[t.omr]||0)+1;niv[t.traningsniva]++;assert.equal(t.kap,3,id);assert.equal(t.spel,true,id);assert.equal(t.geogebra,false,id);
    assert.deepEqual(t.kurs,t.omr==='yttervinkelsatsen'?['2a','2b','2c']:['2b','2c'],id);if(t.traningsniva===3){assert.equal(t.niva,'C',id);assert.equal(t.poang,'0/1/0',id);}}
  assert.deepEqual(per,{yttervinkelsatsen:15,geometriska_begrepp_definitioner:14,bevis_likformighet:14});
  assert.deepEqual(niv,{1:12,2:24,3:7});
  assert.equal(new Set(B.map(x=>x.id)).size,B.length,'dubblerade ID:n');
});

test('Inget nytt kort delar facit med ett annat kort i samma område',()=>{
  const v=x=>{const r=x.rättSvar,t=(Array.isArray(r)?JSON.stringify(r):String(r)).replace(/\s/g,''),n=Number(t);return isNaN(n)?t:String(Math.round(n*1e6)/1e6);};
  for(const id of NYA){const t=get(id);if(t.svarstyp==='alternativ')continue;
    const krock=B.filter(u=>u.omr===t.omr&&u.id!==id&&u.svarstyp!=='alternativ'&&u.rättSvar!=null&&v(u)===v(t)).map(u=>u.id);
    assert.deepEqual(krock,[],`${id} har samma facit som ${krock}`);}
});

test('Facit räknas om',()=>{
  assert.equal(s('3.2053'),52+71);assert.equal(s('3.2054'),140-58);assert.equal(s('3.2055'),44+47);assert.equal(s('3.2056'),180-58);assert.equal(s('3.2057'),(180-28)/2+28);
  assert.equal(5*s('3.2058'),2*s('3.2058')+12+s('3.2058')+30);assert.equal(s('3.2059'),42+29);assert.equal(s('3.2060'),3*135/5);assert.equal(s('3.2062'),128-(180-128));
  assert.equal(s('3.2064'),48+77);assert.equal(s('3.2065'),360);assert.equal(s('3.2066'),(180-112)+(180-136));assert.equal(s('3.2067'),54+22+27);
  assert.equal(s('3.2068'),180-57);assert.equal(s('3.2071'),720/6);assert.equal(s('3.2073'),3*180);assert.equal(3*s('3.2074')+12,5*s('3.2074')-20);
  assert.equal(2*s('3.2075')-24,90);assert.equal(2*s('3.2076')+15,4*s('3.2076')-35);assert.equal(s('3.2078'),38+47);assert.equal(s('3.2079'),64/2+116/2);
  assert.equal((s('3.2080')-2)*180,140*s('3.2080'));assert.equal(s('3.2081'),180-(180-70)/2);
  assert.equal(s('3.2083')**2,4*16);assert.ok(Math.abs(s('3.2084')**2-5*16.2)<1e-9);assert.equal(s('3.2086'),6**2/9);assert.ok(Math.abs(s('3.2087')-180*5/600)<1e-9);
  assert.equal(s('3.2089'),13*10/26);assert.equal(s('3.2090'),12*25/4-12);assert.ok(Math.abs(s('3.2091')-1/(1/4+1/6))<1e-9);assert.equal(s('3.2093'),40);
  assert.ok(Math.abs(s('3.2094')-5.2*10/4)<1e-9);assert.equal(s('3.2095'),37);
});

test('Vinkelbågarna i figurerna har de angivna storlekarna',()=>{
  const bagar=id=>(get(id).t.match(/<path d="M [^"]+"/g)||[]).map(p=>{const[,sx,sy,r,ex,ey]=p.match(/M ([\d.-]+) ([\d.-]+) A ([\d.]+) [\d.]+ 0 0 [01] ([\d.-]+) ([\d.-]+)/).map(Number);
    return 2*Math.asin(Math.min(1,Math.hypot(ex-sx,ey-sy)/(2*r)))*180/Math.PI;});
  const forv={'3.2053':[52,71,123],'3.2054':[58,82,140],'3.2055':[44,47,91],'3.2056':[58,122],'3.2057':[28,104],'3.2058':[54,51,105],'3.2059':[42,29,71],'3.2062':[128,76],
    '3.2064':[48,77,125],'3.2067':[54,22,27,103],'3.2068':[57,123],'3.2074':[60,60],'3.2076':[65,65],'3.2078':[38,47,85],'3.2079':[64,116,90],'3.2081':[70,125],'3.2095':[37,37]};
  for(const[id,v]of Object.entries(forv)){const b=bagar(id);assert.equal(b.length,v.length,id);b.forEach((x,i)=>assert.ok(Math.abs(x-v[i])<0.6,`${id}: ${x} ≠ ${v[i]}`));}
});

test('Precision, flerval och figurer',()=>{
  for(const id of NYA){const t=get(id);if(typeof t.rättSvar==='number'&&!Number.isInteger(t.rättSvar))assert.match(t.t,/decimal|exakt/,id);}
  for(const id of NYA.filter(id=>get(id).svarstyp==='alternativ')){const a=get(id).alternativ,r=a.filter(x=>x.ratt).length;assert.ok(r>=1&&a.length-r>=2,id);if(r===1)assert.equal(a[0].ratt,false,id);}
  const fig=NYA.filter(id=>/<svg/.test(get(id).t));assert.equal(fig.length,26);
  for(const id of fig)for(const svg of get(id).t.match(/<svg[^>]*>/g)){assert.match(svg,/max-width:\d+px/,id);assert.match(svg,/aria-label="[^"]{20,}"/,id);}
  assert.match(get('3.2087').t,/inte skalenlig/);
});
