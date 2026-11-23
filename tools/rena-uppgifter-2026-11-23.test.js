'use strict';
/* Användarbeslut 2026-11-23: Uppgiftslabbets uppgiftstext är ”ren”. Svarsinstruktioner (avrundning, ”Svara exakt”,
   svarsform) och tabellvärden som eleven slår upp själv står i kgInstruktion, som bara Kunskapsgymmet visar.
   Se agent/FELMONSTER_OCH_BESLUT.md och agent/SPRAKOMSKRIVNING_INSTRUKTION.md. */
const { test } = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const las = (f) => { const s = fs.readFileSync(path.join(__dirname, '..', f), 'utf8'); return JSON.parse(s.slice(s.indexOf('['), s.lastIndexOf(']') + 1)); };
const fy1 = las('uppgifter.js'), fy2 = las('uppgifter2.js'), ma1 = las('uppgifterma1.js'), mato2 = las('uppgiftermato2.js');
const q = (b, id) => b.find((x) => x.id === id);
const synlig = (h) => String(h || '').replace(/<svg[\s\S]*?<\/svg>/g, ' ').replace(/<[^>]+>/g, ' ').replace(/\s+/g, ' ');

test('tabellvärden står i kgInstruktion, inte i Uppgiftslabbets text', () => {
  const fall = [
    [fy1, '7.169', /Aluminiumets specifika värmekapacitet är 900 J\/\(kg·K\)\. Vattnets specifika värmekapacitet är 4180/],
    [fy1, '8.413', /Kopparns resistivitet är 1,7·10⁻⁸ Ωm\./],
    [fy1, '7.105', /Isens smältvärme är 334 kJ\/kg\./],
    [fy2, '4.55', /Vattnets brytningsindex är 1,33\./],
    [fy2, '4.394', /Vattnets brytningsindex är 1,333\./],
  ];
  for (const [b, id, rx] of fall) {
    const u = q(b, id);
    assert.match(u.kgInstruktion, rx, id);
    assert.doesNotMatch(synlig(u.t), /värmekapacitet|smältvärme|resistivitet|brytningsindex/, id);
  }
  assert.doesNotMatch(q(fy2, '4.394').t, /\(1,333\)/);
});

test('blandade meningar: uppgiftens egna data står kvar', () => {
  const u = q(fy1, '6.101');
  assert.match(synlig(u.t), /Lufttrycket är 101,3 kPa\./);
  assert.doesNotMatch(synlig(u.t), /densitet/);
  assert.equal(u.kgInstruktion, 'Vattnets densitet är 998 kg/m³.');
});

test('värden som inte är tabellvärden och ämnen som annars inte framgår står kvar', () => {
  assert.match(q(fy2, '2.357').t, /Ljudets fart är 336 m\/s/);
  for (const id of ['2.6', '2.107', '2.108', '2.111', '2.113', '2.24', '2.40', '2.88', '2.92', '2.51', '2.277', '6.437', '6.490'])
    assert.match(synlig(q(fy1, id).t), /densitet/i, id);
});

test('svarsinstruktioner står i kgInstruktion', () => {
  const u = q(mato2, '2.409');
  assert.doesNotMatch(u.t, /Svara exakt/);
  assert.equal(u.kgInstruktion, 'Svara exakt.');
  assert.equal(ma1.filter((x) => x.kgInstruktion === 'Svara med en olikhet.').length, 47);
  assert.equal(ma1.filter((x) => /Skriv detta som en olikhet\./.test(x.t)).length, 7);
  assert.ok(!ma1.some((x) => /olikhetstecken\./.test(x.kgInstruktion || '')));
});
