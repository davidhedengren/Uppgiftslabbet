'use strict';
// AI-banken 2026-11-11, sjunde omgången: 30 självrättande uppgifter, mest E-nivå.
// Svaren räknas om med egna simuleringar, oberoende av byggskriptens Python-kod.
const {test}=require('node:test'),a=require('node:assert/strict'),fs=require('node:fs'),vm=require('node:vm');
const c={window:{}};vm.runInNewContext(fs.readFileSync('uppgifterai.js','utf8'),c);
const bank=c.window.BANKAI,q=id=>bank.find(u=>u.id===id),eq=(id,w)=>a.equal(JSON.stringify(q(id).rättSvar),JSON.stringify(w),id);
const nm=([r,k])=>String.fromCharCode(65+r)+(k+1),STD=[[-1,0],[0,1],[1,0],[0,-1]];
const find=(m,ch)=>{for(let r=0;r<m.length;r++){const k=m[r].indexOf(ch);if(k>=0)return[r,k];}};
const nb=(m,n)=>STD.map(([x,y])=>[n[0]+x,n[1]+y]).filter(([r,k])=>m[r]?.[k]!==undefined&&m[r][k]!=='#');
const cost=(m,[r,k])=>/\d/.test(m[r][k])?+m[r][k]:1,man=(x,y)=>Math.abs(x[0]-y[0])+Math.abs(x[1]-y[1]);
function bfs(m){const s=find(m,'S'),g=find(m,'G'),qq=[s],seen=new Set([nm(s)]),par={},out=[],snaps=[];while(qq.length){const n=qq.shift();out.push(nm(n));if(nm(n)===nm(g))break;for(const v of nb(m,n))if(!seen.has(nm(v))){seen.add(nm(v));par[nm(v)]=nm(n);qq.push(v);}snaps.push(qq.map(nm));}
 const path=[nm(g)];while(par[path[0]])path.unshift(par[path[0]]);return{out,path,snaps};}
function dist(m,s){const d={[nm(s)]:0},qq=[s];while(qq.length){const n=qq.shift();for(const v of nb(m,n))if(!(nm(v) in d)){d[nm(v)]=d[nm(n)]+1;qq.push(v);}}return d;}
function dfs(m){const s=find(m,'S'),g=find(m,'G'),seen=new Set(),out=[],st=[];const go=n=>{seen.add(nm(n));out.push(nm(n));st.push(nm(n));if(nm(n)===nm(g))return true;for(const v of nb(m,n))if(!seen.has(nm(v))&&go(v))return true;st.pop();return false;};go(s);return{out,path:st};}
function search(m,mode){const s=find(m,'S'),g=find(m,'G'),G={[nm(s)]:0},cell={[nm(s)]:s},op=new Set([nm(s)]),cl=new Set(),seen=new Set([nm(s)]),out=[];const h=k=>man(cell[k],g);
 while(op.size){const n=[...op].sort((x,y)=>mode==='greedy'?h(x)-h(y)||x.localeCompare(y):(G[x]+h(x))-(G[y]+h(y))||h(x)-h(y)||x.localeCompare(y))[0];op.delete(n);cl.add(n);out.push(n);if(n===nm(g))break;
  for(const v of nb(m,cell[n])){const k=nm(v),alt=G[n]+cost(m,v);if(mode==='greedy'){if(!seen.has(k)){seen.add(k);G[k]=alt;cell[k]=v;op.add(k);}}else if(!cl.has(k)&&alt<(G[k]??1e9)){G[k]=alt;cell[k]=v;op.add(k);}}}
 return{out,cost:G[nm(g)],open:[...op],G,h};}
function cheapest(m,s,t){const d={[nm(s)]:0},cell={[nm(s)]:s},done=new Set();while(true){const n=Object.keys(d).filter(k=>!done.has(k)).sort((x,y)=>d[x]-d[y])[0];if(!n)break;done.add(n);for(const v of nb(m,cell[n])){const k=nm(v);if(d[n]+cost(m,v)<(d[k]??1e9)){d[k]=d[n]+cost(m,v);cell[k]=v;}}}return d[nm(t)];}
const mm=(t,max)=>typeof t==='number'?t:(max?Math.max:Math.min)(...t.map(x=>mm(x,!max)));
function ab(t,max){let leaf=0;const named=t=>typeof t==='number'?{n:'L'+(++leaf),v:t}:t.map(named),tree=named(t),cut=[],seen=[],exact=[];const names=t=>t.n?[t.n]:t.flatMap(names);
 function go(t,max,al,be,top){if(t.n){seen.push(t.n);return t.v;}let v=max?-Infinity:Infinity,cutHere=false;for(let i=0;i<t.length;i++){const x=go(t[i],!max,al,be,false);if(max){v=Math.max(v,x);al=Math.max(al,v);}else{v=Math.min(v,x);be=Math.min(be,v);}
  if(al>=be&&i+1<t.length){cut.push(...t.slice(i+1).flatMap(names));cutHere=true;break;}}return top?v:(t.cut=cutHere,v);}
 const v=go(tree,max,-Infinity,Infinity,true);return{v,cut,seen,exactKids:tree.filter(k=>!k.n&&!k.cut).length,tree};}
const NYA=['1.44','1.45','1.46','1.47','1.48','1.49','1.50','1.51','1.52','1.53','1.54','2.54','2.55','2.56','2.57','2.58','2.59','2.60','2.61','2.62','2.63','2.64','2.65','2.66','3.37','3.38','3.39','3.40','3.41','3.42'];

test('format, nivåer och områden',()=>{
 for(const id of NYA){const u=q(id);a.ok(u,id);a.equal(u.spel,true);a.equal(u['självrättning'],true);a.equal(u.svarstyp,'flera_delar');a.equal(u.rättSvar.length,u.spelDelar.length);
  u.spelDelar.forEach((d,i)=>{a.equal(u.rättSvar[i],d.rättSvar);a.match(d.s,/facit-rubrik/);
   if(d.svarstyp==='numeriskt'){a.ok(Number.isInteger(d.rättSvar));a.equal(d.tolerans,0);}else{a.equal(d.alternativ.filter(x=>x.ratt).length,1,id);for(const x of d.alternativ)a.ok(x.kommentar.length>12,id);}});}
 // Områdena räknas som när omgången byggdes; omgrupperingen 2026-11-11 sparar dem i omrTidigare.
 const o0=u=>u.omrTidigare||u.omr,omr={};for(const id of NYA)omr[o0(q(id))]=(omr[o0(q(id))]||0)+1;
 a.equal(JSON.stringify(omr),JSON.stringify({ko_stack:2,ko_sokning:3,bfs:3,dfs:3,astar_sokning:5,astar_varden:3,viktade_vagar:3,prioritetsko:2,minimax:3,alfa_beta:3}));
 const parts=NYA.flatMap(id=>q(id).spelDelar);a.ok(parts.filter(d=>d.niva==='E').length/parts.length>=0.7,'mest E');
 for(const id of ['1.48','1.49','2.54'])a.match(q(id).spelIntro,/En robot startar i den gröna rutan/);
});
test('köer, stackar, BFS och DFS',()=>{
 eq('1.44',['skriv text',2]);eq('1.45',['Bild',3]);eq('2.65',['Dana',1]);
 const k46={S:['A','B','C'],A:['D','E'],C:['F','G']},q46=['S'];for(let i=0;i<2;i++){const n=q46.shift();q46.push(...(k46[n]||[]));}eq('1.46',[q46.length,q46[0]]);
 const k47={S:['A','B'],A:['C','D'],B:['E'],D:['F','G']},s47=['S'],o47=[];while(s47.length){const n=s47.pop();o47.push(n);if(n==='G')break;s47.push(...[...(k47[n]||[])].reverse());}eq('1.47',[o47[3],s47.length]);
 const r48=bfs(['S..','.#.','..G']);eq('1.48',['A3',r48.snaps[2].length]);
 const m49=['.S..#','.#...','...#.','.#..G'],r49=bfs(m49);eq('1.49',[Object.values(dist(m49,find(m49,'S'))).filter(v=>v===1).length,r49.out[2],r49.path.length-1]);
 const m50=['S.#..','.##..','....#','#...G'],r50=bfs(m50);eq('1.50',[r50.out[6],Object.values(dist(m50,find(m50,'S'))).filter(v=>v===2).length,r50.out.length]);
 const r51=bfs(['S...','.##.','.#G.','....']);eq('1.51',[r51.path.length-1,r51.out[r51.out.length-2]]);
 for(const[id,m,k]of [['1.52',['S..#.','.#...','.#.#.','...#G'],4],['1.53',['S.#...','..#.#.','......','.#.#.G'],7]]){const r=dfs(m),b=bfs(m);eq(id,[r.out[k-1],r.out.length,r.path.length-1,r.path.length===b.path.length?'Ja':'Nej']);}
 const k54={S:['A','B'],A:['C','D'],B:['E','F']},o54=[];const go=n=>{o54.push(n);return n==='D'||[...(k54[n]||[])].reverse().some(go);};go('S');eq('1.54',[o54[2],o54.length]);
});
test('A*, girig bäst först och g/h/f',()=>{
 const r54=search(['S..#','.#..','..#.','...G'],'astar');eq('2.54',[r54.out[2],r54.out.length,r54.cost]);
 const m55=['....','S.#G','....'],s55=find(m55,'S'),g55=find(m55,'G'),f55=nb(m55,s55).map(v=>[nm(v),1+man(v,g55)]).sort((x,y)=>x[1]-y[1]);a.ok(f55[0][1]<f55[1][1]);eq('2.55',[f55[0][0],1+man([0,0],g55)]);
 const g56=search(['S...','#.#.','...G'],'greedy');eq('2.56',[g56.out[1]+' och '+g56.out[2],man([0,2],[2,3])]);
 const m57=['S...','..#.','...G'];const st=search(m57,'astar');a.deepEqual(st.out.slice(0,2),['A1','A2']);
 a.equal(1+man([1,0],[2,3]),5);a.equal(2+man([0,2],[2,3]),5);a.equal(2+man([1,1],[2,3]),5);eq('2.57',['B1, A3 och B2',3]);
 eq('2.58',[3+man([3,1],[3,4])<6+man([0,4],[3,4])?'Q':'P',6+man([0,4],[3,4])]);
 eq('2.59',[man([1,2],[3,4]),3+man([1,2],[3,4])]);
 const hs={P:man([0,4],[3,5]),Q:man([3,1],[3,5]),R:man([2,4],[3,5])};eq('2.60',[Object.keys(hs).sort((x,y)=>hs[x]-hs[y])[0],hs.Q]);
 const m61=['S.#..','..#..','..#..','....G'],g61=dist(m61,[0,0])['A4'];eq('2.61',[g61,g61+man([0,3],[3,4])]);
});
test('viktade vägar, prioritetsköer, minimax och alfa–beta',()=>{
 eq('2.62',['S → B → C → M',Math.min(2+9,2+5+2,4+1+2)]);
 const m63=['S44.','....','.3..','...G'],path=c=>c.reduce((s,x)=>s+cost(m63,x),0);eq('2.63',['Väg 2',path([[0,1],[0,2],[0,3],[1,3],[2,3],[3,3]])]);
 const m64=['.....','.#.#.','S433G'];eq('2.64',[4+3+3+1,cheapest(m64,[2,0],[2,4]),8]);
 const T={A:[2,8],B:[5,2],C:[3,6],D:[6,4],E:[1,9]},o=Object.keys(T).sort((x,y)=>T[x][0]+T[x][1]-T[y][0]-T[y][1]);eq('2.66',[o[1],T[o[0]][0]+T[o[0]][1]]);
 eq('3.37',[Math.min(5,7),mm([[4,8],[6,2,9],[5,7]],true),'Draget till C']);
 eq('3.38',[Math.min(8,2),mm([[[3,7],[6,1]],[[8,2],[4,5]]],false),'Draget till A']);
 eq('3.39',['L4',mm([[2,9],[5,4]],true)]);
 const r40=ab([[4,7],[2,8],[5,3],[6,9]],true);eq('3.40',[r40.v,r40.cut.length,r40.exactKids]);
 const r41=ab([[3,6],[7,1],[2,5]],false);eq('3.41',[r41.v,r41.cut.length,r41.seen[r41.seen.length-1]]);
 const t42=[[[2,5],[6,1]],[[7,3],[4,8]],[[1,9],[6,2]]],r42=ab(t42,true);eq('3.42',[r42.v,r42.cut.length,Math.max(mm(t42[0],false),mm(t42[1],false))]);
 for(const[t,m]of [[[[4,7],[2,8],[5,3],[6,9]],true],[[[3,6],[7,1],[2,5]],false],[t42,true]])a.equal(ab(t,m).v,mm(t,m));
});
test('validatorn hittar inget i omgången',()=>{const r=require('./granska-uppgifter.js').granskaProjekt(process.cwd()).resultat.find(x=>x.fil==='uppgifterai.js');
 a.deepEqual(r.fynd.filter(f=>NYA.includes(f.id)||(f.relateradeId||[]).some(i=>NYA.includes(i))),[]);});
