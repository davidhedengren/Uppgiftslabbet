'use strict';
// Nivåindelning i AI-banken enligt agent/AI_NIVAINDELNING.md (användarbeslut 2026-11-11).
const {test}=require('node:test'),a=require('node:assert/strict'),fs=require('node:fs'),vm=require('node:vm');
const c={window:{}};vm.runInNewContext(fs.readFileSync('uppgifterai.js','utf8'),c);
const bank=c.window.BANKAI,q=id=>bank.find(u=>u.id===id),del=k=>q(k.slice(0,-1)).spelDelar.find(d=>d.etikett===k.slice(-1));
const parts=bank.flatMap(u=>u.spelDelar.map(d=>({u,d})));
test('E/C/A och träningsnivå hänger ihop',()=>{
 for(const{u,d}of parts){const k=u.id+d.etikett;
  if(d.niva==='E')a.ok(d.traningsniva<=2,k);if(d.niva==='C')a.equal(d.traningsniva,3,k);if(d.niva==='A')a.ok(d.traningsniva>=4,k);
  a.equal(d.poang,{E:'1/0/0',C:'0/1/0',A:'0/0/1'}[d.niva],k);}
 for(const u of bank){const r={E:0,C:1,A:2},top=u.spelDelar.reduce((m,d)=>r[d.niva]>r[m]?d.niva:m,'E');a.equal(u.niva,top,u.id);
  a.equal(u.traningsniva,Math.max(...u.spelDelar.map(d=>d.traningsniva)),u.id);
  a.equal(u.poang,[0,1,2].map(i=>u.spelDelar.reduce((s,d)=>s+ +d.poang.split('/')[i],0)).join('/'),u.id);}
});
test('alfa–beta-beskärning är A-nivå, rot- och nodvärden är vanlig minimax',()=>{
 for(const{u,d}of parts.filter(x=>x.u.omr==='alfa_beta')){const value=/Vilket värde får (roten|[A-Z])\?|Bestäm rotens minimaxvärde/.test(d.fraga);
  const stod=['3.56','3.57','3.58','3.59','3.60','3.61','3.66','3.67','3.68','3.69'].includes(u.id)||['3.70c','3.71c','3.72c'].includes(u.id+d.etikett);/* begreppsfrågor är E (2026-11-12) *//* beskärning med stöd: E–C (3.66–3.69 mängdträning 2026-11-12) */
  if(value||stod)a.notEqual(d.niva,'A',u.id+d.etikett);else a.equal(d.niva,'A',u.id+d.etikett);}
 for(const{u,d}of parts.filter(x=>x.u.omr!=='alfa_beta'))a.doesNotMatch(d.fraga,/beskär|α|β/,u.id+d.etikett);
});
test('många E-uppgifter',()=>{
 const n=k=>parts.filter(x=>x.d.niva===k).length;a.ok(n('E')/parts.length>=0.55,'minst 55 % E');a.ok(n('A')>0&&n('C')>0);
 // ko_sokning ingår sedan omgrupperingen 2026-11-11 i bfs och dfs.
 for(const omr of ['ko_stack','prioritetsko','bfs','dfs','minimax'])a.ok(parts.filter(x=>x.u.omr===omr&&x.d.niva==='E').length/parts.filter(x=>x.u.omr===omr).length>=0.7,omr);
});
test('f och g: E när g följer en rak väg, C när g går runt väggar eller genom terräng',()=>{
 for(const k of ['2.01a','2.01b','2.06a','2.07a','2.15a','2.38a','2.38c','2.40a'])a.equal(del(k).niva,'E',k);
 for(const k of ['2.01c','2.08a','2.16b','2.25a','2.25b','2.39a','2.39c','2.32a'])a.equal(del(k).niva,'C',k);
 for(const k of ['2.16c','3.07c'])a.equal(del(k).niva,'A',k);
});
test('sju nya E-uppgifter (2.47–2.53) i Kunskapsgymmets format med kontrollerade svar',()=>{
 const want={'2.47':['B3',3],'2.48':['A2',2],'2.49':[5,2],'2.50':[4,11],'2.51':[3,2,5],'2.52':[7,'S → A → M',6],'2.53':[2,9]};
 for(const[id,w]of Object.entries(want)){const u=q(id);a.ok(u,id);a.equal(JSON.stringify(u.rättSvar),JSON.stringify(w),id);a.equal(u.spel,true);a.equal(u.svarstyp,'flera_delar');
  a.equal(u.niva,'E',id);for(const d of u.spelDelar){a.equal(d.niva,'E');a.ok(d.traningsniva<=2);a.equal(d['självrättning'],true);}}
 const man=(x,y)=>Math.abs(x[0]-y[0])+Math.abs(x[1]-y[1]);
 a.deepEqual([[0,1],[1,2],[1,0]].map(c=>1+man(c,[2,3])),[5,3,5]);a.equal(man([0,1],[0,3]),2);a.equal(man([1,0],[0,3]),4);
 a.deepEqual([man([0,2],[3,4]),man([2,3],[3,4])],[5,2]);a.equal(7+man([0,3],[3,4]),11);a.equal(3+man([1,2],[2,3]),5);
 a.equal(Math.min(4+3,2+6,2+1+3),6);a.equal(3+3+1+1+1,9);
});
