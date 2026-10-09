const test=require('node:test');
const assert=require('node:assert/strict');
const fs=require('node:fs');
const vm=require('node:vm');
const c={window:{}};vm.runInNewContext(fs.readFileSync(require('node:path').join(__dirname,'../uppgifter.js'),'utf8'),c);
const q=id=>c.window.BANK.find(q=>q.id===id);
const g=9.82;
// Oberoende beräkningar från uppgifternas givna värden.
const cases=[
 ["6.2",[(65 * g), (((65 * g) / 2000) * 10000.0), ((((65 * g) / 2) / 2000) * 10000.0)]],
 ["6.297",((600 / 30000) * 10000.0)],
 ["6.222",(400 / 0.02)],
 ["6.223",(450 / 0.025)],
 ["6.11",[(250 * 1000), (250 / 100), (3 * 100), (101300 / 1000)]],
 ["6.224",((500 / 0.03) / 1000)],
 ["6.23",[(0.001 * 100000), (45000000.0 / 100000)]],
 ["6.225",(20000 * 0.035)],
 ["6.24",(((18 * g) / (4 * 0.0003)) / 1000)],
 ["6.226",(600 / 15000)],
 ["6.227",((650 / (450 * 0.0001)) / 1000)],
 ["6.228",(35000 * 0.02)],
 ["6.229",(400 / 16000)],
 ["6.42",[(120 / 4), (120 * 15), ((120 * 15) / (4 * 25))]],
 ["6.230",((450 / (0.2 * 0.15)) / 1000)],
 ["6.231",((500 / (0.035 * 2)) / 1000)],
 ["6.232",(((550 * 1.2) / 0.04) / 1000)],
 ["6.51",[(20 * 1000), (20000 * 0.02), (400 / g)]],
 ["6.233",((600 / 0.045) / 1000)],
 ["6.290",(250 / 0.05)],
 ["6.292",(90 / 3000)],
 ["6.295",((360 / (120 * 0.0001)) / 1000)],
 ["6.55",[((4500 * g) / 1000), (4 * 0.12), (((4500 * g) / (4 * 0.12)) / 1000)]],
 ["6.234",((9 / 6) ** 2)],
 ["6.235",(((80 * g) / (220 * 0.0001)) / 1000)],
 ["6.57",(((300 * ((200 / 25) ** 2)) / g) / 1000)],
 ["6.236",((2400 * 5) / 80)],
 ["6.237",(((65 * g) / ((2 * 160) * 0.0001)) / 1000)],
 ["6.59",[(((6 * g) / 5800) * 10000.0), (6 / (((6 * g) / 5800) ** 1.5))]],
 ["6.238",(2.2 * ((1920 / 120) ** 0.5))],
 ["6.239",(((75 * g) / 36825) * 10000.0)],
 ["6.240",(30 * ((2.6 / 9.5) ** 2))],
 ["6.299",((15 * 4) / 20)],
 ["6.241",((19640 * (240 * 0.0001)) / g)],
 ["6.93",(((101000 * Math.PI) * (0.03 ** 2)) / g)],
 ["6.242",(120 * ((8 / 2) ** 2))],
 ["6.298",((50 * 24) / 3)],
 ["6.94",((70 / 0.04) / (280 / ((2 * 0.38) * 1.2)))],
 ["6.243",(((70 * g) / (180 * 0.0001)) / 1000)],
 ["6.95",[(((55 * g) / 0.0001) / 1000000.0), (((4000 * g) / (800 * 0.0001)) / 1000), ((55 / 0.0001) / (4000 / (800 * 0.0001)))]],
 ["6.96",(((9.2 * g) / (0.25 ** 2)) / 1000)],
 ["6.244",((290000 * Math.PI) * ((0.034 / 2) ** 2))],
 ["6.97",((22 / (1.8 * 0.0001)) / 1000)],
 ["6.245",Math.ceil(((2 * (((950 / 85000) / Math.PI) ** 0.5)) * 1000))],
 ["6.98",[(2400 * (0.1 ** 2)), ((2400 * (0.1 ** 2)) / g)]],
 ["6.246",((900 * g) * ((1.5 / 10) ** 2))],
 ["6.247",(((270000 - 101000) * Math.PI) * ((0.032 / 2) ** 2))],
 ["6.248",((80000 * Math.PI) * ((0.12 / 2) ** 2))],
 ["6.102",(1 * (((900 * g) / 687) ** 0.5))],
 ["6.249",(((850000 * Math.PI) * ((0.13 / 2) ** 2)) / g)],
 ["6.173",(((((200000 - 101000) * Math.PI) * ((0.003 / 2) ** 2)) / g) * 1000)],
 ["6.250",((250000 * Math.PI) * ((0.03 / 2) ** 2))],
 ["6.291",(60000 * 0.002)],
 ["6.296",((180000 - 120000) * (50 * 0.0001))],
 ["6.293",(140 - 100)],
 ["6.294",(101 + 35)],
 ["6.350",(600 / 0.3)],
 ["6.351",(3000 * 0.2)],
 ["6.352",(500 / 2500)],
 ["6.367",[((1200 * g) / ((12 / 2) ** 2)), (0.15 * ((12 / 2) ** 2))]],
 ["6.368",[(((101300 * Math.PI) * (0.03 ** 2)) / g), ((((101300 - 30000) * Math.PI) * (0.03 ** 2)) / g)]],
 ["6.419",[(400 / 0.0002), ((90 * g) / 0.02), ((56 * g) / 4.5e-05), ((56 * g) / 0.0016)]],
 ["6.420",((5000 * g) / ((4 * Math.PI) * ((1.4 / (2 * Math.PI)) ** 2)))],
 ["6.421",[(20 / (Math.PI * (0.004 ** 2))), (20 / (Math.PI * (0.0003 ** 2)))]],
 ["6.422",[(101300 * (2.5 * 1.2)), (300000.0 / g)]],
 ["6.423",[(200000 * 2e-06), (((4 * 200000) * 0.014) / g)]],
 ["6.424",[(101300 * (0.4 * 0.3)), ((0.05 * 101300) * (0.55 * 1.75))]],
 ["6.425",((10 * (4 * (0.02 ** 2))) / (3 * (0.01 ** 2)))],
 ["6.426",((7870 * 0.03) * g)],
 ["6.427",(0.02 / (Math.PI * (0.0001 ** 2)))],
 ["6.428",((180000 - 101000) * 0.00041)],
 ["6.429",Math.ceil(((101300 * (0.2 * 0.1)) / 169))],
 ["6.430",[((85 * g) / ((2 * 0.055) * 2.15)), ((85 * g) / (0.055 * 2.15)), (((85 * g) * Math.cos((25 * Math.PI / 180))) / ((2 * 0.055) * 2.15))]],
 ["6.431",(8500 / (8960 * g))],
 ["6.432",((101300 - 98600) * (9.1 * 7.6))],
 ["6.433",(((101300 * Math.PI) * (0.024 ** 2)) / 3600)],
 ["6.434",((16 * (g + 1.5)) / (0.5 * 0.15))],
 ["6.435",((101300 * 2) * (((5.5 * 4.25) + (5.5 * 2.4)) + (4.25 * 2.4)))],
 ["6.447",[(((850 * g) * 0.75) + (45 / (Math.PI * (0.15 ** 2)))), ((0.8 * g) / (Math.PI * (0.15 ** 2)))]],
 ["6.448",[(((1200 * g) * (0.25 * 0.01)) / 1), ((0.01 * 1) / (0.25 * 0.01)), ((1200 * g) * ((7.7 / 125) ** 2)), ((1520 * g) / 125)]],
 ["6.449",(2 / (Math.sqrt(((120 * g) / 100)) - 1))],
 ["6.450",((2 * 9) * ((19 / 9.5) ** 2))],
 ["6.451",(((40 * g) * (15 / 65)) / 1600)],
 ["6.550",(12 / 0.04)],
 ["6.551",(600 / 0.12)],
 ["6.552",(1000 / 200)],
 ["6.553",2],
 ["6.554",(10000 * 0.03)],
 ["6.555",(100 / 500)],
 ["6.556",((20 / 0.01) * 0.1)],
];
test('Tryck: alla numeriska uppgifter räknas från givna värden',()=>{
 const tasks=c.window.BANK.filter(t=>t.kap===6&&t.omr==='tryck'&&(typeof t.rättSvar==='number'||Array.isArray(t.rättSvar)));
 assert.equal(tasks.length,90);assert.deepEqual(new Set(cases.map(x=>x[0])),new Set(tasks.map(x=>x.id)));
 for(const[id,values]of cases){const t=q(id),want=Array.isArray(values)?values:[values],got=Array.isArray(t.rättSvar)?t.rättSvar:[t.rättSvar];assert.equal(want.length,got.length,id);
 want.forEach((v,i)=>assert.ok(Math.abs(v-got[i])<=1e-10*Math.max(1,Math.abs(v)),`${id} del ${i}: ${v} mot ${got[i]}`));}
});
test('De skrivna numeriska slutsvaren stämmer med beräkningarna',()=>{
 let checked=0;const failures=[];
 for(const[id,values]of cases){const t=q(id),vs=Array.isArray(values)?values:[values];
 vs.forEach((v,i)=>{const p=t.spelDelar?t.spelDelar[i]:t,plain=p.s.replace(/<[^>]*>/g,' ').replace(/&nbsp;/g,' ').replace(/\{,\}/g,',').replace(/\\cdot10\^\{(-?\d+)\}/g,'e$1'),answer=plain.split('Svar:').at(-1);
 const m=answer.match(/([−+-]?\d+(?:[ \u00a0]\d{3})*(?:[,.]\d+)?)(?:e([+-]?\d+))?/);
 let shown=m?Number(m[1].replace(/\s/g,'').replace('−','-').replace(',','.')):NaN;
 if(m&&m[2])shown*=10**Number(m[2]);
 const tol=Array.isArray(t.tolerans)?t.tolerans[i]:t.tolerans;
 if(!(Math.abs(shown-v)<=tol+1e-10*Math.max(1,Math.abs(v))))failures.push(`${id} del ${i}: skrivet ${shown}, beräknat ${v} ± ${tol}`);checked++;
 });}assert.equal(checked,121);assert.deepEqual(failures,[]);
});

test('Tryck: gränsvärden, fysikmodeller och delkort har tillräckliga egna data',()=>{
 for(const id of ['6.353','6.549']){
  assert.equal(q(id).spel,true);assert.equal(q(id).självrättning,true);
  assert.equal(q(id).svarstyp,'alternativ');
  assert.equal(q(id).alternativ.filter(a=>a.ratt).length,1);
 }
 assert.equal(q('6.245').rättSvar,120);
 assert.ok(950/(Math.PI*(.119/2)**2)>85000);
 assert.ok(950/(Math.PI*(.120/2)**2)<=85000);
 assert.equal(q('6.429').rättSvar,12);
 assert.ok(11*169/.020<101300);assert.ok(12*169/.020>=101300);
 assert.match(q('6.429').t,/0,20 m × 0,10 m/);
 assert.doesNotMatch(q('6.429').t,/lufttryck|totala trycket/);
 for(const id of ['6.367','6.368']){
  assert.equal(q(id).spelDelning,'deluppgifter');assert.equal(q(id).spelDelar.length,2);
  for(const p of q(id).spelDelar){assert.ok(p.ledtrad);assert.match(p.t,/cm/);assert.match(p.s,/Svar:/);}
 }
 assert.match(q('6.42').spelDelar[2].s,/120\\cdot15=1800/);
 assert.match(q('6.42').spelDelar[2].s,/4\{,\}0\\cdot25=100/);
 assert.doesNotMatch(q('6.42').spelDelar[0].t+q('6.42').spelDelar[1].t,/<svg/);
 assert.match(q('6.51').spelDelar[2].t,/400 N/);
 assert.doesNotMatch(q('6.51').spelDelar[2].s,/20000|20 000|0\{,\}020/);
 assert.match(q('6.98').spelDelar[1].t,/24 N/);assert.doesNotMatch(q('6.98').spelDelar[1].ledtrad,/Tryck och area/);
 assert.match(q('6.97').t,/hålls stilla/);assert.match(q('6.97').t,/utlopp är stängt/);
 assert.match(q('6.423').t,/fyra däck/);assert.match(q('6.423').spelDelar[1].t,/fyra däck/);
 assert.doesNotMatch(q('6.447').spelDelar[1].t,/850|45,0|75,0/);
 assert.match(q('6.434').s,/F_N-mg=ma/);
 assert.match(q('6.451').t,/Ovanför den lilla kolven/);
 assert.match(q('6.450').t,/summan av storlekarna/);
 assert.match(q('6.248').s,/p_\\mathrm\{max\}A/);
 for(const t of c.window.BANK.filter(t=>t.kap===6&&t.omr==='tryck')){
  if(t.spelDelar)assert.match(t.t,/<ol type="a">/);
  for(const p of [t,...(t.spelDelar||[])]){
   assert.doesNotMatch(p.s,/<ol|facit-numero|facit-stegnummer/);
   assert.doesNotMatch(p.t+p.s,/\bformenen\b|\bstor kolven\b|\bfonografnål\b|\bP a\b|\bk g\b/);
  }
 }
});
