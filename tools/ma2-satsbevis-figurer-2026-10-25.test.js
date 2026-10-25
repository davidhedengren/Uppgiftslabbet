'use strict';
/* Ma2 sats och bevis, figurer 2026-10-25. Först fick 45 kort figur. Efter lärarens granskning togs figurerna bort igen
   på logik- och begreppskorten, eftersom de var tvingade. Figurer behålls bara där uppgiften handlar om en konkret figur
   eller beräkning: 3.236 och 3.352 (tredje vinkeln i en triangel), 3.433 (yttervinklarnas summa) och 3.2128 (sexhörningen). */
const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('node:fs'),vm=require('node:vm'),path=require('node:path');
const c={window:{}};vm.runInNewContext(fs.readFileSync(path.join(__dirname,'..','uppgifterma2.js'),'utf8'),c);
const B=JSON.parse(JSON.stringify(c.window.BANKMA2));const get=id=>{const t=B.find(x=>x.id===id);assert.ok(t,id);return t;};
const BEHALL=['3.236','3.352','3.433','3.2128'];
const BORTTAGNA=['3.11','3.21','3.40','3.51','3.71','3.72','3.83','3.104','3.105','3.106','3.107','3.118','3.124','3.136','3.137','3.196','3.231','3.248','3.249',
  '3.250','3.251','3.252','3.279','3.281','3.300','3.304','3.324','3.328','3.348','3.356','3.426','3.429','3.437','3.506',
  '3.2122','3.2123','3.2124','3.2125','3.2126','3.2127','3.2129'];

test('Figurerna behålls bara på de fyra kort där de bär uppgiften',()=>{
  for(const id of BEHALL){const svg=get(id).t.match(/<svg[^>]*>/g);assert.ok(svg&&svg.length===1,id);assert.match(svg[0],/aria-label="[^"]{30,}"/,id);}
  for(const id of BORTTAGNA)assert.doesNotMatch(get(id).t,/<svg/,id);
  const q=get('3.506');for(const d of q.spelDelar)assert.doesNotMatch(d.fraga,/<svg/,'3.506 del '+d.etikett);
});

test('Borttagningen lämnade facit och alternativ orörda',()=>{
  assert.deepEqual(get('3.104').alternativ.filter(a=>a.ratt).map(a=>a.txt),['Endast A ⇒ B är sann.']);
  assert.equal(get('3.352').rättSvar,70);assert.equal(get('3.124').rättSvar,9);assert.deepEqual(get('3.506').rättSvar,['sant','falskt','nej']);assert.equal(get('3.2128').rättSvar,720);
});
