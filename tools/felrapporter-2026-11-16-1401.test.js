'use strict';
// Felrapporter 2026-11-16 14:01. Logg: agent/FELRAPPORTER_2026-11-16_1401.md
const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('node:fs'),vm=require('node:vm'),path=require('node:path');
function bank(file,key){const c={window:{}};vm.runInNewContext(fs.readFileSync(path.join(__dirname,'..',file),'utf8'),c);return c.window[key];}
const ma1=bank('uppgifterma1.js','BANKMA1'),ma5=bank('uppgiftermatf1.js','BANKMATF1');
const q=(b,id)=>{const x=b.find(x=>x.id===id);assert.ok(x,id);return x};

test('Ma5 4.469 frågar efter kvoten mellan felen och facit följer mallen',()=>{
 const u=q(ma5,'4.469');
 assert.match(u.t,/Hur många gånger mindre blir felet när steglängden halveras\? \(?Svara med kvoten mellan felen\.\)?/);/* språkomskrivningen 2026-11-19 */
 assert.doesNotMatch(u.t,/Hur mycket mindre/);
 assert.match(u.t,/h=0\{,\}2/);assert.match(u.t,/h=0\{,\}1/);
 const f1=Math.E-1.2**5,f2=Math.E-1.1**10;
 assert.ok(Math.abs(f1-0.229962)<1e-6);assert.ok(Math.abs(f2-0.124540)<1e-6);
 assert.ok(Math.abs(u.rättSvar-f1/f2)<1e-9);assert.equal(u.tolerans,0.05);
 assert.match(u.s,/facit-steglista/);assert.match(u.s,/1\{,\}85/);assert.match(u.s,/Ungefär 1,85 gånger mindre/);
 assert.match(u.ledtrad,/\(1\+h\)/);assert.doesNotMatch(u.ledtrad,/nettot/);
 for(const x of [u.t,u.s,u.ledtrad]){assert.ok(!x.includes("\\'"),'accent \\\' i LaTeX');assert.ok(!x.includes('\t'));}
});

test('Ma5 4.174 och 4.582 (stabilitet, utanför kursen) visas inte i Kunskapsgymmet',()=>{
 for(const id of ['4.174','4.582'])assert.equal(q(ma5,id).spel,false,id);
});

test('Ma1 4.529: höjden ritas innanför trapetsen',()=>{
 const t=q(ma1,'4.529').t;
 const pts=t.match(/<polygon points="([^"]+)"/)[1].trim().split(/\s+/).map(p=>p.split(',').map(Number));
 const xs=pts.map(p=>p[0]),ys=pts.map(p=>p[1]);
 const h=t.match(/<line x1="([\d.]+)" y1="([\d.]+)" x2="([\d.]+)" y2="([\d.]+)" stroke="#c2410c"[^>]*stroke-dasharray/);
 assert.ok(h,'streckad höjd');const [x1,y1,x2,y2]=h.slice(1).map(Number);
 assert.equal(x1,x2);assert.ok(x1>Math.min(...xs)&&x1<Math.max(...xs));
 assert.equal(y1,Math.min(...ys));assert.equal(y2,Math.max(...ys));
 // höjden ska ligga innanför de båda sneda sidorna på hela sträckan
 const kant=(a,b,y)=>a[0]+(b[0]-a[0])*(y-a[1])/(b[1]-a[1]);
 for(const y of [y1,(y1+y2)/2,y2]){
  assert.ok(x1>=kant(pts[0],pts[3],y)-1e-9&&x1<=kant(pts[1],pts[2],y)+1e-9,`y=${y}`);
 }
 assert.doesNotMatch(t,/x1="300\.0"/);
 assert.match(t,/text-anchor="end"[^>]*>0,6 m</);
});
