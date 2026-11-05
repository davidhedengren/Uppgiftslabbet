'use strict';
// Felrapporter 2026-11-05 21:56 (Ma2). Se agent/FELRAPPORTER_2026-11-05_2156.md.
const {test} = require('node:test'), assert = require('node:assert/strict'), fs = require('fs'), vm = require('vm');
const c = {window: {}}; vm.runInNewContext(fs.readFileSync('uppgifterma2.js', 'utf8'), c);
const q = (id) => c.window.BANKMA2.find((x) => x.id === id);
const arr = (x) => JSON.parse(JSON.stringify(x));

test('Lösningar anges i ett fält per lösning, inte som fritext med varierande skrivsätt', () => {
  const mangd = {'1.51': [[-3, 0, 3], 'x'], '1.143': [[-2, 0, 2], 'x'], '1.311': [[-3, 0, 3], 'x'], '2.160': [[-3, 0, 3], 'x'],
    '2.62': [[-13, -8, -7], 'k'], '2.451': [[7, 8, 13], 'k']};
  for (const [id, [v, e]] of Object.entries(mangd)) {
    const t = q(id);
    assert.equal(t.svarstyp, 'flera_delar', id); assert.equal(t.svarsstruktur, 'mängd', id);
    assert.deepEqual(arr(t.rättSvar), v, id); assert.deepEqual(arr(t.svarEtiketter), v.map(() => e), id);
    assert.match(t.s, /facit-svar/, id);
  }
  const ordnad = {'1.116': [[9, -6], ['a', 'b']], '1.218': [[2, 3], ['a', 'b']], '2.316': [[1, -6], ['a', 'b']], '1.172': [[3, 0.5], ['x', 'y']], '2.678': [[5, 4], ['a', 'b']]};
  for (const [id, [v, e]] of Object.entries(ordnad)) {
    const t = q(id);
    assert.equal(t.svarsstruktur, 'ordnad', id); assert.deepEqual(arr(t.rättSvar), v, id); assert.deepEqual(arr(t.svarEtiketter), e, id);
  }
  const t = q('1.115');
  assert.deepEqual(arr(t.rättSvar), [[0, -5], -5, 0]);
  assert.match(t.t, /utom två värden/);
  assert.doesNotMatch(t.ledtrad, /determinant/);
});

test('Svaren stämmer med en egen beräkning', () => {
  const rot = (f) => [-20, -13, -8, -7, -5, -3, -2, 0, 2, 3].filter((x) => Math.abs(f(x)) < 1e-9);
  assert.deepEqual(rot((x) => 3 * x ** 3 - 12 * x), [-2, 0, 2]);
  assert.deepEqual(rot((x) => 2 * x ** 3 - 18 * x), [-3, 0, 3]);
  assert.deepEqual(rot((a) => (a + 2) * (a + 3) - 6), [-5, 0]);
  const kPos = [[1, 12], [2, 6], [3, 4]].map(([r, s]) => r + s);
  assert.deepEqual(kPos.map((k) => -k).sort((a, b) => a - b), arr(q('2.62').rättSvar));
  assert.deepEqual(kPos.sort((a, b) => a - b), arr(q('2.451').rättSvar));
  const [a, b] = q('2.316').rättSvar; assert.equal(-b / (2 * a), 3); assert.equal(a * 9 + b * 3 + 10, 1);
});

test('Formuleringar och figurer efter elevrapporterna', () => {
  assert.ok(q('3.282').alternativ.some((x) => x.ratt && /Vinkel–vinkel/.test(x.txt)));
  assert.ok(q('3.282').alternativ.every((x) => (x.kommentar || '').length > 10));
  assert.match(q('4.2127').t, /densamma för alla normalfördelningar/);
  assert.match(q('3.2101').t, /parallellt med dörren/);
  assert.match(q('3.2140').t, /mittpunkterna/); assert.match(q('3.2140').t, />rand</);
  assert.match(q('3.523').t, /AB = 2·AC/); assert.match(q('3.523').t, />AC</);
  for (const id of ['3.520', '3.523']) {
    // Bisektrisens två halvor har en lucka mellan bågarna: ingen båge slutar där nästa börjar.
    const bagar = [...q(id).t.matchAll(/M ([\d.]+) ([\d.]+) A ([\d.]+) \3 0 0 0 ([\d.]+) ([\d.]+)/g)];
    for (let i = 1; i < bagar.length; i++) assert.ok(!(bagar[i - 1][4] === bagar[i][1] && bagar[i - 1][5] === bagar[i][2]), id);
  }
  const b = q('4.13').spelDelar.find((d) => d.etikett === 'b');
  assert.match(b.s, /InverseNormal\(0, 1, 0\.9\)/); assert.match(q('4.13').s, /InverseNormal/);
  assert.ok(Math.abs(8 / 1.2815515655446004 - 6.24) < 0.005);
});
