'use strict';
const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('node:fs'),vm=require('node:vm'),path=require('node:path');
const c={window:{}};vm.runInNewContext(fs.readFileSync(path.join(__dirname,'../uppgifter.js'),'utf8'),c);
const q=id=>c.window.BANK.find(x=>x.id===id),g=9.82,sin=d=>Math.sin(d*Math.PI/180),cos=d=>Math.cos(d*Math.PI/180),asin=v=>Math.asin(v)*180/Math.PI,atan=v=>Math.atan(v)*180/Math.PI;
const h291=Math.sqrt(4**2-1.6**2),s452=(550*1.3+200*1.6)/3.2,s130=g*(78*1.5+32*2.5)/5,f508=g*(75*2+20*2.5)/5,x510=Math.sqrt(5**2-4.7**2);
// Givna värden har lästs från frågorna; uttrycken läser aldrig rättSvar eller facit.
const cases=[
 ["4.6",(((4*g)*0.6)/0.3)],
 ["4.10",[(15*0.8),((15*0.8)/0.4)]],
 ["4.11",[(50*g),((50*g)*0.5),(((50*g)*0.5)/1.4)]],
 ["4.14",((30*12)/28)],
 ["4.451",((500*1.2)/3)],
 ["4.50",[(60/0.3),(60/0.6),((60/0.3)*0.55),(130/(60/0.3))]],
 ["4.51",[(16*g),((16*g)*2),((16*2)/0.5),((16*2)/0.8)]],
 ["4.61",[(30*g),((30*g)*1.5),((30*1.5)/45)]],
 ["4.62",[((200*9)/79),((400*9)/79)]],
 ["4.75",((150*1.4)/(60*g))],
 ["4.76",[((5*1.2)/1.5),((6*0.8)/1.4),((4*1.4)/0.8)]],
 ["4.77",asin((45/(150*0.4)))],
 ["4.127",[(200*0.25),(100/0.5),(150/200),2]],
 ["4.130",[((32+78)*g),s130,(((32+78)*g)-s130),2.5]],
 ["4.452",[s452,(750-s452)]],
 ["4.131",[((600*0.8)-(240*2)),(600+240)]],
 ["4.194",(((25*g)*0.3)/1.2)],
 ["4.219",(((45-35)*3)/25)],
 ["4.220",[(5*g),((5*g)*0.32),(((5*g)*0.32)/0.04),(0.32/0.04)]],
 ["4.243",((14*0.9)/65)],
 ["4.245",[((12*g)*0.18),(((12*g)*0.18)/0.2),(((12*g)*0.18)/0.1)]],
 ["4.249",[(300*0.4),((300*0.4)/1.2)]],
 ["4.250",[(120*0.18),((120*0.18)/0.12)]],
 ["4.251",[((2800*7.7)/9500),(((9500*3.4)/7.7)/1000)]],
 ["4.253",((20*1.2)/70)],
 ["4.255",((20*20)/4)],
 ["4.291",[(((12*g)*0.8)/h291),(0.8/h291)]],
 ["4.301",(((40*0.6)-(30*0.5))+(20*0.4))],
 ["4.304",[((0.3*g)*0.2),((300*20)/40)]],
 ["4.309",(((2*0)+(6*1))/8)],
 ["4.311",(((12*1)+(8*0.25))/20)],
 ["4.312",atan((0.5/0.8))],
 ["4.505",((18*1.5)/24)],
 ["4.506",(((8.2*1.2)-((2.5*g)*0.35))/(g*0.6))],
 ["4.507",(((100*25)+(20*1))/(100+20))],
 ["4.508",[f508,((95*g)-f508)]],
 ["4.509",((31.6*1.72)/(31.6+35.1))],
 ["4.510",(((g*x510)*(((68*3)/4.7)+(12/2)))/4.7)],
 ["4.511",((((620*sin(30))*0.5)-(180*0.5))/g)],
 ["4.512",(((5800*12)-((200*g)*6))/(600*g))],
 ["4.513",atan((1.2/2.2))],
 ["4.514",(((21*0.15)+(7*0.4))/0.05)],
 ["4.515",(((2.5*g)*Math.sqrt(((0.34**2)-((0.34-0.12)**2))))/(0.34-0.12))]
];
function check(id,expected){const t=q(id),want=Array.isArray(expected)?expected:[expected],got=Array.isArray(t.rättSvar)?t.rättSvar:[t.rättSvar];assert.equal(want.length,got.length,id);want.forEach((v,i)=>{const tol=Array.isArray(t.tolerans)?t.tolerans[i]:t.tolerans;assert.ok(Math.abs(v-got[i])<=tol+Number.EPSILON*32*Math.max(Math.abs(v),Math.abs(got[i])),`${id} del ${i}: ${v} jämfört med ${got[i]} ± ${tol}`);});}
test('Kraftmoment: samtliga 43 numeriska uppgifter räknas självständigt',()=>{
 const tasks=c.window.BANK.filter(t=>t.kap===4&&t.omr==='moment'&&(typeof t.rättSvar==='number'||Array.isArray(t.rättSvar)));assert.equal(tasks.length,43);assert.deepEqual(new Set(cases.map(x=>x[0])),new Set(tasks.map(x=>x.id)));for(const[id,v]of cases)check(id,v);
});
test('Kortets givna avrundade stödkraft ger ett godkänt eget svar',()=>{check('4.508',[f508,95*g-393]);});
test('Momentkort har egna förutsättningar, rätt enheter och nödvändig geometri',()=>{
 assert.match(q('4.291').spelDelar[1].s,/\\sqrt\{4\{,\}0\^2-1\{,\}6\^2\}/);
 assert.deepEqual(Array.from(q('4.127').svarEnhet),['Nm','N','m',null]);assert.equal(q('4.507').svarEnhet,'cm');
 assert.doesNotMatch(q('4.130').spelDelar[3].t,/1,5 m/);assert.doesNotMatch(q('4.249').spelDelar[0].t,/F₂|1,2 m/);
 assert.doesNotMatch(q('4.304').spelDelar[0].fraga,/tråden/);assert.match(q('4.515').t,/grepp/);
});
test('Alla 76 numeriska slutsvar i lösningsförslagen stämmer med beräkningarna',()=>{
 let checked=0;
 for(const[id,expected]of cases){const t=q(id),vs=Array.isArray(expected)?expected:[expected];
  vs.forEach((v,i)=>{const part=t.spelDelar?t.spelDelar[i]:t,cardId=t.spelDelar?id+String.fromCharCode(97+i):id;
   const math=[...part.s.matchAll(/\\\[([\s\S]*?)\\\]/g)].map(x=>x[1]).join(' ');const hits=[...math.matchAll(/(?:\\approx|=)\s*(-?\d+(?:\{,\}\d+)?)(?:\\cdot10\^\{?(-?\d+)\}?)?/g)];
   const last=hits.at(-1),shown=last?Number(last[1].replace('{,}','.'))*10**Number(last[2]||0):NaN;
   const tol=Array.isArray(t.tolerans)?t.tolerans[i]:t.tolerans;
   assert.ok(Number.isFinite(shown),`Ingen kontrollerbar slutsiffra i ${cardId}`);
   assert.ok(Math.abs(shown-v)<=tol+Number.EPSILON*32*Math.max(Math.abs(v),Math.abs(shown)),`${cardId}: facit visar ${shown}, fysisk beräkning ${v} ± ${tol}`);checked++;
  });
 }
 assert.equal(checked,76);
});
