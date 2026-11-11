'use strict';
// AI-banken 2026-11-11, femte omgången: enklare tabeller, tydligare ordval och 24 nya uppgifter
// (12 alfa–beta-träd i tre svårighetsgrader, 4 minimaxträd och 8 övriga). Svaren kontrolleras
// med egna simuleringar, oberoende av Python-koden i byggskripten.
const {test}=require('node:test'),a=require('node:assert/strict'),fs=require('node:fs'),vm=require('node:vm');
const c={window:{}};vm.runInNewContext(fs.readFileSync('uppgifterai.js','utf8'),c);
const bank=c.window.BANKAI,q=id=>bank.find(u=>u.id===id),has=(id,s)=>a.ok(q(id).s.includes(s),id+': '+s);
const AB={'3.15':[[[3,7],[2,9]],true,3,'L4'],'3.16':[[[6,8],[7,9],[4,5]],true,7,'L6'],'3.17':[[[4,6],[7,2,9]],false,6,'L4,L5'],
 '3.18':[[[2,5,3],[4,1],[6,8]],false,4,'L7'],'3.19':[[[6,9,8],[3,10,7],[7,2,12]],true,6,'L5,L6,L9'],'3.20':[[[5,2,3],[9,4,6],[6,7,1]],false,5,'L5,L6,L8,L9'],
 '3.21':[[[[5,7],[9,6]],[[3,2],[4,8]]],true,7,'L4,L7,L8'],'3.22':[[[[4,-1],[-2,-3]],[[5,1],[-3,2]]],false,-1,'L4,L7,L8'],
 '3.23':[[[[0,1],[3,3]],[[0,0],[9,9]],[[6,5],[8,2]]],true,6,'L4,L7,L8,L12'],'3.24':[[[[12,10],[5,6],[14,7]],[[11,11],[13,12],[6,4]]],false,10,'L4,L9,L10,L11,L12'],
 '3.25':[[[[5,9,-5],[4,-1]],[[1,-6],[1,-1,5]],[[-1,-5],[8,-1]]],true,4,'L8,L9,L10,L13,L14'],'3.26':[[[[12,3],[-1,5]],[[8,10],[10,5,-5]],[[-4,2,-2],[3,5]]],false,3,'L4,L7,L8,L9']};
const MM={'3.27':[[[4,9],[6,3],[8,7]],false,6],'3.28':[[[[3,-2],[5,1]],[[-4,6],[2,0]]],true,3],'3.29':[[[[2,7],[5,3]],[[6,1],[4,9]],[[8,3],[5,6]]],false,3],'3.30':[[[4,[2,7,1]],[[5,3],6,[-1,8]]],true,5]};
const NYA=[...Object.keys(AB),...Object.keys(MM),'1.28','1.29','1.30','1.31','2.31','2.32','2.33','2.34'];
const mm=(t,max)=>typeof t==='number'?t:(max?Math.max:Math.min)(...t.map(x=>mm(x,!max)));
function ab(t,max){let leaf=0;const cut=[],seen=[];const all=t=>typeof t==='number'?[++leaf]:t.flatMap(all);
 const named=t=>typeof t==='number'?{n:'L'+(++leaf),v:t}:t.map(named);leaf=0;const tree=named(t);
 const names=t=>t.n?[t.n]:t.flatMap(names);
 function go(t,max,al,be){if(t.n){seen.push(t.n);return t.v;}let v=max?-Infinity:Infinity;for(let i=0;i<t.length;i++){const x=go(t[i],!max,al,be);if(max){v=Math.max(v,x);al=Math.max(al,v);}else{v=Math.min(v,x);be=Math.min(be,v);}if(al>=be){cut.push(...t.slice(i+1).flatMap(names));break;}}return v;}
 return{v:go(tree,max,-Infinity,Infinity),cut,seen};}
const nm=([r,k])=>String.fromCharCode(65+r)+(k+1),STD=[[-1,0],[0,1],[1,0],[0,-1]];
const find=(m,ch)=>{for(let r=0;r<m.length;r++){const k=m[r].indexOf(ch);if(k>=0)return[r,k];}};
const nb=(m,n)=>STD.map(([x,y])=>[n[0]+x,n[1]+y]).filter(([r,k])=>m[r]?.[k]!==undefined&&m[r][k]!=='#');
const cost=(m,[r,k])=>/\d/.test(m[r][k])?+m[r][k]:1,man=(x,y)=>Math.abs(x[0]-y[0])+Math.abs(x[1]-y[1]);
function bfs(m){const s=find(m,'S'),g=find(m,'G'),qq=[s],seen=new Set([nm(s)]),par={},out=[],queued=new Set([nm(s)]);while(qq.length){const n=qq.shift();out.push(nm(n));if(nm(n)===nm(g))break;for(const v of nb(m,n))if(!seen.has(nm(v))){seen.add(nm(v));queued.add(nm(v));par[nm(v)]=nm(n);qq.push(v);}}
 const path=[nm(g)];while(par[path[0]])path.unshift(par[path[0]]);return{out,path,queued};}
function dfs(m){const s=find(m,'S'),g=find(m,'G'),seen=new Set(),out=[],st=[];const go=n=>{seen.add(nm(n));out.push(nm(n));st.push(nm(n));if(nm(n)===nm(g))return true;for(const v of nb(m,n))if(!seen.has(nm(v))&&go(v))return true;st.pop();return false;};go(s);return{out,path:st};}
function astar(m){const s=find(m,'S'),g=find(m,'G'),G={[nm(s)]:0},cell={[nm(s)]:s},par={},op=new Set([nm(s)]),cl=new Set(),out=[];const h=k=>man(cell[k],g);
 while(op.size){const n=[...op].sort((x,y)=>(G[x]+h(x))-(G[y]+h(y))||h(x)-h(y)||x.localeCompare(y))[0];op.delete(n);cl.add(n);out.push(n+' '+G[n]+' '+h(n)+' '+(G[n]+h(n)));if(n===nm(g))break;
  for(const v of nb(m,cell[n])){const k=nm(v),alt=G[n]+cost(m,v);if(!cl.has(k)&&alt<(G[k]??1e9)){G[k]=alt;cell[k]=v;par[k]=n;op.add(k);}}}
 const path=[nm(g)];while(par[path[0]])path.unshift(par[path[0]]);return{out,path,cost:G[nm(g)]};}
function cheapest(m,s,t){const d={[nm(s)]:0},cell={[nm(s)]:s},done=new Set();while(true){const n=Object.keys(d).filter(k=>!done.has(k)).sort((x,y)=>d[x]-d[y])[0];if(!n)break;done.add(n);for(const v of nb(m,cell[n])){const k=nm(v);if(d[n]+cost(m,v)<(d[k]??1e9)){d[k]=d[n]+cost(m,v);cell[k]=v;}}}return d[nm(t)];}

test('tabeller att fylla i har tomma celler och startraden "Från början"',()=>{
 for(const u of bank)for(const h of [u.t,u.s,u.spelIntro,...u.spelDelar.flatMap(d=>[d.fraga,d.s])]){
  a.doesNotMatch(h,/>…<\/td>/,u.id);
  for(const t of h.match(/<table class="data">[\s\S]*?<\/table>/g)||[])if(/<thead><tr><th style="text-align:left">Tas ut<\/th>/.test(t))a.doesNotMatch(t,/<tr><td style="text-align:left">–<\/td>/,u.id);}
 for(const id of ['1.04','1.05','1.13','1.14','1.22','1.23','1.29'])a.match(q(id).t,/Från början/,id);
 a.match(q('1.04').t,/<td style="text-align:left;min-width:7em;height:2.6em"><\/td>/);
});
test('BFS- och A*-uppgifter säger "tas ut" i stället för "besöks"',()=>{
 for(const id of ['1.01','1.06','1.08','2.02','2.09','2.17','2.19','2.28'])for(const d of q(id).spelDelar)a.doesNotMatch(d.fraga,/besöks|besöksordning|Girig/,id+d.etikett);
 a.match(q('1.01').t,/a\) Ange i vilken ordning rutorna tas ut ur kön\./);
});
test('24 nya uppgifter med fullständiga delar och unika texter',()=>{
 a.equal(new Set(bank.map(u=>u.id)).size,bank.length);a.ok(bank.length>=95);
 for(const id of NYA){const u=q(id);a.ok(u,id);a.equal(u.spel,false);a.equal(u['självrättning'],false);a.equal(u['miniräknare'],true);a.equal(u.geogebra,false);a.match(u.s,/facit-steglista/);
  a.doesNotMatch(JSON.stringify(u),/UCS|Dijkstra/);
  for(const d of u.spelDelar){a.ok(d.fraga&&d.ledtrad&&d.s);a.match(d.s,/facit-rubrik/);a.match(d.s,/facit-svar/);
   for(const x of d.alternativ||[]){a.ok(x.kommentar.length>15,id);a.ok(u.t.includes('</strong> '+x.txt+'</p>'),id);}}}
 const fam={};for(const id of Object.keys(AB))fam[q(id).familj]=(fam[q(id).familj]||0)+1;
 a.deepEqual(Object.values(fam),[4,4,4]);
 for(const id of Object.keys(AB)){const u=q(id),lv=Math.max(...u.spelDelar.map(d=>d.traningsniva));if(u.familj.endsWith('svår'))a.equal(lv,5,id);else a.ok(lv===4||lv===5,id);/* beskärning är A-nivå, se AI_NIVAINDELNING.md */}
});
test('alfa–beta: rotvärde och beskurna löv i alla tolv träd',()=>{
 for(const[id,[t,max,root,cut]]of Object.entries(AB)){const r=ab(t,max);a.equal(r.v,root,id);a.equal(r.v,mm(t,max),id);a.equal(r.cut.join(','),cut,id);
  a.ok(r.cut.length>0,id);const u=q(id);has(id,'<strong>Svar:</strong> '+String(root).replace('-','−')+'.');
  for(const l of cut.split(','))a.ok(u.spelDelar[1].s.includes(l),id+' '+l);
  a.match(u.spelDelar[1].s,new RegExp('totalt '+cut.split(',').length+' av '));}
 const r16=ab(AB['3.16'][0],true);has('3.16',r16.seen.length+' av 6 löv.');
 has('3.20','4 löv.');has('3.17','β = 6.');has('3.25','α = 4.');has('3.18','<strong>Svar:</strong> 4.');has('3.26','<strong>Svar:</strong> 3.');
 has('3.22','α = −1, β = −2.');has('3.15','Draget till A.');has('3.19','I B.');has('3.23','Exakt: A, C. Bara gräns: B.');
});
test('figurernas lövvärden stämmer med de träd som svaren räknas på',()=>{
 for(const[id,[t]]of [...Object.entries(AB),...Object.entries(MM)]){const svg=q(id).spelIntro;
  const shown=[...svg.matchAll(/font-size="18" fill="#111827">([^<]+)<\/text>/g)].map(m=>m[1].replace('−','-'));
  a.equal(shown.join(','),t.flat(Infinity).join(','),id);a.match(svg,/<polygon/);}
});
test('minimax: rotvärden och vägar',()=>{
 for(const[id,[t,max,root]]of Object.entries(MM)){a.equal(mm(t,max),root,id);}
 has('3.27','Värdet 6, draget till B.');has('3.28','R → A → C → lövet 3 (L1).');has('3.29','Värdet 3, draget till A.');has('3.30','R → B → D → lövet 5 (L5).');
});
test('övriga nya uppgifter',()=>{
 const st=[],out=[];for(const x of ['A','B',0,'C','D','E',0,0,'F']){if(x)st.push(x);else out.push(st.pop());}a.equal(out.join(),'B,E,D');a.equal(st.join(' '),'A C F');
 const kids={S:['A','B','C'],A:['D'],B:['E','F'],C:['G']},s2=['S'],o2=[];while(s2.length){const n=s2.pop();o2.push(n);if(n==='G')break;s2.push(...[...(kids[n]||[])].reverse());}a.equal(o2.join(''),'SADBEFCG');
 const m30=['S..#.','.#...','...#.','#.#.G'],r30=bfs(m30);a.equal(r30.out.length,14);a.equal(r30.path.length-1,7);a.ok(!r30.queued.has('D4'));
 a.equal(q('1.30').spelDelar[2].alternativ.find(x=>x.ratt).txt,'D4');
 const m31=['S.#..','...#.','.#...','.#.#G'];a.equal(dfs(m31).out.join(' '),'A1 A2 B2 B3 C3 C4 C5 B5 A5 A4 D5');a.equal(dfs(m31).path.length-1,7);a.equal(bfs(m31).path.length-1,7);
 const pq=[],o4=[];for(const x of [['A',4],['B',2],['C',6],0,['D',1],['E',3],0,0]){if(x)pq.push(x);else{pq.sort((p,r)=>p[1]-r[1]);o4.push(pq.shift()[0]);}}a.equal(o4.join(),'B,D,E');
 const m32=['S....','.#.#.','...#.','#.#.G'],g32=find(m32,'G'),fv=c=>cheapest(m32,[0,0],c)+man(c,g32);a.deepEqual([[0,3],[2,1],[3,3]].map(fv).join(),'7,7,9');
 const r33=astar(['.S..','.#.#','...G']);a.equal(r33.out.join(' | '),'A2 0 4 4 | A3 1 3 4 | A4 2 2 4 | B3 2 2 4 | C3 3 1 4 | C4 4 0 4');a.equal(r33.path.join(' '),'A2 A3 B3 C3 C4');
 const m34=['.....','.###.','S43.G'];a.equal(cheapest(m34,[2,0],[2,4]),8);a.equal(astar(m34).cost,8);a.equal(astar(m34).path.length-1,8);
});
test('validatorn hittar inget i den nya omgången',()=>{const r=require('./granska-uppgifter.js').granskaProjekt(process.cwd()).resultat.find(x=>x.fil==='uppgifterai.js');
 a.deepEqual(r.fynd.filter(f=>NYA.includes(f.id)||(f.relateradeId||[]).some(i=>NYA.includes(i))),[]);});
