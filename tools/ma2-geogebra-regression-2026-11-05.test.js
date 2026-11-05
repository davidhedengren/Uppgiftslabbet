'use strict';
// Ma2: regression och korrelation med GeoGebra-skärmbilder (5 november 2026).
// Se agent/MA2_REGRESSION_GEOGEBRA_BILDER_2026-11-05.md.
const {test} = require('node:test'), assert = require('node:assert/strict'), fs = require('fs'), vm = require('vm');
const c = {window: {}}; vm.runInNewContext(fs.readFileSync('uppgifterma2.js', 'utf8'), c);
const q = (id) => c.window.BANKMA2.find((x) => x.id === id);
const del = (id, e) => q(id).spelDelar.find((d) => d.etikett === e);
const bilder = (s) => [...s.matchAll(/src="(bilder\/[^"]+\.png)"/g)].map((m) => m[1]);
function linje(x, y) {
  const n = x.length, mx = x.reduce((a, b) => a + b) / n, my = y.reduce((a, b) => a + b) / n;
  const sxy = x.reduce((s, v, i) => s + (v - mx) * (y[i] - my), 0), sxx = x.reduce((s, v) => s + (v - mx) ** 2, 0), syy = y.reduce((s, v) => s + (v - my) ** 2, 0);
  return {k: sxy / sxx, m: my - (sxy / sxx) * mx, r: sxy / Math.sqrt(sxx * syy)};
}

const FACIT = {
  '4.138': [null, 'a', 'b', 'c'], '4.139': [null, 'a', 'b'], '4.141': [null], '4.146': [null], '2.773': [null], '4.400': [null],
  '4.2098': [null], '4.383': [null, 'a'], '4.2107': [null], '4.2129': [null], '2.372': [null],
};

test('Facit visar Tvåvariabels regressionsanalys steg för steg med riktiga bilder', () => {
  for (const [id, delar] of Object.entries(FACIT)) {
    for (const e of delar) {
      const s = e ? del(id, e).s : q(id).s;
      assert.match(s, /Tvåvariabels regressionsanalys/, id + (e || ''));
      assert.match(s, /geogebra-tvavariabel-meny\.png/, id + (e || ''));
      assert.match(s, /-regression\.png/, id + (e || ''));
      assert.match(s, /<p class="facit-svar">/, id + (e || ''));
      for (const b of bilder(s)) assert.ok(fs.statSync(b).size > 1000, `${id}: ${b}`);
    }
    assert.equal(q(id).geogebra, true, id);
  }
});

test('Ekvationerna och r i facit stämmer med en egen minsta kvadrat-beräkning och med rättSvar', () => {
  const f = (x, y) => linje(x, y);
  let L = f([1, 2, 3, 4, 5], [7, 10, 12, 15, 17]); assert.deepEqual([+L.k.toFixed(1), +L.m.toFixed(1)], Array.from(q('4.138').rättSvar).slice(0, 2));
  assert.ok(Math.abs(L.k * 6 + L.m - q('4.138').rättSvar[2]) < 1e-9);
  L = f([1, 2, 3, 4, 5], [12, 15, 17, 21, 24]); assert.deepEqual([+L.k.toFixed(2), +L.m.toFixed(2)], [3, 8.8]); assert.deepEqual(Array.from(q('4.139').rättSvar), [3, 8.8]);
  L = f([1, 2, 3, 4, 5], [48, 54, 61, 67, 70]); assert.deepEqual([+L.k.toFixed(1), +L.m.toFixed(1)], Array.from(q('4.146').rättSvar).slice(0, 2));
  L = f([0, 1, 2, 3, 4, 5, 6], [52.1, 55.8, 60.2, 63.7, 68.1, 71.6, 76.0]); assert.ok(Math.abs(L.k - 4) < 0.05 && Math.abs(L.m - 52) < 0.05);
  L = f([2, 3, 4, 5, 6, 7, 8], [14.2, 16.1, 18.5, 20.1, 22.4, 24.6, 26.3]); assert.equal(+L.k.toFixed(2), q('4.400').rättSvar);
  L = f([0, 1, 2, 3, 4], [24.5, 26.0, 27.8, 29.1, 30.9]); assert.equal(+L.k.toFixed(2), q('4.2098').rättSvar);
  L = f([12.0, 14.5, 17.2, 19.8, 22.4, 25.1, 27.6, 30.3], [14.1, 16.4, 19.3, 21.7, 24.6, 27.0, 29.8, 32.0]); assert.ok(Math.abs(L.r - q('4.383').rättSvar[0]) < 1e-6);
  L = f([36, 37, 39, 40, 41, 43, 44, 45], [160, 171, 166, 178, 172, 185, 177, 188]); assert.equal(+L.r.toFixed(2), q('4.2107').rättSvar);
  L = f([2, 4, 5, 7, 8, 10, 12], [11, 15, 13, 20, 17, 22, 25]); assert.equal(+L.r.toFixed(2), q('4.2129').rättSvar);
  assert.match(q('4.2107').s, /0\.8602/); assert.match(q('4.2129').s, /0\.9471/); assert.match(del('4.383', 'a').s, /0\.9996/);
  assert.match(q('4.139').s, /y = 3x \+ 8\.8/);
});

test('Delarna som inte använder regressionen är orörda', () => {
  assert.match(del('4.383', 'b').s, /16\{,\}0\/8=2\{,\}0/);
  assert.match(q('4.141').s, /En enstaka mätpunkt som avviker mycket/);
  assert.match(q('4.146').s, /utanför dataintervallet/);
  assert.doesNotMatch(q('4.146').s, /<strong>GeoGebra:<\/strong> Lägg x- och y-värden/);
});
