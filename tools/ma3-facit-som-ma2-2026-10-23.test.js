const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('fs'),vm=require('vm'),path=require('path');
const ctx={window:{}};vm.runInNewContext(fs.readFileSync(path.join(__dirname,'../uppgiftermato1.js'),'utf8'),ctx);const bank=ctx.window.BANKMATO1,q=id=>bank.find(q=>q.id===id);
const svar=s=>{const m=String(s||'').match(/<p class="facit-svar"><strong>Svar: ([\s\S]*?)<\/strong><\/p>/);return m?m[1]:null;};
const antal=(s,re)=>(String(s).match(re)||[]).length;

// Se agent/MA3_FACIT_SOM_MA2_2026-10-23.md.
test('Ma3-facit har steglista och svarsrad som i Ma2',()=>{
 const steg=bank.filter(t=>/facit-steglista/.test(t.s)).length,medSvar=bank.filter(t=>/facit-svar/.test(t.s)).length;
 assert.ok(steg>=2900,`steglistor: ${steg}`);assert.ok(medSvar>=2400,`svarsrader: ${medSvar}`);
 for(const t of bank){
  if(!/facit-steglista/.test(t.s))continue;
  for(const tag of ['div','ol','li'])assert.equal(antal(t.s,new RegExp('<'+tag+'[\\s>]','g')),antal(t.s,new RegExp('</'+tag+'>','g')),`${t.id}: obalanserad <${tag}>`);
  assert.doesNotMatch(t.s,/<li>\s*<\/li>|<p><\/p>/,t.id);
 }
});

test('Genererade svarsrader innehåller ingen rå kalkylatorsyntax',()=>{
 for(const t of bank){
  const s=svar(t.s);if(s===null)continue;
  assert.doesNotMatch(s,/sqrt\(|\)\s*\/\s*\(|\^\(|\*|\\dfrac\{-|e-0\d|(?<![\\a-z])pi\b/,`${t.id}: ${s}`);
  assert.doesNotMatch(s,/\{,\}\d*0\\\)/,`${t.id}: avslutande nolla i ${s}`);
 }
 assert.equal(svar(q('3.309').s),'\\(\\dfrac{x^6}{3}-\\dfrac{x^3}{3}+7x+C\\)');
 assert.equal(svar(q('3.134').s),'\\(F(x)=\\dfrac{2x^{3/2}}{3}+C\\)');
 assert.equal(svar(q('2.127').s),'a) \\(-\\dfrac{1}{x^2}+\\dfrac{5}{2\\sqrt{x}}\\), b) \\(\\dfrac{3(x^{7/2}+2)}{x^3}\\)');
 assert.equal(svar(q('4.29').s),'\\(-\\dfrac{3}{2}\\)');
 assert.equal(svar(q('3.462').s),'a) \\(2{,}958\\), b) \\(3\\), c) \\(0{,}042\\)');
});

test('Handskrivna svarsrader stämmer med egen räkning',()=>{
 // 3.38: intäkt 100x(120-2x) kr, max vid x=30.
 const R=x=>100*x*(120-2*x);assert.equal(R(30),180000);assert.ok(R(29)<R(30)&&R(31)<R(30));assert.match(svar(q('3.38').s),/x=30.*180\\,000/);
 // 3.27: x^2+ax-6 har nollstället 2 om a=1, och (x^2+x-6)/(x-2)=x+3 → 5.
 assert.equal(4+2*1-6,0);assert.match(svar(q('3.27').s),/a=1.*5/);
 // 3.478: x^3-4x är udda; arean är 2·∫0^2(4x-x^3)dx = 8.
 assert.equal(2*(2*2**2-2**4/4),8);assert.match(svar(q('3.478').s),/0.*8/);
 // 4.172: Z=3x+5y i hörnen (0,0),(0,8),(4,4),(6,0).
 const Z=[[0,0],[0,8],[4,4],[6,0]].map(([x,y])=>3*x+5*y);assert.equal(Math.max(...Z),40);assert.equal(Z.indexOf(40),1);assert.match(svar(q('4.172').s),/Z=40.*0,\\,8/);
 // 3.231 och 3.235: extrempunkter.
 const f=x=>x**3-3*x;assert.equal(f(-1),2);assert.equal(f(1),-2);assert.match(svar(q('3.231').s),/\(-1,\\,2\).*\(1,\\,-2\).*y=-3x/);
 assert.match(svar(q('3.235').s),/\(0,\\,0\).*-a\^2.*2\\sqrt a/);
 // 2.282: f'(x)=3(x-1)(x-3) byter tecken + → − vid 1 och − → + vid 3.
 const d=x=>3*(x-1)*(x-3);assert.ok(d(0.9)>0&&d(1.1)<0&&d(2.9)<0&&d(3.1)>0);assert.match(svar(q('2.282').s),/maximipunkt.*x=1.*minimipunkt.*x=3/);
 for(const id of ['1.451','1.491','2.29','2.121','2.422','2.423','2.231','3.237','1.212'])assert.ok(svar(q(id).s),id);
});

test('Uppgifter med deluppgifter eller bevis får inga ofullständiga svarsrader',()=>{
 for(const id of ['3.149','3.217','3.774','4.197','4.207'])assert.equal(svar(q(id).s),null,id);
 for(const id of ['2.124','2.129','2.134','2.413','2.414'])assert.doesNotMatch(q(id).s,/facit-steglista/,id);
});
