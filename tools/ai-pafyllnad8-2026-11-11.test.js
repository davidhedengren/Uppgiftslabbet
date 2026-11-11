'use strict';
// AI-banken 2026-11-11, tionde omgången: 2.78–2.87 (heuristiken h och prioritetsköer) samt
// delmoment i kapitel 3. Svaren räknas om oberoende av byggskriptets Python-kod.
const {test}=require('node:test'),a=require('node:assert/strict'),fs=require('node:fs'),vm=require('node:vm');
const c={window:{}};vm.runInNewContext(fs.readFileSync('uppgifterai.js','utf8'),c);
const bank=c.window.BANKAI,q=id=>bank.find(u=>u.id===id),del=k=>q(k.slice(0,-1)).spelDelar.find(d=>d.etikett===k.slice(-1));
const svar=k=>JSON.stringify(del(k).svarstyp==='alternativ'?del(k).alternativ.find(x=>x.ratt).txt:del(k).rättSvar);
const eq=(k,v)=>a.equal(svar(k),JSON.stringify(v),k);
const NYA=['2.78','2.79','2.80','2.81','2.82','2.83','2.84','2.85','2.86','2.87'];
const man=([r1,k1],[r2,k2])=>Math.abs(r1-r2)+Math.abs(k1-k2);
// Prioritetskö: lägst (eller högst) värde, lika värden i bokstavsordning.
function prio(ops,hogst=false){const kö=[],ut=[];for(const o of ops){if(o){kö.push(o);continue;}kö.sort((x,y)=>(hogst?y[1]-x[1]:x[1]-y[1])||x[0].localeCompare(y[0]));ut.push(kö.shift());}return{ut:ut.map(x=>x[0]),kö};}
const adj=E=>{const g={};for(const[x,y,w]of E){(g[x]??=[]).push([y,w]);(g[y]??=[]).push([x,w]);}return g;};
function astar(E,h,s,m){const g=adj(E),G={[s]:0},öppen=new Set([s]),stängd=new Set(),ut=[];while(öppen.size){const n=[...öppen].sort((x,y)=>(G[x]+h[x])-(G[y]+h[y])||h[x]-h[y]||x.localeCompare(y))[0];
 öppen.delete(n);stängd.add(n);ut.push(n);if(n===m)break;for(const[v,w]of g[n])if(!stängd.has(v)&&G[n]+w<(G[v]??1e9)){G[v]=G[n]+w;öppen.add(v);}}return{ut,kostnad:G[m]};}
function girig(E,h,s,m){const g=adj(E),sett=new Set([s]),kö=[s],G={[s]:0},ut=[];while(kö.length){kö.sort((x,y)=>h[x]-h[y]||x.localeCompare(y));const n=kö.shift();ut.push(n);if(n===m)break;
 for(const[v,w]of g[n])if(!sett.has(v)){sett.add(v);G[v]=G[n]+w;kö.push(v);}}return{ut,kostnad:G[m]};}
const kortast=(E,s,m)=>astar(E,new Proxy({},{get:()=>0}),s,m).kostnad;

test('format, nivåer och pappersversion',()=>{
 for(const id of NYA){const u=q(id);a.ok(u,id);a.equal(u.spel,true);a.equal(u['självrättning'],true);a.equal(u.kap,2);
  a.doesNotMatch(u.t,/\((Skriv|Svara)[^)]*\)/,id);a.match(u.s,/facit-steglista/);
  u.spelDelar.forEach((d,i)=>{a.equal(JSON.stringify(u.rättSvar[i]),JSON.stringify(d.rättSvar));a.match(d.s,/facit-rubrik/);a.ok(d.ledtrad.length>20);
   for(const x of d.alternativ||[]){a.ok(x.kommentar.length>15,id+x.txt);a.doesNotMatch(x.txt,/^[A-Z]\d*$/,id+': ensamt nodnamn');}});}
 const fam=id=>q(id).familj;
 for(const id of ['2.78','2.79','2.80','2.81'])a.equal(fam(id),'Heuristiken h');
 for(const id of ['2.82','2.83','2.84'])a.equal(fam(id),'Uttag ur en prioritetskö');
 for(const id of ['2.85','2.86','2.87'])a.equal(fam(id),'Prioritetskön i girig bäst först och A*');
 const parts=NYA.flatMap(id=>q(id).spelDelar);a.ok(parts.filter(d=>d.niva==='E').length/parts.length>=0.8);
 for(const id of ['2.78','2.79','2.86','2.87'])a.match(q(id).t,/<svg/,id+' har figur');
});

test('heuristiken h räknas om',()=>{
 const E78=[['S','A',4],['S','B',3],['A','M',5],['B','C',4],['C','M',3],['A','C',2]],h78={S:7,A:4,B:6,C:3,M:0};
 for(const n of Object.keys(h78))a.ok(h78[n]<=kortast(E78,n,'M'),'fågelvägen överskattar inte '+n);
 eq('2.78a','Orten A');eq('2.78b',kortast(E78,'A','M')-h78.A);a.match(svar('2.78c'),/uppskattning/);
 const M=['S.....','.#.##.','...G..','.##...','......'],G=[2,3];
 eq('2.79a',man([4,0],G));eq('2.79b',0);
 eq('2.79c',[[-1,0],[1,0],[0,-1],[0,1]].map(([x,y])=>[G[0]+x,G[1]+y]).filter(([r,k])=>M[r]?.[k]&&M[r][k]!=='#').length);
 const rad=ch=>ch.charCodeAt(0)-65;eq('2.80a',man([rad('B'),2],[rad('F'),9]));eq('2.80b',man([rad('C'),2],[rad('F'),9]));
 a.match(svar('2.80c'),/exakt 1/);a.equal(svar('2.81b'),JSON.stringify('h minskar med 1'));
});

test('prioritetsköer räknas om',()=>{
 const r82=prio([['E',3],['F',1],['H',5],null,['M',2],null,null]);eq('2.82a',r82.ut.join(', '));a.equal(r82.kö[0][0],'H');eq('2.82b','Historia');
 const r83=prio([['A',7],['B',12],['C',9],null,['D',15],['E',8],null,null],true);eq('2.83a',r83.ut.join(', '));eq('2.83b',Math.max(...r83.kö.map(x=>x[1])));
 const start=[['K',5],['L',3],['N',8],['P',3]];eq('2.84a',prio([...start,null,null,null]).ut.join(', '));
 eq('2.84b','Noden '+prio([...start,null,null,['R',4],null]).ut.at(-1));
});

test('girig bäst först och A* räknas om',()=>{
 const rad={A:[2,6],B:[5,3],C:[1,5],D:[4,4]},min=f=>Object.keys(rad).sort((x,y)=>f(x)-f(y)||x.localeCompare(y))[0];
 eq('2.85a','Noden '+min(n=>rad[n][1]));eq('2.85b',rad.B[0]+rad.B[1]);eq('2.85c','Noden '+min(n=>rad[n][0]+rad[n][1]));
 const E86=[['S','A',2],['S','B',4],['A','C',5],['B','C',1],['C','M',2]],h86={S:6,A:6,B:3,C:2,M:0},r86=astar(E86,h86,'S','M');
 eq('2.86a',2+h86.A);eq('2.86b','Noden '+r86.ut[1]);eq('2.86c',r86.ut.join(', '));
 for(const n of Object.keys(h86))a.ok(h86[n]<=kortast(E86,n,'M'));
 const E87=[['S','A',2],['S','B',1],['A','M',6],['B','C',2],['C','M',2]],h87={S:4,A:1,B:3,C:2,M:0};
 const g87=girig(E87,h87,'S','M'),a87=astar(E87,h87,'S','M');
 eq('2.87a','Noden '+g87.ut[1]);eq('2.87b',g87.kostnad);eq('2.87c',a87.ut.join(', '));eq('2.87d',a87.kostnad);
 a.ok(a87.kostnad<g87.kostnad);for(const n of Object.keys(h87))a.ok(h87[n]<=kortast(E87,n,'M'));
});

test('kapitel 3: två delmoment per kort, gamla delmoment sparade',()=>{
 const fam={};for(const u of bank.filter(u=>u.kap===3)){(fam[u.omr]??=new Set()).add(u.familj);a.ok(u.familjTidigare===undefined||u.familjTidigare!==u.familj);}
 a.equal(JSON.stringify([...fam.minimax].sort()),JSON.stringify(['Minimaxvärden och bästa drag','Tolka och resonera om minimax']));
 a.equal(JSON.stringify([...fam.alfa_beta].sort()),JSON.stringify(['Beskärningens idé','Rotvärde och beskurna löv']));
 // Begreppsfrågorna och beskärning med stöd ligger i Beskärningens idé.
 for(const id of ['3.14','3.56','3.57','3.58','3.59','3.60','3.61'])a.equal(q(id).familj,'Beskärningens idé',id);
 for(const id of ['3.43','3.44','3.45','3.46','3.50','3.54'])a.equal(q(id).familj,'Tolka och resonera om minimax',id);
 // Alla delmoment i banken har minst 8 uppgifter.
 const n={};for(const u of bank)n[u.omr+'|'+u.familj]=(n[u.omr+'|'+u.familj]||0)+1;
 for(const [k,v] of Object.entries(n))a.ok(v>=8,k+': '+v);
});

test('validatorn hittar inget nytt',()=>{const r=require('./granska-uppgifter.js').granskaProjekt(process.cwd()).resultat.find(x=>x.fil==='uppgifterai.js');
 const ok=f=>(f.kod==='EXACT_TEXT_DUPLICATE'&&['3.04','3.05'].includes(f.id))||(f.kod==='VERY_SIMILAR_TEXT'&&['2.06','2.08'].includes(f.id));
 a.deepEqual(r.fynd.filter(f=>!ok(f)).map(f=>f.kod+' '+f.id+' '+(f.relateradeId||[]).join(',')),[]);});
