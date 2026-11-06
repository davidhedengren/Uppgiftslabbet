'use strict';
/* Ma1 kapitel 0: mängdträning och felrapport 2026-11-06 08:31 (0.02, 0.125, 0.62).
   Testet räknar om varje dels svar direkt ur den fråga eleven ser, oberoende av byggskriptet
   tools/bygg-ma1-kap0-mangdtraning-2026-11-06.py. Logg: agent/MA1_KAP0_MANGDTRANING_2026-11-06.md */
const test = require('node:test'), assert = require('node:assert/strict'), fs = require('node:fs'), path = require('node:path'), vm = require('node:vm');
const kod = fs.readFileSync(path.join(__dirname, '../uppgifterma1.js'), 'utf8');
const c = {window: {}}; vm.runInNewContext(kod, c);
const bank = c.window.BANKMA1, byId = new Map(bank.map(u => [u.id, u]));
const NYA = Array.from({length: 86}, (_, i) => `0.${1302 + i}`);

const ren = h => h.replace(/<[^>]+>/g, ' ').replace(/\s+/g, ' ').trim();
const tal = s => Number(s.replace(/\\ /g, '').replace(/\{,\}/g, '.').replace(/,/g, '.').replace(/−/g, '-'));
const bratal = v => typeof v === 'string' && v.includes('/') ? v.split('/').map(Number).reduce((a, b) => a / b) : v;
const nara = (a, b) => Math.abs(a - b) <= 1e-9 * Math.max(1, Math.abs(b));

function raknaUttryck(tex) {
  const js = tex.replace(/\\frac\{(\d+)\}\{(\d+)\}/g, '($1/$2)').replace(/\{,\}/g, '.').replace(/\\cdot/g, '*')
    .replace(/\\div/g, '/').replace(/\^\{?(\d+)\}?/g, '**$1').replace(/\\ /g, '').replace(/\s+/g, '');
  assert.match(js, /^[-+*/().\d]+$/, tex);
  // -6**2 är inte giltig JS; skriv det som -(6**2) precis som matematiken läser det.
  return Function(`return (${js.replace(/(^|[^\d)])-(\d+)\*\*(\d+)/g, '$1-($2**$3)')});`)();
}

const ENH = {m: 1, dm: .1, cm: .01, mm: .001, km: 1000, g: 1, kg: 1000, mg: .001, ton: 1e6, l: 1, dl: .1, cl: .01, ml: .001,
  'dm³': 1, 'cm³': .001, 'm³': 1000, 'm²': 1, 'dm²': .01, 'cm²': 1e-4, 'km²': 1e6, h: 3600, min: 60, s: 1};
const PREFIX = {k: 3, c: -2, m: -3, 'µ': -6, M: 6, G: 9};

/* Oberoende facit ur frågetexten. */
function raknaDel(fraga) {
  const f = ren(fraga);
  let m;
  if ((m = f.match(/Skriv \\\((.+?)\\ \\text\{(.+?)\}\\\) i (\S+?)\.$/))) {
    const [, v, fran, till] = m;
    if (ENH[fran] && ENH[till]) return tal(v) * ENH[fran] / ENH[till];
    const pre = fran.slice(0, -till.length);
    assert.ok(pre in PREFIX && fran.endsWith(till), fran);
    return tal(v) * 10 ** PREFIX[pre];
  }
  if ((m = f.match(/Beräkna \\\((.+?)\\,\\%\\\) av \\\((.+?)\\\)/))) return tal(m[1]) / 100 * tal(m[2]);
  if ((m = f.match(/Hur många procent är \\\((.+?)\\\) av \\\((.+?)\\\)/))) return tal(m[1]) / tal(m[2]) * 100;
  if ((m = f.match(/Skriv \\\((.+?)\\,\\%\\\) i decimalform/))) return tal(m[1]) / 100;
  if ((m = f.match(/Skriv \\\(([\d{},]+)\\\) i procent/))) return tal(m[1]) * 100;
  if ((m = f.match(/Skriv \\\((.+?)\\cdot 10\^\{(-?\d+)\}\\\) i decimalform/))) return tal(m[1]) * 10 ** Number(m[2]);
  if ((m = f.match(/Skriv \\\((.+?)\\\) i grundpotensform/))) return tal(m[1]);
  if ((m = f.match(/Förkorta \\\(\\frac\{(\d+)\}\{(\d+)\}\\\)/))) return Number(m[1]) / Number(m[2]);
  if ((m = f.match(/Avrunda \\\((.+?)\\\) till (.+?)\.$/))) {
    const steg = {'heltal': 0, 'en decimal': 1, 'två decimaler': 2, 'tre decimaler': 3, 'närmaste tiotal': -1, 'närmaste hundratal': -2, 'närmaste tusental': -3}[m[2]];
    const k = 10 ** steg;
    return Math.round(tal(m[1]) * k + 1e-9) / k;
  }
  m = f.match(/\\\((.+)\\\)/);
  assert.ok(m, 'ingen formel i ' + f);
  return raknaUttryck(m[1]);
}

test('86 nya mängdträningsuppgifter i kapitel 0 med 1–4 deluppgifter', () => {
  const antal = {1: 0, 2: 0, 3: 0, 4: 0};
  for (const id of NYA) {
    const u = byId.get(id);
    assert.ok(u, id);
    assert.equal(u.kap, 0); assert.equal(JSON.stringify(u.kurs), '["1a","1b","1c"]');
    assert.equal(u.miniräknare, false, id); assert.equal(u.geogebra, false, id);
    antal[(u.spelDelar || [1]).length]++;
  }
  for (const n of [1, 2, 3, 4]) assert.ok(antal[n] >= 15, `för få uppgifter med ${n} delar: ${antal[n]}`);
});

test('svaren stämmer med frågan, räknat oberoende av byggaren', () => {
  let n = 0;
  for (const id of NYA) {
    const u = byId.get(id);
    const delar = u.spelDelar ? u.spelDelar.map(d => d.t) : [u.t];
    const svar = Array.isArray(u.rättSvar) ? u.rättSvar : [u.rättSvar];
    assert.equal(svar.length, delar.length, id);
    delar.forEach((t, i) => { n++; assert.ok(nara(bratal(svar[i]), raknaDel(t)), `${id} del ${i}: ${svar[i]} ≠ ${raknaDel(t)}`); });
  }
  assert.equal(n, 208);
});

test('delarna blir svårare a → d och har egen träningsnivå, ledtråd och facit', () => {
  for (const id of [...NYA, '0.02']) {
    const u = byId.get(id);
    if (!u.spelDelar) { assert.ok(u.traningsniva >= 1, id); continue; }
    const nivaer = u.spelDelar.map(d => d.traningsniva);
    assert.ok(nivaer.every(x => Number.isInteger(x) && x >= 1), id);
    assert.ok(nivaer.every((x, i) => i === 0 || x >= nivaer[i - 1]), `${id}: ${nivaer}`);
    assert.equal(u.traningsniva, Math.max(...nivaer), id);
    for (const d of u.spelDelar) {
      assert.match(d.s, /facit-steglista/); assert.match(d.s, /facit-rubrik/); assert.match(d.s, /facit-svar/);
      assert.ok(d.ledtrad && !/Steg \d/.test(d.s), id);
    }
  }
});

test('facitrubrikerna visar uppgiftens egna tal', () => {
  for (const id of NYA) {
    const u = byId.get(id);
    for (const r of u.s.match(/<p class="facit-rubrik">.*?<\/p>/g)) assert.match(r, /\d/, `${id}: ${r}`);
  }
});

test('felrapport 0.125: inget "strikt" i Ma1-banken, "mellan" i fetstil i frågan', () => {
  assert.doesNotMatch(kod, /strikt/i);
  assert.match(byId.get('0.125').t, /ligger <strong>mellan<\/strong> −4 och 3/);
  assert.match(byId.get('0.125').s, /”Mellan” betyder att ändpunkterna inte räknas/);
  assert.match(byId.get('0.76').t, /<strong>mellan<\/strong>/);
});

test('felrapport 0.62: eleven skriver −7·(−5), utan parentes runt −4−3', () => {
  const t = byId.get('0.62').t;
  assert.ok(t.includes('och skriver \\(-7\\cdot(-5)=35\\)'), t);
  assert.ok(!t.includes('(-4-3)'));
});

test('felrapport 0.02: fyra deluppgifter med stigande svårighet', () => {
  const u = byId.get('0.02');
  assert.equal(JSON.stringify(u.rättSvar), '[-3,1,2,-2]');
  assert.equal(u.spelDelar.map(d => d.traningsniva).join(), '1,2,2,3');
  assert.equal(u.poang, '4/0/0');
  u.spelDelar.forEach((d, i) => assert.ok(nara(u.rättSvar[i], raknaDel(d.t)), d.t));
});
