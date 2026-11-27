'use strict';
// Kvalitetsrapporten 2026-11-27, omgång 2 (agent/KVALITETSRAPPORT_2026-11-27.md): miniräknare och figuretiketter.
const { test } = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const las = (f) => { const s = fs.readFileSync(path.join(__dirname, '..', f), 'utf8'); return JSON.parse(s.slice(s.indexOf('['), s.lastIndexOf(']') + 1)); };
const hitta = (f, id) => las(f).find((x) => String(x.id) === id);
const svg = (q) => JSON.stringify(q).replace(/\\"/g, '"').match(/<svg.*?<\/svg>/)[0];

test('Ma3c 1.980 har miniräknare (175/40 m görs inte snabbt i huvudet)', () => {
  assert.equal(hitta('uppgiftermato1.js', '1.980')['miniräknare'], true);
});

test('Flaggade etiketter har vit kant (paint-order="stroke")', () => {
  const lista = JSON.parse(fs.readFileSync(path.join(__dirname, 'svg-etikettkant-2026-11-27.json'), 'utf8'));
  assert.equal(lista.length, 119);
  let antal = 0;
  for (const { bank, id, etiketter } of lista) {
    const s = JSON.stringify(hitta(bank, id)).replace(/\\"/g, '"');
    const avkoda = (x) => x.replace(/<[^>]+>/g, '').replace(/&#(\d+);/g, (m, n) => String.fromCodePoint(+n))
      .replace(/&#x([0-9a-f]+);/gi, (m, n) => String.fromCodePoint(parseInt(n, 16))).replace(/&lt;/g, '<').replace(/&gt;/g, '>').replace(/&amp;/g, '&').trim();
    const kantade = [...s.matchAll(/<text([^>]*)>(.*?)<\/text>/g)].filter((m) => /paint-order="stroke"/.test(m[1])).map((m) => avkoda(m[2]));
    for (const e of etiketter) {
      assert.ok(kantade.some((k) => k === e || (e.length === 24 && k.startsWith(e))), `${bank} ${id} ${e}`);
      antal++;
    }
  }
  assert.equal(antal, 172);
});

test('Flyttade etiketter', () => {
  for (const [f, id] of [['uppgifterma1.js', '2.56'], ['uppgifterma1.js', '2.58'], ['uppgifterma2.js', '2.210'], ['uppgifterma2.js', '2.413']]) {
    const s = svg(hitta(f, id));
    assert.doesNotMatch(s, /x="391.60" y="(?:192.67|207.86)"[^>]*>f</, `${f} ${id}`);
    assert.match(s, /text-anchor="end"[^>]*>f<\/text>/, `${f} ${id}`);
  }
  assert.match(svg(hitta('uppgiftermato1.js', '3.501')), /<text x="250" y="62" text-anchor="end"[^>]*>2x\+1<\/text>/);
  assert.match(svg(hitta('uppgiftermato2.js', '4.589')), /<text x="164.7" y="128.0" text-anchor="middle"[^>]*font-weight="bold"[^>]*>−3<\/text>/);
});
