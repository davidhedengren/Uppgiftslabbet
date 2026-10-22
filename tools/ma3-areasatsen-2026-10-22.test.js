const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('fs'),vm=require('vm'),path=require('path');
const c={window:{}};vm.runInNewContext(fs.readFileSync(path.join(__dirname,'../uppgiftermato1.js'),'utf8'),c);const bank=c.window.BANKMATO1,q=id=>bank.find(q=>q.id===id),ids=Array.from({length:8},(_,i)=>'4.'+(512+i));
const sin=d=>Math.sin(d*Math.PI/180),near=(a,b)=>assert.ok(Math.abs(a-b)<1e-8,`${a} ≠ ${b}`);
test('Areor, jämförelser och vinkelberäkning stämmer',()=>{
 near(7*12*sin(30)/2,q('4.513').rättSvar);near((4*6*sin(60)/2)/(4*3*sin(60)/2),q('4.514').rättSvar);near(6*6*sin(60)/2,6*6*sin(120)/2);
 near(58/2,q('4.516').rättSvar);near(12*5-8*6*sin(30)/2,q('4.518').rättSvar);near(6*6*sin(180-75-75)/2,q('4.519').rättSvar);
 assert.equal(q('4.517').rättSvar,90);for(let v=0;v<=180;v++)assert.ok(30*sin(v)<=30);
 assert.match(q('4.512').alternativ.find(a=>a.ratt).txt,/sin50/);assert.equal(q('4.515').alternativ.find(a=>a.ratt).txt,'Trianglarna har lika stor area.');
});
test('SVG-trianglarnas faktiska vinklar och sidförhållanden stämmer',()=>{
 let count=0;for(const id of ids)for(const m of q(id).t.matchAll(/<polygon data-geometry="triangle"[^>]+>/g)){
  const tag=m[0],attr=n=>tag.match(new RegExp(n+'="([^"]+)"'))[1],a=+attr('data-side-a'),b=+attr('data-side-b'),deg=+attr('data-angle');
  const [A,B,C]=attr('points').split(' ').map(p=>p.split(',').map(Number)),u=B.map((v,i)=>v-A[i]),v=C.map((v,i)=>v-A[i]),la=Math.hypot(...u),lb=Math.hypot(...v);
  near(la/lb,a/b);near(Math.acos((u[0]*v[0]+u[1]*v[1])/(la*lb))*180/Math.PI,deg);
  const actualArea=Math.abs(u[0]*v[1]-u[1]*v[0])/2/(la/a)**2;near(actualArea,a*b*sin(deg)/2);count++;
 }assert.equal(count,7);
 const tag=q('4.519').t.match(/<polygon data-geometry="isosceles"[^>]+>/)[0],[A,B,C]=tag.match(/points="([^"]+)"/)[1].split(' ').map(p=>p.split(',').map(Number)),u=B.map((v,i)=>v-A[i]),v=C.map((v,i)=>v-A[i]);near(Math.hypot(...u),Math.hypot(...v));near(Math.acos((u[0]*v[0]+u[1]*v[1])/(Math.hypot(...u)*Math.hypot(...v)))*180/Math.PI,30);
 assert.doesNotMatch(q('4.513').t,/cm/);assert.match(q('4.513').t,/12 m/);
});
test('Alla kort har figur, rätt spår, nivå, enhet och verktyg',()=>{
 const levels={1:0,2:0};for(const id of ids){const t=q(id);levels[t.traningsniva]++;assert.equal(t.omr,'areasatsen');assert.equal(t.kap,4);assert.deepEqual(Array.from(t.kurs),['1c']);assert.equal(t.spel,true);assert.equal(t.självrättning,true);assert.equal(t.miniräknare,true);assert.equal(t.geogebra,false);assert.match(t.t,/<svg /);assert.match(t.s,/facit-svar/);assert.doesNotMatch(t.t+t.s,/[\u0000-\u0008\u000b-\u001f]|<p><\/p>/);}
 assert.deepEqual(levels,{1:5,2:3});assert.equal(q('4.514').svarFormat,'multipel');assert.equal(q('4.517').svarEnhet,'°');assert.equal(new Set(bank.map(q=>q.id)).size,bank.length);
});
