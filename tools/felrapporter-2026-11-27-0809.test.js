'use strict';
// Felrapporter 2026-11-27 08:09 (agent/FELRAPPORTER_2026-11-27_0809.md).
const { test } = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const las = (f) => { const s = fs.readFileSync(path.join(__dirname, '..', f), 'utf8'); return JSON.parse(s.slice(s.indexOf('['), s.lastIndexOf(']') + 1)); };
const fy1 = las('uppgifter.js');
const ma3 = las('uppgiftermato1.js');
const hitta = (b, id) => b.find((x) => x.id === id);
const svarsrader = (s) => [...s.matchAll(/<p(?: class="facit-svar")?>(?:<strong>Svar:<\/strong>|Svar:)(.*?)<\/p>|<p><strong>Svar:((?!<\/strong>).*?)<\/strong>/g)].map((m) => (m[1] ?? m[2]).trim());

test('Fy1 4.271: två värdesiffror och exakt rättSvar; facit oförändrat', () => {
  const q = hitta(fy1, '4.271');
  assert.deepEqual(q.svarVardesiffror, [2, 2, 2]);
  assert.equal(q.rättSvar[0], 122.75);
  assert.equal(q.rättSvar[1], 3068.75);
  assert.ok(Math.abs(q.rättSvar[2] - 16 / 3) < 1e-12);
  assert.deepEqual(svarsrader(q.s), ['122,75 N.', '3068,75 N/m.', '5,33 cm.']);
  assert.match(q.t, /Den extra lasten fördelas lika/);
  assert.doesNotMatch(JSON.stringify(q), /Bortse från övrig deformation|Extra lasten/);
});

test('Fy1: inga 5–7 värdesiffror utom där data eller omvandling kräver det', () => {
  const tillatna = new Set(['6.38', '6.138', '7.31', '9.389', '9.392', '9.397', '9.403', '9.572', '6.505', '5.470', '6.152']);
  const hog = fy1.filter((q) => [].concat(q.svarVardesiffror ?? []).some((n) => Number.isInteger(n) && n >= 5)).map((q) => q.id);
  assert.deepEqual(hog.filter((id) => !tillatna.has(id)), []);
  // absoluttryck: fyra värdesiffror, så att bara lufttrycket inte godtas
  for (const id of ['6.255', '6.259', '6.265', '6.309']) assert.equal(hitta(fy1, id).svarVardesiffror, 4, id);
  assert.deepEqual(hitta(fy1, '6.8').svarVardesiffror, [2, 4, 3]);
});

test('Fy1 3.283: frågan säger vad komposanten är och vilken riktning som är positiv', () => {
  const q = hitta(fy1, '3.283');
  assert.match(q.spelDelar[0].fraga, /hur långt personen förflyttar sig i x-led/);
  assert.match(q.spelDelar[1].fraga, /uppåt räknas positivt och nedåt negativt/);
  for (const d of q.spelDelar) assert.ok(d.t.startsWith(q.spelIntro), d.etikett);
  assert.deepEqual(q.rättSvar, [5, -2]);
  assert.doesNotMatch(q.t, /[Ss]vara med tecken/);
});

test('Ma3c: talen på axlarna står intill axlarna (1.904 m.fl.)', () => {
  const ids = ['1.865', '1.871', '1.896', '1.904', '1.907', '1.910', '2.1149', '2.1152', '2.1164', '2.1165', '2.1166',
    '2.1169', '2.1173', '3.1195', '3.1197'];
  for (const id of ids) {
    const svg = hitta(ma3, id).t.match(/<svg[\s\S]*?<\/svg>/)[0];
    assert.doesNotMatch(svg, /<text x="49" /, id);              // y-talen stod vid ramens vänsterkant
    assert.doesNotMatch(svg, /<text x="[\d.]+" y="302" /, id);  // x-talen stod under ramen
    assert.equal((svg.match(/>0<\/text>/g) || []).length, 1, id); // nollan en gång
    assert.match(svg, /L443 [\d.]+ M435/, id);                  // x-axeln har pil
  }
  // 1.904: x-talen under x-axeln (y = 144) och y-talen vid y-axeln (x = 245)
  const svg = hitta(ma3, '1.904').t;
  assert.match(svg, /<text x="393" y="165"[^>]*>2<\/text>/);
  assert.match(svg, /<text x="237" y="81"[^>]*>4<\/text>/);
  // stapeldiagrammet 1.895 och 3.1204 (redan rätt) är orörda
  assert.match(hitta(ma3, '1.895').t, /<text x="49" /);
});
