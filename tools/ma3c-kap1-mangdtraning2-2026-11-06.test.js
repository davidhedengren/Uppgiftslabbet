'use strict';
// Ma3c kapitel 1, omgång 2 (agent/MA3C_KAP1_MANGDTRANING_2026-11-06.md): rationella uttryck,
// polynomfunktioner och sekant/tangent, 1.1046–1.1077.
const test = require('node:test');
const assert = require('node:assert/strict');
const fs = require('fs');
const vm = require('vm');
const path = require('path');

const c = { window: {} };
vm.runInNewContext(fs.readFileSync(path.join(__dirname, '../uppgiftermato1.js'), 'utf8'), c);
const bank = c.window.BANKMATO1;
const nya = Array.from({ length: 32 }, (_, i) => bank.find((q) => q.id === `1.${1046 + i}`));
const js = (t) => t.replace(/−/g, '-').replace(/\\dfrac\{([^{}]+)\}\{([^{}]+)\}/g, '(($1)/($2))')
  .replace(/\s+/g, '').replace(/\^/g, '**').replace(/(?<=[0-9xh)])(?=[xh(])/g, '*').replace(/(^|\()-/g, '$10-');
const fn = (t, v = 'x') => new Function(v, `return ${js(t)};`);
const delar = (q) => (q.spelDelar ? q.spelDelar.map((d, i) => ({ d, r: q.rättSvar[i] })) : [{ d: q, r: q.rättSvar }]);
const nara = (a, b) => Math.abs(a - b) < 1e-9;

test('32 uppgifter, 102 kort på nivå 2–3 med stigande svårighet', () => {
  assert.ok(nya.every(Boolean));
  assert.equal(new Set(bank.map((q) => q.id)).size, bank.length);
  const omr = {};
  let kort = 0;
  for (const q of nya) {
    omr[q.omr] = (omr[q.omr] || 0) + 1;
    const n = delar(q).map(({ d }) => d.traningsniva);
    kort += n.length;
    assert.ok(n.every((v) => v === 2 || v === 3), q.id);
    assert.equal(JSON.stringify(n), JSON.stringify([...n].sort()), q.id);
  }
  assert.deepEqual(omr, { rationella_uttryck: 10, polynomfunktioner: 14, tangent_sekant: 8 });
  assert.equal(kort, 102);
});

test('uteslutna x gör nämnaren noll, och nollställen gör bara täljaren noll', () => {
  for (const q of nya.filter((q) => q.omr === 'rationella_uttryck')) {
    for (const { d, r } of delar(q)) {
      const fraga = d.fraga || q.t;
      const [, T, N] = fraga.match(/\\dfrac\{([^{}]+)\}\{([^{}]+)\}/);
      const t = fn(T), n = fn(N), lista = [].concat(r);
      if (/lika med noll/.test(fraga)) {
        for (const v of lista) { assert.ok(nara(t(v), 0) && !nara(n(v), 0), q.id); }
      } else {
        for (const v of lista) assert.ok(nara(n(v), 0), `${q.id}: ${v}`);
        for (let v = -12; v <= 12; v++) if (nara(n(v), 0)) assert.ok(lista.includes(v), `${q.id} saknar ${v}`);
      }
    }
  }
});

test('nollställen, symmetrilinje och extremvärde stämmer med funktionen', () => {
  for (const q of nya.filter((q) => q.familj === 'Andragradsfunktioner och extremvärden')) {
    const f = fn(q.spelIntro.match(/f\(x\)=([^\\]+)\\\)/)[1]);
    const [z, sym, ext] = q.rättSvar;
    for (const v of z) assert.ok(nara(f(v), 0), q.id);
    assert.ok(nara(sym, (z[0] + z[1]) / 2), q.id);
    assert.ok(nara(ext, f(sym)), q.id);
    const a = f(sym + 1) - f(sym);
    assert.match(q.spelDelar[2].fraga, a > 0 ? /minsta/ : /största/, q.id);
  }
});

test('bestämda funktioner har rätt nollställen och uppfyller villkoret', () => {
  for (const q of nya.filter((q) => q.familj === 'Bestämma polynomfunktion från villkor')) {
    for (const { d, r } of delar(q)) {
      const f = fn(r);
      for (const m of d.fraga.matchAll(/x=(−?-?\d+)\\\)/g)) assert.ok(nara(f(+m[1].replace('−', '-')), 0), `${q.id}: ${r}`);
      const v = d.fraga.match(/f\((−?-?\d+)\)=(−?-?\d+)/);
      if (v) assert.ok(nara(f(+v[1].replace('−', '-')), +v[2].replace('−', '-')), `${q.id}: ${r}`);
    }
  }
});

test('sekant- och tangentlutningar räknas om från funktionen', () => {
  for (const q of nya.filter((q) => q.omr === 'tangent_sekant')) {
    const f = fn(q.spelIntro.match(/f\(x\)=([^\\]+)\\\)/)[1]);
    const [k12, k03, kvot, tang] = q.rättSvar;
    const [x1, x2] = [...q.spelDelar[0].fraga.matchAll(/x=(−?-?\d+)/g)].map((m) => +m[1].replace('−', '-'));
    assert.ok(nara(k12, (f(x2) - f(x1)) / (x2 - x1)), q.id);
    const x0 = +q.spelDelar[1].fraga.match(/x=(−?-?\d+)\\\)/)[1].replace('−', '-');
    assert.ok(Math.abs(k03 - (f(x0 + 0.1) - f(x0)) / 0.1) < 1e-9, q.id);
    const kv = fn(kvot, 'h');
    for (const hv of [0.5, 0.01, -0.2]) assert.ok(Math.abs(kv(hv) - (f(x0 + hv) - f(x0)) / hv) < 1e-9, q.id);
    assert.ok(nara(tang, kv(0)), q.id);
  }
});

test('facit: rubrik i varje steg, svarsrad och ingen senare dels svar i delfacit', () => {
  for (const q of nya) {
    for (const { d } of delar(q)) {
      assert.match(d.s, /<p class="facit-svar"><strong>Svar:<\/strong>/, q.id);
      assert.equal((d.s.match(/<li>/g) || []).length, (d.s.match(/class="facit-rubrik"/g) || []).length, q.id);
    }
    if (q.omr === 'polynomfunktioner' && q.spelIntro) {
      // Delkort a (nollställen) får inte visa extremvärdet från c.
      assert.ok(!q.spelDelar[0].s.includes(`f(${q.rättSvar[1]})`), q.id);
    }
  }
});
