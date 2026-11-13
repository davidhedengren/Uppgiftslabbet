'use strict';
const{test}=require('node:test'),assert=require('node:assert/strict'),fs=require('node:fs'),vm=require('node:vm'),path=require('node:path');
const root=path.join(__dirname,'..'),ctx={window:{}};for(const f of['uppgifter.js','uppgifter2.js'])vm.runInNewContext(fs.readFileSync(path.join(root,f),'utf8'),ctx);
const q=(bank,id)=>ctx.window[bank].find(q=>q.id===id),fy=id=>q('BANK2',id),near=(x,y,tol=1e-9)=>assert.ok(Math.abs(x-y)<tol*Math.max(1,Math.abs(y)),`${x} != ${y}`);
test('Fiskens avstånd utgår från ögats lodlinje och innehåller båda sträckorna',()=>{
 const t=fy('4.403'),angle=Math.asin(Math.sin(Math.PI/4)/1.33);near(t.rättSvar,.52+.65*Math.tan(angle));assert.match(t.t,/lodlinjen genom dina ögon/);assert.match(t.t,/markerat x/);assert.match(t.t,/Vattenyta/);assert.match(t.s,/x=x_l\+x_v/);assert.doesNotMatch(t.t,/vattenkant/);
});
test('Nickeltrådens nettostrålning använder den givna omgivningstemperaturen',()=>{
 const t=fy('4.456'),area=Math.PI*.000445*.955,T=t.rättSvar+273.15;assert.match(t.t,/20 °C/);near(5.67e-8*area*(T**4-293.15**4),56.5*12);assert.match(t.s,/T_0=20/);near(t.rättSvar,1457.1556835628662);assert.match(fy('4.454').t,/Bortse från inkommande strålning/);
});
test('Ljudintensitetens konkreta kedja ger samma 66,77 dB utan en färdig nivåändringsformel',()=>{
 const intensity=1e-12*10**(82/10)*(3/12)**2*4*.12;near(10*Math.log10(intensity/1e-12),66.77121254719663);
 const t=fy('2.104');for(const text of['Decibel är en logaritmisk skala','16 gånger mindre','Fyra oberoende','Skärmen släpper igenom','Tillbaka till decibel'])assert.ok(t.s.includes(text),text);
 assert.doesNotMatch(t.s,/20\\log|Delta L/);assert.match(t.s,/66\{,\}8/);
});
test('De fem ljudjämförelserna och piplösningarna har egna rubriker och slutrader',()=>{
 for(const id of['2.99','2.101','2.103','2.104','2.105','2.172','2.135','2.179','4.403','4.454','4.456']){
 const t=fy(id);for(const p of[t,...t.spelDelar||[]]){assert.match(p.s,/facit-steglista/,id);assert.match(p.s,/facit-rubrik/,id);assert.match(p.s,/facit-svar/,id);assert.doesNotMatch(p.s,/facit-metod|facit-not/,id);}
 }
 near(70+10*Math.log10(2),73.01029995663981);near(84+10*Math.log10(1/16),71.95880017344075);
 near(4*Math.PI*6**2*1e-12*10**7.8,.028543591714118988,1e-5);
 near(.8/(4*Math.PI*4**2),.0039788735772973835);near(Math.sqrt(.8/(4*Math.PI*1e-5)),79.78845608028654);
});
test('Pipornas figurlängder stämmer med vågmönster och lösning',()=>{
 const t=fy('2.135');for(const s of[t.t,...t.spelDelar.map(p=>p.t)])for(const [x,y]of[['156.00','137.50'],['311.00','137.50'],['466.00','137.50']])assert.match(s,new RegExp('rotate\\(-90 '+x+' '+y+'\\)'));
 near(340/(2*.8),212.5);near(340/(4*.6/3),425);near(340/(4*.45),188.88888888888889);
 const organ=fy('2.179');assert.doesNotMatch(organ.t,/mörkast|klang/);assert.equal(organ.spelDelar.length,3);assert.equal(organ.spelDelar[0].traningsniva,2);assert.match(organ.spelDelar[2].s,/jämnt och udda/);near(340/(2*262),.648854961832061);
});
test('Vektorkedjornas kalibrering och fysik bevaras vid radbrytning',()=>{
 assert.equal(q('BANK','4.940').spelDelar[0].traningsniva,2);
 const t=q('BANK','4.948');assert.deepEqual(Array.from(t.rättSvar).slice(0,3),[70,0,70]);assert.equal(t.spelDelar.length,4);
 for(const id of['4.933','4.938','4.939','4.940','4.947','4.948'])for(const p of q('BANK',id).spelDelar)assert.ok(p.s&&p.t,id);
});
test('Pulsmötet avser en markerad punkt och har en figur även för hela summan',()=>{
 const t=fy('2.69');assert.equal((t.t.match(/går 0,30 m\/s/g)||[]).length,2);assert.match(t.s,/0\{,\}60\+0\{,\}60=1\{,\}20/);assert.match(t.t,/där, och åt vilket håll/);assert.match(t.t,/Skissa också/);assert.match(t.s,/<svg/);assert.match(t.s,/punkt för punkt/);assert.match(t.s,/1,0 cm över/);assert.match(t.s,/ungefär 2 cm under/);
});
test('Samtliga berörda fysikuppgifter tillåter miniräknare; ingen behöver GeoGebra',()=>{
 for(const id of['4.403','4.456','4.454','2.104','2.99','2.101','2.103','2.105','2.172','2.135','2.179','2.69']){const t=fy(id);assert.equal(t.miniräknare,true,id);assert.equal(t.geogebra,false,id);for(const p of t.spelDelar||[])assert.notEqual(p.miniräknare,false,id);}
});
