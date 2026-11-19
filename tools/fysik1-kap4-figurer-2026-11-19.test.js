'use strict';
// Fy1 kapitel 4: figurer i uppgifter som saknade figur (agent/FY1_KAP4_FIGURER_2026-11-19.md).
const test = require('node:test');
const assert = require('node:assert/strict');
const fs = require('fs');
const vm = require('vm');
const path = require('path');

const c = { window: {} };
vm.runInNewContext(fs.readFileSync(path.join(__dirname, '..', 'uppgifter.js'), 'utf8'), c);
const q = (id) => c.window.BANK.find((t) => t.id === id);
// id -> delkort som får figuren (null = alla)
const FIGURER = {
  // Newtons tredje lag
  '4.463': null, '4.464': null, '4.465': null, '4.496': null, '4.501': null, '4.896': null, '4.894': null,
  // normalkraft
  '4.477': null, '4.478': null, '4.502': null, '4.207': ['a'], '4.217': null, '4.646': null, '4.642': null, '4.816': null,
  // gravitation och tyngdkraft
  '4.74': ['b', 'c'], '4.354': null, '4.379': null, '4.753': null, '4.738': null, '4.739': null, '4.188': null,
  '4.474': null, '4.498': null, '4.887': null,
};

test('kapitel 4: figuren finns i frågan och på rätt delkort', () => {
  for (const [id, kort] of Object.entries(FIGURER)) {
    const t = q(id);
    assert.equal((t.t.match(/<svg/g) || []).length, 1, id);
    const fig = t.t.match(/<span class="fig">[\s\S]*?<\/svg><\/span>/)[0];
    assert.match(fig, /role="img" aria-label="[^"]{20,}"/, id);
    assert.match(fig, /<rect width="\d+" height="\d+" fill="#fff"\/>/, `${id}: vit bakgrund`);
    assert.doesNotMatch(fig, /positiv/i, id);
    if (t.spelIntro && kort === null) assert.ok(t.spelIntro.includes(fig), `${id}: spelIntro`);
    for (const d of t.spelDelar || []) assert.equal(d.t.includes(fig), kort === null || kort.includes(d.etikett), `${id}${d.etikett}`);
  }
});

test('kraftfigurerna visar de givna krafterna men inte de sökta', () => {
  for (const [id, tal] of [['4.463', ['50 kg', '75 kg']], ['4.464', ['45 N', '15 kg']], ['4.496', ['20 N', '4,0 kg', '6,0 kg']],
    ['4.501', ['a = 0,50 m/s²', 'koppling ?']], ['4.896', ['90 N', '10 kg', '20 kg']], ['4.477', ['40 N', '10 kg']],
    ['4.502', ['80 N', '30°']], ['4.207', ['423 g', '257 g', 'visar ?']], ['4.217', ['75 kg', 'a = ?']], ['4.642', ['1,8 m']]]) {
    for (const s of tal) assert.ok(q(id).t.includes(`>${s}<`), `${id}: ${s}`);
  }
  // Normalkraft, kopplingskraft och spännkraft (svaren) är inte utritade.
  for (const id of ['4.477', '4.478', '4.502', '4.816']) assert.doesNotMatch(q(id).t.match(/<svg[\s\S]*?<\/svg>/)[0], />N</, id);
  assert.doesNotMatch(q('4.501').t, />40 kN|>20 kN/); assert.doesNotMatch(q('4.896').t, />30 N</);
});

test('gravitation och tyngdkraft: givna avstånd och mätvärden står i figuren, det sökta är markerat med ?', () => {
  for (const [id, tal] of [['4.74', ['R = 6371 km', '400 km']], ['4.379', ['85 000 km', 'x = ?']], ['4.753', ['2,00 m', 'sten 50 kg']], ['4.738', ['12 cm']],
    ['4.739', ['6 378 km', '6 357 km']], ['4.188', ['200 m mellan masscentrum']], ['4.474', ['visar 14,8 N']], ['4.498', ['på jorden: 4,90 N', 'på månen: ?', 'massa ?']],
    ['4.887', ['12,0 N', '2,03 N']]]) {
    for (const s of tal) assert.ok(q(id).t.includes(`>${s}<`), `${id}: ${s}`);
  }
  assert.doesNotMatch(q('4.74').t, />6771/); assert.doesNotMatch(q('4.379').t, />54/); assert.doesNotMatch(q('4.498').t, />0,808|>0,499/);
});
