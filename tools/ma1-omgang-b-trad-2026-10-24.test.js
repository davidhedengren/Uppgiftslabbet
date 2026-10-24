'use strict';
/* Ma1 2026-10-24 omgång B: stående träddiagram med raka grenar, nya kort i beroende händelser (fylla i grenar),
   svårare sannolikhet i stil med lärarens extrauppgifter, genomsnittlig förändring, bråkform och kvadratrötter med figurer. */
const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('node:fs'),vm=require('node:vm'),path=require('node:path');
const c={window:{}};vm.runInNewContext(fs.readFileSync(path.join(__dirname,'..','uppgifterma1.js'),'utf8'),c);
const B=JSON.parse(JSON.stringify(Object.values(c.window).find(Array.isArray)));const get=id=>{const t=B.find(x=>x.id===id);assert.ok(t,id);return t;};
const ids=(k,a,b)=>Array.from({length:b-a+1},(_,i)=>`${k}.${a+i}`);
const SANN=ids(5,600,619),GF=ids(3,600,612),BR=ids(0,1200,1213),KV=ids(4,750,761);
const TRAD=['5.02','5.16','5.21','5.123','5.124','5.155','5.157'];
const svgar=t=>[t,...(t.spelDelar||[])].flatMap(d=>(d.t||'').match(/<svg[\s\S]*?<\/svg>/g)||[]);

test('Träddiagrammen är stående med raka grenar (inga kurvor) och behåller sina tal',()=>{
  for(const id of TRAD){const s=svgar(get(id));assert.ok(s.length,id);
    for(const v of s){assert.doesNotMatch(v,/<path d="M[\d.]+,[\d.]+ C/,id);assert.match(v,/<line [^>]*stroke-width="2.8"/,id);
      // roten ligger överst: rotens y är minst av alla noder
      const rot=+v.match(/<circle cx="[\d.]+" cy="([\d.]+)" r="6"/)[1];const ys=[...v.matchAll(/<line x1="[\d.]+" y1="([\d.]+)" x2="[\d.]+" y2="([\d.]+)"/g)].map(m=>[+m[1],+m[2]]);
      assert.ok(ys.every(([a,b])=>b>a&&a>=rot),id+' grenarna går nedåt');}}
  const t16=svgar(get('5.16'))[0];for(const p of ['4/7','3/7','3/6','4/6','2/6','0,286','0,143'])assert.ok(t16.includes('>'+p+'<'),'5.16 '+p);
  assert.ok(svgar(get('5.124'))[0].includes('>2/4<')&&svgar(get('5.124'))[0].includes('>1/4<'));
  const t123=svgar(get('5.123'))[0];assert.equal((t123.match(/>\?</g)||[]).length,2,'5.123 har två luckor');
});

test('Nya kort: antal per område, nivå, figurer och inga dubblettfacit',()=>{
  const per={};for(const id of [...SANN,...GF,...BR,...KV]){const t=get(id);per[t.omr]=(per[t.omr]||0)+1;assert.ok([1,2,3,4,5].includes(t.traningsniva),id);}
  assert.deepEqual(per,{beroende_handelser:16,sannolikhet_flera_steg:2,komplementhandelse:2,genomsnittlig_forandring:13,brakform:14,kvadratrotter:12});
  assert.ok(SANN.filter(id=>/<svg/.test(get(id).t)).length>=14);assert.ok(GF.filter(id=>/<svg|<table/.test(get(id).t)).length>=11);
  const v=x=>{const s=String(x.rättSvar),n=Number(s);return isNaN(n)?s:String(Math.round(n*1e6)/1e6);};
  for(const id of [...SANN,...GF,...BR,...KV]){const t=get(id);if(t.svarstyp==='alternativ')continue;
    const krock=B.filter(u=>u.omr===t.omr&&u.id!==id&&u.svarstyp!=='alternativ'&&u.rättSvar!=null&&!Array.isArray(u.rättSvar)&&v(u)===v(t)).map(u=>u.id);
    assert.deepEqual(krock,[],`${id} har samma facit som ${krock}`);}
  // fyll-i-kort: frågetecknet står i trädet och avslöjas inte av färgen i "vilken är fel"
  for(const id of ['5.600','5.601','5.602','5.604','5.608','5.609'])assert.match(get(id).t,/>\?</,id);
  assert.doesNotMatch(get('5.606').t,/fill="#D97706"/);
});

test('Facit räknas om',()=>{
  const fr=(id,s)=>assert.equal(get(id).rättSvar,s,id);const n=(id,x,tol=1e-6)=>assert.ok(Math.abs(Number(get(id).rättSvar)-x)<=tol,`${id}: ${get(id).rättSvar} ≠ ${x}`);
  fr('5.600','5/8');fr('5.601','3/5');fr('5.602','1/6');fr('5.603','5/18');fr('5.604','5/7');fr('5.605','7/18');n('5.607',5);fr('5.608','4/11');fr('5.609','4/9');fr('5.610','1/11');fr('5.611','7/30');
  n('5.613',(25/144-20/132)*100,1e-3);n('5.614',(1-54/60*53/59*52/58)*100,1e-3);fr('5.615','37/42');n('5.616',0.3);n('5.617',1-0.9*0.5*0.2-0.1*0.5*0.8);n('5.618',Math.round(25*(1-(2/3)**6)));n('5.619',(1-0.15**4)*100,1e-3);
  n('3.600',1.06);n('3.601',12.5);n('3.602',5);n('3.603',6);n('3.605',(1.25**0.1-1)*100,1e-3);n('3.606',240000*0.85**3,1e-6);n('3.607',(Math.sqrt(1.12*1.04)-1)*100,1e-3);
  n('3.609',1.25);n('3.610',(Math.sqrt(1.25)-1)*100,1e-3);n('3.611',25);n('3.612',((31/26)**(1/6)-1)*100,1e-3);
  fr('0.1200','5/8');fr('0.1201','3/10');n('0.1202',1.4);fr('0.1203','3/4');fr('0.1204','11/4');n('0.1206',15);fr('0.1207','13/20');n('0.1209',10);fr('0.1210','4/9');n('0.1211',45);fr('0.1212','1/4');n('0.1213',37.5);
  n('4.750',8);n('4.752',60);n('4.753',Math.sqrt(200));n('4.754',1.2);n('4.755',13);n('4.756',3.9);n('4.757',1.5);n('4.758',Math.sqrt(274));n('4.759',Math.sqrt(50/Math.PI));n('4.760',14);
  for(const id of [...SANN,...GF,...BR,...KV].filter(id=>get(id).svarstyp==='alternativ'))assert.equal(get(id).alternativ.filter(a=>a.ratt).length,1,id);
});
