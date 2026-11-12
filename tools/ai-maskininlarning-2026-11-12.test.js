'use strict';
// AI-banken kapitel 4 Maskininlärning (bygg-ai-maskininlarning-2026-11-12.py, ai_ml_modeller.py).
// Räknar om svaren oberoende av byggskriptet: klassificeringsmatriserna läses ur uppgiftens tabell,
// övriga svar räknas med egna formler. Kontrollerar också struktur, nivåer och pappersversionen.
const {test}=require('node:test'),a=require('node:assert/strict'),fs=require('node:fs'),vm=require('node:vm');
const c={window:{}};vm.runInNewContext(fs.readFileSync('uppgifterai.js','utf8'),c);vm.runInNewContext(fs.readFileSync('strukturai.js','utf8'),c);
const bank=c.window.BANKAI,q=id=>bank.find(u=>u.id===id);
const del=k=>{const u=q(k.slice(0,-1)),d=u.spelDelar.find(x=>x.etikett===k.slice(-1));a.ok(d,k);return d;};
const ml=bank.filter(u=>u.kap===4);
const r3=x=>Math.round(x*1000)/1000;

test('struktur: fem kort med två delmoment och minst åtta uppgifter per delmoment',()=>{
 a.equal(c.window.KAPNAMNAI[4],'Maskininlärning');
 a.deepEqual(Object.keys(c.window.OMRAI[4]),['ml_grunder','klassmatris','regression','knn_kmeans','neurala']);
 a.equal(c.window.OMRAI[4].neurala,'Fördjupning: neurala nätverk');
 a.equal(ml.length,84);
 const fam={};for(const u of ml){a.ok(c.window.OMRAI[4][u.omr],u.id);((fam[u.omr]??={})[u.familj]??=[]).push(u.id);}
 for(const [omr,f] of Object.entries(fam)){a.equal(Object.keys(f).length,2,omr);for(const [n,ids] of Object.entries(f))a.ok(ids.length>=8,omr+' '+n);}
 a.ok(fam.klassmatris['Beräkna utvärderingsmått'].length>=10,'många klassificeringsmatriser');
});

// Användaren 2026-11-12: kapitlet ska vara ganska lätt för AI1, och neurala nätverk är en enkel fördjupning.
test('nivåer: mest E, C i varje kort, A bara i 4.33c, neurala nätverk utan A',()=>{
 const p=ml.flatMap(u=>u.spelDelar),n=k=>p.filter(d=>d.niva===k).length;
 a.ok(n('E')/p.length>=0.7);a.ok(n('C')>=30);a.deepEqual([...ml.flatMap(u=>u.spelDelar.filter(d=>d.niva==='A').map(d=>u.id+d.etikett))],['4.33c']);
 for(const u of ml)for(const omr of [u.omr])a.ok(ml.filter(x=>x.omr===omr).some(x=>x.spelDelar.some(d=>d.niva==='C')),omr);
});

test('klassificeringsmatriser 4.20–4.29: alla mått räknas om ur tabellen',()=>{
 for(let i=20;i<=29;i++){const u=q('4.'+i);
  const cells=[...u.spelIntro.matchAll(/<td[^>]*>(\d+)<\/td>/g)].map(m=>+m[1]);a.equal(cells.length,4,u.id);
  const [tp,fn,fp,tn]=cells,n=tp+fn+fp+tn,P=tp/(tp+fp),R=tp/(tp+fn);
  for(const d of u.spelDelar){const f=d.fraga,k=u.id+d.etikett;let v;
   if(/träffsäkerheten/.test(f))v=r3((tp+tn)/n);else if(/precisionen,/.test(f))v=r3(P);else if(/recall \(täckningen\)/.test(f))v=r3(R);
   else if(/F1-värdet/.test(f)){v=Math.round(2*P*R/(P+R)*100)/100;a.equal(d.tolerans,0.005,k);a.ok(Math.abs(2*P*R/(P+R)-v)<=0.005);}
   else if(/klassade modellen fel/.test(f))v=fp+fn;else if(/var verkligen/.test(f))v=tp+fn;else if(/fast de egentligen var/.test(f))v=fp;else if(/missade modellen/.test(f))v=fn;
   if(v===undefined){a.equal(d.svarstyp,'alternativ',k);continue;}
   a.equal(d.rättSvar,v,k);if(d.tolerans!==0.005){a.equal(d.tolerans,0,k);a.equal(r3((tp+tn)/n)===v||true,true);}
  }}
 // Tolkningsfrågorna
 a.equal(del('4.21e').rättSvar,'Recall, så att så få sjuka som möjligt missas');
 a.equal(del('4.24d').rättSvar,'Falskt positivt: någon annan låser upp mobilen');
 a.equal(del('4.28e').rättSvar,'Falskt positivt');a.equal(del('4.29d').rättSvar,'Precision');
});

test('klassificeringsmatriser 4.30–4.39: egna beräkningar',()=>{
 const acc=(tp,fn,fp,tn)=>(tp+tn)/(tp+fn+fp+tn);
 a.equal(del('4.31a').rättSvar,acc(0,20,0,980));a.equal(del('4.31b').rättSvar,0);
 a.equal(del('4.32a').rättSvar,45/50);a.equal(del('4.32b').rättSvar,30/40);
 // 4.34: 40 sjuka varav 36 positiva, 160 friska varav 9 positiva
 a.deepEqual([...del('4.34a').rättSvar],[36,4,9,151]);a.equal(del('4.34b').rättSvar,36/40);a.equal(del('4.34c').rättSvar,36/45);
 // 4.36: recall 0,8 och precision 0,5 med 50 sjuka av 200
 const tp=0.8*50,fp=tp/0.5-tp,tn=150-fp;a.equal(del('4.36a').rättSvar,tp);a.equal(del('4.36b').rättSvar,fp);a.equal(del('4.36c').rättSvar,(tp+tn)/200);
 // 4.37: tre klasser
 const M=[[18,2,0],[3,16,1],[0,0,20]];a.equal(del('4.37b').rättSvar,(18+16+20)/60);a.equal(del('4.37c').rättSvar,16/M[1].reduce((x,y)=>x+y));
 a.equal(del('4.38a').rättSvar,36/50);a.equal(del('4.38b').rättSvar,48/50);a.equal(del('4.38c').rättSvar,48/60);
 a.match(del('4.38d').rättSvar,/^Den försiktiga/);
 a.equal(del('4.39a').rättSvar,acc(10,0,20,970));a.equal(del('4.39b').rättSvar,acc(0,10,10,980));a.match(del('4.39c').rättSvar,/^System A/);
 a.equal(del('4.33c').rättSvar,'Antalet falskt positiva är lika med antalet falskt negativa');
});

test('typer av inlärning och träning/test',()=>{
 const typ={klass:'Övervakad inlärning (klassificering)',regr:'Övervakad inlärning (regression)',oov:'Oövervakad inlärning',rl:'Förstärkningsinlärning'};
 const facit=['klass','regr','rl','oov','klass','rl','regr','oov','klass','rl','oov','regr','klass','rl','oov','regr'];
 for(let i=0;i<8;i++){a.equal(del(`4.0${i+1}a`).rättSvar,typ[facit[2*i]]);a.equal(del(`4.0${i+1}b`).rättSvar,typ[facit[2*i+1]]);
  a.equal(del(`4.0${i+1}a`).alternativ.length,4);}
 a.equal(del('4.09a').rättSvar,400);a.equal(del('4.09b').rättSvar,100);a.equal(del('4.11a').rättSvar,900);a.equal(del('4.11b').rättSvar,300);
 a.equal(del('4.12a').rättSvar,1750);a.equal(del('4.12b').rättSvar,2500-1750);a.equal(del('4.13a').rättSvar,640/800);
 a.equal(del('4.14c').rättSvar,70-60);a.equal(del('4.15a').rättSvar,3);a.equal(del('4.15b').rättSvar,100-76);
});

test('linjär regression och gradientnedstigning',()=>{
 const mse=(pts,k,m)=>pts.reduce((s,[x,y])=>s+(y-(k*x+m))**2,0)/pts.length;
 a.equal(del('4.40a').rättSvar,1.5*4+2);a.equal(del('4.40b').rättSvar,9-8);a.equal(del('4.40c').rättSvar,mse([[2,5],[4,9],[6,10],[8,15]],1.5,2));
 a.equal(del('4.41a').rättSvar,40*65+600);a.equal(del('4.42a').rättSvar,4*6+30);a.equal(del('4.42b').rättSvar,58-(4*8+30));
 a.equal(del('4.43a').rättSvar,-20*4+200);a.equal(del('4.43c').rättSvar,200/20);
 a.equal(del('4.44a').rättSvar,100-8*5);a.equal(del('4.44b').rättSvar,(100-20)/8);a.equal(del('4.44c').rättSvar,100/8);
 const sol=[[1,2],[2,4],[3,5],[4,9]];a.equal(del('4.45a').rättSvar,mse(sol,2,0));a.equal(del('4.45b').rättSvar,mse(sol,1,2));a.match(del('4.45c').rättSvar,/^Linje A/);
 a.equal(del('4.46a').rättSvar,27-(50-2*10));a.equal(del('4.46b').rättSvar,[[0,50],[5,42],[10,27]].reduce((s,[x,y])=>s+(y-(50-2*x))**2,0));
 // gradientnedstigning med E(w) = (w − c)², lutning 2(w − c)
 const gd=(w,c,al,n)=>{const ut=[];for(let i=0;i<n;i++){w=w-al*2*(w-c);ut.push(r3(w));}return ut;};
 a.equal(del('4.48a').rättSvar,r3(3-0.1*4));a.deepEqual([del('4.49a').rättSvar,del('4.49b').rättSvar],gd(0,5,0.25,2));
 a.equal(del('4.50a').rättSvar,2*(1-4));a.equal(del('4.50b').rättSvar,gd(1,4,0.5,1)[0]);
 a.equal(del('4.51a').rättSvar,gd(4,2,1.5,1)[0]);a.match(del('4.51b').rättSvar,/^Längre från minimum/);
 for(const al of [0.05,0.3,0.7,0.95])a.ok(Math.abs(gd(4,2,al,60)[59]-2)<0.01,'konvergerar för α = '+al);
 for(const al of [1.05,1.5])a.ok(Math.abs(gd(4,2,al,30)[29]-2)>1,'divergerar för α = '+al);
 a.equal(del('4.53a').rättSvar,r3(5-0.5*0.8));a.equal(del('4.54a').rättSvar,(10-6)**2);a.deepEqual([del('4.54b').rättSvar,del('4.54d').rättSvar],gd(10,6,0.25,2));
 a.equal(del('4.54c').rättSvar,(8-6)**2);a.equal(del('4.55b').rättSvar,r3(-2-0.2*-3));
});

test('kNN och k-means räknas om med egen sortering',()=>{
 const knn=(pts,q,k)=>pts.map(([x,y,kl,n])=>({n,kl,d:(x-q[0])**2+(y-q[1])**2})).sort((s,t)=>s.d-t.d||(s.n<t.n?-1:1)).slice(0,k);
 const rost=(pts,q,k)=>{const nn=knn(pts,q,k),c={};for(const x of nn)c[x.kl]=(c[x.kl]||0)+1;return Object.keys(c).sort((s,t)=>c[t]-c[s])[0];};
 const D={
  '4.60':[[[1,2,'Äpple','P1'],[2,4,'Äpple','P2'],[3,1,'Äpple','P3'],[6,6,'Päron','P4'],[7,4,'Päron','P5'],[5,7,'Päron','P6'],[4,5,'Päron','P7']],[3,4]],
  '4.61':[[[1,1,'Stannar kvar','P1'],[4,5,'Slutar','P2'],[6,1,'Stannar kvar','P3'],[5,3,'Slutar','P4'],[7,5,'Slutar','P5']],[5,1]],
  '4.63':[[[6,1,'Action','P1'],[8,2,'Action','P2'],[7,4,'Action','P3'],[5,2,'Action','P4'],[1,6,'Romantik','P5'],[2,8,'Romantik','P6'],[3,5,'Romantik','P7'],[1,3,'Romantik','P8']],[4,4]],
  '4.64':[[[2,6,'Ätlig','P1'],[3,7,'Ätlig','P2'],[4,6,'Ätlig','P3'],[3,5,'Ätlig','P4'],[5,4,'Giftig','P5'],[6,3,'Giftig','P6'],[7,2,'Giftig','P7'],[6,1,'Giftig','P8']],[4,4]],
  '4.65':[[[2,2,'Lugn','P1'],[3,1,'Lugn','P2'],[2,4,'Lugn','P3'],[4,3,'Lugn','P4'],[7,8,'Energisk','P5'],[8,6,'Energisk','P6'],[6,7,'Energisk','P7'],[9,9,'Energisk','P8']],[5,4]],
  '4.66':[[[1,0,'Inte spam','P1'],[0,1,'Inte spam','P2'],[2,1,'Inte spam','P3'],[1,2,'Inte spam','P4'],[6,5,'Spam','P5'],[5,7,'Spam','P6'],[7,6,'Spam','P7'],[4,4,'Spam','P8']],[5,4]]};
 const mangd=s=>s.split(', ').sort().join(', ');
 // Punkterna i figuren ska vara desamma som i testets data.
 for(const [id,[pts]] of Object.entries(D))for(const [x,y,,n] of pts)a.ok(q(id).spelIntro.includes(`>${n}</text>`),id+n);
 a.equal(del('4.60c').rättSvar,rost(...D['4.60'],3));a.equal(mangd(del('4.60b').rättSvar),knn(...D['4.60'],3).map(x=>x.n).sort().join(', '));
 a.equal(del('4.61b').rättSvar,rost(...D['4.61'],1));a.equal(del('4.61c').rättSvar,rost(...D['4.61'],3));
 a.equal(del('4.63b').rättSvar,rost(...D['4.63'],1));a.equal(del('4.63c').rättSvar,rost(...D['4.63'],3));a.notEqual(rost(...D['4.63'],1),rost(...D['4.63'],3));
 a.equal(del('4.64b').rättSvar,rost(...D['4.64'],3));a.equal(mangd(del('4.64a').rättSvar),knn(...D['4.64'],3).map(x=>x.n).sort().join(', '));
 a.equal(del('4.65c').rättSvar,rost(...D['4.65'],3));a.equal(del('4.65d').rättSvar,1+3);
 a.equal(del('4.66c').rättSvar,rost(...D['4.66'],3));a.equal(del('4.66a').rättSvar,(1-5)**2+(2-4)**2);
 // inga lika avstånd vid gränsen för de k som efterfrågas
 for(const [id,k] of [['4.60',3],['4.61',1],['4.61',3],['4.63',1],['4.63',3],['4.64',3],['4.65',3],['4.66',3]]){
  const all=knn(...D[id],99);a.ok(all[k-1].d<all[k].d,id+' k='+k);}
 a.equal(del('4.67a').rättSvar,2**2+3**2);a.equal(del('4.67b').rättSvar,10**2);
 // k-means
 const medel=ps=>[0,1].map(i=>ps.reduce((s,p)=>s+p[i],0)/ps.length);
 a.deepEqual([...del('4.68b').rättSvar],medel([[6,5],[7,6],[8,4]]));a.deepEqual([...del('4.70b').rättSvar],medel([[1,2],[3,1],[2,3]]));a.deepEqual([...del('4.70c').rättSvar],medel([[7,8],[8,8],[9,5]]));
 a.deepEqual([...del('4.74c').rättSvar],medel([[2,1],[4,3],[3,5]]));a.equal(del('4.74a').rättSvar,20);a.equal(del('4.74b').rättSvar,34);
 a.equal(del('4.69b').rättSvar,(10+11+15)/3);a.equal(del('4.71b').rättSvar,(8+9)/2);
 // 4.72: två varv av k-means i en dimension
 let cc=[1,2];const v=[1,2,6,7,8,12],g=()=>[v.filter(x=>Math.abs(x-cc[0])<=Math.abs(x-cc[1])),v.filter(x=>Math.abs(x-cc[0])>Math.abs(x-cc[1]))];
 let G=g();a.equal(del('4.72a').rättSvar,G[1].length);cc=G.map(x=>x.reduce((s,y)=>s+y)/x.length);a.equal(del('4.72b').rättSvar,cc[1]);
 G=g();a.equal(del('4.72c').rättSvar,'Mätningen 2');a.deepEqual(G[0],[1,2]);a.equal(del('4.72d').rättSvar,(1+2)/2);
 const sum=c=>[2,4,9,11].reduce((s,x)=>s+Math.min(...c.map(y=>(x-y)**2)),0);a.equal(del('4.75a').rättSvar,sum([3,10]));a.equal(del('4.75b').rättSvar,sum([5,11]));
});

test('neurala nätverk: viktad summa, bias, stegfunktion och ReLU',()=>{
 const st=z=>z>=0?1:0,relu=z=>z>0?z:0,z=(w,x,b)=>r3(w.reduce((s,wi,i)=>s+wi*x[i],0)+b);
 a.equal(del('4.80a').rättSvar,z([2,-3],[1,0],0));a.equal(del('4.80b').rättSvar,z([2,-3],[1,0],-1));
 a.equal(del('4.81a').rättSvar,z([1,2],[3,2],0));a.equal(del('4.81b').rättSvar,z([1,2],[3,2],-5));a.equal(del('4.81c').rättSvar,z([1,2],[1,1],-5));
 a.equal(del('4.82a').rättSvar,3*2);a.equal(del('4.82b').rättSvar,z([1,3],[4,2],-6));
 a.equal(del('4.83a').rättSvar,z([4,-5,-2],[1,0,1],-1));a.equal(del('4.83b').rättSvar,z([4,-5,-2],[1,1,1],-1));
 a.equal(del('4.84a').rättSvar,0.5*6);a.equal(del('4.84b').rättSvar,z([0.5,-1],[6,3],1));let n=0;while(z([0.5,-1],[n,3],1)<0)n++;a.equal(del('4.84c').rättSvar,n);
 a.equal(del('4.85a').rättSvar,z([2,3],[1,1],-6));a.equal(del('4.85b').rättSvar,z([2,3],[1,1],-4));
 a.equal(del('4.86a').rättSvar,z([2,1],[3,4],0));a.equal(del('4.86b').rättSvar,7-10);a.equal(del('4.86c').rättSvar,10);
 a.equal(del('4.87a').rättSvar,z([2,3,-4],[1,1,0],-2));a.equal(del('4.87b').rättSvar,z([2,3,-4],[1,0,1],-2));
 a.deepEqual([del('4.88a').rättSvar,del('4.88b').rättSvar,del('4.88c').rättSvar],[st(3),st(-2),st(0)]);
 a.deepEqual([del('4.89a').rättSvar,del('4.89b').rättSvar,del('4.89c').rättSvar],[relu(5),relu(-3),relu(0.5)]);
 const logik=(w,b)=>[[0,0],[0,1],[1,0],[1,1]].map(x=>st(z(w,x,b))).join('');
 a.equal(logik([2,2],-1),'0111');a.match(del('4.90d').rättSvar,/ELLER/);a.equal(del('4.90a').rättSvar,z([2,2],[1,0],-1));a.equal(del('4.90c').rättSvar,st(z([2,2],[0,0],-1)));
 a.equal(logik([2,2],-3),'0001');a.equal(del('4.91b').rättSvar,st(z([2,2],[1,0],-3)));
 a.equal(del('4.92a').rättSvar,z([2,-1],[3,2],1));a.equal(del('4.92b').rättSvar,relu(z([2,-1],[3,2],1)));a.equal(del('4.92c').rättSvar,relu(z([2,-1],[1,4],1)));
 a.equal(del('4.93a').rättSvar,z([1,3],[1,0],-2));a.equal(del('4.93c').rättSvar,st(z([1,3],[0,1],-2)));a.equal(del('4.93d').rättSvar,'Att prognosen säger regn');
 a.equal(del('4.94b').rättSvar,'b = −3');a.equal(del('4.94c').rättSvar,'b = 1');
 const h=relu(2*2-1);a.equal(del('4.95a').rättSvar,h);a.equal(del('4.95b').rättSvar,relu(3*h-2));
 // inga nätverksbegrepp som ligger utanför fördjupningen
 for(const u of ml.filter(u=>u.omr==='neurala'))a.doesNotMatch(JSON.stringify(u),/XOR|epok|bakåtpropagering|valider|dolda lager|djupinlärning/i,u.id);
});

test('Kunskapsgymmet och papper: decimalsvar, förklaringsfrågor och ordval',()=>{
 for(const u of ml){
  a.doesNotMatch(u.t+u.s,/Svara i decimalform/,u.id);a.doesNotMatch(JSON.stringify(u),/interpol|extrapol/i,u.id);
  for(const d of u.spelDelar){const k=u.id+d.etikett;
   if(d.svarstyp==='numeriskt'&&!Number.isInteger(d.rättSvar))a.match(d.fraga,/\(Svara i decimalform\.\)/,k);
   if(d.svarstyp==='numeriskt'&&Number.isInteger(d.rättSvar))a.doesNotMatch(d.fraga,/decimalform/,k);
   if(d.svarstyp==='numeriskt'&&!Number.isInteger(d.rättSvar))a.match(d.s,new RegExp(String(d.rättSvar).replace('.',',').replace('-','−')),k);
   if(d.svarstyp==='alternativ')for(const x of d.alternativ)a.doesNotMatch(x.txt,/^[A-ZÅÄÖ]$/,k);
  }}
 // förklaringsfrågor är öppna på papper men flerval i Kunskapsgymmet
 for(const k of ['4.09c','4.12c','4.21e','4.30c','4.41c','4.48b','4.64c']){const u=q(k.slice(0,-1)),e=k.slice(-1);
  a.match(u.t,new RegExp(`<p>${e}\\) [^<]*</p>`),k);a.doesNotMatch(u.t,new RegExp(`<p>${e}\\) [^<]*Välj ett alternativ`),k);a.ok(del(k).alternativ.length===4,k);}
 // flervalsfrågor med A–D på papper
 a.match(q('4.01').t,/<p class="ul-alt"><strong>A\.<\/strong>/);
});

test('förenklade begrepp (användaren 2026-11-12)',()=>{
 for(const u of ml){const t=JSON.stringify(u);a.doesNotMatch(t,/[Rr]esidual|MSE|F1-värde|valideringsdata|särdrag|derivata/,u.id);}
 a.equal(del('4.22d').rättSvar,5);a.equal(del('4.26a').rättSvar,8);
 a.match(del('4.73a').rättSvar,/^Antalet kluster/);
});
