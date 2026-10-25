'use strict';
/* Ma2 sats och bevis: figurer till äldre kort, lärarbeslut 2026-10-25 (”hellre figur än utan när den tillför något”).
   37 kort fick figur. Åtta kort är dokumenterade undantag. */
const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('node:fs'),vm=require('node:vm'),path=require('node:path');
const c={window:{}};vm.runInNewContext(fs.readFileSync(path.join(__dirname,'..','uppgifterma2.js'),'utf8'),c);
const B=JSON.parse(JSON.stringify(c.window.BANKMA2));const get=id=>{const t=B.find(x=>x.id===id);assert.ok(t,id);return t;};
const MED=['3.11','3.21','3.40','3.51','3.71','3.72','3.83','3.104','3.105','3.106','3.107','3.118','3.124','3.136','3.137','3.196','3.231','3.236','3.248','3.249',
  '3.250','3.251','3.252','3.279','3.281','3.300','3.304','3.324','3.328','3.348','3.352','3.356','3.426','3.429','3.433','3.437','3.506'];
// Undantag: symbolens betydelse (3.277, 3.278) och vad ett bevis är (3.117), där en bild vore själva svaret;
// direkta insättningar (3.207, 3.280, 3.305, 3.329) och ren algebra (3.2130), där en figur inte tillför något.
const UTAN=['3.117','3.207','3.277','3.278','3.280','3.305','3.329','3.2130'];

test('Alla kort i sats_bevis har figur utom de dokumenterade undantagen',()=>{
  const omr=B.filter(q=>q.omr==='sats_bevis');
  assert.deepEqual(omr.filter(q=>!/<svg/.test(q.t)).map(q=>q.id).sort(),[...UTAN].sort());
  for(const id of MED){const svg=get(id).t.match(/<svg[^>]*>/g);assert.ok(svg&&svg.length===1,id);assert.match(svg[0],/role="img"/,id);assert.match(svg[0],/aria-label="[^"]{30,}"/,id);assert.match(svg[0],/max-width:\d+px/,id);}
});

test('Flerdelskortet 3.506 har figur i del a och c men inte i b, där den skulle visa motexemplet',()=>{
  const q=get('3.506'),d=e=>q.spelDelar.find(x=>x.etikett===e).fraga;
  assert.match(d('a'),/<svg/);assert.match(d('c'),/<svg/);assert.doesNotMatch(d('b'),/<svg/);
  assert.ok(q.t.indexOf('<svg')>q.t.indexOf('II:'),'figuren står efter påståendena');
});

test('Figurerna avslöjar inte motexempel och facit är oförändrat',()=>{
  // Satsens figur, inte motexemplet: rektangel för diagonalsatsen, och ingen likbent trapets.
  for(const id of ['3.136','3.426'])assert.match(get(id).t,/rektangel ABCD/,id);
  assert.deepEqual(get('3.104').alternativ.filter(a=>a.ratt).map(a=>a.txt),['Endast A ⇒ B är sann.']);
  assert.equal(get('3.352').rättSvar,70);assert.equal(get('3.124').rättSvar,9);assert.deepEqual(get('3.506').rättSvar,['sant','falskt','nej']);
});
