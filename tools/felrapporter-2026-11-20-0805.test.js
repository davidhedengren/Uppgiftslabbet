'use strict';
// Felrapporter 2026-11-20 08:05. Se agent/FELRAPPORTER_2026-11-20_0805.md.
const { test } = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');

const ROT = path.join(__dirname, '..');
const bank = (fil) => {
  const s = fs.readFileSync(path.join(ROT, fil), 'utf8');
  return JSON.parse(s.slice(s.indexOf('['), s.lastIndexOf(']') + 1));
};
const hamta = (b) => (id) => {
  const q = b.find((x) => x.id === id);
  assert.ok(q, id);
  return q;
};
const ma1 = hamta(bank('uppgifterma1.js'));
const ma2 = hamta(bank('uppgifterma2.js'));
const mato1 = hamta(bank('uppgiftermato1.js'));
const mato2 = hamta(bank('uppgiftermato2.js'));
const fy2 = hamta(bank('uppgifter2.js'));
const text = (h) => String(h || '').replace(/<svg[\s\S]*?<\/svg>/g, ' ').replace(/<[^>]+>/g, ' ');
const formatLista = (q) => [].concat(q.svarFormat);

test('Ma1 0.1383 och 0.1362: enhets- och prefixbyten godtar grundpotensform (omvandling)', () => {
  assert.equal(ma1('0.1383').svarFormat, 'omvandling');
  assert.equal(ma1('0.1383').svarEnhet, 'W');
  assert.equal(ma1('0.1383').rättSvar, 1.5e9);
  assert.deepEqual(formatLista(ma1('0.1362')), ['omvandling', 'omvandling', 'omvandling', 'omvandling']);
  assert.deepEqual(Array.from(ma1('0.1362').rättSvar), [1200, 0.8, 3000, 50000]);
  const alla = bank('uppgifterma1.js');
  const kvar = alla.filter((q) => ['prefix', 'enhetsbyten'].includes(q.omr) && formatLista(q).includes('decimalform'));
  // Dessa fyra säger i kgInstruktion att svaret ska skrivas som vanligt tal och behåller decimalform.
  assert.deepEqual(kvar.map((q) => q.id).sort(), ['0.244', '0.246', '0.560', '0.562']);
  for (const q of kvar) assert.match(text(q.kgInstruktion), /vanligt tal|tiopotens/i, q.id);
  assert.equal(alla.filter((q) => formatLista(q).includes('omvandling')).length, 123);
  // Där decimalformen är det som tränas står formatet kvar.
  for (const id of ['0.236', '0.415', '0.607', '0.1100', '0.1384']) assert.ok(formatLista(ma1(id)).every((f) => f === 'decimalform'), id);
});

test('Ma1 0.825: facit visar att 15:31 också kan skrivas som bråk', () => {
  const q = ma1('0.825');
  assert.equal(q.rättSvar, '15:31');
  assert.equal(7500 / 15500, 15 / 31);
  assert.match(q.s, /\\tfrac\{15\}\{31\}/);
});

test('Ma1 0.1004: ordningen för avrundningen står i frågan', () => {
  const q = ma1('0.1004');
  const priser = [12.45, 8.49, 23.5, 6.45, 9.48];
  const emma = priser.map((p) => Math.floor(p + 0.5)).reduce((a, b) => a + b);
  const kassa = Math.round(priser.reduce((a, b) => a + b));
  assert.equal(kassa - emma, q.rättSvar);
  assert.match(text(q.t), /avrundar först varje pris/);
  assert.match(text(q.t), /Kassan lägger i stället ihop de exakta priserna och avrundar summan/);
  assert.doesNotMatch(text(q.t), /skiljer hennes summa från den exakta summan avrundad/);
  assert.match(q.s, /facit-rubrik/);
  assert.match(q.s, /60\{,\}37/);
});

const RADIANER = ['1.30', '1.73', '1.136', '1.291', '1.297', '1.154', '1.155', '1.156', '1.157', '1.158', '1.159',
  '1.151', '1.518', '1.522', '1.524'];

test('Ma4 1.156 med flera: perioden efterfrågas i radianer, även på delkortet', () => {
  for (const id of RADIANER) {
    const q = mato2(id);
    assert.equal(q.omr, 'kurvor_radianer', id);
    assert.match(text(q.t), /radianer/, id);
    for (const d of q.spelDelar || []) {
      const fr = text(d.fraga || d.t);
      if (/period/.test(fr)) assert.match(fr + text(q.spelIntro), /radianer/, id + d.etikett);
    }
  }
  assert.match(text(mato2('1.151').spelIntro), /x\s*\\\)\s*är i radianer/);
  const q = mato2('1.156');
  assert.deepEqual(Array.from(q.rättSvar), ['pi', -1]);
  assert.match(q.s, /T=\\dfrac\{2\\pi\}\{k\}/);
  assert.match(q.spelDelar[0].s, /T=\\frac\{2\\pi\}\{2\}=\\pi/);
  assert.match(q.spelDelar[1].s, /2\+3\\cdot\(-1\)=-1/);
  assert.doesNotMatch(q.s, /Varför metoden fungerar/);
  assert.doesNotMatch(text(q.ledtrad), /grafen/);
});

test('Ma4 1.672: toleransen godtar bara korrekt avrundade tre decimaler', () => {
  const q = mato2('1.672');
  assert.ok(Math.abs(q.rättSvar - 2 * Math.SQRT2) < 1e-12);
  assert.equal(q.tolerans, 0.0005);
  assert.ok(Math.abs(2.828 - q.rättSvar) <= q.tolerans);
  assert.ok(Math.abs(2.829 - q.rättSvar) > q.tolerans);
  assert.ok(Math.abs(2.827 - q.rättSvar) > q.tolerans);
});

test('Ma4 2.685: axelnamnet t (min) står till höger om pilen, inte på kurvan', () => {
  const q = mato2('2.685');
  const svg = q.t.match(/<svg[\s\S]*?<\/svg>/)[0];
  assert.match(svg, /viewBox="0 0 510 300"/);
  assert.match(svg, /<text x="458\.0" y="263\.0"[^>]*text-anchor="start"[^>]*>t \(min\)<\/text>/);
  assert.equal(q.rättSvar, 6);
  assert.match(q.s, /9-3=6/);
});

test('Ma2 3.143 med flera och Ma3c 4.119: svaren rättas i valfri ordning', () => {
  for (const q of [ma2('3.140'), ma2('3.141'), ma2('3.143'), ma2('3.187'), mato1('4.119')]) {
    assert.equal(q.svarsstruktur, 'mängd', q.id);
    assert.equal(q.rättSvar.length, 2, q.id);
  }
  assert.deepEqual(Array.from(ma2('3.143').rättSvar), [5, 12]);
  assert.equal(5 + 12, 34 / 2);
  assert.equal(5 ** 2 + 12 ** 2, 13 ** 2);
});

test('Fy2 2.164: måtten ligger utanför bassängen', () => {
  const q = fy2('2.164');
  const svg = q.t.match(/<svg[\s\S]*?<\/svg>/g);
  assert.equal(svg.length, 1);
  const rect = svg[0].match(/<rect x="60" y="56" width="400" height="200"/);
  assert.ok(rect);
  const pos = (etikett) => {
    const m = svg[0].match(new RegExp('<text x="([\\d.]+)" y="([\\d.]+)"[^>]*>' + etikett + '</text>'));
    assert.ok(m, etikett);
    return { x: +m[1], y: +m[2] };
  };
  assert.ok(pos('0,50 m').y < 56);
  assert.ok(pos('2,0 m').x < 60);
  assert.ok(pos('3,0 m').y > 256);
  // P ligger i ett minimum: vägskillnaden är en halv våglängd.
  const r1 = Math.hypot(2, 1), r2 = Math.hypot(2, 2);
  assert.ok(Math.abs(r2 - r1 - 1.18 / 2) < 0.01);
  assert.equal(q.alternativ.find((a) => a.ratt).txt, 'Minimum');
});

test('Kunskapsgymmet: rättningen för omvandling, a/b, a.e. och närmevärde finns', { skip: !fs.existsSync(path.join(ROT, '..', 'kunskapsgymmet', 'index.html')) }, () => {
  const html = fs.readFileSync(path.join(ROT, '..', 'kunskapsgymmet', 'index.html'), 'utf8');
  assert.match(html, /case "decimalform": case "omvandling":/);
  assert.match(html, /\["decimalform","omvandling","energi_per_nukleon"/);
  assert.match(html, /Förhållandet a:b får också skrivas som a\/b/);
  assert.match(html, /Areaenheter utan fysisk enhet/);
  assert.match(html, /Exakt värde följt av närmevärde/);
});
