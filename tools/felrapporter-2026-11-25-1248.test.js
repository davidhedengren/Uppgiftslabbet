'use strict';
// Felrapport 2026-11-25 12:48 (agent/FELRAPPORTER_2026-11-25_1248.md): momentet kvotregeln i Ma4 har bara kvoter.
const { test } = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const s = fs.readFileSync(path.join(__dirname, '..', 'uppgiftermato2.js'), 'utf8');
const bank = JSON.parse(s.slice(s.indexOf('['), s.lastIndexOf(']') + 1));
const q = (id) => bank.find((x) => x.id === id);

test('2.165, 2.163 och 2.108: varje del är en kvot och facit följer kvotregeln', () => {
  for (const id of ['2.165', '2.163', '2.108']) {
    const u = q(id);
    assert.equal(u.omr, 'kvotregeln', id);
    for (const d of u.spelDelar) assert.match(d.fraga, /\\d?frac/, `${id}${d.etikett}`);
    assert.match(u.s, /Kvotregeln: /, id);
    assert.doesNotMatch(u.ledtrad, /kedjeregeln och c\)|produkter/, id);
  }
  assert.deepEqual(q('2.165').rättSvar.slice(0, 2), ['(2cos(x)+1)/((2+cos(x))^2)', '(x^2+2x-3)/((x+1)^2)']);
});

test('2.117 ligger i produktregeln med sparat tidigare moment', () => {
  const u = q('2.117');
  assert.equal(u.omr, 'produktregeln');
  assert.equal(u.familj, 'Derivering med produktregeln');
  assert.ok(u.omrTidigare.includes('kvotregeln'));
  assert.deepEqual(u.rättSvar, [3, 2]);
});

test('numerisk kontroll av de nya derivatorna', () => {
  const fall = [
    [(x) => Math.sin(x) / (2 + Math.cos(x)), (x) => (2 * Math.cos(x) + 1) / (2 + Math.cos(x)) ** 2],
    [(x) => (x * x - 3 * x) / (x + 1), (x) => (x * x + 2 * x - 3) / (x + 1) ** 2],
    [(x) => Math.exp(2 * x) / (x + 1), (x) => Math.exp(2 * x) * (2 * x + 1) / (x + 1) ** 2],
    [(x) => x / Math.log(x), (x) => (Math.log(x) - 1) / Math.log(x) ** 2],
    [(x) => x * x / Math.exp(x), (x) => (2 * x - x * x) / Math.exp(x)],
    [(x) => x / Math.sin(x), (x) => (Math.sin(x) - x * Math.cos(x)) / Math.sin(x) ** 2],
  ];
  for (const [f, df] of fall) for (const x of [0.4, 1.7, 2.6]) {
    const h = 1e-6, num = (f(x + h) - f(x - h)) / (2 * h);
    assert.ok(Math.abs(num - df(x)) < 1e-5 * Math.max(1, Math.abs(num)));
  }
});
