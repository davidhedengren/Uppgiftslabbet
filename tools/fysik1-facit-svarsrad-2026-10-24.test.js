const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('fs'),vm=require('vm'),path=require('path');
const ctx={window:{}};vm.runInNewContext(fs.readFileSync(path.join(__dirname,'../uppgifter.js'),'utf8'),ctx);const bank=ctx.window.BANK,q=id=>bank.find(t=>t.id===id);
const svar=s=>[...String(s).matchAll(/<p class="facit-svar"><strong>Svar:<\/strong> ([\s\S]*?)<\/p>/g)].map(m=>m[1]);

// Se agent/FYSIK1_FACIT_SVARSRAD_2026-10-24.md. Kapitel 9 hanteras av en annan session.
test('Fy1-facit: svaret står i en svarsruta, inte i ett löst fetstilt stycke',()=>{
 for(const t of bank){
  if(t.kap===9)continue;
  assert.doesNotMatch(t.s,/<p><strong>\s*Svar:/,`${t.id}: löst svarsstycke`);
  for(const s of svar(t.s))assert.doesNotMatch(s,/<\/?strong>|<p[\s>]/,`${t.id}: ${s}`);
 }
 assert.ok(bank.filter(t=>/facit-svar/.test(t.s)).length>=1990);
});

test('Runda 1 och 2: styckeform, förklaring före formeln och kommentar före svaret',()=>{
 for(const id of ['3.609','4.826','4.830','9.431']){
  assert.doesNotMatch(q(id).s,/facit-steglista/,id);
  assert.match(q(id).s,/^<div class="facit-v2 facit-stegvis"><div class="facit-forklaring"><div class="facit-stycke"><p class="facit-metod">/,id);
 }
 // 5.32 c: kommentaren om minustecknet står före svarsrutan, och värdet stämmer: 0,15·(−25) − 0,15·20.
 assert.ok(Math.abs(0.15*-25-0.15*20-(-6.75))<1e-12);
 assert.match(q('5.32').s,/<p>Minustecknet betyder att impulsen är riktad åt vänster\.<\/p><p class="facit-svar"><strong>Svar:<\/strong> −6,75 Ns\.<\/p>/);
 assert.deepEqual(svar(q('4.64').s),['30 N.','180 N/m.','0,08 m (8 cm).']);
});

// Runda 3: talet i en genererad svarsruta ska stämma med rättSvar inom toleransen.
const tal=x=>{const m=x.match(/^\\\((-?)([\d\\,]+)(?:\{,\}(\d+))?(?:\\cdot10\^\{(-?\d+)\})?\\\)/);if(!m)return null;
 return (m[1]?-1:1)*Number(m[2].replace(/\\,/g,'')+'.'+(m[3]||'0'))*10**Number(m[4]||0);};
test('Runda 3: svarsrutans tal stämmer med självrättningen',()=>{
 let n=0;
 for(const t of bank){
  if(t.kap===9||t.svarstyp!=='numeriskt'||typeof t.rättSvar!=='number')continue;
  const s=svar(t.s);if(s.length!==1)continue;const v=tal(s[0]);if(v===null)continue;
  const tol=Math.max(t.tolerans||0,Math.abs(t.rättSvar)*1e-9);
  // Facit får visa ett grövre avrundat värde än toleransen, men aldrig ett annat tal.
  const steg=10**Math.floor(Math.log10(Math.abs(v)||1))/10;
  if(Math.abs(v-t.rättSvar)<=tol*1.0001+1e-12){n++;continue;}
  assert.ok(Math.abs(v-t.rättSvar)<=Math.max(tol,steg*5),`${t.id}: ${s[0]} mot ${t.rättSvar}`);
 }
 assert.ok(n>=590,`kontrollerade svarsrutor: ${n}`);
 assert.equal(svar(q('2.210').s)[0],'\\(3{,}50\\cdot10^{-4}\\) A.');
 assert.equal(svar(q('4.77').s)[0],'\\(48{,}6\\)°.');
 assert.equal(svar(q('7.227').s)[0],'Värmestrålning.');
});
