'use strict';
// Ma3c Funktioner 2026-11-20: 1.545, 1.546, 1.551 och 1.552 varierade, och begreppet ”diskret funktion” borttaget.
const { test } = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const las = (f) => { const s = fs.readFileSync(path.join(__dirname, '..', f), 'utf8'); return JSON.parse(s.slice(s.indexOf('['), s.lastIndexOf(']') + 1)); };
const mato1 = las('uppgiftermato1.js'), ma1 = las('uppgifterma1.js');
const q = (b, id) => b.find((x) => x.id === id);
const text = (h) => String(h || '').replace(/<svg[\s\S]*?<\/svg>/g, ' ').replace(/<[^>]+>/g, ' ');

test('Ingen elevtext i Ma3c eller Ma1 använder ordet diskret', () => {
  for (const b of [mato1, ma1]) for (const x of b) {
    for (const k of ['t', 's', 'ledtrad', 'spelIntro']) assert.doesNotMatch(String(x[k] || ''), /diskret/i, x.id + k);
    for (const d of x.spelDelar || []) for (const k of ['t', 's', 'ledtrad', 'fraga']) assert.doesNotMatch(String(d[k] || ''), /diskret/i, x.id + k);
    for (const a of x.alternativ || []) assert.doesNotMatch(JSON.stringify(a), /diskret/i, x.id);
  }
});

test('De fyra uppgifterna har olika sammanhang, frågor och svar', () => {
  const fyra = ['1.545', '1.546', '1.551', '1.552'].map((id) => q(mato1, id));
  assert.equal(new Set(fyra.map((x) => text(x.t))).size, 4);
  assert.deepEqual(fyra.map((x) => x.rättSvar), [14 + 9 + 22, 35 - 10, 3, 70 * 4 - (60 + 45 * 4)]);
  assert.match(text(fyra[0].t), /lotter/); assert.match(fyra[0].t, /<table/);
  assert.match(text(fyra[1].t), /solros/); assert.match(fyra[1].t, /<svg/);
  assert.match(text(fyra[2].t), /zoner/); assert.match(fyra[2].t, /<td>48<\/td>/);
  assert.match(text(fyra[3].t), /bowlinghallar/);
  for (const x of fyra) {
    assert.equal(x.niva, 'E', x.id);
    assert.doesNotMatch(text(x.t), /f\(1\)\+f\(2\)\+f\(3\)/, x.id);
    assert.match(x.s, /facit-rubrik/, x.id);
    assert.match(x.s, /<strong>Svar:<\/strong>/, x.id);
  }
});

test('1.453 (NP) frågar efter heltalsvärden och har samma rätta alternativ', () => {
  const x = q(mato1, '1.453');
  assert.match(text(x.t), /bara anta heltalsvärden/);
  assert.match(x.alternativ.find((a) => a.ratt).txt, /stolar/);
});
