'use strict';
// A-uppgifter på nivå 4–5 i Ma3c och Fy1 (agent/A_UPPGIFTER_2026-11-10.md). Svaren räknas om oberoende av byggskripten.
const test = require('node:test');
const assert = require('node:assert/strict');
const fs = require('fs');
const vm = require('vm');
const path = require('path');

const las = (f) => { const c = { window: {} }; vm.runInNewContext(fs.readFileSync(path.join(__dirname, '..', f), 'utf8'), c); return Object.values(c.window).find(Array.isArray); };
const ma = las('uppgiftermato1.js'), fy = las('uppgifter.js');
const MA = ['2.1285', '3.1271', '3.1272', '4.609', '1.1100', '3.1273', '4.610'];
const FY = ['3.746', '4.910', '4.911', '5.637', '5.638', '6.565', '7.231', '8.739'];
const q = (b, id) => b.find((t) => t.id === id);
const nara = (a, b, tol = 1e-3) => assert.ok(Math.abs(a - b) <= tol, `${a} ≠ ${b}`);
const g = 9.82;

test('15 A-uppgifter med 38 kort, högsta delen på nivå 5 och stigande svårighet', () => {
  let kort = 0;
  for (const [b, ids] of [[ma, MA], [fy, FY]]) for (const id of ids) {
    const t = q(b, id);
    assert.ok(t, id); assert.equal(t.niva, 'A', id); assert.equal(t.traningsniva, 5, id); assert.equal(t.spel, true); assert.equal(t.självrättning, true);
    const n = t.spelDelar ? t.spelDelar.map((d) => d.traningsniva) : [t.traningsniva];
    kort += n.length;
    assert.equal(JSON.stringify(n), JSON.stringify([...n].sort()), id);
    assert.ok(n.every((v) => v >= 3) && n[n.length - 1] === 5, id);
    if (t.spelDelar) assert.equal(t.spelDelar[t.spelDelar.length - 1].niva, 'A', id);
  }
  assert.equal(kort, 38);
  assert.equal(new Set(ma.map((t) => t.id)).size, ma.length); assert.equal(new Set(fy.map((t) => String(t.id))).size, fy.length);
});

test('facit följer mallen: rubrik i varje steg, formel i någon rubrik, svarsrad och Givet och sökt i fysik', () => {
  for (const [b, ids, fysik] of [[ma, MA, false], [fy, FY, true]]) for (const id of ids) {
    const t = q(b, id);
    const facit = t.spelDelar ? t.spelDelar.map((d) => d.s) : [t.s];
    for (const s of facit) {
      assert.equal((s.match(/<li>/g) || []).length, (s.match(/class="facit-rubrik"/g) || []).length, id);
      assert.match(s, /<p class="facit-rubrik">[^<]*\\\(/, `${id}: ingen rubrik med formel`);
      assert.match(s, /<p class="facit-svar"><strong>Svar:<\/strong>/, id);
      assert.doesNotMatch(s, /abc-formeln|None|null|undefined/, id);
    }
    if (fysik) for (const d of t.spelDelar) if (/Givet och sökt/.test(d.s)) assert.match(d.s, /Sökt: /, id);
    if (t.spelDelar) {
      assert.match(t.s, /facit-mark">a\)/, id);
      for (const d of t.spelDelar) assert.ok(String(d.ledtrad).replace(/<[^>]+>/g, '').length >= 20, `${id}: ledtråd`);
    }
    assert.match(t.t + t.s, /<svg/, `${id}: figur`);
  }
});

test('Ma3c: svaren räknas om oberoende', () => {
  // 2.1285: y = 4x − 4 tangerar båda parablerna (dubbelrot i skärningsekvationen).
  assert.equal(q(ma, '2.1285').rättSvar, 'y=4x-4');
  assert.equal((-4) ** 2 - 4 * 1 * 4, 0);           // x² − 4x + 4 = 0
  assert.equal(0 ** 2 - 4 * (-1) * 0, 0);           // −x² + 4x − 4 − (4x − 4) = −x² = 0
  // 3.1271: tangent, andra skärningen och arean (numerisk integration).
  const a = q(ma, '3.1271').rättSvar;
  assert.equal(a[0], 'y=3x-2'); assert.equal(a[1], -2); nara((-2) ** 3, 3 * -2 - 2);
  let area = 0; const N = 30000;
  for (let i = 0; i < N; i++) { const x = -2 + 3 * (i + 0.5) / N; area += (x ** 3 - 3 * x + 2) * 3 / N; }
  nara(area, a[2], 1e-6); assert.equal(a[2], 6.75);
  // 3.1272: a, minimivärdet och antalet heltal k med tre lösningar.
  const f = (x) => x ** 3 - 3 * x * x - 9 * x, b = q(ma, '3.1272').rättSvar;
  assert.equal(b[0], -3); assert.equal(3 * 1 + 2 * b[0] * -1 - 9, 0); assert.equal(f(3), b[1]); assert.equal(f(-1), 5);
  // Tre olika lösningar precis när k ligger mellan extremvärdena: f(3) < k < f(−1).
  let antal = 0;
  for (let k = -40; k <= 20; k++) if (f(3) < k && k < f(-1)) antal++;
  assert.equal(antal, b[2]);
  const byten = (k) => { let n = 0; for (let i = 0; i < 14000; i++) { const x = -6.00037 + i * 0.001; if ((f(x) - k) * (f(x + 0.001) - k) < 0) n++; } return n; };
  assert.equal(byten(-26), 3); assert.equal(byten(4), 3); assert.equal(byten(-28), 1); assert.equal(byten(6), 1);
  // 4.609: två trianglar med arean 14.
  const [v, bc] = q(ma, '4.609').rättSvar;
  for (let i = 0; i < 2; i++) { nara(0.5 * 7 * 5 * Math.sin(v[i] * Math.PI / 180), 14); nara(bc[i] ** 2, 49 + 25 - 70 * Math.cos(v[i] * Math.PI / 180), 1e-2); }
  nara(v[0] + v[1], 180);
  // 1.1100: a, övriga nollställen och c.
  const p = (x) => x ** 3 + 3 * x * x - 4 * x - 12, c = q(ma, '1.1100').rättSvar;
  assert.equal(c[0], 3); assert.equal(p(2), 0); for (const r of c[1]) assert.equal(p(r), 0);
  nara(p(-2.5), c[2] * (-2.5 - 2), 1e-9); nara(3 * 2.5 ** 2 + 6 * -2.5 - 4, c[2], 1e-9); // lika värde och lika lutning: dubbelrot i x = −2,5
  // 3.1273: största vinst och bästa skatt (sökning).
  const V = (x, t = 0) => x * (130 - 0.5 * x) - (400 + 10 * x + 0.1 * x * x) - t * x, d = q(ma, '3.1273').rättSvar;
  let bastV = -1e9; for (let x = 0; x <= 200; x += 0.01) bastV = Math.max(bastV, V(x));
  nara(bastV, d[0], 1e-3);
  let bastS = -1, bastT = 0;
  for (let t = 0; t <= 120; t += 0.5) {
    const bx = (120 - t) / 1.2;                        // V_t'(x) = −1,2x + 120 − t = 0
    assert.ok(V(bx, t) >= V(bx + 1, t) && V(bx, t) >= V(bx - 1, t));
    if (t * bx > bastS) { bastS = t * bx; bastT = t; }
  }
  assert.equal(bastT, d[1]); nara(bastS, 3000, 1e-9);
  // 4.610: vinkel, diagonal och konstanten k.
  const e = q(ma, '4.610').rättSvar;
  nara(Math.cos(e[0] * Math.PI / 180), (64 + 25 - 121) / 80, 1e-5); nara(e[1] ** 2, 57, 1e-3); assert.equal(121 + 57, e[2] * (64 + 25));
});

test('Fy1: svaren räknas om oberoende', () => {
  const r = (id) => q(fy, id).rättSvar;
  // 3.746: avstånd efter reaktionstiden och minsta retardation (relativ rörelse).
  assert.equal(r('3.746')[0], 600 - (30 - 10) * 1.0); nara(r('3.746')[1], 20 ** 2 / (2 * 580), 1e-5);
  // 4.910: hissen.
  const a1 = 12 * g / 70, v = a1 * 2.5, a3 = 9 * g / 70;
  nara(r('4.910')[0], a1); nara(r('4.910')[1], v); nara(r('4.910')[2], a1 * 2.5 ** 2 / 2 + v * 6 + v * v / (2 * a3));
  // 4.911: upp och ned för planet, kontroll med energi.
  const al = 25 * Math.PI / 180, s = 36 / (2 * g * (Math.sin(al) + 0.3 * Math.cos(al)));
  nara(r('4.911')[0], s); nara(r('4.911')[1] ** 2, 36 - 4 * 0.3 * g * Math.cos(al) * s);
  // 5.637: energi genom fjäder, sträv yta och ramp.
  const E0 = 800 * 0.12 ** 2 / 2, W = 0.25 * 0.4 * g * 0.6;
  nara(r('5.637')[0], Math.sqrt(2 * (E0 - W) / 0.4)); nara(r('5.637')[1], (E0 - W) / (0.4 * g));
  const stot = E0 / (0.25 * 0.4 * g); assert.equal(Math.floor(stot / 0.6) % 2, 1); nara(r('5.637')[2], stot - Math.floor(stot / 0.6) * 0.6);
  // 5.638: isärskjutning.
  const vA = Math.sqrt(2 * 0.2 * g * 1.6), vB = 0.6 * vA / 0.4;
  nara(r('5.638')[0], vA); nara(r('5.638')[1], vB ** 2 / (2 * 0.2 * g)); nara(r('5.638')[2], 100 * 0.4 * vB ** 2 / (0.6 * vA ** 2 + 0.4 * vB ** 2));
  // 6.565: kolven.
  const dp = 2.0 * g / 15e-4 / 1000; nara(r('6.565')[0], 101.3 + dp); nara(r('6.565')[1], 12 * (101.3 + dp) / (101.3 - dp));
  // 7.231: isbitarna.
  const qis = 2.10 * 0.054 * 18 + 334 * 0.054, qd = 4.18 * 0.33 * 22, per = qis / 3;
  nara(r('7.231')[0], qis); nara(r('7.231')[1], (qd - qis) / (4.18 * 0.384)); assert.equal(r('7.231')[2], Math.ceil(qd / per)); assert.ok(qd > qis);
  // 8.739: kretsen.
  const I = 12 / (4 + 4 + 0.5); nara(r('8.739')[0], 12 - 0.5 * I); nara(r('8.739')[1], (4 * I) ** 2 / 12);
  const Rx = r('8.739')[2], Rp = 1 / (1 / 6 + 1 / Rx); nara(12 - 0.5 * 12 / (4 + Rp + 0.5), 11.0, 1e-6);
  // 580 m rättas exakt: 600 får inte godtas som avrundning.
  assert.equal(q(fy, '3.746').svarVardesiffror[0], null);
});

test('delkorten är självbärande och läcker inte senare svar', () => {
  const m = q(ma, '3.1271');
  assert.match(m.spelDelar[1].fraga, /y=3x-2/); assert.match(m.spelDelar[2].fraga, /x=-2/);
  assert.doesNotMatch(m.t, /y=3x-2/); assert.doesNotMatch(m.spelDelar[0].s, /27|6\{,\}75/); assert.doesNotMatch(m.spelDelar[1].s, /\\tfrac\{27\}/);
  assert.doesNotMatch(q(ma, '3.1272').spelDelar[0].s, /-27|31/); assert.doesNotMatch(q(ma, '1.1100').spelDelar[0].s, /-0\{,\}25/);
  assert.doesNotMatch(q(fy, '4.910').spelDelar[0].s, /4\{,\}2|37\{,\}5/); assert.doesNotMatch(q(fy, '5.637').spelDelar[0].s, /1\{,\}3[12]|0\{,\}46/);
  for (const id of FY) for (const d of q(fy, id).spelDelar) assert.ok(d.t.startsWith(q(fy, id).spelIntro), id);
});
