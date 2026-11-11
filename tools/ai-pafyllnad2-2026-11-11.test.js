'use strict';
// AI-banken 2026-11-11, fjärde omgången: 20 nya uppgifter (två per område) utan UCS.
// Svaren kontrolleras med egna simuleringar, oberoende av byggskriptens Python-kod.
const {test}=require('node:test'),a=require('node:assert/strict'),fs=require('node:fs'),vm=require('node:vm');
const c={window:{}};vm.runInNewContext(fs.readFileSync('uppgifterai.js','utf8'),c);
const bank=c.window.BANKAI,q=id=>bank.find(u=>u.id===id),has=(id,s)=>a.ok(q(id).s.includes(s),id+': '+s);
const NYA=['1.20','1.21','1.22','1.23','1.24','1.25','1.26','1.27','2.23','2.24','2.25','2.26','2.27','2.28','2.29','2.30','3.11','3.12','3.13','3.14'];
const nm=([r,k])=>String.fromCharCode(65+r)+(k+1),STD=[[-1,0],[0,1],[1,0],[0,-1]];
const find=(m,ch)=>{for(let r=0;r<m.length;r++){const k=m[r].indexOf(ch);if(k>=0)return[r,k];}};
const nb=(m,n)=>STD.map(([x,y])=>[n[0]+x,n[1]+y]).filter(([r,k])=>m[r]?.[k]!==undefined&&m[r][k]!=='#');
const cost=(m,[r,k])=>/\d/.test(m[r][k])?+m[r][k]:1,man=(x,y)=>Math.abs(x[0]-y[0])+Math.abs(x[1]-y[1]);
function bfs(m){const s=find(m,'S'),g=find(m,'G'),qq=[s],seen=new Set([nm(s)]),par={},out=[],snaps=[];while(qq.length){const n=qq.shift();out.push(nm(n));if(nm(n)===nm(g))break;for(const v of nb(m,n))if(!seen.has(nm(v))){seen.add(nm(v));par[nm(v)]=nm(n);qq.push(v);}snaps.push(qq.map(nm));}
 const path=[nm(g)];while(par[path[0]])path.unshift(par[path[0]]);return{out,path,snaps};}
function dfs(m){const s=find(m,'S'),g=find(m,'G'),seen=new Set(),out=[],st=[];const go=n=>{seen.add(nm(n));out.push(nm(n));st.push(nm(n));if(nm(n)===nm(g))return true;for(const v of nb(m,n))if(!seen.has(nm(v))&&go(v))return true;st.pop();return false;};go(s);return{out,path:st};}
function best(m,s,t){const d={[nm(s)]:0},cell={[nm(s)]:s},done=new Set();while(true){const n=Object.keys(d).filter(k=>!done.has(k)).sort((x,y)=>d[x]-d[y])[0];if(!n)break;done.add(n);for(const v of nb(m,cell[n])){const k=nm(v);if(d[n]+cost(m,v)<(d[k]??1e9)){d[k]=d[n]+cost(m,v);cell[k]=v;}}}return d[nm(t)];}
function search(m,mode){const s=find(m,'S'),g=find(m,'G'),G={[nm(s)]:0},cell={[nm(s)]:s},par={},op=new Set([nm(s)]),cl=new Set(),seen=new Set([nm(s)]),out=[];const h=k=>man(cell[k],g);
 while(op.size){const n=[...op].sort((x,y)=>mode==='greedy'?h(x)-h(y)||x.localeCompare(y):(G[x]+h(x))-(G[y]+h(y))||h(x)-h(y)||x.localeCompare(y))[0];op.delete(n);cl.add(n);out.push(n);if(n===nm(g))break;
  for(const v of nb(m,cell[n])){const k=nm(v),alt=G[n]+cost(m,v);if(mode==='greedy'){if(!seen.has(k)){seen.add(k);G[k]=alt;cell[k]=v;par[k]=n;op.add(k);}}else if(!cl.has(k)&&alt<(G[k]??1e9)){G[k]=alt;cell[k]=v;par[k]=n;op.add(k);}}}
 const path=[nm(g)];while(par[path[0]])path.unshift(par[path[0]]);return{out,path,cost:G[nm(g)],open:[...op].sort(),G,h};}
function graph(edges,h,s,t,mode){const adj={};for(const[x,y,w]of edges){(adj[x]??=[]).push([y,w]);(adj[y]??=[]).push([x,w]);}const G={[s]:0},par={},op=new Set([s]),cl=new Set(),seen=new Set([s]),out=[];
 while(op.size){const n=[...op].sort((x,y)=>mode==='greedy'?h[x]-h[y]||x.localeCompare(y):G[x]+h[x]-G[y]-h[y]||h[x]-h[y]||x.localeCompare(y))[0];op.delete(n);cl.add(n);out.push(n+' '+G[n]+' '+h[n]+' '+(G[n]+h[n]));if(n===t)break;
  for(const[v,w]of adj[n]){if(mode==='greedy'){if(!seen.has(v)){seen.add(v);G[v]=G[n]+w;par[v]=n;op.add(v);}}else if(!cl.has(v)&&G[n]+w<(G[v]??1e9)){G[v]=G[n]+w;par[v]=n;op.add(v);}}}
 const path=[t];while(par[path[0]])path.unshift(par[path[0]]);return{out,path,cost:G[t]};}
function ab(t,max,al=-Infinity,be=Infinity,log=[]){if(typeof t==='number'){log.push(t);return t;}let v=max?-Infinity:Infinity;for(const x of t){const r=ab(x,!max,al,be,log);if(max){v=Math.max(v,r);al=Math.max(al,v);}else{v=Math.min(v,r);be=Math.min(be,v);}if(al>=be)break;}return v;}
const mm=(t,max)=>typeof t==='number'?t:(max?Math.max:Math.min)(...t.map(x=>mm(x,!max)));

test('20 nya uppgifter, två per område, med fullständiga delar',()=>{
 a.equal(new Set(bank.map(u=>u.id)).size,bank.length);a.ok(bank.length>=71);const omr={};
 for(const id of NYA){const u=q(id);a.ok(u,id);omr[u.omr]=(omr[u.omr]||0)+1;a.equal(u.spel,true);a.equal(u['självrättning'],true);a.equal(u['miniräknare'],true);a.equal(u.geogebra,false);a.match(u.s,/facit-steglista/);
  a.doesNotMatch(JSON.stringify(u),/UCS|Dijkstra/);a.equal(u.traningsniva,Math.max(...u.spelDelar.map(d=>d.traningsniva)));
  for(const d of u.spelDelar){a.ok(d.fraga&&d.ledtrad&&d.s);a.match(d.s,/facit-rubrik/);a.match(d.s,/facit-svar/);a.equal(d.visaAlternativ,d.alternativ.length>0);
   if(d.alternativ.length){a.equal(d.alternativ.filter(x=>x.ratt).length>1,/Välj alla som stämmer/.test(d.fraga),id);a.equal(new Set(d.alternativ.map(x=>x.txt)).size,d.alternativ.length);for(const x of d.alternativ){a.ok(x.kommentar.length>15,id);a.ok(u.t.includes('</strong> '+x.txt+'</p>'),id);}}}}
 a.equal(JSON.stringify(omr),JSON.stringify({ko_stack:2,ko_sokning:2,bfs:2,dfs:2,prioritetsko:2,astar_varden:2,astar_sokning:2,viktade_vagar:2,minimax:2,alfa_beta:2}));
});
test('köer, stackar och prioritetsköer',()=>{
 const f=[],s=[],of=[],os=[];for(const x of ['P','Q',0,'R','S',0,'T']){if(x){f.push(x);s.push(x);}else{of.push(f.shift());os.push(s.pop());}}
 a.equal([of,os,f,s].map(x=>x.join('')).join('|'),'PQ|QS|RST|PRT');has('1.21','Kön: P och Q. Stacken: Q och S.');
 const pq=(rule)=>{const k=[],o=[];let t=0;for(const x of [['P',3],['Q',5],['M',3],0,['S',1],['K',3],0,0,0]){if(x)k.push([...x,t++]);else{k.sort((p,r)=>p[1]-r[1]||(rule==='alfa'?p[0].localeCompare(r[0]):p[2]-r[2]));o.push(k.shift()[0]);}}return o.join(', ');};
 a.equal(pq('ordning'),'P, S, M, K');a.equal(pq('alfa').split(', ')[0],'M');has('2.23','P, S, M, K.');
 a.equal(q('2.24').spelDelar.slice(0,3).map(d=>d.alternativ.find(x=>x.ratt).txt).join(''),'ACB');
 a.equal(q('1.20').spelDelar.map(d=>d.alternativ.find(x=>x.ratt).txt).join(','),'FIFO-kö,Stack,FIFO-kö,Stack');
});
test('BFS, DFS och köer i träd och grafer',()=>{
 const kids={S:['A','B'],A:['C','D'],B:['E'],C:['F']},qq=['S'],o=[];while(qq.length){const n=qq.shift();o.push(n);if(n==='F')break;qq.push(...(kids[n]||[]));}a.equal(o.join(''),'SABCDEF');
 const ali=['S','A','C','D','B','F'];a.equal(ali.indexOf('F'),5);a.equal(o.indexOf('F'),6);a.equal(q('1.22').spelDelar[0].alternativ.find(x=>x.ratt).txt,'A');
 const adj={S:['A','B'],A:['C','S'],B:['C','S'],C:['A','B','G'],G:['C']},q2=['S'],seen=new Set(['S']),o2=[];let addC=0;while(q2.length){const n=q2.shift();o2.push(n);if(n==='G')break;for(const v of [...adj[n]].sort())if(!seen.has(v)){seen.add(v);q2.push(v);if(v==='C')addC++;}}
 a.equal(o2.join(''),'SABCG');a.equal(addC,1);
 const r24=bfs(['S.#..','..#.#','.....','#.##.','...#G']);a.equal(r24.out.slice(0,6).join(', '),'A1, A2, B1, B2, C1, C2');a.equal(r24.path.length-1,8);a.equal(r24.out.length,18);has('1.24','A1, A2, B1, B2, C1, C2.');
 const r25=bfs(['..#..','.....','#.S.#','..#..','G....']);a.equal(r25.snaps[0].join(', '),'B3, C4, C2');a.equal(r25.path.length-1,4);
 const k6={S:['A','B'],A:['C','D'],B:['G'],C:['E','F']},d6=[];const go=n=>{d6.push(n);if(n==='G')return true;return(k6[n]||[]).some(go);};go('S');a.equal(d6.join(''),'SACEFDBG');
 const q6=['S'],b6=[];while(q6.length){const n=q6.shift();b6.push(n);if(n==='G')break;q6.push(...(k6[n]||[]));}a.equal(b6.join(''),'SABCDG');
 const r27=dfs(['S.#','..#','#.G']);a.equal(r27.out.join(' '),'A1 A2 B2 C2 C3');a.equal(q('1.27').spelDelar[0].alternativ.find(x=>x.ratt).txt,r27.out[2]);
});
test('g, h och f samt girig bäst först och A*',()=>{
 const m25=['S3..','.3#.','...G'];a.equal(best(m25,[0,0],[0,2]),4);a.equal(man([0,2],[2,3]),3);a.equal(q('2.25').spelDelar[1].alternativ.find(x=>x.ratt).txt,'7');
 const m26=['S..#G','.#.#.','.#...','...#.'],s26=[0,0],g26=[0,4];a.equal([[0,2],[2,3],[3,2]].map(x=>best(m26,s26,x)+'/'+man(x,g26)).join(' '),'2/2 5/3 5/5');a.equal(best(m26,[0,2],g26),6);
 const m27=['....G','44...','44...','S....'],gr=search(m27,'greedy'),as=search(m27,'astar');a.equal(gr.path.join(' '),'D1 C1 B1 A1 A2 A3 A4 A5');a.equal(gr.cost,13);a.equal(as.cost,7);a.equal(as.out[1],'D2');
 has('2.27','Girig bäst först: 13. A*: 7.');
 const m28=['S...','.#..','...G'],r28=search(m28,'astar');a.equal(r28.out.join(', '),'A1, A2, A3, A4, B4, C4');a.equal(r28.open.join(),'B1,B3');for(const k of r28.open)a.equal(r28.G[k]+r28.h(k),5);
 const m29=['S3..','.33.','..3.','3..G'];a.equal(best(m29,[0,0],[3,3]),6);a.equal(['A2','A3','A4','B4','C4','D4'].reduce((s,x)=>s+(m29[x.charCodeAt(0)-65][+x[1]-1]==='3'?3:1),0),8);
 const E=[['S','A',2],['A','M',9],['S','B',3],['B','C',2],['C','M',2]],h={S:4,A:2,B:4,C:2,M:0};
 const g30=graph(E,h,'S','M','greedy'),a30=graph(E,h,'S','M','astar');a.equal(g30.path.join(''),'SAM');a.equal(g30.cost,11);a.equal(a30.path.join(''),'SBCM');a.equal(a30.cost,7);
 a.equal(a30.out.join(' | '),'S 0 4 4 | A 2 2 4 | B 3 4 7 | C 5 2 7 | M 7 0 7');
 for(const[x,y,w]of E)a.ok(Math.abs(h[x]-h[y])<=w,'h ska vara konsekvent');
});
test('minimax och alfa–beta',()=>{
 a.equal(mm([[3,7],[5,6],[2,9]],true),5);a.equal(mm([[3,7],[5,6],[2,1]],true),5);a.equal(mm([[8,7],[5,6],[2,9]],true),7);
 a.equal(mm([[[4,2],[1,6]],[[3,5],[7,0]]],true),5);has('3.12','R → B → E → lövet 5 (L6).');
 let log=[];a.equal(ab([[3,5],[6,1,4],[2,8]],false,-Infinity,Infinity,log),5);a.equal(log.join(),'3,5,6,2,8');has('3.13','L4 och L5.');
 log=[];a.equal(ab([[2,7],[1,3]],true,-Infinity,Infinity,log),2);a.equal(log.join(),'2,7,1');log=[];ab([[2,7],[3,1]],true,-Infinity,Infinity,log);a.equal(log.length,4);
});
test('validatorn hittar inget i den nya omgången',()=>{const r=require('./granska-uppgifter.js').granskaProjekt(process.cwd()).resultat.find(x=>x.fil==='uppgifterai.js');
 a.deepEqual(r.fynd.filter(f=>NYA.includes(f.id)||(f.relateradeId||[]).some(i=>NYA.includes(i))),[]);});
