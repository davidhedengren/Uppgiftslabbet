'use strict';
/* Ma1 kapitel 1 (algebra): mängdträning 2026-11-06, #1.1623–1.1674.
   Testet räknar om varje dels svar direkt ur den fråga eleven ser, oberoende av byggskriptet
   tools/bygg-ma1-kap1-mangdtraning-2026-11-06.py. Logg: agent/MA1_KAP1_MANGDTRANING_2026-11-06.md */
const test = require('node:test'), assert = require('node:assert/strict'), fs = require('node:fs'), path = require('node:path'), vm = require('node:vm');
const c = {window: {}}; vm.runInNewContext(fs.readFileSync(path.join(__dirname, '../uppgifterma1.js'), 'utf8'), c);
const byId = new Map(c.window.BANKMA1.map(u => [u.id, u]));
const NYA = Array.from({length: 52}, (_, i) => `1.${1623 + i}`);
const ren = h => h.replace(/<[^>]+>/g, ' ').replace(/\s+/g, ' ').trim();
const nara = (a, b) => Math.abs(a - b) <= 1e-9 * Math.max(1, Math.abs(b));

/* TeX/elevsvar → JavaScript-funktion av en bokstav. */
function js(tex) {
  let s = tex.replace(/\\d?frac\{([^{}]+)\}\{([^{}]+)\}/g, '(($1)/($2))').replace(/\{,\}/g, '.').replace(/\\cdot/g, '*')
    .replace(/\^\{?(\d+)\}?/g, '**$1').replace(/\s+/g, '');
  s = s.replace(/(\d|\))(?=[a-z(])/g, '$1*').replace(/([a-z])(?=[a-z(\d])/g, '$1*');
  assert.match(s, /^[-+*/().\da-z]+$/, tex);
  // -x**2 är inte giltig JS; minustecknet ligger utanför potensen, precis som i matematiken.
  return s.replace(/(^|[^\w)])-([a-z\d.]+\*\*\d+)/g, '$1-($2)');
}
const fn = (uttr, v) => Function(v, `return ${js(uttr)};`);

/* Lösningen till en linjär ekvation i v. */
function los(ekv, v) {
  const [vl, hl] = ekv.split('=');
  const f = t => fn(vl, v)(t) - fn(hl, v)(t);
  const k = f(1) - f(0);
  assert.ok(Math.abs(k) > 1e-12, ekv);
  const x = -f(0) / k;
  assert.ok(nara(f(x + 2), 2 * k), 'inte linjär: ' + ekv);
  return x;
}

function raknaDel(t) {
  const r = ren(t);
  let m;
  if ((m = r.match(/^Lös ekvationen\.? \\\((.+?)\\\)\.?$/))) {
    const v = (m[1].replace(/\\[a-z]+/g, '').match(/[a-z]/) || ['x'])[0];
    return {typ: 'tal', varde: los(m[1], v)};
  }
  if ((m = r.match(/^(?:Förenkla uttrycket|Multiplicera in och förenkla)\.? \\\((.+?)\\\)\.?$/))) {
    const v = (m[1].replace(/\\[a-z]+/g, '').match(/[a-z]/) || ['x'])[0];
    return {typ: 'polynom', fraga: m[1], v};
  }
  if ((m = r.match(/^Beräkna värdet av \\\((.+?)\\\) då (.+)\.$/))) {
    const varden = [...m[2].matchAll(/\\\(([a-z])=(-?[\d{},]+)\\\)/g)].map(x => [x[1], Number(x[2].replace('{,}', '.'))]);
    return {typ: 'tal', varde: Function(...varden.map(x => x[0]), `return ${js(m[1])};`)(...varden.map(x => x[1]))};
  }
  if ((m = r.match(/^Formeln \\\((\w)=(.+?)\\\) är given\. Beräkna \\\((\w)\\\) då (.+)\.$/))) {
    const [, subj, hl, okand, txt] = m;
    const givna = Object.fromEntries([...txt.matchAll(/\\\(([A-Za-z])=([\d{},]+)\\\)/g)].map(x => [x[1], Number(x[2].replace('{,}', '.'))]));
    const sattIn = (s) => s.replace(/[A-Za-z]/g, ch => ch in givna ? `(${givna[ch]})` : ch);
    if (okand === subj) return {typ: 'tal', varde: Function(`return ${js(sattIn(hl).replace(/[A-Z]/g, ''))};`)()};
    const ekv = `${subj in givna ? givna[subj] : subj}=${sattIn(hl)}`;
    return {typ: 'tal', varde: los(ekv.replace(new RegExp(okand, 'g'), 'q'), 'q')};
  }
  throw new Error('okänd fråga: ' + r);
}

function delfragor(u) {
  if (u.spelDelar) return u.spelDelar.map(d => d.t);
  return [u.t.replace(/^<p>(Formeln .*? är given\.)<\/p><p>/, '<p>$1 ')];
}

test('52 nya uppgifter i kapitel 1 med 1–4 delar', () => {
  const antal = {1: 0, 2: 0, 3: 0, 4: 0};
  for (const id of NYA) {
    const u = byId.get(id);
    assert.ok(u, id); assert.equal(u.kap, 1); assert.equal(u.miniräknare, false);
    antal[(u.spelDelar || [1]).length]++;
  }
  for (const n of [1, 2, 3, 4]) assert.ok(antal[n] >= 9, `${n} delar: ${antal[n]}`);
});

test('svaren stämmer med frågan, räknat oberoende av byggaren', () => {
  let n = 0;
  for (const id of NYA) {
    const u = byId.get(id);
    const svar = Array.isArray(u.rättSvar) ? u.rättSvar : [u.rättSvar];
    delfragor(u).forEach((t, i) => {
      n++;
      const r = raknaDel(t.replace(/^<p>(Formeln .*? är given\.)<\/p><p>/, '<p>$1 '));
      if (r.typ === 'tal') { assert.ok(nara(Number(svar[i]), r.varde), `${id} del ${i}: ${svar[i]} ≠ ${r.varde}`); return; }
      // Förenklat svar: samma värde som frågan för flera x, inga parenteser och högst en term per potens.
      const f = fn(r.fraga, r.v), g = fn(String(svar[i]), r.v);
      for (const x of [-3, -1, 0, 2, 5, 0.5]) assert.ok(nara(g(x), f(x)), `${id} del ${i}: ${svar[i]} vid ${x}`);
      assert.doesNotMatch(String(svar[i]), /[()]/, id);
      const pot = String(svar[i]).match(/[a-z](\^\d)?|(?<![\^\d])\d+(?![a-z\d^])/g).map(x => x.includes('^') ? x : /[a-z]/.test(x) ? '1' : '0');
      assert.equal(new Set(pot).size, pot.length, `${id}: ${svar[i]} är inte förenklat`);
    });
  }
  assert.equal(n, 120);
});

test('delarna blir svårare a → d, egen ledtråd och FACITMALL-facit med uppgiftens tal i rubrikerna', () => {
  for (const id of NYA) {
    const u = byId.get(id);
    if (u.spelDelar) {
      const niv = u.spelDelar.map(d => d.traningsniva);
      assert.ok(niv.every((x, i) => i === 0 || x >= niv[i - 1]), `${id}: ${niv}`);
      for (const d of u.spelDelar) { assert.match(d.s, /facit-steglista/); assert.match(d.s, /facit-svar/); assert.ok(d.ledtrad); }
    }
    for (const r of u.s.match(/<p class="facit-rubrik">.*?<\/p>/g)) assert.match(r, /\d|\\\(/, `${id}: ${r}`);
    assert.doesNotMatch(u.s, /Steg \d|(?<![\d,])0[a-z]|[+-]0(?![\d,.])|\\frac\{11\}\{2\}/, id);
  }
});

test('ekvationsfacit avslutas med kontroll där båda leden får samma värde', () => {
  for (const id of NYA.filter(i => /ekv|ekvationer/.test(byId.get(i).omr))) {
    for (const d of byId.get(id).spelDelar || [byId.get(id)]) {
      const vl = d.s.match(/\\text\{VL\}=[^\]]*?=?(-?[\d{},]+)\\\]/), hl = d.s.match(/\\text\{HL\}=[^\]]*?=?(-?[\d{},]+)\\\]/);
      assert.ok(vl && hl && vl[1] === hl[1], `${id}: kontroll saknas eller fel`);
    }
  }
});
