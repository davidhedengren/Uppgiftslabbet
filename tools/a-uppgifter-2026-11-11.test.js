'use strict';
// A-uppgifter på nivå 4–5, omgång 2 (agent/A_UPPGIFTER_2026-11-11.md). Svaren räknas om oberoende av byggskripten.
const test = require('node:test');
const assert = require('node:assert/strict');
const fs = require('fs');
const vm = require('vm');
const path = require('path');

const las = (f) => { const c = { window: {} }; vm.runInNewContext(fs.readFileSync(path.join(__dirname, '..', f), 'utf8'), c); return Object.values(c.window).find(Array.isArray); };
const ma = las('uppgiftermato1.js'), fy = las('uppgifter.js');
const FY = ['4.912', '5.639', '5.640', '7.232', '3.747', '5.641'];
const MA = [];
const q = (b, id) => b.find((t) => t.id === id);
const nara = (a, b, tol = 1e-3) => assert.ok(Math.abs(a - b) <= tol, `${a} ≠ ${b}`);
const g = 9.82;
// Avrundning till n värdesiffror, som eleven gör.
const vs = (x, n) => Number(x.toPrecision(n));

test('uppgifterna är A-uppgifter med stigande svårighet och sista delen på nivå 5', () => {
  for (const [b, ids] of [[ma, MA], [fy, FY]]) for (const id of ids) {
    const t = q(b, id);
    assert.ok(t, id); assert.equal(t.niva, 'A', id); assert.equal(t.traningsniva, 5, id); assert.equal(t.spel, true); assert.equal(t.självrättning, true);
    const n = t.spelDelar.map((d) => d.traningsniva);
    assert.equal(JSON.stringify(n), JSON.stringify([...n].sort()), id);
    assert.ok(n.every((v) => v >= 3) && n[n.length - 1] === 5, id);
    assert.equal(t.spelDelar[t.spelDelar.length - 1].niva, 'A', id);
  }
  assert.equal(new Set(ma.map((t) => t.id)).size, ma.length); assert.equal(new Set(fy.map((t) => String(t.id))).size, fy.length);
});

test('facit följer mallen: rubrik i varje steg, formel i någon rubrik, svarsrad, figur och Givet och sökt i fysik', () => {
  for (const [b, ids, fysik] of [[ma, MA, false], [fy, FY, true]]) for (const id of ids) {
    const t = q(b, id);
    for (const d of t.spelDelar) {
      const s = d.s;
      assert.equal((s.match(/<li>/g) || []).length, (s.match(/class="facit-rubrik"/g) || []).length, id);
      assert.match(s, /<p class="facit-rubrik">[^<]*\\\(/, `${id}: ingen rubrik med formel`);
      assert.match(s, /<p class="facit-svar"><strong>Svar:<\/strong>/, id);
      assert.doesNotMatch(s, /abc-formeln|\bNone\b|\bnull\b|\bundefined\b|\bNaN\b/, id);
      if (fysik) { assert.match(s, /<p class="facit-rubrik">Givet och sökt<\/p>/, id); assert.match(s, /Sökt: /, id); }
      assert.ok(String(d.ledtrad).replace(/<[^>]+>/g, '').length >= 20, `${id}: ledtråd`);
    }
    assert.match(t.s, /facit-mark">a\)/, id);
    assert.match(t.t, /<svg/, `${id}: figur i frågan`);
  }
});

test('Fy1: svaren räknas om oberoende', () => {
  const r = (id) => q(fy, id).rättSvar;
  // 4.912: lådan på flaket. Kontroll i vägens system: lådan hinner 2,5 m längre än framstammen.
  const t = r('4.912')[2];
  nara(r('4.912')[0], 0.50 * g); nara(r('4.912')[1], 0.40 * g);
  nara((20 * t - 0.40 * g * t * t / 2) - (20 * t - 6.5 * t * t / 2), 2.5, 1e-9); assert.ok(t < 20 / 6.5);
  // 5.639: bromssträcka, avstånd och fart vid trädet (rörelseformler i stället för energi).
  const v50 = 50 / 3.6, v70 = 70 / 3.6, a = 11200 / 1500;
  nara(r('5.639')[0], v50 ** 2 / (2 * a)); nara(r('5.639')[1], v50 * 0.80 + v50 ** 2 / (2 * a));
  nara(r('5.639')[2], 3.6 * Math.sqrt(v70 ** 2 - 2 * a * (r('5.639')[1] - v70 * 0.80)));
  // 5.640: pumpen.
  const m = 998 * 6.0 * 4.0 * 0.25, Ep = m * g * 3.2, eta = (Ep + m * 49 / 2) / (750 * 720);
  nara(r('5.640')[0], Ep / 1000); nara(r('5.640')[1], 100 * eta); nara(r('5.640')[2], (Ep + m * 9 / 2) / eta / 750 / 60);
  // 7.232: te, mugg och mjölk. Energibalansen ska gå jämnt upp.
  const [T, mj] = r('7.232');
  nara(4.18 * 0.25 * (95 - T), 0.80 * 0.30 * (T - 20), 1e-9);
  nara((4.18 * 0.25 + 0.80 * 0.30) * (T - 60), 3.9 * (mj / 1000) * (60 - 6), 1e-9);
  // 3.747: helikoptern. Hastigheten över marken ska sakna östkomposant.
  const [th, t1, t2] = r('3.747'), rad = Math.PI / 180;
  nara(-60 * Math.sin(th * rad) + 15, 0, 1e-9); nara(t1, 90000 / (60 * Math.cos(th * rad)) / 60);
  const w = 15 * Math.SQRT1_2, th2 = Math.asin(w / 60);
  nara(t2, 90000 / (60 * Math.cos(th2) + w) / 60); assert.ok(t2 < 25 && t1 > 25);
  // 5.641: arean under kraft–tid-grafen med numerisk integration.
  const F = (u) => (u <= 2 ? 450 * u : u <= 6 ? 900 : 900 - 450 * (u - 6));
  let I = 0, I44 = 0; const N = 80000;
  for (let i = 0; i < N; i++) { const u = (i + 0.5) * 8 / N; I += F(u) * 8 / N / 1000; if (u < 4.4) I44 += F(u) * 8 / N / 1000; }
  nara(I, r('5.641')[0], 1e-6); nara(r('5.641')[1], -18 + I / 0.170); nara(I44, 0.170 * 18, 1e-3); assert.equal(r('5.641')[2], 4.4);
});

test('Fy1: avrundade mellanresultat ger samma slutsvar', () => {
  const r = (id) => q(fy, id).rättSvar;
  // En elev som räknar vidare med sitt avrundade delsvar ska få samma svar med två och tre värdesiffror.
  const lika = (exakt, alt, id) => { for (const n of [2, 3]) for (const v of alt) assert.equal(vs(v, n), vs(exakt, n), `${id}: ${v} mot ${exakt}`); };
  const v70 = 70 / 3.6, a = 11200 / 1500, fart = (d) => 3.6 * Math.sqrt(v70 ** 2 - 2 * a * (d - v70 * 0.80));
  lika(r('5.639')[2], [fart(24), fart(24.0)], '5.639c');
  const m = 998 * 6, E2 = m * g * 3.2 + m * 9 / 2, tid = (eta) => E2 / eta / 750 / 60;
  lika(r('5.640')[2], [tid(0.62), tid(0.620)], '5.640c');
  const mjolk = (T) => 1000 * (4.18 * 0.25 + 0.80 * 0.30) * (T - 60) / (3.9 * 54);
  lika(r('7.232')[1], [mjolk(81), mjolk(81.0)], '7.232b');
  const tid2 = (al) => Math.sqrt(2 * 2.5 / (6.5 - al));
  lika(r('4.912')[2], [tid2(3.9), tid2(3.93)], '4.912c');
});

test('delkorten är självbärande och läcker inte senare svar', () => {
  for (const id of FY) { const t = q(fy, id); for (const d of t.spelDelar) assert.ok(d.t.startsWith(t.spelIntro), id); }
  assert.match(q(fy, '4.912').spelDelar[2].fraga, /3,93 m\/s²/); assert.match(q(fy, '5.639').spelDelar[2].fraga, /24,0 m/);
  assert.match(q(fy, '5.640').spelDelar[2].fraga, /62,0 %/); assert.match(q(fy, '7.232').spelDelar[1].fraga, /81,0 °C/);
  assert.match(q(fy, '5.641').spelDelar[1].fraga, /5,4 Ns/);
  // Huvudfrågan innehåller inte mellanresultaten.
  assert.doesNotMatch(q(fy, '4.912').t, /3,93/); assert.doesNotMatch(q(fy, '5.639').t, /24,0 m/); assert.doesNotMatch(q(fy, '5.640').t, /62,0/);
  // Tidigare delfacit avslöjar inte senare svar.
  assert.doesNotMatch(q(fy, '4.912').spelDelar[0].s, /3,9|1,4 s/); assert.doesNotMatch(q(fy, '4.912').spelDelar[1].s, /1,4 s|1\{,\}39/);
  assert.doesNotMatch(q(fy, '5.639').spelDelar[0].s, /24|57/); assert.doesNotMatch(q(fy, '5.639').spelDelar[1].s, /57|15\{,\}6/);
  assert.doesNotMatch(q(fy, '5.640').spelDelar[0].s, /62|146/); assert.doesNotMatch(q(fy, '5.640').spelDelar[1].s, /7\{,\}7|463/);
  assert.doesNotMatch(q(fy, '7.232').spelDelar[0].s, /128|130 g/);
  assert.doesNotMatch(q(fy, '3.747').spelDelar[0].s, /26 min|58\{,\}1/); assert.doesNotMatch(q(fy, '3.747').spelDelar[1].s, /22 min|69\{,\}7/);
  assert.doesNotMatch(q(fy, '5.641').spelDelar[0].s, /13\{,\}8|4\{,\}4/); assert.doesNotMatch(q(fy, '5.641').spelDelar[1].s, /4\{,\}4|2\{,\}16/);
});

test('Fy1: enhet skrivs bara när den inte är underförstådd, och inga avrundningskrav skrivs ut', () => {
  for (const id of FY) { const t = q(fy, id); for (const d of t.spelDelar) assert.doesNotMatch(d.fraga, /decimal|värdesiffr|avrunda/i, id); }
  assert.match(q(fy, '5.639').spelDelar[2].fraga, /\(Svara i km\/h\.\)$/); assert.match(q(fy, '5.640').spelDelar[0].fraga, /\(Svara i kJ\.\)$/);
  assert.match(q(fy, '7.232').spelDelar[1].fraga, /\(Svara i gram\.\)$/); assert.match(q(fy, '5.641').spelDelar[2].fraga, /\(Svara i ms\.\)$/);
  assert.doesNotMatch(q(fy, '4.912').t, /Svara i/);
});
