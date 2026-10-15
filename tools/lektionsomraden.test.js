'use strict';
const {test}=require('node:test'),assert=require('node:assert/strict');
const fs=require('node:fs'),vm=require('node:vm'),path=require('node:path');
const root=path.join(__dirname,'..'),html=fs.readFileSync(path.join(root,'index.html'),'utf8');
for(const track of ['2a','2b','2c'])test('Områdesträdet behåller lektionsordning och döljer historiska grupper i '+track,()=>{
 const tree={innerHTML:''},c=vm.createContext({window:{},document:{querySelectorAll:()=>[]},Set,state:{omr:new Set()},$:()=>tree,$$:()=>[],aktivtSpår:()=>track});
 vm.runInContext(fs.readFileSync(path.join(root,'strukturma2.js'),'utf8'),c);
 c.DB={omr:c.window.OMRMA2,grupp:c.window.GRUPPMA2};
 c.områdeSynligtFörSpår=(k,o)=>c.window.SPARMA2[k][o].includes(track);
 const bank=Object.entries(c.DB.omr).flatMap(([kap,areas])=>Object.keys(areas).filter(o=>c.områdeSynligtFörSpår(kap,o)).map(omr=>({kap,omr})));
 c.variantBank=()=>bank;c.kapitelNamn=k=>c.window.KAPNAMNMA2[k];
 const start=html.indexOf('function byggTräd(){');
 vm.runInContext(html.slice(start,html.indexOf('\n}',start)+2),c);c.byggTräd();
 const keys=[...tree.innerHTML.matchAll(/data-omr="([^"]+)"/g)].map(m=>m[1]);
 assert.deepEqual(keys.slice().sort(),bank.map(t=>t.kap+':'+t.omr).sort());
 assert.ok(keys.indexOf('1:rata_linjens_ekvation')<keys.indexOf('1:konjugatregeln'));
 assert.ok(keys.indexOf('1:konjugatregeln')<keys.indexOf('1:faktorisering'));
 assert.ok(!tree.innerHTML.includes('data-grupp="1:ekvationssystem"'));
 // ST03: i 2c ingår konjugat- och kvadreringsreglerna i Uttryck med parenteser.
 assert.ok(tree.innerHTML.includes(track==='2c'?'Uttryck med parenteser':'Konjugatregeln och kvadreringsreglerna'));
 assert.equal(tree.innerHTML.includes('data-grupp="1:losa_ekvationssystem"'),track==='2c');
 assert.equal(tree.innerHTML.includes('data-grupp="3:cirkelgeometri"'),track==='2b');
});
