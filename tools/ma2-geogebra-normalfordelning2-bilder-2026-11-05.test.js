'use strict';
// Omgång 2: Sannolikhetskalkylatorns skärmbilder i resterande Ma2-normalfördelningsfacit
// (MA2_NORMALFORDELNING_GEOGEBRA_BILDER2_2026-11-05.md).
const test = require('node:test');
const assert = require('node:assert');
const fs = require('fs');
const path = require('path');

const root = path.resolve(__dirname, '..');
const src = fs.readFileSync(path.join(root, 'uppgifterma2.js'), 'utf8');
const bank = JSON.parse(src.slice(src.indexOf('['), src.lastIndexOf(']') + 1));
const q = (id) => bank.find((u) => u.id === id);
const facit = (u) => [u.s, ...(u.spelDelar || []).map((d) => d.s)];

// uppgift -> bilder (slugs) som ska finnas i facit
const BILDER = {
  '4.07': ['4-07'], '4.08': ['4-08-a', '4-08-b'], '4.13': ['4-13'], '4.19': ['4-19'], '4.26': ['4-26'],
  '4.27': ['4-27-a', '4-27-b'], '4.37': ['4-37'], '4.38': ['4-38-a', '4-38-b'], '4.45': ['4-45-a', '4-45-b'],
  '4.51': ['4-51'], '4.53': ['4-53'], '4.57': ['4-57-a', '4-57-b'], '4.69': ['4-69'], '4.70': ['4-70'],
  '4.87': ['4-87-a1', '4-87-a2', '4-87-b', '4-87-c'], '4.95': ['4-95-a', '4-95-b'], '4.104': ['4-104'],
  '4.116': ['4-116-a', '4-116-b'], '4.117': ['4-117-a', '4-117-b'], '4.153': ['4-153-a', '4-153-b'],
  '4.176': ['4-176-a', '4-176-b'], '4.177': ['4-177-a', '4-177-b'], '4.178': ['4-178-a', '4-178-b'],
  '4.216': ['4-216-a', '4-216-b'], '4.218': ['4-218'], '4.231': ['4-231-a', '4-231-b'], '4.260': ['4-260'],
  '4.261': ['4-261'], '4.263': ['4-263-a', '4-263-b'], '4.285': ['4-285'], '4.287': ['4-287-a', '4-287-b'],
  '4.304': ['4-304'], '4.2043': ['4-2043-a', '4-2043-b'], '4.2045': ['4-2045'], '4.2046': ['4-2046'],
  '4.2049': ['4-2049'], '4.2051': ['4-2051'], '4.2093': ['4-2093'], '4.2094': ['4-2094'], '4.2120': ['4-2120'],
  '4.2123': ['4-2123'], '4.2125': ['4-2125'], '4.2126': ['4-2126'], '4.2127': ['4-2127'],
  '4.523': ['4-523'], '4.526': ['4-526'], '4.530': ['4-530'], '4.2087': ['4-2087'], '4.2088': ['4-2088'],
  '4.2089': ['4-2089'], '4.2091': ['4-2091'], '4.2095': ['4-2095'], '4.110': ['4-110'], '4.217': ['4-217'], '4.58': ['4-58'],
};

test('varje uppgift har sina inringade bilder och vägen till kalkylatorn', () => {
  for (const [id, slugs] of Object.entries(BILDER)) {
    const alla = facit(q(id)).join('');
    assert.ok(alla.includes('bilder/geogebra-sannolikhet-perspektiv.png'), id);
    assert.match(alla, /Perspektiv<\/strong> och sedan <strong>Sannolikhet/, id);
    for (const sl of slugs) {
      assert.ok(alla.includes(`bilder/geogebra-${sl}.png`), `${id} ${sl}`);
      assert.ok(fs.statSync(path.join(root, `bilder/geogebra-${sl}.png`)).size > 5000, sl);
    }
    assert.equal(q(id).geogebra, true, id);
    assert.equal(q(id).miniräknare, true, id);
  }
});

test('varje fristående delkort med en beräkning visar själv hur kalkylatorn öppnas', () => {
  for (const id of Object.keys(BILDER)) {
    for (const d of q(id).spelDelar || []) {
      if (!d.s.includes('bilder/geogebra-4-')) continue;
      assert.ok(d.s.includes('geogebra-sannolikhet-perspektiv.png'), `${id}${d.etikett}`);
      assert.equal((d.s.match(/geogebra-sannolikhet-perspektiv\.png/g) || []).length, 1, `${id}${d.etikett}`);
    }
    assert.equal((q(id).s.match(/geogebra-sannolikhet-perspektiv\.png/g) || []).length, 1, id);
  }
});

test('befintlig facittext står kvar i de facit som fick bilder infogade', () => {
  assert.match(q('4.07').spelDelar[0].s, /Vid X ≤ visas cirka 1,9954/);
  assert.match(q('4.178').s, /Använd andelen före avrundning från a\)/);
  assert.match(q('4.285').s, /Beräkna den ökade mängden/);
  assert.match(q('4.287').s, /Subtrahera ekvationerna/);
});

test('omskrivna tunna facit har rubriker och svarsrad', () => {
  for (const id of ['4.523', '4.526', '4.530', '4.2087', '4.2088', '4.2089', '4.2091', '4.2095', '4.110', '4.217', '4.58']) {
    const s = q(id).s;
    assert.match(s, /<p class="facit-svar"><strong>Svar:<\/strong>/, id);
    assert.ok((s.match(/class="facit-rubrik"/g) || []).length >= 4, id);
    assert.ok((s.match(/<li>/g) || []).length === (s.match(/class="facit-rubrik"/g) || []).length, id);
  }
});
