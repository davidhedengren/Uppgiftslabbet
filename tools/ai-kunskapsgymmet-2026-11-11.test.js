'use strict';
// AI-banken 2026-11-11, sjätte omgången: 30 självrättande uppgifter i Kunskapsgymmets format.
// Testet kontrollerar formatet och räknar om varje svar med egna simuleringar.
const {test}=require('node:test'),a=require('node:assert/strict'),fs=require('node:fs'),vm=require('node:vm');
const c={window:{}};vm.runInNewContext(fs.readFileSync('uppgifterai.js','utf8'),c);
// Efterbearbetningen 2026-11-12 skriver ensamma namn som ”Noden B”/”Rutan P” (och 1.22a ”Efter uttaget av A”).
// Testerna nedan räknar fram bokstäverna, så prefixet tas bort här. Själva prefixen kontrolleras i
// tools/ai-efterbearbetning-2026-11-12.test.js.
c.window.BANKAI=JSON.parse(JSON.stringify(c.window.BANKAI).replace(/(?:Noden|Rutan|Efter uttaget av) ([A-Z])(?=["<.:])/g,'$1'));
const bank=c.window.BANKAI,q=id=>bank.find(u=>u.id===id);
const nm=([r,k])=>String.fromCharCode(65+r)+(k+1),STD=[[-1,0],[0,1],[1,0],[0,-1]];
const find=(m,ch)=>{for(let r=0;r<m.length;r++){const k=m[r].indexOf(ch);if(k>=0)return[r,k];}};
const nb=(m,n)=>STD.map(([x,y])=>[n[0]+x,n[1]+y]).filter(([r,k])=>m[r]?.[k]!==undefined&&m[r][k]!=='#');
const cost=(m,[r,k])=>/\d/.test(m[r][k])?+m[r][k]:1,man=(x,y)=>Math.abs(x[0]-y[0])+Math.abs(x[1]-y[1]);
function bfs(m){const s=find(m,'S'),g=find(m,'G'),qq=[s],seen=new Set([nm(s)]),par={},out=[];let longest=1;while(qq.length){const n=qq.shift();out.push(nm(n));if(nm(n)===nm(g))break;for(const v of nb(m,n))if(!seen.has(nm(v))){seen.add(nm(v));par[nm(v)]=nm(n);qq.push(v);}longest=Math.max(longest,qq.length);}
 const path=[nm(g)];while(par[path[0]])path.unshift(par[path[0]]);return{out,path,longest};}
function dist(m,s){const d={[nm(s)]:0},qq=[s];while(qq.length){const n=qq.shift();for(const v of nb(m,n))if(!(nm(v) in d)){d[nm(v)]=d[nm(n)]+1;qq.push(v);}}return d;}
function dfs(m){const s=find(m,'S'),g=find(m,'G'),seen=new Set(),out=[],st=[];const go=n=>{seen.add(nm(n));out.push(nm(n));st.push(nm(n));if(nm(n)===nm(g))return true;for(const v of nb(m,n))if(!seen.has(nm(v))&&go(v))return true;st.pop();return false;};go(s);return{out,path:st};}
function search(m,mode){const s=find(m,'S'),g=find(m,'G'),G={[nm(s)]:0},cell={[nm(s)]:s},par={},op=new Set([nm(s)]),cl=new Set(),seen=new Set([nm(s)]),out=[];const h=k=>man(cell[k],g);
 while(op.size){const n=[...op].sort((x,y)=>mode==='greedy'?h(x)-h(y)||x.localeCompare(y):(G[x]+h(x))-(G[y]+h(y))||h(x)-h(y)||x.localeCompare(y))[0];op.delete(n);cl.add(n);out.push(n);if(n===nm(g))break;
  for(const v of nb(m,cell[n])){const k=nm(v),alt=G[n]+cost(m,v);if(mode==='greedy'){if(!seen.has(k)){seen.add(k);G[k]=alt;cell[k]=v;par[k]=n;op.add(k);}}else if(!cl.has(k)&&alt<(G[k]??1e9)){G[k]=alt;cell[k]=v;par[k]=n;op.add(k);}}}
 return{out,cost:G[nm(g)]};}
function cheapest(m,s,t){const d={[nm(s)]:0},cell={[nm(s)]:s},done=new Set();while(true){const n=Object.keys(d).filter(k=>!done.has(k)).sort((x,y)=>d[x]-d[y])[0];if(!n)break;done.add(n);for(const v of nb(m,cell[n])){const k=nm(v);if(d[n]+cost(m,v)<(d[k]??1e9)){d[k]=d[n]+cost(m,v);cell[k]=v;}}}return d[nm(t)];}
function graph(edges,start,goal,h){const adj={};for(const[x,y,w]of edges){(adj[x]??=[]).push([y,w]);(adj[y]??=[]).push([x,w]);}const G={[start]:0},op=new Set([start]),cl=new Set(),out=[],par={};
 while(op.size){const n=[...op].sort((x,y)=>(G[x]+(h?h[x]:0))-(G[y]+(h?h[y]:0))||(h?h[x]-h[y]:0)||x.localeCompare(y))[0];op.delete(n);cl.add(n);out.push(n);if(n===goal)break;for(const[v,w]of adj[n])if(!cl.has(v)&&G[n]+w<(G[v]??1e9)){G[v]=G[n]+w;par[v]=n;op.add(v);}}
 const path=[goal];while(par[path[0]])path.unshift(par[path[0]]);return{out,cost:G[goal],path};}
const mm=(t,max)=>typeof t==='number'?t:(max?Math.max:Math.min)(...t.map(x=>mm(x,!max)));
function ab(t,max){let leaf=0;const named=t=>typeof t==='number'?{n:'L'+(++leaf),v:t}:t.map(named),tree=named(t),cut=[],seen=[],firstCut=[];const names=t=>t.n?[t.n]:t.flatMap(names);
 function go(t,max,al,be,path){if(t.n){seen.push(t.n);return t.v;}let v=max?-Infinity:Infinity;for(let i=0;i<t.length;i++){const x=go(t[i],!max,al,be,path.concat(i));if(max){v=Math.max(v,x);al=Math.max(al,v);}else{v=Math.min(v,x);be=Math.min(be,v);}
  if(al>=be&&i+1<t.length){if(!firstCut.length)firstCut.push(path);cut.push(...t.slice(i+1).flatMap(names));break;}}return v;}
 return{v:go(tree,max,-Infinity,Infinity,[]),cut,seen,firstCut:firstCut[0]};}
const NYA=['1.32','1.33','1.34','1.35','1.36','1.37','1.38','1.39','1.40','1.41','1.42','1.43','2.35','2.36','2.37','2.38','2.39','2.40','2.41','2.42','2.43','2.44','2.45','2.46','3.31','3.32','3.33','3.34','3.35','3.36'];
const ans=id=>Array.from(q(id).rättSvar),eq=(id,want)=>a.equal(JSON.stringify(ans(id)),JSON.stringify(want),id);

test('Kunskapsgymmets format: självrättande delar med entydiga svar',()=>{
 for(const id of NYA){const u=q(id);a.ok(u,id);a.equal(u.spel,true);a.equal(u['självrättning'],true);a.equal(u.svarstyp,'flera_delar');a.equal(u.svarsstruktur,'ordnad');
  a.equal(u.rättSvar.length,u.spelDelar.length);a.equal(JSON.stringify(u.svarEtiketter),JSON.stringify(u.spelDelar.map(d=>d.etikett)));a.equal(u.svarFormat.length,u.spelDelar.length);
  u.spelDelar.forEach((d,i)=>{a.equal(d.spel,true);a.equal(d['självrättning'],true);a.equal(u.rättSvar[i],d.rättSvar,id);a.ok(Number.isInteger(d.traningsniva));a.match(d.s,/facit-svar/);a.ok(d.ledtrad.length>20);
   if(d.svarstyp==='numeriskt'){a.ok(Number.isInteger(d.rättSvar),id);a.equal(d.tolerans,0);a.equal(d.svarFormat,'numeriskt');a.equal(d.alternativ.length,0);a.ok(d.s.includes('<strong>Svar:</strong> '+String(d.rättSvar).replace('-','−')+'.'),id);}
   else{a.equal(d.svarstyp,'alternativ',id);const r=d.alternativ.filter(x=>x.ratt);a.equal(r.length,1,id);a.equal(d.rättSvar,r[0].txt);a.equal(d.visaAlternativ,true);a.match(d.fraga,/Välj ett alternativ\./);
    a.equal(new Set(d.alternativ.map(x=>x.txt)).size,d.alternativ.length,id);for(const x of d.alternativ){a.ok(x.kommentar.length>12,id+x.txt);a.ok(u.t.includes('</strong> '+x.txt+'</p>'),id);}}});}
 // Områdena räknas som när omgången byggdes; omgrupperingen 2026-11-11 sparar dem i omrTidigare.
 const o0=u=>u.omrTidigare||u.omr,omr={};for(const id of NYA)omr[o0(q(id))]=(omr[o0(q(id))]||0)+1;a.ok(Object.values(omr).every(n=>n===3));a.equal(Object.keys(omr).length,10);
});
test('köer, stackar och prioritetsköer',()=>{
 eq('1.32',['C',3]);eq('1.33',[3,'F']);eq('1.34',['R','Q']);
 const pq=[],o=[];for(const x of [['G',6],['H',2],['K',5],0,['M',1],0,0]){if(x)pq.push(x);else{pq.sort((p,r)=>p[1]-r[1]);o.push(pq.shift()[0]);}}a.equal(o[2],'K');eq('2.35',['K',pq[0][1]]);
 const T={P:[4,7],Q:[6,3],R:[2,9],S:[5,6]},best=Object.keys(T).sort((x,y)=>T[x][0]+T[x][1]-T[y][0]-T[y][1])[0];eq('2.36',[best,T[best][0]+T[best][1]]);
 const U={B:[3,5],D:[4,4],F:[6,2],H:[2,7]},f=k=>U[k][0]+U[k][1],lo=Math.min(...Object.keys(U).map(f)),tie=Object.keys(U).filter(k=>f(k)===lo);eq('2.37',[tie.length,tie.sort((x,y)=>U[x][1]-U[y][1])[0]]);
});
test('köer och stackar under sökning i träd och labyrinter',()=>{
 const k35={S:['A','B','C'],A:['D','E'],B:['F'],C:['G','H'],E:['I']},q35=['S'],o35=[];let L=1;while(q35.length){const n=q35.shift();o35.push(n);if(n==='I')break;q35.push(...(k35[n]||[]));L=Math.max(L,q35.length);}eq('1.35',[L,o35[o35.length-2]]);
 const k36={S:['A','B'],A:['C','D'],B:['E','F'],E:['G']},s36=['S'],o36=[];let top=null;while(s36.length){const n=s36.pop();o36.push(n);if(n==='G')break;s36.push(...[...(k36[n]||[])].reverse());if(n==='A')top=s36[s36.length-1];}eq('1.36',[top,o36.length]);
 const r37=bfs(['S...','.#.#','...G']);eq('1.37',['A2 och B1',r37.longest,r37.out[r37.out.length-2]]);
});
test('BFS och DFS i labyrinter',()=>{
 const r38=bfs(['S..#.','.#...','...#.','.#..G']);eq('1.38',[r38.path.length-1,r38.out[4],r38.out.length]);
 const m39=['.#...','S..#.','.#...','...#G'],r39=bfs(m39),d39=dist(m39,find(m39,'S'));eq('1.39',[Object.values(d39).filter(v=>v===2).length,r39.path.length-1,r39.out[3]]);
 const m40=['S.#.','...#','#...','..#G'],r40=bfs(m40),d40=dist(m40,find(m40,'S'));eq('1.40',[r40.out[5],r40.out.length,Object.values(d40).filter(v=>v===3).length]);
 for(const[id,m,k]of [['1.41',['S..#','.#..','.#.#','...G'],5],['1.43',['S.#..','.....','#.##.','...#G'],6]]){const r=dfs(m),b=bfs(m);eq(id,[r.out[k-1],r.out.length,r.path.length-1,r.path.length===b.path.length?'Ja':'Nej']);}
 const k42={S:['A','B'],A:['C','D'],B:['E','F'],D:['G','H']},o42=[];const go=n=>{o42.push(n);return n==='F'||(k42[n]||[]).some(go);};go('S');eq('1.42',[o42[4],o42.length]);
});
test('g, h och f samt A*',()=>{
 const m38=['S...#','.##..','...#.','#...G'],P=[0,3],g38=find(m38,'G'),gv=dist(m38,[0,0])[nm(P)];eq('2.38',[gv,man(P,g38),gv+man(P,g38)]);
 const m39=['S3..','.#3.','..#G'],P39=[0,3],g39=cheapest(m39,[0,0],P39);eq('2.39',[g39,man(P39,find(m39,'G')),g39+man(P39,find(m39,'G'))]);
 const m40=['S....','.###.','.#G..','.###.','.....'],P40=[2,0],G40=find(m40,'G');eq('2.40',[dist(m40,[0,0])[nm(P40)],man(P40,G40),dist(m40,G40)[nm(P40)]-man(P40,G40)]);
 a.ok(ans('2.40')[2]>=4,'tydlig skillnad mellan h och verklig väg');
 for(const[id,m,k]of [['2.41',['S..#','.#..','...G'],4],['2.43',['...G','.#.#','S...'],5]]){const r=search(m,'astar');eq(id,[r.out[k-1],r.out.length,r.cost]);}
 const m42=['.....G','3.3...','3.3...','S.....'];eq('2.42',[search(m42,'greedy').cost,search(m42,'astar').cost]);a.ok(ans('2.42')[0]>ans('2.42')[1]);
});
test('viktade vägar',()=>{
 const m44=['S4..','.4.3','...G'];eq('2.44',[[[0,1],[0,2],[0,3],[1,3],[2,3]].reduce((s,c)=>s+cost(m44,c),0),cheapest(m44,[0,0],[2,3])]);
 const r45=graph([['S','A',3],['S','B',1],['A','C',2],['B','C',6],['B','A',1],['C','M',2],['A','M',8]],'S','M');eq('2.45',[r45.cost,r45.path.length-1]);
 const h={S:6,A:4,B:5,C:2,D:3,M:0},r46=graph([['S','A',2],['S','B',3],['A','C',3],['B','D',2],['C','M',2],['D','M',4],['A','B',1]],'S','M',h);eq('2.46',[r46.out[1],r46.out.length,r46.cost]);
});
test('minimax och alfa–beta',()=>{
 eq('3.31',[Math.min(5,6),mm([[7,3],[5,6],[2,8]],true),'Draget till B']);
 eq('3.32',[mm([6,2],false),mm([[[4,1],[6,2]],[[3,9],[5,0]]],false),'Draget till A']);
 eq('3.33',[mm([[2,-3],[-1,4],1],false),mm([[[2,-3],[-1,4],1],[[5,-2],[0,3]]],true),'Draget till B']);
 const r34=ab([[5,8],[3,9],[6,4]],true);eq('3.34',[r34.v,r34.cut.length,r34.cut[0]]);
 const r35=ab([[[6,1],[7,2]],[[4,4],[8,5]]],true);eq('3.35',[r35.v,r35.cut.length,r35.seen.length]);a.ok(r35.cut.length>=3);
 const r36=ab([[2,6,4],[7,1],[8,3,5]],false);eq('3.36',[r36.v,r36.cut.length,'ABC'[r36.firstCut[0]]]);
 for(const[t,m]of [[[[5,8],[3,9],[6,4]],true],[[[[6,1],[7,2]],[[4,4],[8,5]]],true],[[[2,6,4],[7,1],[8,3,5]],false]])a.equal(ab(t,m).v,mm(t,m));
});
test('validatorn hittar inget i den nya omgången',()=>{const r=require('./granska-uppgifter.js').granskaProjekt(process.cwd()).resultat.find(x=>x.fil==='uppgifterai.js');
 a.deepEqual(r.fynd.filter(f=>NYA.includes(f.id)||(f.relateradeId||[]).some(i=>NYA.includes(i))),[]);});
