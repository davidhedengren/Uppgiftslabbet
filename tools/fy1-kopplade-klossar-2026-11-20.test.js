'use strict';
// Fy1 newton2: kopplade klossar med snören och trissor, 4.979–4.1004 (2026-11-20).
// Se agent/FY1_KOPPLADE_KLOSSAR_2026-11-20.md. Svaren räknas om här oberoende av byggskriptet.
const { test } = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');

const ROT = path.join(__dirname, '..');
const src = fs.readFileSync(path.join(ROT, 'uppgifter.js'), 'utf8');
const bank = JSON.parse(src.slice(src.indexOf('['), src.lastIndexOf(']') + 1));
const IDS = Array.from({ length: 26 }, (_, i) => `4.${979 + i}`);
const Q = Object.fromEntries(bank.filter((q) => IDS.includes(q.id)).map((q) => [q.id, q]));
const g = 9.82;
const text = (h) => String(h || '').replace(/<svg[\s\S]*?<\/svg>/g, ' ').replace(/<[^>]+>/g, ' ');

const VANTADE = {
  '4.979': [10], '4.980': [10 / 3, 10 / 3], '4.981': [10 / 6, 10 / 6, 5], '4.982': [9], '4.983': [7 / 3, 10 / 3],
  '4.984': [g / 3, 4 * g / 3], '4.985': [5 * g / 7, 12 * g / 7, 8 * g / 7], '4.986': [g / 3, 2 * g / 3],
  '4.987': [2 * g / 3, 4 * g / 3, g], '4.988': [g / 6, g / 2, 5 * g / 6],
  '4.989': [(2 * g - 1) / 3, (2 * g - 1) / 3 + 1],
  '4.990': [(5 * g - 1) / 6, (5 * g - 1) / 6 + 1, 2 * (g - (5 * g - 1) / 6)], '4.991': [g / 2, 1.5 * g],
  '4.992': [g / 3, 4 * g / 3, 2 * g], '4.993': [(g - 4) / 9, 2 * (g + (g - 4) / 9), 3 * (g - (g - 4) / 9)],
  '4.994': [1.5], '4.995': [540], '4.996': [250 * (g + 0.8)], '4.997': [0.2 * g],
  '4.998': [4 * g / 40, 18 * (g + 4 * g / 40)],
  '4.999': [(2 * g - 0.3 * 4 * g) / 6, 2 * (g - (2 * g - 0.3 * 4 * g) / 6)],
  '4.1000': [1.5 * 2.4 / (g - 2.4)], '4.1002': [(2 * g + 5 + 5 * 1.5) / (g - 1.5)],
  '4.1003': [(1.5 * g - 3) / 3.5, Math.sqrt(2 * ((1.5 * g - 3) / 3.5) * 0.6)], '4.1004': [18],
};

test('Alla 26 uppgifter finns i newton2 med eget delmoment', () => {
  assert.equal(Object.keys(Q).length, 26);
  for (const q of Object.values(Q)) {
    assert.equal(q.kap, 4, q.id);
    assert.equal(q.omr, 'newton2', q.id);
    assert.equal(q.familj, 'Kopplade klossar med snören och trissor', q.id);
    assert.equal(q.självrättning, true, q.id);
    assert.equal(q.miniräknare, true, q.id);
  }
});

test('Svaren stämmer med en oberoende omräkning (g = 9,82 m/s²)', () => {
  for (const [id, v] of Object.entries(VANTADE)) {
    const r = [].concat(Q[id].rättSvar);
    assert.equal(r.length, v.length, id);
    r.forEach((x, i) => assert.ok(Math.abs(x - v[i]) < 1e-9 * Math.max(1, Math.abs(v[i])), `${id} del ${i}: ${x} ≠ ${v[i]}`));
  }
  assert.deepEqual(Array.from(Q['4.1001'].rättSvar), ['g/2', '3*m*g/2']);
  assert.deepEqual(Array.from(Q['4.1001'].svarFormat), ['uttryck', 'uttryck']);
});

test('Häftets felaktiga facit är rättade', () => {
  // Det gamla facit: 3) S2 = 5,1 N, 4) a = 8,0, 5) a = 1,3, 7) a = 1,3, 14) S2 = 40 N, 15) a = 2,2 m/s².
  assert.ok(Math.abs(Q['4.981'].rättSvar[2] - 5.0) < 1e-9);
  assert.equal(Q['4.982'].rättSvar, 9);
  assert.ok(Math.abs(Q['4.983'].rättSvar[0] - 2.333) < 0.001);
  assert.ok(Math.abs(Q['4.985'].rättSvar[0] - 7.014) < 0.001);
  assert.ok(Math.abs(Q['4.992'].rättSvar[2] - 19.64) < 1e-9);
  assert.ok(Math.abs(Q['4.993'].rättSvar[0] - 0.6467) < 0.0001);
});

test('Nivåer: E, C och A finns, och varje delkort har nivå och träningsnivå', () => {
  const nivaer = new Set(Object.values(Q).map((q) => q.niva));
  assert.deepEqual([...nivaer].sort(), ['A', 'C', 'E']);
  const e12 = Object.values(Q).flatMap((q) => (q.spelDelar || [q]).filter((d) => d.traningsniva <= 2));
  assert.ok(e12.length >= 10, `nivå 1–2: ${e12.length}`);
  for (const q of Object.values(Q)) {
    for (const d of q.spelDelar || []) {
      assert.match(d.niva, /^[ECA]$/, q.id + d.etikett);
      assert.ok(d.traningsniva >= 1 && d.traningsniva <= 5, q.id + d.etikett);
    }
  }
});

test('Uppgifterna är fristående: massor och krafter står i texten, figur finns, g står inte i frågan', () => {
  for (const q of Object.values(Q)) {
    const t = text(q.t);
    assert.match(t, /mass(an|orna|a)|väger/, q.id);
    assert.match(q.t, /<svg/, q.id);
    assert.doesNotMatch(t, /9,82/, q.id);
    assert.doesNotMatch(t, /föregående|uppgiften ovan|samma som i uppgift|tidigare uppgift/i, q.id);
  }
});

test('Delkort börjar med samma inledning och figur och får accelerationen i frågan', () => {
  for (const q of Object.values(Q)) {
    if (!q.spelDelar) continue;
    assert.equal(q.spelDelning, 'deluppgifter', q.id);
    for (const [i, d] of q.spelDelar.entries()) {
      assert.ok(d.t.startsWith(q.spelIntro), q.id + d.etikett);
      if (i > 0 && q.id !== '4.1001') assert.match(text(d.t), /accelererar med \d+,\d{3,4} m\/s²/, q.id + d.etikett);
      assert.match(d.s, /facit-svar/, q.id + d.etikett);
      assert.doesNotMatch(d.s, /från a\)/, q.id + d.etikett);
    }
  }
});

test('Facit följer facitmallen: rubriker med Newtons andra lag och svarsrad', () => {
  for (const q of Object.values(Q)) {
    assert.match(q.s, /facit-stegvis/, q.id);
    assert.match(q.s, /class="facit-rubrik"/, q.id);
    assert.match(q.s, /F_\{\\text\{res\}\}=m/, q.id);
    assert.match(q.s, /<strong>Svar:<\/strong>/, q.id);
    assert.doesNotMatch(q.s, /None|null|undefined/, q.id);
  }
  // Svarsraden har två värdesiffror och stämmer med rättSvar.
  assert.match(Q['4.985'].s, /Svar:<\/strong> 7,0 m\/s²/);
  assert.match(Q['4.985'].s, /Svar:<\/strong> 17 N/);
  assert.match(Q['4.985'].s, /Svar:<\/strong> 11 N/);
  assert.match(Q['4.993'].s, /Svar:<\/strong> 0,65 m\/s²/);
});

test('Häftet finns med rättat facit', () => {
  const html = fs.readFileSync(path.join(ROT, 'material', 'fysik1', 'Fardighetstraning_Newtons_andra_lag.html'), 'utf8');
  assert.match(html, /Färdighetsträning – Newtons andra lag/);
  assert.equal((html.match(/class="kort"/g) || []).length, 15);
  for (const v of ['7{,}0\\ \\text{m/s}^2', '0{,}65\\ \\text{m/s}^2', '28\\ \\text{N}', '5{,}0\\ \\text{N}']) {
    assert.ok(html.includes(v), v);
  }
  assert.ok(fs.existsSync(path.join(ROT, 'material', 'fysik1', 'Fardighetstraning_Newtons_andra_lag.pdf')));
});
