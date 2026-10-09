const test=require('node:test');
const assert=require('node:assert/strict');
const fs=require('node:fs');
const vm=require('node:vm');
const c={window:{}};vm.runInNewContext(fs.readFileSync(require('node:path').join(__dirname,'../uppgifter.js'),'utf8'),c);
const q=id=>c.window.BANK.find(q=>q.id===id);
const g=9.82;
// Oberoende beräkningar från uppgifternas givna värden.
const cases=[
 ["5.277",0.2 * 8],
 ["5.298",2 * 3],
 ["5.299",0.45 * 20],
 ["5.300",90 * 5],
 ["5.278",0.25 * 10],
 ["5.16",[420 / 30, 1.673 * 2]],
 ["5.279",3.6 / 0.3],
 ["5.301",20 / 5],
 ["5.312",3 / 0.2],
 ["5.32",[0.15 * 20, 0.15 * -25, 0.15 * (-25 - 20), 0.15 * (-25 - 20) / 0.008]],
 ["5.280",4.9 / 14],
 ["5.302",18 / 6],
 ["5.313",-12 / -4],
 ["5.281",0.4 * -16],
 ["5.282",0.45 * (0 - 18)],
 ["5.318",0.5 * (0 - 6)],
 ["5.48",0.5 * 0.2 * 300 / 4.5],
 ["5.283",0.2 * 20 - 3],
 ["5.309",4 + 3],
 ["5.82",[220 * 0.4, 220 * 0.4, 220 * 0.4 / 12]],
 ["5.285",0.22 * (-12 - 12) / 0.025],
 ["5.287",1000 * 0.16 * (-10 - 16) / -128],
 ["5.157",[90 / 12, 90 / 3]],
 ["5.288",0.16 * (-14 - 26)],
 ["5.158",[78 * 5.5, 1100 * 80 / 3.6, 280000 * 900 / 3.6]],
 ["5.310",0.15 * 12],
 ["5.311",1000 * 36 / 3.6],
 ["5.161",[80 * 0.25, 80 * 0.25, 80 * 0.25 / 4]],
 ["5.162",[250 * 0.04, 250 * 0.04 / 0.6]],
 ["5.291",0.19 * (14 - 24)],
 ["5.303",12 * 0.5],
 ["5.304",100 * 0.02],
 ["5.305",15 / 0.3],
 ["5.306",8 / 20],
 ["5.307",2 * 3],
 ["5.308",-6 / 3],
 ["5.314",40 * 0.15],
 ["5.315",-4 / 0.08],
 ["5.316",1000 * -1.5 / -30],
 ["5.317",2 * (4 - 1)],
 ["5.319",3 + 4 / 2],
 ["5.320",3 - 8 / 2],
 ["5.321",2 * 3 + 1 * -4],
 ["5.365",[0.45 * (20 - -8) / 0.012, (20 + 8) / 8]],
 ["5.366",0.5 * 0.005 * 600 / 0.06],
 ["5.367",0.5 * 12],
 ["5.368",[4 * 0.75, 20 / 3, 3 * g * 8]],
 ["5.369",350 * 10 / 1100],
 ["5.370",[5500 * 3 / 400, 0.5 * 41.25 * 3]],
 ["5.371",[3 - 12000 * 10 / 1500000, 1500000 * 3 / 12000, 1500000 * 3 / 60]],
 ["5.372",480000 * (29.5 - 24.3) / 12],
 ["5.373",[25 / (0.6 * g), 25 / (0.12 * g)]],
 ["5.374",42 - 0.28 * g * 3.5],
 ["5.375",0.045 * 25 / 0.002],
 ["5.376",50 * 0.01 / 0.2],
 ["5.377",7.26 * 13 / 220],
 ["5.378",0.08 / 0.17],
 ["5.379",2300 * 15 / 0.56],
 ["5.380",[3 + 25 * 0.05 / 0.16, 3 - 12 * 0.05 / 0.16]],
 ["5.381",[0.35 * (-3.1 - 5), -2.84 / 0.055]],
 ["5.382",[0.42 * 18 / 650, 0.42 * (18 + 13) / 650]],
 ["5.383",75 * (15 + 2.6) / 0.15],
 ["5.384",[0.145 * (55 + 45), 14.5 / 0.002]],
 ["5.385",0.06 * (50 + 40) / 0.03],
 ["5.386",[1.2 * (2.1 - -5.2) + 1.2 * g * 0.02, 9 / 0.02]],
 ["5.387",[Math.abs(14 - 1200 * 0.027 / 0.4), 14 + 1200 * 0.027 / 0.4]],
 ["5.388",[50 + 3600 / 1200, 50 - 3600 / 1800, (53 - 48) * 120]],
 ["5.389",35 * 1.5 / 0.5],
 ["5.390",4 / 24],
 ["5.391",5.9 * 8.9 / 0.018],
 ["5.392",[200000.0 * 50 / 25, 200000.0 * 50 / 100000.0]],
 ["5.393",0.06 * (50 + 20) / 84],
 ["5.394",0.15 * ((2 * g * 1.25) ** 0.5 + (2 * g * 0.96) ** 0.5)],
 ["5.395",[(2 * g) ** 0.5, 0.05 * ((2 * g) ** 0.5 / 0.01 + g), 0.5 * (2 * g) ** 0.5 * 0.01]],
 ["5.396",0.1 * (2 * g * 2 / (2 * 0.06) + g)],
 ["5.397",[24 ** 2 / (2 * g), 2 / 24, 75 * 24 / 0.0833 + 75 * g]],
 ["5.398",[150 / 0.02, 150 / 900]],
 ["5.399",[(2 * g * 12) ** 0.5, 0.6 / (2 * g * 12) ** 0.5, 12 / 0.3 + 1]],
 ["5.400",[36 ** 2 / (2 * g), 8 / 36, 10000 / (36 ** 2 / 8 + g)]],
 ["5.601",12 * 0.5],
 ["5.602",0.5 * 0.2 * 60],
 ["5.604",20 * 0.1 + 10 * 0.2],
 ["5.605",0.5 * 0.4 * 80 / 0.4],
 ["5.606",40 * 0.1 - 20 * 0.2],
 ["5.607",30 * 0.2 / 2],
];

test('Rörelsemängd: alla numeriska uppgifter räknas från givna värden',()=>{
 const tasks=c.window.BANK.filter(t=>t.kap===5&&t.omr==='rorelsemangd'&&(typeof t.rättSvar==='number'||Array.isArray(t.rättSvar)));
 assert.equal(tasks.length,85);assert.deepEqual(new Set(cases.map(x=>x[0])),new Set(tasks.map(x=>x.id)));
 for(const[id,values]of cases){const t=q(id),want=Array.isArray(values)?values:[values],got=Array.isArray(t.rättSvar)?t.rättSvar:[t.rättSvar];assert.equal(want.length,got.length,id);
 want.forEach((v,i)=>assert.ok(Math.abs(v-got[i])<=1e-10*Math.max(1,Math.abs(v)),`${id} del ${i}: ${v} mot ${got[i]}`));}
});
test('De skrivna numeriska slutsvaren stämmer med beräkningarna',()=>{
 let checked=0;const failures=[];
 for(const[id,values]of cases){const t=q(id),vs=Array.isArray(values)?values:[values];
 vs.forEach((v,i)=>{const p=t.spelDelar?t.spelDelar[i]:t,plain=p.s.replace(/<[^>]*>/g,' ').replace(/&nbsp;/g,' '),answer=plain.split('Svar:').at(-1);
 const m=answer.match(/([−+-]?\d+(?:[,.]\d+)?)(?:\s*[·×]\s*10([⁻⁰¹²³⁴⁵⁶⁷⁸⁹]+))?/);
 let shown=m?Number(m[1].replace('−','-').replace(',','.')):NaN;
 if(m&&m[2]){const digits={'⁻':'-','⁰':'0','¹':'1','²':'2','³':'3','⁴':'4','⁵':'5','⁶':'6','⁷':'7','⁸':'8','⁹':'9'};shown*=10**Number([...m[2]].map(c=>digits[c]).join(''));}
 const tol=Array.isArray(t.tolerans)?t.tolerans[i]:t.tolerans;
 if(!(Math.abs(shown-v)<=tol+1e-10*Math.max(1,Math.abs(v))))failures.push(`${id} del ${i}: skrivet ${shown}, beräknat ${v} ± ${tol}`);checked++;
 });}assert.equal(checked,122);assert.deepEqual(failures,[]);
});
test('Kortens förutsättningar, riktningar och ändrade frågetyper hänger ihop',()=>{
 assert.equal(q('5.365').spelDelning,'deluppgifter');assert.equal(q('5.365').spelDelar.length,2);
 assert.match(q('5.365').spelDelar[1].t,/8,0 m\/s/);assert.match(q('5.365').spelDelar[1].t,/20 m\/s/);
 assert.match(q('5.381').spelDelar[1].t,/−2,84 kg·m\/s/);assert.match(q('5.386').spelDelar[1].t,/9,00 Ns/);
 assert.match(q('5.387').t,/oförändrad under hela tiden/);
 assert.match(q('5.388').spelDelar[2].t,/53 respektive 48/);assert.doesNotMatch(q('5.388').spelDelar[2].t,/1200|1800/);
 assert.match(q('5.395').spelDelar[2].t,/konstant acceleration/);assert.match(q('5.395').spelDelar[2].t,/från vila/);
 assert.doesNotMatch(q('5.396').t,/brunt|8,0 N/);
 assert.match(q('5.397').spelDelar[2].t,/0,0833 s/);
 assert.equal(q('5.399').svarEnhet[2],null);assert.equal(q('5.400').svarEnhet[2],'kg');
 assert.match(q('5.400').spelDelar[2].t,/10,0 kN/);assert.doesNotMatch(q('5.400').spelDelar[2].t,/80 kg/);
});
