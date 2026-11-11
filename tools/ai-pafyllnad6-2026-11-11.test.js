'use strict';
// AI-banken 2026-11-11, nionde omgången: minimax och beskärning med stöd på E–C-nivå.
const {test}=require('node:test'),a=require('node:assert/strict'),fs=require('node:fs'),vm=require('node:vm');
const c={window:{}};vm.runInNewContext(fs.readFileSync('uppgifterai.js','utf8'),c);
const bank=c.window.BANKAI,q=id=>bank.find(u=>u.id===id),eq=(id,w)=>a.equal(JSON.stringify(q(id).rättSvar),JSON.stringify(w),id);
const mm=(t,max)=>typeof t==='number'?t:(max?Math.max:Math.min)(...t.map(x=>mm(x,!max)));
function ab(t,max){let leaf=0;const named=t=>typeof t==='number'?{n:'L'+(++leaf),v:t}:t.map(named),tree=named(t),cut=[],seen=[];const names=t=>t.n?[t.n]:t.flatMap(names);
 function go(t,max,al,be){if(t.n){seen.push(t.n);return t.v;}let v=max?-Infinity:Infinity;for(let i=0;i<t.length;i++){const x=go(t[i],!max,al,be);if(max){v=Math.max(v,x);al=Math.max(al,v);}else{v=Math.min(v,x);be=Math.min(be,v);}if(al>=be&&i+1<t.length){cut.push(...t.slice(i+1).flatMap(names));break;}}return v;}
 return{v:go(tree,max,-Infinity,Infinity),cut,seen};}
const MM=['3.50','3.51','3.52','3.53','3.54','3.55'],AB=['3.56','3.57','3.58','3.59','3.60','3.61'];
test('format och nivåer: E–C, ingen A',()=>{
 for(const id of [...MM,...AB]){const u=q(id);a.ok(u,id);a.equal(u.spel,true);a.equal(u.svarstyp,'flera_delar');a.notEqual(u.niva,'A',id);
  for(const d of u.spelDelar){a.ok(['E','C'].includes(d.niva));for(const x of d.alternativ)a.ok(x.kommentar.length>15,id);}}
 for(const id of MM)a.equal(q(id).omr,'minimax');for(const id of AB)a.equal(q(id).omr,'alfa_beta');
 const lv=k=>q(k.slice(0,-1)).spelDelar.find(d=>d.etikett===k.slice(-1)).niva;
 for(const k of ['3.56a','3.56b','3.57c','3.59a','3.61a'])a.equal(lv(k),'E',k);for(const k of ['3.57a','3.57b','3.58b','3.59b','3.60c','3.61b','3.50c','3.54b'])a.equal(lv(k),'C',k);
 for(const id of ['3.15','3.19','3.23','3.34'])a.ok(q(id).spelDelar.some(d=>d.niva==='A'),'äldre beskärningsuppgifter är oförändrat A: '+id);
});
test('minimaxsvar',()=>{
 eq('3.50',[Math.min(-1,mm([1],true)),mm([[-1,[1]],[-1]],true),'MIN vinner om båda spelar så bra som möjligt']);
 const v51=[[2,7],[6,8],[5,1],[3,9]];eq('3.51',[v51.filter(x=>Math.min(...x)>=5).length,mm(v51,true),'Draget till B']);
 eq('3.52',[mm([[3,6],[5,7]],true),'Draget till A',mm([[8,6],[5,7]],true)]);
 eq('3.53',['MIN',3,mm([[4,1,6],[3,8],[7,2]],true)]);eq('3.54',[Math.min(4,9),'Nej, båda dragen garanterar värdet 4']);a.equal(Math.min(4,9),Math.min(4,6));
 eq('3.55',[Math.min(3,9),Math.max(Math.min(5,7),Math.min(8,4)),mm([[[6,2],[3,9]],[[5,7],[8,4]]],false)]);
});
test('beskärning med stöd: svaren stämmer med alfa–beta',()=>{
 const r57=ab([[5,8],[3,9]],true);a.deepEqual(r57.cut,['L4']);eq('3.57',['Nej, B blir högst 3','Nej, B kan ändå inte bli bättre än A för MAX',r57.v]);
 const r58=ab([[4,2],[6,1]],false);a.deepEqual(r58.cut,['L4']);eq('3.58',[6,'Nej, roten väljer A ändå',r58.v]);
 const r59=ab([[6,7],[2,8]],true);eq('3.59',[Math.min(6,7),r59.cut[0]]);
 const a60=ab([[5,6],[3,9]],true),b60=ab([[5,6],[9,3]],true);a.equal(a60.v,b60.v);eq('3.60',[2-a60.cut.length,2-b60.cut.length,'Ordningen påverkar hur mycket som kan beskäras, men inte rotens värde']);
 const r61=ab([[4,6],[1,5],[2,3]],true);eq('3.61',[Math.min(4,6),r61.seen.length]);
 for(const[t,m]of [[[[5,8],[3,9]],true],[[[4,2],[6,1]],false],[[[6,7],[2,8]],true],[[[4,6],[1,5],[2,3]],true]])a.equal(ab(t,m).v,mm(t,m));
});
test('validatorn hittar inget i omgången',()=>{const r=require('./granska-uppgifter.js').granskaProjekt(process.cwd()).resultat.find(x=>x.fil==='uppgifterai.js');
 const ids=[...MM,...AB];a.deepEqual(r.fynd.filter(f=>ids.includes(f.id)||(f.relateradeId||[]).some(i=>ids.includes(i))),[]);});
