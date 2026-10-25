'use strict';
/* Ma2 kap 3, etapp 2: randvinkelområdet (lärarbeslut 2026-10-25).
   33 kort har skalenliga figurer i varierade lägen, och vinkelbågarna mäts här ur SVG-koordinaterna.
   Varje båge börjar och slutar på ritade vinkelben. Texterna är varierade, och facit har en rubrik per steg. */
const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('node:fs'),vm=require('node:vm'),path=require('node:path');
const c={window:{}};vm.runInNewContext(fs.readFileSync(path.join(__dirname,'..','uppgifterma2.js'),'utf8'),c);
const B=JSON.parse(JSON.stringify(c.window.BANKMA2)),get=id=>{const t=B.find(x=>x.id===id);assert.ok(t,id);return t;};
const SERIE=Array.from({length:20},(_,i)=>`3.${363+i}`);
const OVRIGA=['3.03','3.42','3.132','3.17','3.47','3.157','3.293','3.331','3.361','3.2029','3.2134','3.2137','3.2139'];
const svg=q=>(q.t+(q.spelIntro||'')).match(/<svg[\s\S]*?<\/svg>/)[0];
const bagar=s=>[...s.matchAll(/<path d="M ([\d.-]+) ([\d.-]+) A ([\d.]+) [\d.]+ 0 0 [01] ([\d.-]+) ([\d.-]+)"/g)].map(m=>{const[sx,sy,r,ex,ey]=[m[1],m[2],m[3],m[4],m[5]].map(Number);return{sx,sy,ex,ey,v:2*Math.asin(Math.min(1,Math.hypot(ex-sx,ey-sy)/(2*r)))*180/Math.PI};});
const strackor=s=>[...s.matchAll(/<line x1="([\d.-]+)" y1="([\d.-]+)" x2="([\d.-]+)" y2="([\d.-]+)"/g)].map(m=>[1,2,3,4].map(i=>+m[i]));
const avst=(x,y,[x1,y1,x2,y2])=>{const dx=x2-x1,dy=y2-y1;let t=((x-x1)*dx+(y-y1)*dy)/(dx*dx+dy*dy);t=Math.max(0,Math.min(1,t));return Math.hypot(x-x1-t*dx,y-y1-t*dy);};
const FORV={'3.363':[34,34,68],'3.364':[41,41,41],'3.365':[116,58,58],'3.366':[27,27,54],'3.367':[52,52,52],'3.368':[74,37,37],'3.369':[38,38,76],'3.370':[46,46,46],
  '3.371':[130,65,65],'3.372':[32,32,64],'3.373':[43,31,43,86],'3.374':[96,35,48,48],'3.375':[36,36,72],'3.376':[70,35],'3.377':[40,40,80],'3.378':[29,47,29,58],
  '3.379':[35,48,35,48],'3.380':[31,31,62],'3.381':[42,42,42,42],'3.382':[37,37,37,74],'3.03':[116],'3.42':[62],'3.132':[128],'3.17':[80,40],'3.47':[28,56],
  '3.157':[124,62],'3.293':[100,50],'3.331':[154,77],'3.361':[90,90,90],'3.2029':[130,65],'3.2134':[110,35],'3.2137':[48,96],'3.2139':[146,73]};

test('Vinkelbågarna har rätt storlek och sitter på vinkelbenen',()=>{
  for(const[id,v]of Object.entries(FORV)){const s=svg(get(id)),b=bagar(s),L=strackor(s);
    assert.equal(b.length,v.length,id);b.forEach((x,i)=>assert.ok(Math.abs(x.v-v[i])<1,`${id}: båge ${i} är ${x.v.toFixed(1)}°, inte ${v[i]}°`));
    for(const x of b){assert.ok(Math.min(...L.map(l=>avst(x.sx,x.sy,l)))<1.5,id);assert.ok(Math.min(...L.map(l=>avst(x.ex,x.ey,l)))<1.5,id);}
    assert.doesNotMatch(s,/Mät inte i figuren/,id);}
});
test('Svaren och de nya svaren',()=>{
  const svar={'3.363':[34,68],'3.364':[41,41],'3.375':[36,32],'3.376':15,'3.377':[12,80],'3.379':[35,48],'3.382':[37,37,74],'3.03':[58,32],'3.42':[124,62],'3.132':[64,26],'3.331':77,'3.361':90,'3.2029':65,'3.2139':73};
  for(const[id,v]of Object.entries(svar))assert.deepEqual(get(id).rättSvar,v,id);
  assert.equal(get('3.42').niva,'E');assert.equal(get('3.42').poang,'2/0/0');
  // Delkorten i 3.42 är oberoende: b-facit visar inte medelpunktsvinkeln från a.
  assert.doesNotMatch(get('3.42').spelDelar[1].s,/124/);
});
test('Varierade figurer och texter',()=>{
  const ids=[...SERIE,...OVRIGA],figurer=new Set(),borjan=new Set();
  for(const id of ids){const q=get(id),f=svg(q).replace(/aria-label="[^"]*"/,'');assert.ok(!figurer.has(f),`${id}: samma figur som ett annat kort`);figurer.add(f);
    const b=q.t.replace(/<[^>]+>/g,'').slice(0,45);assert.ok(!borjan.has(b),`${id}: samma textinledning`);borjan.add(b);}
  assert.equal(SERIE.filter(id=>/^<p>Bestäm vinklarna \\(x\\) och \\(y\\)\.<\/p>/.test(get(id).t)).length,0);
});
test('Facit har en rubrik per steg, och delkorten har egna ledtrådar',()=>{
  for(const id of [...SERIE,...OVRIGA]){const q=get(id);
    for(const s of [q.s,...(q.spelDelar||[]).map(d=>d.s)]){const li=(s.match(/<li>/g)||[]).length,r=(s.match(/facit-rubrik/g)||[]).length;assert.ok(li>0&&r>=li,`${id}: ${li} steg, ${r} rubriker`);assert.match(s,/facit-svar/,id);}
    for(const d of q.spelDelar||[])assert.ok((d.ledtrad||'').length>10,`${id}${d.etikett}: ledtråd`);}
});
