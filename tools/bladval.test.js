'use strict';
const {test} = require('node:test');
const assert = require('node:assert/strict');
const {dra, ersätt, familj} = require('../bladval');
const uppgift = (id, f, niva, extra={}) => ({id, kap:1, omr:'algebra', familj:f, niva, formaga:['procedur'], ...extra});
const pool = ['Parenteser','Ekvationer','Faktorisering'].flatMap(f => ['E','C','A'].flatMap(n =>
  Array.from({length:6}, (_,i)=>uppgift(f+n+i,f,n))));
const inst = (antal,profil='varierad') => ({antal,profil,längd:'alla'});
const familjer = xs => new Set(xs.map(familj));
function slumpfrö(frö) {
  return () => ((frö=(Math.imul(1664525,frö)+1013904223)>>>0)/4294967296);
}

test('Profilerna ger metodblock, spridning respektive stigande nivå i samma bank',()=>{
  const rutin=dra(pool,inst(9,'rutin')), blandat=dra(pool,inst(9)), stege=dra(pool,inst(9,'stegring'));
  assert.equal(familjer(rutin).size,1);assert.equal(familjer(blandat).size,3);
  assert.deepEqual(stege.map(t=>t.niva),['E','E','E','C','C','C','A','A','A']);
  for(const xs of [rutin,blandat,stege]) assert.equal(new Set(xs.map(t=>t.id)).size,9);
});
test('Ett nytt blad, en låst uppgift och byte av en uppgift',()=>{
  const val=inst(8), första=dra(pool,val);
  första[3]={...första[3],t:'Egen text',_bladLåst:true};
  const historia=new Map(första.map(t=>[t.id,1]));
  const nästa=dra(pool,val,första,historia);
  assert.equal(nästa[3],första[3]); assert.equal(nästa.filter(t=>historia.has(t.id)).length,1);
  const byte=ersätt(pool,nästa,1,historia,'alla');
  assert.equal(familj(byte),familj(nästa[1]));assert.equal(byte.niva,nästa[1].niva);
  assert.ok(!nästa.includes(byte));
  assert.throws(()=>dra(pool,inst(2),första),/låst/);
  assert.throws(()=>ersätt(nästa,nästa,1,historia,'alla'),/ingen ytterligare/);
});
test('En knapp nivå går till delmomentet som verkligen måste ha den',()=>{
  const a=uppgift('ae','En','E'), b=uppgift('ac','En','C'), c=uppgift('be','Två','E');
  const val={...inst(2),familjer:new Map([[familj(a),1],[familj(c),1]]),nivåantal:[1,1,0]};
  const ut=dra([a,b,c],val);
  assert.deepEqual(new Set(ut.map(x=>x.id)),new Set(['ac','be']));
  assert.throws(()=>dra([a,c],val),/kombinera/);
  assert.throws(()=>dra([a,b,c],{...val,nivåantal:[1,0,0]}),/tillsammans/);
});
test('Fri fördelning, exakta delmoment och arbetsmängd',()=>{
  const k1=familj(pool[0]),k2=familj(pool[20]);
  const val={...inst(8,'rutin'),familjer:new Map([[k1,3],[k2,null]]),nivåantal:[6,1,1]};
  const ut=dra(pool,val);assert.equal(ut.filter(x=>familj(x)===k1).length,3);
  assert.equal(ut.filter(x=>familj(x)===k2).length,5);assert.equal(ut.filter(x=>x.niva==='E').length,6);
  const längre=pool.map(x=>({...x,id:x.id+'fler',spelDelar:[{},{}]}));
  assert.ok(dra([...pool,...längre],{...inst(12),längd:'lång'}).every(x=>x.spelDelar));
  assert.throws(()=>dra([],inst(12)),/Inga uppgifter/);
});
test('Möjliga kombinationer av glesa delmoment och nivåer får alltid en lösning',()=>{
  const rnd=slumpfrö(123);
  for(let i=0;i<250;i++){
    const xs=pool.filter(()=>rnd()<0.12);
    const facit=xs.filter(()=>rnd()<0.6); if(!facit.length) continue;
    const krav=new Map();
    for(const x of facit) krav.set(familj(x),(krav.get(familj(x))||0)+1);
    const nivåantal=['E','C','A'].map(n=>facit.filter(t=>t.niva===n).length);
    const lista=dra(xs,{...inst(facit.length),familjer:krav,nivåantal},[],new Map(),rnd);
    assert.deepEqual(nivåantal,['E','C','A'].map(n=>lista.filter(x=>x.niva===n).length));
    for(const [k,n] of krav) assert.equal(lista.filter(x=>familj(x)===k).length,n);
  }
});

test('Svårighetsgrad utgår från träningsnivån och den svåraste delen av hela uppgiften',()=>{
  const {svårighetsgrad} = require('../bladval');
  assert.equal(svårighetsgrad(uppgift('a','Metod','E',{traningsniva:'2'})),2);
  assert.equal(svårighetsgrad(uppgift('b','Metod','C',{traningsniva:[1,3],spelDelar:[{traningsniva:4}]})),4);
  assert.equal(svårighetsgrad(uppgift('c','Metod','A',{spelDelar:[{traningsniva:5}]})),5);
  assert.equal(svårighetsgrad(uppgift('d','Metod','A',{traningsniva:[null,'',0,6,2.5]})),null);
});

test('Matematikblad tar med valda förmågor även när en äldre tagg saknar ö',()=>{
  const {matcharFörmågor} = require('../bladval');
  const val = {...inst(2), förmågor:new Set(['problemlösning','resonemang'])};
  const problem = uppgift('p','Algebra','C',{formaga:'problemlosning'});
  const argument = uppgift('a','Algebra','C',{formaga:['begrepp','resonemang']});
  const xs = [problem, argument, ...pool];
  assert.deepEqual(new Set(dra(xs,val).map(x=>x.id)),new Set(['p','a']));
  assert.equal(matcharFörmågor({},null),true);
  assert.equal(matcharFörmågor({},val.förmågor),false);
  assert.throws(()=>dra(xs,{...val,förmågor:new Set()}),/minst en förmåga/);
  assert.throws(()=>dra(xs,val,[{...pool[0],_bladLåst:true}]),/låst/);
  const andra = {...problem,id:'p2'};
  assert.equal(ersätt([...xs,andra],[argument,problem],1,new Map(),'alla',Math.random,val.förmågor).id,'p2');
  assert.throws(()=>ersätt([...xs,{...argument,id:'a2'}],[argument,problem],1,new Map(),'alla',Math.random,val.förmågor),/behåller/);
});
