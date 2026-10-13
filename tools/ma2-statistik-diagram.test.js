'use strict';
const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('node:fs'),vm=require('node:vm'),path=require('node:path');
const root=path.join(__dirname,'..'),c={window:{}};for(const file of ['uppgifterma2.js','strukturma2.js'])vm.runInNewContext(fs.readFileSync(path.join(root,file),'utf8'),c);
const get=n=>c.window.BANKMA2.find(q=>q.id===`4.${n}`),plain=x=>JSON.parse(JSON.stringify(x)),close=(a,b,eps=1e-8)=>assert.ok(Math.abs(a-b)<eps,`${a} != ${b}`),mean=v=>v.reduce((a,b)=>a+b,0)/v.length,median=v=>{const a=v.slice().sort((a,b)=>a-b);return(a[Math.floor((a.length-1)/2)]+a[Math.floor(a.length/2)])/2;};
const expanded=(values,counts)=>values.flatMap((v,i)=>Array(counts[i]).fill(v));
function tags(n,tag,cls){return [...get(n).t.matchAll(new RegExp('<'+tag+'\\b([^>]+)>','g'))].map(m=>Object.fromEntries([...m[1].matchAll(/([\w-]+)="([^"]*)"/g)].map(x=>[x[1],x[2]]))).filter(x=>!cls||x.class===cls);}
const cells=n=>[...get(n).t.matchAll(/<td>(.*?)<\/td>/g)].map(m=>m[1]);
const bars=n=>tags(n,'rect','stat-bar');
test('Femton nya uppgifter har rätt kurs, område, hjälpmedel och entydiga kontrakt',()=>{
 for(let n=307;n<=321;n++){
  const q=get(n);assert.ok(q,n);assert.deepEqual(plain(q.kurs),['2a','2b','2c']);assert.equal(q.kap,4);assert.ok(c.window.OMRMA2[4][q.omr]);assert.ok(q.familj);assert.ok(q.t&&q.s&&q.ledtrad);assert.equal(typeof q.miniräknare,'boolean');assert.equal(q.geogebra,false);assert.equal(q.spel,true);assert.notEqual(q.rättSvar,null);assert.equal(q.traningsniva>=3?'C':'E',q.niva);
  if(q.svarstyp==='alternativ'){assert.equal(q.alternativ.filter(a=>a.ratt).length,1);assert.match(q.t,/Välj ett alternativ/);assert.equal(q.rättSvar,q.alternativ.find(a=>a.ratt).txt);}
  if(q.spelDelar){assert.equal(q.spelDelar.length,q.rättSvar.length);assert.equal(q.tolerans.length,q.rättSvar.length);assert.equal(q.svarFormat.length,q.rättSvar.length);assert.equal(q.svarEnhet.length,q.rättSvar.length);assert.equal(q.självrättning.length,q.rättSvar.length);}
 }
 assert.deepEqual(plain(c.window.SPARMA2[4].tabeller_diagram),['2a','2b','2c']);assert.ok(c.window.GRUPPMA2[4].find(x=>x.id==='tabeller_diagram').omr.includes('tabeller_diagram'));assert.ok(c.window.BANKMA2.some(q=>q.omr==='tabeller_diagram'&&q.traningsniva===1));
});
test('Lodräta tabellers värden stämmer med median och frekvensviktat medelvärde',()=>{
 assert.deepEqual(cells(307),['0','5','1','9','2','4','3','2']);assert.equal(get(307).rättSvar,5);
 assert.equal(get(310).rättSvar,median([4,8,6,10,7]));assert.deepEqual(cells(310).filter((_,i)=>i%2),['4','8','6','10','7']);
 const values=expanded([0,1,2,3],[4,8,6,2]);assert.equal(values.length,20);close(get(311).rättSvar[0],median(values));close(get(311).rättSvar[1],mean(values));
 assert.doesNotMatch(get(311).spelDelar[0].s,/1\{,\}3|26\/20/);assert.doesNotMatch(get(311).spelDelar[1].s,/Medianen|10:e|11:e/);
});
test('Stolp- och histogramhöjder använder den visade skalan',()=>{
 for(const [n,vals,ymin,ymax]of [[308,[8,12,18,6],0,20],[314,[6,10,8,4],0,12],[318,[100,120],90,130],[321,[3,4,3],0,5]]){
  const rs=bars(n);assert.equal(rs.length,vals.length);rs.forEach((r,i)=>{close(ymin+Number(r.height)/(n===308?272:177)*(ymax-ymin),vals[i],.001);close(+r.y + +r.height,n===308?330:235,.02);});
 }
 assert.equal(get(308).rättSvar,18);assert.equal(get(314).rättSvar,6+10);assert.match(get(314).t,/0–4|5–9/);
 assert.match(get(318).alternativ.find(a=>a.ratt).txt,/20 %/);assert.equal((120-100)/100*100,20);
});
test('Punkter i linjediagrammet och den kumulativa kurvan ligger på rätt värden',()=>{
 for(const [n,values]of [[309,[40,60,50,80,70]],[315,[0,10,30,50,75,90,100]]]){
  const pts=tags(n,'circle','stat-point');assert.equal(pts.length,values.length);pts.forEach((p,i)=>{close((235-Number(p.cy))/177*100,values[i],.003);close(+p.cx,65+i/(values.length-1)*380,.006);});
 }
 assert.equal(get(309).rättSvar,'Torsdag');assert.equal(get(315).rättSvar,40);assert.equal([0,10,20,30,40,50,60][[0,10,30,50,75,90,100].indexOf(75)],40);
});
test('Staplad graf har hela personer och kräver jämförelse av rätt andelar',()=>{
 const rs=tags(312,'rect','stat-stack'),counts=[[20,10,10],[24,40,16]];assert.equal(rs.length,6);
 rs.forEach((r,i)=>close(+r.height/220*80,counts.flat()[i],.003));assert.equal(counts[0].reduce((a,b)=>a+b),40);assert.equal(counts[1].reduce((a,b)=>a+b),80);
 assert.equal(get(312).rättSvar[0],20/40>24/80?'A':'B');close(get(312).rättSvar[1],100*(20/40-24/80));assert.match(get(312).spelIntro,/>24<\/text>/);assert.equal(get(312).svarEnhet[1],'procentenheter');
});
test('Cirkeldiagrammets sektorer motsvarar andelarna och antalet elever',()=>{
 const paths=tags(313,'path','stat-sector'),shares=[25,40,20,15];assert.equal(paths.length,4);
 paths.forEach((p,i)=>{const numbers=p.d.match(/-?\d+(?:\.\d+)?/g).map(Number),a=Math.atan2(numbers[3]-144,numbers[2]-150),b=Math.atan2(numbers.at(-1)-144,numbers.at(-2)-150),degrees=(b-a)*180/Math.PI;close(((degrees+360)%360)/360*100,shares[i],.001);});
 assert.equal(shares.reduce((a,b)=>a+b),100);assert.equal(get(313).rättSvar,240*shares[0]/100);
});
test('Lådagram och prickdiagram ger median, kvartilavstånd och rätt mittenvärden',()=>{
 const boxes=tags(316,'rect','stat-box'),medianLines=tags(316,'line').filter(x=>x['stroke-width']==='3');assert.equal(boxes.length,2);close(+boxes[0].width/375*50,28-20);close(+boxes[1].width/375*50,32-18);close((+medianLines[0].x1-70)/375*50,24);close((+medianLines[1].x1-70)/375*50,26);assert.deepEqual(plain(get(316).rättSvar),['A',(32-18)-(28-20)]);
 const dots=tags(317,'circle','stat-dot'),times=dots.map(d=>(+d.cx-65)/380*10);assert.equal(dots.length,10);assert.deepEqual(times.slice().sort((a,b)=>a-b),[2,2,4,4,4,6,6,6,6,8]);assert.equal(get(317).rättSvar,median(times));
});
test('Saknad frekvens och olika gruppvikter löses självständigt',()=>{
 const x=get(319).rättSvar;assert.equal(x,7);close((11+x)/(8+x),1.2);assert.deepEqual(cells(319),['0','3','1','?','2','4','3','1']);
 const groupedA=[9/10,12/20],groupedB=[32/40,1/2],a=(9+12)/(10+20),b=(32+1)/(40+2);assert.ok(groupedA.every((p,i)=>p>groupedB[i]));assert.ok(b>a);close(a,.7);close(b,33/42);assert.match(get(320).alternativ.find(a=>a.ratt).txt,/B har ungefär 79/);
});
test('Grupperade heltalsdata ger möjliga medelvärdesgränser, inte ett exakt medelvärde',()=>{
 const lows=expanded([0,5,10],[3,4,3]),highs=expanded([4,9,14],[3,4,3]);assert.deepEqual(plain(get(321).rättSvar),[mean(lows),mean(highs)]);assert.notEqual(mean(lows),mean(highs));assert.equal(get(321).svarsstruktur,'ordnad');assert.deepEqual(plain(get(321).svarEtiketter),['Minsta medelvärde','Största medelvärde']);assert.match(get(321).t,/hela minuter/);
});
