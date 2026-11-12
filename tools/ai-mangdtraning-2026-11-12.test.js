'use strict';
// AI-banken 2026-11-12: mängdträning (1.77–1.96, 2.88–2.103, 3.62–3.69).
// Svaren räknas om oberoende av byggskriptet: labyrinter, sökträd och spelträd läses ur
// figurerna som eleven ser, köer och prioritetsköer ur texten.
const {test}=require('node:test'),a=require('node:assert/strict'),fs=require('node:fs'),vm=require('node:vm');
const c={window:{}};vm.runInNewContext(fs.readFileSync('uppgifterai.js','utf8'),c);
const bank=c.window.BANKAI,q=id=>bank.find(u=>u.id===id);
const ids=(k,fr,til)=>Array.from({length:til-fr+1},(_,i)=>`${k}.${fr+i}`);
const NYA=[...ids(1,77,96),...ids(2,88,103),...ids(3,62,69)];
const ORD=['första','andra','tredje','fjärde','femte','sjätte','sjunde','åttonde','nionde','tionde'];
const svgOf=u=>u.spelIntro.match(/<svg[\s\S]*?<\/svg>/)[0];
const ren=h=>String(h).replace(/<[^>]+>/g,' ').replace(/\s+/g,' ').trim();
const rätt=d=>d.svarstyp==='alternativ'?d.alternativ.filter(x=>x.ratt).map(x=>x.txt):d.rättSvar;
const L=xs=>xs.join(', ');

// ---------------------------------------------------------------- labyrinter ur figuren
function labyrint(u){const svg=svgOf(u),celler=[...svg.matchAll(/<rect data-cell="([A-Z])(\d+)" x="(\d+)" y="(\d+)"[^>]*fill="([^"]+)"/g)];
 const R=Math.max(...celler.map(m=>m[1].charCodeAt(0)-64)),C=Math.max(...celler.map(m=>+m[2]));const rows=Array.from({length:R},()=>Array(C).fill('.'));let s,g,P=null;
 const färg={'#334155':'#','#d6b98c':'3'};for(const m of celler){const r=m[1].charCodeAt(0)-65,k=+m[2]-1;
  if(m[5]==='#22a05a')s=[r,k];else if(m[5]==='#d94343')g=[r,k];else if(färg[m[5]])rows[r][k]=färg[m[5]];else a.equal(m[5],'#fff',u.id+' okänd färg');}
 const mark=svg.match(/<rect x="(\d+)" y="(\d+)" width="\d+" height="\d+" fill="#fff3b0"/);
 if(mark){const x0=+celler[0][3],y0=+celler[0][4];P=[Math.floor((+mark[2]-y0)/52),Math.floor((+mark[1]-x0)/52)];}
 a.ok(s&&g,u.id);return{rows:rows.map(r=>r.join('')),s,g,P};}
const nm=([r,k])=>String.fromCharCode(65+r)+(k+1),eqc=(x,y)=>x[0]===y[0]&&x[1]===y[1];
const ÖPPEN=(L,[r,k])=>L.rows[r]?.[k]!==undefined&&L.rows[r][k]!=='#';
const nb=(L,n)=>[[-1,0],[0,1],[1,0],[0,-1]].map(([x,y])=>[n[0]+x,n[1]+y]).filter(v=>ÖPPEN(L,v));
const kost=(L,v)=>L.rows[v[0]][v[1]]==='3'?3:1,man=(x,y)=>Math.abs(x[0]-y[0])+Math.abs(x[1]-y[1]);
function bfs(L){const kö=[L.s],sett=new Set([nm(L.s)]),far={},ut=[],dist={[nm(L.s)]:0};while(kö.length){const n=kö.shift();ut.push(nm(n));if(eqc(n,L.g))break;
  for(const v of nb(L,n))if(!sett.has(nm(v))){sett.add(nm(v));far[nm(v)]=nm(n);dist[nm(v)]=dist[nm(n)]+1;kö.push(v);}}
 const väg=[nm(L.g)];while(far[väg[0]])väg.unshift(far[väg[0]]);return{ut,väg};}
function avstånd(L,från){const d={[nm(från)]:0},kö=[från];while(kö.length){const n=kö.shift();for(const v of nb(L,n))if(!(nm(v) in d)){d[nm(v)]=d[nm(n)]+1;kö.push(v);}}return d;}
function dfs(L){const sett=new Set(),ut=[],st=[];const gå=n=>{sett.add(nm(n));ut.push(nm(n));st.push(nm(n));if(eqc(n,L.g))return true;for(const v of nb(L,n))if(!sett.has(nm(v))&&gå(v))return true;st.pop();return false;};gå(L.s);return{ut,väg:st};}
function billigast(L){const best={[nm(L.s)]:0},klar=new Set(),cell={[nm(L.s)]:L.s};while(true){const n=Object.keys(best).filter(x=>!klar.has(x)).sort((x,y)=>best[x]-best[y])[0];if(!n)break;klar.add(n);
  for(const v of nb(L,cell[n])){const k=nm(v),alt=best[n]+kost(L,v);if(alt<(best[k]??1e9)){best[k]=alt;cell[k]=v;}}}return best[nm(L.g)];}

// ---------------------------------------------------------------- sökträd och spelträd ur figuren
function sökträd(u){const svg=svgOf(u),noder={};let mål=null;
 for(const m of svg.matchAll(/<circle cx="(\d+)" cy="(\d+)" r="18" fill="([^"]+)"[^>]*\/><text[^>]*>([A-Z])<\/text>/g)){noder[`${m[1]},${m[2]}`]=m[4];if(m[3]==='#d94343')mål=m[4];}
 const kids={};for(const m of svg.matchAll(/<line x1="(\d+)" y1="(\d+)" x2="(\d+)" y2="(\d+)"/g)){const[p,b]=+m[2]<+m[4]?[`${m[1]},${m[2]}`,`${m[3]},${m[4]}`]:[`${m[3]},${m[4]}`,`${m[1]},${m[2]}`];
  (kids[noder[p]]??=[]).push([+b.split(',')[0],noder[b]]);}
 for(const k in kids)kids[k]=kids[k].sort((x,y)=>x[0]-y[0]).map(x=>x[1]);return{kids,mål,alla:Object.values(noder)};}
function trädBFS(kids,mål){const kö=['S'],ut=[],far={};while(kö.length){const n=kö.shift();ut.push(n);if(n===mål)break;for(const k of kids[n]||[]){far[k]=n;kö.push(k);}}const v=[mål];while(far[v[0]])v.unshift(far[v[0]]);return{ut,väg:v};}
function trädDFS(kids,mål){const ut=[],st=[];const gå=n=>{ut.push(n);st.push(n);if(n===mål||(kids[n]||[]).some(gå))return true;st.pop();return false;};gå('S');return{ut,väg:st};}
function spelträd(u){const svg=svgOf(u).replace(/<polygon points="\d+,7[\s\S]*$/,'');const pkt=s=>s.split(',').map(Number);
 const linjer=[...svg.matchAll(/<line x1="([\d.]+)" y1="([\d.]+)" x2="([\d.]+)" y2="([\d.]+)"/g)].map(m=>[[+m[1],+m[2]],[+m[3],+m[4]]]);
 const key=p=>p.join(',');const barn={},förälder={};for(const[x,y]of linjer){const[p,b]=x[1]<y[1]?[x,y]:[y,x];(barn[key(p)]??=[]).push(b);förälder[key(b)]=key(p);}
 const rot=Object.keys(barn).find(k=>!(k in förälder));const värde={},namn={};
 for(const m of svg.matchAll(/<rect x="([\d.]+)" y="(\d+)" width="36"[^>]*\/><text x="[\d.]+" y="\d+"[^>]*font-size="18"[^>]*>([−\-\d]+)<\/text>/g))värde[`${+m[1]+18},${+m[2]+16}`]=+m[3].replace('−','-');
 for(const m of svg.matchAll(/<polygon points="([^"]+)"[^>]*\/><text x="([\d.]+)" y="(\d+)"[^>]*>([A-Z])<\/text>/g)){const ps=m[1].split(' ').map(pkt),cx=ps.reduce((s,p)=>s+p[0],0)/3;
  const k=Object.keys(barn).find(k=>Math.abs(pkt(k)[0]-cx)<1&&Math.abs(pkt(k)[1]-(+m[3]-6))<3);namn[k]=m[4];}
 const rotMax=/<polygon points="[^"]+" fill="#dbf5f1"[^>]*\/><text[^>]*>R</.test(svg);
 const bygg=(k,max)=>barn[k]?{namn:namn[k],max,barn:barn[k].sort((x,y)=>x[0]-y[0]).map(b=>bygg(key(b),!max))}:{löv:värde[k]};
 const t=bygg(rot,rotMax);return t;}
const mm=n=>'löv' in n?n.löv:(n.max?Math.max:Math.min)(...n.barn.map(mm));
const hitta=(n,x)=>n.namn===x?n:(n.barn||[]).map(b=>hitta(b,x)).find(Boolean);

test('mängdträningen: 44 uppgifter, självrättande, rätt delmoment och mest E',()=>{
 a.equal(NYA.length,44);for(const id of NYA){const u=q(id);a.ok(u,id);a.equal(u.spel,true);a.equal(u['självrättning'],true);a.equal(u.familjTidigare,undefined,id);a.equal(u.omrTidigare,undefined,id);
  a.doesNotMatch(u.t,/\((Skriv|Svara)[^)]*\)/,id);a.match(u.t,/<svg|Stegen:/,id);
  u.spelDelar.forEach((d,i)=>{a.equal(JSON.stringify(u.rättSvar[i]),JSON.stringify(d.rättSvar));a.match(d.s,/facit-rubrik/);
   for(const x of d.alternativ||[]){a.ok(x.kommentar.length>15,id+x.txt);a.doesNotMatch(x.txt,/^[A-Z]$/,id);}});}
 const parts=NYA.flatMap(id=>q(id).spelDelar);a.ok(parts.filter(d=>d.niva==='E').length/parts.length>=0.85);
});

test('köer, stackar och prioritetsköer räknas om ur texten',()=>{
 for(const id of ids(1,77,82)){const u=q(id),stack=/stack/i.test(u.spelIntro.match(/<title>([^<]*)/)[1]);
  const start=u.spelIntro.match(/<title>(?:FIFO-kö|Stack) med ([A-Z, ]+?)(?:,? där| nerifrån)/)[1].split(', ');
  const steg=ren(u.t).match(/följande steg: (.*?)\. a\)/)[1].split(' → ');const s=[...start],ut=[];
  for(const x of steg){const m=x.match(/^lägg in ([A-Z])$/);if(m)s.push(m[1]);else{a.equal(x,'ta ut en nod');ut.push(stack?s.pop():s.shift());}}
  a.equal(u.spelDelar[0].rättSvar,L(ut),id);a.equal(rätt(u.spelDelar[1])[0],'Noden '+(stack?s.at(-1):s[0]),id);}
 for(const id of ids(2,88,91)){const u=q(id),steg=ren(u.t).match(/Stegen: (.*?)\. a\)/)[1].split(' → '),kö=[],ut=[];
  for(const x of steg){const m=x.match(/^lägg in ([A-Z])\((\d+)\)$/);if(m)kö.push([m[1],+m[2]]);else{kö.sort((p,r)=>p[1]-r[1]||p[0].localeCompare(r[0]));ut.push(kö.shift());}}
  const d=u.spelDelar;a.equal(d[0].rättSvar,L(ut.map(x=>x[0])),id);a.equal(d[1].rättSvar,ut[2][1]);a.equal(d[2].rättSvar,Math.min(...kö.map(x=>x[1])));}
});

test('BFS och DFS i labyrinter räknas om ur figuren',()=>{
 for(const id of [...ids(1,83,86),...ids(1,87,90)]){const u=q(id),Lab=labyrint(u),dfsUpg=+id.split('.')[1]>=87;
  const r=dfsUpg?dfs(Lab):bfs(Lab),bv=bfs(Lab).väg;
  for(const d of u.spelDelar){const f=ren(d.fraga),k=f.match(/som ([a-zåäö]+) ruta/);
   if(k)a.equal(rätt(d)[0],r.ut[ORD.indexOf(k[1])],id+d.etikett);
   else if(/exakt (\d+) steg/.test(f)){const n=+f.match(/exakt (\d+) steg/)[1];a.equal(d.rättSvar,Object.values(avstånd(Lab,Lab.s)).filter(v=>v===n).length,id+d.etikett);}
   else if(/Hur många steg har vägen/.test(f))a.equal(d.rättSvar,r.väg.length-1,id+d.etikett);
   else if(/Hur många rutor (tas ut|besöker)/.test(f))a.equal(d.rättSvar,r.ut.length,id+d.etikett);
   else if(/en av de kortaste/.test(f))a.equal(rätt(d)[0],r.väg.length===bv.length?'Ja':'Nej',id+d.etikett);
   else a.fail(id+d.etikett+': okänd fråga '+f);}}
});

test('BFS och DFS i sökträd räknas om ur figuren',()=>{
 for(const id of ids(1,91,96)){const u=q(id),{kids,mål,alla}=sökträd(u),r=+id.split('.')[1]>=94?trädDFS(kids,mål):trädBFS(kids,mål);
  const d=u.spelDelar;a.equal(d[0].rättSvar,L(r.ut),id);a.equal(d[1].rättSvar,alla.length-r.ut.length,id);a.equal(d[2].rättSvar,L(r.väg),id);
  a.ok(r.ut.length>=5&&r.ut.length<=9,id);}
});

test('g, h och f samt A*:s första steg räknas om ur figuren',()=>{
 for(const id of ids(2,92,95)){const u=q(id),Lab=labyrint(u);a.ok(Lab.P,id);const gv=avstånd(Lab,Lab.s)[nm(Lab.P)],hv=man(Lab.P,Lab.g);
  a.equal(gv,man(Lab.P,Lab.s),id+': g följer en rak väg (E-nivå)');
  const d=u.spelDelar;a.equal(d[0].rättSvar,gv,id);a.equal(d[1].rättSvar,hv,id);a.equal(d[2].rättSvar,gv+hv,id);}
 for(const id of ids(2,96,99)){const u=q(id),Lab=labyrint(u),grannar=nb(Lab,Lab.s).sort((x,y)=>nm(x).localeCompare(nm(y)));
  const f=grannar.map(v=>1+man(v,Lab.g)),d=u.spelDelar;
  a.equal(JSON.stringify(d[0].svarEtiketter),JSON.stringify(grannar.map(v=>'f för '+nm(v))),id);a.equal(JSON.stringify(d[0].rättSvar),JSON.stringify(f),id);
  const bäst=grannar.map((v,i)=>[f[i],man(v,Lab.g),nm(v)]).sort((x,y)=>x[0]-y[0]||x[1]-y[1]||x[2].localeCompare(y[2]))[0][2];
  a.equal(rätt(d[1])[0],'Rutan '+bäst,id);a.equal(d[2].rättSvar,bfs(Lab).väg.length-1,id);}
});

test('vägkostnad i labyrinter räknas om ur figuren',()=>{
 for(const id of ids(2,100,103)){const u=q(id),Lab=labyrint(u),d=u.spelDelar;
  const väg=ren(d[0].fraga).match(/vägen (.*)\?/)[1].split(' → '),cells=väg.map(x=>[x.charCodeAt(0)-65,+x.slice(1)-1]);
  for(let i=1;i<cells.length;i++){a.equal(man(cells[i],cells[i-1]),1,id);a.ok(ÖPPEN(Lab,cells[i]),id);}
  a.ok(eqc(cells[0],Lab.s)&&eqc(cells.at(-1),Lab.g),id);
  a.equal(d[0].rättSvar,cells.slice(1).reduce((s,v)=>s+kost(Lab,v),0),id);const b=billigast(Lab);a.equal(d[1].rättSvar,b,id);
  // Billigaste väg bland dem med färst steg (lager för lager).
  const dist=avstånd(Lab,Lab.s),best={[nm(Lab.s)]:0};const celler=Object.keys(dist).sort((x,y)=>dist[x]-dist[y]);
  for(const k of celler){const n=[k.charCodeAt(0)-65,+k.slice(1)-1];for(const v of nb(Lab,n))if(dist[nm(v)]===dist[k]+1)best[nm(v)]=Math.min(best[nm(v)]??1e9,best[k]+kost(Lab,v));}
  a.match(ren(d[2].fraga),new RegExp(`har ${dist[nm(Lab.g)]} steg`));a.equal(rätt(d[2])[0].startsWith('Ja'),best[nm(Lab.g)]===b,id);}
});

test('minimax och beskärning med stöd räknas om ur figuren',()=>{
 for(const id of ids(3,62,65)){const u=q(id),t=spelträd(u),d=u.spelDelar,nod=ren(d[0].fraga).match(/värde får ([A-Z])\?/)[1];
  a.equal(d[0].rättSvar,mm(hitta(t,nod)),id);a.equal(d[1].rättSvar,mm(t),id);
  const bäst=t.barn.filter(b=>mm(b)===mm(t));a.equal(bäst.length,1,id);a.equal(rätt(d[2])[0],'Draget till '+bäst[0].namn,id);}
 for(const id of ids(3,66,69)){const u=q(id),t=spelträd(u),d=u.spelDelar,[A,B]=t.barn,l3=B.barn[0].löv;
  a.equal(+ren(u.t).match(/L3 = (\d+)/)[1],l3,id);a.equal(d[0].rättSvar,mm(A),id);a.equal(d[2].rättSvar,mm(t),id);
  // B blir högst L3 (MIN-nod) eller minst L3 (MAX-nod). L4 behövs bara om B ändå kan slå A.
  const kapa=t.max?l3<=mm(A):l3>=mm(A);a.equal(rätt(d[1])[0].startsWith('Nej'),kapa,id);a.equal(d[1].niva,'C',id);}
 const kap=ids(3,66,69).map(id=>rätt(q(id).spelDelar[1])[0].startsWith('Nej'));a.ok(kap.includes(true),'minst en uppgift där L4 kan hoppas över');
});

test('validatorn hittar inget nytt',()=>{const r=require('./granska-uppgifter.js').granskaProjekt(process.cwd()).resultat.find(x=>x.fil==='uppgifterai.js');
 const ok=f=>(f.kod==='EXACT_TEXT_DUPLICATE'&&['3.04','3.05'].includes(f.id))||(f.kod==='VERY_SIMILAR_TEXT'&&['2.06','2.08'].includes(f.id));
 a.deepEqual(r.fynd.filter(f=>!ok(f)).map(f=>f.kod+' '+f.id+' '+(f.relateradeId||[]).join(',')),[]);});
