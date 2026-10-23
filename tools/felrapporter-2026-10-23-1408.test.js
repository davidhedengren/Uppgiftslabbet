const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('fs'),vm=require('vm'),path=require('path');
const root=path.join(__dirname,'..'),load=(f,key)=>{let c={window:{}};vm.runInNewContext(fs.readFileSync(path.join(root,f),'utf8'),c);return c.window[key];},ma=load('uppgifterma1.js','BANKMA1'),fy=load('uppgifter.js','BANK'),get=(b,id)=>b.find(q=>q.id===id);
test('Reapriset och fem procentanalogier har oavrundade numeriska mål',()=>{
 const models={'3.175':65/35*100,'3.35':(1-(1.15*.85)**20)*100,'3.108':(1-1.12*.88)*100,'3.134':(1-(170000/250000)**(1/6))*100,'3.138':(1-(192000/300000)**.25)*100,'3.168':(1.035**6-1)*100};
 for(const[id,x]of Object.entries(models)){const q=get(ma,id);assert.ok(Math.abs(q.rättSvar-x)<1e-10,id);assert.equal(q.svarFormat,'numeriskt');assert.equal(q.svarEnhet,'%');assert.equal(q.tolerans,1e-10);assert.equal(q.miniräknare,true);assert.equal(q.geogebra,false);assert.match(q.s,/facit-rubrik/);assert.match(q.s,/facit-svar/);}
 assert.match(get(ma,'3.35').t,/minskat/);assert.match(get(ma,'3.108').t,/lägre/);assert.match(get(ma,'3.138').t,/i procent/);
});
test('Påståendena rättas som verkliga alternativ, utan motstridigt bokstavsfacit',()=>{
 for(const id of ['3.72','3.27']){const q=get(ma,id);assert.equal(q.svarstyp,'alternativ');assert.equal(q.rättSvar,null);assert.equal(q.alternativ.length,4);assert.equal(q.självrättning,true);assert.equal(q.miniräknare,true);assert.equal(q.geogebra,false);}
 assert.deepEqual(Array.from(get(ma,'3.72').alternativ,a=>a.ratt),[true,false,true,true]);
 assert.ok(Math.abs(1.25*.8-1)<1e-12);assert.equal((260-200)/200*100,30);assert.equal(get(ma,'3.27').alternativ.filter(a=>a.ratt).length,1);
});
test('Påståendena följer med till Uppgiftslabbets skärm- och exportunderlag',()=>{
 const source=fs.readFileSync(path.join(root,'index.html'),'utf8'),c={};
 for(const name of ['altVisas','uppgiftsText','altFacit']){const i=source.indexOf('function '+name+'(');vm.runInNewContext(source.slice(i,source.indexOf('\n}',i)+2),c);}
 c.altBokstav=i=>String.fromCharCode(65+i);
 for(const id of ['3.27','3.72']){const q=get(ma,id),text=c.uppgiftsText(q);assert.equal((text.match(/class="ul-alt"/g)||[]).length,4);for(const a of q.alternativ)assert.ok(text.includes(a.txt));for(const a of q.alternativ.filter(a=>a.ratt))assert.ok(c.altFacit(q).includes(a.txt));}
 // Ett numeriskt kort med gamla, oanvända alternativ ska förbli numeriskt.
 assert.equal(c.altVisas(get(ma,'3.408')),false);assert.equal(get(ma,'3.408').svarstyp,'numeriskt');
});
test('Truckens retardationsstorlek är positiv; tågets acceleration har tecken',()=>{
 const q=get(fy,'3.84');assert.equal(q.rättSvar[0],20/8);assert.equal(q.svarEnhet[0],'m/s²');assert.equal(q.rättSvar[1],20*8/2);assert.equal(q.rättSvar[2],90-80);assert.match(q.spelDelar[0].fraga,/storlek/);assert.match(q.spelDelar[0].t,/<svg/);assert.equal(q.miniräknare,true);
 for(const[id,part,value]of [['3.16',1,12/8],['3.18',0,12/8],['3.26',1,8/4],['3.33',0,3/6],['3.34',1,-.5]]){const a=get(fy,id);assert.equal(a.rättSvar[part],value,id);assert.equal(a.svarEnhet[part],'m/s²');assert.equal(a.miniräknare,true);}
});
