'use strict';
// Felrapport 2026-11-25 10:47 (agent/FELRAPPORTER_2026-11-25_1047.md): Fy1 2.258 utan modellspråk och svarsinstruktion.
const { test } = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const s = fs.readFileSync(path.join(__dirname, '..', 'uppgifter.js'), 'utf8');
const q = JSON.parse(s.slice(s.indexOf('['), s.lastIndexOf(']') + 1)).find((x) => x.id === '2.258');

test('Fy1 2.258: enkel text, figur före frågan, oförändrat svar', () => {
  const text = q.t.replace(/<svg[\s\S]*?<\/svg>/g, '');
  assert.doesNotMatch(text, /linjärt|kalibrering|sensorns|Antag att|Ange svaret|decimal/);
  assert.match(text, /99,8 grader/);
  assert.ok(q.t.indexOf('<svg') < q.t.indexOf('Vilken är den verkliga temperaturen'));
  assert.equal(q.rättSvar, 50);
  assert.ok(Math.abs((50.7 - 0.8) / (100.6 - 0.8) * 100 - 50) < 1e-9);
  assert.match(q.s, /Givet och sökt/);
  assert.doesNotMatch(q.ledtrad, /kalibrering/);
});
