'use strict';
const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('node:fs'),vm=require('node:vm'),path=require('node:path');
const c={window:{}};vm.runInNewContext(fs.readFileSync(path.join(__dirname,'../uppgifter.js'),'utf8'),c);
const q=id=>c.window.BANK.find(x=>x.id===id),g=9.82,sin=d=>Math.sin(d*Math.PI/180),cos=d=>Math.cos(d*Math.PI/180),asin=v=>Math.asin(v)*180/Math.PI,atan=v=>Math.atan(v)*180/Math.PI;
const degrees=v=>v*180/Math.PI;
// Givna värden har lästs från frågorna; uttrycken läser aldrig rättSvar eller facit.
const cases=[
 ["4.333",((0.5*200)*(0.06**2))],
 ["4.339",(((0.5*200)*(0.1**2))/((0.22*1.4)*g))],
 ["4.342",Math.sqrt(((2*(((0.5*260)*(0.13**2))-(((0.22*2)*g)*0.13)))/2))],
 ["5.4",[((0.5*250)*(0.12**2)),Math.sqrt(((250*(0.12**2))/0.05)),(((0.5*250)*(0.12**2))/(0.05*g))]],
 ["5.11",[((0.5*900)*(0.18**2)),((((0.5*900)*(0.18**2))/(0.35*g))-0.18)]],
 ["5.20",[((45*80)/1000),(5400/45)]],
 ["5.23",[42,(42/(3*g)),(32/(2.4*g))]],
 ["5.294",(((20*g)*2)+(39.28*5))],
 ["5.38",(((0.5*6)*60)+(4*60))],
 ["5.45",[((0.8*g)*15),((0.8*g)*30),((0.8*g)*(30-15))]],
 ["5.46",[(80*15),(600/4),(2400/300)]],
 ["5.53",[((8*g)*2.4),((8*g)*2.4),(((8*g)*2.4)/12)]],
 ["5.57",[(((3.7*10)*3600)/1000),(((3.7*10)*3600)/(70*g))]],
 ["5.62",[((((-0.3*20)*g)*cos(10))*12),(((20*g)*12)*sin(10)),(((20*g)*12)*(sin(10)+(0.3*cos(10))))]],
 ["5.65",[(360000000.0/180000.0),0]],
 ["5.66",[((180*cos(35))*6),(180*6)]],
 ["5.67",[((250*40)/1000),((500*40)/1000),((250*20)/1000)]],
 ["5.71",[0,((4*g)*0.75),((4*g)*0.75),((4*g)*(0.75+0.4))]],
 ["5.72",[(25*g),((25*g)*1.8),((((12*25)*g)*1.8)/1000)]],
 ["5.183",(15*2.4)],
 ["5.184",((-500*25)/1000)],
 ["5.186",((15*((10*20)/0.5))/1000)],
 ["5.188",((20*0.82)*16)],
 ["5.189",[(178*3),(534/120),(534/2.5)]],
 ["5.192",((22*g)*0.45)],
 ["5.193",((((75+15)*g)*28)/1000)],
 ["5.194",[(((120*g)*5)/1000),((((0.55*120)*g)*5)/1000)]],
 ["5.195",(((175*g)*2.2)/1000)],
 ["5.197",(550/(g*1.5))],
 ["5.198",((4.5*g)*(1.75-0.95))],
 ["5.200",((0.4*g)*((0.13/2)-0.035))],
 ["5.207",degrees(Math.acos((212.5/(85*5))))],
 ["5.208",((((240*cos(30))*1.5)*10)/1000)],
 ["5.209",[(100*5),((100*cos(30))*5),((15*g)*5)]],
 ["5.211",[(((18*g)*sin(20))+40),(((((18*g)*sin(20))+40)*26)/1000)]],
 ["5.230",(((0.5*35)*0.1)+(35*0.05))],
 ["5.231",(((400+100)/2)*(24-2))],
 ["5.233",((0.5*25)*(0.45**2))],
 ["5.234",((-0.5*25)*(0.45**2))],
 ["5.236",(((2*13.4)/(0.0237**2))/1000)],
 ["5.334",(40*3)],
 ["5.335",(12*0.5)],
 ["5.336",((2*g)*5)],
 ["5.337",((0.5*g)*1.2)],
 ["5.340",((0.5*200)*(0.1**2))],
 ["5.341",((0.5*80)*(0.2**2))],
 ["5.344",(-5*2)],
 ["5.345",(-3*4)],
 ["5.346",(180/6)],
 ["5.347",(100/25)],
 ["5.348",((0.25*g)*2)],
 ["5.349",(58.92/(2*g))],
 ["5.353",((0.5*400)*(0.05**2))],
 ["5.354",Math.sqrt(((2*4)/200))],
 ["5.355",((2*2)/(0.1**2))],
 ["5.358",(40*5)],
 ["5.359",((0.5*0.3)*60)],
 ["5.360",((50*4)+((0.5*2)*50))],
 ["5.361",((30*2)+(60*1))],
 ["5.497",[((52*g)*80),(((10*150)*g)*1.2),(1590/(g*2.45)),((66.2*g)*(2260-1270))]],
 ["5.498",[(((65*g)*125)/(80*4186)),(((0.2*280)*4186)/(75*g)),Math.ceil((((0.2*280)*4186)/(20*0.45)))]],
 ["5.499",[((65*g)*-85),((65*g)*(4420-(-85))),(1600000.0/(65*g))]],
 ["5.500",[(((72*g)*1200)*sin(4.3)),(((20*g)*3)*(1-cos(45))),degrees(Math.acos((1-(4500/((600*g)*8)))))]],
 ["5.501",[((1202*g)*40),(((1202-801)*g)*40)]],
 ["5.502",(((0.5*88)*(0.04**2))/(0.04*g))],
 ["5.520",[(18*3.2),(500*25),(((0.5*46)*g)*10.3),((24*0.65)*18)]],
 ["5.521",(15*(((10*20)/0.5)+60))],
 ["5.522",(1200000.0/((0.61*800)*g))],
 ["5.523",[(165*2.8),(462/140),(462/1.8)]],
 ["5.524",[((0.5*113)*(15**2)),((0.5*1300)*(21.5**2))]],
 ["5.525",[((18*g)*0.65),(((75+15)*g)*28),((-175*g)*2.2),(620/(g*1.8))]],
 ["5.526",[((-120*g)*5),(((0.55*120)*g)*5)]],
 ["5.527",[((6.2*g)*(1.9-0.82)),((0.35*g)*((0.11/2)-0.04)),(((25*g)*0.15)*((((0+1)+2)+3)+4))]],
 ["5.528",[(72*g),((72*g)*0.65),((-72*g)*0.65)]],
 ["5.529",[((70*cos(35))*5.5),((85*cos(60))*5),(((240*cos(30))*1.5)*10)]],
 ["5.530",[((18*g)*sin(20)),(((18*g)*sin(20))*26),((((18*g)*sin(20))+40)*26)]],
 ["5.531",[((((0.25*15)*g)*cos(28))*1.2),(((15*g)*sin(28))*1.2)]],
 ["5.532",[((150*g)*1),degrees(Math.asin((1/5))),(((150*g)*1)/5),((150*g)*1)]],
 ["5.533",[((0.03*0.25)*g),(25/(0.03*g)),((0.5*0.25)*(25**2))]],
 ["5.534",[((40*cos(30))*4.5),((0.25*((5*g)-(40*sin(30))))*4.5)]],
 ["5.535",[((0.5*32)*(0.38**2)),((0.5*150)*((0.3**2)-(0.1**2))),((2*13.4)/(0.0237**2))]],
 ["5.619",(-6*3)],
 ["5.621",0],
 ["5.622",(20*(5-2))]
];
function check(id,expected){const t=q(id),want=Array.isArray(expected)?expected:[expected],got=Array.isArray(t.rättSvar)?t.rättSvar:[t.rättSvar];assert.equal(want.length,got.length,id);want.forEach((v,i)=>{const tol=Array.isArray(t.tolerans)?t.tolerans[i]:t.tolerans;assert.ok(Math.abs(v-got[i])<=tol+Number.EPSILON*32*Math.max(Math.abs(v),Math.abs(got[i])),`${id} del ${i}: ${v} jämfört med ${got[i]} ± ${tol}`);});}
test('Arbete: samtliga 84 numeriska uppgifter räknas självständigt',()=>{
 const tasks=c.window.BANK.filter(t=>t.kap===5&&t.omr==='arbete'&&(typeof t.rättSvar==='number'||Array.isArray(t.rättSvar)));assert.equal(tasks.length,84);assert.deepEqual(new Set(cases.map(x=>x[0])),new Set(tasks.map(x=>x.id)));for(const[id,v]of cases)check(id,v);
});
test('Enskilda energikort har rätt egna givens och frågar efter ett entydigt svar',()=>{
 assert.doesNotMatch(q('5.4').spelDelar[2].t,/vågrätt|Samma anordning/);
 assert.match(q('5.4').spelDelar[2].t,/50 g/);assert.ok(q('5.4').spelDelar[2].s.includes('0{,}050'));
 assert.match(q('5.57').spelDelar[1].t,/133,2 kJ/);assert.doesNotMatch(q('5.57').spelDelar[1].t,/mAh/);
 assert.ok(q('5.53').spelDelar[1].s.includes(String.raw`8{,}0\cdot9{,}82`));
 assert.match(q('5.498').spelDelar[0].t,/andel/);assert.match(q('5.498').spelDelar[2].t,/hela lyft/);
 assert.equal(q('5.498').rättSvar[2],26047);assert.equal(q('5.498').tolerans[2],0);
 assert.doesNotMatch(q('5.527').spelDelar[0].ledtrad,/0,80/);
 assert.ok(q('5.525').rättSvar[2]<0);assert.ok(q('5.526').rättSvar[0]<0);
});
test('Alla 151 numeriska slutsvar i lösningsförslagen stämmer med beräkningarna',()=>{
 let checked=0;
 for(const[id,expected]of cases){const t=q(id),vs=Array.isArray(expected)?expected:[expected];
  vs.forEach((v,i)=>{const part=t.spelDelar?t.spelDelar[i]:t,cardId=t.spelDelar?id+String.fromCharCode(97+i):id;
   const math=[...part.s.matchAll(/\\\[([\s\S]*?)\\\]|\\\(([\s\S]*?)\\\)/g)].map(x=>x[1]||x[2]).join(' ');const hits=[...math.matchAll(/(?:\\approx|=)\s*([-+]?\d+(?:\{,\}\d+)?)(?:\\cdot10\^\{?([-+]?\d+)\}?)?/g)];
   const last=hits.at(-1),shown=last?Number(last[1].replace('{,}','.'))*10**Number(last[2]||0):NaN;
   const tol=Array.isArray(t.tolerans)?t.tolerans[i]:t.tolerans;
   assert.ok(Number.isFinite(shown),`Ingen kontrollerbar slutsiffra i ${cardId}`);
   assert.ok(Math.abs(shown-v)<=tol+Number.EPSILON*32*Math.max(Math.abs(v),Math.abs(shown)),`${cardId}: facit visar ${shown}, fysisk beräkning ${v} ± ${tol}`);checked++;
  });
 }
 assert.equal(checked,151);
});
