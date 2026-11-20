'use strict';
// Ma3c Funktioner: rutinuppgifter "förenkla f(x+h) − f(x)", 1.1129–1.1144 (2026-11-20).
const { test } = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const s = fs.readFileSync(path.join(__dirname, '..', 'uppgiftermato1.js'), 'utf8');
const bank = JSON.parse(s.slice(s.indexOf('['), s.lastIndexOf(']') + 1));
const IDS = Array.from({ length: 16 }, (_, i) => `1.${1129 + i}`);
const Q = IDS.map((id) => bank.find((q) => q.id === id));

// Oberoende kontroll: utvärdera svaret och f(X+h) − f(X) i några punkter.
const F = {
  '1.1129': [(x) => 4 * x + 1], '1.1130': [(t) => 7 - 2 * t], '1.1131': [(x) => x * x], '1.1132': [(x) => 3 * x * x],
  '1.1133': [(x) => 2 * x * x + 3 * x], '1.1134': [(x) => x * x - 5 * x], '1.1135': [(x) => x * x + 4 * x + 7],
  '1.1136': [(t) => 5 * t * t - t], '1.1137': [(x) => 6 - x * x], '1.1138': [(x) => -x * x + 6 * x],
  '1.1139': [(x) => -3 * x * x + 2 * x - 1], '1.1140': [(x) => 0.5 * x * x + 2 * x], '1.1141': [(x) => x * x + 3 * x, 2],
  '1.1142': [(x) => 2 * x * x - x + 4], '1.1143': [(x) => 4 * x * x - 3 * x, null, true], '1.1144': [(x) => x * x - 2 * x + 5],
};
const varde = (uttr, vars) => {
  let e = uttr.replace(/\^2/g, '**2');
  e = e.replace(/(\d)([a-z])/g, '$1*$2').replace(/([a-z])([a-z])/g, '$1*$2').replace(/([a-z])([a-z])/g, '$1*$2');
  return Function(...Object.keys(vars), `return ${e};`)(...Object.values(vars));
};

test('16 uppgifter i Funktionsvärden med rätt svar', () => {
  for (const q of Q) {
    assert.ok(q, 'saknas');
    assert.equal(q.omr, 'funktioner'); assert.equal(q.familj, 'Funktionsvärden');
    assert.equal(q.svarFormat, 'förenklat_polynom'); assert.equal(q.spel, true);
    const [f, punkt, kvot] = F[q.id];
    for (const [x, h] of [[1.3, 0.7], [-2, 0.25], [0.5, -1.5]]) {
      const X = punkt ?? x;
      let rätt = f(X + h) - f(X);
      if (kvot) rätt /= h;
      const v = varde(q.rättSvar, { x, t: x, a: x, h });
      assert.ok(Math.abs(v - rätt) < 1e-9, `${q.id}: ${q.rättSvar} ger ${v}, väntat ${rätt}`);
    }
  }
});

test('Nivåer och facit', () => {
  assert.deepEqual([...new Set(Q.map((q) => q.niva))].sort(), ['C', 'E']);
  // Felrapport 2026-11-20 11:04: flera termer och kvadreringsregeln ger träningsnivå 3 (lärarbeslut).
  assert.deepEqual(Q.filter((q) => q.traningsniva <= 2).map((q) => q.id), ['1.1129', '1.1130', '1.1131', '1.1132']);
  for (const q of Q) {
    assert.match(q.s, /facit-rubrik/);
    assert.match(q.s, /<strong>Svar:<\/strong>/);
    if (!['1.1129', '1.1130'].includes(q.id)) assert.match(q.s, /[Kk]vadreringsregeln/, q.id);
  }
  assert.equal(new Set(Q.map((q) => q.t)).size, 16);
});
