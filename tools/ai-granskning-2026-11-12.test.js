'use strict';
// AI-banken, granskningen 2026-11-12: (1) delkortens facit nämner alternativen med text, inte
// bokstav, (2) C- och A-uppgifter för prov samt E i alfa–beta, (3) träningsnivå 1 i DFS och A*,
// (4) inga ensamma bokstäver som alternativ. Svaren räknas om oberoende av byggskripten.
const {test}=require('node:test'),a=require('node:assert/strict'),fs=require('node:fs'),vm=require('node:vm');
const c={window:{}};vm.runInNewContext(fs.readFileSync('uppgifterai.js','utf8'),c);
const bank=c.window.BANKAI,q=id=>bank.find(u=>u.id===id),del=k=>q(k.slice(0,-1)).spelDelar.find(d=>d.etikett===k.slice(-1));
const rätt=k=>{const d=del(k);return d.svarstyp==='alternativ'?d.alternativ.filter(x=>x.ratt).map(x=>x.txt).join('|'):JSON.stringify(d.rättSvar);};
const ren=h=>String(h).replace(/<[^>]+>/g,' ').replace(/\s+/g,' ').trim();

test('1. delkortens facit nämner alternativen med text, huvudfacit behåller bokstäverna',()=>{
 let listor=0;
 for(const u of bank)for(const d of u.spelDelar){const al=d.alternativ||[];if(!al.length)continue;
  a.doesNotMatch(d.s,/<li><strong>[A-Z]:<\/strong>/,u.id+d.etikett);
  const m=d.s.match(/<ul>((?:<li>.*?<\/li>)+)<\/ul><\/div>$/);if(!m)continue;listor++;
  const rader=[...m[1].matchAll(/<li><strong>(.*?):<\/strong> (.*?)<\/li>/g)];a.equal(rader.length,al.length,u.id+d.etikett);
  rader.forEach((r,i)=>{a.equal(r[1],al[i].txt.replace(/\.$/,''),u.id+d.etikett);a.equal(r[2],al[i].kommentar,u.id+d.etikett);});}
 a.ok(listor>=250,'minst 250 delkort har en kommentarlista');
 // Pappersfacit (t och s) använder bokstäverna A–D, i samma ordning som i uppgiftstexten.
 const u=q('2.85');a.match(u.t,/<strong>A\.<\/strong> Noden B/);a.match(u.s,/<li><strong>A:<\/strong> B har lägst h/);
});

test('4. inga ensamma bokstäver som alternativ, och texten på papper stämmer med alternativen',()=>{
 for(const u of bank)for(const d of u.spelDelar)for(const x of d.alternativ||[])a.doesNotMatch(x.txt,/^[A-Z]$/,u.id+d.etikett);
 for(const u of bank){const papper=[...u.t.matchAll(/<p class="ul-alt"><strong>[A-Z]\.<\/strong> (.*?)<\/p>/g)].map(m=>m[1]);
  const alla=new Set(u.spelDelar.flatMap(d=>(d.alternativ||[]).map(x=>x.txt)));for(const t of papper)a.ok(alla.has(t),u.id+': '+t);}
 a.equal(rätt('2.09a'),'Rutan Q');a.equal(rätt('2.14b'),'Noden T');a.equal(rätt('1.22a'),'Efter uttaget av A');
 a.match(del('2.09a').s,/<strong>Svar:<\/strong> Rutan Q\.<\/p>/);a.match(q('2.09').s,/<strong>Svar:<\/strong> Rutan Q\.<\/p>/);
});

test('2. C på köer och stackar räknas om',()=>{
 const perm=[];const gå=(i,st,ut)=>{if(ut.length===4){perm.push(ut.join(''));return;}if(i<4)gå(i+1,[...st,'ABCD'[i]],ut);if(st.length)gå(i,st.slice(0,-1),[...ut,st.at(-1)]);};gå(0,[],[]);
 a.equal(new Set(perm).size,14);a.ok(rätt('1.97a').startsWith('Ja')===perm.includes('BADC'));a.ok(rätt('1.97b').startsWith('Nej')&&!perm.includes('CABD'));a.match(rätt('1.97c'),/^Nej/);
 const kids={S:['A','B'],A:['C','D'],B:['E','F']};
 const kör=(kö,höger)=>{const s=['S'],ut=[];while(s.length){const n=kö?s.shift():s.pop();ut.push(n);if(n==='F')break;const b=kids[n]||[];s.push(...(kö||höger?b:[...b].reverse()));}return ut.join(', ');};
 a.match(ren(del('1.98a').fraga),new RegExp(kör(true,false)));a.equal(rätt('1.98a'),'En FIFO-kö');
 a.match(ren(del('1.98b').fraga),new RegExp(kör(false,false)));a.equal(rätt('1.98b'),'En stack');
 a.match(ren(del('1.98c').fraga),new RegExp(kör(false,true)+'\\.'));a.equal(rätt('1.98c'),'En stack där det högra barnet hamnar överst');
});

test('2. C på prioritetsköer: A*:s öppna lista med uppdaterat f',()=>{
 const E=[['S','A',1],['S','B',4],['A','B',1],['A','M',7],['B','C',1],['C','M',1]],h={S:4,A:3,B:2,C:1,M:0},g={S:0},öppen=new Set(['S']),stängd=new Set(),ut=[],fM=[];
 const adj={};for(const[x,y,w]of E){(adj[x]??=[]).push([y,w]);(adj[y]??=[]).push([x,w]);}
 while(öppen.size){const n=[...öppen].sort((x,y)=>g[x]+h[x]-g[y]-h[y]||h[x]-h[y]||x.localeCompare(y))[0];öppen.delete(n);stängd.add(n);ut.push(n);if(n==='M')break;
  for(const[v,w]of adj[n])if(!stängd.has(v)&&g[n]+w<(g[v]??1e9)){g[v]=g[n]+w;öppen.add(v);if(v==='M')fM.push(g[v]+h.M);}}
 a.equal(rätt('2.104a'),JSON.stringify(ut.join(', ')));a.equal(rätt('2.104b'),JSON.stringify(fM));a.ok(fM[0]>fM[1]);
 a.match(rätt('2.105a'),/f-värdena används inte/);a.match(rätt('2.105b'),/billigare väg/);
 // Fågelvägen och h överskattar inte (h ≤ verklig kostnad kvar).
 const kortast=n=>{const d={[n]:0},kv=new Set([n]);while(kv.size){const x=[...kv].sort((p,r)=>d[p]-d[r])[0];kv.delete(x);for(const[v,w]of adj[x])if(d[x]+w<(d[v]??1e9)){d[v]=d[x]+w;kv.add(v);}}return d.M;};
 for(const n in h)a.ok(h[n]<=kortast(n),n);
});

test('2. A i sökningsdelen räknas om',()=>{
 // 1.99: DFS med två grannordningar och BFS
 const M=['S.#..','...#.','.#...','...#G'],R=M.length,C=M[0].length,cell=ch=>{for(let r=0;r<R;r++){const k=M[r].indexOf(ch);if(k>=0)return[r,k];}};
 const öppen=([r,k],m=M)=>r>=0&&k>=0&&r<m.length&&k<m[0].length&&m[r][k]!=='#',nm=([r,k])=>String.fromCharCode(65+r)+(k+1);
 const dfsLängd=ord=>{const S=cell('S'),G=cell('G'),sett=new Set(),st=[];const gå=n=>{sett.add(nm(n));st.push(n);if(nm(n)===nm(G))return true;for(const[x,y]of ord){const v=[n[0]+x,n[1]+y];if(öppen(v)&&!sett.has(nm(v))&&gå(v))return true;}st.pop();return false;};gå(S);return st.length-1;};
 const U=[-1,0],Rr=[0,1],D=[1,0],L=[0,-1];a.equal(rätt('1.99a'),'7');a.equal(dfsLängd([U,Rr,D,L]),7);a.equal(dfsLängd([D,Rr,U,L]),9);a.equal(rätt('1.99b'),'9');
 a.match(rätt('1.99c'),/beror på grannordningen/);
 // 2.106: tre heuristiker
 const M6=['S.....','.##.#.','...#..','.#...G'],G6=[3,5],dist={};{const kö=[G6];dist[G6.join()]=0;while(kö.length){const n=kö.shift();for(const[x,y]of[U,Rr,D,L]){const v=[n[0]+x,n[1]+y];if(öppen(v,M6)&&!(v.join() in dist)){dist[v.join()]=dist[n.join()]+1;kö.push(v);}}}}
 const man=p=>Math.abs(p[0]-G6[0])+Math.abs(p[1]-G6[1]);
 for(const[k,dv]of Object.entries(dist)){const p=k.split(',').map(Number);a.ok(Math.abs(p[1]-G6[1])<=man(p)&&man(p)<=dv,k);}
 a.equal(rätt('2.106a'),String(2*man([3,3])));a.equal(rätt('2.106b'),String(dist['3,3']));a.ok(2*man([3,3])>dist['3,3']);
 a.equal(rätt('2.106c'),'h₂');a.match(rätt('2.106d'),/^h₁/);
 // 2.107: 2k < 6
 a.equal([1,2,3,4,5,6].filter(k=>2*k<6).join(),'1,2');a.equal(rätt('2.107a'),'8');a.equal(rätt('2.107b'),'6');a.equal(rätt('2.107c'),'k ≤ 2');
 // 2.108: girig bäst först och A* i S333G / .....
 const M8=['S333G','.....'],G8=[0,4],k8=([r,k])=>/\d/.test(M8[r][k])?+M8[r][k]:1,h8=p=>Math.abs(p[0]-G8[0])+Math.abs(p[1]-G8[1]);
 const grannar=n=>[U,Rr,D,L].map(([x,y])=>[n[0]+x,n[1]+y]).filter(v=>öppen(v,M8));
 let n=[0,0],gk=0;const sett=new Set([n.join()]);while(n.join()!==G8.join()){const v=grannar(n).filter(v=>!sett.has(v.join())).sort((x,y)=>h8(x)-h8(y))[0];sett.add(v.join());gk+=k8(v);n=v;}
 const best={'0,0':0},kv=new Set(['0,0']);while(kv.size){const x=[...kv].sort((p,r)=>best[p]-best[r])[0];kv.delete(x);for(const v of grannar(x.split(',').map(Number))){const alt=best[x]+k8(v);if(alt<(best[v.join()]??1e9)){best[v.join()]=alt;kv.add(v.join());}}}
 a.equal(rätt('2.108a'),String(gk));a.equal(rätt('2.108b'),String(best['0,4']));a.match(rätt('2.108c'),/kan hitta en dyrare väg/);
 for(const k of ['1.99c','2.106c','2.106d','2.107c','2.108c'])a.equal(del(k).niva,'A',k);
});

test('2. E i alfa–beta: nodvärden, rotvärde och begrepp',()=>{
 const mm=(t,max)=>typeof t==='number'?t:(max?Math.max:Math.min)(...t.map(x=>mm(x,!max)));
 for(const[id,v,max]of[['3.70',[[3,7],[2,9],[8,5]],true],['3.71',[[4,1],[6,2],[3,8]],false],['3.72',[[5,9,6],[2,8,7]],true]]){
  a.equal(rätt(id+'a'),String(mm(v[0],!max)),id);a.equal(rätt(id+'b'),String(mm(v,max)),id);a.equal(q(id).niva,'E',id);
  // Det finns en beskärning: B:s första löv är redan sämre för roten än A.
  const A=mm(v[0],!max),b1=v[1][0];a.ok(max?b1<=A:b1>=A,id);}
 a.match(rätt('3.70c'),/^Ja/);a.equal(rätt('3.72c'),'Minimax');
});

test('nivåbalansen räcker för prov och för nya elever i Kunskapsgymmet',()=>{
 const delar=omr=>bank.filter(u=>u.omr===omr).flatMap(u=>u.spelDelar);
 for(const omr of ['ko_stack','prioritetsko'])a.ok(delar(omr).filter(d=>d.niva==='C').length>=5,omr+': C-delkort');
 a.ok(bank.filter(u=>u.omr!=='alfa_beta').flatMap(u=>u.spelDelar).filter(d=>d.niva==='A').length>=8,'A-delkort utanför alfa–beta');
 a.ok(bank.filter(u=>u.omr==='alfa_beta'&&u.niva==='E').length>=4,'hela E-uppgifter i alfa–beta');
 a.ok(delar('dfs').filter(d=>d.traningsniva===1).length>=20,'DFS nivå 1');a.ok(delar('astar_sokning').filter(d=>d.traningsniva===1).length>=28,'A* nivå 1');
 a.ok(delar('viktade_vagar').filter(d=>d.traningsniva<=2).length>=50,'viktade vägar nivå 1–2');
});

test('validatorn hittar inget nytt',()=>{const r=require('./granska-uppgifter.js').granskaProjekt(process.cwd()).resultat.find(x=>x.fil==='uppgifterai.js');
 const ok=f=>(f.kod==='EXACT_TEXT_DUPLICATE'&&['3.04','3.05'].includes(f.id))||(f.kod==='VERY_SIMILAR_TEXT'&&['2.06','2.08'].includes(f.id));
 a.deepEqual(r.fynd.filter(f=>!ok(f)).map(f=>f.kod+' '+f.id+' '+(f.relateradeId||[]).join(',')),[]);});
