'use strict';
/* Ma1 faktorisering 2026-11-06, #1.1685–1.1704: bryt ut största gemensamma faktor.
   Testet kontrollerar varje svar oberoende av byggskriptet tools/bygg-ma1-faktorisering-2026-11-06.py:
   produkten ska vara lika med frågans polynom, och parentesen får inte ha någon gemensam faktor kvar.
   Formatet "största_faktor" kräver just detta i Kunskapsgymmet. Logg: agent/MA1_FAKTORISERING_2026-11-06.md */
const test = require('node:test'), assert = require('node:assert/strict'), fs = require('node:fs'), path = require('node:path'), vm = require('node:vm');
const c = {window: {}}; vm.runInNewContext(fs.readFileSync(path.join(__dirname, '../uppgifterma1.js'), 'utf8'), c);
const byId = new Map(c.window.BANKMA1.map(u => [u.id, u]));
const NYA = Array.from({length: 20}, (_, i) => `1.${1685 + i}`);

/* '12x^2y^3-18xy^2' → [{k:12, e:{x:2,y:3}}, {k:-18, e:{x:1,y:2}}] */
function poly(s) {
  return s.replace(/\\cdot|\s|[{}]/g, '').match(/[+-]?[^+-]+/g).map(t => {
    const m = t.match(/^([+-]?)(\d*)((?:[a-z](?:\^\d+)?)*)$/);
    assert.ok(m && (m[2] || m[3]), 'kan inte tolka ' + t);
    const e = {};
    for (const [, v, p] of m[3].matchAll(/([a-z])(?:\^(\d+))?/g)) e[v] = (e[v] || 0) + Number(p || 1);
    return {k: Number(m[2] || 1) * (m[1] === '-' ? -1 : 1), e};
  });
}
const varde = (termer, x) => termer.reduce((s, t) => s + t.k * Object.entries(t.e).reduce((p, [v, n]) => p * x[v] ** n, 1), 0);
const gcd = (a, b) => b ? gcd(b, a % b) : Math.abs(a);

test('20 uppgifter, 42 kort, alla med formatet största_faktor', () => {
  let n = 0;
  for (const id of NYA) {
    const u = byId.get(id);
    assert.equal(u.omr, 'faktorisering'); assert.equal(u.miniräknare, false);
    for (const f of [].concat(u.svarFormat)) { assert.equal(f, 'största_faktor'); n++; }
  }
  assert.equal(n, 42);
});

/* Äldre tvåfältsuppgifter som gjordes om till ett fält samma dag (tools/ma1-faktorisering-ett-falt-2026-11-06.py). */
const GAMLA = ['1.03', '1.24', '1.25', '1.29', '1.30', '1.31', '1.90', '1.94', '1.160', '1.162', '1.165', '1.195', '1.217', '1.259',
  '1.260', '1.262', '1.406', '1.407', '1.414', '1.415', '1.416', '1.417', '1.434', '1.911', '1.912', '1.913', '1.916', '1.917',
  '1.918', '1.1044', '1.1045', '1.1046', '1.1047', '1.1048', '1.1049'];

test('35 äldre uppgifter har ett svarsfält med hela det faktoriserade uttrycket', () => {
  assert.equal(GAMLA.length, 35);
  for (const id of GAMLA) {
    const u = byId.get(id);
    assert.equal(u.svarstyp, 'uttryck', id); assert.equal(u.svarFormat, 'största_faktor', id);
    assert.equal(typeof u.rättSvar, 'string', id);
    assert.equal(u.svarEtiketter, undefined, id); assert.equal(u.svarsstruktur, undefined, id);
    assert.doesNotMatch(u.t, /fält/, id);
    assert.match(u.s, /Dividera varje term med/); assert.match(u.s, /Kontroll: multiplicera in/); assert.match(u.s, /facit-svar/);
  }
  // 1.261 kräver att parentesen börjar med 2x och behåller därför sina två fält.
  assert.equal(JSON.stringify(byId.get('1.261').svarFormat), '["förenklat_polynom","förenklat_polynom"]');
});

test('svaret är frågans polynom med största möjliga faktor utbruten', () => {
  for (const id of [...NYA, ...GAMLA]) {
    const u = byId.get(id);
    const fragor = u.spelDelar ? u.spelDelar.map(d => d.t.match(/\\\((.+?)\\\)/)[1]) : [u.t.match(/\\\((.+?)\\\)/)[1]];
    const svar = [].concat(u.rättSvar);
    fragor.forEach((f, i) => {
      const P = poly(f.replace(/\^\{(\d+)\}/g, '^$1'));
      const m = svar[i].match(/^(-?\d*(?:[a-z](?:\^\d+)?)*)\((.+)\)$/);
      assert.ok(m, `${id}: ${svar[i]}`);
      const M = poly(m[1] === '-' ? '-1' : m[1] || '1')[0], I = poly(m[2]);
      for (const x of [{x: 2, y: 3, a: -1, b: 5, m: 2, n: -3}, {x: -3, y: 2, a: 4, b: -2, m: -1, n: 4}, {x: 0.5, y: -1, a: 3, b: 7, m: 3, n: 0.5}])
        assert.ok(Math.abs(varde([M], x) * varde(I, x) - varde(P, x)) < 1e-9, `${id}: ${svar[i]} ≠ ${f}`);
      assert.equal(I.map(t => t.k).reduce(gcd), 1, `${id}: talfaktor kvar i ${m[2]}`);
      for (const v of new Set(I.flatMap(t => Object.keys(t.e)))) assert.ok(I.some(t => !t.e[v]), `${id}: ${v} kvar i alla termer`);
    });
  }
});

test('stigande träningsnivå, egen ledtråd och fullständigt facit med kontroll', () => {
  for (const id of NYA) {
    const u = byId.get(id);
    for (const d of u.spelDelar || [u]) {
      assert.match(d.s, /Dividera varje term med/); assert.match(d.s, /Kontroll: multiplicera in/); assert.match(d.s, /facit-svar/);
      assert.match(d.ledtrad, /delbara med|bokstav/);
    }
    if (u.spelDelar) {
      const niv = u.spelDelar.map(d => d.traningsniva);
      assert.ok(niv.every((x, i) => i === 0 || x >= niv[i - 1]), `${id}: ${niv}`);
    }
  }
});
