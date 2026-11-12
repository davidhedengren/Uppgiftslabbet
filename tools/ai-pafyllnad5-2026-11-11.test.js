'use strict';
// AI-banken 2026-11-11, åttonde omgången: 16 teoriuppgifter (flerval) och 12 beräkningar
// inom minimax, oinformerad och informerad sökning. Beräkningarna räknas om oberoende.
const {test}=require('node:test'),a=require('node:assert/strict'),fs=require('node:fs'),vm=require('node:vm');
const c={window:{}};vm.runInNewContext(fs.readFileSync('uppgifterai.js','utf8'),c);
// Efterbearbetningen 2026-11-12 skriver ensamma namn som ”Noden B”/”Rutan P” (och 1.22a ”Efter uttaget av A”).
// Testerna nedan räknar fram bokstäverna, så prefixet tas bort här. Själva prefixen kontrolleras i
// tools/ai-efterbearbetning-2026-11-12.test.js.
c.window.BANKAI=JSON.parse(JSON.stringify(c.window.BANKAI).replace(/(?:Noden|Rutan|Efter uttaget av) ([A-Z])(?=["<.:])/g,'$1'));
const bank=c.window.BANKAI,q=id=>bank.find(u=>u.id===id),eq=(id,w)=>a.equal(JSON.stringify(q(id).rättSvar),JSON.stringify(w),id);
const nm=([r,k])=>String.fromCharCode(65+r)+(k+1),STD=[[-1,0],[0,1],[1,0],[0,-1]];
const find=(m,ch)=>{for(let r=0;r<m.length;r++){const k=m[r].indexOf(ch);if(k>=0)return[r,k];}};
const nb=(m,n)=>STD.map(([x,y])=>[n[0]+x,n[1]+y]).filter(([r,k])=>m[r]?.[k]!==undefined&&m[r][k]!=='#');
const man=(x,y)=>Math.abs(x[0]-y[0])+Math.abs(x[1]-y[1]);
function bfs(m){const s=find(m,'S'),g=find(m,'G'),qq=[s],seen=new Set([nm(s)]),par={},out=[];while(qq.length){const n=qq.shift();out.push(nm(n));if(nm(n)===nm(g))break;for(const v of nb(m,n))if(!seen.has(nm(v))){seen.add(nm(v));par[nm(v)]=nm(n);qq.push(v);}}
 const path=[nm(g)];while(par[path[0]])path.unshift(par[path[0]]);return{out,path};}
function dist(m,s){const d={[nm(s)]:0},qq=[s];while(qq.length){const n=qq.shift();for(const v of nb(m,n))if(!(nm(v) in d)){d[nm(v)]=d[nm(n)]+1;qq.push(v);}}return d;}
function dfs(m){const s=find(m,'S'),g=find(m,'G'),seen=new Set(),out=[],st=[];const go=n=>{seen.add(nm(n));out.push(nm(n));st.push(nm(n));if(nm(n)===nm(g))return true;for(const v of nb(m,n))if(!seen.has(nm(v))&&go(v))return true;st.pop();return false;};go(s);return{out,path:st};}
function search(m,mode){const s=find(m,'S'),g=find(m,'G'),G={[nm(s)]:0},cell={[nm(s)]:s},op=new Set([nm(s)]),cl=new Set(),seen=new Set([nm(s)]),out=[];const h=k=>man(cell[k],g);
 while(op.size){const n=[...op].sort((x,y)=>mode==='greedy'?h(x)-h(y)||x.localeCompare(y):(G[x]+h(x))-(G[y]+h(y))||h(x)-h(y)||x.localeCompare(y))[0];op.delete(n);cl.add(n);out.push(n);if(n===nm(g))break;
  for(const v of nb(m,cell[n])){const k=nm(v),alt=G[n]+1;if(mode==='greedy'){if(!seen.has(k)){seen.add(k);cell[k]=v;op.add(k);}}else if(!cl.has(k)&&alt<(G[k]??1e9)){G[k]=alt;cell[k]=v;op.add(k);}}}
 return{out,cost:G[nm(g)]};}
const mm=(t,max)=>typeof t==='number'?t:(max?Math.max:Math.min)(...t.map(x=>mm(x,!max)));
const TEORI=['1.55','1.56','1.57','1.58','1.59','1.60','2.67','2.68','2.69','2.70','2.71','2.72','2.73','3.43','3.44','3.45','3.46'];
const NYA=[...TEORI,'1.61','1.62','1.63','1.64','2.74','2.75','2.76','2.77','3.47','3.48','3.49'];

test('format och områden: bara minimax, oinformerad och informerad sökning',()=>{
 a.equal(NYA.length,28);
 for(const id of NYA){const u=q(id);a.ok(u,id);a.equal(u.spel,true);a.equal(u['självrättning'],true);a.equal(u.svarstyp,'flera_delar');a.notEqual(u.omr,'alfa_beta');
  u.spelDelar.forEach((d,i)=>{a.equal(u.rättSvar[i],d.rättSvar);a.match(d.s,/facit-rubrik/);
   if(d.svarstyp==='alternativ'){a.equal(d.alternativ.filter(x=>x.ratt).length,1,id);a.equal(new Set(d.alternativ.map(x=>x.txt)).size,d.alternativ.length);for(const x of d.alternativ)a.ok(x.kommentar.length>15,id+' '+x.txt);}
   else{a.ok(Number.isInteger(d.rättSvar));a.equal(d.tolerans,0);}});}
 const theoryParts=TEORI.flatMap(id=>q(id).spelDelar);a.ok(theoryParts.filter(d=>d.svarstyp==='alternativ').length>=30,'många flervalsfrågor');
});
test('teorifrågornas rätta svar',()=>{
 const want={'1.55':['En FIFO-kö','Den har minst antal steg','Efter avstånd från start'],
  '1.56':['En stack','Nej, DFS kan hitta en lång väg först','Backar till den senaste rutan som har en obesökt granne'],
  '1.58':['Den använder ingen uppskattning av hur långt det är kvar till målet','BFS och DFS'],'1.59':['Sökningen beter sig som DFS','Den som lades in senast'],
  '2.69':['Bara h','f = g + h','Girig bäst först'],'2.70':['Den använder en uppskattning av avståndet kvar till målet','A*'],
  '2.71':['h får aldrig vara större än den verkliga kostnaden kvar','Nej, minst h steg behövs alltid för att nå målet'],
  '3.43':['Välja det drag som ger störst värde','Att MIN alltid väljer det drag som är sämst för MAX','Hur bra slutläget är för MAX'],
  '3.44':['Ett läge i spelet','Ett drag','Antalet lägen växer så snabbt att trädet blir för stort'],'3.45':['Minst 5','Spelarna turas om att göra drag']};
 for(const[id,w]of Object.entries(want))eq(id,w);
 eq('2.68',['Antalet rader plus antalet kolumner mellan rutan och målet',3,'h räknar inte med väggarna, och väggarna tvingar fram en omväg']);
 const m=['S....','.###.','.#G#.','.....'],G=find(m,'G');a.equal(man([1,0],G),3);a.equal(dist(m,G)['B1'],5);
 eq('3.46',[mm([[9,1],[4,6]],true),'MIN skulle svara med draget som ger 1']);
});
test('nivåer: E för begrepp, C för förklaringar, A för att värdera heuristiken',()=>{
 const lv=k=>{const u=q(k.slice(0,-1)),d=u.spelDelar.find(x=>x.etikett===k.slice(-1));return d.niva;};
 for(const k of ['1.55a','1.56b','1.58a','2.67a','2.69a','2.70b','3.43a','3.44b'])a.equal(lv(k),'E',k);
 for(const k of ['1.57a','1.60b','2.68c','2.69c','3.45a','3.46b'])a.equal(lv(k),'C',k);
 for(const k of ['2.71a','2.71b'])a.equal(lv(k),'A',k);
});
test('beräkningsuppgifternas svar',()=>{
 const m61=['S...#.','.##...','...#..','.#...G'],r61=bfs(m61);eq('1.61',[Object.values(dist(m61,[0,0])).filter(v=>v===3).length,r61.out[7],r61.path.length-1]);
 for(const[id,m,k]of [['1.62',['.S.#','.#..','...#','#..G'],3],['1.63',['S..#..','.#....','.#.##.','...#.G'],8]]){const r=dfs(m),b=bfs(m);eq(id,[r.out[k-1],r.out.length,r.path.length-1,r.path.length===b.path.length?'Ja':'Nej']);}
 const kids={S:['A','B'],A:['C','D'],B:['E'],C:['F'],E:['G']},qq=['S'],o=[],par={};while(qq.length){const n=qq.shift();o.push(n);if(n==='G')break;for(const k of kids[n]||[]){par[k]=n;qq.push(k);}}eq('1.64',[o.length,par.G]);
 const r74=search(['S....','.##..','...#.','.#..G'],'astar');eq('2.74',[r74.out[5],r74.out.length,r74.cost]);
 const m75=['.....','.S.#G','.....'],s75=find(m75,'S'),g75=find(m75,'G'),n75=nb(m75,s75);eq('2.75',[n75.length,search(m75,'greedy').out[1],man([1,2],g75)]);
 const g76={P:5,Q:6,R:4},c76={P:[0,5],Q:[2,3],R:[3,2]},G76=[3,5],f76=k=>g76[k]+man(c76[k],G76);eq('2.76',[Object.keys(g76).sort((x,y)=>f76(x)-f76(y))[0],f76('Q')]);
 eq('2.77',[10,2+3+2,10-(2+3+2)]);
 eq('3.47',[Math.max(1,7),mm([[[3,-2],[4,1]],[[-5,6],[2,0]],[[1,7],[-3,8]]],true),'Draget till C']);
 eq('3.48',[Math.min(7,0),mm([[[5,2],[1,4]],[[3,6],[7,0]]],false),'Draget till A']);
 eq('3.49',['L4',mm([[[4,8],[2,6]],[[7,1],[5,3]]],true)]);
});
test('validatorn hittar inget i omgången',()=>{const r=require('./granska-uppgifter.js').granskaProjekt(process.cwd()).resultat.find(x=>x.fil==='uppgifterai.js');
 a.deepEqual(r.fynd.filter(f=>NYA.includes(f.id)||(f.relateradeId||[]).some(i=>NYA.includes(i))),[]);});
