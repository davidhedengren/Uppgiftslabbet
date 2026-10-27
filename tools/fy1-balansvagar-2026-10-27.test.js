'use strict';
// Balansvågar (Albert och Isaac): begreppsfrågor om vridmoment, en förklaringsuppgift och en beräkning med lutande våg.
const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('node:fs'),vm=require('node:vm'),path=require('node:path');
const c={window:{}};vm.runInNewContext(fs.readFileSync(path.join(__dirname,'../uppgifter.js'),'utf8'),c);
const q=id=>c.window.BANK.find(x=>x.id===id),rad=d=>d*Math.PI/180;
const ids=['4.902','4.903','4.904','4.905','4.906','4.907','4.908','4.909'],flerval=['4.902','4.903','4.904','4.905','4.906','4.909'];
const ratt=id=>q(id).alternativ.filter(a=>a.ratt).map(a=>a.txt);
// Viloläge för en våg med vridpunkten h ovanför bommen: (mH − mV)·L·cos θ = (mH + mV)·h·sin θ
const vila=(mV,mH,L,h)=>Math.atan((mH-mV)*L/((mH+mV)*h))*180/Math.PI;

test('Alla åtta balansvågskort finns i Fy1 kap 4 moment och har egen figur',()=>{
 for(const id of ids){const t=q(id);assert.ok(t,id);assert.equal(t.kap,4,id);assert.equal(t.omr,'moment',id);
  assert.equal((t.t.match(/<svg/g)||[]).length,1,id);assert.match(t.t,/aria-label="[^"]{20,}"/,id);
  assert.ok(t.ledtrad,id);assert.match(t.s,/facit-svar/,id);assert.equal(t.geogebra,false,id);}
});
test('Flervalsfrågorna har ett rätt alternativ och en kommentar till varje alternativ',()=>{
 for(const id of flerval){const t=q(id);assert.equal(t.svarstyp,'alternativ',id);assert.equal(t.självrättning,true,id);
  assert.equal(t.alternativ.length,4,id);assert.equal(ratt(id).length,1,id);
  for(const a of t.alternativ)assert.ok(a.kommentar&&a.kommentar.length>20,id+': '+a.txt);
  assert.match(t.t,/Välj ett alternativ/,id);}
});
test('Rätt alternativ följer momentmodellen för vridpunktens läge',()=>{
 // Vridpunkt ovanför bommen: den tyngre skålen sjunker, och lutningen ökar när h minskar.
 assert.ok(vila(100,110,15,3)>0);assert.equal(ratt('4.902')[0],'Den högra');
 assert.match(ratt('4.903')[0],/^Isaacs/);
 // h = 0 (Albert): momentskillnaden (mH − mV)·g·L·cos θ byter aldrig tecken, så bommen tippar till lodrätt.
 for(const d of [0,30,60,89])assert.ok((51-50)*Math.cos(rad(d))>0);assert.match(ratt('4.904')[0],/lodrätt/);
 // h = 0 och lika massor: momenten är lika i alla lägen.
 assert.match(ratt('4.905')[0],/kvar/);
 assert.match(ratt('4.906')[0],/A går tillbaka.*B blir kvar.*C tippar/);
 assert.ok(vila(100,101,15,1)>vila(100,101,15,3));assert.ok(vila(100,101,10,3)<vila(100,101,15,3));assert.ok(vila(200,201,15,3)<vila(100,101,15,3));
 assert.match(ratt('4.909')[0],/^Minska h/);
});
test('Förklaringsuppgiften rättas manuellt och facit använder momentarmar',()=>{
 const t=q('4.907');assert.equal(t.svarstyp,'resonemang');assert.equal(t.självrättning,false);
 assert.match(t.s,/momentarm/);assert.match(t.s,/Albert/);assert.match(t.s,/Isaac/);
});
test('Beräkningen med lutande våg räknas självständigt och delkorten bär egna förutsättningar',()=>{
 const t=q('4.908'),L=15,h=3.0,v=10,hoger=L*Math.cos(rad(v))-h*Math.sin(rad(v)),vanster=L*Math.cos(rad(v))+h*Math.sin(rad(v));
 const want=[hoger,vanster,100*15.29/14.25];
 t.rättSvar.forEach((x,i)=>assert.ok(Math.abs(x-want[i])<=t.tolerans[i]/10,`del ${i}`));
 assert.ok(Math.abs(vila(100,want[2],L,h)-v)<0.05);
 assert.deepEqual(Array.from(t.svarEnhet),['cm','cm','g']);assert.equal(t.spelDelning,'deluppgifter');
 assert.match(t.spelIntro,/<svg/);assert.match(t.spelIntro,/3,0 cm/);assert.match(t.spelIntro,/100 g/);
 assert.match(t.spelDelar[2].fraga,/15,29 cm/);assert.match(t.spelDelar[2].fraga,/14,25 cm/);
 assert.equal(hoger.toFixed(2),'14.25');assert.equal(vanster.toFixed(2),'15.29');
 for(const d of t.spelDelar){assert.ok(d.fraga&&d.s&&d.ledtrad,d.etikett);assert.doesNotMatch(d.fraga,/avrund|decimal|värdesiffr/i,d.etikett);}
});
