'use strict';
/* Ma2 kap 3–4, omgång S5 2026-10-25: 53 text- och problemlösningskort på nivå 1–3 i de tunnaste områdena
   (3.2096–3.2121: geometrisk problemlösning, koordinatgeometri, kordasatsen/bisektrissatsen;
    4.2112–4.2138: regression, normalfördelning med GeoGebra, korrelation, tabeller och diagram). */
const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('node:fs'),vm=require('node:vm'),path=require('node:path');
const c={window:{}};vm.runInNewContext(fs.readFileSync(path.join(__dirname,'..','uppgifterma2.js'),'utf8'),c);
const B=JSON.parse(JSON.stringify(c.window.BANKMA2));const get=id=>{const t=B.find(x=>x.id===id);assert.ok(t,id);return t;};
const NYA=[...Array.from({length:26},(_,i)=>`3.${2096+i}`),...Array.from({length:27},(_,i)=>`4.${2112+i}`)];
const s=id=>get(id).rättSvar,nara=(a,b,t)=>Math.abs(a-b)<=t;
const tat=z=>Math.exp(-z*z/2)/Math.sqrt(2*Math.PI);
const Phi=z=>{if(z<0)return 1-Phi(-z);const n=2000,h=z/n;let S=tat(0)+tat(z);for(let i=1;i<n;i++)S+=(i%2?4:2)*tat(i*h);return 0.5+S*h/3;};
const N=(x,mu,sd)=>Phi((x-mu)/sd),inv=p=>{let lo=-6,hi=6;for(let i=0;i<80;i++){const m=(lo+hi)/2;if(Phi(m)<p)lo=m;else hi=m;}return lo;};
const ls=(xs,ys)=>{const n=xs.length,X=xs.reduce((a,b)=>a+b),Y=ys.reduce((a,b)=>a+b),XY=xs.reduce((a,x,i)=>a+x*ys[i],0),XX=xs.reduce((a,x)=>a+x*x,0),YY=ys.reduce((a,y)=>a+y*y,0);
  const k=(n*XY-X*Y)/(n*XX-X*X);return{k,m:(Y-k*X)/n,r:(n*XY-X*Y)/Math.sqrt((n*XX-X*X)*(n*YY-Y*Y))};};

test('53 kort med nivå 1–3, rätt kapitel, kursspår och GeoGebra-flagga',()=>{
  const per={},niv={1:0,2:0,3:0},kap3=['geometri_problemlosning','koordinatgeometri_problemlosning','kordasatsen_biskarningssatsen'],
    smal=['geometri_problemlosning','kordasatsen_biskarningssatsen','linjar_regression','korrelation_koefficient'];
  for(const id of NYA){const t=get(id);per[t.omr]=(per[t.omr]||0)+1;niv[t.traningsniva]++;assert.equal(t.kap,kap3.includes(t.omr)?3:4,id);assert.equal(t.spel,true,id);assert.equal(t.miniräknare,true,id);
    assert.deepEqual(t.kurs,smal.includes(t.omr)?['2b','2c']:['2a','2b','2c'],id);assert.equal(t.geogebra,/GeoGebra/.test(t.t),id);
    if(t.traningsniva===3){assert.equal(t.niva,'C',id);assert.equal(t.poang,'0/1/0',id);}}
  assert.deepEqual(per,{geometri_problemlosning:11,koordinatgeometri_problemlosning:8,kordasatsen_biskarningssatsen:7,linjar_regression:8,normalfordelning_digitala_verktyg:8,korrelation_koefficient:5,tabeller_diagram:6});
  assert.deepEqual(niv,{1:15,2:29,3:9});
  assert.equal(new Set(B.map(x=>x.id)).size,B.length,'dubblerade ID:n');
});

test('Inget nytt kort delar facit med ett annat kort i samma område',()=>{
  const v=x=>{const r=x.rättSvar,t=(Array.isArray(r)?JSON.stringify(r):String(r)).replace(/\s/g,''),n=Number(t);return isNaN(n)?t:String(Math.round(n*1e6)/1e6);};
  for(const id of NYA){const t=get(id);if(t.svarstyp==='alternativ')continue;
    const krock=B.filter(u=>u.omr===t.omr&&u.id!==id&&u.svarstyp!=='alternativ'&&u.rättSvar!=null&&v(u)===v(t)).map(u=>u.id);
    assert.deepEqual(krock,[],`${id} har samma facit som ${krock}`);}
});

test('Geometri och koordinater räknas om, och alla trianglar går att rita',()=>{
  assert.equal(s('3.2096'),14*9);assert.equal(s('3.2097'),110);assert.equal(s('3.2098'),2700);assert.ok(nara(s('3.2099'),200+60*Math.PI,0.05));assert.ok(nara(s('3.2100'),1.68+0.18*Math.PI,0.005));
  assert.ok(Math.hypot(2,0.9)<2.3);assert.equal(s('3.2102'),0.6*180/2);assert.ok(nara(s('3.2103'),1024-225*Math.PI,0.05));assert.ok(nara(s('3.2104'),8*Math.PI,0.05));assert.equal(s('3.2105'),72);assert.equal(s('3.2106'),192);
  assert.equal(s('3.2107'),13);assert.deepEqual(s('3.2108'),[2,1]);assert.ok(nara(s('3.2109'),Math.sqrt(52)-Math.sqrt(45),0.005));assert.equal(s('3.2111'),2300);assert.equal(s('3.2112'),17);
  const y=s('3.2113');assert.equal(4+(5-y)**2,36+(1-y)**2);
  assert.equal(s('3.2115'),49*4/7);assert.equal(s('3.2117'),10*9/5);assert.equal(15*15,5*(2*s('3.2118')-5));assert.equal(s('3.2119'),16);assert.equal(s('3.2120'),21*2/3);assert.ok(nara(s('3.2121'),2*Math.sqrt(105),0.05));
  // Triangelolikheten för trianglarna som anges med tre sidor (40/30/49, 18/10/14, 16/8/21).
  for(const[a,b,c]of[[40,30,49],[18,10,14],[16,8,21]])assert.ok(a<b+c&&b<a+c&&c<a+b,`${a},${b},${c}`);
  for(const id of NYA.filter(id=>get(id).omr==='geometri_problemlosning')){assert.match(get(id).t,/<svg/,id);assert.doesNotMatch(get(id).s,/facit-steglista/,id);}
});

test('Statistik räknas om',()=>{
  assert.ok(nara(s('4.2112'),126.6,1e-9));assert.equal(s('4.2114'),41-47);assert.ok(nara(s('4.2115'),-ls([1,2,3,4,5,6],[14.2,13.9,13.5,13.4,12.9,12.7]).k,0.005));
  assert.equal(s('4.2116'),51);assert.ok(nara(s('4.2117'),2.6/0.045,0.05));assert.ok(nara(0.5*s('4.2119')-1,3.5,1e-9));
  assert.ok(nara(s('4.2120'),100*(1-N(190,180,7)),0.06));assert.ok(nara(s('4.2121'),100*(N(120,100,15)-N(85,100,15)),0.06));assert.ok(nara(s('4.2122'),500*N(140,165,18),0.6));
  assert.ok(nara(s('4.2123'),420+60*inv(0.85),0.06));assert.ok(nara(s('4.2124'),4000*N(2,3.2,0.6),0.6));assert.ok(nara(s('4.2125'),500+8*inv(0.05),0.06));
  assert.ok(nara(s('4.2126'),2/inv(0.99),0.006));assert.ok(nara(s('4.2127'),200*(1-Phi(1.5)),0.06));
  assert.ok(nara(s('4.2129'),ls([2,4,5,7,8,10,12],[11,15,13,20,17,22,25]).r,0.005));
  assert.equal(s('4.2133'),9);assert.equal(s('4.2134'),12);assert.ok(nara(s('4.2135'),126,1e-9));assert.ok(nara(s('4.2136'),100*85/1200,0.05));assert.equal(s('4.2138'),45);
});

test('Precision, flerval och figurer',()=>{
  for(const id of NYA){const t=get(id);if(typeof t.rättSvar==='number'&&!Number.isInteger(t.rättSvar))assert.match(t.t,/decimal|exakt/,id);if(/med ett heltal/.test(t.t))assert.ok(Number.isInteger(t.rättSvar),id);}
  for(const id of NYA.filter(id=>get(id).svarstyp==='alternativ')){const a=get(id).alternativ,r=a.filter(x=>x.ratt).length;assert.ok(r>=1&&a.length-r>=2,id);if(r===1)assert.equal(a[0].ratt,false,id);}
  const fig=NYA.filter(id=>/<svg/.test(get(id).t));assert.equal(fig.length,27);
  for(const id of fig)for(const svg of get(id).t.match(/<svg[^>]*>/g))assert.match(svg,/aria-label="[^"]{20,}"/,id);
  // Punkterna i koordinatfigurerna ligger inom viewBox.
  for(const id of ['3.2107','3.2109','3.2111','3.2112','3.2113']){const t=get(id).t,[,w,h]=t.match(/viewBox="0 0 ([\d.]+) ([\d.]+)"/).map(Number);
    for(const m of t.matchAll(/<circle cx="([\d.-]+)" cy="([\d.-]+)"/g)){const x=+m[1],y=+m[2];assert.ok(x>0&&x<w&&y>0&&y<h,`${id}: (${x}, ${y})`);}}
});
