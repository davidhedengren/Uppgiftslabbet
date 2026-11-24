'use strict';
const {test} = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');

function read(file) {
  return fs.readFileSync(path.join(__dirname, '..', file), 'utf8');
}

function functionsBetween(file, start, end) {
  const source = read(file);
  const first = source.indexOf(start), last = source.indexOf(end, first);
  assert.ok(first >= 0 && last > first);
  return source.slice(first, last);
}

test('En elev kan få alla matematikpoäng och noll för kommunikation', () => {
  const context = vm.createContext({window:{}});
  vm.runInContext(read('uppgifterma2.js'), context);
  vm.runInContext(functionsBetween('index.html', 'function analysNiva(', 'async function analyseraSparatDokument('), context);
  const q = context.window.BANKMA2.find(x => x.id === '3.438');
  assert.equal(q.poang, '0/1/4');
  assert.equal(q.spel, false);
  assert.match(q.s, /Kommunikation \(1 A-poäng\)/);
  const [task] = context.byggAnalysOverforing({blad:[q],omr:{},kurs:{id:'ma2'},spår:null,klass:'',titel:''}).data.tasks;
  assert.equal(task.parts.length, 2);
  const [math, communication] = task.parts;
  assert.equal(math.max, 4);
  assert.equal(communication.max, 1);
  vm.runInContext(functionsBetween('analys/index.html', 'function num(', 'function fmt(')
    + functionsBetween('analys/index.html', 'const ABILITY_LABELS=', 'function usedFamilies('), context);
  const student = {scores:{[math.id]:4, [communication.id]:0}};
  assert.equal(context.abilityPoints(task,'kommunikation'), 1);
  assert.equal(context.abilityPoints(task,'kommunikation',student), 0);
  assert.equal(context.abilityPoints(task,'resonemang',student), 2);
  assert.equal(context.abilityPoints(task,'begrepp',student), 2);
});

test('K-poängen anges i facit och tillhör en skriftlig läraruppgift på C- eller A-nivå', () => {
  for (const file of ['ma1','ma2','mato1','mato2','matf1']) {
    const context = {window:{}};
    vm.runInNewContext(read('uppgifter'+file+'.js'), context);
    for (const task of Object.values(context.window)[0]) {
      assert.ok(!task.formaga.includes('problemlosning'), file+' '+task.id);
      if (!task.formaga.includes('kommunikation')) continue;
      assert.ok(['C','A'].includes(task.niva));
      assert.ok(task.s.includes('Kommunikation (1 '+task.niva+'-poäng)'));
      assert.ok(!(task.spel && task.självrättning && !task.spelDelar?.length));
    }
  }
});
