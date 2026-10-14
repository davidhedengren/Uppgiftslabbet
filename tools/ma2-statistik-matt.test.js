'use strict';
const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('node:fs'),vm=require('node:vm'),path=require('node:path');
const root=path.join(__dirname,'..'),ctx={window:{}};vm.runInNewContext(fs.readFileSync(path.join(root,'uppgifterma2.js'),'utf8'),ctx);
const models=require('./fixtures/ma2-statistik-matt.json'),get=id=>ctx.window.BANKMA2.find(x=>x.id===id),plain=x=>JSON.parse(JSON.stringify(x));
const mean=v=>v.reduce((a,b)=>a+b,0)/v.length,med=v=>{const a=v.slice().sort((a,b)=>a-b);return (a[Math.floor((a.length-1)/2)]+a[Math.floor(a.length/2)])/2;};
const sd=(v,sample=true)=>Math.sqrt(v.reduce((a,x)=>a+(x-mean(v))**2,0)/(v.length-(sample?1:0))),pair=(v,s=true)=>[mean(v),sd(v,s)];
const mode=v=>{const c=new Map();v.forEach(x=>c.set(x,(c.get(x)||0)+1));const n=Math.max(...c.values()),a=[...c].filter(x=>x[1]===n).map(x=>x[0]).sort((a,b)=>a-b);return a.length===1?a[0]:a;};
const range=v=>Math.max(...v)-Math.min(...v),iqr=v=>{const a=v.slice().sort((a,b)=>a-b);assert.equal(a.length%2,0);return med(a.slice(a.length/2))-med(a.slice(0,a.length/2));};
function close(a,b){if(Array.isArray(b)){assert.equal(a.length,b.length);b.forEach((x,i)=>close(a[i],x));}else if(typeof b==='number')assert.ok(Math.abs(a-b)<1e-9,`${a} != ${b}`);else assert.equal(a,b);}
function expected(m){const v=m.values;switch(m.type){case'basic':return[mean(v),med(v),mode(v)];case'categorical':return['Blå',13,600/13];case'measures':return[med(v),mode(v),pair(v,m.sample),m.quartiles?iqr(v):range(v)];case'comparison':return[pair(m.A),pair(m.B),({'4.346':'A','4.348':0,'4.349':2,'4.350':'B'})[m.id]];case'outlier':return[med(v),mode(v),pair(v),'median'];case'weighted':return[pair(v),med(v),mode(v),iqr(v),'nej'];default:throw Error(m.type);}}
test('Alla 30 uppgifters läges- och spridningsmått räknas oberoende',()=>{assert.equal(models.length,30);for(const m of models)close(plain(get(m.id).rättSvar),expected(m));});
test('Tabeller och diagram visar de observationer som facit använder',()=>{
 for(const m of models){const q=get(m.id),s=q.spelIntro;assert.match(s,/<table|<svg/);
  const cells=[...s.matchAll(/<td>(.*?)<\/td>/g)].map(x=>x[1]);const n=x=>Number(x.replace('−','-').replace(',','.'));
  if(m.type==='categorical'){assert.deepEqual(cells,['Blå','6','Grön','4','Röd','3']);continue;}
  if(m.type==='comparison'){if(m.representation==='frequency')for(let i=0;i<5;i++)assert.deepEqual(cells.slice(3*i,3*i+3).map(n),[i,m.A.filter(x=>x===i).length,m.B.filter(x=>x===i).length]);else close(cells.filter((_,i)=>i%3===1).map(n),m.A),close(cells.filter((_,i)=>i%3===2).map(n),m.B);continue;}
  if(m.representation==='raw')close(cells.filter((_,i)=>i%2).map(n),m.values);
  if(m.representation==='frequency'){const actual=[];for(let i=0;i<cells.length;i+=2)actual.push(...Array(n(cells[i+1])).fill(n(cells[i])));close(actual,m.values.slice().sort((a,b)=>a-b));}
  if(['bars','dots'].includes(m.representation)){
   const counts=new Map();m.values.forEach(x=>counts.set(x,(counts.get(x)||0)+1));const max=Math.max(...counts.values())+1,min=Math.min(...m.values),span=Math.max(...m.values)-min;
   const tags=[...s.matchAll(/<(?:rect|circle)\b([^>]*)>/g)].map(x=>Object.fromEntries([...x[1].matchAll(/([\w-]+)="([^"]*)"/g)].map(y=>[y[1],y[2]]))).filter(x=>x.class?.startsWith('more-'));
   if(m.representation==='bars'){assert.equal(tags.length,counts.size);for(const t of tags){assert.ok(Math.abs(+t.height/184*max-counts.get(+t['data-value']))<.001);assert.ok(Math.abs(+t.y + +t.height-242)<.002);assert.ok(Math.abs(+t.x+13-(90+(+t['data-value']-min)/span*327))<.001);}}
   else {assert.equal(tags.length,m.values.length);for(const [v,c]of counts){const dots=tags.filter(x=>+x['data-value']===v);assert.equal(dots.length,c);dots.forEach((d,i)=>{assert.ok(Math.abs(+d.cy-(242-(i+1)/max*184))<.001);assert.ok(Math.abs(+d.cx-(90+(v-min)/span*327))<.001);});}}
  }
 }
});
test('Alla 111 delkort har tabell/figur, egen fråga, facit, ledtråd och riktiga svarsfält',()=>{
 let count=0;for(const m of models){const q=get(m.id);assert.equal(q.kap,4);assert.deepEqual(plain(q.kurs),['2a','2b','2c']);assert.equal(q.spel,true);assert.equal(q.miniräknare,['basic','categorical'].includes(m.type));if(!['basic','categorical'].includes(m.type))assert.equal(q.geogebra,true);assert.equal(q.spelDelning,'deluppgifter');assert.equal(q.spelDelar.length,q.rättSvar.length);assert.equal(q.svarEtiketter.length,q.rättSvar.length);
  q.spelDelar.forEach((p,i)=>{count++;assert.ok(p.fraga&&p.s&&p.ledtrad);assert.doesNotMatch(p.fraga+p.ledtrad,/svaret från|föregående del|använd ditt svar/i);assert.doesNotMatch(p.s,/facit-steglista|<ol/);if(Array.isArray(q.rättSvar[i])){assert.equal(p.svarEtiketter.length,q.rättSvar[i].length);assert.equal(q.svarFormat[i].length,q.rättSvar[i].length);assert.equal(q.svarEnhet[i].length,q.rättSvar[i].length);assert.equal(q.tolerans[i].length,q.rättSvar[i].length);assert.ok(['ordnad','mängd'].includes(p.svarsstruktur));}assert.ok(p.traningsniva>=1&&p.traningsniva<=3);});
 }assert.equal(count,111);
});
test('Samtliga databeräkningar använder nu Sx med n−1',()=>{
 for(const m of models.filter(x=>x.type==='measures')){const q=get(m.id),p=q.spelDelar[2];assert.match(p.fraga,/Sx/);assert.equal(m.sample,true);assert.ok(Math.abs(sd(m.values,true)-q.rättSvar[2][1])<1e-9);if(!m.values.every(v=>v===m.values[0]))assert.notEqual(sd(m.values,false),q.rättSvar[2][1]);}
});
test('Rätt avrundning godtas och närliggande felavrundning ligger utanför toleransen',()=>{
 function check(a,t){if(Array.isArray(a))return a.forEach((v,i)=>check(v,t[i]));if(typeof a!=='number'||t!==.005)return;const rounded=Math.round((a+Number.EPSILON)*100)/100;assert.ok(Math.abs(a-rounded)<=t+1e-12);assert.ok(Math.abs(a-(rounded+.01))>t);assert.ok(Math.abs(a-(rounded-.01))>t);}
 for(const m of models)get(m.id).rättSvar.forEach((a,i)=>check(a,get(m.id).tolerans[i]));
});
test('Två typvärden är en mängd, medan medelvärde och standardavvikelse är ordnade',()=>{
 for(const id of ['4.345','4.347']){const q=get(id);assert.equal(q.spelDelar[1].svarsstruktur,'mängd');assert.equal(q.spelDelar[2].svarsstruktur,'ordnad');}
 close(get('4.344').rättSvar,[2,2,[2,0],0]);close(get('4.350').rättSvar,[[2,Math.sqrt(10/9)],[2,Math.sqrt(26/9)],'B']);
});
