'use strict';
// Felrapporter 2026-11-18 12:36 (agent/FELRAPPORTER_2026-11-18_1236.md).
const test = require('node:test');
const assert = require('node:assert/strict');
const fs = require('fs');
const vm = require('vm');
const path = require('path');

const bank = (f) => { const c = { window: {} }; vm.runInNewContext(fs.readFileSync(path.join(__dirname, '..', f), 'utf8'), c); return Object.values(c.window).find(Array.isArray); };
const fy = bank('uppgifter.js'), ma4 = bank('uppgiftermato2.js'), ma1 = bank('uppgifterma1.js');
const q = (b, id) => b.find((t) => String(t.id) === id);
const lika = (a, b) => assert.equal(JSON.stringify(a), JSON.stringify(b));

test('Fy1 3.196: tabell i varje del, figur med riktningar och oförändrade svar', () => {
  const t = q(fy, '3.196');
  lika(t.rättSvar, [5, 2, -3, -4, -5, 3]);
  assert.match(t.t, /<table class="data">/); assert.match(t.t, /<svg/);
  assert.doesNotMatch(t.t + t.spelDelar.map((d) => d.t).join(''), /Hastigheterna är|nedan/);
  for (const d of t.spelDelar) {
    assert.ok(d.t.startsWith(t.spelIntro), d.etikett);
    assert.match(d.t, /<table class="data">.*<\/table><p>Hur stor är vagnens medelacceleration mellan 0 s och 2 s\?<\/p>$/, d.etikett);
  }
  assert.match(t.spelDelar[2].t, /<td>−5<\/td><td>−8<\/td><td>−11<\/td>/);
});

test('Fy1 3.651, 3.652: kraftuppgifter ligger i Vektorer i kraftkapitlet, inte i Hastighet som vektor', () => {
  for (const id of ['3.651', '3.652']) {
    const t = q(fy, id);
    assert.equal(t.omr, 'kraftvektorer'); assert.equal(t.kap, 4); assert.ok(t.omrTidigare.includes('vektorer'));
  }
  // Inga uppgifter om krafter finns kvar i Hastighet som vektor.
  for (const t of fy.filter((x) => x.omr === 'vektorer')) {
    const text = t.t.replace(/<svg[\s\S]*?<\/svg>/g, '').replace(/<[^>]+>/g, ' ');
    assert.doesNotMatch(text, /kraft/i, t.id);
    assert.doesNotMatch(text, /(?:^|[\s(])N(?:[\s.,)]|$)/, t.id);
    assert.ok(![].concat(t.svarEnhet || []).includes('N'), t.id);
  }
});

test('Ma4 cirkelsektorn: längder och areor med π godtar både exakt svar och närmevärde', () => {
  const fall = { '1.319': [0, 1, 2], '1.324': [0, 1, 2], '1.118': [1, 2], '1.124': [0, 1], '1.167': [0, 1], '1.306': [0, 1, 3] };
  const varde = { '1.319': [2, 5, 7.5], '1.324': [49 / 12, 49 / 4, 49 / 3], '1.118': [4, 12], '1.124': [4, 12], '1.167': [10, 60], '1.306': [5 / 3, 10, 6] };
  for (const [id, delar] of Object.entries(fall)) {
    const t = q(ma4, id);
    delar.forEach((i, k) => {
      assert.equal(t.svarFormat[i], 'numeriskt', `${id} ${i}`);
      assert.ok(Math.abs(t.rättSvar[i] - varde[id][k] * Math.PI) < 1e-12, `${id} ${i}`);
      assert.equal(t.tolerans[i], 1e-9, `${id} ${i}`);
    });
    assert.match(t.s, /\\approx/, id);
  }
  // Frågor som kräver exakt svar behåller uttrycksformatet.
  assert.equal(q(ma4, '1.463').svarFormat, 'uttryck'); assert.equal(q(ma4, '1.471').svarFormat, 'uttryck');
});

test('Ma4 1.424: facit visar formelbladets 1/√2 och √2/2', () => {
  const t = q(ma4, '1.424');
  assert.match(t.s, /Formelbladet: \\\(\\cos45\^\\circ=\\tfrac\{1\}\{\\sqrt2\}\\\)/);
  assert.match(t.s, /Svar:<\/strong> \\\(\\frac\{1\}\{\\sqrt2\}\\\), som också kan skrivas/);
  assert.equal(t.rättSvar, 'sqrt(2)/2'); assert.equal(t.svarFormat, 'uttryck');
});

test('Ma1 2.306 c: konkret fråga, självbärande kort och facit utan kommutativ', () => {
  const t = q(ma1, '2.306'), c = t.spelDelar[2];
  assert.match(c.t, /f\(g\(3\)\)=25\\\) men att \\\(g\(f\(3\)\)=12/);
  assert.doesNotMatch(t.s + c.s, /kommutativ|Steg 1/);
  assert.equal((t.s.match(/class="facit-del"/g) || []).length, 3);
  lika(t.rättSvar, [25, 12, null]);
});

test('Ma1 1.87: formen 4(b − 2)(…) står i frågan och svaret rättas som uttryck', () => {
  const t = q(ma1, '1.87');
  assert.equal(t.rättSvar, '2a+3'); assert.equal(t.svarFormat, 'uttryck');
  assert.match(t.t, /4\(b-2\)\\cdot\(\\ \\ldots\\ \)/);
  assert.doesNotMatch(t.t, /utan parenteser/);
});
