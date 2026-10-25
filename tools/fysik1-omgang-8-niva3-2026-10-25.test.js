'use strict';
/* Fy1 2026-10-25 omgång 8: nivå 3 (och några nivå 2) i a-t-diagram, tyngdkraft, ström och parallellkoppling.
   Områdena hade bara 1–5 kort på nivå 3. Facit räknas om här från uppgifternas givna värden. */
const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('node:fs'),vm=require('node:vm'),path=require('node:path');
const c={window:{}};vm.runInNewContext(fs.readFileSync(path.join(__dirname,'..','uppgifter.js'),'utf8'),c);
const B=JSON.parse(JSON.stringify(c.window.BANK));const q=id=>{const t=B.find(x=>x.id===id);assert.ok(t,id);return t;};
const NYA=[...['3.733','3.734','3.735','3.736','3.737','3.738'],...Array.from({length:6},(_,i)=>`4.${885+i}`),...Array.from({length:13},(_,i)=>`8.${636+i}`)];
const near=(id,v)=>{const t=q(id);assert.ok(Math.abs(t.rättSvar-v)<=Math.abs(v)*1e-9+1e-12,`${id}: ${t.rättSvar} ≠ ${v}`);};
const g=9.82,e=1.602e-19;

test('25 nya Fy1-kort, främst nivå 3, med fysikformat och unika facit',()=>{
  const per={};let n3=0;
  for(const id of NYA){const t=q(id);per[t.omr]=(per[t.omr]||0)+1;if(t.traningsniva===3){n3++;assert.equal(t.niva,'C',id);assert.equal(t.poang,'(0/1/0)',id);}
    assert.equal(t.miniräknare,true,id);assert.match(t.s,/facit-svar/,id);assert.doesNotMatch(t.s,/facit-steglista/,id);}
  assert.deepEqual(per,{at_diagram:6,tyngdkraft:6,strom:6,parallellkoppling:7});assert.equal(n3,18);
  for(const id of NYA){const t=q(id);if(t.svarstyp!=='numeriskt')continue;
    const krock=B.filter(w=>w.omr===t.omr&&w.id!==id&&typeof w.rättSvar==='number'&&Math.abs(w.rättSvar-t.rättSvar)<1e-9).map(w=>w.id);
    assert.deepEqual(krock,[],`${id} har samma facit som ${krock}`);
    if(t.tolerans>0)assert.match(t.t,/\(Svara[^)]*(decimal|heltal|värdesiffror)[^)]*\)/,id);}
  for(const id of NYA.filter(id=>q(id).svarstyp==='alternativ'))assert.ok(!q(id).alternativ[0].ratt,id);
  // kretsfiguren: huvudledningen får inte kortsluta de parallella grenarna
  assert.doesNotMatch(q('8.648').t,/L420 60 L60 60/);
});

test('Facit räknas om',()=>{
  // a-t-diagram
  near('3.733',(0+2.5*4)/2*4+10*4+(10+(10-1.5*4))/2*4);near('3.734',-6*8+2*8*8/2);near('3.735',2+6*4/2);near('3.736',2+(15-3*2)/1.2);near('3.738',1.5*2*2/2*2+1.5*2*5);
  assert.deepEqual(q('3.737').alternativ.find(a=>a.ratt).txt.match(/−?\d+/g).slice(0,1),['3']);
  // tyngdkraft
  near('4.885',35/1.62*g);near('4.886',400/1.62);near('4.887',g*2.03/12.0);near('4.888',g/1.62);near('4.890',900*(g-3.71)/1000);
  // ström
  near('8.636',0.8*4500/1500);near('8.637',(26-12)/(10-6));near('8.638',13*60/e);near('8.639',0.4*3+0.4*2/2);near('8.640',2.5+0.8-1.2);near('8.641',20e3*50e-6/e);
  // parallellkoppling
  near('8.642',1/(1/15-1/60));near('8.643',2*1.8/3);near('8.644',40*0.3/0.2);near('8.645',1/(1/10+1/15+1/30));
  near('8.647',Math.floor(16/(1200/230)));assert.ok(3*1200/230<16&&4*1200/230>16);near('8.648',12/30+12/60);
});
