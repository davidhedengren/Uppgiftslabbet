'use strict';
const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('node:fs'),vm=require('node:vm'),path=require('node:path');
const root=path.join(__dirname,'..'),c={window:{}};
for(const file of ['uppgifterma1.js','strukturma1.js'])vm.runInNewContext(fs.readFileSync(path.join(root,file),'utf8'),c);
const get=id=>c.window.BANKMA1.find(q=>q.id===id),plain=x=>JSON.parse(JSON.stringify(x));
const NYA=Array.from({length:48},(_,i)=>`1.${1136+i}`);

/* Uppgiftens uttryck (som det står i frågan) och facit skrivna som JS, för numerisk ekvivalens. */
const FORENKLA={
  '1.1136':['4*(x+5)','4*x+20'],'1.1137':['6*(a-2)','6*a-12'],'1.1138':['3*x+(2*x-7)','5*x-7'],
  '1.1139':['5*(1-2*x)','5-10*x'],'1.1140':['-(4-3*m)','3*m-4'],'1.1141':['-3*(x+4)','-3*x-12'],
  '1.1142':['-5*(2*a-3)','-10*a+15'],'1.1143':['10-(4-x)','x+6'],'1.1144':['3*(2*x-1)+4','6*x+1'],
  '1.1145':['5*y-2*(y-6)','3*y+12'],'1.1146':['2*(x+3)-(x-5)','x+11'],'1.1147':['-(3*x-2)-(x+4)','-4*x-2'],
  '1.1148':['4*(a+2*b)-3*(a-b)','a+11*b'],'1.1149':['-2*(x-1)-3*(1-x)','x-1'],
  '1.1153':['500-3*(x+15)','455-3*x'],'1.1154':['5*(x+3)-2*(x-1)','3*x+17'],
  '1.1155':['2*(3*x-(x+4))','4*x-8'],'1.1156':['3*(x+4)-2*(x+6)','x'],
  '1.1159':['3*(2*x+7)','6*x+21'],'1.1160':['6*(2*r-3)','12*r-18'],'1.1161':['2*(3*t-2)+2*(t+5)','8*t+6'],
  '1.1162':['3*(2*z-5)+7','6*z-8'],'1.1163':['2*(w+1)+(3*w-4)','5*w-2'],'1.1164':['6*(p-1)+4*(2*p+3)','14*p+6'],
  '1.1165':['2*(x+5)+2*(2*x)-4*(x+2)','2*x+2'],'1.1166':['3*(2*(2*d+15)+2*d)','18*d+90'],'1.1167':['6*(x+4)/2-(x+5)','2*x+7'],
  '1.1168':['(8*x+6)/2','4*x+3'],'1.1169':['0.2*(15*n+40)','3*n+8'],'1.1170':['-2*(3*p-q+4)','-6*p+2*q-8'],
  '1.1171':['12-(5*w-3+2*w)','15-7*w'],'1.1178':['5*r-2*(20-r)','7*r-40'],'1.1179':['2*(p-50)+3*(p+150-50)','5*p+200'],
  '1.1180':['15-2*(4-(x-3))','2*x+1'],'1.1181':['-(2*(x+5)+3*(x-1))','-5*x-7'],
};
const VAR=['x','y','a','b','m','n','p','q','r','t','w','z','d'];
const varde=(uttryck,v)=>Function(...VAR,`return ${uttryck}`)(...VAR.map(k=>v[k]));
const tillJs=s=>String(s).replace(/(\d)([a-z])/g,'$1*$2');

test('48 uppgifter i delmomentet Uttryck med parenteser har rätt placering och verktyg',()=>{
  for(const id of NYA){
    const q=get(id);assert.ok(q,id);
    assert.equal(q.kap,1);assert.equal(q.omr,'forenkla_uttryck');assert.equal(q.familj,'Uttryck med parenteser');
    assert.deepEqual(plain(q.kurs),['1a','1b','1c']);assert.ok(c.window.OMRMA1[1][q.omr]);
    /* Teckenhanteringen vid multiplikation är det som tränas; räknaren skulle ta över den delen. */
    assert.equal(q.miniräknare,false);assert.equal(q.geogebra,false);
    assert.equal(q.spel,true);assert.equal(q.självrättning===true||Array.isArray(q.självrättning),true);
    assert.ok(q.t&&q.s&&q.ledtrad&&q.niva&&q.poang);
  }
  const familj=c.window.BANKMA1.filter(q=>q.familj==='Uttryck med parenteser');
  assert.equal(familj.length,48);
  /* Variation: inga två uppgifter i delmomentet har samma facit. */
  const facit=familj.map(q=>JSON.stringify(q.rättSvar));
  assert.equal(new Set(facit).size,facit.length,facit.filter((f,i)=>facit.indexOf(f)!==i).join(' '));
  const tn=familj.flatMap(q=>[].concat(q.traningsniva));
  for(const n of [1,2,3,5])assert.ok(tn.includes(n),`träningsnivå ${n} saknas`);
  assert.deepEqual([...new Set(familj.map(q=>q.niva))].sort(),['A','C','E']);
});

test('Varje facit är lika med uttrycket i frågan och står i förenklad form',()=>{
  for(const [id,[fraga,svar]] of Object.entries(FORENKLA)){
    const q=get(id);const ratt=Array.isArray(q.rättSvar)?q.rättSvar[0]:q.rättSvar;
    assert.equal(tillJs(ratt).replace(/\s/g,''),svar.replace(/\s/g,''),id);
    for(let k=0;k<8;k++){
      const v={x:k*3-7,y:5-k*2,a:k-4,b:2*k+1,m:7-k,n:k*2-5,p:9-k*3,q:k+3,r:4-k,t:k*k-6,w:2-k,z:k*5-11,d:k+7};
      assert.ok(Math.abs(varde(fraga,v)-varde(svar,v))<1e-12,`${id} ${JSON.stringify(v)}`);
    }
    assert.doesNotMatch(String(ratt),/[()]/,id);
    if(id!=='1.1156')assert.equal(q.svarFormat,'förenklat_polynom');
  }
});

test('Begrepps- och problemlösningsuppgifterna har entydiga svar',()=>{
  assert.equal(get('1.1150').rättSvar,'C');assert.match(get('1.1150').t,/C: \\\(-2x\+6\\\)/);
  assert.equal(get('1.1151').rättSvar,'B');assert.match(get('1.1151').t,/B: .*13-2x/);
  for(const x of [-3,0,2,5]){
    assert.equal(-4*(2*x-3),-8*x+12);
    assert.equal(4*(x+3)-3*(x-2),x+18);
    assert.equal(3*(x+2)-(-2)*(x-1),5*x+4);
  }
  assert.equal(get('1.1152').rättSvar,-4);assert.equal(get('1.1157').rättSvar,3);
  assert.deepEqual(plain(get('1.1158').rättSvar),[3,-2]);assert.equal(get('1.1158').svarsstruktur,'ordnad');
  const d=get('1.1156');assert.deepEqual(plain(d.rättSvar),['x',2026]);assert.equal(d.spelDelar.length,2);
  assert.doesNotMatch(d.spelDelar[0].s,/2026/);
});

test('Figuren i 1.1154 har rätt proportioner för de utmärkta måtten',()=>{
  const t=get('1.1154').t;
  assert.match(t,/M70 50 H190 V110 H370 V200 H70 Z/);
  /* Med x=7 är figuren skalenlig, 30 px per cm: bredderna 300 px = x+3 = 10 och 180 px = x-1 = 6, höjderna 150 px = 5 och 60 px = 2. */
  assert.equal(300/30,7+3);assert.equal(180/30,7-1);assert.equal(150/30,5);assert.equal(60/30,2);
  for(const etikett of ['x + 3','x − 1','>5<','>2<'])assert.ok(t.includes(etikett),etikett);
});
