'use strict';
const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('node:fs'),vm=require('node:vm'),path=require('node:path');
const c={window:{}};vm.runInNewContext(fs.readFileSync(path.join(__dirname,'..','uppgifter2.js'),'utf8'),c);const get=id=>c.window.BANK2.find(q=>q.id===id),ids=Array.from({length:16},(_,i)=>'3.'+(516+i)),changed=['3.421',...Array.from({length:6},(_,i)=>'3.'+(435+i)),...Array.from({length:6},(_,i)=>'3.'+(197+i))],near=(a,b)=>assert.ok(Math.abs(a-b)<1e-10*Math.max(1,Math.abs(b)),`${a} != ${b}`);
test('16 unika kort med fullständig metadata och figurer, utan formelledningar',()=>{
 const counts={};for(const id of ids){const q=get(id);assert.ok(q,id);counts[q.traningsniva]=(counts[q.traningsniva]||0)+1;assert.match(q.t,/<svg/);assert.equal(q.miniräknare,true);assert.equal(q.geogebra,false);assert.equal(q.spel,true);assert.equal(q.självrättning,true);assert.match(q.s,/facit-svar/);assert.doesNotMatch(q.s,/facit-steglista/);assert.doesNotMatch(q.t,/e=Blv|F=qvB|Använd .*=/);if(q.alternativ)assert.equal(q.alternativ.filter(a=>a.ratt).length,1);else assert.equal(typeof q.rättSvar,'number');}
 assert.deepEqual(counts,{1:3,2:9,3:4});assert.equal(new Set(ids.map(id=>get(id).t)).size,16);
});
test('Numeriska facit beräknade från modellerna, inklusive nya okända storheter',()=>{
 const expected={'3.516':100*.18/(.4*3),'3.517':.1/(.25*2),'3.519':.3*.4*3,'3.520':(.36-.12)/(.5*.3*.4),'3.523':.6*.12*2.5,'3.524':(.8*.5*3)**2/2*4,'3.525':.4*.25*(5-2)/1.5,'3.528':50*.004/.5,'3.529':.6*.04/(.002*.12),'3.531':2*.2/.5,'3.198':20*.008*.3/.12,'3.421':.8*.5*4*Math.sin(Math.PI/6),'3.436':(1/5)/.4,'3.438':.6*.5*4*Math.sin(Math.PI/6),'3.439':(.5*.4*5)**2/2};
 for(const [id,v]of Object.entries(expected))near(get(id).rättSvar,v);
 assert.equal(get('3.529').tolerans,0);assert.equal(get('3.529').svarVardesiffror,undefined);
});
const correct=id=>get(id).alternativ.filter(a=>a.ratt).map(a=>a.txt).join('|');
test('Begreppsfallen skiljer inducerad spänning, ström, polaritet och flödesändring',()=>{
 assert.match(correct('3.518'),/oförändrad/);assert.match(correct('3.521'),/spänning.*ingen ström/);assert.match(correct('3.522'),/inte ändras/);assert.match(correct('3.526'),/P är fortfarande positiv/);assert.match(correct('3.527'),/Nej.*tvärs/);assert.match(correct('3.530'),/hela ringen/);
 // Två vändningar lämnar magnetiska kraftens riktning oförändrad.
 const cross=(v,b)=>[v[1]*b[2]-v[2]*b[1],v[2]*b[0]-v[0]*b[2],v[0]*b[1]-v[1]*b[0]].map(x=>x+0);
 assert.deepEqual(cross([1,0,0],[0,0,-1]),cross([-1,0,0],[0,0,1]));assert.deepEqual(cross([0,1,0],[0,0,-1]),[-1,0,0]);
});
test('Sex omarbetade Lenzkort prövar olika situationer med verifierade riktningar',()=>{
 assert.match(correct('3.197'),/^Medurs/);assert.match(correct('3.199'),/^In i bilden under hela/);assert.match(correct('3.200'),/ut ur bilden.*motverkar minskningen/);assert.match(correct('3.201'),/^Medurs – ingen ström – moturs/);assert.match(correct('3.202'),/öka i stället/);
 for(let n=197;n<=202;n++){const q=get('3.'+n);assert.match(q.t,/<svg/);assert.equal(q.miniräknare,true);assert.equal(q.geogebra,false);assert.equal(q.spel,true);assert.match(q.s,/facit-svar/);}
 assert.equal(get('3.200').traningsniva,1);assert.equal(get('3.199').traningsniva,3);
});
test('Diagrammens koordinater följer mätdata och tidsintervall',()=>{
 for(const [id,start,end]of [['3.519',[60,280],[430,42]],['3.520',[60,208.6],[430,65.8]],['3.528',[60,280],[430,280]],['3.201',[60,280],[430,280]]]){
  const q=get(id),m=q.t.match(/<path d="(M[^"]+)" stroke="#2b67a2" fill="none" stroke-width="3"/);assert.ok(m,id);const pts=[...m[1].matchAll(/(?:M|L)([\d.]+) ([\d.]+)/g)].map(x=>[+x[1],+x[2]]);assert.deepEqual(pts[0],start,id);assert.deepEqual(pts.at(-1),end,id);
 }
 // 3.528 has a 4 mWb plateau from 1 to 2 s, followed by a twice-as-steep decline.
 const d=get('3.528').t.match(/<path d="(M[^"]+)" stroke="#2b67a2"/)[1];const pts=[...d.matchAll(/(?:M|L)([\d.]+) ([\d.]+)/g)].map(m=>[+m[1],+m[2]]);assert.ok(pts.some(([x,y])=>x===208&&y===42));assert.ok(pts.some(([x,y])=>x===356&&y===42));
});
test('Aktiv stavlängd, slingans passage och vinkel är skalenliga',()=>{
 const q=get('3.523');assert.match(q.t,/<rect x="135" y="45" width="285" height="83"/);assert.match(q.t,/M285 60L285 230/);near((45+83-60)/(230-60),12/30);
 const loop=get('3.531');assert.match(loop.t,/<rect x="45" y="95" width="85" height="85"/);assert.match(loop.t,/<rect x="160" y="55" width="255"/);near(255/85,.6/.2);
 for(const id of ['3.421','3.438']){const q=get(id);assert.match(q.t,/vinkelrät mot rörelseriktningen/);const a=Math.atan2(200-100,273.205-100)*180/Math.PI;assert.ok(Math.abs(a-30)<.0001);assert.match(q.t,/Staven ses från ena änden/);}
});
test('Äldre formelhjälp och kryssprodukt återinförs inte',()=>{
 for(const id of changed){const q=get(id);assert.doesNotMatch(q.t,/Inducerad spänning i en rak ledare:/,id);assert.equal(q.miniräknare,true);assert.equal(q.geogebra,false);}
 assert.doesNotMatch(get('3.435').s,/\\times/);assert.match(get('3.439').t,/Fältet är vinkelrätt mot skenornas plan/);for(const id of ['3.436','3.517','3.519','3.520'])assert.match(get(id).t,/vinkelräta mot varandra/);
});
