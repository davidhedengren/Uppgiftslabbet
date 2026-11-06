'use strict';
// Ma3c kapitel 1, mängdträning på nivå 2–3 (agent/MA3C_KAP1_MANGDTRANING_2026-11-06.md).
const test = require('node:test');
const assert = require('node:assert/strict');
const fs = require('fs');
const vm = require('vm');
const path = require('path');

const c = { window: {} };
vm.runInNewContext(fs.readFileSync(path.join(__dirname, '../uppgiftermato1.js'), 'utf8'), c);
const bank = c.window.BANKMATO1;
const ids = Array.from({ length: 42 }, (_, i) => `1.${1004 + i}`);
const nya = ids.map((id) => bank.find((q) => q.id === id));

// Liten tolk för elevtext som 3x^2(2x-3) eller (x+2)^3-(x-1)(x+1).
const js = (t) => t.replace(/−/g, '-').replace(/\s+/g, '').replace(/\^/g, '**')
  .replace(/(?<=[0-9x)])(?=[x(])/g, '*')
  // Unärt minus före en potens är inte tillåtet i JavaScript: skriv -x**3 som 0-x**3.
  .replace(/(^|\()-/g, '$10-');
const f = (t) => new Function('x', `return ${js(t)};`);
const uttryck = (fraga) => fraga.split('\\(')[1].split('\\)')[0].replace(/=0$/, '');
const delar = (q) => (q.spelDelar ? q.spelDelar.map((d, i) => ({ d, r: q.rättSvar[i], fmt: q.svarFormat[i] }))
  : [{ d: q, r: q.rättSvar, fmt: q.svarFormat }]);

test('42 nya uppgifter i fyra moment på träningsnivå 2–3', () => {
  assert.ok(nya.every(Boolean));
  assert.equal(new Set(bank.map((q) => q.id)).size, bank.length);
  const omr = {};
  for (const q of nya) {
    omr[q.omr] = (omr[q.omr] || 0) + 1;
    assert.equal(q.kap, 1);
    assert.deepEqual([...q.kurs], ['1b', '1c']);
    assert.equal(q.spel, true);
    assert.equal(q.självrättning, true);
    for (const { d } of delar(q)) assert.ok([2, 3].includes(d.traningsniva), q.id);
  }
  assert.deepEqual(omr, { algebra_polynom: 14, polynom: 12, faktorisera_polynom: 8, polynomekvationer: 8 });
  const kort = nya.reduce((s, q) => s + (q.spelDelar ? q.spelDelar.length : 1), 0);
  assert.equal(kort, 123);
});

test('a) är enklast: delarna har stigande eller lika träningsnivå', () => {
  for (const q of nya.filter((q) => q.spelDelar)) {
    const n = Array.from(q.spelDelar, (d) => d.traningsniva);
    assert.equal(JSON.stringify(n), JSON.stringify([...n].sort()), q.id);
    assert.equal(q.traningsniva, Math.max(...n), q.id);
  }
});

test('utvecklingar och faktoriseringar stämmer i flera x-värden', () => {
  let n = 0;
  for (const q of nya) {
    for (const { d, r, fmt } of delar(q)) {
      if (!['förenklat_polynom', 'faktoriserat'].includes(fmt)) continue;
      const a = f(uttryck(d.fraga || q.t)), b = f(r);
      for (const v of [-3, -1.5, 0, 0.5, 2, 4]) assert.ok(Math.abs(a(v) - b(v)) < 1e-9, `${q.id}: ${r}`);
      if (fmt === 'faktoriserat') assert.match(r, /\)\(|\)$|x\(/, `${q.id}: faktorform ${r}`);
      if (fmt === 'förenklat_polynom') assert.doesNotMatch(r, /\(/, `${q.id}: utan parenteser`);
      n++;
    }
  }
  assert.equal(n, 58);
});

test('alla rötter löser ekvationen och inga saknas', () => {
  for (const q of nya.filter((q) => q.omr === 'polynomekvationer')) {
    for (const { d, r } of delar(q)) {
      const p = f(uttryck(d.fraga));
      for (const x of r) assert.ok(Math.abs(p(x)) < 1e-9, `${q.id}: x=${x}`);
      // Polynomets grad ger högsta antalet rötter; varje del har så många olika rötter som graden.
      const grad = Math.max(...[...uttryck(d.fraga).matchAll(/x\^(\d)/g)].map((m) => +m[1]), 1);
      const produkt = (uttryck(d.fraga).match(/\(/g) || []).length;
      assert.equal(new Set(r).size, r.length, q.id);
      assert.ok(r.length === grad || produkt, `${q.id}: ${r.length} rötter, grad ${grad}`);
    }
  }
});

test('funktionsvärden och koefficienter räknas om från polynomet', () => {
  for (const q of nya.filter((q) => q.omr === 'polynom')) {
    const P = q.spelIntro.match(/p\(x\)=([^\\]+)\\\)/)[1];
    const p = f(P);
    for (const { d, r } of delar(q)) {
      const m1 = d.fraga.match(/^Beräkna \\\(p\((−?[-\d]+)\)\\\)\.$/);
      const m2 = d.fraga.match(/p\((−?[-\d]+)\)-2p\((−?[-\d]+)\)/);
      if (m1) assert.equal(r, p(+m1[1].replace('−', '-')), q.id);
      if (m2) assert.equal(r, p(+m2[1].replace('−', '-')) - 2 * p(+m2[2].replace('−', '-')), q.id);
      if (/konstanttermen/.test(d.fraga)) assert.equal(r, p(0), q.id);
    }
  }
});

test('facit följer facitmallen: rubrik i varje steg, svarsrad och inga senare svar i delfacit', () => {
  for (const q of nya) {
    for (const { d, r } of delar(q)) {
      const s = d.s;
      assert.match(s, /<p class="facit-svar"><strong>Svar:<\/strong>/, q.id);
      assert.equal((s.match(/<li>/g) || []).length, (s.match(/class="facit-rubrik"/g) || []).length, q.id);
      assert.ok(d.ledtrad && d.ledtrad.length > 30, q.id);
    }
    if (q.spelDelar) {
      for (const [i, d] of q.spelDelar.entries()) {
        for (const senare of q.rättSvar.slice(i + 1)) {
          if (typeof senare === 'string' && senare.length > 5) assert.ok(!d.s.includes(senare), `${q.id}${d.etikett} visar ${senare}`);
        }
      }
    }
  }
});
