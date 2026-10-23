const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('fs'),vm=require('vm'),path=require('path');
const c={window:{}};vm.runInNewContext(fs.readFileSync(path.join(__dirname,'../uppgiftermato1.js'),'utf8'),c);const bank=c.window.BANKMATO1,q=id=>bank.find(q=>q.id===id),ids=Array.from({length:6},(_,i)=>'4.'+(520+i));
const near=(a,b)=>assert.ok(Math.abs(a-b)<1e-8,`${a} != ${b}`),cos=d=>Math.cos(d*Math.PI/180);
test('Cosinussamband, trubbiga vinklar och omvända problem',()=>{
 near(q('4.521').rättSvar**2,25+9-30*cos(120));near(cos(q('4.523').rättSvar),(25+49-100)/70);
 near(q('4.524').rättSvar**2+36,(64+100)/2);near(q('4.525').rättSvar**2*(2-2*cos(120)),144);
 assert.ok(50-50*cos(100)>50-50*cos(40));assert.match(q('4.522').alternativ.find(a=>a.ratt).txt,/y\\gt x/);
 assert.equal(q('4.523').tolerans,.05);assert.equal(q('4.524').tolerans,.005);assert.equal(q('4.525').tolerans,.005);
});
test('SVG-vinklar, sidförhållanden och diagonaler mäts från koordinaterna',()=>{
 let n=0;for(const id of ids)for(const m of q(id).t.matchAll(/<polygon data-geometry="triangle"[^>]+>/g)){
  const tag=m[0],attr=k=>tag.match(new RegExp(k+'="([^"]+)"'))[1],a=+attr('data-side-a'),b=+attr('data-side-b'),angle=+attr('data-angle');
  const [A,B,C]=attr('points').split(' ').map(p=>p.split(',').map(Number)),u=B.map((v,i)=>v-A[i]),v=C.map((x,i)=>x-A[i]),la=Math.hypot(...u),lb=Math.hypot(...v);
  near(la/lb,a/b);near(Math.acos((u[0]*v[0]+u[1]*v[1])/(la*lb))*180/Math.PI,angle);
  const actual=Math.hypot(B[0]-C[0],B[1]-C[1])/(la/a);near(actual**2,a*a+b*b-2*a*b*cos(angle));n++;
 }assert.equal(n,6);
 const comparison=[...q('4.522').t.matchAll(/<polygon[^>]+points="([^"]+)"/g)].map(m=>m[1].split(' ').map(p=>p.split(',').map(Number)));
 near(Math.hypot(comparison[0][1][0]-comparison[0][0][0],comparison[0][1][1]-comparison[0][0][1]),Math.hypot(comparison[1][1][0]-comparison[1][0][0],comparison[1][1][1]-comparison[1][0][1]));
 for(const id of ids){const polygons=[...q(id).t.matchAll(/<polygon data-geometry="triangle"[^>]+>/g)],arcs=[...q(id).t.matchAll(/<path data-angle-arc="([^"]+)" d="([^"]+)"/g)];assert.equal(arcs.length,polygons.length);arcs.forEach((m,i)=>{const A=polygons[i][0].match(/points="([^ ,]+),([^ ]+)/).slice(1).map(Number),v=m[2].match(/-?\d+(?:\.\d+)?(?:e-?\d+)?/g).map(Number),end=v.slice(-2);near(Math.hypot(v[0]-A[0],v[1]-A[1]),27);near(Math.hypot(end[0]-A[0],end[1]-A[1]),27);near(Math.atan2(A[1]-end[1],end[0]-A[0])*180/Math.PI,+m[1]);});}
 const tag=q('4.524').t.match(/<polygon data-geometry="parallelogram"[^>]+>/)[0],[A,B,C,D]=tag.match(/points="([^"]+)"/)[1].split(' ').map(p=>p.split(',').map(Number)),len=(p,r)=>Math.hypot(p[0]-r[0],p[1]-r[1]),scale=len(A,B)/6;
 near(len(A,C)/scale,10);near(len(B,D)/scale,8);near(len(A,D)/scale,Math.sqrt(46));near(len(B,C),len(A,D));
});
test('Sex figurkort endast för Ma3c: nivå, svarsenhet och verktyg',()=>{
 const levels={1:0,2:0,3:0};for(const id of ids){const t=q(id);levels[t.traningsniva]++;assert.equal(t.omr,'cosinussatsen');assert.equal(t.kap,4);assert.deepEqual(Array.from(t.kurs),['1c']);assert.equal(t.spel,true);assert.equal(t.självrättning,true);assert.equal(t.miniräknare,true);assert.equal(t.geogebra,false);assert.match(t.s,/facit-svar/);assert.match(t.t,/<svg /);assert.doesNotMatch(t.t+t.s,/[\u0000-\u0008\u000b-\u001f]|<p><\/p>/);}
 assert.deepEqual(levels,{1:2,2:2,3:2});assert.equal(new Set(bank.map(q=>q.id)).size,bank.length);
});
