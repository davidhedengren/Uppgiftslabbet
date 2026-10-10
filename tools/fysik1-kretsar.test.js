'use strict';
const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('node:fs'),vm=require('node:vm'),path=require('node:path');
const c={window:{}};vm.runInNewContext(fs.readFileSync(path.join(__dirname,'../uppgifter.js'),'utf8'),c);const q=id=>c.window.BANK.find(x=>x.id===id),area=d=>Math.PI*(d/2)**2,wire=(rho,L,d)=>rho*L/area(d),near=(a,b,id)=>{if(b===null)return;if(Array.isArray(b)){b.forEach((v,i)=>near(a[i],v,id));return;}assert.equal(typeof a,'number',id);assert.ok(Math.abs(a-b)<=Math.abs(b)*1e-10+1e-30,id+': '+a+' / '+b);};
const r8=1.72e-8*50/1.5e-6,r28=wire(1.72e-8,8,.0005),r61=1.7e-8*2.5/(Math.PI*.0005**2),r84=1.72e-8*30/1e-6,i84=12/(6+r84),V424=1/8.96*1e-6,L424=Math.sqrt(V424/1.7e-8),A430=1.7e-8*50/(3/6.7),a433=area(.0008),l433=(.2/8960)/a433,r436cu=wire(1.7e-8,5,.0014),r436al=wire(2.7e-8,5,.0014),r437=1.7e-8*80/1.3e-6;
const cases=[
 ['8.1',Math.sqrt(2.4/1.7*3*8)],['8.188',6/4.7],['8.189',5.6*1.8],['8.190',12/2.6],['8.192',10/.45],
 ['8.8',[r8,10*r8,100*r8,null]],['8.28',[area(.0005),r28,3*r28]],['8.38',[1.5/400,230/.5]],['8.61',[r61,r61*.15]],['8.76',[[230/1e5*1e3,230/1e3*1e3],null,null]],['8.80',[1e-6,.17,.34,.085]],['8.82',[48,null,null]],['8.196',1.68e-8*16/.336*1e6],['8.198',.336*.5e-6/1.68e-8],['8.200',1.68e-8*14/.7e-6],['8.84',[24/12,r84,[i84*r84,12-i84*r84]]],['8.108',[null,null,(5.44-1.36)/(.08-.02)]],['8.113',2*Math.sqrt(1.6e-8*.25/.008/Math.PI)*1e3],['8.157',[230/.26,(230/.26)/30,230/30]],['8.158',[3,3/.03,null,null]],['8.201',3/.75],['8.175',12/30],['8.176',9/.25],['8.177',1.72e-8*20/2.5e-6],['8.178',4],['8.179',9/(6/.2)],['8.180',12/.075],['8.204',4],
 ['8.410',wire(1.6e-8,8,.0001)],['8.411',3*.5e-6/15],['8.412',10*area(.0004)/1.7e-8],['8.413',wire(1.7e-8,5.4,.0015)],['8.414',2*Math.sqrt(5.5e-8*1/.32/Math.PI)*1e3],['8.415',100*wire(2.7e-8,10,.0022)/wire(1.7e-8,24,.0018)],['8.416',[15*3/4,15/4]],['8.417',21*9],['8.418',.2*1.7/2.7],['8.419',.01*4],['8.420',2e6*(.025*.0002)/.2],['8.421',2.7e-8*1e4/4.9e-4],['8.422',1.7e-8*10/(Math.PI*(.025**2-.015**2))],['8.423',48/36],['8.424',[L424,2*Math.sqrt(V424/L424/Math.PI)*1e3]],['8.425',4.5*wire(2.7e-8,40,.0004)],['8.426',(12/4)*area(.00025)/1.7e-8],['8.427',3*wire(1.7e-8,.2,.001)],['8.428',3/wire(1e-6,.5,.0008)],['8.429',(1.5/.53)*area(.0006)/1.7e-8],['8.430',2*Math.sqrt(A430/Math.PI)*1e3],['8.431',75*2.4/3.1],['8.432',150*wire(2.7e-8,.02,.02)],['8.433',1.5/(1.7e-8*l433/a433)],['8.434',2700*175*(2.7e-8*175/(.3/125))],['8.435',[12*1.7/11.7,5*10/11.7]],['8.436',[r436cu+r436al,.095*r436al/(r436cu+r436al)]],['8.437',230/(15+r437)*r437],['8.438',((230-200)/(60/200))*area(.0004)/1.7e-8/2],['8.439',6*(1+.0038*(34-20))],['8.440',.12/.0043],['8.441',(43.7/38-1)/(55-20)],['8.442',20+(140/12-1)/.0045],['8.443',37+(-.15)/(-.044)],['8.444',100*.0045*(.07/.0034)],['8.472',(.25e-6*.04)*4100],['8.473',[.075/5e9,(.075/5e9)*.5/1.602e-19]],['8.474',9**2*(6*3600)/110e3]
];
test('Kretsar: numeriska svar följer oberoende beräkningar från frågornas givna data',()=>{for(const[id,value]of cases)near(q(id).rättSvar,value,id);assert.equal(cases.length,66);});
test('Fristående kort räknas från egna avrundade data',()=>{
 for(const[id,part,v]of[['8.8',1,.573*10],['8.8',2,.573*100],['8.28',1,1.72e-8*8/1.96e-7],['8.28',2,.701*3],['8.61',1,.0541*.15],['8.157',1,885/30],['8.424',1,2*Math.sqrt(1.116e-7/2.56/Math.PI)*1e3],['8.436',1,.095*.0877/(.0552+.0877)]])near(q(id).spelDelar[part].rättSvar,v,id);
 for(const id of ['8.8','8.28','8.61','8.76','8.80','8.82','8.84','8.157','8.158','8.416','8.424','8.435','8.436','8.473'])for(const p of q(id).spelDelar){assert.ok(p.t);assert.ok(p.ledtrad);assert.doesNotMatch(p.t,/från [ab]\)|föregående del|svaret ovan/);}
});
test('Diameterformlerna kvadrerar hela radien och lampan använder kabelns ström',()=>{
 for(const id of ['8.410','8.412','8.413','8.425','8.427','8.428','8.436'])assert.doesNotMatch(q(id).s,/10\^\{-3\\,2\}/);
 assert.match(q('8.84').s,/6,516/);assert.match(q('8.438').t,/ska bli 200 V/);assert.doesNotMatch(q('8.438').t,/högst/);
 assert.doesNotMatch(q('8.416').spelDelar[0].ledtrad,/fem/);assert.doesNotMatch(q('8.416').spelDelar[0].s,/3\{,\}75|3,75/);
 for(const id of ['8.196','8.198','8.200'])assert.match(q(id).t,/1,68·10⁻⁸/);
});
test('Rutinens nivå och lärarens grafarbete hålls isär',()=>{
 for(const id of ['8.188','8.189','8.190','8.192','8.175','8.176','8.195'])assert.equal(q(id).traningsniva,1);
 for(const id of ['8.28','8.61','8.177','8.179','8.180','8.432','8.442','8.443','8.444','8.474']){assert.equal(q(id).traningsniva,2);assert.equal(q(id).niva,'E');}
 for(const id of ['8.81','8.108'])assert.equal(q(id).spel,false);
 assert.deepEqual(Array.from(q('8.158').spelDelar,p=>p.etikett),['a','b','d']);assert.equal(q('8.440').svarFormat,'temperaturandring');
 const p=q('8.82').spelDelar[1];assert.equal(p.alternativ.filter(a=>a.ratt).length,3);
});
