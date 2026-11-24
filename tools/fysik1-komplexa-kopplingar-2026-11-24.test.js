'use strict';
/* Fy1 kopplingar: mängdträning på komplexa kopplingar 8.740–8.781 (agent/FY1_KOMPLEXA_KOPPLINGAR_2026-11-24.md).
   Svaren räknas om oberoende av byggskriptet. */
const { test } = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const s = fs.readFileSync(path.join(__dirname, '..', 'uppgifter.js'), 'utf8');
const bank = JSON.parse(s.slice(s.indexOf('['), s.lastIndexOf(']') + 1));
const q = (id) => bank.find((x) => x.id === id);
const par = (...r) => 1 / r.reduce((a, x) => a + 1 / x, 0);
const nara = (a, b, id) => assert.ok(Math.abs(a - b) <= 1e-9 * Math.max(1, Math.abs(b)), `${id}: ${a} ≠ ${b}`);
const IDS = Array.from({ length: 42 }, (_, i) => `8.${740 + i}`);

const VANTAT = {
  '8.740': 12 - 4, '8.741': 0.90 - 0.35, '8.742': par(8, 8), '8.743': 15 + 25, '8.744': 9 - 3.6, '8.745': 15 * 0.40,
  '8.746': 2 * 4.5, '8.747': 7.5, '8.748': 10 + 6 + 5, '8.749': 0.20 + 0.30 + 0.15,
  '8.750': 4 + par(6, 12), '8.751': par(10 + 20, 30), '8.752': par(6, 3) + par(4, 4), '8.753': 9 / (par(10, 15) + 3),
  '8.754': 1.2 * par(20, 30), '8.755': 6 / (10 + 20), '8.756': par(12 + 12, 12), '8.757': (30 * 0.20) / (0.60 - 0.20),
  '8.758': par(10, 10, 2 + 3), '8.759': 8 * 12 / (4 + 8), '8.760': 2.2 + par(5.6, 5.6), '8.761': 9 / (1000 + par(2000, 2000)) * 1000,
  '8.764': ((12 / (2 + par(6, 3))) * par(6, 3)) / 3,
  '8.765': 5 * 24 / (3 + par(8, 8) + 5),
  '8.766': ((6 / (2 + par(12, 6))) * par(12, 6)) / 12,
  '8.767': ((12 / (5 + par(30, 30))) * par(30, 30)) / 30,
  '8.768': 2 * ((18 / (par(6, 6) + 3)) / 2) ** 2,
  '8.770': 12 / (10 + par(10, 10)) - 12 / 20,
  '8.771': ((24 / (par(6, 3) + par(4, 4))) * par(6, 3)) / 3,
  '8.772': 40 * (230 / 80) ** 2,
  '8.773': 1 / (1 / (16 - 10) - 1 / 15),
  '8.775': (() => { const g = 4 + par(4, 4), up = (10 / (2 + par(6, g))) * par(6, g); return 4 * up / g; })(),
  '8.776': 1 / (1 / (18 / 0.90 - 12) - 1 / 20),
  '8.777': 12 * 12 / 18 - 12 * par(12, 12) / (6 + par(12, 12)),
  '8.778': (9 - 6) / (0.50 + 6 / 24),
  '8.780': (() => { // R₃ ur villkoret: 10·(Ib(R3+10)/30 + Ib) + Ib(R3+10) = 20 med Ib = 0,40 A
    const f = (r3) => 10 * (0.4 * (r3 + 10) / 30 + 0.4) + 0.4 * (r3 + 10) - 20;
    let lo = 0, hi = 100; for (let i = 0; i < 100; i++) { const m = (lo + hi) / 2; if (f(m) > 0) hi = m; else lo = m; } return (lo + hi) / 2; })(),
  '8.781': (() => { let n = 1; while (12 * par(...Array(n + 1).fill(24)) / (4 + par(...Array(n + 1).fill(24))) >= 9) n++; return n; })(),
};

test('42 nya uppgifter i området kopplingar med figur och båda delmomenten', () => {
  for (const id of IDS) {
    const u = q(id);
    assert.ok(u, id);
    assert.equal(u.omr, 'kopplingar', id);
    assert.match(u.t, /<svg[\s\S]*<\/svg>/, id);
    assert.ok(['Blandade kopplingar', 'Ström och spänning i blandade kopplingar'].includes(u.familj), id);
    assert.ok(u.ledtrad && u.ledtrad.length > 20, id);
    assert.match(u.s, /facit-steglista/, id);
    assert.match(u.s, /facit-svar/, id);
  }
  const fam = (f) => IDS.filter((id) => q(id).familj === f).length;
  assert.ok(fam('Ström och spänning i blandade kopplingar') >= 8);
});

test('nivåer: många på nivå 1–2, men också 3, 4 och 5', () => {
  const n = {};
  for (const id of IDS) n[q(id).traningsniva] = (n[q(id).traningsniva] || 0) + 1;
  assert.ok(n[1] >= 10 && n[2] >= 12 && n[3] >= 10 && n[4] >= 4 && n[5] >= 2, JSON.stringify(n));
});

test('svaren stämmer med oberoende beräkningar', () => {
  for (const [id, v] of Object.entries(VANTAT)) nara(q(id).rättSvar, v, id);
  assert.deepEqual(q('8.774').rättSvar.map((x) => +x.toFixed(6)), [6, +(1 / 3).toFixed(6)]);
});

test('flerval: rätt alternativ och kommentar till varje felaktigt', () => {
  const ratt = { '8.762': 'L₁', '8.763': 'L₁ lyser starkare', '8.769': 'I R₂', '8.779': 'L₁ svagare och L₂ starkare' };
  for (const [id, txt] of Object.entries(ratt)) {
    const a = q(id).alternativ;
    assert.equal(a.filter((x) => x.ratt).length, 1, id);
    assert.equal(a.find((x) => x.ratt).txt, txt, id);
    for (const x of a) assert.ok(x.kommentar && x.kommentar.length > 10, id);
  }
  // 8.769: effekten i varje resistor (R₂ vinner trots att R₁ har hela strömmen)
  const I = 10 / (1 + par(2, 6)), up = I * par(2, 6);
  assert.ok(up ** 2 / 2 > I ** 2 * 1 && I ** 2 * 1 > up ** 2 / 6);
});

test('uppgiftstexten har inga svarsinstruktioner och figurerna ryms i mobil', () => {
  for (const id of IDS) {
    const u = q(id);
    assert.doesNotMatch(u.t.replace(/<svg[\s\S]*?<\/svg>/g, ''), /Avrunda|Svara (?:med|exakt)|decimal/, id);
    const vb = u.t.match(/viewBox="0 0 ([\d.]+) ([\d.]+)"/);
    assert.ok(vb && +vb[1] <= 420, `${id}: bredd ${vb && vb[1]}`);
  }
});
