'use strict';
// Fy1 kapitel 2: figurer i uppgifter som saknade figur (agent/FY1_KAP2_FIGURER_2026-11-18.md).
const test = require('node:test');
const assert = require('node:assert/strict');
const fs = require('fs');
const vm = require('vm');
const path = require('path');

const c = { window: {} };
vm.runInNewContext(fs.readFileSync(path.join(__dirname, '..', 'uppgifter.js'), 'utf8'), c);
const q = (id) => c.window.BANK.find((t) => t.id === id);
const DENSITET = ['2.37', '2.77', '2.86', '2.87', '2.114', '2.144', '2.151', '2.162', '2.163', '2.165', '2.166', '2.167', '2.168', '2.179',
  '2.180', '2.181', '2.182', '2.188', '2.190', '2.192', '2.196', '2.203', '2.275', '2.277', '2.285', '2.289', '2.290'];

const MATNOGG = ['2.234', '2.15', '2.243', '2.245', '2.251', '2.255', '2.258', '2.269', '2.49', '2.45', '2.271'];
const MEDEL = ['3.9', '3.51', '3.97', '3.125', '3.130', '3.133', '3.234', '3.103', '3.236', '3.235', '3.101', '2.296', '2.304', '2.313', '2.320'];

test('kapitel 2: figuren finns i frågan, i inledningen och på varje delkort', () => {
  for (const id of [...DENSITET, ...MEDEL, ...MATNOGG]) {
    const t = q(id);
    assert.equal((t.t.match(/<svg/g) || []).length, 1, id);
    const fig = t.t.match(/<span class="fig">[\s\S]*?<\/svg><\/span>/)[0];
    assert.match(fig, /role="img" aria-label="[^"]{20,}"/, id);
    assert.match(fig, /<rect width="\d+" height="\d+" fill="#fff"\/>/, `${id}: vit bakgrund`);
    if (t.spelIntro) assert.ok(t.spelIntro.includes(fig), `${id}: spelIntro`);
    for (const d of t.spelDelar || []) assert.ok(d.t.includes(fig), `${id}${d.etikett}`);
  }
});

test('densitet: figurerna avslöjar inte sökta storheter', () => {
  // Okända storheter är markerade med ?, inte med sitt värde.
  for (const id of ['2.192', '2.275', '2.290']) assert.match(q(id).t, /\?<\/text>/, id);
  assert.doesNotMatch(q('2.192').t, /5,66|5,7 cm/);
  assert.doesNotMatch(q('2.275').t, /2,2 cm|2,20 cm/);
  assert.doesNotMatch(q('2.290').t, /9,6 cm|9,56/);
  assert.match(q('2.196').t, />\? ml</);
  // Givna värden i figuren stämmer med texten.
  for (const [id, tal] of [['2.165', ['78,0 ml', '83,0 ml']], ['2.285', ['40 ml', '60 ml']], ['2.188', ['87 ml', '13 ml', '132,4 g', '49,6 g']],
    ['2.190', ['35,00 g', '98,44 g', '89,22 g']], ['2.180', ['5,0 cm', 'Ø 2,0 cm']], ['2.181', ['2,0 cm', '1,0 cm']],
    ['2.179', ['3,50 cm', '2,50 cm', '1,50 m']], ['2.203', ['0,30 m', '0,40 m', 'Ø 2,0 cm']]]) {
    for (const s of tal) assert.ok(q(id).t.includes(`>${s}<`), `${id}: ${s}`);
  }
});

test('medelhastighet: figurerna visar de givna värdena och markerar det okända med ?', () => {
  for (const [id, tal] of [['3.51', ['32 m österut', '14 m västerut']], ['3.130', ['85 m']], ['3.133', ['4,20 s', '2,70 s', '3,80 s']],
    ['3.236', ['90 km i 90 km/h', '90 km i ? km/h', 'stopp 12 min']], ['3.235', ['50 km/h', '80 km/h', 'v = ?']], ['2.296', ['avstånd ?']],
    ['3.103', ['avstånd ?']], ['2.313', ['4,0 m/s', '3,1 m/s', '3,6 m/s', '3,9 m/s']], ['3.101', ['6371 km', '700 km', '7,5 km/s']]]) {
    for (const s of tal) assert.ok(q(id).t.includes(`>${s}<`), `${id}: ${s}`);
  }
  // Svaret på 3.51 b (förflyttningen 18 m) och 2.296 (3,0 km) syns inte i figuren.
  assert.doesNotMatch(q('3.51').t, />18 m</); assert.doesNotMatch(q('2.296').t, />3,0 km</);
});

test('mätnoggrannhet: figurerna visar mätvärdena utan att avslöja svaren', () => {
  for (const [id, tal] of [['2.234', ['83,42 g']], ['2.245', ['72,40 kg']], ['2.243', ['14,8 s', '10 svängningar']], ['2.251', ['1,4 m', '8,62 m', 'avstånd ?']],
    ['2.258', ['visar 0,8 °C', 'visar 100,6 °C', 'visar 50,7 °C', 'verklig temperatur ?']], ['2.269', ['40 varv', '12,6 ± 0,1 mm']],
    ['2.49', ['312 g', '309 g']], ['2.45', ['omkrets 1,45 ± 0,02 m', 'längd 12,0 ± 0,3 m']], ['2.15', ['0,10 ± 0,02 mm', '52 ± 1 mm']]]) {
    for (const s of tal) assert.ok(q(id).t.includes(`>${s}<`), `${id}: ${s}`);
  }
  assert.doesNotMatch(q('2.243').t, />1,48/); assert.doesNotMatch(q('2.245').t, />72,20/); assert.doesNotMatch(q('2.269').t, />0,315/);
});

test('enheter: figur i frågan, och på delkort bara när kortet har samma data', () => {
  const KORT = { '2.11': [], '2.12': ['a'], '2.35': [], '2.223': null, '2.363': null };
  for (const [id, kort] of Object.entries(KORT)) {
    const t = q(id);
    assert.equal((t.t.match(/<svg/g) || []).length, 1, id);
    for (const d of t.spelDelar || []) assert.equal(/<svg/.test(d.t), kort === null || kort.includes(d.etikett), `${id}${d.etikett}`);
  }
  assert.ok(q('2.11').t.includes('>avstånd ?<')); assert.ok(q('2.223').t.includes('>? µm<')); assert.ok(q('2.363').t.includes('>antal korn ?<'));
  assert.doesNotMatch(q('2.223').t, />3,92/);
});
