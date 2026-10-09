const test=require('node:test'),assert=require('node:assert/strict'),fs=require('node:fs'),vm=require('node:vm'),path=require('node:path');
const c={window:{}};vm.runInNewContext(fs.readFileSync(path.join(__dirname,'../uppgifter.js'),'utf8'),c);
const q=id=>c.window.BANK.find(q=>q.id===id);
const cases=[
 ["7.85",()=>(.100*334)],
 ["7.86",()=>(50.1/334)],
 ["7.87",()=>(.420*334)],
 ["7.88",()=>(.075*2260)],
 ["7.89",()=>(.120*2260)],
 ["7.92",()=>(42.62/334)],
 ["7.94",()=>(83.5)],
 ["7.95",()=>(.180*397)],
 ["7.96",()=>(271.2/2260)],
 ["7.97",()=>(.060*840)],
 ["7.98",()=>(.200*571)],
 ["7.104",()=>(.4-339/2260)],
 ["7.106",()=>(452/2260)],
 ["7.132",()=>(16.7/.05)],
 ["7.133",()=>(66.8/(.1*334))],
 ["7.134",()=>(.050*2260)],
 ["7.54",()=>(.4*2260)],
 ["7.90",()=>(4000/5)],
 ["7.105",()=>(250*334/1000)],
 ["7.51",()=>(.8*334)],
 ["7.14",()=>(.25*334+.25*4.18*20)],
 ["7.108",()=>(.1*2260+.1*4.18*60)],
 ["7.21",()=>(1*(4.18*20+334+2.1*18))],
 ["7.99",()=>(.23*(2.1*14+334+4.18*30))],
 ["7.15",()=>(.8*(2.1*10+334+4.18*100+2260)/1000)],
 ["7.199",()=>(5*(334+4.18*30)*1000)],
 ["7.100",()=>(100/(.4*334)*100)],
 ["7.101",()=>(-10)],
 ["7.114",()=>((.220-42.62/334)*1000)],
 ["7.107",()=>((.2-(50-.2*2.1*10)/334)*1000)],
 ["7.111",()=>((80-.2*(2.1*10+334))/(.2*4.18))],
 ["7.109",()=>(334/(2.1*10+334+4.18*20)*100)],
 ["7.117",()=>(.65*.2*334)],
 ["7.23",()=>(.024759*(2.1*15+334))],
 ["7.24",()=>(20.9/(334+4.18*5)*1000)],
 ["7.103",()=>(500*240/1000/.3)],
 ["7.113",()=>(.3*2260000/(.78*1500)/60)],
 ["7.116",()=>(.36*2260/(1800*540/1000)*100)],
 ["7.119",()=>((.8*1000*240/1000)/(.8-.715))],
 ["7.213",()=>(.75*(2200*15+334000)/(.8*400))],
 ["7.196",()=>(Math.sqrt(2*(450*1643+276000)))],
 ["7.201",()=>(.5*.5*64*7.5**2/334000)],
 ["7.205",()=>(.055*250**2/2/334000)],
 ["7.206",()=>(Math.sqrt(2*(130*307+23000)))],
 ["7.207",()=>(334000/9.82)],
 ["7.214",()=>(.55*3*9.82*15/334000)],
 ["7.217",()=>(.060*9.82*(2-1.8)/334000)],
 ["7.112",()=>((0.41*4.18*35-0.13*(2.1*15+334))/((0.41+0.13)*4.18))],
 ["7.220",()=>((0.25*4.18*18-0.04*(2.2*18+334))/((0.25+0.04)*4.18))],
 ["7.115",()=>((.2-(.2*4.18*20-.2*2.1*10)/334)*1000)],
 ["7.204",()=>(60*3.5/334)],
 ["7.216",()=>(.4*.9*30/334)],
 ["7.219",()=>(.25*.385*130/334)],
 ["7.202",()=>(.0056*.002*917*334000/(700*.0056))],
 ["7.211",()=>(2.2*10**6*.12*917*334000)],
 ["7.215",()=>(300*6*3600/(334000*917))],
 ["7.203",()=>(50*(4180*10+334000)/1200/3600)],
 ["7.195",()=>((270-0.45*4.18*(100-80))/2260)],
 ["7.210",()=>((1000-2*4.18*(100-20))/2260)],
 ["7.200",()=>((100-.6*4.18*20)/334)],
 ["7.212",()=>(1.2-(627*1200/1000-1.2*4.18*85)/2260)],
 ["7.208",()=>(120*2260/(4.18*100))],
 ["7.190",()=>([1.2*397000,.025*840000])],
 ["7.191",()=>([.055*(450*(1538-25)+276000),.018*(2200*18+334000),100/(4.18*(100-21)+2260)])],
 ["7.192",()=>(.04*(2200*10+334000+4180*100+2260000+2080*10))],
 ["7.193",()=>(340/213)],
 ["7.194",()=>([100/(.235*947+105),100/(.13*1049+64)])],
 ["7.6",()=>([1.8*4.18*(100-18),1.8*2260/1000])],
 ["7.16",()=>([.08*2.1*6,.08*334,(.08*2.1*6+.08*334)*1000/150/60])],
 ["7.22",()=>([.005*2260,11.3/(.2*4.18)])],
 ["7.25",()=>([2*.9*640/1000,2*397/1000,1.152+.794])],
 ["7.26",()=>([.08*.235*942,.08*(.235*942+105)])],
 ["7.102",()=>([.1*4.18*80,(.1*2260)/(.1*4.18*80)])],
 ["7.45",()=>([3*4.18*5,3*334,3*2.1*3,(62.7+1002+18.9)/1000])],
 ["7.46",()=>([.12*334+.37*4.18*18,(.12*334+.37*4.18*18)/(800*210/1000)*100])],
 ["7.49",()=>([1.5*2260/1000,1.5*2260000/(.75*1800)/60])],
 ["7.52",()=>([80,210,40/.2,40/.2])],
 ["7.197",()=>([.5*(220**2-160**2)/2/130,20+.5*(220**2-160**2)/2/130])],
 ["7.198",()=>([.25*4180*80/105,(83600/105*120-83600)/2260000])],
 ["7.209",()=>([.2*(4180*16+334000)/100,(.2*(4180*16+334000)+.2*385*16)/100])],
 ["7.218",()=>([(0.664*4.18*20-0.1*(2.2*0+334))/((0.664+0.1)*4.18),.04*334/(4.18*10),.2*4.18*20/334])],
 ["7.221",()=>([(.05*(2260+4.18*100)+5*4.18*11)/((5+.05)*4.18),.5*334/(2260+4.18*100),(2260+4.18*50)/(334+4.18*50)])],
 ["7.222",()=>(8*(2260+4.18*50)/(4.18*35))],
 ["7.223",()=>([(0.2*4.18*35-0.065*(2.2*8+334))/((0.2+0.065)*4.18),.065*(2.2*8+334)/(4.18*35)])],
 ["7.224",()=>([.056*(105+.235*(962-20))/(4.18*(20-10)),.056*(105+.235*(962-100))/(4.18*(100-10)+2260)])],
 ["7.131",()=>(0)],
];
test('Fasändring: självrättningens svar följer 86 beräkningsmodeller från givna värden',()=>{
 let fields=0;
 for(const[id,f]of cases){const t=q(id),raw=f(),xs=Array.isArray(raw)?raw:[raw];
 const vs=Array.isArray(t.rättSvar)?t.rättSvar:[t.rättSvar];assert.equal(vs.length,xs.length,id);
 xs.forEach((v,i)=>{assert.ok(Math.abs(v-vs[i])<=1e-12*Math.max(Math.abs(v),1e-12),id+' del '+i+' '+vs[i]+' / '+v);fields++;});}
 assert.equal(fields,115);
});
function written(part){
 const s=part.s.replace(/<[^>]*>/g,' ').replace(/\{,\}/g,'.').replace(/\\cdot\s*10\^\{(-?\d+)\}/g,'e$1');
 const m=s.split('Svar:').at(-1).match(/([−+-]?\d+(?:[ \u00a0]\d{3})*(?:[,.]\d+)?)(?:e([+-]?\d+))?/);
 return m?Number(m[1].replace(/\s/g,'').replace('−','-').replace(',','.'))*10**Number(m[2]||0):NaN;
}
function rounding(t,x){
 const words={en:1,två:2,tre:3,fyra:4,fem:5,sex:6};
 let m=t.match(/(\d+|en|två|tre|fyra|fem|sex) decimal/),d=m?(words[m[1]]??Number(m[1])):null;
 if(d===null&&t.includes('heltal'))d=0;
 if(d===null){m=t.match(/(\d+|två|tre|fyra) värdesiffror/);if(!m)return null;const sf=words[m[1]]??Number(m[1]);d=sf-1-Math.floor(Math.log10(Math.abs(x)));}
 const scale=10**(-d);return Math.sign(x)*Math.floor(Math.abs(x)/scale+0.5+1e-10)*scale;
}
test('Fasändring: skrivna slutsvar har den avrundning som frågan ber om',()=>{
 const failures=[];let fields=0;
 for(const[id,f]of cases){const t=q(id),raw=f(),xs=Array.isArray(raw)?raw:[raw];
 xs.forEach((v,i)=>{const part=t.spelDelar?t.spelDelar[i]:t,shown=written(part),want=rounding(part.fraga||part.t,v);
 const tol=Array.isArray(t.tolerans)?t.tolerans[i]:t.tolerans;
 if(want===null ? Math.abs(shown-v)>tol+1e-12 : Math.abs(shown-want)>1e-10*Math.max(Math.abs(want),1e-12))failures.push({id,part:i,shown,want});fields++;});}
 assert.equal(fields,115);assert.deepEqual(failures,[]);
});

test('Fasändring: varje delkort har egen fråga och en egen förklaring',()=>{
 const tasks=c.window.BANK.filter(q=>q.omr==='fasandring');assert.equal(tasks.length,103);
 for(const t of tasks){assert.doesNotMatch(t.s,/<ol|facit-steglista/);
  for(const d of t.spelDelar||[]){assert.ok(d.t&&d.s,t.id);assert.doesNotMatch(d.t,/samma tid|svaret i|från [a-c]\)/i,t.id);}
 }
});
test('Fasändring: begrepp besvaras genom val av text, inte sifferkoder',()=>{
 const ids=['7.5','7.91','7.93','7.110','7.48','7.129','7.130','7.135','7.136'];
 for(const id of ids){const t=q(id);assert.equal(t.svarstyp,'alternativ',id);assert.equal(t.rättSvar,null,id);assert.equal(t.alternativ.filter(a=>a.ratt).length,1,id);}
});
test('7.224: förångande vatten kyler silvret till 100 °C och det nya svaret följer energibalansen',()=>{
 const t=q('7.224');assert.match(t.spelDelar[1].t,/kyls till 100 °C/);
 const m=t.rättSvar[1];assert.ok(Math.abs(m*(4180*90+2260000)-.056*(105000+235*862))<1e-8);
 // Den tidigare modellen svalnade till 20 °C genom förångning vid 100 °C.
 const old=.056*(105000+235*942)/(4180*90+2260000);
 assert.ok(Math.abs(old-m)>t.tolerans[1]);
});
test('7.118: stora mängder kall is kan frysa allt vatten och ge temperatur under noll',()=>{
 const m=20,mw=.5,available=mw*(4.18*30+334),threshold=available/(2.1*10);
 assert.ok(threshold>10.93&&threshold<10.94);
 const T=(available-m*2.1*10)/(2.1*(m+mw));assert.ok(T<0&&T>-10);
 assert.match(q('7.118').s,/sluttemperaturen kan bli lägre än 0 °C/);
});
test('Fasändring: lärarbladets deluppgifter och energienheter är tydliga',()=>{
 const t=q('7.45').t;assert.match(t,/<strong>a\)<\/strong>[^<]*svalnar från 5,0 °C till 0 °C/);
 assert.match(t,/<strong>b\)<\/strong>[^<]*fryser vid 0 °C/);
 assert.match(t,/<strong>c\)<\/strong>[^<]*svalnar från 0 °C till −3,0 °C/);
 assert.match(q('7.223').t,/vatten vid 35 °C behövs för att precis smälta/);
 assert.match(q('7.212').s,/752400\\,\\mathrm\{J\}/);
 assert.doesNotMatch(q('7.212').s,/752400\\,\\mathrm\{kJ\}/);
});
