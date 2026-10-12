'use strict';
const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('node:fs'),vm=require('node:vm'),path=require('node:path');
const c={window:{}};vm.runInNewContext(fs.readFileSync(path.join(__dirname,'../uppgifter.js'),'utf8'),c);
const ids=Array.from({length:15},(_,i)=>`3.${410+i}`),tasks=ids.map(id=>c.window.BANK.find(q=>q.id===id));
const q=id=>tasks.find(x=>x.id===id);
test('15 unika uppgifter: elva spelbara och fyra ritningsuppgifter endast i labbet',()=>{
 assert.equal(new Set(c.window.BANK.map(q=>q.id)).size,c.window.BANK.length);
 assert.ok(tasks.every(Boolean));assert.equal(tasks.filter(q=>q.spel).length,11);
 for(const t of tasks){assert.equal(t.miniräknare,true);assert.equal(t.kap,3);}
 for(const id of ['3.421','3.422','3.423','3.424']){
  const t=q(id);assert.equal(t.spel,false);assert.equal(t.självrättning,false);
  assert.equal(t.rättSvar,null);assert.doesNotMatch(t.t,/data-tangent/);assert.match(t.s,/data-tangent/);
 }
 for(const id of ['3.418','3.419','3.420'])assert.doesNotMatch(q(id).t,/<svg/);
});
test('Numeriska slutsvar följer koordinatskillnader med rätt tecken och enheter',()=>{
 const rows=[['3.410',(8-2)/(4-1),'m/s'],['3.411',(6-14)/(5-1),'m/s'],['3.412',0,'m/s'],
 ['3.413',(14-2)/(5-2),'m/s²'],['3.414',(2-14)/(6-3),'m/s²'],['3.416',(8-2)/(4-2),'m/s'],
 ['3.417',((36-7.2)/3.6)/(6-2),'m/s²'],['3.418',(9.61-8.41)/(3.1-2.9),'m/s'],['3.419',(2-7)/(3.5-1.5),'m/s²']];
 for(const[id,expected,unit]of rows){assert.ok(Math.abs(q(id).rättSvar-expected)<1e-10,id);assert.equal(q(id).svarEnhet,unit);}
 for(const id of ['3.415','3.420'])assert.equal(q(id).alternativ.filter(a=>a.ratt).length,1);
 assert.ok(q('3.415').alternativ.find(a=>a.ratt).txt.includes('0 m/s²'));
 assert.match(q('3.420').alternativ.find(a=>a.ratt).txt,/Nej/);
});
// Independent analytic models used to check the actual SVG path and tangent,
// not merely answer metadata. Coordinates: plot (60,40)–(436,280).
const models=[
 ['3.410',6,0,20,t=>2+t*t/2,2,2],['3.411',5,0,18,t=>14-t*t/2,2,-2],
 ['3.412',6,0,12,t=>12-(t-3)**2,3,0],['3.413',6,0,20,t=>2+t*t/2,4,4],
 ['3.414',6,0,20,t=>18-t*t/2,4,-4],['3.415',4,0,8,t=>3+4*t-t*t,2,0],
 ['3.416',4,0,16,t=>t**3/4,2,3],['3.417',6,0,43.2,t=>7.2+.9*t*t,4,7.2],
 ['3.421',6,0,20,t=>20*(1-Math.exp(-t/2)),2,10/Math.E],
 ['3.422',5,0,16,t=>t**3/8,4,6],['3.423',6,-8,2,t=>-8+(t-2)**2/2,4,2],
 ['3.424',6,0,20,t=>2+t*t/2,4,4],['3.424',6,0,20,t=>8+t*t/8,4,1,1]
];
test('Alla diagramkurvor, kontaktpunkter och tangenter är geometriskt korrekta',()=>{
 for(const[id,xmax,ymin,ymax,f,t0,m,figureIndex=0]of models){
  const t=q(id),source=t.spel?t.t:t.s;
  const svg=[...source.matchAll(/<svg\b[\s\S]*?<\/svg>/g)][figureIndex][0];
  const xs=x=>(x-60)*xmax/376,ys=y=>ymin+(280-y)*(ymax-ymin)/240;
  const d=svg.match(/data-curve="0" d="([^"]+)"/)[1];
  const coords=[...d.matchAll(/(?:M|L) ([\d.-]+) ([\d.-]+)/g)];assert.equal(coords.length,241,id);
  for(const [,x,y]of coords)assert.ok(Math.abs(ys(+y)-f(xs(+x)))<.001,`${id}: kurva`);
  const tag=svg.match(/<line[^>]*data-tangent="true"[^>]*>/)[0];
  const attr=name=>+tag.match(new RegExp(`${name}="([^"]+)"`))[1];
  const actual=(ys(attr('y2'))-ys(attr('y1')))/(xs(attr('x2'))-xs(attr('x1')));
  assert.ok(Math.abs(actual-m)<.001,`${id}: tangentlutning`);
  const intercept=ys(attr('y1'))-actual*xs(attr('x1'));
  assert.ok(Math.abs(actual*t0+intercept-f(t0))<.001,`${id}: tangeringspunkt`);
  const point=svg.match(/<circle data-contact="true" cx="([\d.-]+)" cy="([\d.-]+)"/);
  assert.ok(Math.abs(xs(+point[1])-t0)<.001&&Math.abs(ys(+point[2])-f(t0))<.001,`${id}: markerad punkt`);
  const derivative=(f(t0+1e-5)-f(t0-1e-5))/2e-5;
  assert.ok(Math.abs(derivative-m)<1e-6,`${id}: analytisk lutning`);
 }
 // The second cyclist has x=8+t²/8, hence v=1 at t=4, and x=10 for both.
 assert.equal(8+4**2/8,2+4**2/2);assert.equal((4)/(4/4),4);
});
