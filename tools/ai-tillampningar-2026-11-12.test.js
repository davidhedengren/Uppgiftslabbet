'use strict';
// AI-banken 2026-11-12: tio C-uppgifter med AI-tillämpningar (1.107, 1.108, 2.117–2.122, 3.79, 3.80).
// Svaren räknas om oberoende av byggskriptet. Förklaringsfrågorna är öppna på papper och flerval i Kunskapsgymmet.
const {test}=require('node:test'),a=require('node:assert/strict'),fs=require('node:fs'),vm=require('node:vm');
const c={window:{}};vm.runInNewContext(fs.readFileSync('uppgifterai.js','utf8'),c);
const bank=c.window.BANKAI,q=id=>bank.find(u=>u.id===id),del=k=>q(k.slice(0,-1)).spelDelar.find(d=>d.etikett===k.slice(-1));
const rätt=k=>{const d=del(k);return d.svarstyp==='alternativ'?d.alternativ.filter(x=>x.ratt).map(x=>x.txt).join('|'):JSON.stringify(d.rättSvar);};
const NYA=['1.107','1.108','2.117','2.118','2.119','2.120','2.121','2.122','3.79','3.80'];
const ÖPPNA={'1.107':['d'],'1.108':['d'],'2.117':['e'],'2.118':['d'],'2.119':['d'],'2.120':['d'],'2.121':['d'],'2.122':['c','d'],'3.79':['c'],'3.80':['e']};
const L=xs=>JSON.stringify(xs.join(', '));
const adj=E=>{const g={};for(const[x,y,w=1]of E){(g[x]??=[]).push([y,w]);(g[y]??=[]).push([x,w]);}for(const k in g)g[k].sort((p,r)=>p[0].localeCompare(r[0]));return g;};
function bfsG(E,s,m){const g=adj(E),kö=[s],sett=new Set([s]),far={},ut=[],d={[s]:0};while(kö.length){const n=kö.shift();ut.push(n);if(n===m)break;for(const[v]of g[n])if(!sett.has(v)){sett.add(v);far[v]=n;d[v]=d[n]+1;kö.push(v);}}
 const väg=[m];while(far[väg[0]])väg.unshift(far[väg[0]]);return{ut,väg,d};}
function astarG(E,h,s,m){const g=adj(E),G={[s]:0},öppen=new Set([s]),stängd=new Set(),ut=[];while(öppen.size){const n=[...öppen].sort((x,y)=>G[x]+h[x]-G[y]-h[y]||h[x]-h[y]||x.localeCompare(y))[0];
 öppen.delete(n);stängd.add(n);ut.push(n);if(n===m)break;for(const[v,w]of g[n])if(!stängd.has(v)&&G[n]+w<(G[v]??1e9)){G[v]=G[n]+w;öppen.add(v);}}return{ut,kost:G[m]};}
function girigG(E,h,s,m){const g=adj(E),sett=new Set([s]),kö=[s],G={[s]:0},ut=[];while(kö.length){kö.sort((x,y)=>h[x]-h[y]||x.localeCompare(y));const n=kö.shift();ut.push(n);if(n===m)break;
 for(const[v,w]of g[n])if(!sett.has(v)){sett.add(v);G[v]=G[n]+w;kö.push(v);}}return{ut,kost:G[m]};}
const kortast=(E,s,m)=>astarG(E,new Proxy({},{get:()=>0}),s,m).kost;

test('format: självrättande i Kunskapsgymmet, öppna förklaringsfrågor på papper',()=>{
 for(const id of NYA){const u=q(id);a.ok(u,id);a.equal(u.spel,true);a.equal(u['självrättning'],true);a.match(u.t,/<svg|<table/,id);
  a.ok(u.spelDelar.some(d=>['C','A'].includes(d.niva)),id+': har C eller A');
  for(const e of ÖPPNA[id]){const d=del(id+e);a.equal(d.svarstyp,'alternativ',id+e);a.ok(d.alternativ.length>=4);
   for(const x of d.alternativ){a.ok(x.kommentar.length>15,id+e);a.ok(!u.t.includes('</strong> '+x.txt+'</p>'),id+e+': alternativen syns inte på papper');}
   const para=u.t.match(new RegExp(`<p>${e}\\) ([^<]*)</p>`));a.ok(para,id+e);a.doesNotMatch(para[1],/Välj ett alternativ/,id+e);
   const start=u.s.indexOf(`<span class="facit-mark">${e})</span>`),slut=u.s.indexOf('<div class="facit-del">',start);
   a.doesNotMatch(u.s.slice(start,slut<0?undefined:slut),/<ul>/,id+e+': pappersfacit utan alternativlista');}}
});

test('BFS och DFS i nätverk och hus räknas om',()=>{
 const E=[['A','C'],['A','D'],['A','E'],['C','F'],['D','F'],['D','G'],['E','H'],['F','I'],['G','I'],['H','J'],['I','B'],['J','B']],r=bfsG(E,'A','B');
 a.equal(JSON.stringify(del('1.107a').rättSvar.split(', ').sort()),JSON.stringify(Object.keys(r.d).filter(k=>r.d[k]===2).sort()));
 a.equal(rätt('1.107b'),String(r.d.B));a.equal(rätt('1.107c'),L(r.väg));a.match(rätt('1.107d'),/ett steg bort före/);
 const kids={S:['A','B'],A:['C','D'],C:['E'],E:['F'],B:['G']},mål=['F','G'];
 const kö=['S'],bu=[];while(kö.length){const n=kö.shift();bu.push(n);if(mål.includes(n))break;kö.push(...(kids[n]||[]));}
 const du=[];const gå=n=>{du.push(n);return mål.includes(n)||(kids[n]||[]).some(gå);};gå('S');
 a.equal(rätt('1.108a'),'Rummet '+bu.at(-1));a.equal(rätt('1.108b'),String(bu.length));a.equal(rätt('1.108c'),String(du.length));a.match(rätt('1.108d'),/^BFS/);
});

test('navigeringsapp, reseplanerare och åttapussel räknas om',()=>{
 const E=[['S','A',4],['A','M',8],['S','B',3],['B','C',3],['C','M',3],['B','D',5],['D','M',2]],h={S:7,A:5,B:6,C:3,D:2,M:0},r=astarG(E,h,'S','M');
 for(const n in h)a.ok(h[n]<=kortast(E,n,'M'),'h överskattar inte '+n);
 a.equal(rätt('2.117a'),JSON.stringify([4+h.A,3+h.B]));a.equal(rätt('2.117b'),'Korsningen '+r.ut[1]);a.equal(rätt('2.117c'),L(r.ut));a.equal(rätt('2.117d'),String(r.kost));
 const E2=[['S','A',6],['A','M',15],['S','B',4],['B','C',4],['C','M',4]],h2={S:8,A:2,B:7,C:3,M:0},gr=girigG(E2,h2,'S','M'),as=astarG(E2,h2,'S','M');
 for(const n in h2)a.ok(h2[n]<=kortast(E2,n,'M'));
 a.equal(rätt('2.120a'),'Hållplatsen '+gr.ut[1]);a.equal(rätt('2.120b'),String(gr.kost));a.equal(rätt('2.120c'),String(as.kost));
 const mål='12345678_',hf=b=>[...b].filter((x,i)=>x!=='_'&&x!==mål[i]).length,start='1234_6758';
 const nya=[[-1,0],[0,1],[1,0],[0,-1]].map(([dr,dc])=>{const i=start.indexOf('_'),r=Math.floor(i/3)+dr,c2=i%3+dc;if(r<0||r>2||c2<0||c2>2)return null;const j=r*3+c2,b=[...start];[b[i],b[j]]=[b[j],b[i]];return b.join('');}).filter(Boolean);
 a.equal(rätt('2.121a'),String(hf(start)));a.equal(rätt('2.121b'),JSON.stringify(nya.map(hf)));
 const bäst=nya.map(hf).indexOf(Math.min(...nya.map(hf)));a.equal(rätt('2.121c'),'Läge '+(bäst+1));
 // h överskattar aldrig: jämför med verkligt antal drag (BFS i pusslets lägen) för startläget och grannarna.
 const drag=b=>{const i=b.indexOf('_'),ut=[];for(const[dr,dc]of[[-1,0],[0,1],[1,0],[0,-1]]){const r=Math.floor(i/3)+dr,cc=i%3+dc;if(r<0||r>2||cc<0||cc>2)continue;const j=r*3+cc,x=[...b];[x[i],x[j]]=[x[j],x[i]];ut.push(x.join(''));}return ut;};
 const avst=b=>{const d={[b]:0},kö=[b];while(kö.length){const n=kö.shift();if(n===mål)return d[n];for(const v of drag(n))if(!(v in d)){d[v]=d[n]+1;kö.push(v);}}};
 for(const b of[start,...nya])a.ok(hf(b)<=avst(b),b);
});

test('lager, drönare och triage räknas om',()=>{
 const grid=rows=>{const ch=x=>{for(let r=0;r<rows.length;r++){const k=rows[r].indexOf(x);if(k>=0)return[r,k];}};return{rows,s:ch('S'),g:ch('G')};};
 const nb=(Lb,[r,k])=>[[-1,0],[0,1],[1,0],[0,-1]].map(([x,y])=>[r+x,k+y]).filter(([x,y])=>Lb.rows[x]?.[y]!==undefined&&Lb.rows[x][y]!=='#');
 const k=([r,c])=>String.fromCharCode(65+r)+(c+1),man=(p,q2)=>Math.abs(p[0]-q2[0])+Math.abs(p[1]-q2[1]);
 const bfs=(Lb,mål=Lb.g)=>{const kö=[Lb.s],d={[k(Lb.s)]:0},ut=[];while(kö.length){const n=kö.shift();ut.push(n);if(k(n)===k(mål))break;for(const v of nb(Lb,n))if(!(k(v) in d)){d[k(v)]=d[k(n)]+1;kö.push(v);}}return{ut,d};};
 const astar=Lb=>{const G={[k(Lb.s)]:0},cell={[k(Lb.s)]:Lb.s},öppen=new Set([k(Lb.s)]),stängd=new Set(),ut=[],h=x=>man(cell[x],Lb.g);
  while(öppen.size){const n=[...öppen].sort((x,y)=>G[x]+h(x)-G[y]-h(y)||h(x)-h(y)||x.localeCompare(y))[0];öppen.delete(n);stängd.add(n);ut.push(n);if(n===k(Lb.g))break;
   for(const v of nb(Lb,cell[n])){const kk=k(v);if(!stängd.has(kk)&&G[n]+1<(G[kk]??1e9)){G[kk]=G[n]+1;cell[kk]=v;öppen.add(kk);}}}return ut;};
 const lag=grid(['S......','.##.##.','.......','.##.##.','......G']),rb=bfs(lag);
 a.equal(rätt('2.118a'),String(rb.d[k(lag.g)]));a.equal(rätt('2.118b'),String(rb.ut.length));a.equal(rätt('2.118c'),String(astar(lag).length));
 a.ok(astar(lag).length<rb.ut.length/2);
 const dr=grid(['S..#..','...#..','.....G']),P=[0,4];
 a.equal(rätt('2.119a'),String(man(P,dr.g)));const gP=bfs(dr,P).d[k(P)];a.equal(rätt('2.119b'),String(gP));a.equal(rätt('2.119c'),String(gP+man(P,dr.g)));
 a.ok(gP>man(dr.s,P),'g går runt förbudszonen');
 // Triage: en läkare, 10 minuter per besök, lägst prioritet först, sedan tidigast ankomst.
 const pat=[['A',0,2],['B',2,3],['C',6,1],['D',14,2],['E',19,1],['F',27,2],['G',35,1]];let t=0;const väntar=[],kvar=[...pat],ordn=[],start={};
 while(kvar.length||väntar.length){while(kvar.length&&kvar[0][1]<=t)väntar.push(kvar.shift());if(!väntar.length){t=kvar[0][1];continue;}
  väntar.sort((x,y)=>x[2]-y[2]||x[1]-y[1]);const x=väntar.shift();ordn.push(x[0]);start[x[0]]=t;t+=10;}
 a.equal(rätt('2.122a'),L(ordn));a.equal(rätt('2.122b'),String(start.B-2));a.match(rätt('2.122c'),/mer akut prioritet/);a.match(rätt('2.122d'),/längre patienten har väntat/);
 a.equal(del('2.122d').niva,'A');
});

test('luffarschack och schackdator räknas om',()=>{
 const LIN=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]],vinst=b=>{for(const[x,y,z]of LIN)if(b[x]!=='.'&&b[x]===b[y]&&b[y]===b[z])return b[x];return null;};
 const mm=(b,tur)=>{const w=vinst(b);if(w)return w==='X'?1:-1;if(!b.includes('.'))return 0;const v=[...b].map((c2,i)=>c2==='.'?mm(b.slice(0,i)+tur+b.slice(i+1),tur==='X'?'O':'X'):null).filter(x=>x!==null);return tur==='X'?Math.max(...v):Math.min(...v);};
 const B0='X..X.OOXO',tomma=[...B0].map((x,i)=>x==='.'?i:-1).filter(i=>i>=0),värde=tomma.map(i=>mm(B0.slice(0,i)+'X'+B0.slice(i+1),'O'));
 a.equal(rätt('3.79a'),String(värde[0]));a.equal(rätt('3.79b'),'Draget till '+'ABC'[värde.indexOf(Math.max(...värde))]);a.equal(JSON.stringify(värde),'[-1,0,-1]');
 a.ok(tomma.some(i=>vinst(B0.slice(0,i)+'O'+B0.slice(i+1))==='O'),'O hotar att vinna');a.match(rätt('3.79c'),/kan O vinna/);
 const ab=(t,max,al=-Infinity,be=Infinity,logg=[])=>{if(typeof t==='number'){logg.push(t);return t;}let v=max?-Infinity:Infinity;for(const k of t){const x=ab(k,!max,al,be,logg);if(max){v=Math.max(v,x);al=Math.max(al,v);}else{v=Math.min(v,x);be=Math.min(be,v);}if(al>=be)break;}return v;};
 const V=[[3,5],[1,4],[2,0,6]],l1=[];a.equal(ab(V,true,-Infinity,Infinity,l1),3);a.equal(l1.length,4);
 a.equal(rätt('3.80a'),'3');a.match(rätt('3.80b'),/^Nej/);a.equal(rätt('3.80c'),'1');
 const l2=[];ab([V[1],V[2],V[0]],true,-Infinity,Infinity,l2);a.equal(rätt('3.80d'),String(l2.length));a.match(rätt('3.80e'),/fler grenar kan beskäras/);
});

test('validatorn hittar inget nytt',()=>{const r=require('./granska-uppgifter.js').granskaProjekt(process.cwd()).resultat.find(x=>x.fil==='uppgifterai.js');
 const ok=f=>(f.kod==='EXACT_TEXT_DUPLICATE'&&['3.04','3.05'].includes(f.id))||(f.kod==='VERY_SIMILAR_TEXT'&&['2.06','2.08'].includes(f.id));
 a.deepEqual(r.fynd.filter(f=>!ok(f)).map(f=>f.kod+' '+f.id+' '+(f.relateradeId||[]).join(',')),[]);});
