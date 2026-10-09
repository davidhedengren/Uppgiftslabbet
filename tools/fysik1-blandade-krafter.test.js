'use strict';
const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('node:fs'),vm=require('node:vm'),path=require('node:path');
const c={window:{}};vm.runInNewContext(fs.readFileSync(path.join(__dirname,'../uppgifter.js'),'utf8'),c);
const q=id=>c.window.BANK.find(x=>x.id===id),g=9.82,sin=d=>Math.sin(d*Math.PI/180),cos=d=>Math.cos(d*Math.PI/180),asin=v=>Math.asin(v)*180/Math.PI,atan=v=>Math.atan(v)*180/Math.PI;
const a168=g*sin(20),a279=60/18-.25*g,a284=g*(1.2-.2*3)/(3+1.2);
// Givna värden har lästs från frågorna; uttrycken läser aldrig rättSvar eller facit.
const cases=[
 ["4.151",[(240*0.05),(((240*0.05)-6)/1.2),((0.5*(((240*0.05)-6)/1.2))*(2**2))]],
 ["4.425",((60-15)/10)],
 ["4.153",[(2.4/3),((700*(g+(2.4/3)))/1000),((0.5*2.4)*3)]],
 ["4.155",[(3/2),((500*(g+(3/2)))/1000),((0.5*3)*2)]],
 ["4.427",((25-80)/14)],
 ["4.158",[(-8/5),((75*8)/5),((0.5*8)*5)]],
 ["4.429",((18*2)+15)],
 ["4.159",[((2*9)/(3**2)),((((20*2)*9)/(3**2))+25),((2*9)/3)]],
 ["4.160",[((1400+600)*0.8),(600*0.8),(0.8*12),((0.5*0.8)*(12**2)),((600*0.8)+150)]],
 ["4.430",(60-(20*2))],
 ["4.161",[(((200000*20)/100)/1000),0,(((200000*20)/50)/1000),(((((0.5*100)*20)/1000)+((200*20)/1000))+(((0.5*50)*20)/1000))]],
 ["4.162",((((20/5)*3)/500)*100)],
 ["4.164",[((20-4)/32),(3/((20-4)/32)),((0.5*((20-4)/32))*(6**2))]],
 ["4.165",[((14**2)/(2*0.6)),(((1300*(14**2))/(2*0.6))/1000),(((2*0.6)/14)*1000),(((1300*(14**2))/(2*0.2))/1000)]],
 ["4.166",[((1.2-2.4)/8),((19*(2.4-1.2))/8),((0.5*(2.4+1.2))*8),((2.4-1.2)/(8*g))]],
 ["4.167",[((30-18)/8),(((30-18)/8)*4),((30/500)*100)]],
 ["4.434",(70*(g+1.4))],
 ["4.168",[a168,Math.sqrt(((2*a168)*3)),Math.sqrt(((2*3)/a168))]],
 ["4.169",[(350*(g+0.6)),(0.6*3),((0.5*0.6)*(3**2)),(350*g)]],
 ["4.435",((45/(6+4))-(0.14*g))],
 ["4.436",(80*(g-1.8))],
 ["4.201",[(36/24),((36/24)*4),Math.sqrt(((2*12)/(36/24)))]],
 ["4.437",((3*55)/7)],
 ["4.225",[(80*0.15),((80000*0.15)/250),((80000*0.15)/(250*g))]],
 ["4.226",[(g*sin(30)),((g*sin(30))*2),(((0.5*g)*sin(30))*(2**2))]],
 ["4.441",((18*g)*(sin(25)+(0.18*cos(25))))],
 ["4.278",(((0.5*((30-12)/6))*(2**2))+(((((30-12)/6)*2)**2)/(2*(12/6))))],
 ["4.279",[((0.25*18)*g),a279,Math.sqrt(((2*a279)*5)),(((2*a279)*5)/((2*0.25)*g))]],
 ["4.442",((14**2)/((2*0.48)*g))],
 ["4.280",(((350*0.072)-(2*g))/2)],
 ["4.443",((g*(3-(0.1*7)))/(7+3))],
 ["4.281",[((25-10)/5),((220*(25-10))/5),((0.5*(10+25))*5),((220*(25-10))/(5*300))]],
 ["4.284",[a284,(1.2*(g-a284)),Math.sqrt(((2*a284)*0.8)),Math.sqrt(((2*0.8)/a284))]],
 ["4.285",(((250*0.12)/3)-(0.25*g))],
 ["4.286",[(20/8),(((900*20)/8)/1000)]],
 ["4.446",(((3*(g-2))-(6*2))/(6*g))]
];
function check(id,expected){const t=q(id),want=Array.isArray(expected)?expected:[expected],got=Array.isArray(t.rättSvar)?t.rättSvar:[t.rättSvar];assert.equal(want.length,got.length,id);want.forEach((v,i)=>{const tol=Array.isArray(t.tolerans)?t.tolerans[i]:t.tolerans;assert.ok(Math.abs(v-got[i])<=tol+Number.EPSILON*32*Math.max(Math.abs(v),Math.abs(got[i])),`${id} del ${i}: ${v} jämfört med ${got[i]} ± ${tol}`);});}
test('Blandade krafter: samtliga 36 numeriska uppgifter räknas självständigt',()=>{
 const tasks=c.window.BANK.filter(t=>t.kap===4&&t.omr==='blandat_kraft'&&(typeof t.rättSvar==='number'||Array.isArray(t.rättSvar)));assert.equal(tasks.length,36);assert.deepEqual(new Set(cases.map(x=>x[0])),new Set(tasks.map(x=>x.id)));for(const[id,v]of cases)check(id,v);
});
test('Självständiga kort använder sina egna givna data och rätt enheter',()=>{
 assert.equal(q('4.164').svarEnhet[1],'s');assert.equal(q('4.201').svarEnhet[2],'s');
 assert.doesNotMatch(q('4.160').spelDelar[1].t,/första fyra|a–d/);assert.doesNotMatch(q('4.160').spelDelar[4].t,/första fyra|nytt fall|a–d/);
 assert.match(q('4.201').spelDelar[1].t,/1,5 m\/s²/);assert.doesNotMatch(q('4.201').spelDelar[1].ledtrad,/kraft|massa/);
 assert.match(q('4.281').spelDelar[3].t,/660 N/);assert.doesNotMatch(q('4.281').spelDelar[3].t,/ursprungliga/);
 assert.match(q('4.225').spelDelar[2].t,/48 m\/s²/);assert.match(q('4.284').spelDelar[3].s,/0\{,\}60/);
 for(const id of ['4.153','4.286'])assert.match(q(id).spelDelar[0].s,/\\frac\{\\Delta v\}\{\\Delta t\}/);
});
test('Alla 84 numeriska slutsvar i lösningsförslagen stämmer med beräkningarna',()=>{
 let checked=0;
 for(const[id,expected]of cases){const t=q(id),vs=Array.isArray(expected)?expected:[expected];
  vs.forEach((v,i)=>{const part=t.spelDelar?t.spelDelar[i]:t,cardId=t.spelDelar?id+String.fromCharCode(97+i):id;
   const math=[...part.s.matchAll(/\\\[([\s\S]*?)\\\]/g)].map(x=>x[1]).join(' ');const hits=[...math.matchAll(/(?:\\approx|=)\s*([-+]?\d+(?:\{,\}\d+)?)(?:\\cdot10\^\{?([-+]?\d+)\}?)?/g)];
   const last=hits.at(-1),shown=last?Number(last[1].replace('{,}','.'))*10**Number(last[2]||0):NaN;
   const tol=Array.isArray(t.tolerans)?t.tolerans[i]:t.tolerans;
   assert.ok(Number.isFinite(shown),`Ingen kontrollerbar slutsiffra i ${cardId}`);
   assert.ok(Math.abs(shown-v)<=tol+Number.EPSILON*32*Math.max(Math.abs(v),Math.abs(shown)),`${cardId}: facit visar ${shown}, fysisk beräkning ${v} ± ${tol}`);checked++;
  });
 }
 assert.equal(checked,84);
});
