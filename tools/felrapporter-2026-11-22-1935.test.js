'use strict';
// Felrapporter 2026-11-22 19:35. Se agent/FELRAPPORTER_2026-11-22_1935.md.
const { test } = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const las = (f) => { const s = fs.readFileSync(path.join(__dirname, '..', f), 'utf8'); /* 2026-11-23: läs Kunskapsgymmets vy (tabellvärden och svarsinstruktioner i kgInstruktion) */ return require('./kg-vy.cjs')({ window: { B: JSON.parse(s.slice(s.indexOf('['), s.lastIndexOf(']') + 1)) } }).window.B; };
const fy1 = las('uppgifter.js'), ma2 = las('uppgifterma2.js'), mato1 = las('uppgiftermato1.js');
const q = (b, id) => b.find((x) => x.id === id);

test('Fy1: densiteterna hör till materialen', () => {
  for (const id of ['2.143', '2.275', '2.277']) {
    const x = q(fy1, id);
    for (const t of [x.t, x.spelIntro || '', ...(x.spelDelar || []).map((d) => d.t || '')]) assert.doesNotMatch(t, /Densiteterna är/, id);
    assert.match(x.t, /Aluminium har densiteten 2,70 g\/cm³/, id);
  }
  assert.match(q(fy1, '2.143').spelDelar[0].t, /[Pp]lasten (har densiteten )?1,20 g\/cm³/); // 2026-11-27: aluminiums tabellvärde står i kgInstruktion, plastens (uppgiftens egna data) i texten
});

test('Fy1: enheter på axlarna i a-t- och s-t-diagrammen', () => {
  for (const id of ['3.105', '3.355', '3.361', '3.603']) assert.match(q(fy1, id).t, />t \(s\)<\/text>/, id);
  for (const id of ['3.355', '3.361', '3.603']) assert.match(q(fy1, id).t, />a \(m\/s²\)<\/text>/, id);
  assert.match(q(fy1, '3.105').t, />s \(m\)<\/text>/);
});

test('Fy1 3.202: raketsläde med sammanhang, tre värdesiffror', () => {
  const x = q(fy1, '3.202');
  assert.match(x.t, /raketsläde/);
  for (const d of x.spelDelar) assert.match(d.t, /raketsläde/, d.etikett);
  assert.deepEqual(Array.from(x.svarVardesiffror), [3, 3, 3, 3]);
  assert.ok(Math.abs(x.rättSvar[1] + 282 / 1.4) < 1e-9);
  assert.ok(Math.abs(x.rättSvar[3] - 282 / 1.4 / 9.82) < 1e-9);
  assert.doesNotMatch(x.s, /201\{,\}43|20,51/);
});

test('Ma2 2.631: rättSvar utan LaTeX, format uttryck', () => {
  const x = q(ma2, '2.631');
  assert.equal(x.rättSvar, 'x^2-8x+7');
  assert.equal(x.svarFormat, 'uttryck');
});

test('Ma3c: x³ − 8 löses med ansats på nivå A, eller med tabell/räknare på E', () => {
  for (const id of ['3.799', '1.136']) {
    const x = q(mato1, id);
    assert.equal(x.niva, 'A', id); assert.equal(x.traningsniva, 5, id);
    assert.match(x.s, /x\^2\+ax\+b/, id); assert.doesNotMatch(x.s, /kubdifferens/i, id);
  }
  assert.match(q(mato1, '1.44').t, /<table/); assert.equal(q(mato1, '1.44').niva, 'E');
  assert.match(q(mato1, '1.506').t, /räknare/); assert.equal(q(mato1, '1.506').miniräknare, true);
  for (const id of ['1.44', '1.506', '1.136', '3.799']) assert.equal(q(mato1, id).rättSvar, 12, id);
  assert.notEqual(q(mato1, '1.136').t, q(mato1, '1.506').t);
});

test('Kunskapsgymmet: förenklat_polynom godtar utbruten faktor', { skip: !fs.existsSync(path.join(__dirname, '..', '..', 'kunskapsgymmet', 'index.html')) }, () => {
  const html = fs.readFileSync(path.join(__dirname, '..', '..', 'kunskapsgymmet', 'index.html'), 'utf8');
  assert.match(html, /Utbruten gemensam faktor godtas också/);
});
