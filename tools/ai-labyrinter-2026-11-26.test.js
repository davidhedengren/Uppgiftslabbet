'use strict';
// AI-banken 2026-11-26 (tools/bygg-ai-labyrinter-2026-11-26.py): labyrinter med riktiga väggar.
// 15 uppgifter vars labyrint saknade väggar (eller hade en enda) är ombyggda, och 2.123–2.152 är nya
// g(n)-, h(n)- och f(n)-uppgifter för en markerad ruta. Alla svar räknas om här, oberoende av byggskriptet,
// ur figuren som eleven ser (väggar, terräng, start, mål och markerad ruta).
const {test}=require('node:test'),a=require('node:assert/strict'),fs=require('node:fs'),vm=require('node:vm');
const c={window:{}};vm.runInNewContext(fs.readFileSync('uppgifterai.js','utf8'),c);
const bank=c.window.BANKAI,q=id=>bank.find(u=>u.id===id);
const OMBYGGDA=['1.104','2.25','2.27','2.28','2.29','2.42','2.44','2.48','2.51','2.53','2.55','2.57','2.63','2.75','2.108'];
const NYA=Array.from({length:30},(_,i)=>`2.${123+i}`);
const ren=h=>String(h).replace(/<svg[\s\S]*?<\/svg>/g,' ').replace(/<[^>]+>/g,' ').replace(/&gt;/g,'>').replace(/\s+/g,' ').trim();
const rätt=d=>d.svarstyp==='alternativ'?d.alternativ.filter(x=>x.ratt).map(x=>x.txt)[0]:d.rättSvar;

function labyrint(u){const svg=u.spelIntro.match(/<svg[\s\S]*?<\/svg>/)[0],celler=[...svg.matchAll(/<rect data-cell="([A-Z])(\d+)" x="(\d+)" y="(\d+)"[^>]*fill="([^"]+)"/g)];
 const R=Math.max(...celler.map(m=>m[1].charCodeAt(0)-64)),C=Math.max(...celler.map(m=>+m[2]));const rows=Array.from({length:R},()=>Array(C).fill('.'));let s,g,P=null;
 const färg={'#334155':'#','#d6b98c':'3','#c4d7ef':'4','#f4ba88':'5'};for(const m of celler){const r=m[1].charCodeAt(0)-65,k=+m[2]-1;
  if(m[5]==='#22a05a')s=[r,k];else if(m[5]==='#d94343')g=[r,k];else if(färg[m[5]])rows[r][k]=färg[m[5]];else a.equal(m[5],'#fff',u.id+' okänd färg');}
 const mark=svg.match(/<rect x="(\d+)" y="(\d+)" width="\d+" height="\d+" fill="#fff3b0"/);
 if(mark){const x0=+celler[0][3],y0=+celler[0][4];P=[Math.floor((+mark[2]-y0)/52),Math.floor((+mark[1]-x0)/52)];}
 a.ok(s&&g,u.id);return{rows:rows.map(r=>r.join('')),s,g,P};}
const nm=([r,k])=>String.fromCharCode(65+r)+(k+1),cell=t=>[t.charCodeAt(0)-65,+t.slice(1)-1],eqc=(x,y)=>x[0]===y[0]&&x[1]===y[1];
const öppen=(L,[r,k])=>L.rows[r]?.[k]!==undefined&&L.rows[r][k]!=='#';
const nb=(L,n)=>[[-1,0],[0,1],[1,0],[0,-1]].map(([x,y])=>[n[0]+x,n[1]+y]).filter(v=>öppen(L,v));
const kost=(L,v)=>/[345]/.test(L.rows[v[0]][v[1]])?+L.rows[v[0]][v[1]]:1,man=(x,y)=>Math.abs(x[0]-y[0])+Math.abs(x[1]-y[1]);
const vägkost=(L,väg)=>väg.slice(1).reduce((s,v)=>s+kost(L,v),0);
const vägur=t=>t.split(' → ').map(cell);
function giltig(L,väg){a.ok(eqc(väg[0],L.s));a.ok(eqc(väg.at(-1),L.g));for(let i=1;i<väg.length;i++){a.ok(öppen(L,väg[i]));a.equal(man(väg[i-1],väg[i]),1);}}
function bfs(L){const kö=[L.s],far={},sett=new Set([nm(L.s)]);while(kö.length){const n=kö.shift();if(eqc(n,L.g))break;
  for(const v of nb(L,n))if(!sett.has(nm(v))){sett.add(nm(v));far[nm(v)]=n;kö.push(v);}}
 const väg=[L.g];while(far[nm(väg[0])])väg.unshift(far[nm(väg[0])]);return väg;}
function billigast(L,mål=L.g){const best={[nm(L.s)]:0},klar=new Set(),cel={[nm(L.s)]:L.s};for(;;){const n=Object.keys(best).filter(x=>!klar.has(x)).sort((x,y)=>best[x]-best[y])[0];if(!n)break;klar.add(n);
  for(const v of nb(L,cel[n])){const k=nm(v),alt=best[n]+kost(L,v);if(alt<(best[k]??1e9)){best[k]=alt;cel[k]=v;}}}return best[nm(mål)];}
function girig(L){const öppna=[L.s],sett=new Set([nm(L.s)]),far={},ut=[];while(öppna.length){öppna.sort((x,y)=>man(x,L.g)-man(y,L.g)||(nm(x)<nm(y)?-1:1));const n=öppna.shift();ut.push(n);if(eqc(n,L.g))break;
  for(const v of nb(L,n))if(!sett.has(nm(v))){sett.add(nm(v));far[nm(v)]=n;öppna.push(v);}}
 const väg=[L.g];while(far[nm(väg[0])])väg.unshift(far[nm(väg[0])]);return{ut,väg};}
function astar(L){const g={[nm(L.s)]:0},cel={[nm(L.s)]:L.s},öppna=new Set([nm(L.s)]),stängda=new Set(),ut=[],efter=[];const h=k=>man(cel[k],L.g),f=k=>g[k]+h(k);
 while(öppna.size){const n=[...öppna].sort((x,y)=>f(x)-f(y)||h(x)-h(y)||(x<y?-1:1))[0];öppna.delete(n);stängda.add(n);ut.push(n);
  if(eqc(cel[n],L.g)){efter.push(new Set(öppna));break;}
  for(const v of nb(L,cel[n])){const k=nm(v);if(stängda.has(k))continue;const alt=g[n]+kost(L,v);if(alt<(g[k]??1e9)){g[k]=alt;cel[k]=v;öppna.add(k);}}efter.push(new Set(öppna));}
 return{ut,efter,g,f};}
const lista=xs=>[...xs].sort().join(', ');
const ochLista=xs=>{xs=[...xs].sort();return xs.length>1?xs.slice(0,-1).join(', ')+' och '+xs.at(-1):xs[0];};

function förväntat(u,d,L){const F=ren(d.fraga);let m;
 if((m=F.match(/^Bestäm ([ghf])\(n\) för rutan ([A-Z])\.$/))){a.ok(L.P,u.id+' markerad ruta');a.ok(u.spelIntro.includes(`>${m[2]}</text>`),u.id+' bokstaven i figuren');
  const gv=billigast(L,L.P),hv=man(L.P,L.g);return{g:gv,h:hv,f:gv+hv}[m[1]];}
 if(/^Vad kostar den billigaste vägen/.test(F))return billigast(L);
 if((m=F.match(/^Vad kostar vägen ([A-Z]\d+(?: → [A-Z]\d+)+)\?$/))){const v=vägur(m[1]);giltig(L,v);return vägkost(L,v);}
 if((m=F.match(/^Vägen ([A-Z]\d+(?: → [A-Z]\d+)+) har (lika många steg som|färre steg än) den billigaste vägen\. Vad kostar den\?$/))){const v=vägur(m[1]);giltig(L,v);
  const billig=u.spelDelar.find(x=>/Ange den billigaste vägen/.test(x.fraga)).rättSvar.split(', ').length;
  a.ok(m[2]==='lika många steg som'?v.length===billig:v.length<billig,u.id+' stegjämförelsen');return String(vägkost(L,v));}
 if((m=F.match(/^Hur många lerrutor går vägen ([A-Z]\d+(?: → [A-Z]\d+)+) genom\?$/))){const v=vägur(m[1]);giltig(L,v);return v.slice(1).filter(x=>L.rows[x[0]][x[1]]==='3').length;}
 const vägar=[...ren(u.spelIntro).matchAll(/Väg (\d): ([A-Z]\d+(?: → [A-Z]\d+)+)\./g)].map(x=>vägur(x[2]));
 if(/^Vilken väg är billigast\?$/.test(F)){vägar.forEach(v=>giltig(L,v));const[k1,k2]=vägar.map(v=>vägkost(L,v));return k1<k2?'Väg 1':k2<k1?'Väg 2':'De kostar lika mycket';}
 if(/^Vad kostar väg 1\?$/.test(F))return vägkost(L,vägar[0]);
 if(/^Vad kostar vägen som girig bäst först hittar\?$/.test(F))return vägkost(L,girig(L).väg);
 if(/^Vad kostar vägen som A\* hittar\?$/.test(F))return billigast(L);
 if(/^Vad kostar vägen som BFS hittar\?$/.test(F))return vägkost(L,bfs(L));
 if(/^Ange den billigaste vägen\.$/.test(F)){const v=d.rättSvar.split(', ').map(cell);giltig(L,v);a.equal(vägkost(L,v),billigast(L));return d.rättSvar;}
 if(/^Vilken granne till start tar girig bäst först ut först\?$/.test(F))return nm(girig(L).ut[1]);
 if(/^Vilken granne till start tar A\* ut först\?$/.test(F))return astar(L).ut[1];
 if(/^Vilken av grannarna till start har lägst f\(n\)\?$/.test(F))return astar(L).ut[1];
 if((m=F.match(/^Vilket f\(n\)-värde har ([A-Z]\d+)\?$/))){const v=cell(m[1]);a.ok(nb(L,L.s).some(x=>eqc(x,v)));return kost(L,v)+man(v,L.g);}
 if(/^Ange i vilken ordning rutorna tas ut ur öppna listan\.$/.test(F))return astar(L).ut.join(', ');
 if(/^Vilka rutor ligger kvar i öppna listan när målet tas ut\?$/.test(F))return lista(astar(L).efter.at(-1));
 if((m=F.match(/^Vilka rutor ligger i öppna listan direkt efter att ([A-Z]\d+) har tagits ut\?$/))){const A=astar(L);a.equal(A.ut[1],m[1]);return ochLista(A.efter[1]);}
 if((m=F.match(/^Hur många av rutorna i öppna listan har f\(n\) = (\d+)\?$/))){const A=astar(L);const kvar=[...A.efter[1]];a.equal(Math.min(...kvar.map(A.f)),+m[1]);return kvar.filter(k=>A.f(k)===+m[1]).length;}
 if(/^Hur många grannar har start\?$/.test(F))return nb(L,L.s).length;
 if(/^Vilken ruta tar girig bäst först ut efter start\?$/.test(F))return nm(girig(L).ut[1]);
 if(/^Vilket h\(n\)-värde har den rutan\?$/.test(F))return man(girig(L).ut[1],L.g);
 if((m=F.match(/^([A-Z]\d+) ligger kvar i öppna listan med samma f\(n\) som målet\. Varför tas målet ut före \1\?$/))){const A=astar(L);
  a.ok(A.efter.at(-1).has(m[1]));a.equal(A.f(m[1]),A.g[nm(L.g)]);return 'Målet har lägst h(n), och vid lika f(n) väljs lägst h(n)';}
 if(/^Vilket påstående om (girig bäst först|BFS) stämmer i alla labyrinter/.test(F))return null;
 a.fail(u.id+d.etikett+' okänd fråga: '+F);}

test('45 labyrintuppgifter med riktiga väggar som tvingar fram omvägar',()=>{
 for(const id of [...OMBYGGDA,...NYA]){const u=q(id);a.ok(u,id);const L=labyrint(u);
  const väggar=L.rows.join('').split('#').length-1;a.ok(väggar>=3,id+' väggar');
  a.ok(bfs(L).length-1>man(L.s,L.g),id+' väggarna ska tvinga fram en omväg');
  a.ok(L.rows.length>=4&&L.rows[0].length>=4,id+' storlek');}
 const storlekar=new Set(NYA.map(id=>{const L=labyrint(q(id));return L.rows.length+'x'+L.rows[0].length;}));a.ok(storlekar.size>=5,'varierade storlekar');
 const lera=NYA.filter(id=>/[345]/.test(labyrint(q(id)).rows.join(''))).length;a.ok(lera>=6&&lera<=15,'några med terräng: '+lera);});

test('alla svar räknas om ur figuren',()=>{
 for(const id of [...OMBYGGDA,...NYA]){const u=q(id),L=labyrint(u);a.equal(u.svarstyp,'flera_delar');a.equal(u.spel,true);a.equal(u['självrättning'],true);
  u.spelDelar.forEach((d,i)=>{a.equal(JSON.stringify(u.rättSvar[i]),JSON.stringify(d.rättSvar),id+d.etikett);
   const v=förväntat(u,d,L);if(v!==null)a.equal(String(rätt(d)),String(v),id+d.etikett+' '+ren(d.fraga));
   a.match(d.s,/facit-rubrik/);a.match(d.s,new RegExp('Svar:'));
   if(d.svarstyp==='alternativ'){a.equal(d.alternativ.filter(x=>x.ratt).length,1,id+d.etikett);a.equal(new Set(d.alternativ.map(x=>x.txt)).size,d.alternativ.length);
    for(const x of d.alternativ)a.ok(x.kommentar.length>15,id+d.etikett+' '+x.txt);}
   else if(d.svarFormat==='numeriskt'){a.ok(Number.isInteger(d.rättSvar));a.equal(d.tolerans,0);}});}});

test('de nya g(n)-, h(n)- och f(n)-uppgifterna: format, delmoment, nivå och varierad text',()=>{
 const texter=new Set();
 for(const id of NYA){const u=q(id);a.equal(u.omr,'astar_varden');a.equal(u.familj,'g, h och f för en ruta');a.equal(u.niva,'E');a.equal(u.poang,'3/0/0');
  a.equal(JSON.stringify(u.formaga),'["procedur"]');a.equal(JSON.stringify(u.spelDelar.map(d=>d.traningsniva)),'[2,1,1]');
  const L=u.spelDelar.map(d=>ren(d.fraga).match(/rutan ([A-Z])\./)[1]);a.equal(new Set(L).size,1);
  a.equal(u.spelDelar.map(d=>ren(d.fraga).slice(0,10)).join('|'),'Bestäm g(n|Bestäm h(n|Bestäm f(n');
  const t=ren(u.t);a.ok(!texter.has(t),id+' samma text som en annan uppgift');texter.add(t);
  a.match(t,/A\*/);a.match(t,/Manhattanavståndet/);}
 // g(n) skiljer sig oftast från Manhattanavståndet från start, eftersom väggarna eller terrängen tvingar fram en omväg.
 const omväg=NYA.filter(id=>{const L=labyrint(q(id));return billigast(L,L.P)>man(L.s,L.P);}).length;a.ok(omväg>=27,'omvägar: '+omväg);});

test('texten: f(n)-notation och inga påklistrade alternativ',()=>{
 for(const id of [...OMBYGGDA,...NYA]){const u=q(id),txt=JSON.stringify(u);
  a.doesNotMatch(txt,/Välj ett alternativ/,id);a.doesNotMatch(ren(u.t),/\b[fgh] = /,id);a.doesNotMatch(txt,/f\(n\) = g\(n\) \+ h\([A-Z]\)/,id);
  a.doesNotMatch(txt,/\.\./,id);}
 for(const id of ['2.61','2.120'])a.doesNotMatch(JSON.stringify(q(id)),/f\(n\) = g\(n\) \+ h\([A-Z]\)/,id);});
