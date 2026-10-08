'use strict';
const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('node:fs'),vm=require('node:vm'),path=require('node:path');
const c={window:{}};vm.runInNewContext(fs.readFileSync(path.join(__dirname,'../uppgifter.js'),'utf8'),c);
const q=id=>c.window.BANK.find(x=>x.id===id),g=9.82,sin=d=>Math.sin(d*Math.PI/180),cos=d=>Math.cos(d*Math.PI/180),tan=d=>sin(d)/cos(d),asin=v=>Math.asin(v)*180/Math.PI,atan=v=>Math.atan(v)*180/Math.PI;
const down=(d,mu)=>g*(sin(d)-mu*cos(d)),brake=(d,mu)=>g*(sin(d)+mu*cos(d));
const f583=18-5*g*sin(15),mu583=f583/(5*g*cos(15)),m586=136.8/(g*sin(20));
const a610=down(25,.19),b610=brake(25,.19),s610=3**2/(2*b610);
const b614=brake(30,.12),a614=down(30,.12),s614=5**2/(2*b614);
const b616=brake(35,.14),s616=2.5/sin(35),v619=Math.sqrt(2*g*sin(30)*8);
const s629=1230*g*sin(25)/cos(31),m631=40/(g*tan(35));
// Givens transcribed during manual review; calculations do not read answers or solution HTML.
const cases=[
 ["4.45",[(5*g),((5*g)*cos(15)),((5*g)*sin(15))]],
 ["4.46",[asin((0.7/2)),tan(asin((0.7/2)))]],
 ["4.47",down(25,0.4)],
 ["4.59",[((15*g)*sin(20)),((15*g)*cos(20))]],
 ["4.392",down(30,0.17)],
 ["4.393",-brake(15,0.19)],
 ["4.394",((sin(18)-(1/g))/cos(18))],
 ["4.124",[((30*g)*sin(15)),(((0.25*30)*g)*cos(15)),((30*g)*(sin(15)+(0.25*cos(15))))]],
 ["4.176",[((12*g)*sin(20)),tan(20)]],
 ["4.397",atan(0.25)],
 ["4.318",down(15,0.4)],
 ["4.319",((4**2)/(2*brake(32,0.28)))],
 ["4.320",(9.5*down(38,0.35))],
 ["4.321",tan(27)],
 ["4.485",((5*g)*sin(30))],
 ["4.486",((8*g)*cos(20))],
 ["4.487",(g*sin(15))],
 ["4.489",((12*g)*sin(25))],
 ["4.490",((g*sin(10))*3)],
 ["4.492",(40/(g*sin(35)))],
 ["4.578",[((105*g)*cos(22)),((105*g)*sin(22)),tan(22)]],
 ["4.579",[((0.18*g)*cos(15)),((0.18*g)*sin(15)),tan(15)]],
 ["4.580",[(((0.35*75)*g)*cos(28)),(75*brake(28,0.35))]],
 ["4.581",tan(38)],
 ["4.582",[((2*g)*sin(10)),down(35,0.36),atan(0.36)]],
 ["4.583",[f583,mu583,down(15,mu583)]],
 ["4.584",[((55*g)*sin(20)),(55*brake(20,0.35))]],
 ["4.585",[(g*sin(25)),down(25,0.15),tan(25)]],
 ["4.586",[m586,(20/((m586*g)*cos(20)))]],
 ["4.587",((1200*g)*sin(12))],
 ["4.588",atan(0.85)],
 ["4.589",down(29,0.18)],
 ["4.590",[((80*g)*sin(15)),tan(15)]],
 ["4.591",(85*(1.1+(g*sin(14))))],
 ["4.592",atan(1.2)],
 ["4.593",[(30*brake(30,0.3)),(30*(brake(30,0.3)+0.5))]],
 ["4.594",(brake(40,0.13)-(0.13*g))],
 ["4.595",((7/5)*tan(15))],
 ["4.600",(((40*g)*(sin(30)+(0.4*cos(30))))/(cos(30)-(0.4*sin(30))))],
 ["4.601",(((250*cos(27))-((29*g)*sin(27)))/(((29*g)*cos(27))+(250*sin(27))))],
 ["4.602",((2*g)*((sin(37)/0.5)-cos(37)))],
 ["4.603",(((100*g)*(sin(35)+(0.65*cos(35))))/(cos(20)+(0.65*sin(20))))],
 ["4.604",[(0.2*(((100*g)*cos(15))-(600*sin(20)))),((((600*cos(20))-((100*g)*sin(15)))-(0.2*(((100*g)*cos(15))-(600*sin(20)))))/100)]],
 ["4.605",[(10*down(45,0.5)),(10*brake(45,0.5))]],
 ["4.606",(down(35,0.1)*5)],
 ["4.607",Math.sqrt(((2*50)/down(20,0.1)))],
 ["4.608",Math.sqrt(((2*9)/down(8,0.06)))],
 ["4.609",asin((((2*(18-(2*3.3)))/(3.3**2))/g))],
 ["4.610",[a610,s610,((3/b610)+Math.sqrt(((2*s610)/a610)))]],
 ["4.611",(22*((((60/3.6)**2)/(2*75))-down(6,0.1)))],
 ["4.612",[Math.sqrt((((2*g)*sin(37))*5)),Math.sqrt(((2*down(37,0.25))*5))]],
 ["4.613",((3**2)/(2*brake(30,0.4)))],
 ["4.614",[(5/b614),s614,Math.sqrt(((2*a614)*s614))]],
 ["4.615",(Math.sqrt((((6/3.6)**2)+((2*down(50,0.12))*45)))*3.6)],
 ["4.616",[Math.sqrt(((21**2)-((2*b616)*s616))),Math.sqrt(((2*b616)*s616))]],
 ["4.617",((((10**2)/(2*14.2))-(g*sin(20)))/(g*cos(20)))],
 ["4.618",[Math.sqrt(((8**2)-((2*g)*1.8))),Math.sqrt((((8**2)-((2*g)*1.8))-(((2*80)/98)*8)))]],
 ["4.619",[((v619**2)/((2*0.4)*g)),((v619/(g*sin(30)))+(v619/(0.4*g)))]],
 ["4.620",[((42**2)/(2*brake(9,0.98))),((42**2)/((2*g)*((0.98*cos(9))-sin(9))))]],
 ["4.621",(20/(((20/sin(20))*cos(20))+45))],
 ["4.622",(((5**2)+((2*down(28,0.18))*110))/((2*0.15)*g))],
 ["4.623",[(850*sin(22)),(850*cos(22)),(g*sin(22))]],
 ["4.624",[((95*g)*cos(10)),(g*sin(10))]],
 ["4.625",[((67*g)*sin(8)),(g*sin(8))]],
 ["4.626",(100/(g*sin(20)))],
 ["4.627",asin((0.86/3.95))],
 ["4.628",(((2*g)*sin(53))/845)],
 ["4.629",[s629,(((1230*g)*cos(25))-(s629*sin(31)))]],
 ["4.631",[m631,(((m631*g)*cos(35))+(40*sin(35)))]],
 ["4.633",[Math.sqrt(((2*50)/(g*sin(13)))),Math.sqrt((((2*g)*sin(13))*50))]],
 ["4.634",Math.sqrt(((12**2)-((2*g)*2.5)))],
 ["4.635",[asin((((19**2)/(2*40))/g)),((19**2)/((2*g)*sin(20)))]]
];
function check(id,expected){const t=q(id),want=Array.isArray(expected)?expected:[expected],got=Array.isArray(t.rättSvar)?t.rättSvar:[t.rättSvar];assert.equal(want.length,got.length,id);want.forEach((v,i)=>{const tol=Array.isArray(t.tolerans)?t.tolerans[i]:t.tolerans;assert.ok(Math.abs(v-got[i])<=tol+Number.EPSILON*32*Math.max(Math.abs(v),Math.abs(got[i])),`${id} del ${i}: ${v} jämfört med ${got[i]} ± ${tol}`);});}
test('Lutande plan: samtliga 72 numeriska huvuduppgifter räknas självständigt',()=>{
 const tasks=c.window.BANK.filter(t=>t.kap===4&&t.omr==='lutande_plan'&&t.rättSvar!=null);assert.equal(tasks.length,72);assert.deepEqual(new Set(cases.map(x=>x[0])),new Set(tasks.map(x=>x.id)));for(const[id,v]of cases)check(id,v);
});
test('Elevkortens egna avrundade givna värden ger svar inom rättningens tolerans',()=>{
 for(const[id,v]of [['4.583',[f583,5.292/(5*g*cos(15)),down(15,.11)]],['4.586',[m586,20/(40.7*g*cos(20))]],['4.593',[30*brake(30,.3),224+30*.5]],['4.604',[.2*(100*g*cos(15)-600*sin(20)),(600*cos(20)-100*g*sin(15)-149)/100]],['4.629',[s629,1230*g*cos(25)-5960*sin(31)]]])check(id,v);
});
test('Startfart, avrundning och kraftbalans finns på det fristående kortet',()=>{
 assert.match(q('4.610').spelDelar[2].t,/3,0 m\/s/);assert.match(q('4.610').spelDelar[2].s,/t_\{\\text\{upp\}\}/);
 assert.match(q('4.631').spelDelar[1].s,/40cos35/);assert.doesNotMatch(q('4.631').spelDelar[1].t,/5,8 kg/);
 assert.match(q('4.616').spelDelar[1].t,/2,50 m/);assert.doesNotMatch(q('4.616').spelDelar[1].t,/21,0 m\/s/);
 assert.doesNotMatch(q('4.635').spelDelar[1].t,/andra backen/);assert.match(q('4.635').spelDelar[1].t,/19,0 m\/s/);
 assert.match(q('4.47').s,/0\{,\}590/);assert.match(q('4.124').spelDelar[0].s,/76\{,\}2/);
 assert.match(q('4.614').spelDelar[1].ledtrad,/v_0/);assert.doesNotMatch(q('4.490').ledtrad,/Vagnen/);
 assert.doesNotMatch(q('4.491').ledtrad,/deler/);assert.doesNotMatch(q('4.590').spelDelar[1].ledtrad,/μ|mu/);
});
test('Facits numeriska slutsvar stämmer med de självständiga beräkningarna',()=>{
 const direct={'4.45a':/=([\d]+\{,\}[\d]+)\\,\\mathrm N/,'4.485':/Svar med tre värdesiffror: ([\d]+,[\d]+)/,'4.593b':/=([\d]+)\\,\\mathrm N/,'4.619a':/=([\d]+\{,\}[\d]+)\\,\\mathrm m/,'4.615':/Svar: ([\d]+,[\d]+) km\/h/};
 let checked=0;
 for(const[id,expected]of cases){const t=q(id),vs=Array.isArray(expected)?expected:[expected];
  vs.forEach((v,i)=>{const part=t.spelDelar?t.spelDelar[i]:t,cardId=t.spelDelar?id+String.fromCharCode(97+i):id;
   const hits=[...part.s.matchAll(/\\approx\s*(-?\d+(?:\{,\}\d+)?)(?:\\cdot10\^\{?(-?\d+)\}?)?/g)];
   const last=hits.at(-1),literal=direct[cardId]?.exec(part.s),shown=direct[cardId]?(literal?Number(literal[1].replace('{,}',',').replace(',','.')):NaN):(last?Number(last[1].replace('{,}','.'))*10**Number(last[2]||0):NaN);
   const tol=Array.isArray(t.tolerans)?t.tolerans[i]:t.tolerans;
   assert.ok(Number.isFinite(shown),`Ingen kontrollerbar slutsiffra i ${cardId}`);
   assert.ok(Math.abs(shown-v)<=tol+Number.EPSILON*32*Math.max(Math.abs(v),Math.abs(shown)),`${cardId}: facit visar ${shown}, fysisk beräkning ${v} ± ${tol}`);checked++;
  });
 }
 assert.equal(checked,113);
});
