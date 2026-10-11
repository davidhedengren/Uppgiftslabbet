'use strict';
const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('node:fs'),path=require('node:path'),vm=require('node:vm');
const c={window:{}};vm.createContext(c);for(const f of ['uppgifter.js','uppgifterma1.js'])vm.runInContext(fs.readFileSync(path.join(__dirname,'..',f),'utf8'),c);
const fy=id=>c.window.BANK.find(t=>t.id===id),ma=id=>c.window.BANKMA1.find(t=>t.id===id),g=9.82,sin=a=>Math.sin(a*Math.PI/180);
const close=(a,b)=>assert.ok(Math.abs(a-b)<1e-10,`${a} ≠ ${b}`);
test('5.224: samma bromskraft används utan för tidig avrundning; varje kort är självständigt',()=>{
 const t=fy('5.224'),F=(.5*5**2/2)/2-.5*g*sin(20),distance=16/(.5*g*sin(40)+F),b=t.spelDelar[1];
 close(t.rättSvar[0],F);close(t.rättSvar[1],distance);close(b.rättSvar,16/(.5*g*sin(40)+1.4457));
 assert.equal(distance.toFixed(2),'3.48');assert.equal((16/(.5*g*sin(40)+1.45)).toFixed(2),'3.47');
 assert.match(t.t,/Bromskraften F är oförändrad/);assert.match(b.t,/1,4457 N/);assert.doesNotMatch(b.t,/5,0 m\/s|20°|svaret från a/);
 assert.ok(Math.abs(3.48-b.rättSvar)<=t.tolerans[1]);assert.ok(Math.abs(3.47-b.rättSvar)>t.tolerans[1]);
});
test('0.992: en decimal är angiven och både 3,1 och extra precision godtas',()=>{
 const t=ma('0.992'),raw=25*(135/18)/60;close(t.rättSvar,raw);assert.match(t.t,/tom pool/);assert.match(t.t,/en decimal/);
 assert.ok(Math.abs(3.1-raw)<=t.tolerans);assert.ok(Math.abs(3.2-raw)>t.tolerans);assert.ok(Math.abs(3.0-raw)>t.tolerans);
 assert.match(t.s,/3\{,\}125/);assert.match(t.s,/3\{,\}1/);assert.equal(t.traningsniva,2);assert.equal(t.niva,'E');
});
test('6.105 och fem tryckanalogier skiljer vattenpelarens ökning från totaltrycket',()=>{
 for(const[id,want]of [['6.105',700000/(998*g)],['6.254',29460/(1000*g)],['6.305',3928/(1000*g)],['6.261',(179860-101300)/(1000*g)],['6.264',24000/(870*g)],['6.356',19640/(1000*g)]])close(fy(id).rättSvar,want);
 assert.match(fy('6.105').t,/högre än vid vattenytan/);assert.doesNotMatch(fy('6.105').t,/insidan|utsidan|behållare/);assert.equal(fy('6.261').traningsniva,2);
});
test('5.55: gram till kilogram och energier stämmer; tidigare rättning bevaras',()=>{
 const t=fy('5.55');close(t.rättSvar[0],25/1000);close(t.rättSvar[1],.025*62**2/2);close(t.rättSvar[2],.025*124**2/2);
 assert.equal(t.spelDelar[0].traningsniva,1);assert.match(t.spelDelar[0].t,/25 g/);assert.doesNotMatch(t.spelDelar[0].t,/62 m\/s/);
});
test('Exakt halvavrundning i 5.514 d godtar 4810, full precision och avvisar 4800',()=>{
 const t=fy('5.514'),raw=(.015*310**2/2)/.15;assert.equal(raw,4805);assert.equal(t.rättSvar[3],4810);
 assert.ok(Math.abs(raw-t.rättSvar[3])<=t.tolerans[3]);assert.ok(Math.abs(4800-t.rättSvar[3])>t.tolerans[3]);
 assert.match(t.spelDelar[3].s,/4810/);
});
test('Proportionalitetsanalogier har korrekta svar och rimlig rutinnivå',()=>{
 for(const[id,want]of [['0.987',21/(7/2)+5*(7/2)],['0.988',40/2.5*6],['0.989',26.1/87*100],['0.990',Math.round(100/(42/350))],['0.991',(6.8-.55*10)*2.5]]){
  close(ma(id).rättSvar,want);assert.equal(ma(id).traningsniva,2);assert.equal(ma(id).niva,'E');
 }
 assert.match(ma('0.991').t,/två decimaler/);
});
test('Halvavrundningar: rätt avrundat värde och full precision, inte andra grannvärdet',()=>{
 const cases=[['5.72',0,25*g,246,245],['5.270',0,.260*2.25*30,17.6,17.5],['5.160',3,(3*2.5-4*1.5+3)/4,1.13,1.12],
 ['5.370',0,5500*3/400,41.3,41.2],['5.375',0,.045*25/.002,563,562],['5.381',0,.35*(-3.1-5),-2.84,-2.83],
 ['5.209',2,15*g*5,737,736],['5.578',0,((96000+60000)/(72/3.6)-1500*(.2+.3))/2,3530,3520],
 ['5.505',2,305/4,76.3,76.2],['5.509',1,57*(7**2-6**2)/2,371,370],['5.514',3,(.015*310**2/2)/.15,4810,4800],
 ['6.457',1,.1*g/.004,246,245],['5.529',1,85*5*.5,213,212],['5.533',0,.030*.25*g,.0737,.0736],
 ['5.418',1,.25*.79**2/2-.25*.12**2/2-.35*.65**2/2,.00228,.00227],['5.440',2,.0225*(30-23)/.2,.788,.787]];
 for(const[id,i,raw,rounded,wrong]of cases){const t=fy(id),target=Array.isArray(t.rättSvar)?t.rättSvar[i]:t.rättSvar,tol=Array.isArray(t.tolerans)?t.tolerans[i]:t.tolerans;
  assert.equal(target,rounded,id);assert.ok(Math.abs(target-raw)<=tol+1e-10,id);assert.ok(Math.abs(target-wrong)>tol+1e-10,id);
 }
});
