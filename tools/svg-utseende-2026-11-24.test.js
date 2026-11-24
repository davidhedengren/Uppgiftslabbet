'use strict';
/* Figurer och kort som ser professionella ut (agent/SVG_UTSEENDE_2026-11-24.md). */
const { test } = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const ROOT = path.join(__dirname, '..');
const BANKER = ['uppgifter.js', 'uppgifter2.js', 'uppgifterma1.js', 'uppgifterma2.js', 'uppgiftermato1.js', 'uppgiftermato2.js', 'uppgiftermatf1.js'];
const las = (f) => { const s = fs.readFileSync(path.join(ROOT, f), 'utf8'); return JSON.parse(s.slice(s.indexOf('['), s.lastIndexOf(']') + 1)); };
const svgs = (q) => JSON.stringify(q).replace(/\\"/g, '"').match(/<svg[\s\S]*?<\/svg>/g) || [];

test('SVG-attribut har rätt skiftläge och inget typografiskt minus', () => {
  for (const f of BANKER) for (const q of las(f)) for (const s of svgs(q)) {
    for (const tag of s.match(/<[a-zA-Z][^<>]*>/g) || []) {
      assert.doesNotMatch(tag, /\s(viewbox|preserveaspectratio)=/, `${f} ${q.id}`);
      assert.doesNotMatch(tag, /\s[\w-]*−[\w-]*=|\s(?:dy|dx|x|y|font-size)="−/, `${f} ${q.id}`);
    }
  }
});

test('Ma5 riktningsfält: hela innehållet ryms i ramen', () => {
  const b = las('uppgiftermatf1.js');
  for (const id of ['4.84', '4.109']) assert.match(svgs(b.find((q) => q.id === id))[0], /viewBox="0 45 460 318"/, id);
  assert.match(svgs(b.find((q) => q.id === '4.110'))[0], /viewBox="0 -6 460 322"/);
});

test('Fy1 9.434: exponenten i 10⁻¹⁰ är upphöjd', () => {
  const s = svgs(las('uppgifter.js').find((q) => q.id === '9.434'))[0];
  assert.match(s, /<tspan dy="-6" font-size="[\d.]+">−10<\/tspan>/);
});

test('delbokstaven följs av mellanslag', () => {
  for (const f of ['uppgifter.js', 'uppgifter2.js']) assert.doesNotMatch(fs.readFileSync(path.join(ROOT, f), 'utf8'), /<strong>[a-h]\)<\/strong>[A-ZÅÄÖa-zåäö(]/, f);
});

test('figurtext förstorad för mobil (exempel som var 6 px)', () => {
  const fy = svgs(las('uppgifter.js').find((q) => q.id === '6.52'))[0];
  assert.match(fy, /font-size="1[5-9](?:\.\d+)?"[^>]*>fönster</);
  const ma4 = las('uppgiftermato2.js').find((q) => q.id === '2.51');
  assert.ok(svgs(ma4).length > 0);
});

const KG = path.join(ROOT, '..', 'kunskapsgymmet', 'index.html');
test('Kunskapsgymmet: typsnitt, svarsrutor, verktygsrad, listor och facit i mobil', { skip: !fs.existsSync(KG) }, () => {
  const h = fs.readFileSync(KG, 'utf8');
  assert.match(h, /family=IBM\+Plex\+Mono/);
  assert.match(h, /\.ainputs\{[^}]*grid-template-columns:minmax\(0,1fr\)/);
  assert.match(h, /\.hm-grupp\{flex:1 0 100%;flex-wrap:wrap/);
  assert.match(h, /\.tbody ol:not\(\.facit-steglista\)>li::before\{counter-increment:kgdel;content:counter\(kgdel,lower-alpha\) "\)"/);
  assert.match(h, /\.facit-del\{display:block\}/);
  assert.match(h, /svg\[style\*="min-width:420px"\]\{min-width:0!important\}/);
});
