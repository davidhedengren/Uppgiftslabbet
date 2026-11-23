'use strict';
// AI-banken 2026-11-23: spelträd på nivå 1–5 (3.81–3.215 med spelsammanhang, 3.216–3.255 med enkla tillämpningar),
// se agent/AI_SPELTRAD_NIVAER_2026-11-23.md.
// Träden läses ur frågans figur och svaren räknas om oberoende av byggskriptet.
const {test}=require('node:test');
const a=require('node:assert/strict');
const fs=require('node:fs'),vm=require('node:vm'),path=require('node:path');
const c={window:{}};vm.runInNewContext(fs.readFileSync(path.join(__dirname,'../uppgifterai.js'),'utf8'),c);
const B=c.window.BANKAI;
const NYA=B.filter(q=>q.kap===3&&+q.id.split('.')[1]>=81&&+q.id.split('.')[1]<=255);
const TILL=NYA.filter(q=>+q.id.split('.')[1]>=216);
const nr=q=>+q.id.split('.')[1];

// ---------------------------------------------------------------- trädet ur figuren
function träd(u){
 const svg=u.spelIntro.match(/<svg[\s\S]*?<\/svg>/)[0].replace(/<polygon points="20,7[\s\S]*$/,'');
 const linjer=[...svg.matchAll(/<line x1="([\d.]+)" y1="([\d.]+)" x2="([\d.]+)" y2="([\d.]+)"/g)].map(m=>[+m[1],+m[2],+m[3],+m[4]]);
 const noder=[];
 for(const m of svg.matchAll(/<polygon points="([^"]+)" fill="(#[0-9a-f]+)"[^>]*\/><text x="([\d.]+)" y="(\d+)"[^>]*>([A-Z])<\/text>/g)){
  const ps=m[1].split(' ').map(s=>s.split(',').map(Number));
  noder.push({namn:m[5],x:ps.reduce((s,p)=>s+p[0],0)/3,y:+m[4]-6,max:m[2]==='#dbf5f1',barn:[]});}
 for(const m of svg.matchAll(/<rect x="([\d.]+)" y="(\d+)" width="36"[^>]*\/><text x="([\d.]+)" y="\d+"[^>]*font-size="18"[^>]*>([−\d]+)<\/text><text[^>]*>(L\d+)<\/text>/g))
  noder.push({namn:m[5],x:+m[3],y:+m[2]+16,löv:+m[4].replace('−','-')});
 const vid=(x,y)=>{const n=noder.find(n=>Math.abs(n.x-x)<0.6&&Math.abs(n.y-y)<0.6);a.ok(n,u.id+` ingen nod vid ${x},${y}`);return n;};
 for(const[x1,y1,x2,y2]of linjer)vid(x1,y1).barn.push(vid(x2,y2));
 for(const n of noder)if(n.barn)n.barn.sort((p,q)=>p.x-q.x);
 const rot=noder.find(n=>n.namn==='R');a.ok(rot,u.id);
 return rot;
}
const mm=n=>'löv' in n?n.löv:(n.max?Math.max:Math.min)(...n.barn.map(mm));
const lövnamn=n=>'löv' in n?[n.namn]:n.barn.flatMap(lövnamn);
function alfabeta(rot){
 const beskurna=[],in_={},cut={};
 const ab=(n,al,be)=>{
  if('löv' in n)return n.löv;
  in_[n.namn]=[al,be];
  let v=n.max?-Infinity:Infinity;
  for(let i=0;i<n.barn.length;i++){
   const x=ab(n.barn[i],al,be);
   if(n.max){v=Math.max(v,x);al=Math.max(al,v);}else{v=Math.min(v,x);be=Math.min(be,v);}
   if(al>=be&&i+1<n.barn.length){cut[n.namn]=[al,be];for(const k of n.barn.slice(i+1))beskurna.push(...lövnamn(k));break;}
  }
  return v;};
 return {v:ab(rot,-Infinity,Infinity),beskurna,in_,cut};
}

test('175 nya uppgifter, en fråga var, nivåtrappan 1–5',()=>{
 a.equal(NYA.length,175);a.equal(TILL.length,40);
 const per=[0,0,0,0,0,0];for(const q of NYA)per[q.traningsniva]++;
 a.deepEqual(per.slice(1),[38,38,33,33,33]);
 for(const q of NYA){
  const tn=q.traningsniva,fork={1:'E',2:'E',3:'C',4:'A',5:'A'}[tn];
  a.equal(q.niva,fork,q.id);a.equal(q.spelDelar.length,1,q.id);a.equal(q.spelDelar[0].traningsniva,tn,q.id);a.equal(q.visaSomDelkort,true,q.id);
  a.equal(q.omr,tn<=2?'minimax':'alfa_beta',q.id);a.match(q.t,/(MAX|MIN) väljer först|Först väljer /,q.id);
  a.equal(q.spel,true);a.equal(q.självrättning,true);
  a.ok(q.t.startsWith(q.spelIntro)&&q.t.endsWith(q.spelDelar[0].fraga),q.id); // fristående kort, ingen a)
  a.doesNotMatch(q.t,/<p>a\)|\((Skriv|Svara)/,q.id);
  a.match(q.s,/class="facit-svar"/);a.match(q.s,/<svg/,q.id+': facit har trädet');
  a.ok(q.ledtrad.length>40,q.id);
 }
});

test('Nivå 1–2: rotens minimaxvärde, små respektive större träd',()=>{
 for(const q of NYA.filter(q=>q.traningsniva<=2)){
  const r=träd(q),lov=lövnamn(r).length,vals=[];const plock=n=>'löv' in n?vals.push(n.löv):n.barn.forEach(plock);plock(r);
  a.equal(q.rättSvar[0],mm(r),q.id);a.equal(q.spelDelar[0].rättSvar,mm(r),q.id);
  a.notEqual(mm(r),Math.max(...vals),q.id);a.notEqual(mm(r),Math.min(...vals),q.id);
  if(q.traningsniva===1)a.ok(lov>=4&&lov<=7,q.id);else a.ok(lov>=8&&lov<=14,q.id);
  a.match(q.s,/-noderna [A-Z, ]+: värdet = (max|min)\(barnens värden\)/,q.id); // regeln står i rubriken
 }
});

test('Nivå 3–4: vilka löv beskärs med alfa–beta',()=>{
 for(const q of NYA.filter(q=>q.traningsniva===3||q.traningsniva===4)){
  const r=träd(q),{v,beskurna,cut}=alfabeta(r);
  a.equal(q.spelDelar[0].rättSvar,beskurna.join(', '),q.id);a.equal(q.spelDelar[0].svarFormat,'namnmangd');
  a.equal(v,mm(r),q.id);
  if(q.traningsniva===3)a.equal(Object.keys(cut).length,1,q.id+': en beskärning');
  else{a.ok(Object.keys(cut).length>=2,q.id);a.ok(beskurna.length>=3,q.id);}
  a.match(q.spelDelar[0].kgInstruktion,/beteckningarna på löven/);
 }
});

test('Nivå 5: α och β i noden när sökningen går in i den eller när den beskär',()=>{
 let inn=0,besk=0;
 for(const q of NYA.filter(q=>q.traningsniva===5)){
  const r=träd(q),{in_,cut}=alfabeta(r),f=q.spelDelar[0].fraga;
  let m=f.match(/(?:går in i|kommer fram till) noden ([A-Z])/),varden;
  if(m){varden=in_[m[1]];inn++;}else{m=f.match(/(?:I noden|under noden) ([A-Z])/);a.ok(m,q.id);varden=cut[m[1]];besk++;}
  a.ok(varden,q.id);a.ok(varden.every(Number.isFinite),q.id);
  a.deepEqual([...q.spelDelar[0].rättSvar],varden,q.id);
  a.deepEqual([...q.spelDelar[0].svarEtiketter],['α','β']);
 }
 a.ok(inn>=10&&besk>=10);
});

test('Placering i omgrupperingen och nivåskriptet',()=>{
 const omg=fs.readFileSync(path.join(__dirname,'bygg-ai-omgruppering-2026-11-11.py'),'utf8');
 a.match(omg,/range\(81, 141\), \*range\(216, 232\)/);a.match(omg,/range\(141, 216\), \*range\(232, 256\)/);
 const niv=fs.readFileSync(path.join(__dirname,'bygg-ai-nivaer-2026-11-11.py'),'utf8');
 a.match(niv,/81 <= int\(u\['id'\]\.split\('\.'\)\[1\]\) <= 255/);
 // banken ligger i kapitel- och nummerordning
 const ord=B.map(q=>[q.kap,nr(q)]);for(let i=1;i<ord.length;i++)a.ok(ord[i-1][0]<ord[i][0]||(ord[i-1][0]===ord[i][0]&&ord[i-1][1]<ord[i][1]),B[i].id);
});

test('Tillämpningar: vem som är MAX och MIN, vad talen betyder och tolkning i facit',()=>{
 const synlig=h=>h.replace(/<svg[\s\S]*?<\/svg>/g,'').replace(/<[^>]+>/g,' ');
 const sammanhang=new Set();
 for(const q of TILL){
  const t=synlig(q.t);
  a.match(t,/ är MAX och .* är MIN\. Först väljer .*\. Talen i löven är /,q.id);
  sammanhang.add(t.split('.')[0]);
  a.doesNotMatch(t,/Först väljer (vinden|börsen)/,q.id);
  if(q.traningsniva<=2)a.match(q.s,/Vad värdet betyder/,q.id);
  // sammanhang där negativa tal saknar mening har bara positiva löv
  if(/slutpriset|hur säkert lagret|minuter drönaren|paket lagerroboten/.test(t)){const r=träd(q);const v=[];const pl=n=>'löv' in n?v.push(n.löv):n.barn.forEach(pl);pl(r);a.ok(Math.min(...v)>0,q.id);}
 }
 a.ok(sammanhang.size>=10,'minst tio olika tillämpningar');
});
