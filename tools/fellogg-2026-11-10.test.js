'use strict';
// Fellogg 2026-11-10 08:28 (agent/FELRAPPORTER_2026-11-10_0828.md): Ma3c 1.41 och Ma1 1.982.
const test = require('node:test');
const assert = require('node:assert/strict');
const fs = require('fs');
const vm = require('vm');
const path = require('path');

const las = (f) => { const c = { window: {} }; vm.runInNewContext(fs.readFileSync(path.join(__dirname, '..', f), 'utf8'), c); return Object.values(c.window).find(Array.isArray); };
const mato1 = las('uppgiftermato1.js'), ma1 = las('uppgifterma1.js');
const steg = (s) => [(s.match(/<li>/g) || []).length, (s.match(/class="facit-rubrik"/g) || []).length];

test('Ma3c 1.41: varje del har en tydlig metod, egen ledtråd och oförändrade svar', () => {
  const q = mato1.find((t) => t.id === '1.41');
  assert.equal(JSON.stringify(q.rättSvar), JSON.stringify(['3x^2+4x-4', '(x-5)(x+2)', '(x+2)(3x-2)']));
  assert.equal(q.svarFormat[0], 'förenklat_polynom');
  assert.match(q.t, /a\) Multiplicera ut och förenkla/); assert.match(q.spelDelar[0].t, /Multiplicera ut och förenkla/);
  const f = (v) => 3 * v * v + 4 * v - 4;
  assert.ok(Math.abs(f(-2)) < 1e-12 && Math.abs(f(2 / 3)) < 1e-12);
  for (const x of [-3, 0.5, 4]) assert.ok(Math.abs((x + 2) * (3 * x - 2) - f(x)) < 1e-12);
  const c = q.spelDelar[2];
  assert.match(c.s, /pq-formeln/); assert.match(c.s, /Faktorsatsen/); assert.match(c.s, /<svg/); assert.match(c.s, />2\/3</);
  assert.doesNotMatch(c.s, /abc-formeln|0,666667/);
  for (const d of [q, ...q.spelDelar]) { const [a, b] = steg(d.s); assert.equal(a, b, 'rubrik i varje steg'); assert.match(d.s, /facit-svar/); }
  for (const d of q.spelDelar) assert.doesNotMatch(d.ledtrad, /exponenter|funktionsvärde/);
  assert.doesNotMatch(q.ledtrad, /exponenter|funktionsvärde/);
});

test('Ma1 1.982: talen skrivs som 2n så att de säkert är jämna, och svaret är oförändrat', () => {
  const q = ma1.find((t) => t.id === '1.982');
  assert.equal(q.rättSvar, 44);
  const n = (126 - 6) / 6;
  assert.ok(Number.isInteger(n) && 2 * n + 4 === 44 && 2 * n % 2 === 0);
  assert.match(q.s, /2n\+2/); assert.match(q.s, /är ett heltal/); assert.match(q.ledtrad, /2n/);
  const [a, b] = steg(q.s); assert.equal(a, b);
});
