'use strict';
const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('node:fs'),vm=require('node:vm'),path=require('node:path');
const root=path.join(__dirname,'..'),ctx={window:{}};vm.runInNewContext(fs.readFileSync(path.join(root,'uppgifter.js'),'utf8'),ctx);
const models=require('./fixtures/fysik1-elektricitet-fordjupning.json'),get=id=>ctx.window.BANK.find(q=>q.id===id),plain=x=>JSON.parse(JSON.stringify(x));
function close(a,b){if(Array.isArray(b)){assert.equal(a.length,b.length);b.forEach((v,i)=>close(a[i],v));}else assert.ok(Math.abs(a-b)<1e-10,`${a} != ${b}`);}
function expected(m){switch(m.type){
 case'contacts':{let q=[...m.charges];for(const [a,b]of m.contacts){const avg=(q[a]+q[b])/2;q[a]=avg;q[b]=avg;}return q;}
 case'null_force':{const ratio=Math.sqrt(Math.abs(m.charges[1]/m.charges[0]));return -m.positions[1]/(ratio-1);}
 case'vector_force':{const qt=m.charges[0],components=[0,0];for(let i=1;i<m.charges.length;i++){const [x,y]=m.positions[i],r=Math.hypot(x,y);components[0]-=m.k*qt*m.charges[i]*x/r**3;components[1]-=m.k*qt*m.charges[i]*y/r**3;}return[Math.hypot(...components)*1e6,Math.atan2(components[1],components[0])*180/Math.PI];}
 case'ground_order':return null;
 case'cavity_ground':return -m.insideCharge*1e9;
 case'contact_force_ratio':{const shared=(m.charges[0]+m.charges[1])/2,ratio=shared**2/Math.abs(m.charges[0]*m.charges[1]);return Math.round(ratio*1000)/1000;}
 case'switch_inference':{const U=m.currents[0]*(m.seriesR+m.knownR),parallel=U/m.currents[1]-m.seriesR;return[U,1/(1/parallel-1/m.knownR)];}
 case'battery_inference':{const I=m.terminalVoltages.map((u,i)=>u/m.loads[i]),r=(m.terminalVoltages[0]-m.terminalVoltages[1])/(I[1]-I[0]);return[m.terminalVoltages[0]+I[0]*r,r];}
 case'meter_loading':{const parallel=1/(1/m.loadR+1/m.meterR),I=m.sourceU/(m.seriesR+parallel);return[I*parallel,I*1000];}
 case'wire_design':{const I=Math.sqrt(m.desiredPower/m.heaterR),U=I*(m.heaterR+m.wireRs.reduce((a,b)=>a+b));return[U,100*m.desiredPower/(U*I)];}
 case'series_lamps':{const r=m.ratedU.map((u,i)=>u*u/m.ratedP[i]),I=m.sourceU/r.reduce((a,b)=>a+b);return r.map(x=>I*I*x);}
 case'balanced_bridge':{const left=m.leftRs.reduce((a,b)=>a+b),I=m.sourceU/left,v=m.leftRs[1]*I,rightI=v/m.rightLowerR,R=(m.sourceU-v)/rightI;return[R,I+rightI];}
 default:throw Error(m.type);
}}
test('Alla tolv slutsvar följer oberoende laddnings-/kretsmodeller',()=>{assert.equal(models.length,12);for(const m of models){const expectedAnswer=expected(m);if(expectedAnswer===null)assert.equal(get(m.id).rättSvar,null);else close(plain(get(m.id).rättSvar),expectedAnswer);}});
test('Nollkraftspunkt utanför laddningarna: riktningar och ingen falsk rot mellan dem',()=>{
 const m=models.find(x=>x.type==='null_force'),x=expected(m),[q1,q2]=m.charges,d=m.positions[1];
 const field=x=>q1*(x)/Math.abs(x)**3+q2*(x-d)/Math.abs(x-d)**3;
 assert.ok(x<0);assert.ok(Math.abs(field(x))<1e-20);assert.ok(field(d/3)>0);assert.ok(field(d*.75)>0);assert.ok(field(d+.2)<0);assert.match(get(m.id).s,/Mellan kulorna.*åt höger/);
});
test('Induktionsordning och kontaktsekvens bevarar laddning i rätt steg',()=>{
 const contacts=models.find(x=>x.type==='contacts');close(expected(contacts).reduce((a,b)=>a+b),contacts.charges.reduce((a,b)=>a+b));
 const q=get('8.521');assert.equal(q.alternativ.filter(x=>x.ratt).length,1);assert.equal(q.alternativ[0].ratt,true);assert.match(q.alternativ[0].txt,/A: positiv. B: oladdad/);assert.match(q.s,/kan återvända/);
 const cavity=models.find(x=>x.type==='cavity_ground');close(expected(cavity),-6);assert.match(get(cavity.id).t,/jordledningen bort.*utan att röra lådan/);assert.match(get(cavity.id).s,/inte dess nettoladdning/);
});
test('Batteri, strömfördelning, effekt och balans reproducerar givna mätvärden',()=>{
 const m=models.find(x=>x.type==='battery_inference'),[E,r]=expected(m);m.loads.forEach((R,i)=>close(E*R/(R+r),m.terminalVoltages[i]));
 const sw=models.find(x=>x.type==='switch_inference'),[U,R]=expected(sw);close(U/(sw.seriesR+sw.knownR),sw.currents[0]);close(U/(sw.seriesR+1/(1/sw.knownR+1/R)),sw.currents[1]);
 const loading=models.find(x=>x.type==='meter_loading'),[Uv,ImA]=expected(loading);close(Uv/loading.loadR+Uv/loading.meterR,ImA/1000);
 const wire=models.find(x=>x.type==='wire_design'),[wireVoltage,eta]=expected(wire),I=Math.sqrt(wire.desiredPower/wire.heaterR);close(wire.desiredPower+I*I*wire.wireRs.reduce((a,b)=>a+b),wireVoltage*I);assert.ok(eta<100);
 const bridge=models.find(x=>x.type==='balanced_bridge'),[Rx]=expected(bridge);close(bridge.sourceU*bridge.leftRs[1]/(bridge.leftRs[0]+bridge.leftRs[1]),bridge.sourceU*bridge.rightLowerR/(Rx+bridge.rightLowerR));
});
test('Exact half-rounding has a reviewed centre; lower rounded neighbour is rejected',()=>{
 const q=get('8.523');assert.equal((8-2)**2/4/(8*2),.5625);assert.equal(q.rättSvar,.563);assert.equal(q.tolerans,.0005);assert.ok(Math.abs(.5625-q.rättSvar)<q.tolerans+1e-12);assert.ok(Math.abs(.562-q.rättSvar)>q.tolerans);
});
test('Alla nya kort har egen figur, efterfrågade enheter, nivå och fullständigt facit',()=>{
 for(const m of models){const q=get(m.id);assert.equal(q.kap,8);assert.equal(q.spel,true);assert.equal(q.miniräknare,true);assert.equal(q.manuellKomplettering,false);assert.equal(q.traningsniva,m.level);assert.equal(q.niva,m.level===5?'A':'C');assert.match(q.t,/<svg.*viewBox=.*role="img"/);assert.match(q.s,/Svar:/);assert.ok(q.ledtrad);assert.doesNotMatch(q.s,/facit-steglista|<ol/);assert.doesNotMatch(q.t,/använd k\s*=|Coulombs konstant|använd.*formeln|använd g\s*=/i);assert.ok(!q.spelDelar);if(Array.isArray(q.rättSvar)){assert.equal(q.svarEtiketter.length,q.rättSvar.length);assert.equal(q.tolerans.length,q.rättSvar.length);assert.equal(q.svarEnhet.length,q.rättSvar.length);assert.equal(q.svarsstruktur,'ordnad');}}
});
test('Laddningsfigurens längder och bryggans anslutningar följer modellen',()=>{
 const q=get('8.520');assert.match(q.t,/cx="70" cy="230"/);assert.match(q.t,/cx="190" cy="50"/);assert.match(q.t,/cx="190" cy="230"/);close((230-50)/(190-70),.3/.2);
 const bridge=get('8.529');for(const [x,y]of [[210,185],[440,185],[210,60],[210,310]])assert.ok(bridge.t.includes(`cx="${x}" cy="${y}" r="4"`));assert.ok(bridge.t.includes('x1="210" y1="185" x2="303" y2="185"'));assert.ok(bridge.t.includes('x1="347" y1="185" x2="440" y2="185"'));assert.match(bridge.t,/0,00 A/);
});
