const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('fs'),vm=require('vm'),path=require('path');
const c={window:{}};vm.runInNewContext(fs.readFileSync(path.join(__dirname,'../uppgiftermato1.js'),'utf8'),c);const bank=c.window.BANKMATO1,q=id=>bank.find(q=>q.id===id),ids=Array.from({length:9},(_,i)=>'2.'+(1176+i));
test('Förändringskvoter och okända värden kontrolleras oberoende',()=>{
 assert.match(q('2.1176').alternativ.find(a=>a.ratt).txt,/24-12.*6-2/);assert.equal((24-12)/(6-2),3);
 assert.equal(q('2.1177').alternativ.find(a=>a.ratt).txt,'kr/km');
 assert.equal(q('2.1178').rättSvar,(4-10)/(4-1));assert.equal(q('2.1179').rättSvar,(8-11)/(8-7));
 assert.ok(12/4>15/6);assert.match(q('2.1180').alternativ.find(a=>a.ratt).txt,/Planta A/);
 assert.equal((q('2.1181').rättSvar-38)/(5-2),12);
 assert.equal(q('2.1182').rättSvar,(2*3-1*6)/(3+6));
 const a=q('2.1183').rättSvar,f=x=>x*x+a*x;assert.equal((f(4)-f(1))/3,8);
 const b=q('2.1184').rättSvar,g=x=>x*x+2*x;assert.ok(b>1);assert.equal((g(b)-g(1))/(b-1),8);
});
test('Nivå, spår och verktyg passar nio självständiga kort',()=>{
 const levels={1:0,2:0,3:0};for(const id of ids){const t=q(id);levels[t.traningsniva]++;assert.equal(t.omr,'andringskvoter');assert.equal(t.kap,2);assert.deepEqual(Array.from(t.kurs),['1b','1c']);assert.equal(t.spel,true);assert.equal(t.självrättning,true);assert.equal(t.miniräknare,true);assert.equal(t.geogebra,false);assert.match(t.s,/facit-svar/);assert.doesNotMatch(t.t+t.s,/[\u0000-\u0008\u000b-\u001f]|<p><\/p>/);}
 assert.deepEqual(levels,{1:4,2:2,3:3});assert.equal(ids.filter(id=>q(id).t.includes('<svg')).length,3);assert.equal(ids.filter(id=>q(id).t.includes('<table')).length,4);assert.equal(new Set(bank.map(q=>q.id)).size,bank.length);
});
test('De utritade kurvorna följer modellerna, med rätt axelskalor',()=>{
 for(const [id,xmax,ymax,fn] of [['2.1178',5,12,x=>12-2*x],['2.1184',6,50,x=>x*x+2*x]]){
  const paths=[...q(id).t.matchAll(/<path d="([^"]+)"/g)].map(m=>m[1]).filter(d=>d.length>1000);assert.equal(paths.length,1);
  for(const pair of paths[0].slice(1).split(' L')){const [px,py]=pair.split(' ').map(Number),x=(px-60)*xmax/370,y=ymax-(py-42)*ymax/238;assert.ok(Math.abs(y-fn(x))<.0003);}
 }
});
