const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('fs'),vm=require('vm'),path=require('path');
const root=path.join(__dirname,'..'),load=(f,key)=>{const c={window:{}};vm.runInNewContext(fs.readFileSync(path.join(root,f),'utf8'),c);return c.window[key];},ma=load('uppgifterma1.js','BANKMA1'),fy=load('uppgifter2.js','BANK2'),get=(b,id)=>b.find(q=>q.id===id);
test('Procentfacit är fullprecisionsmål med numeriskt format och procentenhet',()=>{
 const models={'3.114':300/11,'3.23':(1-65*36**.75/1088)*100,'3.65':(1.5**.2-1)*100,'3.70':(1/.64-1)*100,'3.71':(1.25/.8-1)*100,'3.105':(1.3**(1/6)-1)*100};
 for(const [id,value]of Object.entries(models)){const q=get(ma,id);assert.ok(Math.abs(q.rättSvar-value)<1e-12,id);assert.equal(typeof q.rättSvar,'number');assert.equal(q.svarFormat,'numeriskt');assert.equal(q.svarEnhet,'%');assert.ok(q.tolerans<=1e-9);assert.equal(q.miniräknare,true);assert.equal(q.geogebra,false);assert.match(q.s,/facit-rubrik/);assert.match(q.s,/facit-svar/);}
 const a=100,b=100*(1.12/.88);assert.ok(Math.abs(a*1.12-b*.88)<1e-12);assert.ok(Math.abs((b-a)/a*100-get(ma,'3.114').rättSvar)<1e-12);
});
test('Referenslösningen behåller produkt, borttagna kvadrattermer och kontroll',()=>{
 const q=get(ma,'1.116'),x=10/3;assert.equal(q.rättSvar,'10/3');assert.equal(q.svarFormat,'bråk');assert.equal(q.traningsniva,4);assert.equal(q.miniräknare,true);
 assert.ok(Math.abs((3*x-4)*(x+2)-32)<1e-12);assert.ok(Math.abs(3*x*x+5*x-18-32)<1e-12);
 for(const title of ['Utveckla vänsterledets produkt','Ta bort samma kvadratterm','Lös den linjära ekvationen','Kontrollera i ursprungsekvationen'])assert.ok(q.s.includes(title));
});
test('Öppet negativt talpar behåller villkoret, inte en enda exempelkombination',()=>{
 const q=get(ma,'0.1121');assert.equal(q.svarFormat,'negativt_talpar');assert.equal(q.svarVillkor.skillnad,6);assert.match(q.s,/många rätta svar/);
 for(const [a,b]of [[-2,-8],[-1,-7],[-.5,-6.5],[-7,-13]])assert.equal(a-b,6);
});
test('Stjärnornas delkort innehåller bara information som behövs i den delen',()=>{
 const a360=get(fy,'5.360').spelDelar[0],b360=get(fy,'5.360').spelDelar[1],a361=get(fy,'5.361').spelDelar[0],b361=get(fy,'5.361').spelDelar[1];
 assert.doesNotMatch(a360.t,/magnitud/i);assert.doesNotMatch(b360.t,/15 500|2,37/);assert.match(b360.t,/2,31/);
 assert.doesNotMatch(a361.t,/22 000|temperatur/);assert.match(a361.t,/−2,8/);assert.doesNotMatch(b361.t,/−2,8|magnitud/);assert.match(b361.t,/1040/);assert.match(b361.t,/22 000/);
 assert.doesNotMatch(get(fy,'5.362').spelDelar[0].t,/magnitud/i);assert.doesNotMatch(get(fy,'5.362').spelDelar[1].t,/radie/);
 assert.doesNotMatch(get(fy,'5.365').spelDelar[0].t,/magnitud/i);assert.doesNotMatch(get(fy,'5.365').spelDelar[1].t,/radie|temperatur/);
 const L=4*Math.PI*(2.37e9)**2*5.670374419e-8*15500**4;assert.ok(Math.abs(get(fy,'5.360').rättSvar[0]/L-1)<1e-12);
});
test('Tidigare rättade HR-diagram, nivå och månpendel finns kvar',()=>{
 for(const id of ['5.314','5.324']){const q=get(fy,id);assert.match(q.t,/<svg/);assert.equal(q.miniräknare,true);assert.equal(q.geogebra,false);}
 assert.equal(get(fy,'5.323').traningsniva,3);assert.equal(get(fy,'5.323').rättSvar,10);
 const q=get(fy,'2.498');assert.match(q.spelDelar[1].fraga,/Hur lång ska pendeln/);assert.ok(Math.abs(q.rättSvar[1]-1.62/(4*Math.PI**2))<1e-12);assert.equal(q.svarEnhet[1],'m');
 assert.equal(get(fy,'3.426').alternativ.find(a=>a.ratt).txt,'Höga toner (diskant)');
});
