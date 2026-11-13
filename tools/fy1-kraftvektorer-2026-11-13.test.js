'use strict';
// Fy1, kapitel 4: nytt område "Vektorer" (kraftvektorer) 2026-11-13.
// Kontrollerar de 48 nya uppgifterna (4.913–4.960) från övningsbladen om resulterande kraft
// samt flytten av vektordelmomenten från newton1. Se agent/FY1_KRAFTVEKTORER_2026-11-13.md.
const test = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');

const rot = path.resolve(__dirname, '..');
const ctx = { window: {} };
vm.createContext(ctx);
for (const f of ['struktur.js', 'uppgifter.js']) vm.runInContext(fs.readFileSync(path.join(rot, f), 'utf8'), ctx);
const B = ctx.window.BANK;
const q = (id) => B.find((t) => t.id === id);
const NYA = [];
for (let n = 913; n <= 960; n++) NYA.push(`4.${n}`);

const SUB = { '₁': 0, '₂': 1, '₃': 2, '₄': 3 };
function krafterUrFigur(t) {
  // aria-label: "Kraft F₁ går från punkten 3 rutor åt höger och 2 rutor uppåt." (1 ruta = 10 N)
  const aria = t.t.match(/aria-label="([^"]*)"/)[1];
  const F = [];
  for (const m of aria.matchAll(/Kraft (\S+(?: N)?) går från punkten (\d+) rut(?:a|or) åt (höger|vänster) och (\d+) rut(?:a|or) (uppåt|nedåt)\./g)) {
    F.push([(m[3] === 'höger' ? 1 : -1) * 10 * +m[2], (m[5] === 'uppåt' ? 1 : -1) * 10 * +m[4]]);
  }
  return F;
}
function riktning(x, y) {
  if (!x && !y) return 'Resultanten är noll och har ingen riktning.';
  if (!y) return x > 0 ? 'Rakt åt höger.' : 'Rakt åt vänster.';
  if (!x) return y > 0 ? 'Rakt uppåt.' : 'Rakt nedåt.';
  return `Snett ${y > 0 ? 'uppåt' : 'nedåt'} åt ${x > 0 ? 'höger' : 'vänster'}.`;
}

test('Området Vektorer finns först i kraftkapitlet', () => {
  assert.deepEqual(Object.keys(ctx.window.OMR['4'])[0], 'kraftvektorer');
  assert.equal(ctx.window.OMR['4'].kraftvektorer, 'Vektorer');
});

test('De befintliga vektordelmomenten är flyttade från newton1 med spårbar historik', () => {
  const flyttade = B.filter((t) => t.omr === 'kraftvektorer' && [].concat(t.omrTidigare || []).includes('newton1'));
  assert.equal(flyttade.length, 41);
  for (const t of flyttade) {
    assert.ok(['Resultantbestämning utan trigonometri', 'Resultantbestämning med trigonometri', 'Komposantuppdelning'].includes(t.familj), t.id);
    if (t.familjNyckel) assert.ok(t.familjNyckel.startsWith('kraftvektorer__'), t.id);
  }
  assert.equal(B.filter((t) => t.omr === 'newton1' && ['Addera krafter som vektorer', 'Krafter i komposanter'].includes(t.familj)).length, 0);
});

test('48 nya uppgifter, unika id och rätt område', () => {
  assert.equal(new Set(B.map((t) => t.id)).size, B.length);
  for (const id of NYA) {
    const t = q(id);
    assert.ok(t, id);
    assert.equal(t.kap, 4);
    assert.equal(t.omr, 'kraftvektorer');
    assert.equal(t.miniräknare, true, id);
  }
});

test('Krafter längs en linje: facit och svar stämmer med figurens krafter', () => {
  const linje = NYA.map(q).filter((t) => [].concat(t.familjTidigare || []).includes('Resultant längs en linje'));
  assert.equal(linje.length, 12);
  for (const t of linje) {
    const aria = t.t.match(/aria-label="([^"]*)"/)[1];
    let net = 0;
    for (const m of aria.matchAll(/(\d+) N åt (höger|vänster)/g)) net += (m[2] === 'höger' ? 1 : -1) * +m[1];
    if (t.svarstyp === 'numeriskt') {
      assert.equal(t.rättSvar, net, t.id);
    } else {
      const ratt = t.alternativ.filter((a) => a.ratt);
      assert.equal(ratt.length, 1, t.id);
      const väntat = net ? `${Math.abs(net)} N åt ${net > 0 ? 'höger' : 'vänster'}` : '0 N, krafterna tar ut varandra';
      assert.equal(ratt[0].txt, väntat, t.id);
      assert.ok(t.alternativ.every((a) => a.kommentar && a.kommentar.length > 20), t.id);
      assert.equal(new Set(t.alternativ.map((a) => a.txt)).size, t.alternativ.length, t.id);
    }
    // Friktion och vattenmotstånd ritas längs underlaget (under markens linje), inte mitt på föremålet.
    for (const m of t.t.matchAll(/<text x="[\d.]+" y="([\d.]+)"[^>]*>((?:friktion|vatten)[^<]*)<\/text>/g)) {
      assert.ok(+m[1] > 130, `${t.id}: ${m[2]} ska stå vid underlaget`);
    }
  }
});

test('Rutnätsuppgifter: komposanter, storlek, vinkel och riktning stämmer med figuren', () => {
  const rut = NYA.map(q).filter((t) => [].concat(t.familjTidigare || []).includes('Addera krafter som vektorer'));
  assert.equal(rut.length, 36);
  for (const t of rut) {
    const F = krafterUrFigur(t);
    assert.ok(F.length >= 2, t.id);
    const fx = F.reduce((s, f) => s + f[0], 0), fy = F.reduce((s, f) => s + f[1], 0);
    const R = Math.hypot(fx, fy);
    const d = t.spelDelar;
    assert.equal(d.length, 4);
    // samma inledning och figur på alla delkort
    for (const del of d) assert.ok(del.t.startsWith(t.spelIntro), `${t.id} ${del.etikett}`);
    if (/Bestäm x-komposanten/.test(d[0].fraga)) {
      assert.equal(t.rättSvar[0], fx, t.id);
      assert.equal(t.rättSvar[1], fy, t.id);
      // a-facit visar inte y-komposanterna (FY1_VEKTORER_DELFACIT_2026-11-02)
      assert.doesNotMatch(d[0].s, /F_\{\dy\}/, t.id);
    } else {
      assert.ok(Math.abs(t.rättSvar[0] - Math.hypot(...F[0])) < 1e-3, t.id);
      assert.ok(Math.abs(t.rättSvar[1] - Math.hypot(...F[1])) < 1e-3, t.id);
    }
    assert.ok(Math.abs(t.rättSvar[2] - R) < 1e-3, t.id);
    if (d[3].svarstyp === 'alternativ') {
      const ratt = d[3].alternativ.filter((a) => a.ratt);
      assert.equal(ratt.length, 1, t.id);
      assert.equal(ratt[0].txt, riktning(fx, fy), t.id);
      assert.equal(d[3].rättSvar, ratt[0].txt, t.id);
      assert.equal(new Set(d[3].alternativ.map((a) => a.txt)).size, 4, t.id);
      // c-facit avslöjar inte riktningen (ingen lösningsfigur före d)
      assert.doesNotMatch(d[2].s, /<svg/, t.id);
    } else {
      const a = Math.atan2(fy, fx) * 180 / Math.PI;
      assert.ok(Math.abs(d[3].rättSvar - a) < 1e-3, t.id);
      assert.equal(d[3].svarEnhet, '°');
    }
    // Pilarna börjar och slutar på kryss i rutnätet (1 ruta = 36 px, marginal 20 px)
    const svg = t.spelIntro;
    for (const m of svg.matchAll(/<polygon points="([\d.]+),([\d.]+) /g)) {
      const x = (+m[1] - 20) / 36, y = (+m[2] - 20) / 36;
      assert.ok(Math.abs(x - Math.round(x)) < 1e-6 && Math.abs(y - Math.round(y)) < 1e-6, `${t.id}: pilspets utanför kryss`);
    }
    assert.equal(t.självrättning.length, 4);
    assert.equal(t.svarEtiketter.join(''), 'abcd');
  }
});

test('Facit följer facitmallen med steglista, formel i rubrik och svarsrad', () => {
  for (const id of NYA) {
    const t = q(id);
    assert.match(t.s, /facit-v2 facit-stegvis/, id);
    assert.match(t.s, /facit-rubrik/, id);
    assert.match(t.s, /<strong>Svar:<\/strong>/, id);
    assert.match(t.s, /facit-rubrik">[^<]*\\\(/, id);
    for (const del of t.spelDelar || []) assert.match(del.s, /<strong>Svar:<\/strong>/, `${id} ${del.etikett}`);
    assert.doesNotMatch(t.s + t.t, /None|null|undefined/, id);
  }
});

test('Delmomenten i Vektorer: utan trigonometri, med trigonometri och komposantuppdelning', () => {
  const v = B.filter((t) => t.omr === 'kraftvektorer');
  const fam = {};
  for (const t of v) fam[t.familj] = (fam[t.familj] || 0) + 1;
  assert.deepEqual(fam, { 'Resultantbestämning utan trigonometri': 55, 'Resultantbestämning med trigonometri': 14, Komposantuppdelning: 20 });
  // Inget kort i delmomentet utan trigonometri kräver trigonometri.
  for (const t of v.filter((x) => x.familj === 'Resultantbestämning utan trigonometri')) {
    assert.notEqual(t.trigonometri, true, t.id);
    assert.ok(!(t.spelDelar || []).some((d) => d.trigonometri), t.id);
    assert.doesNotMatch(t.s, /\\(?:sin|cos|tan)\b/, t.id);
  }
  for (const t of v.filter((x) => x.familj === 'Resultantbestämning med trigonometri')) {
    assert.match(t.s, /\\(?:sin|cos|tan)\b/, t.id);
  }
  for (const t of v) assert.ok([].concat(t.familjTidigare || []).length >= 1, t.id);
});
