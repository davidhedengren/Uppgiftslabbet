'use strict';
// Felrapport 2026-11-23 16:46 (agent/FELRAPPORTER_2026-11-23_1646.md): Ma1 4.103 ska godta varje korrekt avrundat svar.
const { test } = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const s = fs.readFileSync(path.join(__dirname, '..', 'uppgifterma1.js'), 'utf8');
const bank = JSON.parse(s.slice(s.indexOf('['), s.lastIndexOf(']') + 1));

test('Ma1 4.103: exakt facit utan dold precision', () => {
  const u = bank.find((x) => x.id === '4.103');
  const k = Math.sqrt(84) - 4;
  assert.ok((4 + k) ** 2 + 16 - 100 < 1e-9 && 4 + k > 0);
  assert.equal(u.rättSvar, k);
  assert.ok(u.tolerans <= 1e-9);
  assert.doesNotMatch(String(u.t) + (u.kgInstruktion || ''), /avrund|decimal|exakt/i);
  assert.match(u.s, /\\sqrt\{84\}-4=2\\sqrt\{21\}-4\\approx5\{,\}17/);
});
