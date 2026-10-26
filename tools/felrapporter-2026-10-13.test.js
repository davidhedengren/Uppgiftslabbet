'use strict';
const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('node:fs'),vm=require('node:vm'),path=require('node:path');
function bank(c){const v={window:{}};vm.runInNewContext(fs.readFileSync(path.join(__dirname,'../uppgifter'+c+'.js'),'utf8'),v);return new Map(Object.values(v.window).find(Array.isArray).map(q=>[q.id,JSON.parse(JSON.stringify(q))]));}
const b={matf1:bank('matf1'),mato2:bank('mato2'),mato1:bank('mato1'),ma2:bank('ma2'),ma1:bank('ma1')},near=(a,e)=>assert.ok(Math.abs(a-e)<1e-11,`${a} != ${e}`);
const val=s=>Function('return ('+String(s).replace(/\\\(|\\\)/g,'').replace(/\^/g,'**')+')')();
const fact=n=>n<2?1:n*fact(n-1);
test('Mängd-, Venn- och blockuppgifterna räknas från sina givna antal',()=>{
 assert.deepEqual(b.matf1.get('1.15').rättSvar,['Falskt','Sant']);
 assert.deepEqual(b.matf1.get('1.164').rättSvar,[18+7+11,18+11]);assert.equal(b.matf1.get('1.347').rättSvar,36+31-8);
 for(const [id,n]of [['1.308',18+15-4],['1.309',43-(21+20-6)],['1.318',31+27-4],['1.319',70-(34+32-6)],['1.310',24-8],['1.320',20-8]])assert.equal(val(b.matf1.get(id).rättSvar),n);
 for(const [id,n]of [['1.77',fact(5)],['1.72',2*fact(8)],['1.74',fact(10)-2*fact(9)],['1.76',fact(5)*(6*5*4)],['1.138',2*fact(7)],['1.195',fact(7)-2*fact(6)]])assert.equal(val(b.matf1.get(id).rättSvar),n);
});
test('Större kodberäkningar är korrekta och har tillgång till miniräknare',()=>{
 for(const [id,n]of [['1.625',6**4],['1.24',10**4],['1.501',2**10],['1.576',5**5],['1.580',26*10**3],['1.582',4**5]]){assert.equal(val(b.matf1.get(id).rättSvar),n);assert.equal(b.matf1.get(id).miniräknare,true);}
});
test('Sannolikhetsexempel och skidserier bygger på rätt händelser',()=>{
 for(const [id,p]of [['1.548',1/16],['1.549',4/16],['1.550',10/32],['1.551',15/16],['1.552',10/32],['1.553',5/36],['1.554',4/10*3/9]])near(val(b.matf1.get(id).rättSvar),p);
 const p=b.matf1.get('1.727').rättSvar;near(p[0],.83**10);near(p[1],.83**10*.95**10);near(p[2],10*.17*.83**9*.95**10+10*.05*.95**9*.83**10);
 assert.doesNotMatch(b.matf1.get('1.727').spelDelar[0].t,/95|liggande/);
});
test('Primtalsprodukter ger rätt ursprungstal och kräver primtalsformat',()=>{
 for(const [id,n]of [['2.79',360],['2.157',756],['2.209',840]]){const q=b.matf1.get(id);assert.equal(val(q.rättSvar),n);assert.equal(q.svarFormat,'primtalsfaktorisering');assert.match(q.t,/upprepa faktorerna/);}
});
test('Fasvinklar återskapar båda ursprungliga koefficienterna i grader',()=>{
 for(const [id,coeffs]of [['1.131',[[3,4],[5,-12]]],['1.81',[[1,1],[Math.sqrt(3),1],[1,-Math.sqrt(3)],[3,4]]]]){
  const q=b.mato2.get(id);q.rättSvar.forEach(([R,v],i)=>{const amplitude=typeof R==="number"?R:R===String.raw`\sqrt{2}`?Math.SQRT2:NaN;near(amplitude*Math.cos(v*Math.PI/180),coeffs[i][0]);near(amplitude*Math.sin(v*Math.PI/180),coeffs[i][1]);assert.ok(v>-90&&v<90);assert.deepEqual(q.svarFormat[i],['numeriskt','grader']);assert.deepEqual(q.svarEnhet[i],[null,'°']);assert.deepEqual(q.spelDelar[i].svarEtiketter,['R','v']);});
 }
 assert.equal(b.mato2.get('1.149').alternativ.find(a=>a.ratt).txt,String.raw`\(5\sin(x-53{,}1^\circ)\)`); // flervalskort sedan 2026-10-24assert.match(b.mato2.get('1.149').t,/53\{,\}1/);
});
test('Kurvfrågor är fullständiga och deras svar stämmer med funktionerna',()=>{
 for(const [id,expected]of [['1.01',[5,'pi/2',2,[7,-3]]],['1.17',[2,'2*pi/3','pi/6','y=1']],['1.72',[3,'pi',-4,[-1,-7]]],['1.93',[4,'2*pi/3',[2,-6]]],['1.56',['pi/2',['-pi/4','pi/4'],1]],['1.59',[3,'y=2',4]]]){
  const q=b.mato2.get(id);assert.deepEqual(q.rättSvar,expected);assert.doesNotMatch(q.spelIntro,/bestäm<\/p>|funktionens<\/p>/i);
  for(const p of q.spelDelar){assert.match(p.fraga,/Bestäm|Ange|Beräkna|Hur/);assert.doesNotMatch(p.fraga,/,<\/p>| och<\/p>/);}
 }
});
test('Fem kontinuitetsvarianter ger olika algebraiska gränsvärden',()=>{
 const cases=[['1.518',2,x=>(x*x+x-6)/(x-2),5],['3.57',2,x=>(3*x-6)/(x-2),3],['3.799',2,x=>(x**3-8)/(x-2),12],['1.523',3,x=>(x*x-9)/(2*x-6),3],['3.812',-3,x=>(x*x-9)/(x+3),-6]];
 for(const [id,x,f,expected]of cases){assert.equal(b.mato1.get(id).rättSvar,expected);for(const h of [-1e-5,1e-5])assert.ok(Math.abs(f(x+h)-expected)<.0001,id);}
 assert.equal(b.mato1.get('3.799').traningsniva,3);assert.equal(b.mato1.get('3.799').niva,'C');assert.equal(b.mato1.get('1.99').rättSvar,4);
 assert.doesNotMatch(b.mato1.get('4.495').t,/cos0/);assert.equal(b.mato1.get('4.495').rättSvar,0);
});
test('Vinkelräta linjer måste också passera den givna punkten',()=>{
 for(const [id,k,m,other,x,y]of [['1.54',-2,9,.5,4,1],['1.347',3,-1,-1/3,2,5]]){const q=b.ma2.get(id);assert.equal(k*other,-1);assert.equal(k*x+m,y);assert.match(q.t,/båda villkoren/);assert.match(q.s,/Punktvillkoret/);}
});
test('Sex kvadratekvationer har båda rötterna i oordnade fält',()=>{
 for(const [id,f]of [['2.57',x=>(2*x+1)**2-25],['2.01',x=>4*(x-1)**2-25],['2.81',x=>3*(x-2)**2-27],['2.128',x=>x*x-49],['2.129',x=>(x+3)**2-16],['2.49',x=>5*x*x-80]]){const q=b.ma2.get(id);assert.equal(q.rättSvar.length,2);assert.notEqual(...q.rättSvar);q.rättSvar.forEach(x=>assert.equal(f(x),0));assert.equal(q.svarsstruktur,'mängd');assert.match(q.t,/en i varje svarsfält/);}
});
test('Säkerhetsfaktor och materialkostnad har tydlig definition och rätt svar',()=>{
 for(const [id,n]of [['7.488',300/1.5],['7.490',5/2],['7.491',12/4],['7.493',480*2.5],['7.499',120/1.6]]){near(val(b.ma1.get(id).rättSvar),n);assert.match(b.ma1.get(id).t,/betyder/);}
 for(const [id,n]of [['7.162',46*1.07*285+650],['7.163',18*42+295],['7.165',6.5*520+1850],['7.167',245*14+390],['7.168',180*24*.88*1.25]])near(val(b.ma1.get(id).rättSvar),n);
});

test('Ytterligare binomialexempel verifieras utan att ta facits decimaler som sanning',()=>{
 const choose=(n,k)=>fact(n)/(fact(k)*fact(n-k)),bin=(n,p,k)=>choose(n,k)*p**k*(1-p)**(n-k);
 for(const [id,values]of [['1.719',[bin(10,.38,4),Array.from({length:7},(_,j)=>bin(10,.38,j+4)).reduce((a,b)=>a+b)]],['1.720',[.48**10,bin(10,.52,5)]],['1.725',[1-.98**100-100*.02*.98**99,35]],['1.726',[bin(25,.05,0),bin(25,.05,1),bin(25,.05,2)]],['1.728',[bin(13,1/3,12),bin(13,1/3,10),4]]]){
  b.matf1.get(id).rättSvar.forEach((p,i)=>assert.ok(Math.abs(val(p)-values[i])<1e-9,id));
 }
 assert.ok(1-.98**34<=.5);assert.ok(1-.98**35>.5);
});
test('SGD och MGM efterfrågar tal även när metoden använder primtalsfaktorisering',()=>{
 const gcd=(a,b)=>b?gcd(b,a%b):a,lcm=(a,b)=>a*b/gcd(a,b);
 for(const [id,pairs,fn]of [['2.649',[[18,150],[56,42],[238,510],[1144,3146]],gcd],['2.650',[[18,150],[36,27],[81,245]],lcm]]){
  const q=b.matf1.get(id);q.rättSvar.forEach((n,i)=>assert.equal(val(n),fn(...pairs[i])));assert.ok(q.svarFormat.every(f=>f==='numeriskt'));
 }
 for(const [id,a,c]of [['2.80',168,252],['2.158',420,588],['2.210',672,840]])assert.equal(val(b.matf1.get(id).rättSvar),gcd(a,c));
});
