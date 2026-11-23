'use strict';
const test = require('node:test');
const assert = require('node:assert/strict');
const { readFileSync } = require('node:fs');
const { join } = require('node:path');
const vm = require('node:vm');

const context = { window: {} };
vm.runInNewContext(readFileSync(join(__dirname, '../uppgifter.js'), 'utf8'), context);
const bank = context.window.BANK;
const task = id => bank.find(q => q.id === id);
const near = (a, b) => assert.ok(Math.abs(a - b) < 1e-8, `${a} ≠ ${b}`);

test('sex separata A-problem med varsitt numeriskt svar och en figur', () => {
  for (const id of ['2.377', '2.378', '2.379', '2.380', '3.748', '3.749']) {
    const q = task(id);
    assert.equal(q.niva, 'A', id);
    assert.equal(q.traningsniva, 5, id);
    assert.equal(q.miniräknare, true, id);
    assert.equal(q.geogebra, false, id);
    assert.equal(q.spel && q.självrättning, true, id);
    assert.equal(q.svarstyp, 'numeriskt', id);
    assert.match(q.t, /<svg[^>]+aria-label=/, id);
    assert.match(q.s, /class="facit-steglista"/, id);
    assert.match(q.s, /class="facit-svar"/, id);
    assert.ok(q.ledtrad && q.svarEnhet, id);
  }
});

test('densitet: slutna porer, båda mineralproverna och pontonens massbalans', () => {
  const closed = task('2.377').rättSvar / 100 * 125;
  near(216 / 2.70 + (244 - 216) / 1.00 + closed, 125);
  const light = task('2.378').rättSvar;
  const dark = 90 / (45 - 30 / light);
  near(30 / dark + 90 / light, 55);
  const load = task('2.379').rättSvar;
  const dryMass = 1000 * 0.960 * 0.180;
  const floodedMass = 1000 * 0.240 * (0.350 - 0.040);
  near(dryMass + floodedMass + load, 1000 * 0.960 * 0.350);
});

test('rörelse: mötestider, fyra givarpassager och vagnens vändpunkter', () => {
  const drop = task('2.380').rättSvar;
  // Under returen närmar sig bussen och B varandra med 42 km/h.
  const returnTime = (drop - 6 * drop / 36) / (36 + 6);
  const meet = drop - 36 * returnTime;
  near(drop / 36 + (18 - drop) / 6, meet / 6 + (18 - meet) / 36);

  // Kontrollera att front och bakände verkligen passerar samma två punkter.
  const length = task('3.748').rättSvar;
  const front = t => 11.6 * t + 0.4 * t * t;
  near(front(0), 0);
  near(front(4) - length, 0);
  near(front(6), 84);
  near(front(9) - length, 84);

  // Signerade triangel- och rektangelareor på båda sidor om v = 0.
  const forwards = 0.5 * 1.5 * 3 + 2 * 3 + 0.5 * 0.75 * 3;
  const backwards = 0.5 * 2.5 * 5 + 0.5 * 1.25 * 5;
  near(forwards - backwards, 0);
  near(forwards + backwards, task('3.749').rättSvar);
});
