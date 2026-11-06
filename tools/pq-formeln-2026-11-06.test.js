'use strict';
/* pq-formeln i alla kurser, aldrig abc-formeln (användarbeslut 2026-11-06): "Vi använder PQ-formeln i alla kurser,
   inte ABC, ändra det i alla facit". Se agent/PQ_FORMELN_2026-11-06.md och tools/pq-formeln-2026-11-06.py. */
const {test} = require('node:test'), assert = require('node:assert/strict'), fs = require('node:fs'), vm = require('node:vm'), path = require('node:path');
const FILER = ['uppgifter.js', 'uppgifter2.js', 'uppgifterma1.js', 'uppgifterma2.js', 'uppgiftermato1.js', 'uppgiftermato2.js', 'uppgiftermatf1.js'];
const bank = f => { const c = {window: {}}; vm.runInNewContext(fs.readFileSync(path.join(__dirname, '..', f), 'utf8'), c); return Object.values(c.window).find(Array.isArray); };
const texter = x => [x.s, x.ledtrad, x.t, ...(x.spelDelar || []).flatMap(d => [d.s, d.ledtrad, d.t])].filter(Boolean);
// abc-formeln med insatta tal: √(b² ± 4·a·c), med bokstäver, eller som (b ± √D)/2a
const ABC = [/\\sqrt\{[^\]]{0,60}?\^2\s*[-+]\s*4\s*\\cdot/, /b\^2\s*-\s*4ac/, /\(\s*-?[\d{},.]+\s*\\pm\s*\\sqrt\{[^}]*\}\s*\)\s*\/\s*\d/];
// Ordet lösningsformeln får bara stå om differentialekvationer (Ma5 4.595, 4.626)
const ORD = /[Ll]ösningsformel|andragradsformel/;
const ORD_UNDANTAG = new Set(['uppgiftermatf1.js 4.595', 'uppgiftermatf1.js 4.626']);

test('Ingen abc-formel och inget ”lösningsformeln” för andragradsekvationer i någon bank', () => {
  const fel = [];
  for (const f of FILER) for (const x of bank(f)) for (const t of texter(x)) {
    if (ABC.some(r => r.test(t))) fel.push(`${f} ${x.id}: abc`);
    if (ORD.test(t) && !ORD_UNDANTAG.has(`${f} ${x.id}`)) fel.push(`${f} ${x.id}: ordet lösningsformeln`);
  }
  assert.deepEqual([...new Set(fel)], []);
});

test('De omskrivna faciten visar normalform och pq-formeln med samma rötter', () => {
  const fy1 = bank('uppgifter.js'), fy2 = bank('uppgifter2.js'), ma2 = bank('uppgifterma2.js'), m3 = bank('uppgiftermato1.js'), m4 = bank('uppgiftermato2.js'), m5 = bank('uppgiftermatf1.js');
  const q = (b, id) => b.find(x => x.id === id);
  for (const id of ['3.30', '3.123', '3.383', '3.388', '3.389', '3.400', '3.404']) assert.match(q(fy1, id).s, /Alternativ: pq-formeln/, id);
  assert.match(q(fy1, '3.30').s, /t\^2\+1\{,\}629t-4\{,\}481=0/);
  assert.match(q(fy1, '8.488').s, /12\{,\}5\\pm\\sqrt\{12\{,\}5\^2-150\}/);
  assert.match(q(fy2, '1.25').s, /t\^2-2\{,\}342t-5\{,\}703=0/);
  assert.match(q(ma2, '2.32').s, /pq-formeln/);
  assert.match(q(m3, '2.16').s, /\\frac12\\pm\\sqrt\{\\frac14\+5\}/);
  assert.match(q(m4, '4.402').s, /x\^2-4x\+13=0/);
  assert.match(q(m5, '2.152').s, /-2\\pm\\sqrt\{4\+117\}/);
  // Rötterna i pq-form, oberoende räknade
  const pq = (p, q_) => [-p / 2 - Math.sqrt(p * p / 4 - q_), -p / 2 + Math.sqrt(p * p / 4 - q_)];
  const nära = (a, b, tol) => assert.ok(Math.abs(a - b) <= tol, `${a} mot ${b}`);
  nära(pq(8 / 4.91, -22 / 4.91)[1], 1.453, 0.001);            // 3.30
  nära(pq(-25 / 4.91, 20 / 4.91)[0], 0.99, 0.005);             // 3.123
  nära(pq(11.5, -29.75)[1], 2.18, 0.005);                      // 3.383
  nära(pq(12.91 / 0.2314, -85 / 0.2314)[1], 5.95, 0.005);      // 3.388
  nära(pq(-31, 216)[0], 10.58, 0.005);                         // 3.389
  nära(pq(-35 / 4.91, -7 / 4.91)[1], 7.32, 0.005);             // 3.400
  nära(pq(-24 / 4.91, -2.5 / 4.91)[1], 4.99, 0.005);           // 3.404
  nära(pq(-11.5 / 4.91, -28 / 4.91)[1], 3.831, 0.0005);        // Fy2 1.25
});
