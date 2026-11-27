'use strict';
// Kvalitetsrapporten i Kunskapsgymmet 2026-11-27 (agent/KVALITETSRAPPORT_2026-11-27.md).
const { test } = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const las = (f) => { const s = fs.readFileSync(path.join(__dirname, '..', f), 'utf8'); return JSON.parse(s.slice(s.indexOf('['), s.lastIndexOf(']') + 1)); };
const fy1 = las('uppgifter.js');
const ma2 = las('uppgifterma2.js');
const hitta = (b, id) => b.find((x) => String(x.id) === id);
const vb = (svg) => svg.match(/viewBox="([^"]+)"/)[1].split(/\s+/).map(Number);
const forsta = (q) => q.t.match(/<svg[\s\S]*?<\/svg>/)[0];

test('Ma2 3.67 rättas som uttryck, inte som LaTeX-sträng', () => {
  const q = hitta(ma2, '3.67');
  assert.equal(q.rättSvar, 'y=45-x/2');
  assert.equal(q.svarFormat, 'uttryck');
  assert.match(q.s, /45\^\\circ-\\frac\{x\}\{2\}/);
});

test('Figurer med text utanför bilden har vidgad ram (IBM Plex Mono)', () => {
  // 8.16: ”R₂ = 1000 Ω” börjar vid x = 447 och är cirka 105 enheter bred med IBM Plex Mono
  const [x, , w] = vb(forsta(hitta(fy1, '8.16')));
  assert.ok(x + w >= 551, `8.16 slutar vid ${x + w}`);
  // 3.131: ”240 m” står till vänster om x = 0, och land- och vattenbanden följer med till den nya kanten
  const s3131 = forsta(hitta(fy1, '3.131'));
  assert.ok(vb(s3131)[0] < -5);
  assert.match(s3131, new RegExp(`<rect x="${vb(s3131)[0]}" y="60" width="${vb(s3131)[2]}" height="140" fill="#DCE6F2"`));
  // 8.31: alla fyra etiketter ryms
  const [x31, , w31] = vb(forsta(hitta(fy1, '8.31')));
  assert.ok(x31 < 5 && x31 + w31 > 545);
});

test('Fy1 4.852: friktionsetiketten ligger inte på rampens kant', () => {
  const svg = forsta(hitta(fy1, '4.852'));
  assert.match(svg, /<text x="335" y="178" fill="#22764a"[^>]*>f = 20 N<\/text>/);
  // rampens kant går från (45, 287,3) till (455, 69,3); etikettens överkant (y ≈ 165) ligger under kanten
  const kantY = (x) => 287.3146847578291 + (x - 45) * (69.31381777662283 - 287.3146847578291) / 410;
  assert.ok(178 - 13 > kantY(300) && 178 - 13 > kantY(370));
});

test('Fy1: inga kortinledningar i plural i de omskrivna uppgifterna', () => {
  const plural = /varje (?:del|fall)|i alla tre fallen/i;
  for (const id of ['4.747', '4.647', '6.88', '6.530', '6.538', '7.139']) {
    const q = hitta(fy1, id);
    assert.doesNotMatch(q.spelIntro || '', plural, id);
    assert.doesNotMatch(q.t.replace(/<svg[\s\S]*?<\/svg>/g, ''), plural, id);
  }
  for (const id of ['4.747', '4.647', '6.530']) {
    const q = hitta(fy1, id);
    for (const d of q.spelDelar) assert.ok(d.t.startsWith(q.spelIntro), `${id}${d.etikett}`);
  }
});

test('SVG-granskningen laddar IBM Plex Mono innan den mäter', () => {
  const kod = fs.readFileSync(path.join(__dirname, 'granska-svg.js'), 'utf8');
  assert.match(kod, /fonts\.googleapis\.com\/css2\?family=IBM\+Plex\+Mono/);
  assert.match(kod, /document\.fonts\.load/);
  assert.match(kod, /plexSaknas/);
});
