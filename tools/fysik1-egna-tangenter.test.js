'use strict';
const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('node:fs'),vm=require('node:vm'),path=require('node:path');
const c={window:{}};vm.runInNewContext(fs.readFileSync(path.join(__dirname,'../uppgifter.js'),'utf8'),c);
const ids=Array.from({length:15},(_,i)=>`3.${425+i}`),q=id=>c.window.BANK.find(q=>q.id===id);
const f425=t=>t*t/4+t/2,f426=t=>30-t*t/2,f427=t=>6+3*t-t*t/4,f428=t=>2+t**3/8,f429=t=>(t-3)**3/4;
const f430=t=>2+2*t-t*t/8,f431=t=>12/(1+t/4),f432=t=>1+9.82*t-4.91*t*t,f433=t=>t*t*(6-t)/4;
const f434=t=>2+t*t/4,h434=t=>10+t*t/16,f435=t=>.5-2.5*Math.tanh((t-20)/4),f436=t=>24-t*t/5;
const f437=t=>t**3/12+2*t,f438=t=>t*t/2,h438=t=>30*t*t,f439=t=>4*Math.sin(Math.PI*t/4);
// Axis ranges and physical models are independently stated; they are not read from answer HTML.
const model=(xmax,min,max,f,extra=null)=>({xmax,min,max,f,extra});
const specs={
 '3.425':[model(8,0,20,f425)],'3.426':[model(6,0,32,f426)],'3.427':[model(8,0,16,f427)],
 '3.428':[model(6,0,32,f428)],'3.429':[model(6,-8,8,f429)],'3.430':[model(8,0,12,f430)],
 '3.431':[model(12,0,12,f431)],'3.432':[model(2,0,6,f432)],'3.433':[model(6,0,10,f433)],
 '3.434':[model(8,0,20,f434,h434),model(8,0,20,h434)],'3.435':[model(40,-3,4,f435)],
 '3.436':[model(10,0,25,f436)],'3.437':[model(6,0,32,f437)],
 '3.438':[model(6,0,20,f438),model(3,0,300,h438)],'3.439':[model(8,-4,4,f439)]
};
test('15 självständiga läraruppgifter med rutnät och egen tangentritning, samtliga uteslutna ur spel',()=>{
 assert.equal(new Set(c.window.BANK.map(q=>q.id)).size,c.window.BANK.length);
 const levels={};for(const id of ids){const t=q(id);assert.ok(t,id);assert.equal(t.kap,3);
  assert.equal(t.spel,false,id);assert.equal(t.självrättning,false);assert.equal(t.rättSvar,null);
  assert.equal(t.manuellKomplettering,true);assert.equal(t.miniräknare,true);
  assert.doesNotMatch(t.t,/data-tangent|Tangent<\/text>/);assert.match(t.s,/data-tangent/);
  assert.ok((t.t.match(/data-grid="time"/g)||[]).length>=9,id);
  assert.ok((t.t.match(/data-grid="value"/g)||[]).length>=11,id);
  levels[t.traningsniva]=(levels[t.traningsniva]||0)+1;
 }assert.deepEqual(levels,{2:5,3:6,4:2,5:2});
});
test('Varje kurva, markerad tidpunkt och lösningstangent följer sin fysikmodell och axelskala',()=>{
 let count=0;
 for(const id of ids)for(const field of ['t','s']){
  const figures=[...q(id)[field].matchAll(/<svg\b[\s\S]*?<\/svg>/g)].map(m=>m[0]);
  for(let i=0;i<figures.length;i++){
   count++;const svg=figures[i],spec=specs[id][id==='3.438'||(id==='3.434'&&field==='s')?i:0];
   assert.ok(spec,`${id} ${field} ${i}`);
   const x=p=>(p-72)*spec.xmax/480,y=p=>spec.min+(342-p)*(spec.max-spec.min)/288;
   for(const match of svg.matchAll(/data-curve="(\d+)" d="([^"]+)"/g)){
    const fn=match[1]==='0'?spec.f:spec.extra;assert.ok(fn,id);
    const coords=[...match[2].matchAll(/(?:M|L) ([\d.-]+) ([\d.-]+)/g)];assert.equal(coords.length,301,id);
    for(const[,px,py]of coords)assert.ok(Math.abs(y(+py)-fn(x(+px)))<.002,`${id}: kurva ${i}`);
   }
   for(const [,t,px,py]of svg.matchAll(/data-contact="([\d.-]+)" cx="([\d.-]+)" cy="([\d.-]+)"/g)){
    assert.ok(Math.abs(x(+px)-t)<.001&&Math.abs(y(+py)-spec.f(+t))<.002,`${id}: punkt`);
   }
   for(const tag of svg.match(/<line[^>]*data-tangent[^>]*>/g)||[]){
    const a=name=>+tag.match(new RegExp(`${name}="([^"]+)"`))[1];
    const t=a('data-tangent'),m=(y(a('y2'))-y(a('y1')))/(x(a('x2'))-x(a('x1')));
    const derivative=(spec.f(t+1e-5)-spec.f(t-1e-5))/2e-5;
    assert.ok(Math.abs(m-derivative)<.002,`${id}: lutning ${t}`);
    assert.ok(Math.abs(y(a('y1'))+m*(t-x(a('x1')))-spec.f(t))<.002,`${id}: kontakt ${t}`);
   }
  }
 }assert.equal(count,38);
});
test('Fysik och enhetsbyten i de svårare uppgifterna håller',()=>{
 const acceleration=(-2-3)/((24-16)*1e-3);assert.equal(acceleration,-625);assert.equal(.2*acceleration,-125);
 assert.equal(-.4*6.25,-2.5);assert.ok(-.4*7<-2.5&&-.4*6>-2.5);
 const threshold=Math.sqrt(76/3);assert.ok(threshold>5&&threshold<5.1);assert.ok(6-threshold>.9&&6-threshold<1);
 assert.ok(Math.abs((5.5**2/4+2)*3.6-34.425)<1e-10);assert.equal((f437(6)-f437(0))/6*3.6,18);
 assert.equal(120/60,2);assert.equal(4/(120/60),2);
 const velocity=t=>Math.PI*Math.cos(Math.PI*t/4);
 assert.ok(Math.abs(velocity(3.5)-velocity(4.5))<1e-12);
 assert.ok(Math.abs(velocity(3.5)+2.9)<.01);
 assert.match(q('3.439').s,/bevisar inte ensamma/);
 assert.match(q('3.429').s,/passerar markeringen/);
});
