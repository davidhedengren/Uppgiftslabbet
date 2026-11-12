'use strict';
// Felrapporter 2026-11-12 18:41 (agent/FELRAPPORTER_2026-11-12_1841.md): AI kapitel 1 och 4, Ma5 och Ma2.
const test = require('node:test');
const assert = require('node:assert/strict');
const fs = require('fs');
const vm = require('vm');
const path = require('path');

const las = (f) => { const c = { window: {} }; vm.runInNewContext(fs.readFileSync(path.join(__dirname, '..', f), 'utf8'), c); return Object.values(c.window).find(Array.isArray); };
const ai = las('uppgifterai.js'), ma5 = las('uppgiftermatf1.js'), ma2 = las('uppgifterma2.js');
const q = (b, id) => b.find((t) => t.id === id);
const del = (t, e) => t.spelDelar.find((d) => d.etikett === e);
const utanSvg = (h) => h.replace(/<svg[\s\S]*?<\/svg>/g, '');

test('AI 4.65 m.fl.: punkternas förklaring står i diagrammet, inte i texten', () => {
  for (const id of ['4.60', '4.61', '4.63', '4.64', '4.65', '4.66', '4.68', '4.70', '4.74']) {
    const t = q(ai, id);
    assert.doesNotMatch(utanSvg(t.spelIntro), /Blå cirklar|Orange kvadrater|Gröna trianglar|Kryss: klustercentrum/, id);
    assert.match(t.spelIntro, /<svg[\s\S]*(ny punkt|klustercentrum)<\/text>[\s\S]*<\/svg>/, id);
  }
});

test('AI neurala: vikter, bias och indata står i figuren och inte i texten, med rätt formel', () => {
  for (const t of ai.filter((x) => x.omr === 'neurala' && /<svg/.test(x.spelIntro) && !/natverk|Indata<\/text>/.test(x.spelIntro))) {
    const text = utanSvg(t.spelIntro);
    assert.doesNotMatch(text, /Vikterna är|bias är|bias b =|En artificiell neuron multiplicerar/, t.id);
    const n = (t.spelIntro.match(/<rect x="6" y="\d+" width="84"/g) || []).length;
    const formel = Array.from({ length: n }, (_, i) => `w${'₁₂₃'[i]}x${'₁₂₃'[i]}`).join(' + ') + ' + b';
    assert.ok(t.spelIntro.includes(`z = ${formel}`), `${t.id}: ${formel}`);
  }
  assert.match(q(ai, '4.84').spelIntro, /x₁: antalet elever som har önskat<\/text>.*boken<\/text>/);
  assert.match(q(ai, '4.83').spelIntro, /z = w₁x₁ \+ w₂x₂ \+ w₃x₃ \+ b/);
});

test('AI 4.85: del b har en egen figur med det nya bias, utanför <p>', () => {
  const t = q(ai, '4.85'), b = del(t, 'b');
  assert.match(t.spelIntro, /b = −6/); assert.doesNotMatch(t.spelIntro, /b = −4/);
  assert.match(b.fraga, /<\/p><svg[\s\S]*b = −4[\s\S]*<\/svg>$/);
  assert.doesNotMatch(del(t, 'a').fraga, /<svg/);
  assert.equal(b.rättSvar, 1);
});

test('AI 4.10 c och 4.83 c: luriga alternativ med kommentarer', () => {
  for (const [id, e, ratt] of [['4.10', 'c', 'Träna på fler bilder, tagna i olika väder, ljus och vinklar'],
    ['4.83', 'c', 'Ett nästan tomt batteri sänker z med 5, och det väger tyngst av alla tre indata']]) {
    const d = del(q(ai, id), e);
    assert.equal(d.rättSvar, ratt);
    assert.equal(d.alternativ.length, 4);
    assert.equal(d.alternativ.filter((a) => a.ratt).length, 1);
    for (const a of d.alternativ) assert.ok(a.kommentar.length > 30, `${id}: ${a.txt}`);
    const langd = d.alternativ.map((a) => a.txt.length);
    assert.ok(Math.max(...langd) / Math.min(...langd) < 1.6, `${id}: alternativen ska vara ungefär lika långa`);
  }
});

test('AI 1.14 b och grannordning: frågan säger vad som ska skrivas', () => {
  const b = del(q(ai, '1.14'), 'b');
  assert.match(b.fraga, /S och A är redan uttagna\. I vilken ordning tas resten av noderna ut, fram till och med målet F\?/);
  assert.match(b.fraga, /Skriv noderna i ordning, åtskilda med kommatecken/);
  assert.equal(b.rättSvar, 'B, C, D, E, F');
  for (const id of ['1.60', '1.18', '1.99']) {
    for (const f of ['t', 'spelIntro']) assert.match(q(ai, id)[f], /Grannordningen är den ordning som grannarna till en ruta prövas i\./, id);
  }
});

test('AI har ett formelblad med klassificeringsmåtten', () => {
  const pdf = fs.readFileSync(path.join(__dirname, '..', 'formelblad', 'ai.pdf'));
  assert.equal(pdf.subarray(0, 5).toString(), '%PDF-');
});

test('Ma5: ingen heltalskombination av sgd, men sgd och mgm med Euklides algoritm', () => {
  for (const id of ['2.217', '2.115', '2.327']) {
    const t = q(ma5, id);
    assert.doesNotMatch(t.t + t.s + t.ledtrad, /heltalskombination|linjärkombination/i, id);
    assert.match(t.t, /Euklides algoritm/, id);
    assert.equal((t.s.match(/<li>/g) || []).length, (t.s.match(/facit-rubrik/g) || []).length, id);
    assert.match(t.s, /facit-svar"><strong>Svar:<\/strong>/, id);
  }
  assert.doesNotMatch(ma5.map((t) => t.t).join(' '), /heltalskombination/i);
  assert.match(q(ma5, '2.217').s, /11\\,628/); assert.match(q(ma5, '2.115').s, /=420/);
  // 2.327: varje rest delas av d
  for (const r of ['d\\mid16', 'd\\mid10', 'd\\mid6', 'd\\mid4', 'd\\mid2']) assert.ok(q(ma5, '2.327').s.includes(r), r);
});

test('Ma2 3.439: måttet 15 cm gäller hela BC, i uppgiften och i båda delkorten', () => {
  const t = q(ma2, '3.439');
  for (const txt of [t.t, ...t.spelDelar.map((d) => d.t)]) {
    assert.match(txt, />BC = 15 cm<\/text>/);
    assert.doesNotMatch(txt, />15 cm<\/text>/);
    assert.match(txt, /<line x1="60" y1="326" x2="480" y2="326"/);
  }
  assert.deepEqual(Array.from(t.rättSvar), [9, '4/3']);
});
