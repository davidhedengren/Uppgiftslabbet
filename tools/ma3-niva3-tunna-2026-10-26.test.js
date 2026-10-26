'use strict';
/* Ma3 nivå 3 i tunna områden (2026-10-26). Ett block per område. Kontrollerar nivå, format, facit enligt 1.116
   (rubrik i varje steg, svarsrad, inga råa < >), flervalskommentarer, dubblettfacit och räknar om svaren. */
const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('node:fs'),vm=require('node:vm'),path=require('node:path');
const c={window:{}};vm.runInNewContext(fs.readFileSync(path.join(__dirname,'..','uppgiftermato1.js'),'utf8'),c);
const B=JSON.parse(JSON.stringify(c.window.BANKMATO1));const get=id=>{const t=B.find(x=>x.id===id);assert.ok(t,id);return t;};
const r=(p,a,b)=>Array.from({length:b-a+1},(_,i)=>`${p}.${a+i}`);
const OMR={deriveringsregler:r(2,1259,1264),derivata_a_x:r(2,1265,1270),forkorta_rationella:r(1,965,970),rationella_uttryck:r(1,971,976),problemlosning_derivata:r(3,1246,1251),integral_area:r(3,1252,1257),areasatsen:r(4,567,572),enhetscirkeln:r(4,573,578)};
const v=x=>JSON.stringify(x.rättSvar);
for(const [omr,ids] of Object.entries(OMR))test(`${omr}: ${ids.length} nivå 3-kort med facitkraven uppfyllda`,()=>{
  for(const id of ids){const t=get(id);assert.equal(t.omr,omr,id);assert.equal(t.traningsniva,3,id);assert.equal(t.niva,'C',id);assert.equal(t.poang,'0/1/0',id);assert.equal(t.spel,true,id);
    const steg=[...t.s.matchAll(/<li>([\s\S]*?)<\/li>/g)];assert.ok(steg.length>=2,id);for(const m of steg)assert.match(m[1],/^<p class="facit-rubrik">/,id);
    for(const m of steg)assert.doesNotMatch(m[1],/^<p class="facit-rubrik">(Lös ekvationen|Lös|Kontrollera|Förenkla|Beräkna|Beräkna y|Derivera|Svar|Steg \d+|Sätt in|Faktorisera|Multiplicera ut|Kvadratkomplettera|Sätt uttrycken lika|Två lösningar)\.?<\/p>/,`${id}: generisk rubrik`);
    assert.match(t.s,/class="facit-svar"/,id);assert.ok(String(t.ledtrad).replace(/<[^>]+>/g,'').trim().length>=15,id);
    for(const m of (t.t+t.s+t.ledtrad).matchAll(/\\\(([\s\S]*?)\\\)|\\\[([\s\S]*?)\\\]/g))assert.doesNotMatch(m[1]??m[2],/[<>]/,id);
    if(t.svarstyp==='alternativ'){assert.equal(t.alternativ.filter(a=>a.ratt).length,1,id);assert.ok(!t.alternativ[0].ratt,id);for(const a of t.alternativ)if(!a.ratt)assert.ok(a.kommentar,id);}
    else{const krock=B.filter(w=>w.omr===omr&&w.id!==id&&w.rättSvar!=null&&v(w)===v(t)).map(w=>w.id);assert.deepEqual(krock,[],id);}
    if(t.svarstyp==='flera_delar'){assert.equal(t.svarEtiketter.length,t.rättSvar.length,id);if(t.självrättning!==true)assert.deepEqual(t.självrättning,t.rättSvar.map(()=>true),id);}}
});
const d=(f,x,h=1e-5)=>(f(x+h)-f(x-h))/(2*h);
const nara=(a,b,id)=>assert.ok(Math.abs(a-b)<1e-6,`${id}: ${a} ≠ ${b}`);
test('deriveringsregler: derivatorna räknas om numeriskt',()=>{
  for(const x of get('2.1259').rättSvar)nara(d(x=>x**3-3*x*x+2,x),9,'2.1259');
  nara(d(x=>(x*x+4)/Math.sqrt(x),4),get('2.1260').rättSvar,'2.1260');
  const [x3,y3]=get('2.1261').rättSvar,f3=x=>2*Math.sqrt(x);nara(d(f3,x3),0.5,'2.1261');assert.equal(f3(x3),y3);
  const [v5,tt]=get('2.1262').rättSvar,V=t=>200+30*t-t*t;nara(d(V,5),v5,'2.1262');nara(d(V,tt),0,'2.1262');
  assert.equal(get('2.1263').alternativ.find(a=>a.ratt).txt,'f(x) = x³ − 12x');nara(d(x=>x**3-12*x,2),0,'2.1263');
  nara(d(x=>(x**3-4*x)/(x*x),2),get('2.1264').rättSvar,'2.1264');
});
test('derivata_a_x: svaren räknas om',()=>{
  const ln=Math.log;assert.equal(get('2.1265').rättSvar,Math.round(2400*1.035**10*ln(1.035)));
  const t2=ln(4/(40*-ln(0.8)))/ln(0.8),u2=get('2.1266');assert.ok(Math.abs(u2.rättSvar-t2)<=u2.tolerans,'2.1266');
  const u3=get('2.1267');[8*ln(2),8-24*ln(2)].forEach((x,i)=>assert.ok(Math.abs(u3.rättSvar[i]-x)<=u3.tolerans[i],'2.1267'));
  assert.ok(Math.abs(get('2.1268').rättSvar-Math.exp(2))<=get('2.1268').tolerans);
  assert.equal(get('2.1269').alternativ.find(a=>a.ratt).txt,'f′(x) = −ln 2 · 2^(−x)');nara(d(x=>2**-x,1.3),-ln(2)*2**-1.3,'2.1269');
  assert.deepEqual(get('2.1270').rättSvar,[Math.round(10000*1.04**5*ln(1.04)),Math.round(10000*(1.04**6-1.04**5))]);
});
test('forkorta_rationella: förenklingarna prövas i flera punkter',()=>{
  const lika=(f,g,ute,id)=>{for(const x of [-4.5,-1.5,0.5,1.5,3.5,6]){if(ute.includes(x))continue;nara(f(x),g(x),id);}};
  lika(x=>(x*x+5*x)/(x*x+10*x+25),x=>x/(x+5),[],'1.965');assert.deepEqual(get('1.965').rättSvar,['x/(x+5)',[-5]]);
  lika(x=>(x**3-4*x*x+4*x)/(x*x-4),x=>x*(x-2)/(x+2),[],'1.966');assert.deepEqual(get('1.966').rättSvar[1],[-2,2]);
  const x7=get('1.967').rättSvar;nara((x7*x7-x7-6)/(x7*x7-9),0.5,'1.967');
  assert.equal(get('1.968').alternativ.find(a=>a.ratt).txt,'(x − 1)/(x² − 1)');lika(x=>(x-1)/(x*x-1),x=>1/(x+1),[],'1.968');
  lika(x=>(x*x-6*x+9)/(9-x*x),x=>(3-x)/(x+3),[],'1.969');assert.deepEqual(get('1.969').rättSvar[1],[-3,3]);
  assert.deepEqual(get('1.970').rättSvar,[1,2]);assert.doesNotMatch(get('1.970').t,/<circle/);
});
test('rationella_uttryck: svaren räknas om',()=>{
  const [n0,ute]=get('1.971').rättSvar;assert.equal(n0-3,0);assert.notEqual(n0*n0-4,0);for(const x of ute)assert.equal(x*x-4,0);
  const [c,x2]=get('1.972').rättSvar;assert.equal(4+8+c,0);assert.equal(x2*x2+4*x2+c,0);assert.notEqual(x2,2);
  const n=get('1.973').rättSvar;assert.equal((5000+40*n)/n,65);
  assert.equal(get('1.974').alternativ.find(a=>a.ratt).txt,'a måste vara större än 0');
  for(const x of get('1.975').rättSvar)assert.ok(x-1===0||x*x-4*x===0);
  assert.equal(get('1.976').alternativ.find(a=>a.ratt).txt,'(x + 3)/(x² − 3x)');
});
test('problemlosning_derivata: svaren räknas om',()=>{
  const v=t=>8*t-3*t*t,[t1,v1]=get('3.1246').rättSvar;assert.ok(Math.abs(t1-4/3)<0.005&&Math.abs(v1-16/3)<0.005);for(let t=0.01;t<=2.5;t+=0.01)assert.ok(v(t)>0&&v(t)<=16/3+1e-12);
  assert.equal(get('3.1247').rättSvar,12-1.5*2);
  const [x,y]=get('3.1248').rättSvar,f=x=>x*x-2*x,tan=a=>X=>f(a)+d(f,a)*(X-a);nara(tan(3)(x),y,'3.1248');nara(tan(-1)(x),y,'3.1248');
  const V=x=>-0.5*x*x+80*x-1200,[m,xm]=get('3.1249').rättSvar;nara(d(V,50),m,'3.1249');nara(d(V,xm),0,'3.1249');
  const s=t=>6*t-0.75*t*t,[ts,ss]=get('3.1250').rättSvar;nara(d(s,ts),0,'3.1250');assert.equal(s(ts),ss);
  assert.equal(get('3.1251').alternativ.find(a=>a.ratt).txt,'f(2) = 5 och f′(2) = 3');
});
test('integral_area: svaren räknas om',()=>{
  const F=x=>x**3/3-4*x;nara(get('3.1252').rättSvar,-(F(2)-F(0))+(F(3)-F(2)),'3.1252');
  const a=get('3.1253').rättSvar;assert.equal(a*a-1,120);assert.ok(a>1);
  const b=get('3.1254').rättSvar,G=x=>x**4/4+5*x;nara(G(b)-G(-b),130,'3.1254');
  assert.equal(get('3.1255').rättSvar,(12*6-36));
  assert.equal(get('3.1256').rättSvar,2+3);
  assert.equal(get('3.1257').alternativ.find(a=>a.ratt).txt,'∫₀¹ x³ dx < ∫₀¹ x² dx < ∫₀¹ x dx');
});
test('areasatsen: svaren räknas om',()=>{
  const sin=v=>Math.sin(v*Math.PI/180),ar=(a,b,v)=>a*b*sin(v)/2;
  const u1=get('4.567');assert.ok(Math.abs(u1.rättSvar-ar(14,9,110)*85)<=u1.tolerans);
  const u2=get('4.568');assert.ok(Math.abs(u2.rättSvar-5*ar(5,5,72))<=u2.tolerans);
  const u3=get('4.569');assert.ok(Math.abs(u3.rättSvar-(2*ar(5,7,60)+2*ar(5,7,120)))<=u3.tolerans);
  assert.equal(get('4.570').rättSvar,24/3);
  assert.equal(get('4.571').alternativ.find(a=>a.ratt).txt,'Sidorna 5 och 9 med vinkeln 90°');
  for(const v of get('4.572').rättSvar)nara(ar(5,8,v),ar(5,8,90)/2,'4.572');
  for(const id of r(4,567,572))assert.deepEqual(get(id).kurs,['1c'],id);
});
test('enhetscirkeln: svaren räknas om',()=>{
  const g=v=>v*Math.PI/180,S=v=>Math.sin(g(v)),C=v=>Math.cos(g(v));
  nara(S(37)**2+S(53)**2,get('4.573').rättSvar,'4.573');
  const u2=get('4.574');[C(140),C(220),C(320)].forEach((x,i)=>assert.ok(Math.abs(u2.rättSvar[i]-x)<=u2.tolerans[i]+0.0005,'4.574'));
  const u3=get('4.575'),[y,v]=u3.rättSvar;assert.ok(Math.abs(y+Math.sqrt(1-0.28**2))<=u3.tolerans[0]);assert.ok(Math.abs(v-(360-Math.acos(0.28)*180/Math.PI))<=u3.tolerans[1]);
  assert.equal(get('4.576').rättSvar,'-1/4');nara(S(150)*C(300)+C(135)*S(45),-0.25,'4.576');
  assert.equal(get('4.577').alternativ.find(a=>a.ratt).txt,'130°');nara(S(130),S(50),'4.577');nara(C(130),-C(50),'4.577');
  const u6=get('4.578');assert.ok(Math.abs(u6.rättSvar+Math.sqrt(0.84))<=u6.tolerans);
});
