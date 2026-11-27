'use strict';
// Fy1 densitet: blandningsuppgifter på A-nivå (felrapport 2026-11-18 11:38, #2.51). Se agent/FY1_DENSITET_A_2026-11-18.md.
// Svaren räknas om oberoende av byggskriptet tools/bygg-fy1-densitet-a-2026-11-18.py.
const test = require('node:test');
const assert = require('node:assert/strict');
const fs = require('fs');
const vm = require('vm');
const path = require('path');

const c = { window: {} };
vm.runInNewContext(fs.readFileSync(path.join(__dirname, '..', 'uppgifter.js'), 'utf8'), c);
const bank = c.window.BANK;
const q = (id) => bank.find((t) => t.id === id);
const nara = (a, b, tol = 1e-6) => assert.ok(Math.abs(a - b) <= tol, `${a} ≠ ${b}`);
const vs = (x, n) => Number(x.toPrecision(n));
const NYA = ['2.365', '2.366', '2.367', '2.368', '2.369', '2.370'];

test('läraren: uppgifter där mängden av två ämnen bestäms ur blandningens densitet är A-uppgifter', () => {
  const vantat = { '2.51': ['(0/0/3)', 5], '2.90': ['(0/1/2)', 5], '2.146': ['(0/0/2)', 4], '2.200': ['(0/0/2)', 5], '2.202': ['(0/0/2)', 4] };
  for (const [id, [poang, tn]] of Object.entries(vantat)) {
    const t = q(id);
    assert.equal(t.omr, 'densitet', id); assert.equal(t.niva, 'A', id); assert.equal(t.poang, poang, id); assert.equal(t.traningsniva, tn, id);
  }
  // Facit och självrättning är oförändrade.
  assert.equal(q('2.146').rättSvar, 71.9); assert.equal(q('2.200').rättSvar, 36.1); /* 36,1 % med zinkens densitet 7,13 g/cm³ (formelsamlingen, användarbeslut 2026-11-25) */ assert.equal(q('2.202').rättSvar, 250);
  assert.match(q('2.51').s, /0\{,\}566/);
});

test('de nya uppgifterna: A-nivå, delmoment, figur och självrättning', () => {
  for (const id of NYA) {
    const t = q(id);
    assert.ok(t, id); assert.equal(t.omr, 'densitet'); assert.equal(t.kap, 2); assert.equal(t.niva, 'A', id);
    assert.equal(t.traningsniva, 5, id); assert.equal(t.spel, true); assert.equal(t.självrättning, true); assert.equal(t.miniräknare, true);
    assert.ok(['Sammansatta och ihåliga föremål', 'Densitet, flytförmåga och modeller'].includes(t.familj), id);
    assert.ok(t.familjNyckel && t.typ, id);
    assert.match(t.t, /<svg/, `${id}: figur`);
    assert.doesNotMatch(t.t, /\(Svara i|värdesiffror|Avrunda|Bestäm\./, id);
    for (const d of t.spelDelar || []) {
      assert.ok(d.t.startsWith(t.spelIntro), `${id}${d.etikett}: delkortet ska börja med samma inledning`);
      assert.match(d.t, /<svg/, `${id}${d.etikett}: figur på delkortet`);
    }
  }
  assert.equal(new Set(bank.map((t) => String(t.id))).size, bank.length);
});

test('facit följer mallen och svarsraden stämmer med rättSvar', () => {
  for (const id of NYA) {
    const t = q(id);
    const kort = t.spelDelar && t.spelDelar.length ? t.spelDelar.map((d, i) => [d.s, d.ledtrad, t.rättSvar[i], t.svarVardesiffror[i]])
      : [[t.s, t.ledtrad, t.rättSvar, t.svarVardesiffror]];
    for (const [s, led, ratt, n] of kort) {
      assert.match(s, /<p class="facit-rubrik">Givet och sökt<\/p>/, id); assert.match(s, /Sökt: /, id);
      assert.equal((s.match(/<li>/g) || []).length, (s.match(/class="facit-rubrik"/g) || []).length, id);
      assert.match(s, /<p class="facit-rubrik">[^<]*\\\(/, `${id}: rubrik med formel`);
      assert.doesNotMatch(s, /\bNone\b|\bnull\b|\bundefined\b|\bNaN\b|abc-formeln/, id);
      const svar = s.match(/<strong>Svar:<\/strong> ([^<]*)<\/p>/)[1];
      const tal = Number(svar.replace(/·10⁴/, 'e4').match(/[\d,]+(?:e4)?/)[0].replace(',', '.'));
      assert.equal(tal, vs(ratt, n), `${id}: svarsraden ${svar}`);
      assert.ok(String(led).replace(/<[^>]+>/g, '').length >= 30, `${id}: ledtråd`);
    }
  }
});

test('svaren räknas om oberoende', () => {
  const r = (id) => q(id).rättSvar;
  // 2.365: lödtenn. Andelen tenn w ska ge bitens volym 6,0 cm³.
  const w = r('2.365') / 100;
  nara(52 * w / 7.29 + 52 * (1 - w) / 11.34, 36.0 - 30.0, 1e-9);
  // 2.366: mjölk. Volymandelen ger densiteten 1,031; massandelen ur volymandelen.
  const [fv, fm] = r('2.366');
  nara(0.92 * fv / 100 + 1.035 * (1 - fv / 100), 1.031, 1e-9);
  nara(fm, 100 * 0.92 * (fv / 100) / 1.031, 1e-9);
  // 2.367: kylarvätska. Efter bytet ska densiteten vara den för 50 % glykol.
  const [gv, y] = r('2.367');
  nara(1.11 * gv / 100 + 1.00 * (1 - gv / 100), 1.04, 1e-9);
  nara((6.0 * 1.04 - 1.04 * y + 1.11 * y) / 6.0, (1.11 + 1.00) / 2, 1e-9);
  // 2.368: isbit med sten. Medeldensiteten ska vara vattnets.
  const ms = r('2.368');
  nara(120 / (ms / 2.60 + (120 - ms) / 0.917), 1.00, 1e-9);
  // 2.369: jordens kärna. Massan i modellen ska ge medeldensiteten.
  const [k, rk] = r('2.369');
  nara(k, 100 * (3480 / 6370) ** 3, 1e-9);
  nara((rk * k + 4500 * (100 - k)) / 100, 5510, 1e-6);
  // 2.370: flötet. Medeldensiteten ska vara 0,80 g/cm³ så att 80 % är under ytan.
  const mb = r('2.370');
  nara((mb + 0.16 * (12.0 - mb / 11.3)) / 12.0, 0.80, 1e-9);
});

test('delkort som behöver ett tidigare resultat får det i frågan, och avrundat värde ger samma svar', () => {
  assert.match(q('2.366').spelDelar[1].t, /3,48 % av mjölkens volym/);
  assert.match(q('2.367').spelDelar[1].t, /36,4 volymprocent glykol/);
  assert.match(q('2.369').spelDelar[1].t, /16,3 % av jordens volym/);
  // Huvudfrågan visar inte mellanresultaten.
  assert.doesNotMatch(q('2.366').t, /3,48/); assert.doesNotMatch(q('2.367').t, /36,4/); assert.doesNotMatch(q('2.369').t, /16,3/);
  assert.equal(vs(100 * 0.92 * 0.0348 / 1.031, 2), vs(q('2.366').rättSvar[1], 2));
  assert.equal(vs((0.50 - 0.364) * 6.0 / (1 - 0.364), 2), vs(q('2.367').rättSvar[1], 2));
  assert.equal(vs((5510 - 4500 * 0.837) / 0.163, 2), vs(q('2.369').rättSvar[1], 2));
});
