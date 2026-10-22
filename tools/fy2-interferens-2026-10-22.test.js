'use strict';
/* Fy2 interferens 2026-10-22: inga självrättade kort kvar, 28 nya kort med Pythagoras sats och vägskillnad (2.600–2.627). */
const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('node:fs'),vm=require('node:vm'),path=require('node:path');
const c={window:{}};vm.runInNewContext(fs.readFileSync(path.join(__dirname,'..','uppgifter2.js'),'utf8'),c);
const I=JSON.parse(JSON.stringify(c.window.BANK2.filter(t=>t.omr==='interferens')));
const get=id=>{const t=I.find(x=>x.id===id);assert.ok(t,id);return t;};
const nya=I.filter(t=>{const n=Number(t.id.split('.')[1]);return t.id.startsWith('2.')&&n>=600&&n<=627;});
const V=340,hyp=Math.hypot,utanSvg=h=>h.replace(/<svg[\s\S]*?<\/svg>/g,'');
const nara=(a,b,rel=1e-9)=>Math.abs(a-b)<=Math.abs(b)*rel+1e-12;

test('Inga självrättade kort och alla kort har träningsnivå',()=>{
  assert.deepEqual(I.filter(t=>t.svarstyp==='manuell').map(t=>t.id),[]);
  assert.deepEqual(I.filter(t=>t.traningsniva==null).map(t=>t.id),[]);
  for(const t of I) if(t.svarstyp==='alternativ') assert.equal(t.alternativ.filter(a=>a.ratt).length,1,t.id);
});

test('Omgjorda kort: facit räknas om',()=>{
  const d148=Math.sqrt(13)-2;
  assert.ok(nara(get('2.148').rättSvar[1],2*d148));
  assert.ok(nara(get('2.150').rättSvar[0],2*(hyp(1.62,4)-hyp(0.78,4))));
  assert.ok(nara(get('2.167').rättSvar[0],2*(hyp(5,2)-hyp(5,0.4))));
  assert.ok(nara(get('2.168').rättSvar[1],V/(hyp(4.8,2.4)-hyp(4.8,1.2))));
  assert.deepEqual(get('2.159').rättSvar,[340,510,680,850]);assert.equal(get('2.159').svarsstruktur,'mängd');
  assert.deepEqual(get('2.161').rättSvar,[340,1020]);
  assert.deepEqual(get('2.160').rättSvar,['motfas',255,'minimum']);
  assert.deepEqual(get('2.157').rättSvar,[[4,5,1],'minimum']);assert.equal(get('2.157').spelDelar[0].svarsstruktur,'ordnad');
  for(const id of ['2.154','2.157','2.160','2.162']) for(const d of get(id).spelDelar) assert.match(d.t,/\(Svara [^)]*\.\)<\/p><\/div>$/,`${id}${d.etikett}`);
});

test('28 nya kort i fysikformat med figur',()=>{
  assert.equal(nya.length,28);const niv={};
  for(const t of nya){niv[t.traningsniva]=(niv[t.traningsniva]||0)+1;
    assert.match(t.t,/<svg/,t.id);assert.match(t.poang,/^\(\d\/\d\/\d\)$/,t.id);assert.equal(t.miniräknare,true,t.id);
    assert.match(utanSvg(t.t),/\(Svara [^)]*\.\)<\/p>$/,t.id);
    assert.doesNotMatch(utanSvg(t.t),/340 m\/s|ljudhastighet|ljudfart/i,t.id);
    if(t.svarVardesiffror!=null) assert.doesNotMatch(utanSvg(t.t),/decimal|avrund|värdesiffr/i,t.id);
    if(t.svarstyp==='kort_text') assert.match(t.rättSvar,/^(maximum|minimum)$/,t.id);
  }
  assert.deepEqual(niv,{1:10,2:7,3:7,4:4});
});

test('Nya kort: facit räknas om',()=>{
  const v=id=>get(id).rättSvar;
  assert.ok(nara(v('2.600'),hyp(1.2,1.6)));assert.ok(nara(v('2.601'),13));assert.ok(nara(v('2.602'),hyp(60,80)));
  assert.equal(v('2.603'),25/50);assert.equal(v('2.604'),'maximum');assert.equal(v('2.605'),'minimum');assert.equal(v('2.606'),'minimum');
  assert.ok(nara(v('2.607'),0.4));assert.ok(nara(v('2.608'),0.68));assert.ok(nara(v('2.609'),2.5*4));
  assert.ok(nara(v('2.610'),V/(2*(hyp(2,1.5)-2))));assert.ok(nara(v('2.611'),hyp(6,8)-8));
  assert.deepEqual(v('2.612'),[hyp(60,45)-45,'minimum']);assert.ok((hyp(60,45)-45)/12===2.5);
  assert.ok(nara(v('2.613')[0],hyp(7,2.4)-7,1e-12));assert.ok(nara((hyp(7,2.4)-7)/(V/850),1,1e-9));
  assert.ok(nara(v('2.614'),V/850/2));assert.ok(nara(v('2.615'),V/(2*(hyp(1.2,0.5)-1.2))));
  assert.ok(nara(v('2.616'),V/((hyp(0.36,0.27)-0.36)/1.5)));
  const ds=hyp(4.8,2)-4.8,lam=V/2800;assert.equal(v('2.618'),[0,1,2,3,4].filter(k=>(k+0.5)*lam<ds).length);
  assert.equal(v('2.617'),[1,2,3,4,5].filter(n=>n*12<50).length);
  assert.ok(nara(v('2.619'),6*((hyp(3,4)-3)/1.5)));
  assert.ok(nara((hyp(1.2,1.6)-1.2)/(V/425),1));assert.equal(v('2.620')[1],'minimum');
  assert.ok(nara(v('2.621'),V/((hyp(2.4,1)-2.4)/2)));
  assert.ok(nara((hyp(2,2.1)-2)/(V/1700),4.5));assert.deepEqual(v('2.622'),['minimum',5]);
  assert.ok(nara(v('2.623'),0.75/2.5));
  const s=v('2.624');assert.ok(nara(hyp(s,60)-s,12));
  const dS=x=>hyp(3,0.8+x)-hyp(3,0.8-x),x=v('2.625');assert.ok(Math.abs(dS(x)-2*dS(0.4))<1e-9);assert.equal(get('2.625').geogebra,true);
  assert.deepEqual(v('2.626').map(Math.round),[510,850,1190]);
  const L=v('2.627');assert.ok(Math.abs(hyp(L,1.2)-L-V/850/2)<1e-9);
});
