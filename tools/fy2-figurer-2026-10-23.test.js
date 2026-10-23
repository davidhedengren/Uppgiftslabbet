'use strict';
// Självständiga fysik- och geometrikontroller av de rättade figurerna.
const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('node:fs'),vm=require('node:vm'),path=require('node:path');
const c={window:{}};vm.runInNewContext(fs.readFileSync(path.join(__dirname,'..','uppgifter2.js'),'utf8'),c);
const get=id=>c.window.BANK2.find(q=>q.id===id),ids=[...Array.from({length:11},(_,i)=>`3.${230+i}`),'3.490','3.491','3.501','3.502','3.503','3.508','3.509','3.511','3.484','3.485','3.493'];
const attr=(tag,name)=>tag.match(new RegExp('(?:^| )'+name+'="([^"]+)"'))?.[1];
const texts=q=>[...q.t.matchAll(/<text\b([^>]*)>([^<]*)<\/text>/g)].map(m=>({x:+attr(m[1],'x'),y:+attr(m[1],'y'),text:m[2]}));
const vectors=(q,color)=>[...q.t.matchAll(/<path\b[^>]*>/g)].map(m=>m[0]).filter(t=>attr(t,'stroke')===color&&attr(t,'stroke-width')==='3').map(t=>attr(t,'d').match(/^M([\d.]+) ([\d.]+)L([\d.]+) ([\d.]+)$/)).filter(Boolean).map(m=>({a:[+m[1],+m[2]],b:[+m[3],+m[4]]}));
test('Kompassernas facit följer fältet från N till S vid den utritade positionen',()=>{
 for(let n=230;n<=240;n++){
  const q=get(`3.${n}`),ts=texts(q),N=ts.find(t=>t.text==='N'),S=ts.find(t=>t.text==='S');
  const ring=[...q.t.matchAll(/<circle\b[^>]*>/g)].map(m=>m[0]).find(t=>attr(t,'r')==='23');assert.ok(ring,q.id);
  const P=[+attr(ring,'cx'),+attr(ring,'cy')];
  // Textbaseline är 8 px under horisontella polcentra, 7,5 under vertikala.
  const offset=n<237?8:7.5;
  const contribution=(pole,sign)=>{const dx=P[0]-pole.x,dy=P[1]-(pole.y-offset),r=Math.hypot(dx,dy);return [sign*dx/r**3,sign*dy/r**3];};
  const a=contribution(N,1),b=contribution(S,-1),F=[a[0]+b[0],a[1]+b[1]];
  const answer=Math.abs(F[0])>Math.abs(F[1])?(F[0]>0?'A':'B'):(F[1]>0?'D':'C');assert.equal(q.rättSvar,answer,q.id);
  assert.match(q.t,/ovanifrån/);assert.match(q.t,/Bortse från jordens magnetfält/);assert.match(q.t,/Kompassen visas utan nål/);
 }
});
test('Hastighetsfiltret har motriktade krafter och riktningsfrågan har en centrerad jon',()=>{
 const q=get('3.490'),v=vectors(q,'#b74738')[0],E=vectors(q,'#087f8c')[0];assert.ok(v.b[0]>v.a[0]&&v.a[1]===v.b[1]);assert.ok(E.b[1]>E.a[1]&&E.a[0]===E.b[0]);
 assert.match(q.t,/B in i bilden/);assert.equal(q.rättSvar,4e4/.020);
 // I högerorienterade koordinater ger v åt höger och B in i bilden F_m uppåt, mot E nedåt.
 const r=get('3.491');assert.match(r.t,/<circle cx="240" cy="150" r="15"/);assert.match(r.t,/viewBox="0 0 480 300"/);assert.match(r.t,/B ut ur bilden/);
 const rv=vectors(r,'#b74738');assert.equal(rv.length,1);assert.ok(rv[0].b[1]<rv[0].a[1]);assert.equal(r.alternativ.find(a=>a.ratt).txt,'åt höger');
});
test('Flygplanets vingbredd är tvärs flygriktningen, stavens krets har motstånd',()=>{
 const q=get('3.501');assert.match(q.t,/data-aircraft="wings"/);assert.match(q.t,/data-aircraft="fuselage"/);
 const flight=vectors(q,'#b74738')[0],dim=vectors(q,'#243447');assert.equal(dim.length,2);assert.equal(flight.a[0],flight.b[0]);assert.ok(flight.b[1]<flight.a[1]);
 assert.equal(Math.min(...dim.map(v=>v.b[0])),70);assert.equal(Math.max(...dim.map(v=>v.b[0])),410);for(const d of dim)assert.equal(d.a[1],d.b[1]);
 assert.ok(Math.abs(q.rättSvar-4.5e-5*30*250)<1e-12);
 assert.match(get('3.503').t,/<rect x="88" y="127" width="24" height="56"/);assert.match(get('3.503').t,/3,0 Ω/);assert.ok(Math.abs(get('3.503').rättSvar-.6/3)<1e-12);
 assert.ok(Math.abs(get('3.502').rättSvar-.12/(.4*.15))<1e-12);
});
test('Vinkelben, båge och text hör till samma vinkel och komponenterna ger rätt svar',()=>{
 for(const id of ['3.508','3.509','3.511']){
  const q=get(id),B=vectors(q,'#b74738')[0],delta=[B.b[0]-B.a[0],B.b[1]-B.a[1]],angle=Math.atan2(delta[1],delta[0])*180/Math.PI,expected=id==='3.511'?Math.atan(3)*180/Math.PI:70;
  assert.ok(Math.abs(angle-expected)<1e-9,id);
  const arc=q.t.match(/<path data-angle="[^"]+" d="([^"]+)"/)[1],end=arc.match(/ 0 0 1 ([\d.]+) ([\d.]+)$/),endAngle=Math.atan2(+end[2]-B.a[1],+end[1]-B.a[0])*180/Math.PI;assert.ok(Math.abs(endAngle-expected)<.002,id);
  const label=texts(q).find(t=>t.text===(id==='3.511'?'i':'70°'));const la=Math.atan2(label.y-5-B.a[1],label.x-B.a[0])*180/Math.PI;assert.ok(Math.abs(la-expected/2)<1e-9);assert.ok(label.x<B.b[0]-15);
  const value=id==='3.508'?50*Math.cos(angle*Math.PI/180):id==='3.509'?50*Math.sin(angle*Math.PI/180):angle;assert.ok(Math.abs(value-q.rättSvar)<1e-9,id);
 }
});
test('Alla ändrade kort har genomtänkta verktyg och sammanhängande facit',()=>{
 for(const id of ids){const q=get(id);assert.equal(q.miniräknare,true,id);assert.equal(q.geogebra,false,id);assert.equal(q.traningsniva,1,id);assert.equal(q.självrättning,true,id);assert.doesNotMatch(q.s,/facit-steglista|<ol/,id);assert.match(q.s,/facit-svar/,id);}
});
