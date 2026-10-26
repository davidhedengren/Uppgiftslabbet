'use strict';
const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('node:fs'),path=require('node:path'),vm=require('node:vm');
const root=path.join(__dirname,'..'),c={window:{}};vm.runInNewContext(fs.readFileSync(path.join(root,'uppgifterma2.js'),'utf8'),c);
const bank=c.window.BANKMA2,find=id=>bank.find(q=>q.id===id),plain=x=>JSON.parse(JSON.stringify(x));
const report=JSON.parse(fs.readFileSync(path.join(root,'agent/FELRAPPORTER_2026-10-16_0809.json'),'utf8'));
const close=(a,b)=>assert.ok(Math.abs(a-b)<1e-8,`${a} != ${b}`);
test('Varje rapport och varje jämförelse har ett dokumenterat beslut och kommentar',()=>{
 assert.equal(report.rapporter.length,13);assert.equal(new Set(report.granskade).size,81);
 assert.equal(report.atgardade.length+report.granskad_inga_fel.length,81);
 for(const ids of Object.values(report.jamforelsegrupper))assert.ok(ids.length>=6);
 for(const id of report.granskade.filter(id=>id!=='4.142')){assert.ok(find(id)); // 4.142 borttagen (interpolation, användarbeslut 2026-10-22)
 const row=report.poster.find(x=>x.id===id);assert.ok(row.kommentar);assert.equal(typeof find(id)['miniräknare'],'boolean');if(find(id).geogebra)assert.ok(find(id)['miniräknare']);}
 assert.ok(report.granskad_inga_fel.includes('2.484'));
});
test('Uttryckligt logaritmkrav och faktoriserat funktionssvar har avgränsade format',()=>{
 for(const id of ['2.26','2.109','2.217','2.219','2.241','2.250','2.281','2.469','2.529']){const q=find(id);assert.equal(q.svarFormat,'en_logaritm');assert.match(q.t,/en(?:da)? logaritm/);assert.equal(q['miniräknare'],false);assert.equal(q.geogebra,false);}
 for(const id of ['2.86','2.105','2.144','2.167','2.305','2.572'])assert.equal(find(id).svarFormat,'faktoriserat');
 assert.equal(find('2.137').svarFormat[0],'faktoriserat');
});
test('Numeriska exponentialekvationer har rätt avrundat tal, ingen föreskriven likhetsglyph',()=>{
 for(const [id,a,b,c,d] of [['2.14',500,1.12,900,1],['2.56',7,1.3,20,2],['2.221',3,1.08,6,1],['2.223',2,1.15,5,1],['2.249',800,1.06,1000,1]]){
  const q=find(id),exact=Math.log(c/a)/Math.log(b);assert.equal(q.rättSvar,Number(exact.toFixed(d)));assert.equal(q.svarFormat,'numeriskt');assert.equal(q.tolerans,.5*10**-d);
 }
});
test('Koordinater och namngivna sidmått ordnas även på de egna delkorten',()=>{
 for(const [id,i,n] of [['3.202',0,2],['3.05',0,2],['3.408',1,2],['3.412',1,2],['3.412',2,2],['3.413',0,4],['3.413',1,2],['3.515',1,2],['2.709',0,3]]){
  const d=find(id).spelDelar[i];assert.equal(d.svarsstruktur,'ordnad');assert.equal(d.svarEtiketter.length,n);
 }
 for(const id of ['2.73','2.113','2.488','2.503']){const q=find(id);assert.equal(q.svarsstruktur,'mängd');assert.deepEqual(plain(q.svarEtiketter),['Sidlängd','Sidlängd']);assert.deepEqual(plain(q.svarEnhet),['cm','cm']);assert.match(q.t,/<svg/);}
});
test('Svårighetsnivå speglar parameterresonemang och given standardavvikelse',()=>{
 assert.equal(find('2.32').traningsniva,5);assert.equal(find('2.505').traningsniva,4);
 assert.deepEqual(plain(find('2.620').spelDelar.map(q=>q.traningsniva)),[4,3,5]);
 for(const id of ['4.21','4.43','4.56']){const q=find(id);assert.equal(q.traningsniva,4);assert.equal(q.spelDelar[1].traningsniva,4);assert.match(q.spelDelar[1].s,/avstånd/);assert.equal(q.geogebra,false);}
 for(const id of ['4.49','4.75','4.86','4.90','4.93'])assert.equal(find(id).traningsniva,3);
 assert.equal(find('4.90').spelDelar[0].traningsniva,1);assert.equal(find('4.90').spelDelar[1].traningsniva,3);
 for(const [id,a,b,m,sd] of [['4.21',3,-7,12,5],['4.43',1.5,-7,20,4],['4.56',-4,10,25,3]])assert.deepEqual(plain(find(id).rättSvar),[a*m+b,Math.abs(a)*sd]);
});
test('Svåra facit räknas oberoende: rötter, tangering, symmetri och segel',()=>{
 for(const a of [(9+3*Math.sqrt(105))/16,(9-3*Math.sqrt(105))/16]){const r=2*a/3;close(8*a*a-9*a-27,0);close(r*r-2*a*r+a+3,0);close(4*r*r-4*a*r+a+3,0);}
 for(const k of [2+2*Math.sqrt(5),2-2*Math.sqrt(5)]){const x=k/2;close(x*x+2,k*(x-1)-2);close(k*k-4*k-16,0);}
 close(1.4*(4-2)*(4-6),find('2.505').rättSvar);close(1.4*(1-2)*(1-6),7);
 const [sides,perimeter]=find('2.709').rättSvar;assert.deepEqual(plain(sides),[5,12,13]);close(sides[0]**2+sides[1]**2,sides[2]**2);close(sides[0]*sides[1]/2,30);close(perimeter,30*Math.sqrt(45/30));
 assert.match(find('2.30').t,/två olika heltalsrötter/);
});
test('Resonemangsfacit visas efter samtliga numeriska fält på ordnade delkort',()=>{
 for(const [id,i,n] of [['3.412',2,2],['3.413',1,2],['3.515',1,2],['2.709',0,3]]){assert.deepEqual(plain(find(id).spelDelar[i].manuellKomplettering),Array.from({length:n},(_,j)=>j===n-1));}
});
test('Normalfördelningskurvor har korrekt kopplade bokstäver och normaliserad höjd',()=>{
 for(const [id,expected] of [['4.107','C'],['4.226','A']]){
  const q=find(id),curves=[...q.t.matchAll(/data-kurva="([A-C])" data-standardavvikelse="([.\d]+)" points="([^"]+)"/g)];assert.ok(curves.length>=2);
  assert.equal(curves.reduce((a,b)=>+a[2]<+b[2]?a:b)[1],expected);
  for(const [,name,sd,points] of curves){assert.match(q.t,new RegExp(`data-pekare="${name}"`));for(const point of points.split(' ')){const [x,y]=point.split(',').map(Number),want=255-350/(sd*Math.sqrt(2*Math.PI))*Math.exp(-(((x-240)/40)**2)/(2*sd**2));assert.ok(Math.abs(y-want)<.006);}}
 }
});
test('Plantmodellen har höjdenhet och bibehållet rätt värde på självständiga kort',()=>{
 const q=find('4.140');assert.match(q.t,/plantas höjd/);assert.match(q.spelIntro,/höjden i cm/);assert.match(q.spelIntro,/tiden i veckor/);assert.equal(q.rättSvar[0],3.2*20+14);assert.equal(q.svarEnhet[0],'cm');assert.equal(q.geogebra,false);
 for(const d of q.spelDelar)assert.ok(d.s.length>100);
 for(const id of ['4.136','4.138','4.139','4.141'])assert.equal(find(id).geogebra,true);
});
