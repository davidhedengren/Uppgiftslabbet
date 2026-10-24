'use strict';
/* Ma5 2026-10-24: differentialekvationer (y' = ky, inhomogena av första ordningen, homogena och inhomogena av andra ordningen)
   och logistisk tillväxt. 61 nya kort 4.605–4.665 med fokus på träningsnivå 1, variation och lösningskurvor. */
const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('node:fs'),vm=require('node:vm'),path=require('node:path');
const c={window:{}};vm.runInNewContext(fs.readFileSync(path.join(__dirname,'..','uppgiftermatf1.js'),'utf8'),c);
const B=JSON.parse(JSON.stringify(c.window.BANKMATF1));const get=id=>{const t=B.find(x=>x.id===id);assert.ok(t,id);return t;};
const NYA=Array.from({length:61},(_,i)=>`4.${605+i}`);

// Lagrade lösningar tolkas och sätts in numeriskt i ekvationerna.
const fn=s=>new Function('x','A1','A2','return '+s.replace(/^y=/,'').replace(/C_1/g,'A1').replace(/C_2/g,'A2').replace(/\bC\b/g,'A1')
  .replace(/e\^\(/g,'Math.exp(').replace(/e\^x/g,'Math.exp(x)').replace(/\bsin\(/g,'Math.sin(').replace(/\bcos\(/g,'Math.cos('));
const h=1e-4,d1=(f,x)=>(f(x+h)-f(x-h))/(2*h),d2=(f,x)=>(f(x+h)-2*f(x)+f(x-h))/(h*h);
const loser=(s,F,konst=[[0,0],[1.3,-0.7],[-2,2.5]])=>{const g=fn(s);return konst.every(([a,b])=>{const f=x=>g(x,a,b);return [0,0.4,1.1].every(x=>Math.abs(F(f(x),d1(f,x),d2(f,x)))<1e-3*Math.max(1,Math.abs(f(x))));});};

test('61 nya kort i kap 4 med många kort på nivå 1',()=>{
  const per={},tn1={};
  for(const id of NYA){const t=get(id);per[t.omr]=(per[t.omr]||0)+1;if(t.traningsniva===1)tn1[t.omr]=(tn1[t.omr]||0)+1;
    assert.equal(t.kap,4,id);assert.equal(t.spel,true,id);assert.equal(t.geogebra,false,id);assert.ok([1,2,3].includes(t.traningsniva),id);}
  assert.deepEqual(per,{homogena_forsta:12,inhomogena_forsta:12,homogena_andra:13,inhomogena_andra:12,tillvaxt_begransning:12});
  assert.deepEqual(tn1,{homogena_forsta:8,inhomogena_forsta:5,homogena_andra:7,inhomogena_andra:6,tillvaxt_begransning:8});
  assert.equal(new Set(B.map(x=>x.id)).size,B.length,'dubblerade ID:n');
});

test('Nya delmoment har minst åtta uppgifter',()=>{
  for(const [omr,familj] of [['homogena_forsta',"Tolka y' = ky i grafer och sammanhang"],['homogena_andra','Karakteristisk ekvation och lösningstyper'],['tillvaxt_begransning','Logistiska kurvor och lösningar']])
    assert.ok(B.filter(x=>x.omr===omr&&x.familj===familj).length>=8,familj);
});

test('Inget nytt kort delar facit med ett annat kort i samma område',()=>{
  const v=x=>{const r=x.rättSvar,s=(Array.isArray(r)?JSON.stringify(r):String(r)).replace(/\s/g,''),n=Number(s);return isNaN(n)?s:String(Math.round(n*1e6)/1e6);};
  for(const id of NYA){const t=get(id);if(t.svarstyp==='alternativ')continue;
    const krock=B.filter(u=>u.omr===t.omr&&u.id!==id&&u.svarstyp!=='alternativ'&&u.rättSvar!=null&&v(u)===v(t)).map(u=>u.id);
    assert.deepEqual(krock,[],`${id} har samma facit som ${krock}`);}
});

test('Lösningar uppfyller sina differentialekvationer och villkor',()=>{
  const s=id=>get(id).rättSvar;
  assert.ok(loser(s('4.612'),(y,dy)=>dy-6*y));assert.ok(loser(s('4.618'),(y,dy)=>dy+2*y-10));
  assert.ok(loser(s('4.622'),(y,dy)=>dy+2*y-10,[[0,0]]));assert.equal(fn(s('4.622'))(0),5);
  assert.ok(loser(s('4.623'),(y,dy)=>dy-(4-y),[[0,0]]));assert.ok(Math.abs(fn(s('4.623'))(0))<1e-12);
  assert.ok(loser(s('4.631'),(y,dy,d2y)=>d2y-2*dy-3*y));assert.ok(loser(s('4.632'),(y,dy,d2y)=>d2y-10*dy+25*y));assert.ok(loser(s('4.633'),(y,dy,d2y)=>d2y+4*y));
  for(const [id,F,y0,dy0] of [['4.638',(y,dy,d2y)=>d2y+16*y,0,8],['4.639',(y,dy,d2y)=>d2y-2*dy-3*y,0,8],['4.651',(y,dy,d2y)=>d2y-y-2,0,0]]){
    assert.ok(loser(s(id),F,[[0,0]]),id);const f=x=>fn(s(id))(x);assert.ok(Math.abs(f(0)-y0)<1e-9&&Math.abs(d1(f,0)-dy0)<1e-5,id);}
  assert.ok(loser(s('4.643'),(y,dy,d2y)=>d2y-y-5));
  // ansatser och konstanter
  const [a,b]=s('4.624');for(const x of [0,1,2.5])assert.ok(Math.abs(a+(a*x+b)-(2*x+3))<1e-12,'4.624');// y′ + y = 2x + 3
  assert.deepEqual([a,b],[2,1]);assert.equal(s('4.625'),-5);assert.deepEqual(s('4.647'),[1,3]);assert.equal(s('4.648'),6);assert.equal(s('4.652'),5);assert.deepEqual(s('4.653'),[1,0,-2]);
  assert.deepEqual(s('4.640'),[1,-6]);assert.deepEqual(s('4.629'),[2,5]);assert.deepEqual(s('4.634'),[-3,3]);assert.equal(s('4.637'),9);
  assert.equal(s('4.617'),6);assert.equal(s('4.627'),5);assert.equal(s('4.642'),-3);assert.equal(s('4.646'),15);assert.equal(s('4.650'),1.2);assert.equal(s('4.649'),1.5);
  assert.ok(Math.abs(3-3*Math.exp(-2)-s('4.628'))<0.005);assert.ok(Math.abs(10/Math.E-s('4.614'))<0.005);assert.ok(Math.abs(Math.log(2)/0.1-s('4.615'))<0.05);
  assert.ok(Math.abs(100*Math.exp(-0.5)-s('4.611'))<0.05);assert.equal(s('4.616'),'ln(3)');assert.equal(s('4.607'),"y'=0.02y");
});

test('Logistisk tillväxt räknas om',()=>{
  const s=id=>get(id).rättSvar;
  assert.equal(s('4.654'),800);assert.equal(s('4.655'),450);assert.equal(s('4.656'),0.4*50*(1-50/250));assert.equal(s('4.658'),0.6/0.0015);
  assert.equal(s('4.659'),1000);assert.equal(s('4.660'),0.25*400*(1-400/800));assert.equal(s('4.661'),1200/12);assert.equal(s('4.662'),(300-30)/30);
  assert.equal(s('4.663'),600/2);assert.ok(Math.abs(Math.log(24)/0.4-s('4.664'))<0.05);
});

test('Flervalskort har rätt alternativ',()=>{
  const ratt=id=>get(id).alternativ.filter(a=>a.ratt).map(a=>a.txt);
  assert.deepEqual(ratt('4.605'),['\\(y=e^{5x}\\)']);assert.deepEqual(ratt('4.610'),['C']);assert.deepEqual(ratt('4.619'),['\\(y=4\\)']);
  assert.deepEqual(ratt('4.626'),['De rör sig bort från y = 3.']);assert.deepEqual(ratt('4.630'),['\\(r^2+4r-5=0\\)']);
  assert.deepEqual(ratt('4.635'),['De svänger och amplituden avtar.']);assert.deepEqual(ratt('4.636'),["\\(y''+2y'+10y=0\\)"]);
  assert.deepEqual(ratt('4.644'),['\\(y_p=ax+b\\)']);assert.deepEqual(ratt('4.645'),['\\(y_p=a\\cos2x+b\\sin2x\\)']);
  assert.equal(ratt('4.657').length,1);assert.deepEqual(ratt('4.665'),['B']);
});

test('Svarsformat för lösningsfamiljer, lösningar och ekvationer',()=>{
  for(const id of ['4.612','4.618','4.631','4.632','4.633','4.643'])assert.equal(get(id).svarFormat,'diffekv_losning',id);
  for(const id of ['4.622','4.623','4.638','4.639','4.651']){assert.equal(get(id).svarstyp,'ekvation',id);assert.equal(get(id).svarFormat,'uttryck',id);}
  assert.equal(get('4.607').svarFormat,'diffekvation');
  const figurer=NYA.filter(id=>/<svg/.test(get(id).t));assert.equal(figurer.length,13);
  for(const id of figurer){const t=get(id).t;assert.match(t,/style="width:100%;max-width:\d+px"/,id);assert.match(t,/role="img" aria-label="[^"]{20,}"/,id);}
});
