'use strict';
/* Ma2 kap 3, etapp 5: likformighet och topptriangel (lärarbeslut 2026-10-25).
   - Topptriangelfigurerna använde förut samma likbenta eller liksidiga triangel. Nu är de skalenliga i varierade
     lägen, och DE/BC i figuren är lika med längdskalan.
   - Paren av likformiga trianglar var förut ritade i fel skala. Nu är omkretsarnas kvot lika med längdskalan.
   - Texter som var identiska (”Trianglarna är likformiga. Bestäm x.”) är varierade, och facit har rubriker. */
const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('node:fs'),vm=require('node:vm'),path=require('node:path');
const c={window:{}};vm.runInNewContext(fs.readFileSync(path.join(__dirname,'..','uppgifterma2.js'),'utf8'),c);
const B=JSON.parse(JSON.stringify(c.window.BANKMA2)),get=id=>{const t=B.find(x=>x.id===id);assert.ok(t,id);return t;};
const svg=id=>{const q=get(id);return ((q.spelIntro||'')+q.t).match(/<svg[\s\S]*?<\/svg>/)[0];};
const polys=s=>[...s.matchAll(/<polygon points="([^"]+)" fill="none"/g)].map(m=>m[1].trim().split(/\s+/).map(p=>p.split(',').map(Number)));
const omkrets=P=>P.reduce((s,p,i)=>s+Math.hypot(p[0]-P[(i+1)%P.length][0],p[1]-P[(i+1)%P.length][1]),0);
const TOPP={'3.36':0.6,'3.69':0.5,'3.98':0.4,'3.99':1/3,'3.100':0.6,'3.162':0.4,'3.164':0.4,'3.176':0.4,'3.323':0.5,'3.259':1/3,'3.359':0.4,
  '3.600':0.5,'3.601':0.5,'3.602':1/3,'3.603':0.45,'3.604':0.25,'3.605':2/3,'3.606':0.5,'3.607':0.25,'3.608':0.4,'3.609':1/3,'3.610':0.5,'3.611':0.5};
test('Topptriangel: DE/BC i figuren är lika med längdskalan',()=>{
  const former=new Set();
  for(const[id,t]of Object.entries(TOPP)){const s=svg(id),P=polys(s)[0],BC=Math.hypot(P[1][0]-P[2][0],P[1][1]-P[2][1]);
    const de=s.match(/<line x1="([\d.-]+)" y1="([\d.-]+)" x2="([\d.-]+)" y2="([\d.-]+)" stroke="#2f6fca" stroke-width="2.6"/).slice(1).map(Number);
    const kvot=Math.hypot(de[2]-de[0],de[3]-de[1])/BC;assert.ok(Math.abs(kvot-t)<0.01,`${id}: ${kvot.toFixed(3)} ≠ ${t.toFixed(3)}`);
    former.add(P.map(p=>p.map(Math.round).join(',')).join(' '));}
  assert.equal(former.size,Object.keys(TOPP).length,'två topptriangelfigurer är identiska');
});
test('Likformiga trianglar: omkretsarnas kvot är lika med längdskalan',()=>{
  for(const[id,k]of Object.entries({'3.43':2,'3.209':1.5,'3.335':2.5,'3.466':1.5,'3.467':2,'3.468':2.5,'3.469':1.5,'3.470':1.2,'3.639':3,'3.642':3})){
    const [a,b]=polys(svg(id)).map(omkrets);assert.ok(Math.abs(b/a-k)<0.01,`${id}: ${(b/a).toFixed(3)} ≠ ${k}`);}
  const [s,l]=polys(svg('3.641'));const h=P=>Math.max(...P.map(p=>p[1]))-Math.min(...P.map(p=>p[1]));assert.ok(Math.abs(h(l)/h(s)-3)<0.01);
});
test('Varierade texter, nya tal och facit med rubriker',()=>{
  const t=id=>get(id).t.replace(/<svg[\s\S]*?<\/svg>/g,'').replace(/<[^>]+>/g,' ');
  const lika=['3.209','3.335','3.466','3.467','3.468','3.469','3.470'].filter(id=>/^\s*Trianglarna är likformiga\. Bestäm/.test(t(id)));assert.deepEqual(lika,[]);
  assert.equal(get('3.359').rättSvar,8);assert.notEqual(t('3.359'),t('3.337'));
  for(const id of [...Object.keys(TOPP),'3.43','3.209','3.335','3.466','3.467','3.468','3.469','3.470','3.639','3.641','3.642']){const q=get(id);
    for(const s of [q.s,...(q.spelDelar||[]).map(d=>d.s)]){const li=(s.match(/<li>/g)||[]).length,r=(s.match(/facit-rubrik/g)||[]).length;assert.ok(li>0&&r>=li,id);}}
});
