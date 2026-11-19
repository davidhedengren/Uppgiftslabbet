'use strict';
// Fy1 kapitel 3: figurer i uppgifter som saknade figur (agent/FY1_KAP3_FIGURER_2026-11-19.md).
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
  '3.213': null, '3.214': null, '3.215': null, '3.216': null, '3.217': null, '3.218': [], '3.223': null, '3.226': null,
  '3.210': null, '3.360': null, '3.203': null,
  // konstacc
  '3.30': null, '3.63': null, '3.68': null, '3.86': null, '3.118': null, '3.124': null, '3.162': null, '3.170': null, '3.172': null,
  '3.177': null, '3.378': null, '3.379': null, '3.391': null, '3.400': null, '3.406': null, '3.387': ['b', 'c'],
  // vektorer (hastighet som vektor)
  '3.638': null, '3.711': null, '3.713': null, '3.677': null, '3.689': null, '3.723': null, '3.732': null, '3.656': null, '3.730': null,
  '3.705': null, '3.676': null, '3.7': null, '3.52': null, '3.82': ['b', 'c'], '3.95': null,
};

test('kapitel 3: figuren finns i frågan och på rätt delkort', () => {
  for (const [id, kort] of Object.entries(FIGURER)) {
    const t = q(id);
    assert.equal((t.t.match(/<svg/g) || []).length, 1, id);
    const fig = t.t.match(/<span class="fig">[\s\S]*?<\/svg><\/span>/)[0];
    assert.match(fig, /role="img" aria-label="[^"]{20,}"/, id);
    assert.match(fig, /<rect width="\d+" height="\d+" fill="#fff"\/>/, `${id}: vit bakgrund`);
    // Riktningsval står bara i kgInstruktion, aldrig i figuren.
    assert.doesNotMatch(fig, /positiv/i, id);
    if (t.spelIntro && kort === null) assert.ok(t.spelIntro.includes(fig), `${id}: spelIntro`);
    for (const d of t.spelDelar || []) assert.equal(d.t.includes(fig), kort === null || kort.includes(d.etikett), `${id}${d.etikett}`);
  }
});

test('acceleration: figurerna visar givna hastigheter och avslöjar inga svar', () => {
  for (const [id, tal] of [['3.214', ['15,0 m/s', '2,60 m/s']], ['3.215', ['5,4 m/s', '3,8 m/s']], ['3.216', ['in: 30 m/s', 'ut: 30 m/s']],
    ['3.217', ['57 m/s', '44 m/s', '46 m/s']], ['3.218', ['+6,75 m/s', '+5,60 m/s']], ['3.223', ['+12 m/s', '−12 m/s']],
    ['3.210', ['v₀ = 4,50 m/s']], ['3.360', ['B: 20 m/s', 'ikapp ?']], ['3.203', ['vₓ = +20,9 km/s', 'vₓ = −18,5 km/s']]]) {
    for (const s of tal) assert.ok(q(id).t.includes(`>${s}<`), `${id}: ${s}`);
  }
  assert.doesNotMatch(q('3.360').t, />17,8|>396/); assert.doesNotMatch(q('3.214').t, />0,13/);
});

test('konstacc: figurerna visar givna data och markerar det okända med ?', () => {
  for (const [id, tal] of [['3.30', ['8,0 m/s', '22 m']], ['3.63', ['9,0 m/s', 'stoppsträcka ?']], ['3.118', ['9,0 m/s', '1,5 m', 'högsta punkt ?']],
    ['3.162', ['18 cm', 'reaktionstid ?']], ['3.170', ['18 m/s', '45 m', 'möts ?']], ['3.172', ['80 km/h', '60 m']], ['3.177', ['30 m', '6,0 m/s', 'jämsides ?']],
    ['3.378', ['50 km/h', '35 m']], ['3.379', ['2,52 m/s', '4,80 m']], ['3.391', ['16,0 m']], ['3.400', ['35 m/s', '7,0 m']], ['3.387', ['476 m', '855 m', '24 m/s', '10 m/s']]]) {
    for (const s of tal) assert.ok(q(id).t.includes(`>${s}<`), `${id}: ${s}`);
  }
  // 3.400: figuren står efter situationen, inte efter förbehållet.
  assert.ok(q('3.400').t.indexOf('<svg') > q('3.400').t.indexOf('landar på marken.'));
  assert.ok(q('3.387').t.indexOf('<svg') > q('3.387').t.indexOf('45 s efter B.'));
  assert.doesNotMatch(q('3.177').t, />11,5|>11,48/);
});

test('vektorer: vinklar och väderstreck står i figuren, men inte komposanterna', () => {
  for (const [id, tal] of [['3.638', ['30°', '15 m/s', 'väster', 'söder']], ['3.711', ['40°', '12 km/h']], ['3.713', ['15°', '6,0 m/s']], ['3.677', ['45°', '15 m/s']],
    ['3.689', ['30°', 'ström 2,0 m/s']], ['3.723', ['avvikelse ?']], ['3.656', ['400 m österut', '300 m', '60°', '?']], ['3.730', ['3,0 km', '2,0 km', '4,0 km mot sydväst', '?']],
    ['3.705', ['12°', '45 m/s']], ['3.676', ['6°', '240 m/s']], ['3.52', ['6,0 m']], ['3.95', ['60 km', 'flugan 120 km/h']]]) {
    for (const s of tal) assert.ok(q(id).t.includes(`>${s}<`), `${id}: ${s}`);
  }
  // Svaren (komposanter, avstånd) syns inte.
  assert.doesNotMatch(q('3.638').t, />−13|>−7,5/); assert.doesNotMatch(q('3.656').t, />608/); assert.doesNotMatch(q('3.723').t, />16,7/);
  assert.doesNotMatch(q('3.95').t, />40 km</);
});
