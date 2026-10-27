const assert = require('node:assert/strict');
const fs = require('node:fs');
const source = fs.readFileSync('uppgiftermato2.js', 'utf8');
const bank = JSON.parse(source.slice(source.indexOf('['), source.lastIndexOf(']') + 1));
const task = bank.find(q => q.id === '4.322');
assert.equal(task.traningsniva, 5);
assert.equal(task.miniräknare, true);
assert.equal(task.geogebra, true);
assert.equal(task.självrättning, false);
assert(!task.s.includes('startvärde och förändringsfaktor'));
const distances = Array.from({length: 12}, (_, i) => {
  const n = i + 1, r = 1.1 ** n, a = 0.7 * n;
  return Math.hypot(r * Math.cos(a) + 2, r * Math.sin(a) - 1);
});
assert.equal(distances.indexOf(Math.min(...distances)) + 1, 4);
assert(Math.abs(distances[3] - 0.8029) < 0.0001);
assert(distances.every((v, i) => i === 3 || v > distances[3]));
console.log('4.322: nivå, verktyg och samtliga tolv avstånd kontrollerade');
