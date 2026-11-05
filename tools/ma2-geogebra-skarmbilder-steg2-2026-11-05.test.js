'use strict';
// Ma2: GeoGebra-skärmbilder i resten av statistikfacit med Envariabelanalys (steg 2, 5 november 2026).
// Se agent/MA2_STATISTIK_GEOGEBRA_SKARMBILDER_2026-11-05.md.
const {test} = require('node:test'), assert = require('node:assert/strict'), fs = require('fs'), vm = require('vm');
const c = {window: {}}; vm.runInNewContext(fs.readFileSync('uppgifterma2.js', 'utf8'), c);
const q = (id) => c.window.BANKMA2.find((x) => x.id === id);
const del = (id, e) => q(id).spelDelar.find((d) => d.etikett === e);
const sx = (v) => { const m = v.reduce((a, b) => a + b, 0) / v.length; return Math.sqrt(v.reduce((a, b) => a + (b - m) ** 2, 0) / (v.length - 1)); };
const ut = (v, f) => f.flatMap((n, i) => Array(n).fill(v[i]));

// uppgift -> delar som fått GeoGebra-steg (null = ett enda facit)
const DELAR = {
  '4.05': ['b'], '4.10': [null], '4.11': ['a', 'b'], '4.14': [null], '4.28': ['a', 'b'], '4.41': ['a', 'b'], '4.46': [], '4.61': ['a', 'b', 'c'],
  '4.97': [], '4.157': [], '4.174': [null], '4.175': [null], '4.212': [null], '4.235': [null], '4.241': ['a', 'b'], '4.283': [null], '4.284': [null],
  '4.299': ['a', 'b', 'd'], '4.302': ['a', 'b'], '4.303': [null], '5.41': ['a', 'b', 'c', 'd'], '5.66': [], '5.71': [null], '5.94': [null], '5.110': [null],
  '4.310': [null], '4.311': ['a', 'b'], '4.317': [null], '4.322': ['a', 'b', 'c'], '4.323': ['a', 'b', 'c'], '4.324': ['a', 'b', 'c'], '4.325': ['a', 'b', 'c'],
  '4.326': ['a', 'b', 'c'],
'4.348': ['a', 'b'], '4.349': ['a', 'b', 'c'], '4.350': ['a', 'b', 'c'], '4.351': ['a', 'b', 'c', 'd'], '4.360': [null],
  '4.361': ['a'], '4.362': [null], '4.364': ['a', 'b', 'c', 'd'], '4.365': ['a'], '4.366': ['a'], '4.371': ['a', 'b'], '4.373': ['a', 'b', 'c'], '4.384': [null], '4.385': [null],
  '4.386': [null], '4.387': [null], '4.388': [null], '4.389': [null], '4.390': [null], '4.391': [null], '4.392': [null], '4.393': [null], '4.454': [null],
  '4.458': [null], '4.461': [null], '4.463': [null], '4.2015': [null], '4.2016': [null],
};
const bilder = (s) => [...s.matchAll(/src="(bilder\/geogebra-[^"]+\.png)"/g)].map((m) => m[1]);

test('Varje omarbetat facit visar GeoGebra steg för steg med riktiga bilder', () => {
  for (const [id, delar] of Object.entries(DELAR)) {
    const x = q(id);
    // 4.212, 4.384 och 4.385 kräver ingen beräkning; GeoGebra visas bara som kontroll och flaggan behålls.
    if (!['4.212', '4.384', '4.385'].includes(id)) assert.equal(x.geogebra, true, id);
    assert.equal(x.miniräknare, true, id);
    const fac = [x.s, ...delar.filter(Boolean).map((e) => del(id, e).s)];
    for (const s of fac) {
      assert.match(s, /Envariabelanalys/, id);
      for (const b of bilder(s)) assert.ok(fs.statSync(b).size > 1000, `${id}: ${b}`);
    }
    assert.ok(bilder(x.s).length >= 4, id + ': för få bilder i huvudfacit');
    for (const e of delar.filter(Boolean)) {
      const s = del(id, e).s;
      assert.match(s, /geogebra-kalkylblad-perspektiv\.png/, id + e);
      assert.match(s, /geogebra-envariabelanalys-meny\.png/, id + e);
      assert.match(s, /bilder\/geogebra-[0-9-a-z]+-data\.png/, id + e);
      assert.match(s, /-(stolp|analys)\.png/, id + e);
      assert.match(s, /<p class="facit-svar">/, id + e);
    }
  }
});

test('Delkort avslöjar inte senare delars svar', () => {
  for (const id of ['4.364']) {   // 4.343–4.345 kontrolleras i ma2-geogebra-stegbilder-testet
    for (const e of ['a', 'b']) assert.doesNotMatch(del(id, e).s, /raden s|-medel-s|-min-max|-q1-q3/, id + e);
    assert.doesNotMatch(del(id, 'c').s, /raden (Min|Max|Q1|Q3)/, id);
  }
  assert.doesNotMatch(del('4.351', 'a').s, /På raden (Median|Q1|Q3)/);
  assert.doesNotMatch(del('4.11', 'a').s, /raden Median/);
  assert.doesNotMatch(del('4.28', 'a').s, /raden s/);
});

test('Datamängderna i bilderna ger nycklarnas Sx', () => {
  const fall = [
    ['4.283', [58, 60, 60, 62, 68, 70, 70, 72], q('4.283').rättSvar[1]],
    ['4.345', ut([1, 2, 3, 4, 5], [1, 2, 1, 2, 1]), q('4.345').rättSvar[2][1]],
    ['4.350b', ut([0, 1, 2, 3, 4], [3, 1, 2, 1, 3]), q('4.350').rättSvar[1][1]],
    ['4.351', ut([10, 20, 30, 40, 50], [2, 3, 1, 1, 1]), q('4.351').rättSvar[0][1]],
    ['4.364', ut([6.5, 7, 7.5, 8, 8.5], [4, 8, 10, 6, 2]), q('4.364').rättSvar[2][1]],
    ['4.365', ut([45, 55, 65, 75], [4, 10, 12, 4]), q('4.365').rättSvar[0][1]],
    ['4.366', ut([2.5, 7.5, 12.5, 17.5], [6, 14, 8, 2]), q('4.366').rättSvar[0][1]],
    ['4.373', ut([120, 150, 210], [5, 10, 5]), q('4.373').rättSvar[0][1]],
    ['4.390B', [9, 14, 20, 12, 22, 18, 11, 21, 17, 16], 4.4],
  ];
  for (const [n, v, r] of fall) assert.ok(Math.abs(sx(v) - r) < 0.05, n);
  // 4.212 och 4.384 bygger på prickdiagrammen
  assert.ok(sx([2, 2, 2, 7, 7, 12, 12, 12]) > sx([2, 6, 7, 7, 7, 7, 8, 12]));
  assert.ok(Math.abs(sx([4, 5, 8, 10, 10, 12, 15, 16]) - 4.31) < 0.005);
});
