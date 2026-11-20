'use strict';
const test = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');
const context = { window: {} };
vm.runInNewContext(fs.readFileSync(path.join(__dirname, '../uppgiftermato1.js'), 'utf8'), context);
const tasks = new Map(JSON.parse(JSON.stringify(context.window.BANKMATO1)).map(t => [t.id, t]));
const task = n => tasks.get('1.' + n);
const answer = n => task(n).rättSvar;

test('direkt numerisk insättning ligger på nivå 1 även på de enskilda träningskorten', () => {
  for (const n of [12, 17, 22, 165, 167, 169, 546, 552, 559]) {
    for (const q of [task(n), ...(task(n).spelDelar || [])]) {
      assert.equal(q.traningsniva, 1);
      assert.equal(q.niva, 'E');
    }
  }
});

test('uttrycken stämmer även vid negativa steg och negativa startvärden', () => {
  // Utvärdera enbart de lagrade polynomsvaren i denna avgränsade serie.
  function expression(n, args) {
    const src = answer(n).replace(/(\d)(?=[axh])/g, '$1*').replaceAll('^', '**');
    assert.match(src, /^[\daxh*/+.\s-]+$/);
    return vm.runInNewContext(src, args);
  }
  const f = x => 2*x*x-3*x+5;
  const g = x => 5-3*x;
  const p = x => x*x+x-2;
  const k = x => x*x-4*x+1;
  for (const a of [-2, 0, 1.25, 3]) {
    for (const h of [-2, -.5, .25, 3]) {
      assert.equal(expression(1101, {a}), g(2*a)-g(a+1));
      assert.equal(expression(1102, {h}), p(2-h)-p(2));
      assert.equal(expression(1103, {h}), (k(3+h)-k(3))/h || 0);
      assert.equal(expression(1104, {a,h}), (f(a+h)-f(a))/h || 0);
      const recovered = x => expression(1110, {x});
      assert.equal(recovered(1), 2);
      assert.equal((recovered(a+h)-recovered(a))/h || 0, 6*a+3*h-4);
      if (h > 0) {
        const left = expression(1108,{h}), curve = x => x*x-6*x+2;
        assert.equal(curve(left), curve(left+h));
      }
    }
  }
});

test('tabell, grafer, sekantlutning och gränsvärdesfråga', () => {
  const pairs = [[-2,8],[3,-1],[5,5]];
  assert.deepEqual(pairs.filter(([h,y]) => (y-2)/h===-1).map(([h])=>h), [answer(1105)]);
  const f = x => x*x-x-1, g = x => x+2;
  assert.deepEqual(answer(1106), [-1,3]);
  for (const x of answer(1106)) assert.equal(f(x),g(x));
  assert.equal(task(1106).svarsstruktur,'mängd');
  const shifted = x => answer(1107)-((x-1)**2-2);
  assert.deepEqual([-1,1,3].map(shifted),[1,5,1]);
  const curve = x => 12-3*x-x*x, end = answer(1111);
  assert.notEqual(end,2);
  assert.equal((curve(end)-curve(2))/(end-2),-9);
  assert.equal(task(1109).visaAlternativ,true);
  assert.deepEqual(task(1109).alternativ.filter(a=>a.ratt).map(a=>a.txt),['Kvoten saknar värde vid h = 0 men närmar sig 7 när h närmar sig noll.']);
  assert.equal(task(1112).självrättning,false);
  assert.match(task(1112).s,/g\(x\)-f\(x\)=g\(0\)-f\(0\)=3/);
});

test('de pausade uppgifterna finns kvar på lärarbladet och de nya funktionssambanden är spelbara', () => {
  for (const n of ['07',77,430,434,453,461,545,546,551,552,951,955,956,961,962,964]) {
    assert.equal(task(n).spel,false,String(n));
    assert.ok(task(n).t && task(n).s);
  }
  assert.ok(task(1105).spel);
  assert.ok(task(1113).spel && task(1114).spel);
  const x = -3/2, f = t => t*t-4*t;
  assert.equal(f(x+3),f(-x));
  assert.equal(answer(1113),'-3/2');
  assert.equal(answer(1114),[-1,1,3].reduce((y,a)=>y+2*a+1,4));
});
