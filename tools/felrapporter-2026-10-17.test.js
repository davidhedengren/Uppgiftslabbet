'use strict';
const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('node:fs'),vm=require('node:vm');
const c={window:{}};vm.runInNewContext(fs.readFileSync(__dirname+'/../uppgiftermato1.js','utf8'),c);
const bank=JSON.parse(JSON.stringify(c.window.BANKMATO1)),report=JSON.parse(fs.readFileSync(__dirname+'/../agent/FELRAPPORTER_2026-10-17_1917.json','utf8'));
const q=id=>{const task=bank.find(q=>q.id===id);assert.ok(task,id);return task;};
const close=(a,b,tol=1e-6)=>assert.ok(Math.abs(a-b)<=tol,`${a} != ${b}`);
const coords=s=>s.trim().split(/\s+/).map(x=>x.split(',').map(Number));
const svg=id=>q(id).t.match(/<svg[\s\S]*?<\/svg>/)[0];
test('Minimering kräver alla olikheter samtidigt; origo är inte tillåtet',()=>{
 for(const [id,coeff,points,least]of [['4.257',[4,5],[[0,15],[18/5,21/5],[12,0]],35.4],['4.260',[28,24],[[0,12],[21/5,18/5],[15,0]],204]]){
  assert.match(q(id).t,/alla följande villkor gäller samtidigt/);assert.match(q(id).s,/inte tillåtet/);
  const feasible=(x,y)=>x>=0&&y>=0&&(id==='4.257'?x+2*y>=12-1e-9&&3*x+y>=15-1e-9:2*x+y>=12-1e-9&&x+3*y>=15-1e-9);
  assert.equal(feasible(0,0),false);assert.ok(points.every(p=>feasible(...p)));close(Math.min(...points.map(([x,y])=>coeff[0]*x+coeff[1]*y)),least);close(q(id).rättSvar,least);
  assert.match(svg(id),/fill-opacity="\.08"/);
 }
});
test('Tidigare rättade 5,6 år bevaras; andraderivatans korrekta avrundning är 10,9',()=>{
 const a=q('2.321');close(a.rättSvar,Math.log(150/96)/.08);assert.equal(a.tolerans,.05);assert.ok(Math.abs(5.6-a.rättSvar)<=a.tolerans);assert.ok(Math.abs(6-a.rättSvar)>a.tolerans);
 const b=q('2.346');close(b.rättSvar,9*Math.log(3)**2);assert.match(b.t,/en decimal/);assert.equal(b.tolerans,.05);assert.ok(Math.abs(10.9-b.rättSvar)<b.tolerans);assert.ok(Math.abs(10.8-b.rättSvar)>b.tolerans);
 assert.equal(b.geogebra,true);assert.equal(b.miniräknare,true);
 assert.match(q('2.318').t,/endast ekvationen/);assert.equal(q('2.318').svarstyp,'uttryck');assert.equal(q('2.318').geogebra,true);
});
test('Tangenter från (0, −4) hör till x², utan den gamla oavsiktliga förskjutningen',()=>{
 const task=q('2.317');assert.match(task.t,/f\(x\)=x\^2/);assert.doesNotMatch(task.s,/sqrt5|sqrt\s*5|a\^2\+1/);
 for(const a of [-2,2]){const slope=2*a,intercept=-a*a;close(slope*a+intercept,a*a);close(intercept,-4);}
 assert.ok(task.s.includes('(−2, 4)')&&task.s.includes('(2, 4)'));
 for(const id of ['2.316','2.317','2.318','2.349']){assert.equal(q(id).geogebra,true,id);assert.equal(q(id).miniräknare,true,id);}
 assert.doesNotMatch(q('2.323').ledtrad,/tröskel|tidpunkt/);
});
test('Varierade area- och cosinusuppgifter har rätt numeriskt mål, precision och verktyg',()=>{
 for(const [id,a,b,angle]of [['4.438',8,5,50],['4.450',8,7,120],['4.462',8,3,40],['4.467',4,3,150]]){
  const t=q(id);close(t.rättSvar,a*b*Math.sin(angle*Math.PI/180)/2);assert.equal(t.tolerans,.05);assert.equal(t.traningsniva,2);assert.equal(t.miniräknare,true);assert.equal(t.geogebra,false);assert.equal(t.svarEnhet,'cm²');assert.ok(t.t.includes(String(angle)+'^\\circ'));
 }
 close(q('4.463').rättSvar,Math.sqrt(117));assert.equal(q('4.463').tolerans,.05);assert.equal(q('4.463').traningsniva,2);
});
test('Trianglarnas ritade vinklar stämmer och vinkeltexterna ligger inne i triangeln',()=>{
 let n=0;
 for(const [id,g]of Object.entries(report.geometry))if(g.type==='triangle'){
  const s=svg(id),p=coords(s.match(/<polygon points="([^"]+)"/)[1]);assert.equal(p.length,3);n++;
  assert.match(s,/fill-opacity="0.06" stroke="currentColor" stroke-width="2.2"/);
  for(const [vertex,label]of Object.entries(g.angles)){
   const i='ABC'.indexOf(vertex),v=p[i],u=p[(i+1)%3].map((x,j)=>x-v[j]),w=p[(i+2)%3].map((x,j)=>x-v[j]);const angle=Math.acos((u[0]*w[0]+u[1]*w[1])/Math.hypot(...u)/Math.hypot(...w))*180/Math.PI;
   if(label.endsWith('°'))close(angle,Number(label.slice(0,-1)),.003);
   if(label==='90°'){assert.match(s,/<polyline/);continue;}
   const matching=[...s.matchAll(/<text x="([^"]+)" y="([^"]+)"[^>]*>([^<]+)<\/text>/g)].filter(x=>x[3]===label);assert.ok(matching.length,id+label);
   const inside=matching.some(m=>{const t=[Number(m[1]),Number(m[2])];const signs=p.map((a,j)=>{const b=p[(j+1)%3];return (b[0]-a[0])*(t[1]-a[1])-(b[1]-a[1])*(t[0]-a[0]);});return Math.min(...signs)>=-.01||Math.max(...signs)<=.01;});assert.ok(inside,id+label);
  }
 }
 assert.equal(n,26);for(const id of Object.keys(report.geometry))assert.match(svg(id),/color:#243247/);for(const id of ['4.430','4.431','4.435','4.439','4.443','4.449','4.451','4.463'])assert.ok(!svg(id).includes('M55 155 L265 155 L205 45 Z'));
});
test('Sjutton ritade tangenter möter rätt kurva med rätt lutning och kontaktpunkt',()=>{
 let n=0;
 for(const [id,g]of Object.entries(report.geometry))if(g.type==='tangent'){
  n++;const s=svg(id),polys=[...s.matchAll(/<polyline points="([^"]+)"/g)].map(m=>coords(m[1]));assert.equal(polys.length,2,id);
  const world=([X,Y])=>[g.xmin+(X-65)/g.sx,g.ymin+(255-Y)/g.sy],line=polys[1].map(world),slope=(line[1][1]-line[0][1])/(line[1][0]-line[0][0]);close(slope,g.k,.001);
  const t=q(id).t,match=t.match(/f\(x\)=([0-9]*)x\^2([+-][0-9]+)/);
  if(match){const a=Number(match[1]||1),c=Number(match[2]);close(g.k,2*a*g.x0);close(g.k*g.x0+g.m,a*g.x0*g.x0+c);for(const pixel of polys[0]){const [x,y]=world(pixel);close(y,a*x*x+c,.003);}}
  assert.ok(g.ymin<=0&&g.ymax>=0,id);assert.ok(!s.includes('M70 140 Q160 25 255 125'));
 }
 assert.equal(n,17);
});
test('Studskurvor når marken mellan varje båge och behåller höjdkvoten 0,7',()=>{
 for(const id of ['4.75','4.231']){
  const hops=[...svg(id).matchAll(/d="M([\d.]+) 210 Q([\d.]+) (-?[\d.]+) ([\d.]+) 210"/g)];assert.equal(hops.length,5);
  const h=hops.map(m=>210-(210+Number(m[3]))/2);for(let i=1;i<h.length;i++)close(h[i]/h[i-1],.7,.00002);
 }assert.equal((q('4.231').t.match(/En boll släpps/g)||[]).length,1);
});
