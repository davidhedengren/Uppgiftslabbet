'use strict';
/* Fy1 kopplingar: fler kretsar på E-nivå, 8.782–8.811 (agent/FY1_KOMPLEXA_KOPPLINGAR_2026-11-24.md). */
const { test } = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const s = fs.readFileSync(path.join(__dirname, '..', 'uppgifter.js'), 'utf8');
const bank = JSON.parse(s.slice(s.indexOf('['), s.lastIndexOf(']') + 1));
const q = (id) => bank.find((x) => x.id === id);
const par = (...r) => 1 / r.reduce((a, x) => a + 1 / x, 0);
const IDS = Array.from({ length: 30 }, (_, i) => `8.${782 + i}`);

const VANTAT = {
  '8.787': 9 - 3.5, '8.788': 2 + 4, '8.789': 450 - 180, '8.790': 12 / 24, '8.791': (15 * 0.40) / (1.2 - 0.40),
  '8.792': 18 - 25 * 0.40, '8.793': 0.30, '8.794': 2.5 + 3.5, '8.795': par(30, 30, 30), '8.796': 9 / 12, '8.797': 230 / 10,
  '8.798': par(20, 20), '8.799': 4.5 / 15, '8.800': 4 + 2.5 + 3.5, '8.801': par(30, 30, 30) + 15, '8.802': 18 + par(18, 18, 18),
  '8.803': par(12, 4) + par(10, 15), '8.804': par(4.7 + 5.3, 10), '8.805': 6 / 12 + 6 / 6 + 6 / 4, '8.806': 6 / (8 + 4),
  '8.807': 4 * 12 / (8 + 4), '8.808': 5 * 6 / (5 + 10), '8.809': 4 * 6 / (8 + 4), '8.810': 10 * 0.60 / 2, '8.811': 100 * (0.020 + 0.030),
};
const FLERVAL = { '8.782': 'R₂ och R₃', '8.783': 'R₂ och R₃', '8.784': 'L₂ och L₃', '8.785': 'A₁', '8.786': 'Den ökar' };

test('30 nya E-uppgifter på träningsnivå 1–2, var och en med figur', () => {
  const n = { 1: 0, 2: 0 };
  for (const id of IDS) {
    const u = q(id);
    assert.ok(u, id);
    assert.equal(u.omr, 'kopplingar', id);
    assert.equal(u.niva, 'E', id);
    assert.ok([1, 2].includes(u.traningsniva), id);
    n[u.traningsniva]++;
    assert.match(u.t, /<svg[\s\S]*<\/svg>/, id);
    assert.match(u.s, /facit-svar/, id);
    assert.ok(u.ledtrad.length > 20, id);
    assert.doesNotMatch(u.t.replace(/<svg[\s\S]*?<\/svg>/g, ''), /Avrunda|Svara (?:med|exakt)|decimal/, id);
    const vb = u.t.match(/viewBox="0 0 ([\d.]+) ([\d.]+)"/);
    assert.ok(vb && +vb[1] <= 420, `${id}: bredd ${vb && vb[1]}`);
  }
  assert.ok(n[1] >= 15 && n[2] >= 12, JSON.stringify(n));
});

test('svaren stämmer med oberoende beräkningar', () => {
  for (const [id, v] of Object.entries(VANTAT)) assert.ok(Math.abs(q(id).rättSvar - v) < 1e-9 * Math.max(1, v), `${id}: ${q(id).rättSvar} ≠ ${v}`);
});

test('flerval: ett rätt alternativ och kommentarer', () => {
  for (const [id, txt] of Object.entries(FLERVAL)) {
    const a = q(id).alternativ;
    assert.equal(a.filter((x) => x.ratt).length, 1, id);
    assert.equal(a.find((x) => x.ratt).txt, txt, id);
    for (const x of a) assert.ok(x.kommentar.length > 10, id);
  }
});
