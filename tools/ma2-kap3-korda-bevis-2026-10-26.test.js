'use strict';
/* Ma2 kap 3, etapp 6: kordasatsen och bevis med likformighet (lärarbeslut 2026-10-25).
   - Tre nästan identiska kordakort (3.79, 3.315, 3.340) har fått sammanhang och kordafigurer där cirkeln är
     beräknad ur delarna.
   - Sex kort med samma DE ∥ BC-mall har varierade, skalenliga figurer.
   - 3.283 var samma fråga som 3.254 och markerar nu vinkeln AED. 3.254 hade två alternativ för samma vinkel. */
const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('node:fs'),vm=require('node:vm'),path=require('node:path');
const c={window:{}};vm.runInNewContext(fs.readFileSync(path.join(__dirname,'..','uppgifterma2.js'),'utf8'),c);
const B=JSON.parse(JSON.stringify(c.window.BANKMA2)),get=id=>{const t=B.find(x=>x.id===id);assert.ok(t,id);return t;};
const svg=id=>{const q=get(id);return ((q.spelIntro||'')+q.t).match(/<svg[\s\S]*?<\/svg>/)[0];};
test('Kordafigurerna: alla fyra ändpunkter ligger på cirkeln och delarna stämmer',()=>{
  for(const[id,[a,b,cc,d]]of Object.entries({'3.79':[5,6,3,10],'3.315':[4,6,3,8],'3.340':[5,12,6,10]})){const s=svg(id);
    const [cx,cy,r]=s.match(/<circle cx="([\d.]+)" cy="([\d.]+)" r="([\d.]+)" fill="none"/).slice(1).map(Number);
    const L=[...s.matchAll(/<line x1="([\d.-]+)" y1="([\d.-]+)" x2="([\d.-]+)" y2="([\d.-]+)"/g)].map(m=>[1,2,3,4].map(i=>+m[i]));
    for(const[x1,y1,x2,y2]of L){assert.ok(Math.abs(Math.hypot(x1-cx,y1-cy)-r)<1.5,id);assert.ok(Math.abs(Math.hypot(x2-cx,y2-cy)-r)<1.5,id);}
    const len=L.map(([x1,y1,x2,y2])=>Math.hypot(x2-x1,y2-y1));assert.ok(Math.abs(len[0]/len[1]-(a+b)/(cc+d))<0.01,id);
    assert.equal(get(id).rättSvar,d,id);}
  const t=id=>get(id).t.replace(/<svg[\s\S]*?<\/svg>/g,'').replace(/<[^>]+>/g,' ').slice(0,40);assert.equal(new Set(['3.44','3.79','3.315','3.340'].map(t)).size,4);
});
test('Bevis: varierade figurer, rättade alternativ och facit med rubriker',()=>{
  const former=new Set(['3.152','3.177','3.206','3.254','3.255','3.283'].map(id=>svg(id).match(/<polygon points="([^"]+)"/)[1]));assert.equal(former.size,6);
  assert.deepEqual(get('3.283').alternativ.filter(a=>a.ratt).map(a=>a.txt),[String.raw`\(\angle ACB\)`]);assert.match(get('3.283').t,/angle AED/);
  const alt=get('3.254').alternativ.map(a=>a.txt);assert.ok(!(alt.includes(String.raw`\(\angle ACB\)`)&&alt.includes(String.raw`\(\angle BCA\)`)));
  const pol=s=>[...s.matchAll(/<polygon points="([^"]+)" fill="none"/g)].map(m=>m[1].trim().split(/\s+/).map(p=>p.split(',').map(Number)));
  const om=P=>P.reduce((s,p,i)=>s+Math.hypot(p[0]-P[(i+1)%3][0],p[1]-P[(i+1)%3][1]),0);const [x,y]=pol(svg('3.151')).map(om);assert.ok(Math.abs(y/x-1.5)<0.01);
  for(const id of ['3.79','3.315','3.340','3.152','3.177','3.206','3.254','3.255','3.283','3.151','3.284']){const q=get(id);
    for(const s of [q.s,...(q.spelDelar||[]).map(d=>d.s)]){const li=(s.match(/<li>/g)||[]).length,r=(s.match(/facit-rubrik/g)||[]).length;assert.ok(li>0&&r>=li,id);}}
});
