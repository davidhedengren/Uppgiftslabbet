'use strict';
// AI-banken 2026-11-12, omgång 10: alfa–beta på C-nivå (3.73–3.78) och BFS på A-nivå (1.104–1.106).
// Svaren räknas om med egen alfa–beta, BFS och billigaste väg.
const {test}=require('node:test'),a=require('node:assert/strict'),fs=require('node:fs'),vm=require('node:vm');
const c={window:{}};vm.runInNewContext(fs.readFileSync('uppgifterai.js','utf8'),c);
const bank=c.window.BANKAI,q=id=>bank.find(u=>u.id===id),del=k=>q(k.slice(0,-1)).spelDelar.find(d=>d.etikett===k.slice(-1));
const rätt=k=>{const d=del(k);return d.svarstyp==='alternativ'?d.alternativ.filter(x=>x.ratt).map(x=>x.txt).join('|'):d.rättSvar;};
const NYA=['3.73','3.74','3.75','3.76','3.77','3.78','1.104','1.105','1.106'];

// Alfa–beta som returnerar värde och vilka löv som utvärderas (löven numreras L1, L2, … från vänster).
function ab(t,max,al=-Infinity,be=Infinity,logg=[],nr={i:0}){if(typeof t==='number'){logg.push(++nr.i);return t;}
 let v=max?-Infinity:Infinity;for(let i=0;i<t.length;i++){const x=ab(t[i],!max,al,be,logg,nr);if(max){v=Math.max(v,x);al=Math.max(al,v);}else{v=Math.min(v,x);be=Math.min(be,v);}
  if(al>=be){const hoppa=n=>typeof n==='number'?1:n.reduce((s,k)=>s+hoppa(k),0);nr.i+=t.slice(i+1).reduce((s,k)=>s+hoppa(k),0);break;}}return v;}
const mm=(t,max)=>typeof t==='number'?t:(max?Math.max:Math.min)(...t.map(x=>mm(x,!max)));

test('format, delmoment och nivåer',()=>{
 for(const id of NYA){const u=q(id);a.ok(u,id);a.equal(u.spel,true);a.doesNotMatch(u.t,/\((Skriv|Svara)[^)]*\)/,id);a.match(u.t,/<svg/,id);
  for(const d of u.spelDelar){a.match(d.s,/facit-rubrik/);for(const x of d.alternativ||[]){a.ok(x.kommentar.length>15,id+x.txt);a.doesNotMatch(x.txt,/^[A-Z]$/);}}}
 for(const id of ['3.73','3.74','3.75','3.78'])a.equal(q(id).familj,'Beskärningens idé');for(const id of ['3.76','3.77'])a.equal(q(id).familj,'Rotvärde och beskurna löv');
 for(const id of ['1.104','1.105','1.106']){a.equal(q(id).familj,'BFS i labyrinter');a.equal(del(id+'c').niva,'A',id);}
 for(const k of ['3.73b','3.73c','3.74b','3.74c','3.75b','3.75c','3.76a','3.76b','3.76c','3.77b','3.78a','3.78b','3.78c'])a.equal(del(k).niva,'C',k);
 // Svaren på stödfrågorna varierar.
 const svar=['3.73','3.74','3.75'].flatMap(id=>[rätt(id+'b'),rätt(id+'c')]);a.ok(svar.includes('Ja')&&svar.includes('Nej'));
});

test('alfa–beta med stöd räknas om',()=>{
 for(const[id,t,max]of[['3.73',[[4,7],[2,9],[6,5]],true],['3.74',[[3,8],[5,6],[2,9]],true],['3.75',[[6,2],[8,1],[4,5]],false]]){
  const logg=[],v=ab(t,max,-Infinity,Infinity,logg);a.equal(v,mm(t,max),id);
  a.equal(rätt(id+'a'),mm(t[0],!max),id);a.equal(rätt(id+'d'),v,id);
  a.equal(rätt(id+'b'),logg.includes(4)?'Ja':'Nej',id+'b');a.equal(rätt(id+'c'),logg.includes(6)?'Ja':'Nej',id+'c');}
 for(const[id,t,max]of[['3.76',[[5,8,6,9],[7,3,8,4],[9,6,7,10]],true],['3.77',[[2,6,4,3],[5,1,9,2],[4,8,3,7]],false]]){
  const logg=[],v=ab(t,max,-Infinity,Infinity,logg);a.equal(rätt(id+'a'),mm(t[0],!max),id);a.equal(rätt(id+'c'),v,id);
  a.equal(rätt(id+'b'),logg.filter(x=>x>=5&&x<=8).length,id);}
 const bild=[[6,5],[9,7,4,8]],bra=[[6,5],[4,9,7,8]];
 for(const[t,k]of[[bild,'3.78a'],[bra,'3.78b']]){const logg=[];ab(t,true,-Infinity,Infinity,logg);a.equal(rätt(k),logg.filter(x=>x>=3).length,k);}
 a.match(rätt('3.78c'),/lägsta värdena/);
});

test('BFS på A-nivå räknas om',()=>{
 const bfs=(rows,s,g)=>{const R=rows.length,C=rows[0].length,kö=[s],sett=new Set([s.join()]),far={},ut=[];while(kö.length){const n=kö.shift();ut.push(n);if(n.join()===g.join())break;
  for(const[x,y]of[[-1,0],[0,1],[1,0],[0,-1]]){const v=[n[0]+x,n[1]+y];if(v[0]>=0&&v[1]>=0&&v[0]<R&&v[1]<C&&rows[v[0]][v[1]]!=='#'&&!sett.has(v.join())){sett.add(v.join());far[v.join()]=n;kö.push(v);}}}
  const väg=[g];while(far[väg[0].join()])väg.unshift(far[väg[0].join()]);return{ut,väg};};
 const M=['S3..','.3#.','...G'],kost=v=>/\d/.test(M[v[0]][v[1]])?+M[v[0]][v[1]]:1,{väg}=bfs(M,[0,0],[2,3]);
 a.equal(rätt('1.104a'),väg.slice(1).reduce((s,v)=>s+kost(v),0));
 const best={'0,0':0},kv=new Set(['0,0']);while(kv.size){const x=[...kv].sort((p,r)=>best[p]-best[r])[0];kv.delete(x);const n=x.split(',').map(Number);
  for(const[dx,dy]of[[-1,0],[0,1],[1,0],[0,-1]]){const v=[n[0]+dx,n[1]+dy];if(v[0]<0||v[1]<0||v[0]>2||v[1]>3||M[v[0]][v[1]]==='#')continue;const alt=best[x]+kost(v);if(alt<(best[v.join()]??1e9)){best[v.join()]=alt;kv.add(v.join());}}}
 a.equal(rätt('1.104b'),best['2,3']);a.ok(rätt('1.104a')>rätt('1.104b'));a.match(rätt('1.104c'),/behöver inte vara billigast/);
 const öppet=(R,C)=>Array.from({length:R},()=>'.'.repeat(C));
 a.equal(rätt('1.105a'),bfs(öppet(3,4),[0,0],[2,3]).ut.length);a.equal(rätt('1.105b'),bfs(öppet(5,6),[0,0],[4,5]).ut.length);
 for(let R=2;R<=6;R++)for(let C=2;C<=6;C++)a.equal(bfs(öppet(R,C),[0,0],[R-1,C-1]).ut.length,R*C);a.equal(rätt('1.105c'),'R · C');
 const avst=k=>{let n=0;for(let r=0;r<6;r++)for(let c=0;c<6;c++)if(r+c===k)n++;return n;};
 a.equal(rätt('1.106a'),avst(3));a.equal(rätt('1.106b'),avst(5));for(let k=0;k<=5;k++)a.equal(avst(k),k+1);a.equal(rätt('1.106c'),'k + 1');
});

test('alfa–beta på C-nivå och BFS på A-nivå finns nu för prov',()=>{
 const delar=omr=>bank.filter(u=>u.omr===omr).flatMap(u=>u.spelDelar);
 a.ok(delar('alfa_beta').filter(d=>d.niva==='C').length>=35,'alfa–beta C');a.ok(delar('bfs').filter(d=>d.niva==='A').length>=3,'BFS A');
});

test('validatorn hittar inget nytt',()=>{const r=require('./granska-uppgifter.js').granskaProjekt(process.cwd()).resultat.find(x=>x.fil==='uppgifterai.js');
 const ok=f=>(f.kod==='EXACT_TEXT_DUPLICATE'&&['3.04','3.05'].includes(f.id))||(f.kod==='VERY_SIMILAR_TEXT'&&['2.06','2.08'].includes(f.id));
 a.deepEqual(r.fynd.filter(f=>!ok(f)).map(f=>f.kod+' '+f.id+' '+(f.relateradeId||[]).join(',')),[]);});
