'use strict';
// AI-banken 2026-11-11, tredje omgången: lärarkommentarer (1.01, 1.03, 1.04) och 26 nya uppgifter.
// Svaren kontrolleras här med egna simuleringar, oberoende av byggskriptets Python-kod.
const {test}=require('node:test'),a=require('node:assert/strict'),fs=require('node:fs'),vm=require('node:vm');
const c={window:{}};vm.runInNewContext(fs.readFileSync('uppgifterai.js','utf8'),c);
const bank=c.window.BANKAI,q=id=>bank.find(u=>u.id===id);
const NYA=['1.10','1.11','1.12','1.13','1.14','1.15','1.16','1.17','1.18','1.19','2.12','2.13','2.14','2.15','2.16','2.17','2.18','2.19','2.20','2.21','2.22','3.06','3.07','3.08','3.09','3.10'];
const nm=([r,k])=>String.fromCharCode(65+r)+(k+1);
const U=[-1,0],R=[0,1],D=[1,0],L=[0,-1],STD=[U,R,D,L];
function find(rows,ch){for(let r=0;r<rows.length;r++){const k=rows[r].indexOf(ch);if(k>=0)return[r,k];}}
const open=(rows,[r,k])=>rows[r]?.[k]!==undefined&&rows[r][k]!=='#';
const nb=(rows,n,ord=STD)=>ord.map(([x,y])=>[n[0]+x,n[1]+y]).filter(v=>open(rows,v));
function bfs(rows,ord=STD){const s=find(rows,'S'),g=find(rows,'G'),qq=[s],seen=new Set([nm(s)]),par={},out=[],snaps=[];
 while(qq.length){const n=qq.shift();out.push(nm(n));if(nm(n)===nm(g)){snaps.push([nm(n),qq.map(nm)]);break;}
  for(const v of nb(rows,n,ord))if(!seen.has(nm(v))){seen.add(nm(v));par[nm(v)]=nm(n);qq.push(v);}snaps.push([nm(n),qq.map(nm)]);}
 const path=[nm(g)];while(par[path[0]])path.unshift(par[path[0]]);return{out,path,snaps};}
function dfs(rows,ord=STD){const s=find(rows,'S'),g=find(rows,'G'),seen=new Set(),out=[],stack=[];
 const go=n=>{seen.add(nm(n));out.push(nm(n));stack.push(nm(n));if(nm(n)===nm(g))return true;for(const v of nb(rows,n,ord))if(!seen.has(nm(v))&&go(v))return true;stack.pop();return false;};
 go(s);return{out,path:stack};}
function dist(rows,s){const d={[nm(s)]:0},qq=[s];while(qq.length){const n=qq.shift();for(const v of nb(rows,n))if(!(nm(v) in d)){d[nm(v)]=d[nm(n)]+1;qq.push(v);}}return d;}
const man=(x,y)=>Math.abs(x[0]-y[0])+Math.abs(x[1]-y[1]);
function astar(rows){const s=find(rows,'S'),gl=find(rows,'G'),g={[nm(s)]:0},cell={[nm(s)]:s},openS=new Set([nm(s)]),closed=new Set(),out=[],par={};
 while(openS.size){const n=[...openS].sort((x,y)=>(g[x]+man(cell[x],gl))-(g[y]+man(cell[y],gl))||man(cell[x],gl)-man(cell[y],gl)||x.localeCompare(y))[0];
  openS.delete(n);closed.add(n);out.push(n);if(n===nm(gl))break;
  for(const v of nb(rows,cell[n])){const k=nm(v);if(closed.has(k))continue;if(g[n]+1<(g[k]??1e9)){g[k]=g[n]+1;cell[k]=v;par[k]=n;openS.add(k);}}}
 const path=[nm(gl)];while(par[path[0]])path.unshift(par[path[0]]);return{out,path};}
function ucs(edges,s,t){const adj={};for(const[x,y,w]of edges){(adj[x]??=[]).push([y,w]);(adj[y]??=[]).push([x,w]);}
 const best={[s]:0},par={},done=[];while(true){const n=Object.keys(best).filter(k=>!done.some(d=>d[0]===k)).sort((x,y)=>best[x]-best[y]||x.localeCompare(y))[0];if(n===undefined)break;
  done.push([n,best[n]]);if(n===t)break;for(const[v,w]of adj[n])if(best[n]+w<(best[v]??1e9)&&!done.some(d=>d[0]===v)){best[v]=best[n]+w;par[v]=n;}}
 const path=[t];while(par[path[0]])path.unshift(par[path[0]]);return{done,path,cost:best[t]};}
function ab(t,max,al=-Infinity,be=Infinity,log=[]){if(typeof t==='number'){log.push(t);return t;}let v=max?-Infinity:Infinity;
 for(let i=0;i<t.length;i++){const x=ab(t[i],!max,al,be,log);if(max){v=Math.max(v,x);al=Math.max(al,v);}else{v=Math.min(v,x);be=Math.min(be,v);}if(al>=be)break;}return v;}
const mm=(t,max)=>typeof t==='number'?t:(max?Math.max:Math.min)(...t.map(x=>mm(x,!max)));
function astarG(edges,h,s,t){const adj={};for(const[x,y,w]of edges){(adj[x]??=[]).push([y,w]);(adj[y]??=[]).push([x,w]);}
 const g={[s]:0},op=new Set([s]),cl=new Set(),out=[];while(op.size){const n=[...op].sort((x,y)=>g[x]+h[x]-g[y]-h[y]||h[x]-h[y]||x.localeCompare(y))[0];op.delete(n);cl.add(n);out.push([n,g[n],h[n],g[n]+h[n]]);if(n===t)break;
  for(const[v,w]of adj[n])if(!cl.has(v)&&g[n]+w<(g[v]??1e9)){g[v]=g[n]+w;op.add(v);}}return{out,open:[...op]};}
function greedyG(edges,h,s,t){const adj={};for(const[x,y,w]of edges){(adj[x]??=[]).push([y,w]);(adj[y]??=[]).push([x,w]);}
 const g={[s]:0},par={},seen=new Set([s]),op=[s],out=[];while(op.length){op.sort((x,y)=>h[x]-h[y]||x.localeCompare(y));const n=op.shift();out.push(n);if(n===t)break;
  for(const[v,w]of adj[n])if(!seen.has(v)){seen.add(v);par[v]=n;g[v]=g[n]+w;op.push(v);}}const path=[t];while(par[path[0]])path.unshift(par[path[0]]);return{out,path,cost:g[t]};}
const has=(id,s)=>a.ok(q(id).s.includes(s),id+': '+s);

test('lärarkommentarer: enhetliga inledningar i labyrinter, träd och spelträd',()=>{
 for(const id of ['1.01','1.06','1.08'])a.match(q(id).spelIntro,/<p>Labyrinten söks igenom med BFS \(ordning ↑ → ↓ ←\)\.<\/p>/);
 for(const id of ['1.02','1.07'])a.match(q(id).spelIntro,/<p>Labyrinten söks igenom med DFS \(ordning ↑ → ↓ ←\)\.<\/p>/);
 for(const id of ['2.01','2.02','2.03','2.06','2.07','2.08','2.09','2.10','2.11'])a.match(q(id).spelIntro,/Labyrinten söks igenom med /,id);
 for(const id of ['1.04','1.05','1.09'])a.match(q(id).spelIntro,/Trädet söks igenom med /,id);
 for(const id of ['3.01','3.02','3.03','3.04','3.05'])a.match(q(id).spelIntro,/Spelträdet söks igenom med /,id);
 for(const u of bank){a.doesNotMatch(u.t,/<p>(BFS|DFS|A\*)\. /,u.id);a.ok(u.t.includes(u.spelIntro.replace(/<table[\s\S]*$/,'').slice(0,40)),u.id);}
});
test('lärarkommentarer: färgade start- och målnoder samt snygga tabeller',()=>{
 for(const id of ['1.04','1.05','1.09','1.14']){const t=q(id).spelIntro;a.match(t,/<circle[^>]*fill="#22a05a"/,id);a.match(t,/<circle[^>]*fill="#d94343"/,id);a.match(t,/>Start<\/text>/);a.match(t,/>Mål<\/text>/);a.doesNotMatch(t,/#fca5a5|r="23"/);}
 for(const u of bank){for(const h of [u.t,u.s,...u.spelDelar.flatMap(d=>[d.fraga,d.s])]){a.doesNotMatch(h,/<table>/,u.id);a.doesNotMatch(h,/<ol type="A">/,u.id);}}
 a.match(q('1.04').spelDelar[0].fraga,/<td style="text-align:left">–<\/td><td style="text-align:left">S<\/td>/);
 a.match(q('1.05').t,/Stacken efter uttaget/);a.match(q('1.05').spelDelar[1].fraga,/kvar i stacken/);
 a.match(q('1.03').spelIntro,/Noder läggs in och tas ut enligt följande/);a.match(q('2.04').spelIntro,/Noder läggs in i och tas ut ur en prioritetskö/);
 for(const id of ['1.03','1.04','1.05','2.04','2.05'])a.doesNotMatch(q(id).ledtrad,/upptäckte varje ny ruta/,id);
});
test('26 nya uppgifter med fullständiga och självständiga delar',()=>{
 a.ok(bank.length>=51);a.equal(new Set(bank.map(u=>u.id)).size,bank.length);
 const omr={};for(const id of NYA){const u=q(id);a.ok(u,id);omr[u.omr]=(omr[u.omr]||0)+1;
  a.equal(u.spel,false);a.equal(u['självrättning'],false);a.equal(u['miniräknare'],true);a.equal(u.geogebra,false);a.ok(u.ledtrad.length>20);
  a.match(u.s,/facit-steglista/);a.equal(u.traningsniva,Math.max(...u.spelDelar.map(d=>d.traningsniva)));
  for(const d of u.spelDelar){a.ok(d.fraga&&d.ledtrad&&d.s,id);a.match(d.s,/facit-rubrik/);a.match(d.s,/facit-svar/);a.equal(d.visaAlternativ,d.alternativ.length>0);
   a.ok(u.t.includes(d.fraga.replace('<p>','').slice(0,30)),id+d.etikett);
   if(d.alternativ.length){a.equal(d.alternativ.filter(x=>x.ratt).length>1,/Välj alla som stämmer/.test(d.fraga),id);a.match(d.fraga,/Välj (ett alternativ|alla som stämmer)/);
    a.equal(new Set(d.alternativ.map(x=>x.txt)).size,d.alternativ.length);for(const x of d.alternativ){a.ok(x.kommentar.length>15);a.ok(u.t.includes('</strong> '+x.txt+'</p>'),id);}}}}
 a.deepEqual(omr,{ko_stack:3,ko_sokning:2,bfs:2,dfs:3,prioritetsko:3,astar_varden:2,astar_sokning:3,viktade_vagar:3,minimax:3,alfa_beta:2});
 a.ok(NYA.filter(id=>q(id).traningsniva===1).length>=4);
});
test('köer och stackar',()=>{
 const run=(start,ops,take)=>{const s=[...start],o=[];for(const x of ops){if(x)s.push(x);else o.push(take(s));}return[o,s];};
 a.deepEqual(run(['K','M','P'],['R',0,0,'S'],s=>s.shift()),[['K','M'],['P','R','S']]);has('1.10','P, R, S.');
 a.deepEqual(run(['D','H','B'],[0,'X','Y',0,0],s=>s.pop()),[['B','Y','X'],['D','H']]);has('1.11','B, Y, X.');
 a.deepEqual(run([],['A','B',0,'C','D',0,0,0],s=>s.pop())[0],['B','D','C','A']);a.deepEqual(run([],['A','B',0,'C','D',0,0,0],s=>s.shift())[0],['A','B','C','D']);
 const pq=s=>{s.sort((x,y)=>x[1]-y[1]||x[0].localeCompare(y[0]));return s.shift()[0];};
 a.deepEqual(run([],[['M',4],['L',2],['K',4],0,['N',1],0,0,0],pq)[0],['L','N','K','M']);has('2.12','L, N, K, M.');
 a.deepEqual(run([],[['B',6],['D',8],['E',8],0,0],pq)[0],['B','D']);
 const T={P:[2,9],Q:[5,3],R:[4,5],T:[8,1]},by=f=>Object.keys(T).sort((x,y)=>f(T[x])-f(T[y]))[0];
 a.deepEqual([by(v=>v[1]),by(v=>v[0]+v[1])].join(','),'T,Q');
 a.equal(q('2.14').spelDelar.slice(1).map(d=>d.alternativ.find(x=>x.ratt).txt).join(','),'T,Q');has('2.14','P: 11, Q: 8, R: 9, T: 9.');
 const K={K:[4,6],L:[6,3],M:[3,8],N:[5,4]},o=Object.keys(K).sort((x,y)=>K[x][0]+K[x][1]-K[y][0]-K[y][1]||K[x][1]-K[y][1]);a.equal(o[0],'L');
 const efterL={K:10,M:11,N:9,P:7+1};a.equal(Object.keys(efterL).sort((x,y)=>efterL[x]-efterL[y])[0],'P');a.equal(q('2.18').spelDelar[1].alternativ.find(x=>x.ratt).txt,o[0]);has('2.18','P.');
});
test('BFS och DFS i labyrinter och sökträd',()=>{
 const r13=bfs(['S..','.#.','..G']);a.equal(r13.out.join(', '),'A1, A2, B1, A3, C1, B3, C2, C3');a.equal(r13.path.join(' → '),'A1 → A2 → A3 → B3 → C3');
 for(const[n,qq]of r13.snaps)has('1.13','<td style="text-align:left">'+n+'</td><td style="text-align:left">'+(qq.join(' ')||'tom')+'</td>');
 const kids={S:['A','B','C'],A:['D','E'],B:['F'],C:['G','H']},qq=['S'],out=[];while(qq.length){const n=qq.shift();out.push(n);if(n==='F')break;qq.push(...(kids[n]||[]));}
 a.deepEqual(out,['S','A','B','C','D','E','F']);a.deepEqual(qq,['G','H']);has('1.14','2 noder, G och H.');
 const m15=['S.#.','.#..','...#','#..G'],d15=dist(m15,[0,0]);a.deepEqual(Object.keys(d15).filter(k=>d15[k]===4).sort(),['C3','D2']);a.equal(d15.D4,6);a.equal(d15.A4,7);
 a.ok(!bfs(m15).out.includes('A4'));a.equal(q('1.15').spelDelar[2].alternativ.find(x=>x.ratt).txt,'A4');
 const m16=['S...','.##.','...G'];a.equal(bfs(m16).path.join(' → '),'A1 → A2 → A3 → A4 → B4 → C4');a.equal(bfs(m16).out.length,10);
 a.equal(bfs(m16,[L,D,R,U]).path.join(' → '),'A1 → B1 → C1 → C2 → C3 → C4');a.equal(q('1.16').spelDelar[2].alternativ.find(x=>x.ratt).txt,'A1 → B1 → C1 → C2 → C3 → C4');
 const r17=dfs(['S.#.','..#.','#...','.#.G']);a.equal(r17.out.join(', '),'A1, A2, B2, C2, C3, C4, B4, A4, D4');has('1.17',r17.out.join(', '));has('1.17',r17.path.join(' → '));
 const m18=['S...','.#..','.#.#','...G'],a18=dfs(m18),b18=dfs(m18,[D,R,U,L]);a.equal(a18.path.length-1,8);a.equal(b18.path.length-1,6);a.equal(a18.out.length,9);a.equal(b18.out.length,7);a.equal(bfs(m18).path.length-1,6);
 has('1.18',a18.path.join(' → ')+', 8 steg.');has('1.18',b18.path.join(' → ')+', 6 steg.');
 const m19=['S..#.','.#...','.#.#.','...#G'],r19=dfs(m19);a.equal(r19.out.join(', '),'A1, A2, A3, B3, B4, B5, A5, C5, D5');
 a.equal(m19.join('').replace(/#/g,'').length-r19.out.length,6);a.equal(r19.out[r19.out.indexOf('A5')+1],'C5');
});
test('h, g och f samt A* jämfört med BFS',()=>{
 const g215=[1,5];a.deepEqual([[0,1],[3,4],[2,4]].map(x=>man(x,g215)),[5,3,2]);has('2.15','P: h = 5, Q: h = 3, R: h = 2.');
 const m16=['S....','.###.','.#G#.','.#...','.....'];a.equal(man([0,2],[2,2]),2);a.equal(dist(m16,[0,0]).A3,2);a.equal(dist(m16,[2,2]).A3,8);
 const m17=['#..#G','#.#..','.....','S...#'],r17=astar(m17);a.equal(r17.out.join(', '),'D1, C1, C2, B2, A2, A3, C3, C4, B4, B5, A5');has('2.17',r17.out.join(', '));
 a.deepEqual(r17.out.filter(x=>!r17.path.includes(x)),['B2','A2','A3']);
 const m19=['S....','.....','..##.','....G'];a.equal(bfs(m19).out.length,18);a.equal(astar(m19).out.join(', '),'A1, A2, A3, A4, A5, B5, C5, D5');has('2.19','A1, A2, A3, A4, A5, B5, C5, D5.');
});
test('viktade vägar',()=>{
 const r20=ucs([['S','A',2],['S','B',5],['A','B',2],['A','C',6],['B','C',3],['B','D',3],['C','M',1],['D','M',4]],'S','M');a.equal(r20.cost,8);a.equal(r20.path.join(' → '),'S → A → B → C → M');has('2.20','S → A → B → C → M.');
 const r21=astarG([['S','A',1],['S','B',4],['A','C',2],['A','B',2],['B','D',1],['C','D',5],['C','M',6],['D','M',2]],{S:5,A:4,B:3,C:5,D:2,M:0},'S','M');
 a.equal(r21.out.map(x=>x.join(' ')).join(' | '),'S 0 5 5 | A 1 4 5 | B 3 3 6 | D 4 2 6 | M 6 0 6');a.deepEqual(r21.open.join(),'C');has('2.21','S → A → B → D → M, kostnad 6.');
 for(const x of r21.out)has('2.21','<td style="text-align:left">'+x.join('</td><td style="text-align:left">')+'</td>');
 const m22=['S33..','.#3#.','..3.G'],cost=p=>p.split(' → ').slice(1).reduce((s,x)=>{const ch=m22[x.charCodeAt(0)-65][+x.slice(1)-1];return s+(ch==='3'?3:1);},0);
 a.deepEqual(['A1 → A2 → A3 → A4 → A5 → B5 → C5','A1 → B1 → C1 → C2 → C3 → C4 → C5','A1 → A2 → A3 → B3 → C3 → C4 → C5'].map(cost),[10,8,14]);
});
test('minimax och alfa–beta',()=>{
 a.equal(mm([[3,8],[5,2,4],[6,7]],false),5);a.equal(mm([[[-2,4],1],[[3,-5],[0,2,-1]]],true),2);has('3.08','A = 1, B = 2, R = 2.');
 for(let x=-10;x<=20;x++)a.equal(Math.min(x,7)>4,x>=5);a.equal(mm([[4,6],[10,7]],true),7);
 let log=[];a.equal(ab([[5,9,7],[4,8,6],[10,3,11]],true,-Infinity,Infinity,log),5);a.deepEqual(log,[5,9,7,4,10,3]);has('3.09','L5, L6 och L9.');
 log=[];a.equal(ab([[6,9],[4,8,7]],true,-Infinity,Infinity,log),6);a.deepEqual(log,[6,9,4]);
 log=[];ab([[6,9],[8,7,4]],true,-Infinity,Infinity,log);a.deepEqual(log,[6,9,8,7,4]);has('3.10','3 löv, alltså alla.');
});
test('UCS ingår inte i kursen: inga uppgifter eller områdesnamn nämner UCS',()=>{
 for(const u of bank)a.doesNotMatch(JSON.stringify(u),/UCS|Dijkstra|[Uu]niform cost/,u.id);
 a.doesNotMatch(fs.readFileSync('strukturai.js','utf8'),/UCS/);
 const m=['S55G','.##.','....'];a.match(q('2.03').t,/girig bäst först och med A\*/);has('2.03','A1 → A2 → A3 → A4, kostnad 11.');has('2.03','A1 → B1 → C1 → C2 → C3 → C4 → B4 → A4, kostnad 7.');
});
test('validatorn hittar inget nytt i AI-banken',()=>{const r=require('./granska-uppgifter.js').granskaProjekt(process.cwd()).resultat.find(x=>x.fil==='uppgifterai.js');
 a.deepEqual(r.fynd.filter(f=>NYA.includes(f.id)||(f.relateradeId||[]).some(i=>NYA.includes(i))),[]);});
