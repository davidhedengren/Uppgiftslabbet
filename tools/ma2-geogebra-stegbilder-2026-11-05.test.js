'use strict';
// Stegvisa GeoGebra-skärmbilder i Ma2-statistikfacit (MA2_STATISTIK_GEOGEBRA_STEGBILDER_2026-11-05.md).
const test = require('node:test');
const assert = require('node:assert');
const fs = require('fs');
const path = require('path');

const root = path.resolve(__dirname, '..');
const src = fs.readFileSync(path.join(root, 'uppgifterma2.js'), 'utf8');
const bank = JSON.parse(src.slice(src.indexOf('['), src.lastIndexOf(']') + 1));
const q = (id) => bank.find((u) => u.id === id);
const imgs = (s) => [...s.matchAll(/<img src="(bilder\/[^"]+)" alt="([^"]+)"/g)].map((m) => ({ src: m[1], alt: m[2] }));

// GeoGebras statistikpanel för respektive uppgift, avläst i GeoGebra 5.4.916 (svenska).
const SERIE = {
  '4.328': { median: '3.5', medel: '4', s: '1.7889', d: ['Min', '2', 'Max', '7'] },
  '4.329': { median: '1', medel: '1.5', s: '1.2693', d: ['Min', '0', 'Max', '4'] },
  '4.330': { median: '1.5', medel: '2', s: '2.6726', d: ['Q1', '0', 'Q3', '2.5'] },
  '4.331': { median: '10', medel: '10', s: '1.0954', d: ['Min', '8', 'Max', '11'] },
  '4.332': { median: '9.5', medel: '10', s: '1.7889', d: ['Min', '8', 'Max', '13'] },
  '4.333': { median: '3', medel: '3.4', s: '1.7127', d: ['Q1', '2', 'Q3', '4'] },
  '4.334': { median: '14', medel: '15', s: '2.6458', d: ['Min', '12', 'Max', '19'] },
  '4.335': { median: '100', medel: '100.4', s: '1.8166', d: ['Min', '98', 'Max', '103'] },
  '4.336': { median: '2', medel: '2.4', s: '1.5776', d: ['Q1', '1', 'Q3', '4'] },
  '4.337': { median: '2', medel: '2', s: '1.633', d: ['Min', '0', 'Max', '5'] },
  '4.338': { median: '0', medel: '0.5', s: '2.2039', d: ['Q1', '-0.5', 'Q3', '2'] },
  '4.339': { median: '12.6', medel: '12.7', s: '0.4517', d: ['Min', '12.2', 'Max', '13.4'] },
  '4.340': { median: '190', medel: '190', s: '7.0711', d: ['Min', '180', 'Max', '200'] },
  '4.341': { median: '2.5', medel: '3.5', s: '2.3905', d: ['Q1', '2', 'Q3', '5'] },
  '4.342': { median: '2', medel: '2.25', s: '0.9258', d: ['Q1', '1.75', 'Q3', '2.75'] },
};
const ENKLA = { '4.450': '2', '4.451': '1.5119', '4.452': '1.8045', '4.453': '1.1832', '4.455': '1.1629', '4.456': '0.3077', '4.457': '4', '4.459': '2.6693', '6.09': '1.633' };
const sl = (id) => id.replace('.', '-');
const gemensamma = ['bilder/geogebra-kalkylblad-perspektiv.png', 'bilder/geogebra-envariabelanalys-meny.png'];

test('alla refererade skärmbilder finns och har alternativtext', () => {
  for (const id of [...Object.keys(SERIE), ...Object.keys(ENKLA)]) {
    const u = q(id);
    for (const s of [u.s, ...(u.spelDelar || []).map((d) => d.s)]) {
      const b = imgs(s);
      assert.ok(b.length >= 3, id);
      for (const { src: f, alt } of b) {
        assert.ok(fs.statSync(path.join(root, f)).size > 3000, f);
        assert.ok(alt.length > 20, f);
      }
    }
  }
});

test('varje delkort visar hela vägen i GeoGebra med uppgiftens egna bilder', () => {
  for (const [id, v] of Object.entries(SERIE)) {
    const u = q(id);
    for (const d of u.spelDelar) {
      const f = imgs(d.s).map((x) => x.src);
      for (const g of gemensamma) assert.ok(f.includes(g), `${id}${d.etikett} ${g}`);
      assert.ok(f.includes(`bilder/geogebra-${sl(id)}-data.png`), `${id}${d.etikett}`);
      assert.match(d.s, /Perspektiv<\/strong> och sedan <strong>Kalkylblad/);
      if (d.etikett === 'b') {
        assert.ok(f.includes(`bilder/geogebra-${sl(id)}-stolp.png`), id);
        assert.match(d.s, /Stolpdiagram/);
      } else {
        assert.ok(f.includes(`bilder/geogebra-${sl(id)}-analys.png`), `${id}${d.etikett}`);
      }
    }
    // Avlästa värden står som i GeoGebra.
    assert.match(u.spelDelar[0].s, new RegExp(`På raden Median står ${v.median.replace('.', '\\.')}`));
    assert.match(u.spelDelar[2].s, new RegExp(`På raden Medel står ${v.medel.replace('.', '\\.')} och på raden s står ${v.s.replace('.', '\\.')}`));
    assert.match(u.spelDelar[3].s, new RegExp(`${v.d[0]} = ${v.d[1].replace('.', '\\.')} och ${v.d[2]} = ${v.d[3].replace('.', '\\.')}`));
  }
});

test('delkort avslöjar inte senare delars svar', () => {
  for (const [id, v] of Object.entries(SERIE)) {
    const [a, b, c] = q(id).spelDelar;
    // a och b visar varken Sx eller rader för d; c visar inte d:s rader.
    for (const d of [a, b]) {
      assert.ok(!d.s.includes(v.s), `${id}${d.etikett}`);
      assert.ok(!d.s.includes('medel-s.png'), `${id}${d.etikett}`);
      assert.doesNotMatch(d.s, /min-max\.png|q1-q3\.png/);
    }
    assert.ok(imgs(a.s).some((x) => x.src.endsWith('-median.png')), id);
    assert.doesNotMatch(c.s, /min-max\.png|q1-q3\.png|Variationsbredden|Kvartilavståndet/);
  }
});

test('huvudfacit visar arbetsgången en gång och hänvisar sedan till a)', () => {
  for (const id of Object.keys(SERIE)) {
    const s = q(id).s;
    assert.equal((s.match(/geogebra-kalkylblad-perspektiv\.png/g) || []).length, 1, id);
    assert.equal((s.match(/Använd analysfönstret från a\)/g) || []).length, 3, id);
    assert.equal((s.match(/class="facit-svar"/g) || []).length, 4, id);
  }
});

test('enkla uppgifter visar raden s från GeoGebra och behåller egna inledande steg', () => {
  for (const [id, s] of Object.entries(ENKLA)) {
    const u = q(id);
    assert.ok(u.s.includes(`På raden s står ${s}.`) || u.s.includes(`på raden s står ${s}.`), id);
    assert.ok(u.s.includes(`bilder/geogebra-${sl(id)}-data.png`), id);
    assert.equal(u.geogebra, true, id);
    assert.equal(u.miniräknare, true, id);
  }
  assert.match(q('4.457').s, /x=13/);
  assert.match(q('4.456').s, /Beräkna förbättringarna för varje elev/);
  assert.match(q('4.451').s, /Läs av varje prick/);
  assert.match(q('4.455').s, /Läs av varje matchs antal mål/);
});
