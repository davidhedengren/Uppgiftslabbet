const test=require('node:test');
const assert=require('node:assert/strict');
const fs=require('node:fs'),vm=require('node:vm'),path=require('node:path');
const c={window:{}};vm.runInNewContext(fs.readFileSync(path.join(__dirname,'../uppgifter.js'),'utf8'),c);
const q=id=>c.window.BANK.find(q=>q.id===id);
const G0=9.82,S=r=>4*Math.PI*r**3/3,rv=(a,b,w=1000)=>w*a/(a-b);
// Oberoende fysikmodeller från givna mått, massor, densiteter och krafter.
const cases=[
 ["6.1",()=>[((24 * 1.25) / 2.25), (24 / 2.25)]],
 ["6.3",()=>(((13600 * G0) * 0.018) / 1000)],
 ["6.251",()=>((1000 * G0) * 1.5)],
 ["6.8",()=>[(((998 * G0) * 15) / 1000), (101 + (((998 * G0) * 15) / 1000)), ((101000 + ((998 * G0) * 15)) / 101000)]],
 ["6.9",()=>((998 * 7.5) / 9)],
 ["6.252",()=>((1000 * G0) * 2)],
 ["6.300",()=>((800 * G0) * 1)],
 ["6.301",()=>((1000 * G0) * 0.5)],
 ["6.304",()=>((1200 * G0) * 0.25)],
 ["6.150",()=>((800 / 1000) * 10)],
 ["6.253",()=>(24550 / (G0 * 2.5))],
 ["6.306",()=>(17676 / (G0 * 2))],
 ["6.26",()=>[(((998 * G0) * 3.5) / 1000), (((998 * G0) * 5) / 1000), (((916 * G0) * 3.5) / 1000)]],
 ["6.151",()=>((1000 * (15 - 3)) / 15)],
 ["6.254",()=>(29460 / (1000 * G0))],
 ["6.305",()=>(3928 / (1000 * G0))],
 ["6.32",()=>[(101 + (((998 * G0) * 4.5) / 1000)), (((998 * G0) * 2) / 1000)]],
 ["6.255",()=>(101 + (((1000 * G0) * 3.5) / 1000))],
 ["6.302",()=>(100 + 12)],
 ["6.309",()=>(100 + (((1000 * G0) * 1) / 1000))],
 ["6.256",()=>(((1000 * G0) * (4 - 1)) / 1000)],
 ["6.303",()=>(125 - 101)],
 ["6.308",()=>((800 * G0) * (2 - 0.5))],
 ["6.152",()=>[(((1000 * G0) * 0.18) / 1000), (101 + (((1000 * G0) * 0.18) / 1000))]],
 ["6.52",()=>[(((998 * G0) * 3) / 1000), (Math.PI * (0.2 ** 2)), ((((998 * G0) * 3) * Math.PI) * (0.2 ** 2))]],
 ["6.257",()=>(((1000 * G0) * 4.5) / 1000)],
 ["6.61",()=>[(101300 / (789 * G0)), ((101300 / (789 * G0)) - (101300 / (998 * G0)))]],
 ["6.258",()=>(((1450 - 1000) * G0) * 0.16)],
 ["6.259",()=>(101.3 + (((1000 * G0) * 14) / 1000))],
 ["6.65",()=>[(101.3 + (((998 * G0) * 3.5) / 1000)), ((2 * 101300) / (998 * G0))]],
 ["6.260",()=>((700 * G0) * 0.1)],
 ["6.67",()=>(((998 * G0) * 6.5) / 1000)],
 ["6.261",()=>((179860 - 101300) / (1000 * G0))],
 ["6.69",()=>(((998 * G0) * (28 - 9)) / 1000)],
 ["6.262",()=>((850 / 1000) * 14)],
 ["6.70",()=>[(((998 * G0) * 30) / 1000), (101 + (((998 * G0) * 30) / 1000))]],
 ["6.154",()=>((1000 * G0) * (2 * 0.025))],
 ["6.101",()=>[(((998 * G0) * 2.5) / 1000), (101.3 + (((998 * G0) * 2.5) / 1000))]],
 ["6.263",()=>(219.14 - (((1000 * G0) * 12) / 1000))],
 ["6.264",()=>(24000 / (870 * G0))],
 ["6.104",()=>[(((920 * G0) * 0.2) / 1000), ((((920 * 0.2) + (998 * 0.3)) * G0) / 1000), (((920 * 0.2) + (998 * 0.3)) / 998)]],
 ["6.105",()=>(700000 / (998 * G0))],
 ["6.265",()=>(101 + ((((840 * 1.4) + (1000 * 2.8)) * G0) / 1000))],
 ["6.155",()=>[((2 * 3) / 5), ((1000 * G0) * (0.03 + ((0.03 * 2) / 5)))]],
 ["6.107",()=>[(101300 / (998 * G0)), (101.3 * 2)]],
 ["6.266",()=>(18000 / (910 * G0))],
 ["6.109",()=>[(((998 * G0) * 0.6) / 1000), (0.8 * 0.35), ((((998 * G0) * 0.6) * 0.8) * 0.35)]],
 ["6.267",()=>(((27496 / G0) - (800 * 1)) / 1000)],
 ["6.156",()=>[((1000 * 12) / 15), ((1000 * 11.8) / 15.2), ((1000 * 12.2) / 14.8)]],
 ["6.268",()=>(21358.5 / (G0 * 2.5))],
 ["6.133",()=>[(((998 * G0) * 1.5) / 1000), ((((998 * G0) * 1.5) / 2) / 1000), (((((998 * G0) * 1.5) / 2) * 2) * 1.5)]],
 ["6.307",()=>((1000 * G0) * 0.8)],
 ["6.354",()=>(9.82 * 1000)],
 ["6.356",()=>(19640 / (1000 * G0))],
 ["6.357",()=>(((1000 * G0) * (3 - 1)) / 1000)],
 ["6.436",()=>[((998 * G0) * 10), (101300 + ((998 * G0) * 20)), ((350000 - 101300) / (998 * G0))]],
 ["6.437",()=>[(101300 + ((1025 * G0) * 55)), ((1025 * G0) * 3200), ((999 * 101300) / (1025 * G0))]],
 ["6.438",()=>((1.2 * G0) * 35)],
 ["6.439",()=>[((998 * 3.71) * 500), ((3.71 * 500) / G0)]],
 ["6.440",()=>[((4 * 101300) / (1000 * G0)), ((9000000 - 101300) / (1025 * G0))]],
 ["6.441",()=>((1000 * G0) * (0.0001 / (Math.PI * (0.01 ** 2))))],
 ["6.442",()=>[((13600 * G0) * 0.76), ((13600 * 0.76) / 984), ((13600 * G0) * (0.76 - 0.075))]],
 ["6.443",()=>[(1330 / (1020 * G0)), ((610 * 1020) / 13600)]],
 ["6.444",()=>[((13600 * G0) * 0.104), (((13600 * G0) * 0.104) + ((1060 * G0) * 1.37)), (((13600 * G0) * 0.104) - ((1060 * G0) * (1.75 - 1.37)))]],
 ["6.445",()=>[((1060 * G0) * 1.65), (((1060 * G0) * 1.65) * 9.4e-05)]],
 ["6.446",()=>((13600 * (0.76 - 0.747)) / 1.29)],
 ["6.452",()=>((((1025 * G0) * 27.5) * Math.PI) * (0.175 ** 2))],
 ["6.453",()=>(((1250 * 0.0075) / (Math.PI * (0.012 ** 2))) / (1000 * G0))],
 ["6.454",()=>[((1025 * G0) * 0.4), ((101300 / 20) / (1025 * G0))]],
 ["6.455",()=>[((1.5 / (Math.PI * (0.0041 ** 2))) / (1030 * G0)), (28000 / (0.8 * G0))]],
 ["6.456",()=>((((1030 * G0) * 3) * Math.PI) * (0.005 ** 2))],
 ["6.457",()=>[((1000 * G0) * 0.2), ((0.1 * G0) / 0.004), ((0.1 / 1000) / 0.004)]],
 ["6.458",()=>[(((1000 * 0.42) + (850 * 0.18)) * G0), (((1000 * 0.04) + (910 * 0.07)) * G0), (1020 / (1300 * G0))]],
 ["6.459",()=>(((101300 / G0) - 1000) / (13600 - 1000))],
 ["6.460",()=>((1 - (780 / 1000)) * 0.05)],
 ["6.461",()=>(101300 / (0.645 * G0))],
 ["6.462",()=>(0.15 * (1 - (1000 / 13600)))],
 ["6.463",()=>[(0.0001 / 0.0005), ((((0.0001 / 0.0005) * 1000) / 13600) / (1 + (10 / 5)))]],
 ["6.464",()=>[(101300 + ((13600 * G0) * 0.18)), (101300 - ((13600 * G0) * 0.055)), ((175000 - 101300) / (13600 * G0))]],
 ["6.465",()=>((115000 - 96000) / (G0 * 0.55))],
];

test('Vätsketryck: självrättningens svar följer 80 oberoende fysikmodeller',()=>{
 let fields=0;
 for(const[id,f]of cases){const t=q(id),raw=f(),xs=Array.isArray(raw)?raw:[raw];
 const vs=Array.isArray(t.rättSvar)?t.rättSvar:[t.rättSvar];assert.equal(vs.length,xs.length,id);
 xs.forEach((v,i)=>{assert.ok(Math.abs(v-vs[i])<=1e-12*Math.max(Math.abs(v),1e-12),id+' del '+i+' '+vs[i]+' / '+v);fields++;});}
 assert.equal(fields,124);
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
test('Vätsketryck: skrivna slutsvar har den avrundning som frågan ber om',()=>{
 const failures=[];let fields=0;
 for(const[id,f]of cases){const t=q(id),raw=f(),xs=Array.isArray(raw)?raw:[raw];
 xs.forEach((v,i)=>{const part=t.spelDelar?t.spelDelar[i]:t,shown=written(part),want=rounding(part.fraga||part.t,v);
 const tol=Array.isArray(t.tolerans)?t.tolerans[i]:t.tolerans;
 if(want===null ? Math.abs(shown-v)>tol+1e-12 : Math.abs(shown-want)>1e-10*Math.max(Math.abs(want),1e-12))failures.push({id,part:i,shown,want});fields++;});}
 assert.equal(fields,124);assert.deepEqual(failures,[]);
});
test('Vätsketryck: nya enkla kort tränar omvandling och djupjämförelse',()=>{
 const unit=q('6.354');assert.equal(unit.traningsniva,1);assert.equal(unit.rättSvar,9820);assert.equal(unit.svarEnhet,'Pa');
 const compare=q('6.355');assert.equal(compare.traningsniva,1);assert.equal(compare.spel,true);
 assert.deepEqual(Array.from(compare.alternativ,x=>x.ratt),[false,true,false]);
});
test('6.445: kraften gäller ett litet område med given area',()=>{
 const t=q('6.445');assert.doesNotMatch(t.t,/mantelyt/i);assert.equal(t.spelDelar[1].traningsniva,2);
 assert.match(t.t,/0,94 cm²/);assert.ok(Math.abs(t.rättSvar[1]-1060*9.82*1.65*.94e-4)<1e-12);
});
test('6.443: exakt halvtal avrundas till 45,8 mm',()=>{
 const t=q('6.443');assert.equal(t.rättSvar[1],45.75);assert.equal(written(t.spelDelar[1]),45.8);
});

test('Vätsketryck: självständiga delkort har konsekventa givna värden',()=>{
 const heart=q('6.444');for(const d of heart.spelDelar){assert.doesNotMatch(d.t,/13,9 kPa/);}
 assert.doesNotMatch(q('6.457').spelDelar[0].t,/träbit/);
 const force=q('6.445').spelDelar[1];assert.match(force.t,/17,2 kPa/);
 assert.doesNotMatch(force.t,/1,65 m|1060|mantelyt/);
 assert.equal(rounding(force.fraga,17.2e3*.94e-4),written(force));
 assert.equal(q('6.445').traningsniva,3);
});
