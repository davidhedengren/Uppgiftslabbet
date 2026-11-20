'use strict';
// Felrapport 2026-11-20 11:04 (Ma3c 1.1103): insättning i en funktion med flera termer är träningsnivå 3, nivå E.
const { test } = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const s = fs.readFileSync(path.join(__dirname, '..', 'uppgiftermato1.js'), 'utf8');
const bank = JSON.parse(s.slice(s.indexOf('['), s.lastIndexOf(']') + 1));
const q = (id) => bank.find((x) => x.id === id);

test('Flera termer i parentesen: träningsnivå 3, fortfarande E (2/0/0)', () => {
  for (const id of ['1.235', '1.1102', '1.1103', '1.1117', '1.1133', '1.1134', '1.1135', '1.1136', '1.1137', '1.1141',
    '1.1142', '1.1144']) {
    assert.equal(q(id).traningsniva, 3, id);
    assert.equal(q(id).niva, 'E', id);
  }
  assert.equal(q('1.1103').poang, '2/0/0');
});

test('Enkla insättningar står kvar på nivå 1–2', () => {
  for (const [id, tn] of [['1.1101', 2], ['1.1129', 1], ['1.1130', 1], ['1.1131', 2], ['1.1132', 2], ['2.1126', 2]]) {
    assert.equal(q(id).traningsniva, tn, id);
  }
});
