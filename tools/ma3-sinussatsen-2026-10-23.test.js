const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('fs'),vm=require('vm'),path=require('path');
const c={window:{}};vm.runInNewContext(fs.readFileSync(path.join(__dirname,'../uppgiftermato1.js'),'utf8'),c);const bank=c.window.BANKMATO1,q=id=>bank.find(q=>q.id===id),ids=Array.from({length:6},(_,i)=>'4.'+(526+i));
const sin=d=>Math.sin(d*Math.PI/180),near=(a,b)=>assert.ok(Math.abs(a-b)<1e-8,`${a} != ${b}`);
test('Sinussamband, takhöjd och skillnad mellan sidor räknas oberoende',()=>{
 assert.equal(q('4.526').alternativ.find(a=>a.ratt).txt,'75°');near(q('4.527').rättSvar,12*sin(30));near(q('4.528').rättSvar/sin(75),6/sin(45));
 const cot=d=>1/Math.tan(d*Math.PI/180);near(q('4.529').rättSvar,10/(cot(40)+cot(60)));
 const a=q('4.530').rättSvar;near((a+4)/sin(60),a/sin(30));assert.match(q('4.531').alternativ.find(a=>a.ratt).txt,/1,81/);near(Math.round(sin(50)/sin(25)*100)/100,1.81);
 for(const id of ['4.528','4.529','4.530'])assert.equal(q(id).tolerans,.005);
});
test('Verkliga SVG-vinklar, bågändpunkter, sidförhållanden och höjd är korrekta',()=>{
 const angles=[[40,65,75],[45,30,105],[45,75,60],[40,60,80],[30,60,90],[25,50,105]];
 ids.forEach((id,k)=>{const tag=q(id).t.match(/<polygon data-geometry="triangle"[^>]+>/)[0],attr=n=>tag.match(new RegExp(n+'="([^"]+)"'))[1],pts=attr('points').split(' ').map(p=>p.split(',').map(Number)),len=(p,r)=>Math.hypot(p[0]-r[0],p[1]-r[1]);
  for(let i=0;i<3;i++){const P=pts[i],u=pts[(i+1)%3].map((x,j)=>x-P[j]),v=pts[(i+2)%3].map((x,j)=>x-P[j]);near(Math.acos((u[0]*v[0]+u[1]*v[1])/(Math.hypot(...u)*Math.hypot(...v)))*180/Math.PI,angles[k][i]);}
  near(len(pts[0],pts[1])/len(pts[0],pts[2]),+attr('data-side-a')/+attr('data-side-b'));
  for(const m of q(id).t.matchAll(/<path data-vertex="(\d)" data-angle-arc="([^"]+)" d="([^"]+)"/g)){const i=+m[1],P=pts[i],nums=m[3].match(/-?\d+(?:\.\d+)?(?:e-?\d+)?/g).map(Number),start=nums.slice(0,2),end=nums.slice(-2);near(len(P,start),24);near(len(P,end),24);const u=start.map((x,j)=>x-P[j]),v=end.map((x,j)=>x-P[j]);near(Math.acos((u[0]*v[0]+u[1]*v[1])/576)*180/Math.PI,angles[k][i]);const U=pts[(i+1)%3],V=pts[(i+2)%3];near((U[0]-P[0])*u[1]-(U[1]-P[1])*u[0],0);near((V[0]-P[0])*v[1]-(V[1]-P[1])*v[0],0);}
  if(id==='4.529'){const d=q(id).t.match(/data-altitude="true" d="([^"]+)"/)[1].match(/-?\d+(?:\.\d+)?/g).map(Number);near(d[0],d[2]);near(d[0],pts[2][0]);near(d[1],pts[2][1]);near(d[3],pts[0][1]);near((d[3]-d[1])/(len(pts[0],pts[1])/10),q(id).rättSvar);}
 });
});
test('Sex fristående figurkort i rätt spår och nivå, med miniräknare',()=>{
 const levels={1:0,2:0,3:0};for(const id of ids){const t=q(id);levels[t.traningsniva]++;assert.equal(t.omr,'sinussatsen');assert.equal(t.kap,4);assert.deepEqual(Array.from(t.kurs),['1c']);assert.equal(t.spel,true);assert.equal(t.självrättning,true);assert.equal(t.miniräknare,true);assert.equal(t.geogebra,false);assert.match(t.s,/facit-svar/);assert.match(t.t,/<svg /);assert.doesNotMatch(t.t+t.s,/[\u0000-\u0008\u000b-\u001f]|<p><\/p>/);}
 assert.deepEqual(levels,{1:2,2:2,3:2});assert.equal(new Set(bank.map(q=>q.id)).size,bank.length);
});
