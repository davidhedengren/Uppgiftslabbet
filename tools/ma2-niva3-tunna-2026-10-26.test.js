'use strict';
/* Ma2 kap 1–2 nivå 3 i tunna områden (2026-10-26). Ett block per område. Kontrollerar nivå, format, facit enligt 1.116
   (rubrik i varje steg, svarsrad, inga råa < >), flervalskommentarer, dubblettfacit och räknar om svaren. */
const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('node:fs'),vm=require('node:vm'),path=require('node:path');
const c={window:{}};vm.runInNewContext(fs.readFileSync(path.join(__dirname,'..','uppgifterma2.js'),'utf8'),c);
const B=JSON.parse(JSON.stringify(Object.values(c.window).find(Array.isArray)));const get=id=>{const t=B.find(x=>x.id===id);assert.ok(t,id);return t;};
const r=(p,a,b)=>Array.from({length:b-a+1},(_,i)=>`${p}.${a+i}`);
const OMR={grafisk_losning_ekvationssystem:r(1,1229,1234),losningsformel_andragrad:r(2,1217,1222),linjara_representationer:r(1,1235,1240),exponentialgraf:r(2,1223,1228),kvadratkomplettering:r(2,1229,1234)};
const v=x=>JSON.stringify(x.rättSvar);
for(const [omr,ids] of Object.entries(OMR))test(`${omr}: ${ids.length} nivå 3-kort med facitkraven uppfyllda`,()=>{
  for(const id of ids){const t=get(id);assert.equal(t.omr,omr,id);assert.equal(t.traningsniva,3,id);assert.equal(t.niva,'C',id);assert.equal(t.poang,'0/1/0',id);assert.equal(t.spel,true,id);
    const steg=[...t.s.matchAll(/<li>([\s\S]*?)<\/li>/g)];assert.ok(steg.length>=2,id);for(const m of steg)assert.match(m[1],/^<p class="facit-rubrik">/,id);
    for(const m of steg)assert.doesNotMatch(m[1],/^<p class="facit-rubrik">(Lös ekvationen|Lös|Kontrollera|Förenkla|Beräkna|Beräkna y|Derivera|Svar|Steg \d+|Sätt in|Faktorisera|Multiplicera ut|Kvadratkomplettera|Sätt uttrycken lika|Två lösningar)\.?<\/p>/,`${id}: generisk rubrik`);
    assert.match(t.s,/class="facit-svar"/,id);assert.ok(String(t.ledtrad).replace(/<[^>]+>/g,'').trim().length>=15,id);
    for(const m of (t.t+t.s+t.ledtrad).matchAll(/\\\(([\s\S]*?)\\\)|\\\[([\s\S]*?)\\\]/g))assert.doesNotMatch(m[1]??m[2],/[<>]/,id);
    if(t.svarstyp==='alternativ'){assert.equal(t.alternativ.filter(a=>a.ratt).length,1,id);assert.ok(!t.alternativ[0].ratt,id);for(const a of t.alternativ)if(!a.ratt)assert.ok(a.kommentar,id);}
    else{const krock=B.filter(w=>w.omr===omr&&w.id!==id&&w.rättSvar!=null&&v(w)===v(t)).map(w=>w.id);assert.deepEqual(krock,[],id);}
    if(t.svarstyp==='flera_delar'){assert.equal(t.svarEtiketter.length,t.rättSvar.length,id);assert.deepEqual(t.självrättning,t.rättSvar.map(()=>true),id);}}
});
// sys: varje ekvation skrivs som funktion av lösningen och ska bli 0
const sys=(id,...ekv)=>{const x=get(id).rättSvar.map(Number);for(const f of ekv)assert.ok(Math.abs(f(...x))<1e-9,`${id}: ${x} uppfyller inte ${f}`);};
test('grafisk_losning_ekvationssystem: svaren räknas om',()=>{
  sys('1.1229',(x,y)=>2*x-1-y,(x,y)=>-0.5*x+5-y);
  // a och b ger samma linje som 6x − 2y = 4 för två olika x
  sys('1.1230',(a,b)=>6*0-2*(a*0+b)-4,(a,b)=>6*1-2*(a*1+b)-4);
  sys('1.1231',(t,V)=>200-8*t-V,(t,V)=>50+4*t-V);
  const m=get('1.1232').rättSvar;assert.equal(-8+8,0);assert.equal(2*8+m,0);
  sys('1.1233',(x,y)=>0.5*x+1-y,(x,y)=>0.6*x-1-y);
  assert.equal(get('1.1234').alternativ.find(a=>a.ratt).txt,'Om c = 10 har systemet oändligt många lösningar');
});
test('losningsformel_andragrad: svaren räknas om',()=>{
  const [b,l]=get('2.1217').rättSvar;assert.equal(l-b,3);assert.equal(b*l,40);
  assert.deepEqual(get('2.1218').rättSvar,['\\(2+\\sqrt5\\)','\\(2-\\sqrt5\\)']);for(const x of [2+Math.sqrt(5),2-Math.sqrt(5)])assert.ok(Math.abs((x-1)*(x-3)-4)<1e-12);
  const [c,x3]=get('2.1219').rättSvar;assert.equal(36-4*c,0);assert.equal(x3*x3+6*x3+c,0);
  const [b4,x4]=get('2.1220').rättSvar;assert.equal(4+2*b4-14,0);assert.equal(x4*x4+b4*x4-14,0);assert.notEqual(x4,2);
  assert.match(get('2.1221').alternativ.find(a=>a.ratt).txt,/delat ekvationen med 2/);
  assert.deepEqual(get('2.1222').rättSvar,['2','-4/3']);for(const x of [2,-4/3])assert.ok(Math.abs(3*x*x-2*(x+4))<1e-12);
});
test('linjara_representationer: svaren räknas om',()=>{
  const k=(3-5)/(4-1),m=5-k*1;assert.ok(Math.abs(get('1.1235').rättSvar-(-m/k))<1e-12);
  assert.equal(get('1.1236').rättSvar,(100-20)/((30-20)/4));
  const [fast,pp]=get('1.1237').rättSvar;for(const [n,y] of [[12,2040],[20,3160],[35,5260]])assert.equal(fast+pp*n,y);
  const [L0,T]=get('1.1238').rättSvar;const kl=(12-21)/(5-2);assert.equal(L0+kl*2,21);assert.equal(L0+kl*T,0);
  assert.equal(get('1.1239').alternativ.find(a=>a.ratt).txt,'Efter 30 resor är kortet tomt');assert.equal(450-15*30,0);
  const x=get('1.1240').rättSvar;assert.ok(Math.abs((-1.5*x+10)-(x+1))<1e-12);
});
test('exponentialgraf: svaren räknas om',()=>{
  assert.ok(Math.abs(get('2.1223').rättSvar-100*(1-Math.sqrt(289/400)))<1e-9);
  const n=get('2.1224').rättSvar,E=x=>1000+250*x,O=x=>1000*1.12**x;assert.ok(O(n)>E(n)&&O(n-1)<E(n-1));
  assert.equal(get('2.1225').alternativ.find(a=>a.ratt).txt,'Graf B');
  assert.equal(get('2.1226').rättSvar,Math.round(100*((6212/2000)**0.1-1)));
  const x=get('2.1227').rättSvar;assert.ok(5*2**x>10000&&5*2**(x-1)<10000);
  assert.equal(get('2.1228').rättSvar,Math.round(500/Math.sqrt(720/500)));
});
test('kvadratkomplettering: svaren räknas om',()=>{
  assert.equal(get('2.1229').rättSvar,'(x+5)^2-7');for(let x=-5;x<=5;x++)assert.equal((x+5)**2-7,x*x+10*x+18);
  const [mx,xm]=get('2.1230').rättSvar,f=x=>-x*x+4*x+1;assert.equal(f(xm),mx);for(let x=-5;x<=8;x+=0.5)assert.ok(f(x)<=mx);
  const A=x=>x*(12-x);assert.equal(get('2.1231').rättSvar,A(6));for(let x=0;x<=12;x+=0.25)assert.ok(A(x)<=36);
  assert.match(get('2.1232').alternativ.find(a=>a.ratt).txt,/glömt att dra bort 25/);
  const [b,c]=get('2.1233').rättSvar;assert.equal(-b/2,3);assert.equal(9+3*b+c,2);
  const g=x=>(x-1)*(x-5);assert.equal(get('2.1234').rättSvar,g(3));for(let x=-5;x<=9;x+=0.25)assert.ok(g(x)>=-4);
  for(const id of r(2,1229,1234))assert.deepEqual(get(id).kurs,['2c'],id);
});
