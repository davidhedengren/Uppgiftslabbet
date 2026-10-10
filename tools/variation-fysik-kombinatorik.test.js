'use strict';
const {test}=require('node:test');
const assert=require('node:assert/strict');
const fs=require('node:fs');
const path=require('node:path');
const vm=require('node:vm');
function bank(file,key){const c={window:{}};vm.runInNewContext(fs.readFileSync(path.join(__dirname,'..',file),'utf8'),c);return new Map(c.window[key].map(q=>[q.id,q]));}
const fy=bank('uppgifter.js','BANK'),ma=bank('uppgiftermatf1.js','BANKMATF1');
const near=(a,b)=>assert.ok(Math.abs(a-b)<1e-3,`${a} ≠ ${b}`);
function graphAreas(id,xmax,ymin,ymax,width=460){
 const left=width>300?65:45,right=width-25;
 return [...fy.get(id).t.matchAll(/<polyline points="([^"]+)"/g)].map(m=>{
  const points=m[1].split(' ').map(p=>p.split(',').map(Number)).map(([x,y])=>[(x-left)*xmax/(right-left),ymin+(220-y)*(ymax-ymin)/155]);
  return points.slice(1).reduce((s,p,i)=>s+(p[0]-points[i][0])*(p[1]+points[i][1])/2,0);
 });
}
test('De ritade kraftgrafernas areor stämmer med impulser, medelkraft och arbete',()=>{
 for(const [id,xmax,ymin,ymax,divisor] of [
  ['5.601',.5,0,15,1],['5.602',.2,0,60,1],['5.604',.3,0,20,1],
  ['5.605',.4,0,80,.4],['5.606',.3,-25,40,1],['5.607',.2,0,40,2],
  ['5.619',3,-8,2,1]])near(graphAreas(id,xmax,ymin,ymax)[0]/divisor,fy.get(id).rättSvar);
 const [a,b]=graphAreas('5.603',.4,0,20,230);near(a,4);near(b,4);
 const [wa,wb]=graphAreas('5.620',4,0,40,230);near(wa,80);near(wb,80);
});
test('Energijämförelser använder kvadrerad fart och en fullständig energibalans',()=>{
 for(const [id,answer] of [
  ['5.609',4/2],['5.610',(4/2)**2],['5.611',60-15],['5.612',20-5],
  ['5.613',180-30],['5.614',80-25],['5.615',36*(3/6)**2],
  ['5.616',20+30-10],['5.617',Math.sqrt(2*32/4)],['5.621',0],['5.622',20*(5-2)]])
  near(fy.get(id).rättSvar,answer);
});
test('Tryckuppgifterna skiljer totalarea, areaförhållande och trycköverföring',()=>{
 for(const [id,answer] of [
  ['6.550',12/.04],['6.551',600/.12],['6.552',1000/200],['6.553',2],
  ['6.554',10000*.03],['6.555',100/500],['6.556',(20/.01)*.10]])near(fy.get(id).rättSvar,answer);
});
test('Uppräkning visar skillnaden mellan koder med och utan upprepning',()=>{
 const all=[],distinct=[];
 for(const a of [1,2,3])for(const b of [1,2,3]){all.push(`${a}${b}`);if(a!==b)distinct.push(`${a}${b}`);}
 assert.equal(all.length,9);assert.equal(distinct.length,ma.get('1.796').rättSvar);
 assert.match(ma.get('1.795').alternativ.find(a=>a.ratt).txt,/3\^2/);
});
test('Grupper, rollfördelningar och dubbelräknade par kontrolleras genom uppräkning',()=>{
 const groups=new Set(),roles=[];
 for(let a=0;a<6;a++)for(let b=0;b<6;b++)for(let c=0;c<6;c++)
  if(new Set([a,b,c]).size===3){roles.push([a,b,c]);groups.add([a,b,c].sort().join(','));}
 assert.equal(groups.size,20);assert.equal(roles.length,120);
 assert.match(ma.get('1.792').alternativ.find(a=>a.ratt).txt,/binom63/);
 assert.match(ma.get('1.793').alternativ.find(a=>a.ratt).txt,/6\\cdot5\\cdot4/);
 const pairs=new Set();for(let a=0;a<4;a++)for(let b=0;b<4;b++)if(a!==b)pairs.add([a,b].sort().join(','));
 assert.equal(pairs.size,ma.get('1.794').rättSvar);
 const withAlva=new Set();for(let a=1;a<5;a++)for(let b=1;b<5;b++)if(a!==b)withAlva.add([0,a,b].sort().join(','));
 assert.equal(withAlva.size,ma.get('1.799').rättSvar);
});
test('Sannolikheten för två röda kontrolleras med alla ordnade drag utan återläggning',()=>{
 const balls=['R1','R2','B1','B2'];let all=0,favorable=0;
 for(const a of balls)for(const b of balls)if(a!==b){all++;if(a[0]==='R'&&b[0]==='R')favorable++;}
 assert.equal(all,12);assert.equal(favorable,2);
 const q=ma.get('1.801'),[n,d]=q.rättSvar.split('/').map(Number);
 near(n/d,favorable/all);assert.equal(q.svarFormat,'sannolikhet');
});
test('De nya introduktionsuppgifterna har ett entydigt svar och håller sig på nivå 1–2',()=>{
 const qs=[...Array.from({length:22},(_,i)=>fy.get(`5.${601+i}`)),...Array.from({length:8},(_,i)=>fy.get(`6.${549+i}`)),...Array.from({length:10},(_,i)=>ma.get(`1.${792+i}`)),...Array.from({length:4},(_,i)=>fy.get(`4.${754+i}`))];
 assert.equal(qs.length,44);
 for(const q of qs){assert.ok(q);assert.equal(q.niva,'E');assert.ok([1,2].includes(q.traningsniva));
  if(q.svarstyp==='alternativ')assert.equal(q.alternativ.filter(a=>a.ratt).length,1);
  else assert.notEqual(q.rättSvar,null);
 }
});

test('Newtons tredje lag visar lika stora, motsatta krafter på olika föremål',()=>{
 assert.equal(fy.get('4.755').rättSvar,20);
 for(const id of ['4.754','4.755','4.756','4.757']){
  const q=fy.get(id);
  assert.match(q.t,/B på A/);assert.match(q.t,/A på B/);
  assert.match(q.t,/x1="110" y1="90" x2="35" y2="90"/);
  assert.match(q.t,/x1="350" y1="90" x2="425" y2="90"/);
 }
 assert.match(fy.get('4.756').alternativ.find(a=>a.ratt).txt,/olika vagnar/);
 assert.ok(8/2>8/4);assert.equal(fy.get('4.757').alternativ.find(a=>a.ratt).txt,'Vagn A.');
});
test('Seriekopplingskort använder egna data och rättar båda effekterna i ordnade fält',()=>{
 const a=fy.get('8.40'),b=fy.get('8.124');
 near(a.rättSvar[0],220+330);near(a.rättSvar[1],11/(220+330)*1000);near(a.rättSvar[3],11*.020);
 near(b.rättSvar[1],120+180);near(b.rättSvar[2],9/(120+180));
 near(220*.020**2,.088);near(330*.020**2,.132);
 assert.match(a.spelDelar[2].t,/0,020 A/);assert.match(a.spelDelar[2].s,/0\{,\}088/);assert.match(a.spelDelar[2].s,/0\{,\}132/);
 assert.equal(a.självrättning[2],true);assert.equal(b.självrättning[0],true);
 assert.equal(a.rättSvar[2].length,2);near(a.rättSvar[2][0],.088);near(a.rättSvar[2][1],.132);
 assert.equal(a.spelDelar[2].svarsstruktur,'ordnad');
 assert.deepEqual(Array.from(a.spelDelar[2].svarEtiketter),['220 Ω','330 Ω']);
 assert.match(a.spelDelar[1].t,/550 Ω/);assert.match(b.spelDelar[2].t,/300 Ω/);
 assert.deepEqual(Array.from(a.spelDelar,d=>d.traningsniva),[1,2,2,1]);assert.deepEqual(Array.from(b.spelDelar,d=>d.traningsniva),[1,1,1]);
});
