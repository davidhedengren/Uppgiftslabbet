'use strict';
const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('node:fs'),vm=require('node:vm'),path=require('node:path'),cp=require('node:child_process');
const root=path.join(__dirname,'..'),c={window:{}};vm.runInNewContext(fs.readFileSync(path.join(root,'uppgifterma2.js'),'utf8'),c);
const bank=c.window.BANKMA2,q=id=>bank.find(x=>x.id===id),ids=['4.257','4.2148','4.2149','4.2150','4.2151'];
test('Ingen gissning: bandresonemanget föregår kontrollen av 5,90',()=>{
 const s=q('4.257').s;assert.match(s,/95,4/);assert.match(s,/34\{,\}13\+34\{,\}13\+13\{,\}59\+2\{,\}14/);assert.match(s,/mu-0\{,\}05=5\{,\}85/);
 assert.ok(s.indexOf('Fyra band')<s.indexOf('Kontrollera det härledda'));assert.match(s,/6\{,\}00/);assert.match(s,/sök systematiskt/);assert.doesNotMatch(s,/Pröva medelvärdet/);assert.equal(q('4.257').rättSvar,5.9);assert.match(q('4.257').t,/två decimaler/);
});
test('Nya uppgifter, verktyg, svarsmängd och bilder',()=>{
 assert.equal(new Set(bank.map(q=>q.id)).size,bank.length);
 for(const id of ids){const u=q(id);assert.ok(u,id);assert.equal(u.omr,'normalfordelat_material');assert.equal(u.geogebra,true);assert.equal(u.miniräknare,true);assert.equal(u.spel,true);assert.ok(u.ledtrad);
  assert.match(u.s,/facit-steglista/);assert.match(u.s,/facit-rubrik/);assert.match(u.s,/facit-svar/);assert.match(u.s,/GeoGebra/);assert.match(u.s,/symmetri|spegel|sänkning/i);
  for(const [,file] of u.s.matchAll(/src="([^"]+)"/g))assert.ok(fs.statSync(path.join(root,file)).size>1000,file);
 }
 assert.equal(q('4.2148').svarsstruktur,'mängd');assert.deepEqual(Array.from(q('4.2148').rättSvar),[50,54]);assert.match(q('4.2149').t,/större än 205/);assert.match(q('4.2151').t,/längre än 26/);
 assert.equal(q('4.2150').rättSvar,5);assert.match(q('4.2150').t,/standardavvikelsen ska vara kvar/);
});
test('Oberoende normalintegral och numeriska lösningar skyddar avrundningarna',()=>{
 const code=`import math
F=lambda z:(1+math.erf(z/math.sqrt(2)))/2
P=lambda m,s,a,b:F((b-m)/s)-F((a-m)/s)
cases=[(5.9,.05,5.85,6.05,.84,.001),(50,2,48,56,.84,.02),(210,10,190,220,.8185,.05),(495,5,490,510,.84,.02),(27,2,23,29,.8185,.02)]
for target,s,a,b,p,tol in cases:
 mid=(a+b)/2
 lo,hi=(a-10*s,mid) if target<mid else (mid,b+10*s)
 for _ in range(90):
  m=(lo+hi)/2
  if (P(m,s,a,b)<p)==(target<mid):lo=m
  else:hi=m
 assert abs((lo+hi)/2-target)<tol,(target,(lo+hi)/2)
 assert abs(P(target,s,a,b)-p)<.0001
assert abs(P(50,2,48,56)-P(54,2,48,56))<1e-12
assert P(494,5,490,510)<.84<P(496,5,490,510)
assert abs(P(5.925,.05,5.85,6.05)*100-92.70)<.005
assert abs(P(5.875,.05,5.85,6.05)*100-69.12)<.005
`;
 const r=cp.spawnSync('python3',['-c',code],{encoding:'utf8'});assert.equal(r.status,0,r.stderr);
});
test('Skärmbilderna verifierades via GeoGebras modell utan urklipp',()=>{
 const log=JSON.parse(fs.readFileSync(path.join(__dirname,'ma2-medelvarden-geogebra-2026-11-06.json'),'utf8'));assert.equal(log.length,6);
 for(const r of log){assert.equal(+r.low,r.lo);assert.equal(+r.high,r.hi);assert.deepEqual(r.parameters.split(',').map(Number),[r.mu,r.sigma]);assert.ok(r.version)}
 assert.equal(log.find(r=>r.slug==='ma2-4-2151').value,'0.1814');
 const capture=fs.readFileSync(path.join(__dirname,'ma2-medelvarden-skarmbilder-2026-11-06.cjs'),'utf8');assert.doesNotMatch(capture,/navigator\.clipboard|grantPermissions|permissions:/);
});
test('Bankbilder följer appens rot även efter byte till en kursadress',()=>{
 const html=fs.readFileSync(path.join(root,'index.html'),'utf8');
 const helper=html.slice(html.indexOf('function bankBildadresser('),html.indexOf('function uppgiftsText('));
 for(const base of ['/','/Uppgiftslabbet/']){
  const context={APP_ROOT:base};vm.runInNewContext(helper,context);
  for(const id of ['4.257','4.256','4.261','4.285','4.286','4.51']){
   const fixed=context.bankBildadresser(q(id).s);
   assert.doesNotMatch(fixed,/<img[^>]+src=["'](?:\.\/)?bilder\//i,id);
  }
  assert.equal(context.bankBildadresser('<img src="bilder/a.png"><img src="./bilder/b.png">'),`<img src="${base}bilder/a.png"><img src="${base}bilder/b.png">`);
  const other='<img src="https://example.com/a.png"><img src="data:image/png;base64,abc"><svg><image href="#x"/></svg>';
  assert.equal(context.bankBildadresser(other),other);
 }
});
