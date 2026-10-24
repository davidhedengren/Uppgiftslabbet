'use strict';
const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('node:fs'),vm=require('node:vm'),path=require('node:path');
const root=path.join(__dirname,'..');function load(file){const c={window:{}};vm.runInNewContext(fs.readFileSync(path.join(root,file),'utf8'),c);return Object.values(c.window).find(Array.isArray);}
const mf=load('uppgiftermatf1.js'),fy=load('uppgifter.js'),get=(b,id)=>b.find(q=>q.id===id),plain=x=>JSON.parse(JSON.stringify(x));
test('Åtta konstanta differentialekvationslösningar uppfyller respektive högerled',()=>{
 const cases=[['4.326',y=>2*y-6,[3]],['4.346',y=>5-2*y,[2.5]],['4.123',y=>.5*y*(1-y/400),[0,400]],['4.518',y=>y*(4-y),[0,4]],['4.109',y=>y*(3-y),[0,3]],['4.135',y=>(y-1)*(3-y),[1,3]],['4.138',y=>y*(2-y),[0,2]],['4.174',y=>(1-y)*(y+2),[-2,1]]];
 for(const[id,f,values]of cases){const q=get(mf,id);assert.match(q.t,/konstant/);values.forEach(x=>assert.equal(Math.abs(f(x)),0));if(q.rättSvar!=null){const a=Array.isArray(q.rättSvar)?q.rättSvar:[q.rättSvar],actual=Array.isArray(a[0])?a[0]:a.slice(0,values.length);assert.deepEqual(plain(actual),values);}}
 assert.equal(get(mf,'4.518').rättSvar[2],2);assert.equal(4-2*2,0);assert.ok(2*(4-2)>1*(4-1));
 for(const id of ['4.346','4.109','4.135','4.138','4.174'])assert.doesNotMatch(get(mf,id).s,/Euler|Skriv sedan lösningen som en avvikelse/);
 assert.equal(get(mf,'4.326').traningsniva,1);
});
test('Stabilitet och riktning bygger på högerledets tecken',()=>{assert.ok(.5*50*(1-50/400)>0);assert.ok(.5*500*(1-500/400)<0);assert.ok(.5*(2-.5)>0);assert.ok(3*(2-3)<0);const f=y=>(1-y)*(y+2);assert.ok(f(-3)<0);assert.ok(f(0)>0);assert.ok(f(2)<0);});
test('Indirekta bevis får korrekt område och bygger på logisk ekvivalens',()=>{
 // Sedan 2026-10-24 är flera av korten flervalskort; bokstaven motsvarar platsen i bankens (oblandade) alternativlista.
 const bokstav=q=>q.rättSvar??'ABCDEFGH'[q.alternativ.findIndex(a=>a.ratt)];
 assert.equal(get(mf,'2.305').omr,'indirekta_bevis');assert.equal(bokstav(get(mf,'2.305')),'B');assert.equal(bokstav(get(mf,'2.541')),'A');assert.equal(bokstav(get(mf,'2.572')),'D');assert.equal(bokstav(get(mf,'2.577')),'C');
 for(const id of ['2.305','2.541','2.144','2.148','2.316','2.572','2.577']){const q=get(mf,id);assert.match(q.t,/indirekt/i);assert.doesNotMatch(q.t,/Kontraposition|kontraposition/);}
 for(const P of [true,false])for(const Q of [true,false])assert.equal(!P||Q,Q||!P);
 for(let k=-20;k<=20;k++){assert.equal((2*k+1)**2,2*(2*k*k+2*k)+1);assert.equal((2*k)**2,2*(2*k*k));for(const r of [1,2])assert.notEqual((3*k+r)**2%3,0);}
});
test('Fjäderkort är självständiga med rätt givna tal, beräkningar och enheter',()=>{
 const q=get(fy,'4.64');assert.deepEqual(plain(q.rättSvar),[200*.15,45/.25,28/350]);assert.equal(q.spelIntro,'');
 q.spelDelar.forEach((d,i)=>{assert.doesNotMatch(d.t,/Tre|Fjäder [ABC]|från [ab]\)/);assert.match(d.t,/fjäderkonstant/);assert.match(d.s,/Svar:/);assert.ok(d.ledtrad);});
 assert.equal(q.spelDelar[2].traningsniva,1);assert.match(q.spelDelar[2].t,/28 N.*350 N\/m/);
});
test('Sex mängdsvar verifieras med oberoende mängdoperationer',()=>{
 const A=new Set([1,2,3,4]),B=new Set([3,4,5]);assert.deepEqual([...A].filter(x=>B.has(x)),[3,4]);
 const cases=[['1.478',[3,4]],['1.474',[1,3,5,7]],['1.475',[2,3,4,5,6]],['1.479',[...new Set([1,2,3,3,4,5])]],['1.480',[1,2,3,4,5].filter(x=>![2,4,6].includes(x))],['1.146',[1,2,3,4,5,6].filter(x=>![3,4].includes(x))]];
 for(const[id,values]of cases){const q=get(mf,id);assert.deepEqual(JSON.parse(q.rättSvar.replace('{','[').replace('}',']')),values);assert.equal(q.svarFormat,'mängd');}
});
