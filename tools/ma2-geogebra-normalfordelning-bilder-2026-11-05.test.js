'use strict';
// Skärmbilder från GeoGebras Sannolikhetskalkylator i Ma2-facit (MA2_NORMALFORDELNING_GEOGEBRA_BILDER_2026-11-05.md).
const test = require('node:test');
const assert = require('node:assert');
const fs = require('fs');
const path = require('path');

const root = path.resolve(__dirname, '..');
const src = fs.readFileSync(path.join(root, 'uppgifterma2.js'), 'utf8');
const bank = JSON.parse(src.slice(src.indexOf('['), src.lastIndexOf(']') + 1));
const q = (id) => bank.find((u) => u.id === id);

// Värden som GeoGebra 5.4.916 (svenska) visade efter likhetstecknet.
const VISAT = {
  '4.44': ['4-44', '0.8186'], '4.81': ['4-81', '0.6506'], '4.2086': ['4-2086', '0.6147'], '4.2121': ['4-2121', '0.7501'],
  '4.257': ['4-257', '0.84'], '4.89': ['4-89', '0.9332'], '4.100': ['4-100', '0.9088'], '4.123': ['4-123', '0.8944'],
  '4.124': ['4-124', '0.8413'], '4.152': ['4-152', '0.8413'], '4.237': ['4-237', '0.8413'], '4.522': ['4-522', '0.8944'],
  '4.524': ['4-524', '0.1217'], '4.525': ['4-525', '0.1056'], '4.527': ['4-527', '0.2023'], '4.2122': ['4-2122', '0.0824'],
  '4.2124': ['4-2124', '0.0228'],
};
const NormalCdf = (x, mu, s) => { // Abramowitz–Stegun 7.1.26 räcker för fyra decimaler
  const z = (x - mu) / (s * Math.SQRT2), t = 1 / (1 + 0.3275911 * Math.abs(z));
  const y = 1 - (((((1.061405429 * t - 1.453152027) * t) + 1.421413741) * t - 0.284496736) * t + 0.254829592) * t * Math.exp(-z * z);
  return 0.5 * (1 + Math.sign(z) * y);
};

test('varje facit visar vägen till kalkylatorn och en bild av uppgiftens egen beräkning', () => {
  for (const [id, [sl, v]] of Object.entries(VISAT)) {
    const s = q(id).s;
    assert.ok(s.includes('bilder/geogebra-sannolikhet-perspektiv.png'), id);
    assert.ok(s.includes(`bilder/geogebra-${sl}.png`), id);
    assert.ok(fs.statSync(path.join(root, `bilder/geogebra-${sl}.png`)).size > 5000, id);
    assert.match(s, /Perspektiv<\/strong> och sedan <strong>Sannolikhet/);
    assert.ok(s.includes(`Efter likhetstecknet (5) står ${v}.`), id);
    assert.equal(q(id).geogebra, true, id);
    assert.equal(q(id).miniräknare, true, id);
  }
  for (const k of ['a', 'b']) assert.ok(q('4.2092').s.includes(`bilder/geogebra-4-2092-${k}.png`));
});

test('GeoGebras värden stämmer med en oberoende beräkning', () => {
  const fall = { '4.44': NormalCdf(124, 100, 12) - NormalCdf(88, 100, 12), '4.89': NormalCdf(62, 50, 8), '4.524': NormalCdf(160, 167, 6), '4.2124': NormalCdf(2, 3.2, 0.6), '4.257': NormalCdf(6.05, 5.9, 0.05) - NormalCdf(5.85, 5.9, 0.05) };
  for (const [id, p] of Object.entries(fall)) assert.ok(Math.abs(p - +VISAT[id][1]) < 0.0001, `${id}: ${p}`);
});

test('rubrikerna är skrivna för sin uppgift och svarsraden börjar med Svar:', () => {
  const rub = (h) => [...h.matchAll(/class="facit-rubrik">([\s\S]*?)<\/p>/g)].map((m) => m[1]);
  const var_ = {};
  for (const id of [...Object.keys(VISAT), '4.2092']) {
    const s = q(id).s;
    assert.match(s, /<p class="facit-svar"><strong>Svar:<\/strong>/, id);
    for (const r of new Set(rub(s))) (var_[r] = var_[r] || new Set()).add(id);
  }
  assert.deepEqual(Object.entries(var_).filter(([, v]) => v.size > 1).map(([r, v]) => `${r}: ${[...v]}`), []);
});
