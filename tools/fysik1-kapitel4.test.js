'use strict';
const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('node:fs'),vm=require('node:vm'),path=require('node:path');
const c={window:{}};vm.runInNewContext(fs.readFileSync(path.join(__dirname,'../uppgifter.js'),'utf8'),c);const q=id=>c.window.BANK.find(x=>x.id===id),g=9.82;
// Givens independently transcribed during manual review. Do not extract numbers from the solution HTML.
const tyngdkraft=[
 ['4.347',15*4.2],['4.350',136.8/5.7],['4.24',[588/g,588/g*8.87]],['4.356',18*(7.4-3.7)],
 ['4.37',[24.6/3,3*g,24.6/g]],['4.187',[65*1.62,65*g,65]],['4.190',[78*3.71,g/3.71]],['4.208',[120*g,120*1.62,120,120*1.62]],
 ['4.467',5*g],['4.468',147/g],['4.470',1025*3.71/1000],['4.471',12*g],['4.472',196/g*1.62],['4.474',14.8/4],
 ['4.498',[4.9/g*1.62,4.9/g]],['4.503',.4*g/3.71],['4.504',60*g]
];
const normalkraft=[
 ['4.98',[12*g,12*g+40,12*g-40]],['4.115',[65*g,65*(g+1.5),65*(g-1.5)]],['4.207',[(.423-.257)*g,.423*g,.423*g/25*100]],
 ['4.475',8*g],['4.476',10*g+30],['4.477',10*g-40],['4.478',(1.2+.8)*g],['4.480',60*(g+1.5)],['4.481',55*(g-2)],
 ['4.482',72*g],['4.484',(715-65*g)/65],['4.497',70*(g-(1.5*2)/3)/g],['4.502',[20*g-80*Math.sin(Math.PI/6),20*g+80*Math.sin(Math.PI/6)]],
 ['4.636',[50*g,50*(g+5),50*(g-5)]],['4.637',21750/2125-g],['4.638',19000/(g-.75)/1000],['4.639',(163-14*g)/14],
 ['4.640',[4850*(g+.67)/1000,4850*(g-.67)/1000]],['4.641',3200*(g+.55/1.2)/1000],['4.642',Math.sqrt(2*1.8/(54/5-g))],
 ['4.644',[65*(g+10/4)/g,65*(g-10/3)/g]],['4.645',(.75-1)*g],['4.646',[7*(g+1.6),115/7-g]],
 ['4.647',[2*g/405,2*(g+3.2)/405,2*(g-2.5)/405]]
];
const newton3=[
 ['4.456',80],['4.460',.4],['4.463',150/50],['4.464',45/90],['4.465',2*3/3],['4.466',80*.75/40],['4.493',80/60],['4.494',2000/4],
 ['4.496',[6*(20/(4+6)),4*(20/(4+6))]],['4.501',[2*40000*.5/1000,40000*.5/1000]],['4.755',20]
];
for(const[area,cases]of [['tyngdkraft',tyngdkraft],['normalkraft',normalkraft],['newton3',newton3]])test(`Kapitel 4 ${area}: numeriska svar följer oberoende kraftberäkningar`,()=>{
 const tasks=c.window.BANK.filter(x=>x.kap===4&&x.omr===area&&x.rättSvar!=null);assert.equal(new Set(cases.map(x=>x[0])).size,tasks.length);
 for(const[id,expect]of cases){const task=q(id),a=Array.isArray(expect)?expect:[expect],b=Array.isArray(task.rättSvar)?task.rättSvar:[task.rättSvar];assert.equal(a.length,b.length,id);
 a.forEach((v,i)=>{const tol=Array.isArray(task.tolerans)?task.tolerans[i]:task.tolerans;assert.ok(Math.abs(v-b[i])<=(tol||0)+1e-10*Math.max(1,Math.abs(v)),`${id} del ${i}: ${v} jämfört med ${b[i]}`);});}
});
test('Kraftkort har egna givna värden och statisk friktion förväxlas inte med glidfriktion',()=>{
 assert.match(q('4.37').t,/24,6 N på jorden/);assert.match(q('4.207').spelDelar[2].t,/423 g/);assert.doesNotMatch(q('4.207').spelDelar[2].t,/257/);
 assert.match(q('4.98').spelDelar[2].t,/drar rakt uppåt/);assert.doesNotMatch(q('4.98').spelDelar[2].t,/trycker rakt nedåt|<svg/);
 assert.doesNotMatch(q('4.502').s,/friktionen är proportionell/);assert.match(q('4.494').t,/medelacceleration/);
 assert.equal(q('4.504').traningsniva,1);assert.equal(q('4.504').niva,'E');
});
const G=6.674e-11,G2=6.67e-11,sin=a=>Math.sin(a*Math.PI/180),cos=a=>Math.cos(a*Math.PI/180),deg=x=>x*180/Math.PI;
const springs=[
 ['4.323',80*.020],['4.324',15/.15],['4.325',18/450*100],['4.20',[.25*g,.25*g/.040,6/(.25*g/.04)*100,.25*10/4]],['4.326',140*.05],['4.327',9.6/((24-18)/100)],['4.328',15+12.6/180*100],['4.43',1.4*g/95*100],['4.63',[3*g,3*g,3*g/600*100,20-3*g/600*100]],['4.329',-200*.08],['4.64',[200*.15,45/.25,28/350]],['4.65',[12/.15,(12/.15)*.25,30/(12/.15)*100,(12/.15)*.2/g]],['4.73',[26-20,.5*g,.5*g/.06,20+6*1.2/.5]],['4.181',[.5*g,.5*g/30*100,.5*g/45*100,(.5*g/30+.5*g/45)*100]],['4.332',180/2],['4.334',120+220],['4.185',[.8*g,.8*g/120*100]],['4.212',120*.085/g],['4.336',1/(1/80-1/160)],['4.214',[24.5-18,.4*g/.065,.4*(27.75-18)/(24.5-18)]],['4.268',[1.2*g,1.2*g/85*100,24+1.2*g/85*100]],['4.338',220/(100+220)*100],['4.271',[75*g/6,75*g/6/.04,4*100/75]],['4.340',(35/140+35/220)*100],['4.273',[400*.06,400*.06/g,6*1.62/g]],['4.341',4*g/(170+260)*100],['4.274',[45/.25,2*45/.25]],['4.305',120/2],['4.306',1/(1/80+1/120)],['4.307',75+125],['4.308',100/2+50]
];
const gravity=[
 ['4.9',[G*4e24/(5e6)**2,G*4e24*70/(5e6)**2]],['4.346',G*50*80/1.5**2*1e9],['4.348',100/4**2],['4.351',Math.sqrt(9)],['4.354',100/(1+1)**2],['4.357',2/2**2*100],['4.362',g*(6370/(6370+350))**2],['4.363',4*Math.PI*G*3200*240000/3],['4.364',6.6*(3e6)**2/G],['4.365',6000*(1/Math.sqrt(.64)-1)],['4.367',Math.sqrt(G*1.2e24/5)/1000],['4.74',[6371+400,G*5.97e24*1200/(6.771e6)**2/1000,G*5.97e24*1200/(6.371e6)**2/1000]],['4.370',3/2**2*100],['4.372',3*.21/(4*Math.PI*G*220000)],['4.374',g*(6370/(6370+450))**2],['4.375',4*Math.PI*G*4000*280000/3],['4.378',6370*(1/Math.sqrt(.75)-1)],['4.379',85000/(1+Math.sqrt(1.6/5))],
 ['4.735',[G2*75*86/3.5**2,G2*25*40/.45**2,G2*120*32000/13**2]],['4.736',[G2*2.3e30*6.8e30/(8.8e11)**2,G2*1.67e-27*9.11e-31/(5.3e-11)**2]],['4.737',[Math.sqrt(G2*1*3/2.5e-10),Math.sqrt(G2*.04*5.5/1.2e-9)]],['4.738',Math.sqrt(8.8e-6*.24**2/G2)],['4.739',G2*5.977e24*95*(1/(6.357e6)**2-1/(6.378e6)**2)],['4.740',G2*5.97e24*78/(6.732e6)**2],['4.741',(1-(6370/6378.848)**2)*100],['4.742',[G2*7.35e22/(1.737e6)**2,G2*6.42e23/(3.39e6)**2,G2*4.87e24/(6.052e6)**2,G2*1.9e27/(6.99e7)**2]],['4.743',[G2*5.977e24*11600/(6.38e6)**2,G2*5.977e24*11600/(6.978e6)**2]],['4.744',G2*(11000/g)*(3400/g)/12**2],['4.745',G2*7.2*.38/(.11+.028)**2],['4.746',7.51e-11*.45**2/(.015*15)],['4.747',[10*.5,10/2**2]],['4.748',6370000*(Math.sqrt(2)-1)],['4.749',[4*Math.PI*G2*3500*9500/3,Math.sqrt(2/g),Math.sqrt(2/.0093)]],['4.750',3*.005/(4*Math.PI*G2*4830)],['4.751',[1000*2,1000*2/2**2,1000/2**2,1000*.5/.5**2,1000*1.8/1.5**2]],['4.752',2.34*g/(G2*6.42e23/(3.37e6)**2)],['4.753',[G2*50*(500-200),2/(1+Math.sqrt(200/500))]]
];
for(const[area,cases]of [['fjadrar',springs],['gravitation',gravity]])test(`Kapitel 4 ${area}: varje numeriskt svar kontrolleras från uppgiftens givna värden`,()=>{
 const tasks=c.window.BANK.filter(x=>x.kap===4&&x.omr===area&&x.rättSvar!=null);assert.equal(new Set(cases.map(x=>x[0])).size,tasks.length);
 for(const[id,expect]of cases){const t=q(id),a=Array.isArray(expect)?expect:[expect],b=Array.isArray(t.rättSvar)?t.rättSvar:[t.rättSvar];assert.equal(a.length,b.length,id);
 a.forEach((v,i)=>{const tol=Array.isArray(t.tolerans)?t.tolerans[i]:t.tolerans;assert.ok(Math.abs(v-b[i])<=(tol||0)+Number.EPSILON*16*Math.max(Math.abs(v),Math.abs(b[i])),`${id} del ${i}: ${v} jämfört med ${b[i]}`);});}
});
test('Avstånd kvadreras i gravitationsfacit och blykloten överlappar inte',()=>{
 assert.match(q('4.9').spelDelar[0].s,/\{\(5\{,\}0\\cdot10\^6\)\^2\}/);assert.match(q('4.348').s,/\\frac\{r\}\{4r\}/);assert.match(q('4.354').s,/\\frac\{R\}\{2R\}/);
 for(const id of ['4.379','4.385'])assert.match(q(id).s,/\\frac\{G M_\{2\}\}\{\(d-x\)\^2\}/);
 assert.match(q('4.746').t,/45,0 cm/);assert.match(q('4.746').t,/10\^\{-11\}/);
 assert.match(q('4.63').spelDelar[3].s,/\\frac\{29\{,\}46\}\{600\}/);
 assert.doesNotMatch(q('3.336').spelDelar[1].s,/komposanter från a/);
});
const newton1=[
 ['4.91',12*g/(2*cos(25))],['4.96',[30/g,30/cos(45)]],['4.97',[78*g/(cos(25)+sin(25)/sin(40)*cos(40)),78*g/(sin(40)/sin(25)*cos(25)+cos(40))]],['4.102',[75,82-82]],['4.175',[Math.hypot(50-25,60),deg(Math.atan(25/60))]],['4.230',[800*cos(30),0,2*800*cos(30)/1000,2*800*cos(30)/4000]],['4.236',[120*g/(sin(35)+cos(35)/cos(43)*sin(43)),120*g/(cos(43)/cos(35)*sin(35)+sin(43))]],['4.241',[35*g,35*g,35*g,2*35*g]],['4.303',[Math.hypot(10,24),Math.hypot(10,24)/2]],['4.313',120/cos(35)],['4.314',deg(Math.acos(85/130))],['4.315',150*sin(28)/cos(28)],['4.316',45*g/(2*sin(40))],['4.317',deg(Math.asin(72*g/1000))],['4.500',[4*g/(sin(30)+cos(30)/cos(60)*sin(60)),4*g/(cos(60)/cos(30)*sin(30)+sin(60))]],['4.671',[60*g,(100-60)*g,2*60*g]],['4.672',[4*g,(7-4)*g,2*4*g]],['4.673',20/((2+2+3+2)*g)],['4.674',g/50],['3.366',deg(Math.acos((60**2-30**2-40**2)/(2*30*40)))]
];
for(const[id,x,y]of [['3.286',4,2],['3.287',2,3],['3.288',-2,5],['3.289',4,-1],['3.290',2,-5],['3.291',-1,-5],['3.292',-3,2],['3.293',-2,-2]])newton1.push([id,[x,y,Math.hypot(x,y)]]);
for(const[id,a,b]of [['3.301',[-2,4],[2,-4]],['3.302',[-5,-1],[5,-1]],['3.303',[4,0],[-4,3]],['3.304',[4,1],[2,3]],['3.305',[3,3],[3,-2]],['3.306',[1,4],[-4,1]],['3.307',[3,3],[-1,-1]],['3.308',[-2,0],[0,-4]]])newton1.push([id,[a[0]+b[0],a[1]+b[1],Math.hypot(a[0]+b[0],a[1]+b[1])]]);
for(const[id,F,angle]of [['3.314',25,58],['3.315',17,25],['3.316',25,74],['3.321',23,135],['3.322',24,152],['3.323',11,221],['3.324',23,257],['3.325',27,303]])newton1.push([id,[F*cos(angle),F*sin(angle)]]);
for(const[id,x,y]of [['3.319',4,2],['3.327',-2,5],['3.328',2,-5],['3.329',-3,2],['3.331',6,4],['3.332',6,1],['3.338',-3,5],['3.339',-2,-4]])newton1.push([id,(deg(Math.atan2(y,x))+360)%360]);
for(const[id,F1,a1,F2,a2]of [['3.334',19,0,27,51],['3.335',19,0,27,129],['3.336',24,33,22,90],['3.337',18,0,18,225],['3.341',32,18,37,71],['3.342',23,65,21,141],['3.343',20,300,20,210],['3.344',330,52,361,341]]){const x=F1*cos(a1)+F2*cos(a2),y=F1*sin(a1)+F2*sin(a2);newton1.push([id,[Math.hypot(x,y),(deg(Math.atan2(y,x))+360)%360]]);}
test('Kapitel 4 newton1: samtliga numeriska svar kontrolleras från oberoende kraftbalanser och avlästa vektorer',()=>{
 const tasks=c.window.BANK.filter(x=>x.kap===4&&x.omr==='newton1'&&x.rättSvar!=null);assert.equal(new Set(newton1.map(x=>x[0])).size,tasks.length);
 for(const[id,expect]of newton1){const t=q(id),a=Array.isArray(expect)?expect:[expect],b=Array.isArray(t.rättSvar)?t.rättSvar:[t.rättSvar];assert.equal(a.length,b.length,id);
 a.forEach((v,i)=>{const tol=Array.isArray(t.tolerans)?t.tolerans[i]:t.tolerans;assert.ok(Math.abs(v-b[i])<=(tol||0)+Number.EPSILON*16*Math.max(Math.abs(v),Math.abs(b[i])),`${id} del ${i}: ${v} jämfört med ${b[i]}`);});}
});
