'use strict';
/* Ma2 kap 4 statistik, omgång S3 2026-10-25: 51 text- och problemlösningskort 4.2061–4.2111 på nivå 1–3
   (tabeller och diagram, kvartiler, lådagram, normalfördelning med GeoGebra, linjär regression, korrelation). */
const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('node:fs'),vm=require('node:vm'),path=require('node:path');
const c={window:{}};vm.runInNewContext(fs.readFileSync(path.join(__dirname,'..','uppgifterma2.js'),'utf8'),c);
const B=JSON.parse(JSON.stringify(c.window.BANKMA2));const get=id=>{const t=B.find(x=>x.id===id);assert.ok(t,id);return t;};
const NYA=Array.from({length:51},(_,i)=>`4.${2061+i}`);
const s=id=>get(id).rättSvar,nara=(a,b,t)=>Math.abs(a-b)<=t;
// Normalfördelning med Simpsons regel och linjär regression med minsta kvadratmetoden.
const tat=z=>Math.exp(-z*z/2)/Math.sqrt(2*Math.PI);
const Phi=z=>{if(z<0)return 1-Phi(-z);const n=2000,h=z/n;let S=tat(0)+tat(z);for(let i=1;i<n;i++)S+=(i%2?4:2)*tat(i*h);return 0.5+S*h/3;};
const N=(x,mu,sd)=>Phi((x-mu)/sd),inv=p=>{let lo=-6,hi=6;for(let i=0;i<80;i++){const m=(lo+hi)/2;if(Phi(m)<p)lo=m;else hi=m;}return lo;};
const ls=(xs,ys)=>{const n=xs.length,X=xs.reduce((a,b)=>a+b),Y=ys.reduce((a,b)=>a+b),XY=xs.reduce((a,x,i)=>a+x*ys[i],0),XX=xs.reduce((a,x)=>a+x*x,0),YY=ys.reduce((a,y)=>a+y*y,0);
  const k=(n*XY-X*Y)/(n*XX-X*X);return{k,m:(Y-k*X)/n,r:(n*XY-X*Y)/Math.sqrt((n*XX-X*X)*(n*YY-Y*Y))};};
const med=a=>{const b=[...a].sort((x,y)=>x-y),n=b.length;return n%2?b[(n-1)/2]:(b[n/2-1]+b[n/2])/2;};
const kv=a=>{const b=[...a].sort((x,y)=>x-y),h=b.length/2;return[med(b.slice(0,h)),med(b.slice(h))];};

test('51 kort i kap 4 med nivå 1–3, rätt kursspår och GeoGebra där verktyget behövs',()=>{
  const per={},niv={1:0,2:0,3:0};
  for(const id of NYA){const t=get(id);per[t.omr]=(per[t.omr]||0)+1;niv[t.traningsniva]++;assert.equal(t.kap,4,id);assert.equal(t.spel,true,id);assert.equal(t.miniräknare,true,id);
    assert.deepEqual(t.kurs,['korrelation_koefficient','linjar_regression'].includes(t.omr)?['2b','2c']:['2a','2b','2c'],id);
    if(t.traningsniva===3){assert.equal(t.niva,'C',id);assert.equal(t.poang,'0/1/0',id);}
    // GeoGebra tillåts när uppgiften ber om normalfördelning, regression eller r med digitalt verktyg; annars nekas det.
    assert.equal(t.geogebra,/GeoGebra/.test(t.t),id);}
  assert.deepEqual(per,{tabeller_diagram:13,kvartiler_percentiler:6,ladagram:6,normalfordelning_digitala_verktyg:10,linjar_regression:10,korrelation_koefficient:6});
  assert.deepEqual(niv,{1:17,2:23,3:11});
  assert.ok(NYA.filter(id=>get(id).omr==='normalfordelning_digitala_verktyg').every(id=>get(id).geogebra));
  assert.equal(new Set(B.map(x=>x.id)).size,B.length,'dubblerade ID:n');
});

test('Inget nytt kort delar facit med ett annat kort i samma område',()=>{
  const v=x=>{const r=x.rättSvar,t=(Array.isArray(r)?JSON.stringify(r):String(r)).replace(/\s/g,''),n=Number(t);return isNaN(n)?t:String(Math.round(n*1e6)/1e6);};
  for(const id of NYA){const t=get(id);if(t.svarstyp==='alternativ')continue;
    const krock=B.filter(u=>u.omr===t.omr&&u.id!==id&&u.svarstyp!=='alternativ'&&u.rättSvar!=null&&v(u)===v(t)).map(u=>u.id);
    assert.deepEqual(krock,[],`${id} har samma facit som ${krock}`);}
});

test('Tabeller, kvartiler och lådagram räknas om',()=>{
  assert.equal(s('4.2061'),132-91);assert.equal(s('4.2062'),248-210);assert.equal(s('4.2063'),100*168/480);assert.equal(s('4.2064'),2*130+80+2*50);
  assert.ok(nara(s('4.2065'),100*90/138,0.05));assert.ok(nara(s('4.2066'),100*(33/27-1),0.05));assert.equal(s('4.2067'),840*1.25);assert.equal(s('4.2068'),30-(14+10-5));
  assert.ok(nara(s('4.2069'),100*13/30,0.05));assert.ok(nara(s('4.2070'),0.48*300,1e-9));assert.ok(nara(s('4.2072')*1.4*1.25,3500,1e-9));
  assert.equal(s('4.2073'),100*1.2*3500/(2400+2100+2600+2300+2900+3500+1.2*3500));
  assert.equal(s('4.2074'),kv([6,9,11,14,15,18,22,27])[0]);
  const syskon=[];[[0,3],[1,8],[2,7],[3,4],[4,2]].forEach(([v,n])=>{for(let i=0;i<n;i++)syskon.push(v);});assert.equal(s('4.2077'),kv(syskon)[1]);
  const A=kv([52,55,57,58,60,61,63,66]),Bq=kv([48,50,54,58,59,63,67,70]);assert.equal(s('4.2078'),(Bq[1]-Bq[0])-(A[1]-A[0]));
  const q=kv([2,4,5,7,9,s('4.2079'),14,16]);assert.equal(q[1]-q[0],9);
  assert.equal(s('4.2080'),74-38);assert.equal(s('4.2081'),160/4);assert.equal(s('4.2085'),50);
  const femtal=get('4.2083').alternativ.find(a=>a.ratt).txt.split('; ').map(x=>Number(x.replace(',','.'))),d=[4,7,8,10,11,13,14,16,18,21,23,30];
  assert.deepEqual(femtal,[4,kv(d)[0],med(d),kv(d)[1],30]);
});

test('Normalfördelning, regression och korrelation räknas om',()=>{
  assert.ok(nara(s('4.2086'),100*(N(62,58,4)-N(55,58,4)),0.06));assert.ok(nara(s('4.2087'),100*(1-N(9000,8000,600)),0.06));assert.ok(nara(s('4.2088'),100*N(19,23,2.5),0.06));
  assert.ok(nara(s('4.2089'),2500*(N(73,62,5)-N(63,62,5)),0.6));assert.ok(nara(s('4.2090'),340+12*inv(0.05),0.06));assert.ok(nara(s('4.2091'),100*(1-N(40.5,40,0.3)+N(39.5,40,0.3)),0.06));
  assert.ok(nara(s('4.2092'),100*((1-N(258,250,4)+N(242,250,4))-(1-N(258,252,3)+N(242,252,3))),0.06));
  assert.ok(nara(s('4.2093'),500-3*inv(0.02),0.06));assert.ok(nara(s('4.2094'),10/inv(0.9),0.06));assert.ok(nara(s('4.2095'),240*(1-N(80,65,10)),0.6));
  assert.equal(s('4.2096'),-1.2*-5+40);assert.ok(nara(s('4.2098'),ls([0,1,2,3,4],[24.5,26,27.8,29.1,30.9]).k,0.005));
  const r6=ls([1,2,3,4,5,6],[42,47,55,58,66,70]);assert.ok(nara(s('4.2099'),r6.k*8+r6.m,0.5));
  assert.ok(nara(1.5*s('4.2100')+20,2.3*s('4.2100')+8,1e-9));assert.ok(nara(-0.8*s('4.2101')+96,20,1e-9));assert.equal(s('4.2102'),2*8+12);assert.equal(s('4.2103'),2.5*60);
  const kl=ls([0,1,2,3,4,5],[120,135,149,166,178,195]);assert.ok(nara(s('4.2104'),(300-kl.m)/kl.k,0.05));
  assert.ok(nara(s('4.2107'),ls([36,37,39,40,41,43,44,45],[160,171,166,178,172,185,177,188]).r,0.005));
});

test('Precision, flerval och figurer',()=>{
  for(const id of NYA){const t=get(id);if(typeof t.rättSvar==='number'&&!Number.isInteger(t.rättSvar))assert.match(t.t,/decimal|exakt/,id);
    if(/med ett heltal/.test(t.t))assert.ok(Number.isInteger(t.rättSvar),id);}
  for(const id of NYA.filter(id=>get(id).svarstyp==='alternativ')){const a=get(id).alternativ,r=a.filter(x=>x.ratt).length;assert.ok(r>=1&&a.length-r>=2,id);if(r===1)assert.equal(a[0].ratt,false,id);}
  const fig=NYA.filter(id=>/<svg/.test(get(id).t));assert.equal(fig.length,17);
  for(const id of fig)for(const svg of get(id).t.match(/<svg[^>]*>/g))assert.match(svg,/aria-label="[^"]{20,}"/,id);
  // 4.2106 har eget sammanhang och delar inte text med 4.2052.
  assert.notEqual(get('4.2106').t.replace(/<svg[\s\S]*?<\/svg>/g,''),get('4.2052').t.replace(/<svg[\s\S]*?<\/svg>/g,''));
});
