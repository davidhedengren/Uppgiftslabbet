'use strict';
/* Facitgranskning 2026-10-25 av dagens 489 nya kort (lärarbeslut: facit, ledtråd och svar ska alltid granskas noggrant).
   Matematikfacit följer Ma1 1.116: varje steg har en uppgiftsspecifik facit-rubrik med beräkningen i samma steg.
   Fysikfacit har en metodtext. Inga råa < eller > i matte. Svarsrad finns. Felaktiga flervalsalternativ har kommentar. */
const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('node:fs'),vm=require('node:vm'),path=require('node:path');
const r=(p,a,b)=>Array.from({length:b-a+1},(_,i)=>`${p}.${a+i}`);
const SETS={
 'uppgifterma1.js':[...r(2,632,645),...r(5,641,684),...r(1,1551,1566),...r(0,1261,1265),...r(4,820,823),...r(7,781,796)],
 'uppgifterma2.js':[...r(1,1090,1228),...r(2,1097,1216)],
 'uppgifter.js':[...r(9,524,575),...r(3,733,745),...r(4,885,896),...r(8,636,660)],
 'uppgifter2.js':[...r(5,464,486),...r(3,538,543)]};
const bank=f=>{const c={window:{}};vm.runInNewContext(fs.readFileSync(path.join(__dirname,'..',f),'utf8'),c);return JSON.parse(JSON.stringify(Object.values(c.window).find(Array.isArray)));};
const B=Object.fromEntries(Object.keys(SETS).map(f=>[f,bank(f)]));
const kort=f=>SETS[f].map(id=>{const t=B[f].find(x=>x.id===id);assert.ok(t,id);return t;});
const GENERISK=/^(Steg \d+|Förenkla|Lös ekvationen|Beräkna|Svar|Kontroll|Kontrollera|Skriv ekvationen|Skriv funktionen|Skriv formeln|Skriv sambandet|Tolka resultatet|Dra slutsatsen|Jämför värdena|Räkna ut x)$/;

test('Matematikfacit: varje steg har en uppgiftsspecifik rubrik med beräkningen i samma steg',()=>{
  let n=0;
  for(const f of ['uppgifterma1.js','uppgifterma2.js'])for(const t of kort(f)){n++;
    const li=[...t.s.matchAll(/<li>([\s\S]*?)<\/li>/g)].map(m=>m[1]);assert.ok(li.length>0,t.id);
    for(const x of li){const m=x.match(/^<p class="facit-rubrik">([\s\S]*?)<\/p>([\s\S]+)$/);assert.ok(m,`${t.id}: steg utan rubrik eller utan innehåll`);
      assert.doesNotMatch(m[1].trim(),GENERISK,`${t.id}: generisk rubrik ”${m[1]}”`);}}
  assert.equal(n,358);
});

test('Fysikfacit har metodtext, och alla kort har svarsrad och kommenterade felalternativ',()=>{
  for(const f of Object.keys(SETS))for(const t of kort(f)){
    assert.match(t.s,/class="facit-svar"/,t.id);
    if(f==='uppgifter.js'||f==='uppgifter2.js')assert.match(t.s,/class="facit-metod"/,t.id);
    for(const a of t.alternativ||[])if(!a.ratt)assert.ok(a.kommentar,`${t.id}: ${a.txt}`);
    assert.ok(String(t.ledtrad||'').replace(/<[^>]+>/g,'').trim().length>=8,`${t.id}: ledtråd saknas`);}
});

test('Inga råa < eller > inne i matte (de kan tolkas som html-taggar)',()=>{
  const MATTE=/\\\(([\s\S]*?)\\\)|\\\[([\s\S]*?)\\\]/g;
  for(const f of Object.keys(SETS))for(const t of kort(f)){
    const falt=[t.t,t.s,t.ledtrad,...(t.alternativ||[]).flatMap(a=>[a.txt,a.kommentar])];
    for(const v of falt)for(const m of String(v||'').matchAll(MATTE))assert.doesNotMatch((m[1]??m[2]).replace(/&lt;|&gt;/g,''),/[<>]/,`${t.id}: ${m[0].slice(0,60)}`);}
});

test('Exempel: 1.1093 har rubriker som förklarar stegen och en kontroll',()=>{
  const t=B['uppgifterma2.js'].find(x=>x.id==='1.1093');
  assert.match(t.s,/facit-rubrik">\\\(x\^2\\\) finns i båda leden och tar ut varandra/);assert.match(t.s,/Kontrollera i ursprungsekvationen/);
});
