const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('fs'),vm=require('vm'),path=require('path');
const c={window:{}};vm.runInNewContext(fs.readFileSync(path.join(__dirname,'../uppgiftermato1.js'),'utf8'),c);const bank=c.window.BANKMATO1,q=id=>bank.find(q=>q.id===id),ids=Array.from({length:6},(_,i)=>'3.'+(1201+i));
test('Värde, lutning och andraderivata hålls isär',()=>{
 assert.equal(q('3.1201').rättSvar,(0-2)/(3-1));assert.equal(q('3.1202').rättSvar,(-4-(-4))/(3-1));
 assert.equal(q('3.1203').alternativ.find(a=>a.ratt).txt,'Positivt.');assert.ok((-1-(-3))/4>0);
 assert.equal(q('3.1204').rättSvar,6);const h=.0001,f=x=>x**3-3*x;assert.ok(Math.abs((f(1+h)-2*f(1)+f(1-h))/(h*h)-6)<1e-6);
 assert.equal(q('3.1205').alternativ.find(a=>a.ratt).txt,'x=3');for(const x of [0,1,2,3])assert.equal(3-(x-2)**2>0&&-2*(x-2)<0,x===3);
 assert.match(q('3.1206').alternativ.find(a=>a.ratt).txt,/kan vara negativ/);
 for(const x of [.1,.5,1,1.5,1.9]){assert.ok(2*x-6<0);assert.ok(2*x+1>0);} // Båda förstaderivatorna har derivatan 2.
});
test('Sex fristående kort, rätt nivåer och tillåtna verktyg',()=>{
 const levels={1:0,2:0,3:0};for(const id of ids){const t=q(id);levels[t.traningsniva]++;assert.equal(t.omr,'andraderivatan');assert.equal(t.kap,3);assert.deepEqual(Array.from(t.kurs),['1b','1c']);assert.equal(t.spel,true);assert.equal(t.självrättning,true);assert.equal(t.miniräknare,true);assert.equal(t.geogebra,false);assert.match(t.s,/facit-svar/);assert.match(t.t,/<svg /);assert.doesNotMatch(t.t+t.s,/[\u0000-\u0008\u000b-\u001f]|<p><\/p>/);}
 assert.deepEqual(levels,{1:3,2:1,3:2});assert.equal(new Set(bank.map(q=>q.id)).size,bank.length);
});
test('Alla grafpunkter stämmer med sina axlar och respektive derivata',()=>{
 const models=[['3.1201',0,4,-2,4,x=>3-x],['3.1202',0,4,-6,1,x=>-4],['3.1203',0,4,-4,1,x=>-3+x/2],['3.1204',-2,2,-3,3,x=>x**3-3*x],['3.1205',0,4,-2,4,x=>3-(x-2)**2],['3.1206',0,2,0,3,x=>2]];
 for(const [id,xmin,xmax,ymin,ymax,fn] of models){const paths=[...q(id).t.matchAll(/<path d="([^"]+)"/g)].map(m=>m[1]).filter(d=>d.length>1000);assert.equal(paths.length,1);for(const pair of paths[0].slice(1).split(' L')){const [px,py]=pair.split(' ').map(Number),x=xmin+(px-60)*(xmax-xmin)/370,y=ymax-(py-42)*(ymax-ymin)/238;assert.ok(Math.abs(y-fn(x))<.0001,id);}}
});
