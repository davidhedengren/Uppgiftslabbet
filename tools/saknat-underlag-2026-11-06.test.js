'use strict';
const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('fs'),vm=require('vm'),cp=require('child_process');
const IDS={ma1:['0.329','0.403','0.727','0.728','6.405','7.38','7.437','1.1187'],ma2:['2.568','2.721','3.104','3.106','3.328'],mato1:['2.800','3.551','3.727'],mato2:['4.460'],matf1:['4.513','4.587','4.588'],fy1:['4.824','4.828','3.442','2.345'],fy2:['3.521','4.305','4.317']};
const banks={},ctx={},html=fs.readFileSync('index.html','utf8');
for(const b of Object.keys(IDS)){const c={window:{}};vm.runInNewContext(fs.readFileSync(b==='fy1'?'uppgifter.js':b==='fy2'?'uppgifter2.js':'uppgifter'+b+'.js','utf8'),c);banks[b]=Object.values(c.window).find(Array.isArray);}
const q=(b,id)=>banks[b].find(q=>q.id===id);
for(const n of ['altVisas','uppgiftsText','altFacit']){const i=html.indexOf('function '+n+'(');vm.runInNewContext(html.slice(i,html.indexOf('\n}',i)+2),ctx)}ctx.altBokstav=i=>String.fromCharCode(65+i);
test('27 granskade alternativlistor visas en gång, med fullständiga facit och kommentarer',()=>{
 let count=0;
 for(const [b,ids] of Object.entries(IDS))for(const id of ids){count++;const x=q(b,id);
  assert.equal(x.visaAlternativ,true,id);assert.equal(ctx.altVisas(x),true,id);
  assert.equal((ctx.uppgiftsText(x).match(/class="ul-alt"/g)||[]).length,x.alternativ.length,id);
  assert.match(x.s,/facit-steglista/);assert.match(x.s,/facit-rubrik/);assert.match(x.s,/facit-svar/);
  for(const a of x.alternativ){assert.ok(ctx.uppgiftsText(x).includes(a.txt));if(!a.ratt)assert.ok(a.kommentar?.length>8,id);else assert.ok(ctx.altFacit(x).includes(a.txt),id)}
  assert.equal(x.geogebra,false,id);assert.equal(typeof x.miniräknare,'boolean',id);assert.ok(x.traningsniva>=1&&x.traningsniva<=5,id);
 }
 assert.equal(count,27);
});
test('Givna påståenden A och B är inte svarsalternativ och döljer inte svaren',()=>{
 for(const id of ['3.104','3.106']){const x=q('ma2',id);assert.match(x.t,/A:/);assert.match(x.t,/B:/);assert.equal(ctx.altVisas(x),true);assert.equal(ctx.altVisas({...x,visaAlternativ:undefined}),false);}
});
test('Öppna frågor och befintliga figur-/textlistor behåller sin visning',()=>{
 for(const [b,id] of [['ma1','0.36'],['ma1','0.166'],['ma1','0.167'],['ma2','2.58'],['fy2','5.1'],['fy2','3.150'],['ma2','2.410'],['ma2','2.764'],['mato2','4.565']])assert.equal(ctx.altVisas(q(b,id)),false,b+' '+id);
 assert.equal(ctx.altVisas({visaAlternativ:true,t:'Fråga',alternativ:[]}),false);
 assert.equal(ctx.altVisas({visaAlternativ:true,t:'Figur A–B',alternativ:[{txt:'A'},{txt:'B'}]}),false);
});
test('Taluppgifter och fysikens numeriska samband ger rätt alternativ',()=>{
 const flags=(b,id)=>Array.from(q(b,id).alternativ,a=>a.ratt);
 assert.deepEqual(flags('ma1','0.329'),[false,false,true]);
 assert.deepEqual(flags('ma1','0.403'),[2.495,2.405,2.505,2.59].map(n=>n>2.49&&n<2.50));
 assert.deepEqual(flags('ma1','0.727'),[3.15,3.24,3.2,3.26].map(n=>Math.round(n*10)!==32));
 assert.deepEqual(flags('ma1','0.728'),[45,53,46,44].map(n=>Math.round(n/10)!==5));
 assert.deepEqual(flags('ma1','6.405'),[(6+10+14)/3,6+10+14/3,(6+10)*14/3,6+(10+14)/3].map(n=>n===10));
 assert.ok(850000/1e6>.8&&850000/1e6>750/1000);
 assert.deepEqual(flags('ma1','7.38'),[false,false,false,true]);
 assert.equal((10-2)/4,(14-6)/4);assert.equal(400/80,5);
 assert.deepEqual(flags('fy1','3.442'),[false,false,true]);assert.deepEqual(flags('fy1','2.345'),[false,false,false,true]);
 assert.deepEqual(flags('ma2','3.104'),[true,false,false,false]);assert.ok((-5)**2>16&& !(-5>4));
 assert.deepEqual(flags('ma2','3.106'),[true,false,false,false]);assert.ok(3>2&&!(3>5));
});
test('Symbolisk kontroll av uttryck, primitiva funktioner och differentialekvationer',()=>{
 const result=cp.spawnSync('python',['-c',String.raw`
import sympy as s
x,t=s.symbols('x t',real=True)
assert s.expand(x*x-(x-2)**2)==4*x-4
assert s.expand(4*(x-1))==4*x-4
assert [s.diff(f,x)==6*x*x-4*x+3 for f in [2*x**3-2*x*x+3*x,3*x*x-4*x+3,2*x**3-4*x*x+3,6*x**3-2*x*x+3*x]]==[True,False,False,False]
assert [s.diff(f,x)==x**3-2*x for f in [3*x*x-2,x**4/4-4*x,x**4/4-x*x,x**4-2*x*x]]==[False,False,True,False]
assert s.solveset(s.sqrt(x+6)-x,x,domain=s.S.Reals)==s.FiniteSet(3)
functions=[s.Rational('19.64')*(1-s.exp(-t/2)),s.Rational('19.64')*s.exp(t/2),s.Rational('9.82')*t*t,t/2]
assert [f.subs(t,0)==0 and s.simplify(s.diff(f,t)-(s.Rational('9.82')-f/2))==0 for f in functions]==[True,False,False,False]
assert [s.simplify(x*s.diff(f,x)-2*f)==0 for f in [x*x,3*x*x,x*x+1,x**3]]==[True,True,False,False]
assert [s.simplify(s.diff(f,x,2)+9*f)==0 for f in [s.sin(3*x),s.cos(3*x),s.exp(3*x),s.sin(9*x)]]==[True,True,False,False]
`],{encoding:'utf8'});assert.equal(result.status,0,result.stderr);
 for(const id of ['4.587','4.588'])assert.deepEqual(Array.from(q('matf1',id).alternativ,a=>a.ratt),[true,true,false,false]);
 assert.equal(q('matf1','4.513').miniräknare,true);assert.doesNotMatch(q('matf1','4.513').ledtrad,/kraftbalans|terminalhastighet/);
 assert.match(q('matf1','4.587').s,/helt intervall/);
});
test('Fy1 3.32 ger uttryckligen konstant acceleration i båda faserna',()=>{
 const x=q('fy1','3.32');assert.equal((x.t.match(/konstant acceleration/g)||[]).length,2);
 assert.equal(x.spel,false);assert.equal(x.självrättning,false);assert.equal(x.miniräknare,true);
 assert.match(x.t,/Rita ett v-t-diagram/);assert.match(x.s,/<svg/);
 assert.equal(6*8/2+10*8+4*8/2,120);assert.equal(120/(6+10+4),6);
 // Fem kontrollfall: samma information finns uttryckligen eller är själva
 // frågan i uppgiften om vad mätningar kan och inte kan visa.
 assert.match(q('fy1','3.24').t,/konstant acceleration/);
 assert.match(q('fy1','3.31').t,/0,50 m\/s²/);
 assert.match(q('fy1','3.38').t,/vilket antagande behövs/);
 assert.match(q('fy1','3.114').t,/ändras jämnt/);
 assert.match(q('fy1','3.367').t,/accelererar jämnt/);assert.match(q('fy1','3.367').t,/bromsar till sist jämnt/);
 assert.equal(16/8,2);assert.equal(8*16/2,64);
 assert.equal(4/.5,8);assert.equal(2*4/.5,16);
 assert.equal((-2-(-6))/(4-2),2);
 assert.equal(40+25+(3000-40*20/2-25*20/2)/20,182.5);
});
