'use strict';
// AI-banken 2026-11-11: omgruppering i oinformerad och informerad sökning, och tolv nya
// uppgifter med BFS och DFS i träd och grafer (1.65–1.76). Svaren räknas om oberoende.
const {test}=require('node:test'),a=require('node:assert/strict'),fs=require('node:fs'),vm=require('node:vm');
const c={window:{}};vm.runInNewContext(fs.readFileSync('uppgifterai.js','utf8'),c);vm.runInNewContext(fs.readFileSync('strukturai.js','utf8'),c);
const bank=c.window.BANKAI,q=id=>bank.find(u=>u.id===id),del=k=>q(k.slice(0,-1)).spelDelar.find(d=>d.etikett===k.slice(-1));
const svar=k=>JSON.stringify(del(k).svarstyp==='alternativ'?del(k).alternativ.find(x=>x.ratt).txt:del(k).rättSvar);
const eq=(k,v)=>a.equal(svar(k),JSON.stringify(v),k);
const NYA=['1.65','1.66','1.67','1.68','1.69','1.70','1.71','1.72','1.73','1.74','1.75','1.76'];

// Egna simuleringar: barn och grannar från vänster/i bokstavsordning, varje nod en gång.
function bfsT(kids,s,goals){const q=[s],ut=[],far={},kö={};while(q.length){const n=q.shift();ut.push(n);if(goals.includes(n))break;for(const k of kids[n]||[]){far[k]=n;q.push(k);}kö[n]=[...q];}
 const v=[ut.at(-1)];while(far[v[0]])v.unshift(far[v[0]]);return{ut,v,kö};}
function dfsT(kids,s,goals){const ut=[],st=[];const go=n=>{ut.push(n);st.push(n);if(goals.includes(n)||(kids[n]||[]).some(go))return true;st.pop();return false;};go(s);return{ut,v:st};}
const adj=E=>{const g={};for(const[x,y]of E){(g[x]??=[]).push(y);(g[y]??=[]).push(x);}for(const k in g)g[k].sort();return g;};
function bfsG(E,s,mål){const g=adj(E),q=[s],sett=new Set([s]),ut=[],far={},nya={};while(q.length){const n=q.shift();ut.push(n);if(n===mål)break;nya[n]=[];for(const v of g[n])if(!sett.has(v)){sett.add(v);far[v]=n;q.push(v);nya[n].push(v);}}
 const v=[mål];while(far[v[0]])v.unshift(far[v[0]]);return{ut,v,nya};}
function dfsG(E,s,mål){const g=adj(E),sett=new Set(),ut=[],st=[];const go=n=>{sett.add(n);ut.push(n);st.push(n);if(n===mål||g[n].some(v=>!sett.has(v)&&go(v)))return true;st.pop();return false;};go(s);return{ut,v:st};}
const L=xs=>xs.join(', ');

test('struktur: oinformerad och informerad sökning, två delmoment per område',()=>{
 // Kapitel 4 Maskininlärning tillkom 2026-11-12 (ai-maskininlarning-2026-11-12.test.js).
 a.equal(JSON.stringify(c.window.KAPNAMNAI),JSON.stringify({1:'Oinformerad sökning',2:'Informerad sökning',3:'Spelträd och beskärning',4:'Maskininlärning'}));
 a.equal(JSON.stringify(Object.keys(c.window.OMRAI[1])),JSON.stringify(['ko_stack','bfs','dfs']));
 a.equal(JSON.stringify(Object.keys(c.window.OMRAI[2])),JSON.stringify(['prioritetsko','astar_varden','astar_sokning','viktade_vagar']));
 a.ok(!bank.some(u=>u.omr==='ko_sokning'),'kortet Kön under sökningen finns inte längre');
 const fam={};for(const u of bank.filter(u=>u.kap<3)){a.ok(c.window.OMRAI[u.kap][u.omr],u.id);(fam[u.omr]??=new Set()).add(u.familj);}
 for(const [omr,f] of Object.entries(fam))a.equal(f.size,2,omr);
 // Uppgifterna från Kön under sökningen hör nu till BFS eller DFS efter algoritm.
 const fran=bank.filter(u=>u.omrTidigare==='ko_sokning');a.equal(fran.length,17);
 for(const u of fran){const t=u.spelIntro+u.spelDelar.map(d=>d.fraga).join('');if(u.id==='1.58')a.equal(u.omr,'ko_stack');
  else a.equal(u.omr,/DFS|stack/.test(t)&&!/BFS/.test(t)?'dfs':'bfs',u.id);}
 for(const u of bank.filter(u=>u.familjTidigare))a.notEqual(u.familjTidigare,u.familj);
 // Träd och grafer: minst 13 uppgifter var för BFS och DFS.
 a.ok(bank.filter(u=>u.familj==='BFS i träd och grafer').length>=13);a.ok(bank.filter(u=>u.familj==='DFS i träd och grafer').length>=13);
});

test('nya uppgifter: format, nivåer och pappersversion utan svarsinstruktioner',()=>{
 for(const id of NYA){const u=q(id);a.ok(u,id);a.equal(u.spel,true);a.equal(u['självrättning'],true);a.match(u.familj,/^(BFS|DFS) i träd och grafer$/);
  a.match(u.t,/<svg/);a.doesNotMatch(u.t,/\((Skriv|Svara)[^)]*\)/,id);a.match(u.s,/facit-steglista/);
  u.spelDelar.forEach((d,i)=>{a.equal(JSON.stringify(u.rättSvar[i]),JSON.stringify(d.rättSvar));a.match(d.s,/facit-rubrik/);a.ok(d.ledtrad.length>20);
   if(d.svarFormat==='namnordning')a.match(d.fraga,/\((Skriv|Svara)[^)]*\)<\/p>/,id+d.etikett);
   for(const x of d.alternativ||[]){a.ok(x.kommentar.length>15,id+x.txt);a.doesNotMatch(x.txt,/^[A-Z]\d*$/,'ett ensamt nodnamn krockar med A–D på papper');}});}
 const parts=NYA.flatMap(id=>q(id).spelDelar);a.ok(parts.filter(d=>d.niva==='E').length/parts.length>=0.7,'mest E');
 a.ok(parts.some(d=>d.niva==='C'));
});

test('BFS i träd och grafer räknas om',()=>{
 const k65={S:['A','B','C'],A:['D','E'],B:['F'],C:['G','H'],D:['I'],F:['J'],G:['K']},r65=bfsT(k65,'S',['J']);
 eq('1.65a',k65.S.flatMap(n=>k65[n]||[]).length);eq('1.65b',L(r65.ut));eq('1.65c',L(r65.v));
 const k66={S:['A','B'],A:['C','D'],B:['E','F'],C:['G'],D:['H','I'],E:['J']},r66=bfsT(k66,'S',['H']);
 eq('1.66a',L(r66.kö.D));eq('1.66b',r66.ut.length);
 const E67=[['S','A'],['S','B'],['A','B'],['A','C'],['B','D'],['C','D'],['C','E'],['D','G'],['E','G']],r67=bfsG(E67,'S','G');
 a.equal(L(r67.nya.C),'E');eq('1.67a','Bara E');eq('1.67b',L(r67.ut));eq('1.67c',r67.v.length-1);
 const E68=[['S','A'],['A','B'],['B','C'],['C','M'],['S','D'],['D','E'],['E','M'],['D','F'],['F','M']],r68=bfsG(E68,'S','M');
 eq('1.68a',r68.v.length-1);eq('1.68b',L(r68.v));
 const tid={'D-E':12},t=v=>v.slice(1).reduce((s,x,i)=>s+(tid[v[i]+'-'+x]??2),0);a.equal(t(r68.v),16);a.equal(t(['S','D','F','M']),6);
 a.match(svar('1.68c'),/^"Nej/);
 const k69={S:['A','B'],A:['C','D'],B:['Q'],C:['P']};eq('1.69a','Målet '+bfsT(k69,'S',['P','Q']).ut.at(-1));eq('1.69b',bfsT(k69,'S',['P','Q']).ut.length);eq('1.69c','Målet '+dfsT(k69,'S',['P','Q']).ut.at(-1));
 const k70={S:['A','B','C'],A:['D'],B:['E','F'],C:['G'],E:['H']},r70=bfsT(k70,'S',['G']);eq('1.70a','Mappen '+r70.ut[4]);eq('1.70b',r70.ut.length);
});

test('DFS i träd och grafer räknas om',()=>{
 const k71={S:['A','B'],A:['C','D'],C:['E'],D:['F','G'],B:['H'],G:['M']},r71=dfsT(k71,'S',['M']);
 eq('1.71a',L(r71.ut));eq('1.71b',r71.ut.filter(n=>!r71.v.includes(n)).length);eq('1.71c',L(r71.v));
 // 1.72: stack där vänster barn hamnar överst; stacken skrivs nerifrån och upp.
 const k72={S:['A','B'],A:['C','D'],B:['E','F'],D:['G']},st=['S'],ut=[];let efterA;
 while(st.length){const n=st.pop();ut.push(n);if(n==='F')break;st.push(...[...(k72[n]||[])].reverse());if(n==='A')efterA=[...st];}
 eq('1.72a',L(efterA));eq('1.72b','Noden '+ut[5]);
 const E73=[['S','A'],['S','C'],['A','B'],['B','C'],['B','D'],['C','E'],['D','G'],['E','G']],r73=dfsG(E73,'S','G');
 eq('1.73a',L(r73.ut));eq('1.73b',r73.v.length-1);a.equal(bfsG(E73,'S','G').v.length-1,3);a.match(svar('1.73c'),/3 kanter/);
 const k74={S:['A','B','C'],A:['D','E'],D:['F'],B:['G','H'],H:['M'],C:['I']},r74=dfsT(k74,'S',['M']);
 const alla=new Set([...Object.keys(k74),...Object.values(k74).flat()]);
 eq('1.74a',r74.ut.length);eq('1.74b','Läget '+r74.ut[r74.ut.indexOf('F')+1]);eq('1.74c',alla.size-r74.ut.length);
 const k75={S:['A','B','C'],A:['D'],D:['M'],B:['E','F'],C:['G','H']};eq('1.75a',dfsT(k75,'S',['M']).ut.length);eq('1.75b',bfsT(k75,'S',['M']).ut.length);
 const k76={S:['A','B'],A:['C','D'],C:['E','F'],B:['M']},hö=Object.fromEntries(Object.entries(k76).map(([k,v])=>[k,[...v].reverse()]));
 eq('1.76a',dfsT(k76,'S',['M']).ut.length);eq('1.76b',dfsT(hö,'S',['M']).ut.length);eq('1.76c','I vilken ordning barnen undersöks');
});

test('figurerna visar träden och graferna som svaren räknas på',()=>{
 // Varje kant i figuren är en linje mellan två cirklar; jämför kantantalet med datan ovan.
 const kanter={'1.65':11,'1.66':10,'1.67':9,'1.68':9,'1.69':6,'1.70':8,'1.71':9,'1.72':7,'1.73':8,'1.74':10,'1.75':9,'1.76':7};
 for(const [id,n] of Object.entries(kanter)){const svg=q(id).spelIntro.match(/<svg[\s\S]*?<\/svg>/)[0];a.equal((svg.match(/<line /g)||[]).length,n,id);
  a.equal((svg.match(/<circle /g)||[]).length,n+(['1.67','1.68','1.73'].includes(id)?{'1.67':-2,'1.68':-1,'1.73':-1}[id]:1),id);}
});

test('validatorn hittar inget nytt',()=>{const r=require('./granska-uppgifter.js').granskaProjekt(process.cwd()).resultat.find(x=>x.fil==='uppgifterai.js');
 const ok=f=>(f.kod==='EXACT_TEXT_DUPLICATE'&&['3.04','3.05'].includes(f.id))||(f.kod==='VERY_SIMILAR_TEXT'&&['2.06','2.08'].includes(f.id));
 a.deepEqual(r.fynd.filter(f=>!ok(f)).map(f=>f.kod+' '+f.id+' '+(f.relateradeId||[]).join(',')),[]);});
