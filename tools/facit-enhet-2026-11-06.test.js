'use strict';
// Enheten ska synas i facit (användarbeslut 2026-11-06). Se agent/FACIT_ENHET_2026-11-06.md.
const test = require('node:test');
const assert = require('node:assert/strict');
const fs = require('fs');
const vm = require('vm');
const path = require('path');

const las = (f) => { const c = { window: {} }; vm.runInNewContext(fs.readFileSync(path.join(__dirname, '..', f), 'utf8'), c); return Object.values(c.window).find(Array.isArray); };
const B = { fy1: las('uppgifter.js'), ma1: las('uppgifterma1.js'), ma2: las('uppgifterma2.js'), matf1: las('uppgiftermatf1.js') };
const q = (b, id) => B[b].find((t) => t.id === id);
const svar = (s) => [...String(s || '').matchAll(/<p class="facit-svar">([\s\S]*?)<\/p>/g)].map((m) => m[1]).join(' | ');

test('svarsraden visar enheten i de rättade uppgifterna', () => {
  const fall = {
    ma1: { '0.633': /16 s/, '0.757': /4,5 MW/, '3.543': /20 %/, '1.1320': /6 cm/, '1.1330': /6 cm/ },
    ma2: { '2.760': /6 cm/, '3.38': /längdenheter/, '3.64': /13\{,\}6\\\) längdenheter/, '3.264': /5 längdenheter/, '3.266': /10 längdenheter/,
      '3.296': /6 längdenheter/, '3.317': /7 längdenheter/, '3.326': /5\\\) längdenheter/, '3.346': /70\^\\circ/, '5.09': /Bas-abonnemang/,
      '5.25': /250 produkter/, '5.90': /64 W/, '5.103': /äldre personer/, '5.142': /12 Premium-abonnemang/, '5.157': /14 korta och 10 långa besök/,
      '5.169': /120 personer/, '1.697': /9 cm och bredden 6 cm/, '1.699': /30 kr och en bulle 15 kr/ },
    matf1: { '3.262': /cm\^2\/s/, '3.264': /cm\^3\/s/, '3.265': /cm\/s/, '3.266': /cm\^3\/s/ },
  };
  for (const [b, ids] of Object.entries(fall)) for (const [id, re] of Object.entries(ids)) assert.match(svar(q(b, id).s), re, `${b} ${id}`);
  assert.match(svar(q('ma2', '1.234').spelDelar[0].s), /105 kr/);
  assert.match(svar(q('ma2', '3.454').spelDelar[0].s), /5 cm/);
});

test('inga svarsrader med e-notation (2,2475e-05) i någon bank', () => {
  for (const f of ['uppgifter.js', 'uppgifter2.js', 'uppgifterma1.js', 'uppgifterma2.js', 'uppgiftermato1.js', 'uppgiftermato2.js', 'uppgiftermatf1.js']) {
    for (const t of las(f)) for (const s of [t.s, ...(t.spelDelar || []).map((d) => d.s)]) {
      assert.doesNotMatch(svar(s).replace(/\\[a-zA-Z]+/g, ' '), /\d[eE][-+]?\d/, `${f} ${t.id}`);
    }
  }
  assert.match(svar(q('fy1', '8.119').s), /2\{,\}25\\cdot10\^\{-5\}/);
  assert.ok(Math.abs(q('fy1', '8.119').rättSvar[1] - 2.25e-5) < 5e-8);
});

test('Ma2 5.01: varje del har rubriker, svarsrad med enhet och inget senare svar', () => {
  const t = q('ma2', '5.01');
  assert.equal(JSON.stringify(t.rättSvar), '[10,8,119000]');
  assert.ok(10 + 8 === 18 && 8000 * 10 + 12000 * 8 === 176000 && 176000 - (10 * 2500 + 8 * 4000) === t.rättSvar[2]);
  const [a, b, c] = t.spelDelar;
  for (const d of [t, a, b, c]) assert.equal((d.s.match(/<li>/g) || []).length, (d.s.match(/class="facit-rubrik"/g) || []).length);
  assert.match(svar(a.s), /10 Bas-paket/); assert.doesNotMatch(a.s, /y=8|y&=8/);
  assert.match(svar(b.s), /8 Plus-paket/); assert.doesNotMatch(b.s, /x=10|x&=10/);
  assert.match(c.fraga, /10 Bas-paket och 8 Plus-paket/); assert.match(svar(c.s), /119 000 kr/);
  assert.doesNotMatch(t.ledtrad, /vilken storhet som söks/);
});
