'use strict';
const{test}=require('node:test'),assert=require('node:assert/strict'),fs=require('node:fs'),vm=require('node:vm'),path=require('node:path');
const c={window:{}};vm.createContext(c);for(const f of ['uppgifterma1.js','uppgifterma2.js','uppgiftermatf1.js','uppgifter.js'])vm.runInContext(fs.readFileSync(path.join(__dirname,'..',f),'utf8'),c);
const q=(bank,id)=>c.window[bank].find(t=>t.id===id),ma=id=>q('BANKMA2',id),m1=id=>q('BANKMA1',id);
const mean=v=>v.reduce((a,b)=>a+b,0)/v.length,sd=(v,sample=false)=>Math.sqrt(v.reduce((a,x)=>a+(x-mean(v))**2,0)/(v.length-(sample?1:0)));
const close=(a,b)=>assert.ok(Math.abs(a-b)<1e-9,`${a} ≠ ${b}`);
test('Explicit temperaturstickprov räknas med n−1 och avvisar σx',()=>{
 for(const[id,index,v]of [['5.94',1,[20.8,21.2,21,21.4,20.6]],['5.71',1,[20,21,22,21,21]],['5.71',3,[19,21,23,21,21]]]){
  const t=ma(id);assert.match(t.t,/stickprov/);assert.match(t.t,/Sx/);close(t.rättSvar[index],sd(v,true));
  assert.ok(Math.abs(sd(v)-t.rättSvar[index])>t.tolerans[index]);
 }
});
test('Samtliga rådataberäkningar av standardavvikelse har entydigt mått och oberoende facit',()=>{
 const cases=[['4.05',[[8,10,12,14],[9,10,11,12]]],['4.10',[[0,0,0,3,3],[0,0,1,1,4]]],['4.28',[[6,8,9,9,11,17]]],['4.46',[[12,16,18,21,23],[12,16,18,21,23,18]]],['4.97',[[2,5,8,11],[-2,-11,-20,-29]]],['4.157',[[7,9,10,10,14],[7,9,10,10,14,10]]],['4.241',[[-2,0,0,0,2],[-2,-2,0,2,2]]],['4.299',[[31.2,30.8,31.5,30.9,31.1,31],[30.4,31.9,30.6,32,30.5,31.1]]],['4.302',[[4,7,9,12],[4,7,9,12,8]]],['5.66',[[12,13,13,14,14,15,15,16],[12,13,13,14,14,15,15,30]]],['5.110',[[4,5,5,6,5],[2,4,5,6,8]]]];
 for(const[id,lists]of cases){const t=ma(id);assert.match(t.t,/σx|\\sigma|\\\(n\\\)/,id);
  const calculated=lists.map(v=>sd(v).toFixed(id==='4.28'?1:2).replace('.',','));
  for(const v of calculated)assert.ok(t.s.includes(v)||t.s.includes(v.replace(',','{,}'))||['4.302'].includes(id),`${id}: ${v}`);
 }
 close(ma('4.28').rättSvar[1],sd([6,8,9,9,11,17]));
 close(ma('4.157').rättSvar[1],sd([7,9,10,10,14]));close(ma('4.157').rättSvar[2],sd([7,9,10,10,14,10]));
 close(ma('4.299').rättSvar[1][0],sd([31.2,30.8,31.5,30.9,31.1,31]));close(ma('4.299').rättSvar[1][1],sd([30.4,31.9,30.6,32,30.5,31.1]));
 close(ma('4.302').rättSvar[0][1],sd([4,7,9,12]));close(ma('4.302').rättSvar[1][1],sd([4,7,9,12,8]));
});
test('Avrundning och extra precision godtas men nästa avrundade tal och Sx avvisas',()=>{
 for(const[target,tol,correct,wrong]of [[ma('4.28').rättSvar[1],ma('4.28').tolerans[1],3.5,3.4],[ma('4.157').rättSvar[1],ma('4.157').tolerans[1],2.28,2.29],[ma('4.299').rättSvar[1][0],ma('4.299').tolerans[1][0],.23,.25],[ma('4.299').rättSvar[1][1],ma('4.299').tolerans[1][1],.65,.71],[ma('4.302').rättSvar[0][1],ma('4.302').tolerans[0][1],2.92,2.93]]){
  assert.ok(Math.abs(correct-target)<=tol);assert.ok(Math.abs(wrong-target)>tol);
 }
});
test('Stratifierade urval består av hela personer och vägs efter gruppernas storlek',()=>{
 const t=m1('5.571'),sizes=[480,420,300],rates=[.625,.5,.3];
 sizes.forEach((n,i)=>assert.equal(t.rättSvar[i],n/1200*80));
 const yes=t.rättSvar.slice(0,3).map((n,i)=>n*rates[i]);yes.forEach(n=>assert.ok(Number.isInteger(n)));
 close(t.rättSvar[3],yes.reduce((a,b)=>a+b,0)/80*100);assert.notEqual(t.rättSvar[3],mean(rates)*100);
 assert.equal(t.svarEnhet[3],'%');assert.equal(t.traningsniva,3);
 assert.deepEqual(Array.from(m1('5.99').rättSvar),[300,330,270].map(x=>x/900*90));
 const count=[420,300,180].map(x=>x/900*90);assert.deepEqual(count,[42,30,18]);assert.ok(count[2]<25);
});
test('Delkort anger själva ordning, eget mått och ger inte andra delars svar i ledtråden',()=>{
 const t=ma('4.241');for(const p of t.spelDelar){assert.equal(p.svarsstruktur,'ordnad');assert.ok(p.svarEtiketter.length>=2);}
 const u=m1('5.97');for(const p of u.spelDelar){assert.doesNotMatch(p.ledtrad,/a\)|b\)|Sant|Falskt|otillräckligt stöd/);}
 // Den gemensamma introduktionen följer med varje kort; måttet behöver stå en gång.
 assert.match(ma('4.28').spelIntro+ma('4.28').spelDelar[1].fraga,/σx/);
 assert.match(ma('4.28').spelDelar[1].fraga,/standardavvikelsen/);
 assert.match(m1('5.102').spelDelar[0].t,/alla svarar/);
});
test('Målgruppen är definierad när ett urval bedöms som snedvridet',()=>{
 for(const id of ['5.182','5.221','5.526','5.535'])assert.match(m1(id).t,/alla invånare|invånarna/);
 assert.match(m1('5.565').t,/högre inkomster/);assert.doesNotMatch(m1('5.174').t,/Bortfalls-/);assert.match(m1('5.180').t,/A: Bortfall<br>/);
 assert.doesNotMatch(m1('5.545').s,/hur troligt det är att skillnaden beror på slumpen/);
});
test('Förändring av data använder |a| för båda spridningsmåtten; exempel och golfandel stämmer',()=>{
 for(const sample of [false,true]){
  close(sd([2,5,8,11].map(x=>-3*x+4),sample),3*sd([2,5,8,11],sample));
  close(sd([0,0,0,3,3],sample),sd([0,0,1,1,4],sample));
 }
 const v=[276,279,279,277,278,278,280,282,285,272,279,278],s=sd(v,true),m=mean(v);
 close(ma('4.306').rättSvar[0],v.filter(x=>Math.abs(x-m)<=s).length/v.length*100);
 assert.equal((m-s).toFixed(2),'275.44');assert.equal((m+s).toFixed(2),'281.73');
 close(ma('4.283').rättSvar[0],(20*60+30*70)/50);close(ma('4.283').rättSvar[1],Math.sqrt((20*(25+60**2)+30*(25+70**2))/50-66**2));
 for(const x of ma('4.284').rättSvar)close(sd([44,48,48,52,52,52,52,52,x]),sd([44,48,48,52,52,52,52,52]));
});
test('Fysikens vätskeprov och det kombinatoriska stickprovet har korrekta värden',()=>{
 const t=q('BANK','2.175');close(t.rättSvar,2/1.4*3600);assert.ok(Math.abs(5140-t.rättSvar)<=t.tolerans);assert.ok(Math.abs(5150-t.rättSvar)>t.tolerans);
 assert.equal(t.traningsniva,2);
 const choose=(n,k)=>{let p=1;for(let i=1;i<=k;i++)p*=((n-i+1)/i);return p;};
 close(choose(3,1)*choose(9,3)/choose(12,4),28/55);assert.equal(q('BANKMATF1','1.103').rättSvar,'28/55');
});
