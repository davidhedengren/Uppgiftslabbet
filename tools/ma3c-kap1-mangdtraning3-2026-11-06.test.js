'use strict';
// Ma3c kapitel 1, omgång 3 (agent/MA3C_KAP1_MANGDTRANING_2026-11-06.md): förkorta och räkna med
// rationella uttryck, 1.1078–1.1099. Svaren rättas med Kunskapsgymmets format "förkortat_uttryck".
const test = require('node:test');
const assert = require('node:assert/strict');
const fs = require('fs');
const vm = require('vm');
const path = require('path');

const c = { window: {} };
vm.runInNewContext(fs.readFileSync(path.join(__dirname, '../uppgiftermato1.js'), 'utf8'), c);
const bank = c.window.BANKMATO1;
const nya = Array.from({ length: 22 }, (_, i) => bank.find((q) => q.id === `1.${1078 + i}`));
// LaTeX- eller elevuttryck till JavaScript.
const js = (t) => t.replace(/−/g, '-').replace(/\\div/g, '/').replace(/\\cdot/g, '*')
  .replace(/\\dfrac\{((?:[^{}]|\{[^{}]*\})+)\}\{((?:[^{}]|\{[^{}]*\})+)\}/g, '(($1)/($2))')
  .replace(/[{}]/g, '').replace(/\s+/g, '').replace(/\^/g, '**')
  .replace(/(?<=[0-9x)])(?=[x(])/g, '*').replace(/(^|\()-/g, '$10-');
const fn = (t) => new Function('x', `return ${js(t)};`);
const XS = [-7.5, -2.25, 0.5, 1.75, 3.3, 6.6, 9.1];
const lika = (f, g) => XS.every((v) => Math.abs(f(v) - g(v)) < 1e-9 * Math.max(1, Math.abs(f(v))));

test('22 uppgifter, 66 delar på nivå 2–3 med stigande svårighet och förkortat format', () => {
  assert.ok(nya.every(Boolean));
  assert.equal(new Set(bank.map((q) => q.id)).size, bank.length);
  const omr = {};
  let delar = 0;
  for (const q of nya) {
    omr[q.omr] = (omr[q.omr] || 0) + 1;
    const n = q.spelDelar.map((d) => d.traningsniva);
    delar += n.length;
    assert.ok(n.every((v) => v === 2 || v === 3), q.id);
    assert.equal(JSON.stringify(n), JSON.stringify([...n].sort()), q.id);
    assert.equal(q.svarFormat[0], 'förkortat_uttryck', q.id);
  }
  assert.deepEqual(omr, { forkorta_rationella: 14, rakna_rationella: 8 });
  assert.equal(delar, 66);
});

test('varje uttryckssvar är lika med frågans uttryck', () => {
  for (const q of nya) {
    q.spelDelar.forEach((d, i) => {
      if (q.svarFormat[i] !== 'förkortat_uttryck') return;
      const tex = d.fraga.includes('\\(') ? d.fraga.match(/\\\((.+)\\\)/)[1] : q.spelIntro.match(/\\\((.+)\\\)/)[1];
      assert.ok(lika(fn(tex), fn(q.rättSvar[i])), `${q.id}${'abc'[i]}: ${tex} ≠ ${q.rättSvar[i]}`);
    });
  }
});

test('definitionsvillkor: uteslutna x gör nämnaren noll och ekvationens lösning stämmer', () => {
  for (const q of nya.filter((q) => q.familj === 'Förenkla och ange definitionsvillkor')) {
    const [, T, N] = q.spelIntro.match(/\\dfrac\{([^{}]+)\}\{([^{}]+)\}/);
    const t = fn(T), n = fn(N);
    const [, uteslut, losning] = q.rättSvar;
    for (const v of uteslut) assert.equal(n(v), 0, q.id);
    for (let v = -12; v <= 12; v++) if (n(v) === 0) assert.ok(uteslut.includes(v), `${q.id} saknar ${v}`);
    const hl = +q.spelDelar[2].fraga.match(/=(−?-?\d+)\\\)/)[1].replace('−', '-');
    assert.ok(n(losning) !== 0 && Math.abs(t(losning) / n(losning) - hl) < 1e-12, q.id);
  }
});

test('facit: rubrik i varje steg, svarsrad och ingen senare dels svar i delfacit', () => {
  for (const q of nya) {
    for (const d of q.spelDelar) {
      assert.match(d.s, /<p class="facit-svar"><strong>Svar:<\/strong>/, q.id);
      assert.equal((d.s.match(/<li>/g) || []).length, (d.s.match(/class="facit-rubrik"/g) || []).length, q.id);
      assert.doesNotMatch(d.s, /[^0-9.]1\(x/, q.id);
    }
    if (q.familj === 'Förenkla och ange definitionsvillkor') {
      const x = q.rättSvar[2];
      for (const d of q.spelDelar.slice(0, 2)) assert.ok(!d.s.includes(`x=${x}\\)`), q.id);
    }
  }
});
