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
