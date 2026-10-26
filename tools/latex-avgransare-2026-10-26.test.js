'use strict';
/* Matematik som tappat sina LaTeX-avgränsare (”(x)” i stället för \(x\)) i Ma2 och Matf1, rättat 2026-10-26.
   Testet söker igenom textfälten i båda bankerna. Unicode-matematik i löptext (A′(x), y(0)) räknas inte,
   eftersom en primtecken- eller bokstavsföregångare undantas. */
const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('node:fs'),vm=require('node:vm'),path=require('node:path');
const bank=f=>{const c={window:{}};vm.runInNewContext(fs.readFileSync(path.join(__dirname,'..',f),'utf8'),c);return Object.values(c.window).find(Array.isArray);};
const re=/(^|[^\\A-Za-zåäöÅÄÖ0-9_^{}′'])\(([a-z](?:_\d)?)\)/,ENH=new Set(['m','s','h','g','l']);
const utanMatte=s=>s.replace(/<svg[\s\S]*?<\/svg>/g,'').replace(/\\\([\s\S]*?\\\)/g,'M').replace(/\\\[[\s\S]*?\\\]/g,'M').replace(/<[^>]+>/g,' ');
for(const f of ['uppgifterma2.js','uppgiftermatf1.js'])test(`${f}: ingen matematik utan LaTeX-avgränsare`,()=>{
  for(const q of bank(f))for(const s of [q.t,q.s,q.ledtrad,q.spelIntro,...(q.spelDelar||[]).flatMap(d=>[d.t,d.s,d.ledtrad,d.fraga])]){if(typeof s!=='string')continue;
    const m=utanMatte(s).match(re);assert.ok(!m||ENH.has(m[2]),`${q.id}: ${m&&m[0]}`);}
});
test('Matf1: de rättade ledtrådarna',()=>{
  const B=bank('uppgiftermatf1.js'),g=id=>B.find(q=>q.id===id).ledtrad;
  assert.ok(g('2.28').includes(String.raw`\(a\equiv b\pmod n\)`));assert.ok(g('1.127').includes(String.raw`\(x\)`));
  for(const id of ['1.35','1.102','1.226'])assert.ok(g(id).includes(String.raw`exakt \(k\)`),id);
});
