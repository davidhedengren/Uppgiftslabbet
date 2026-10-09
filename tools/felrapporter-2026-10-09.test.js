'use strict';
const test=require('node:test'),assert=require('node:assert/strict'),fs=require('node:fs'),vm=require('node:vm'),path=require('node:path');
const c={window:{}};
for(const file of ['uppgifterma1.js','uppgifterma2.js','uppgifter2.js'])vm.runInNewContext(fs.readFileSync(path.join(__dirname,'..',file),'utf8'),c);
const q=(bank,id)=>c.window[bank].find(q=>q.id===id);
test('0.1047 jämför positioner i decimaltal och ligger på nivå 2',()=>{
 const t=q('BANKMA1','0.1047');assert.equal(t.rättSvar,[.7,.07,.707,.77].sort((a,b)=>b-a)[1]);assert.equal(t.traningsniva,2);
});
test('4.514 ger en ordnad vektor med båda komponenterna multiplicerade',()=>{
 const t=q('BANKMA1','4.514');assert.deepEqual(Array.from(t.rättSvar),[-2,-4].map(x=>-3*x));assert.equal(t.svarsstruktur,'ordnad');assert.match(t.t,/pmatrix/);assert.doesNotMatch(t.s,/facit-steglista/);
});
test('1.84 följer både den lodräta kraftbalansen och cirkelrörelsen',()=>{
 const t=q('BANK2','1.84'),v=24,r=80,g=9.82,theta=Math.atan(v*v/(r*g));
 assert.ok(Math.abs(t.rättSvar-theta*180/Math.PI)<1e-10);
 for(const mass of [500,1200,1800]){
  const normal=mass*g/Math.cos(theta);
  assert.ok(Math.abs(normal*Math.sin(theta)-mass*v*v/r)<1e-9);
 }
 assert.equal(Math.round(t.rättSvar*10)/10,36.2);assert.equal(t.tolerans,.06);
 assert.match(t.s,/F_N\\cos\\theta=mg/);assert.match(t.s,/F_N\\sin\\theta=\\frac\{mv\^2\}\{r\}/);assert.doesNotMatch(t.s,/facit-steglista/);
});
function lines(id){return [...q('BANKMA2',id).t.matchAll(/<line\b([^>]+)>/g)].map(m=>Object.fromEntries([...m[1].matchAll(/(x1|y1|x2|y2)="([^"]+)"/g)].map(x=>[x[1],+x[2]])));}
function point(l,end=false){return end?[l.x2,l.y2]:[l.x1,l.y1];}
function angle(a,o,b){const u=a.map((v,i)=>v-o[i]),v=b.map((x,i)=>x-o[i]);return Math.acos((u[0]*v[0]+u[1]*v[1])/(Math.hypot(...u)*Math.hypot(...v)))*180/Math.PI;}
test('De nya vinkelmarkeringarna följer figurernas faktiska geometri',()=>{
 let l=lines('3.532'),A=point(l[0]),B=point(l[0],true),C=point(l[1],true),D=point(l[3],true);
 for(const [actual,want] of [[angle(B,A,C),40],[angle(A,B,C),60],[angle(B,A,D),20],[angle(D,A,C),20]])assert.ok(Math.abs(actual-want)<.01);
 l=lines('3.535');A=point(l[0]);B=point(l[0],true);C=point(l[1],true);D=point(l[3],true);
 assert.ok(Math.abs(angle(B,A,D)-angle(D,A,C))<.01);
 l=lines('3.537');A=point(l[0]);B=point(l[0],true);C=point(l[1],true);const O=point(l[3]);
 assert.ok(Math.abs(angle(A,C,B)-35)<.01);assert.ok(Math.abs(angle(A,O,B)-70)<.01);
});
