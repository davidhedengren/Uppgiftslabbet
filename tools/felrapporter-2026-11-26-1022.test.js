'use strict';
// Felrapport 2026-11-26 10:22 (agent/FELRAPPORTER_2026-11-26_1022.md): Fy1 2.370, blyvikten är ingjuten i flötet.
const { test } = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const s = fs.readFileSync(path.join(__dirname, '..', 'uppgifter.js'), 'utf8');
const q = JSON.parse(s.slice(s.indexOf('['), s.lastIndexOf(']') + 1)).find((x) => x.id === '2.370');

test('Fy1 2.370: texten säger att blyet sitter inuti flötet och ingår i volymen', () => {
  const text = q.t.replace(/<svg[\s\S]*?<\/svg>/g, '');
  assert.match(text, /ingjuten i den nedre änden/);
  assert.match(text, /trä och bly tillsammans, har volymen 12,0 cm³/);
  assert.doesNotMatch(text, /längst ner/);
});

test('Fy1 2.370: figuren ritar blyet inuti träkroppen', () => {
  const kropp = q.t.match(/<rect x="196" y="([\d.]+)" width="28" height="([\d.]+)"/);
  const bly = q.t.match(/<rect x="202" y="([\d.]+)" width="16" height="([\d.]+)"/);
  assert.ok(kropp && bly);
  const kroppSlut = Number(kropp[1]) + Number(kropp[2]);
  assert.ok(Number(bly[1]) > Number(kropp[1]));
  assert.ok(Number(bly[1]) + Number(bly[2]) < kroppSlut, 'blyet ska sluta ovanför träkroppens nedre kant');
});

test('Fy1 2.370: tabellvärden i kgInstruktion, facit förklarar volymen, svaret oförändrat', () => {
  assert.doesNotMatch(q.t, /11,3|vatten 1,00/);
  assert.match(q.kgInstruktion, /11,3 g\/cm³/);
  assert.match(q.kgInstruktion, /1,00 g\/cm³/);
  assert.match(q.s, /Blyvikten är ingjuten i flötet, så trä och bly fyller tillsammans flötets 12,0 cm³/);
  const m = q.rättSvar;
  assert.ok(Math.abs(m - 7.79) < 0.01);
  assert.ok(Math.abs((m + 0.16 * (12.0 - m / 11.3)) / 12.0 - 0.8) < 1e-9);
});
