'use strict';
const { test } = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');
function bank(file, name) {
  const context = { window: {} };
  vm.runInNewContext(fs.readFileSync(path.join(__dirname, '..', file), 'utf8'), context);
  return new Map(context.window[name].map(q => [q.id, q]));
}
const fy = bank('uppgifter.js', 'BANK');
const mat = bank('uppgiftermatf1.js', 'BANKMATF1');
const number = v => typeof v === 'string' && v.includes('/')
  ? v.split('/').map(Number).reduce((a, b) => a / b) : Number(v);
function close(actual, expected) {
  assert.ok(Math.abs(number(actual) - expected) <= Math.max(1e-9, Math.abs(expected) * 1e-12), `${actual} ≠ ${expected}`);
}
function subsets(n, k, visit, selected = [], start = 0) {
  if (selected.length === k) { visit(selected); return; }
  for (let i = start; i <= n - (k - selected.length); i++) subsets(n, k, visit, [...selected, i], i + 1);
}
test('Bromsande arbete är ändringen i mekanisk energi, med negativt tecken', () => {
  const states = [
    [fy.get('5.493').rättSvar[0], 55, 20, 12, 5],
    [fy.get('5.494').rättSvar, 0.075, 40, 30, 20 - 1.2]
  ];
  for (const [answer, mass, before, after, rise] of states) {
    const initial = mass * before ** 2 / 2;
    const final = mass * after ** 2 / 2 + mass * 9.82 * rise;
    close(answer, final - initial); assert.ok(answer < 0);
  }
});
test('Delkort använder sina egna givna mellanresultat', () => {
  close(fy.get('5.495').rättSvar[2] * 500, 300000);
  close(fy.get('5.511').rättSvar[1] * 1200, 164e6);
  close(fy.get('5.511').rättSvar[2] * 2 * 117000, 164e6);
  close(fy.get('6.422').rättSvar[1] * 9.82, 300000);
  close(fy.get('6.455').rättSvar[1] * 0.8 * 9.82, 28000);
  close(fy.get('6.458').rättSvar[2] * 1300 * 9.82, 1020);
});
test('Vindkraftssvaret är ett helt antal som räcker, medan ett verk färre inte räcker', () => {
  const q = fy.get('5.591'), count = q.rättSvar[1], annual = 3000 * 0.9 * 8760;
  assert.ok(Number.isInteger(count));
  assert.ok(count * annual >= 63e9);
  assert.ok((count - 1) * annual < 63e9);
  assert.equal(q.tolerans[1], 0);
});
test('Två onamngivna lag med skilda bästa spelare räknas en gång', () => {
  const divisions = new Set();
  subsets(10, 5, team => {
    const other = Array.from({ length: 10 }, (_, i) => i).filter(i => !team.includes(i));
    if (team.includes(0) === team.includes(1)) return;
    divisions.add([team.join(','), other.join(',')].sort().join('|'));
  });
  close(mat.get('1.657').rättSvar[2], divisions.size);
});
test('Sannolikheter för minst ett visst antal räknas med fullständig uppräkning', () => {
  for (const [id, total, special, drawn, minimum] of [
    ['1.435', 12, 5, 4, 2], ['1.448', 22, 5, 6, 3]
  ]) {
    let possible = 0, favourable = 0;
    subsets(total, drawn, group => {
      possible++;
      if (group.filter(i => i < special).length >= minimum) favourable++;
    });
    close(mat.get(id).rättSvar, favourable / possible);
  }
});
test('Fördelningar med olika minimikrav stämmer med uppräknade lådinnehåll', () => {
  let count = 0;
  for (let a = 2; a <= 20; a++) for (let b = 3; b <= 20 - a; b++)
    for (let c = 1; c <= 20 - a - b; c++) if (20 - a - b - c >= 2) count++;
  close(mat.get('1.466').rättSvar, count);
});
test('Förenklade binomialfacit ger samma värde som ursprungsuttrycken', () => {
  for (const [id, a, b, n] of [
    ['1.533', 1, 1, 2], ['1.534', 1, 2, 2], ['1.535', 1, 1, 3],
    ['1.538', 2, 1, 3], ['1.540', 3, -1, 3], ['1.543', 2, 1, 4],
    ['1.545', 2, -1, 3], ['1.547', 2, -1, 3]
  ]) {
    const expression = mat.get(id).rättSvar.replace(/\^/g, '**');
    assert.match(expression, /^[0-9x\s+*.-]+$/);
    for (const x of [-3, -1, 0, 2, 4]) {
      const actual = vm.runInNewContext(expression, { x });
      close(actual, (a * x + b) ** n);
    }
  }
});
