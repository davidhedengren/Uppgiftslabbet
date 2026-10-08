'use strict';
const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('node:fs'),vm=require('node:vm'),path=require('node:path');
const c={window:{}};vm.runInNewContext(fs.readFileSync(path.join(__dirname,'../uppgifter.js'),'utf8'),c);const q=id=>c.window.BANK.find(x=>x.id===id);
test('Bilen: beräkna reaktion, bromsning, stopp och träfffart oberoende',()=>{
 const v=80/3.6,brake=v*v/14;const short=v*.8+brake,long=v*2.3+brake,impact=Math.sqrt(v*v-14*(60-v*2.3))*3.6;
 assert.ok(Math.abs(short-53.0511463845)<1e-9);assert.ok(Math.abs(long-86.3844797178)<1e-9);assert.ok(short<60&&long>60);assert.ok(Math.abs(impact-69.18959459)<1e-7);
 const task=q('3.172');assert.match(task.t,/<p>a\)/);assert.match(task.t,/<p>b\)/);assert.match(task.s,/v_0t_r/);assert.match(task.s,/17\{,\}78\+35\{,\}27/);assert.match(task.s,/51\{,\}11\+35\{,\}27/);
});
test('Fysiklösningar saknar numrerade steg men bevarar separata delbokstäver',()=>{
 function visit(x){if(Array.isArray(x))x.forEach(visit);else if(x&&typeof x==='object')for(const[k,v]of Object.entries(x)){if(k==='s'&&typeof v==='string'){assert.doesNotMatch(v,/facit-steglista|<span class="facit-mark">\d+<\/span>/);assert.match(v,/facit-stegvis/);}else if(v&&typeof v==='object')visit(v);}}
 visit(c.window.BANK);assert.match(q('2.315').s,/<strong>a\)/);
});
test('Upphinnandet avser tiden efter B:s start, och varje delkort anger riktning',()=>{
 const task=q('2.307'),t=625;assert.equal(4.2*t-5*(t-300),1000);assert.ok(t>=300);
 assert.match(task.spelDelar[1].t,/Efter att B har börjat/);assert.match(task.spelDelar[2].t,/samma håll/);
 assert.ok(Math.abs(t/60-task.rättSvar[1])<task.tolerans[1]);
});
test('Enkelresans längd och fysisk vindmodell är entydiga',()=>{
 assert.match(q('2.315').spelDelar[0].t,/120 km till en ort och sedan samma 120 km tillbaka/);
 assert.equal(120/(30-10)-120/30,2);
 assert.match(q('2.317').spelDelar[3].t,/båt/i);assert.ok(Math.abs((42/1.4+42/1.68)/2-27.5)<1e-10);
});
test('Pulstiden avser mottagna pulser och varje storhet kontrolleras numeriskt',()=>{
 const task=q('2.320'),u=40/3.6,dt=7500/(1500+u),s=u*dt;
 assert.match(task.t,/tar emot två på varandra följande pulser/);assert.ok(dt<5);assert.ok(Math.abs(s-task.rättSvar)<task.tolerans);
 assert.ok(Math.abs(u*5-task.rättSvar)>task.tolerans);
});
test('Avrundade slutsvar stämmer med oberoende beräkningar och avvisar närmaste felaktiga steg',()=>{
 const data=[['2.223',23.5/6000*1000],['2.280',170/7.8],['3.256',135/11],['3.258',340/14],['3.260',50/3.6],['3.262',650/150],['2.239',.5/45*100],['2.302',.850*(1.25*5/(1.25-.85))],['2.304',5/(5/340-.0137)],['2.309',(1+360/102-360/85)*60],['2.313',1200/3.6+800/3.9-1500/4-500/3.1]];
 for(const[id,value]of data){const task=q(id);assert.ok(Math.abs(value-task.rättSvar)<=task.tolerans,id);assert.ok(Math.abs((task.rättSvar+task.tolerans*2.1)-task.rättSvar)>task.tolerans,id);}
});
test('Densitet: beräkningar och enheter stämmer utan sönderbrutna enhetsbråk',()=>{
 assert.ok(Math.abs(7.87*Math.PI*1.425**2*85.8/1000-4.31)<.005);
 assert.equal(19.3*35-21.5*31,9);
 for(const task of c.window.BANK.filter(x=>x.kap===2))assert.doesNotMatch(task.s,/\\frac\{[^]+? g\}\{c\} m\^\{3\}/,task.id);
});
