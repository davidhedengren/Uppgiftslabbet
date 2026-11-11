'use strict';
// AI-banken 2026-11-11: de 95 manuella uppgifterna är självrättande i Kunskapsgymmet
// (tools/bygg-ai-sjalvrattning-2026-11-11.py). Uppgiftslabbet visar bara t och s, som inte
// får innehålla något som är anpassat för automaträttning.
const {test}=require('node:test'),a=require('node:assert/strict'),fs=require('node:fs'),vm=require('node:vm');
const c={window:{}};vm.runInNewContext(fs.readFileSync('uppgifterai.js','utf8'),c);
const bank=c.window.BANKAI,q=id=>bank.find(u=>u.id===id),del=k=>q(k.slice(0,-1)).spelDelar.find(d=>d.etikett===k.slice(-1));
const GAMLA=bank.filter(u=>/^(1\.(0\d|1\d|2\d|3[01])|2\.(0\d|1\d|2\d|3[0-4])|3\.(0\d|1\d|2\d|30))$/.test(u.id)).map(u=>u.id);
const KG_FLERVAL=['1.07d','2.03c','3.07c'];
const strip=h=>String(h).replace(/<svg[\s\S]*?<\/svg>/g,' ').replace(/<[^>]+>/g,' ').replace(/\s+/g,' ').trim();
// Samma tolkning som Kunskapsgymmets namnordning/namnmangd: namn (A1, S, L12) och tal, inte ord.
const element=x=>(String(x).replace(/[−–]/g,'-').toUpperCase().match(/-?\d+|[A-ZÅÄÖ]+\d*/g)||[]).filter(v=>!/^[A-ZÅÄÖ]{2,}\d*$/.test(v));
const svarsrad=d=>strip((d.s.match(/class="facit-svar"[^>]*>([\s\S]*?)<\/(?:p|div)>/)||[])[1]||'');
const delsekvens=(xs,ys)=>{let j=0;for(const y of ys)if(j<xs.length&&y===xs[j])j++;return j===xs.length;};

test('alla uppgifter är självrättande och metadata stämmer mellan uppgift och delkort',()=>{
 a.ok(bank.length>=202);a.equal(GAMLA.length,95);
 for(const u of bank){
  a.equal(u.spel,true,u.id);a.equal(u['självrättning'],true,u.id);a.equal(u.svarstyp,'flera_delar',u.id);
  a.equal(u.svarsstruktur,'ordnad');a.equal(u.visaSomDelkort===true,u.spelDelar.length===1,u.id);a.equal(JSON.stringify(u.svarEtiketter),JSON.stringify(u.spelDelar.map(d=>d.etikett)));
  u.spelDelar.forEach((d,i)=>{
   a.equal(d.spel,true,u.id+d.etikett);a.equal(d['självrättning'],true);
   a.equal(JSON.stringify(u.rättSvar[i]),JSON.stringify(d.rättSvar),u.id+d.etikett);
   a.equal(JSON.stringify(u.tolerans[i]),JSON.stringify(d.tolerans));a.equal(JSON.stringify(u.svarFormat[i]),JSON.stringify(d.svarFormat ?? null));
   if(d.svarstyp==='alternativ'){
    const ratt=d.alternativ.filter(x=>x.ratt).map(x=>x.txt);a.ok(ratt.length>=1);
    a.equal(JSON.stringify(d.rättSvar),JSON.stringify(ratt.length===1?ratt[0]:ratt),u.id+d.etikett);
    a.equal(ratt.length>1,/Välj alla som stämmer/.test(d.fraga),u.id+d.etikett);
    for(const x of d.alternativ)a.ok(x.kommentar.length>15,u.id+d.etikett+' '+x.txt);
   }else if(d.svarstyp==='flera_delar'){
    a.equal(d.rättSvar.length,d.svarEtiketter.length);a.equal(d.svarsstruktur,'ordnad');
    d.rättSvar.forEach((v,j)=>{if(d.svarFormat[j]==='numeriskt'){a.ok(Number.isInteger(v));a.equal(d.tolerans[j],0);}else a.match(d.svarFormat[j],/^namn(ordning|mangd)$/);});
   }else if(d.svarstyp==='numeriskt'){a.ok(Number.isInteger(d.rättSvar));a.equal(d.tolerans,0);}
   else{a.equal(d.svarstyp,'kort_text');a.match(d.svarFormat,/^namn(ordning|mangd)$/);a.equal(typeof d.rättSvar,'string');}
  });
 }
});

test('Uppgiftslabbets text och facit är orörda: inga svarsinstruktioner eller Kunskapsgymmet-alternativ i t och s',()=>{
 const instr=/\((?:Skriv|Svara|Ange noden|Ta beskärningarna)[^)]*\)/;
 for(const id of GAMLA){const u=q(id);
  a.doesNotMatch(u.t,instr,id);a.doesNotMatch(u.s,instr,id);a.doesNotMatch(u.spelIntro,instr,id);
  for(const d of u.spelDelar){
   const fraga=d.fraga.replace(/ \([^)]*\)(?=<\/p>)/,'').replace(KG_FLERVAL.includes(id+d.etikett)?' Välj ett alternativ.':'\u0000','');
   a.ok(strip(u.t).includes(strip(fraga).replace(/ Fyll i[\s\S]*$/,'').slice(0,40)),id+d.etikett);
  }}
 for(const k of KG_FLERVAL){const d=del(k),u=q(k.slice(0,-1));
  a.equal(d.svarstyp,'alternativ');for(const x of d.alternativ)a.ok(!u.t.includes(x.txt),k+': alternativen visas inte i Uppgiftslabbet');}
});

test('varje svar stämmer med delkortets facit',()=>{
 const undantag={'1.22c':'sjätte','1.04b':'tom'};
 for(const id of GAMLA)for(const d of q(id).spelDelar){const k=id+d.etikett,rad=svarsrad(d);a.ok(rad,k);
  if(undantag[k]){a.match(rad,new RegExp(undantag[k]),k);continue;}
  if(d.svarstyp==='alternativ'){if(KG_FLERVAL.includes(k))continue;
   const nrm=x=>x.toLowerCase().replace(/[^a-zåäö0-9≥≤]/g,''),ratt=[].concat(d.rättSvar);a.ok(ratt.every(t=>nrm(rad).includes(nrm(t))||rad.includes(String.fromCharCode(65+d.alternativ.findIndex(x=>x.txt===t)))),k+': '+rad);continue;}
  const svar=[].concat(d.rättSvar).flatMap(v=>element(String(v).split('|')[0]));
  a.ok(svar.length>0,k);a.ok(delsekvens(svar,element(rad)),`${k}: ${svar} ⊄ ${rad}`);
 }
});

test('köer, stackar och prioritetsköer räknas om oberoende',()=>{
 const kör=(ops,typ)=>{let s=[];const ut=[];for(const o of ops){if(o==='ut'){let i=0;if(typ==='stack')i=s.length-1;if(typ==='prio')i=s.reduce((b,x,j)=>x[1]<s[b][1]||(x[1]===s[b][1]&&x[0]<s[b][0])?j:b,0);ut.push(s.splice(i,1)[0]);}else s.push(o);}return{ut,kvar:s};};
 const N=xs=>xs.map(x=>Array.isArray(x)?x[0]:x).join(', ');
 const ops103=['A','B','C','ut','D','ut','ut','E','ut','ut'];
 a.equal(N(kör(ops103,'fifo').ut),del('1.03a').rättSvar);a.equal(N(kör(ops103,'stack').ut),del('1.03b').rättSvar);
 const p=(n,v)=>[n,v];
 const r204=kör([p('A',5),p('B',3),p('C',7),'ut',p('D',2),p('E',6),'ut','ut',p('F',1),'ut','ut','ut'],'prio');
 a.equal(N(r204.ut),del('2.04a').rättSvar);
 const r204b=kör([p('A',5),p('B',3),p('C',7),'ut',p('D',2),p('E',6),'ut','ut'],'prio');a.deepEqual(N(r204b.kvar).split(', ').sort(),del('2.04b').rättSvar.split(', ').sort());
 a.equal(N(kör([p('M',4),p('L',2),p('K',4),'ut',p('N',1),'ut','ut','ut'],'prio').ut),del('2.12a').rättSvar);
 const r231=kör([p('A',4),p('B',2),p('C',6),'ut',p('D',1),p('E',3),'ut','ut'],'prio');
 a.equal(N(r231.ut),del('2.31a').rättSvar);a.deepEqual(N(r231.kvar).split(', ').sort(),del('2.31b').rättSvar.split(', ').sort());
 // 2.23: lika värde avgörs av vem som lades in först (inte alfabetet)
 const fifoPrio=ops=>{const s=[],ut=[];for(const o of ops){if(o==='ut'){let i=0;s.forEach((x,j)=>{if(x[1]<s[i][1])i=j;});ut.push(s.splice(i,1)[0][0]);}else s.push(o);}return ut;};
 a.equal(fifoPrio([p('P',3),p('Q',5),p('M',3),'ut',p('S',1),p('K',3),'ut','ut','ut']).join(', '),del('2.23a').rättSvar);
 const r112=kör(['A','B','ut','C','D','ut','ut','ut'],'stack');a.equal(N(r112.ut),'B, D, C, A');
 a.equal(N(kör(['A','B','ut','C','D','ut','ut','ut'],'fifo').ut),del('1.12b').rättSvar);
 const r128=kör(['A','B','ut','C','D','E','ut','ut','F'],'stack');a.equal(N(r128.ut),del('1.28b').rättSvar);a.equal(N(r128.kvar),del('1.28a').rättSvar);
 const ops121=['P','Q','ut','R','S','ut','T'];
 a.equal(JSON.stringify([N(kör(ops121,'fifo').kvar),N(kör(ops121,'stack').kvar)]),JSON.stringify(del('1.21a').rättSvar));
 a.equal(JSON.stringify([N(kör(ops121,'fifo').ut),N(kör(ops121,'stack').ut)]),JSON.stringify(del('1.21b').rättSvar));
});

test('de nya flervalsfrågorna: rätt alternativ räknas om',()=>{
 // 3.07c: A = min(4, 6), B = min(x, 7). B > A för heltal x ⇔ x ≥ 5.
 const ok=x=>Math.min(x,7)>Math.min(4,6);
 const ratt=del('3.07c').alternativ.filter(x=>x.ratt).map(x=>x.txt);a.equal(ratt.join('|'),'x ≥ 5');
 for(let x=-10;x<=20;x++)a.equal(ok(x),x>=5);
 for(const alt of del('3.07c').alternativ){const m=alt.txt.match(/x ([≥≤]) (\d+)/),n=+m[2];
  const sant=[...Array(31).keys()].map(i=>i-10).every(x=>(m[1]==='≥'?x>=n:x<=n)===ok(x));a.equal(sant,alt.ratt,alt.txt);}
 // 1.07d: DFS-vägen har 13 steg (delkort c), BFS-vägen enligt facit 9 steg.
 a.equal(del('1.07c').alternativ.find(x=>x.ratt).txt,'13');a.match(svarsrad(del('1.07d')),/9 steg/);
 a.ok(del('1.07d').alternativ.find(x=>x.ratt).txt.includes('9 steg'));
 // 2.03: girig bäst först kostar 11, A* 7 (delkort a och b).
 a.equal(del('2.03a').rättSvar[1],11);a.equal(del('2.03b').rättSvar[1],7);
});

test('validatorn hittar inget nytt i AI-banken',()=>{const r=require('./granska-uppgifter.js').granskaProjekt(process.cwd()).resultat.find(x=>x.fil==='uppgifterai.js');
 const ok=f=>(f.kod==='EXACT_TEXT_DUPLICATE'&&['3.04','3.05'].includes(f.id))||(f.kod==='VERY_SIMILAR_TEXT'&&['2.06','2.08'].includes(f.id));
 a.deepEqual(r.fynd.filter(f=>!ok(f)).map(f=>f.kod+' '+f.id),[]);});
