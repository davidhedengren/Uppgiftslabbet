const test=require('node:test');
const assert=require('node:assert/strict');
const fs=require('node:fs');
const vm=require('node:vm');
const c={window:{}};vm.runInNewContext(fs.readFileSync(require('node:path').join(__dirname,'../uppgifter.js'),'utf8'),c);
const q=id=>c.window.BANK.find(q=>q.id===id);
const g=9.82;
// Oberoende beräkningar från uppgifternas givna värden.
const cases=[
 ["5.91",[(30000 / 25), (30000 / 25), ((30000 * (1000 / 25)) / 1000000.0)]],
 ["5.95",[((80 * g) * 12), (((80 * g) * 12) - ((0.5 * 80) * (12 ** 2))), ((((80 * g) * 12) - ((0.5 * 80) * (12 ** 2))) / 90)]],
 ["5.97",[((0.5 * 500) * (0.12 ** 2)), (((2 * (((0.5 * 500) * (0.12 ** 2)) - ((0.08 * g) * 0.12))) / 0.08) ** 0.5), (((0.5 * 500) * (0.12 ** 2)) / (0.08 * g))]],
 ["5.98",[(((0.5 * 6) * ((4.5 ** 2) - (3 ** 2))) / 8), (((4.5 ** 2) - (3 ** 2)) / ((2 * 8) * g))]],
 ["5.99",[(0.12 * ((250 / 0.8) ** 0.5)), (((0.8 * 0.12) * ((250 / 0.8) ** 0.5)) / 2), (((0.5 * 2) * ((((0.8 * 0.12) * ((250 / 0.8) ** 0.5)) / 2) ** 2)) / 1.5)]],
 ["5.100",[(((0.5 * 0.02) * (150 ** 2)) / 0.08), ((1000 * 0.08) / (150 / 2))]],
 ["5.101",((((2 / 5) ** 2) * 0.8) / 1.2)],
 ["5.104",(0.5 * ((1 / 0.25) - 1))],
 ["5.105",((((100 * 4) * 0.25) * 0.4) / ((0.25 + 0.4) ** 2))],
 ["5.106",(((2 * (((0.5 * 6) * (4 ** 2)) - (((0.15 * 6) * g) * 3))) / 1200) ** 0.5)],
 ["5.108",[(((2 * 12) / 0.025) ** 0.5), ((0.025 * (((2 * 12) / 0.025) ** 0.5)) / 0.04), (12 / (0.025 * g))]],
 ["5.110",[(18 - (1.2 * g)), (((18 / 1.2) - g) * 1.5), (((0.5 * ((18 / 1.2) - g)) * (1.5 ** 2)) + (((((18 / 1.2) - g) * 1.5) ** 2) / (2 * g)))]],
 ["5.112",[((14 ** 2) / ((2 * g) * 22)), (22 / (14 / 2))]],
 ["5.114",[((((30 / 60) * 65) * g) * 6), (((((30 / 60) * 65) * g) * 6) / 0.7)]],
 ["5.115",[(((2 * g) * 8) ** 0.5), (((3 * g) * (8 + 0.15)) / 0.15)]],
 ["5.116",((1.8 / (1.8 + 1.2)) * (((2 * (((0.5 * 900) * (0.15 ** 2)) - (((0.12 * 1.8) * g) * 2.4))) / 1.8) ** 0.5))],
 ["5.117",[((75 * 14) / 0.12), ((75 * 14) / 0.02)]],
 ["5.118",[(40000 * 1.5), ((40000 * 1.5) / 60000), (((0.5 * 40000) * (1.5 ** 2)) - ((0.5 * 60000) * (((40000 * 1.5) / 60000) ** 2))), ((20000 * ((40000 * 1.5) / 60000)) / 0.5)]],
 ["5.120",[(((12000 * g) * Math.sin((4 * Math.PI / 180))) + 2500), (((((12000 * g) * Math.sin((4 * Math.PI / 180))) + 2500) * 15) / 1000), (((((12000 * g) * Math.sin((4 * Math.PI / 180))) + 2500) * 2000) / 1000000.0)]],
 ["5.123",[(((45 * (3 ** 2)) / (2 * 6)) + ((45 * g) * (Math.sin((15 * Math.PI / 180)) + (0.25 * Math.cos((15 * Math.PI / 180)))))), ((((45 * (3 ** 2)) / (2 * 6)) + ((45 * g) * (Math.sin((15 * Math.PI / 180)) + (0.25 * Math.cos((15 * Math.PI / 180)))))) * 3)]],
 ["5.124",[((0.43 * 25) / 0.009), (((0.5 * 0.43) * (25 ** 2)) / 0.009)]],
 ["5.125",[((95 * 2.5) + 60), (((95 * 2.5) + 60) / 95), (60 / 0.8)]],
 ["5.126",[(((0.5 * 90) * (7 ** 2)) / 12), (12 / (7 / 2))]],
 ["5.131",[(55 * 12), (-30 * 12), ((((2 * (55 - 30)) * 12) / 18) ** 0.5)]],
 ["5.132",[-(((2 * g) * 2.5) ** 0.5), (((2 * g) * 1.6) ** 0.5), (((0.045 * ((((2 * g) * 2.5) ** 0.5) + (((2 * g) * 1.6) ** 0.5))) / 0.0008) + (0.045 * g)), 36]],
 ["5.133",[((1500 + 800) * 25), (22000 / 25), (((0.5 * (1500 + 800)) * (25 ** 2)) / 60)]],
 ["5.166",[((0.5 * 1000) * (16 ** 2)), ((1000 * (0 - 16)) / (6 - 5)), ((((4 * 16) / 2) + 16) + (16 / 2)), ((-0.5 * 1000) * (16 ** 2))]],
 ["5.168",((((900 * (g + (2 / 3))) * 2) / 0.8) / 1000)],
 ["5.170",[(((2 * g) * 1.8) ** 0.5), (((2 * g) * 1.1) ** 0.5), ((0.2 * g) * (1.8 - 1.1)), ((100 * (1.8 - 1.1)) / 1.8)]],
 ["5.173",(((2 ** 2) + ((2 * g) * 3)) ** 0.5)],
 ["5.220",((((13000 * 60) - ((0.5 * 1500) * ((24 ** 2) - (7 ** 2)))) - 80000) / (1500 * g))],
 ["5.225",[((((((72 * g) * 2) / 21) + 25) * 5) / 1000), (((5 ** 2) + ((2 * (((g * 2) / 21) - (25 / 72))) * 180)) ** 0.5)]],
 ["5.238",(((10 ** 2) + (((2 / 2) * ((49 - ((2 * g) * 0.5)) - (((0.5 * 2) * g) * Math.cos((30 * Math.PI / 180))))) * 4)) ** 0.5)],
 ["5.239",[(((((0.5 * 1230) * ((20 ** 2) - (6 ** 2))) + ((((1230 * g) * 615) * 0.225) / ((1 + (0.225 ** 2)) ** 0.5))) + (400 * 615)) / 1000000.0), ((((((0.5 * 1230) * ((20 ** 2) - (6 ** 2))) + ((((1230 * g) * 615) * 0.225) / ((1 + (0.225 ** 2)) ** 0.5))) + (400 * 615)) / 50) / 1000)]],
 ["5.240",((((2 * (47 - ((0.5 * 5) * g))) * 7) / (5 * (16 - 1))) ** 0.5)],
 ["5.243",((((30000 * 10) - ((0.5 * 2000) * ((12 ** 2) - (10 ** 2)))) - (((2000 * g) * 110) * Math.sin((5.7 * Math.PI / 180)))) / 110)],
 ["5.249",((900 / ((1000 * 20) * ((g * 10) + ((20 ** 2) / 2)))) * 10000.0)],
];
test('Blandad energi: alla numeriska uppgifter räknas från givna värden',()=>{
 const tasks=c.window.BANK.filter(t=>t.kap===5&&t.omr==='blandat_energi'&&(typeof t.rättSvar==='number'||Array.isArray(t.rättSvar)));
 assert.equal(tasks.length,37);assert.deepEqual(new Set(cases.map(x=>x[0])),new Set(tasks.map(x=>x.id)));
 for(const[id,values]of cases){const t=q(id),want=Array.isArray(values)?values:[values],got=Array.isArray(t.rättSvar)?t.rättSvar:[t.rättSvar];assert.equal(want.length,got.length,id);
 want.forEach((v,i)=>assert.ok(Math.abs(v-got[i])<=1e-10*Math.max(1,Math.abs(v)),`${id} del ${i}: ${v} mot ${got[i]}`));}
});
test('De skrivna numeriska slutsvaren stämmer med beräkningarna',()=>{
 let checked=0;const failures=[];
 for(const[id,values]of cases){const t=q(id),vs=Array.isArray(values)?values:[values];
 vs.forEach((v,i)=>{const p=t.spelDelar?t.spelDelar[i]:t,plain=p.s.replace(/<[^>]*>/g,' ').replace(/&nbsp;/g,' '),answer=plain.split('Svar:').at(-1);
 const m=answer.match(/([−+-]?\d+(?:[ \u00a0]\d{3})*(?:[,.]\d+)?)(?:\s*[·×]\s*10([⁻⁰¹²³⁴⁵⁶⁷⁸⁹]+))?/);
 let shown=m?Number(m[1].replace(/\s/g,'').replace('−','-').replace(',','.')):NaN;
 if(m&&m[2]){const digits={'⁻':'-','⁰':'0','¹':'1','²':'2','³':'3','⁴':'4','⁵':'5','⁶':'6','⁷':'7','⁸':'8','⁹':'9'};shown*=10**Number([...m[2]].map(c=>digits[c]).join(''));}
 const tol=Array.isArray(t.tolerans)?t.tolerans[i]:t.tolerans;
 if(!(Math.abs(shown-v)<=tol+1e-10*Math.max(1,Math.abs(v))))failures.push(`${id} del ${i}: skrivet ${shown}, beräknat ${v} ± ${tol}`);checked++;
 });}assert.equal(checked,80);assert.deepEqual(failures,[]);
});

test('Energimodeller, delkort och lärare har samma fullständiga givna värden',()=>{
 assert.match(q('5.105').s,/\(m_\{1\}\+m_\{2\}\)\^2/);
 assert.match(q('5.124').s,/\\frac\{\\Delta E_\{\\mathrm\{k\}\}\}\{\\Delta t\}/);
 assert.doesNotMatch(q('5.104').t+q('5.104').s,/fjäder|Fjäder/);
 for(const text of ['25 m/s','22 kW','60 m'])assert.ok(q('5.133').t.includes(text),text);
 assert.match(q('5.108').t,/Vid ett lodrätt skott/);
 assert.match(q('5.108').spelDelar[2].t,/lodrätt/);
 assert.match(q('5.95').t,/3667,2 J/);assert.match(q('5.95').spelDelar[2].t,/3667,2 J/);
 assert.match(q('5.114').t,/1914,9 W/);assert.match(q('5.114').spelDelar[1].t,/1914,9 W/);
 assert.match(q('5.118').t,/1,00 m\/s/);assert.match(q('5.118').spelDelar[3].t,/1,00 m\/s/);
 assert.doesNotMatch(q('5.118').spelDelar[0].s,/20\\,000/);
 assert.match(q('5.132').spelDelar[2].s,/\+0\{,\}045\\cdot9\{,\}82/);
 assert.equal(q('5.166').spelDelning,'deluppgifter');assert.equal(q('5.166').spelDelar.length,4);
 assert.doesNotMatch(q('5.166').spelDelar[2].t,/1000 kg/);
 for(const p of q('5.166').spelDelar)assert.match(p.t,/<svg/);
 for(const[id,i]of [['5.95',0],['5.97',0],['5.118',0],['5.131',0]])assert.equal(q(id).spelDelar[i].traningsniva,1);
 for(const t of c.window.BANK.filter(t=>t.omr==='blandat_energi')) {
  if(t.spelDelar)assert.match(t.t,/<ol type="a">/);
  for(const p of [t,...(t.spelDelar||[])]) {
   assert.doesNotMatch(p.s,/<ol|facit-numero|facit-stegnummer/);
   assert.doesNotMatch(p.t,/en antal|under den perioden|innan det stannar|m_\{\\mathrm\{Au\}\}/);
  }
 }
});
