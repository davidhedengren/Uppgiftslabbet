'use strict';
// Felrapporter 2026-11-16 08:16 (Lars-Åke Andersson): Fy2 3.208, 4.18 a och 3.29. Logg: agent/FELRAPPORTER_2026-11-16_0816.md.
const {test}=require('node:test'),a=require('node:assert/strict'),fs=require('node:fs'),vm=require('node:vm');
const las=(f,n)=>{const c={window:{}};vm.runInNewContext(fs.readFileSync(f,'utf8'),c);return c.window[n];};
const fy2=las('uppgifter2.js','BANK2');
const q=id=>{const u=fy2.find(x=>x.id===id);a.ok(u,id);return u;};

test('3.208: ingen pil eller minustecken bredvid slingan',()=>{
 const t=q('3.208').t;
 a.doesNotMatch(t,/x1="296"/);a.doesNotMatch(t,/>−<\/text>/);a.doesNotMatch(t,/<polygon/);
 a.equal((t.match(/<circle /g)||[]).length,6,'slingan och fem kryss finns kvar');
 a.match(t,/minskar i styrka/);a.equal(q('3.208').rättSvar,'medurs');
});

test('3.29: vinkelbågen har sin mittpunkt i kompassens centrum',()=>{
 const t=q('3.29').t,m=t.match(/M ([\d.]+) ([\d.]+) A (\d+) \d+ 0 ([01]) ([01]) ([\d.]+) ([\d.]+)/);
 a.ok(m);const [x1,y1,r,fa,fs,x2,y2]=m.slice(1).map(Number);
 // SVG-specifikationen F.6.5: mittpunkten för en cirkelbåge
 const xp=(x1-x2)/2,yp=(y1-y2)/2,d=xp*xp+yp*yp,k=(fa!==fs?1:-1)*Math.sqrt((r*r-d)/d);
 const cx=k*yp+(x1+x2)/2,cy=-k*xp+(y1+y2)/2;
 a.ok(Math.hypot(cx-168,cy-116)<0.1,`mittpunkt (${cx.toFixed(1)}, ${cy.toFixed(1)})`);
 // 30° från nord, medurs
 a.ok(Math.abs(Math.atan2(x2-168,116-y2)*180/Math.PI-30)<0.1);
});

test('4.18: två värdesiffror godtas, facit för b räknat om, ledtråden handlar om uppgiften',()=>{
 const u=q('4.18'),e=1.602e-19,mp=1.6726e-27,h=6.626e-34;
 const v=Math.sqrt(2*e*2.0e6/mp),lam=h/(mp*v);
 a.ok(Math.abs(u.rättSvar[0]-v)/v<1e-3,'a');a.ok(Math.abs(u.rättSvar[1]-lam)/lam<3e-3,'b');
 a.deepEqual([...u.svarVardesiffror],[2,2,null]);
 a.ok(Math.abs(h/(1.67e-27*1.96e7)-2.02e-14)<0.005e-14,'facitets egna avrundade tal ger 2,02');
 for(const x of [u.s,u.spelDelar[1].s,u.spelDelar[2].t,u.spelDelar[2].s])a.doesNotMatch(x,/2\{,\}03/);
 for(const l of [u.ledtrad,...u.spelDelar.map(p=>p.ledtrad)]){a.doesNotMatch(l,/qvB|F_E/);}
 a.match(u.spelDelar[1].ledtrad,/de Broglies samband/);
});

test('4.17 och 4.27: ingen ledtråd om fältkrafter i uppgifter utan fält',()=>{
 for(const id of ['4.17','4.18','4.27']){const u=q(id);for(const l of [u.ledtrad,...(u.spelDelar||[]).map(p=>p.ledtrad||'')])a.doesNotMatch(l,/Skriv kraften från varje fält/,id);}
 a.match(q('4.17').ledtrad,/Spänningens arbete blir elektronens rörelseenergi\./);
 a.match(q('4.27').ledtrad,/de Broglies samband ger den rörelsemängd som krävs\./);
});
