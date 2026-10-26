const fs=require('fs'),vm=require('vm'),assert=require('node:assert/strict'),path=require('path');
function bank(file){const c={window:{}};vm.runInNewContext(fs.readFileSync(path.join(__dirname,'..',file),'utf8'),c);return Object.fromEntries(Object.values(c.window).find(Array.isArray).map(q=>[q.id,q]));}
const ma2=bank('uppgifterma2.js'),fy=bank('uppgifter.js');
for(const id of ['2.261','2.330','2.333','2.336','2.347','2.354']){
 const q=ma2[id];assert(q.s.includes('facit-rubrik'));assert.equal(q.spelDelar.length,q.rättSvar.length);
 for(const p of q.spelDelar){assert(p.s.includes('facit-rubrik')&&p.s.includes('facit-svar'));assert(q.s.includes(p.s));assert(p.ledtrad.length>40);assert(p.t.length>p.fraga.length);assert.equal(q.miniräknare,true);assert.equal(q.geogebra,false);}
}
const [c,a,t]=ma2['2.261'].rättSvar;assert(Math.abs(c*a*a-45)<1e-11);assert(Math.abs(c*a**5-121.5)<1e-11);assert(Math.abs(c*a**t-200)<1e-10);
assert.equal(a.toFixed(3),'1.392');assert(Math.abs(a-1.393)>ma2['2.261'].tolerans[1]);
assert(!ma2['2.261'].spelDelar[0].s.includes('1{,}392'));
assert(!ma2['2.330'].spelDelar[0].s.includes('-18'));
assert(!ma2['2.336'].spelDelar[0].s.includes('900'));
assert(!ma2['2.347'].spelDelar[0].s.includes('135'));
const f330=x=>2*(x-1)*(x-7);assert.equal(f330(3),-16);assert.equal(f330(4),ma2['2.330'].rättSvar[1]);
for(const x of ma2['2.333'].rättSvar[1])assert(Math.abs(2*(x-2)**2-9)<1e-12);
assert.equal(ma2['2.336'].rättSvar[1],30*30);assert.equal(2*(30+30),120);
assert.equal(5*4**1.5,40);assert.equal(5*9**1.5,ma2['2.347'].rättSvar[1]);
assert.equal(4.5*2**2,18);assert.equal(4.5*8**2,288);assert.equal(4.5*ma2['2.354'].rättSvar[1]**2,72);
for(const [id,value] of Object.entries({'2.321':75/1e6,'2.322':120/100*80/100,'2.323':3.6*1000/60,'2.324':2*60/(150/1000),'2.325':35*12/1000*1000,'2.326':(1.8-.6)*1000})){
 const q=fy[id];assert(Math.abs(q.rättSvar-value)<1e-9);assert(q.ledtrad.length>50);assert(q.s.includes('facit-svar'));assert(!q.s.includes('facit-steglista'));assert(q.miniräknare&&!q.geogebra);
}
console.log('6 Ma2-huvuduppgifter, 13 självständiga delfacit, 6 fysikfacit: matematik, precision, ledtrådar och verktyg godkända.');
// Alla 107 tidigare tomma delfacit ska nu vara självständigt skrivna.
const more=['2.370','2.389','2.390','2.426','2.428','2.433','2.444','2.445','2.459','2.460','2.461','2.462','2.463','2.464','2.493','2.495','2.385','2.387','2.393','2.395','2.397','2.401','2.402','2.404','2.411','2.413','2.414','2.416','2.419','2.420','2.421','2.425','2.427','2.429','2.430','2.431','2.434','2.437','2.439'];
let count=13;
for(const id of more){const q=ma2[id];for(const p of q.spelDelar){count++;assert(p.s.includes('facit-rubrik')&&p.s.includes('facit-svar'));assert(p.ledtrad.replace(/<[^>]*>/g,'').trim().length>12);assert(q.s.includes(p.s));assert(p.t);assert(!q.geogebra||q.miniräknare);} }
assert.equal(count,107);
const same=(id,want)=>assert.deepEqual(JSON.parse(JSON.stringify(ma2[id].rättSvar)),want,id);
assert(Math.abs(ma2['2.370'].rättSvar[0]-(1.52*6+1.3))<1e-12);same('2.390',[2*(-2)**2-(-2)+4,2-1+4]);
same('2.426',[-4*2+9,-4*(-1)+9,1]);same('2.433',[5-3*(-2),5-3*4,1]);
assert.equal(Math.round(ma2['2.459'].rättSvar[1]),9733);assert.equal(ma2['2.459'].tolerans[1],.5);
assert(Math.abs(2.25*ma2['2.463'].rättSvar[2]**3-80)<1e-10);
same('2.385',[[-2,2],[-3,1]]);for(const x of [-3,1])assert.equal(Math.abs(x+1)+1,3);
assert.equal(5-.5*(1-3)**2,3);assert.equal(5-.5*(5-3)**2,3);assert.equal(ma2['2.387'].spelDelar[0].rättSvar,5);
for(const x of [-3,1])assert.equal((x+2-1)**2+1,5);
same('2.395',[[1],[2]]);assert.equal(4-(1+1),2);assert.equal(4-2*2,0);
same('2.397',[3,3,3]);assert.equal((2*3-3)+1,4);
same('2.401',[18,[-4,4]]);same('2.402',[4,0,-1]);same('2.404',[1,4,[-1,3]]);
const cubic=x=>.5*(x-1)**3+2;assert.equal(cubic(2)-cubic(0),ma2['2.411'].rättSvar[0]);assert.equal(cubic(1),2);
same('2.413',[0,8]);same('2.414',[3,3,[-1,1]]);same('2.416',[4,-1,3]);
same('2.419',[-3,2,4/3]);assert(Math.abs(2*(4/3+1)-1-(-4/3+5))<1e-12);
same('2.420',[1,7]);same('2.421',[4.5,-1]);assert.equal(.5*2**3+2-(.5*(-1)**3+2),4.5);
same('2.425',[2,5,2]);same('2.427',[4,-1,3]);same('2.429',[1,[-1,3]]);
same('2.430',[2,11]);same('2.431',[1,3]);same('2.434',[1,3,0]);same('2.437',[4,0,[-2,2]]);same('2.439',[1,-1]);
console.log('107 egna delfacit, grafavläsningar, sammansättningar och precision: godkända.');
for(const id of ['2.636','2.637']){assert.equal(ma2[id].spel,false);assert.equal(ma2[id].självrättning,false);assert.equal(ma2[id].svarstyp,'resonemang');assert.equal(ma2[id].rättSvar,null);assert(ma2[id].s.includes('facit-rubrik'));assert(ma2[id].s.includes('facit-svar'));}
assert.equal(20*5,100);assert.equal(20/5,4);
const r=Math.sqrt(6)/2;for(const [u,v]of [[1+r,1-r],[1-r,1+r]]){assert(Math.abs(u+v-2)<1e-12);assert(Math.abs(u*u+v*v-5)<1e-12);assert(10**u>0&&10**v>0);}
assert.equal(ma2['2.428'].svarFormat[2],'text');
console.log('Två manuella logaritmsystem och avgränsad kontroll av funktionsnotation godkända.');
