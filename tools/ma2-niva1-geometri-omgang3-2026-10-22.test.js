'use strict';
/* Påfyllnad 2026-10-22, omgång 3: 48 kort på nivå 1 i Ma2 kap 3 (3.650–3.697). */
const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('node:fs'),vm=require('node:vm'),path=require('node:path');
const c={window:{}};vm.runInNewContext(fs.readFileSync(path.join(__dirname,'..','uppgifterma2.js'),'utf8'),c);
const nya=c.window.BANKMA2.filter(t=>{const [k,n]=t.id.split('.').map(Number);return k===3&&n>=650&&n<=697;});
const get=id=>nya.find(t=>t.id===id);
const plain=v=>JSON.parse(JSON.stringify(v));

test('48 kort på nivå 1, tolv per område, med figur',()=>{
  assert.equal(nya.length,48);const per={};
  for(const t of nya){per[t.omr]=(per[t.omr]||0)+1;assert.equal(t.traningsniva,1,t.id);assert.equal(t.spel,true,t.id);assert.match(t.t,/<svg/,t.id);
    if(t.svarstyp==='alternativ')assert.equal(t.alternativ.filter(a=>a.ratt).length,1,t.id);}
  assert.deepEqual(per,{geometri_problemlosning:12,koordinatgeometri_problemlosning:12,avstandsformeln_mittpunktsformeln:12,bevis_likformighet:12});
});

test('Facit räknas om',()=>{
  const d=(a,b)=>Math.hypot(b[0]-a[0],b[1]-a[1]);
  const fall={'3.650':180-90-35,'3.651':100/2,'3.652':90,'3.653':10*6-4*3,'3.654':30/2,'3.655':(180-40)/2,'3.656':360-85-95-110,'3.657':65,'3.658':180-65,'3.661':2*5,
    '3.662':6*4,'3.663':6*7/2,'3.664':2*(4-(-2))+2*(5-1),'3.666':7,'3.668':3,'3.670':5-(-2),'3.671':(9-1)*(6-2)/2,'3.672':6*3,
    '3.674':d([-3,1],[2,13]),'3.675':d([0,-5],[8,10]),'3.676':d([1,1],[4,3]),'3.677':d([0,0],[9,12]),'3.683':d([1,2],[13,7]),'3.684':d([2,3],[5,7]),
    '3.691':8*9/6,'3.692':48,'3.694':7.5/3,'3.697':5*6/3};
  for(const [id,v] of Object.entries(fall)){const t=get(id);assert.ok(Math.abs(t.rättSvar-v)<=Math.max(1e-9,t.tolerans||0),`${id}: ${t.rättSvar} ≠ ${v}`);}
  const mitt=(a,b)=>[(a[0]+b[0])/2,(a[1]+b[1])/2];
  assert.deepEqual(plain(get('3.665').rättSvar),[-6,6]);
  assert.deepEqual(plain(get('3.678').rättSvar),mitt([-5,2],[2,-6]));
  assert.deepEqual(plain(get('3.679').rättSvar),mitt([0,10],[6,0]));
  assert.deepEqual(plain(get('3.680').rättSvar),mitt([2,9],[14,3]));
  assert.deepEqual(plain(get('3.685').rättSvar),mitt([-4,7],[4,-1]));
});

test('Likformighetsbeslut stämmer med vinklar och sidkvoter',()=>{
  const ratt=id=>get(id).alternativ.find(a=>a.ratt).txt;
  assert.notEqual(180-45-65,180-45-80);assert.match(ratt('3.686'),/^Nej/);
  assert.equal(180-35-85,60);assert.match(ratt('3.687'),/^Ja/);
  assert.ok([4/2,6/3,8/4].every(k=>k===2));assert.match(ratt('3.688'),/^Ja/);
  assert.notEqual(10/6,2);assert.match(ratt('3.689'),/^Nej/);
});
