'use strict';
const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('node:fs'),vm=require('node:vm'),path=require('node:path');
const c={window:{}};vm.runInNewContext(fs.readFileSync(path.join(__dirname,'..','uppgifterma2.js'),'utf8'),c);
const bank=c.window.BANKMA2;
const get=id=>bank.find(t=>t.id===id&&/^normalfordel/.test(t.omr));
const plain=v=>JSON.parse(JSON.stringify(v));
const text=h=>String(h||'').replace(/<svg[\s\S]*?<\/svg>/g,' ').replace(/<[^>]+>/g,' ');

/* Facit före omskrivningen 2026-10-22: sammanhangen är nya men talen och svaren är desamma. */
const FACIT={"4.06":15.9,"4.07":[6,2.3],"4.08":[70,130],"4.13":[50,6.24],"4.19":6,"4.26":[5.02,30,null],"4.37":4,"4.38":[30,50],"4.39":28,"4.44":655,"4.45":[86,58],"4.50":82,"4.53":62,"4.57":[60.8,81.4],"4.66":[10,95.4],"4.69":12,"4.72":[42,58],"4.81":65.1,"4.87":[9.6,47.04,52.96],"4.89":93.3,"4.94":68.2,"4.95":[58.98060543069249,91.01939456930751,80],"4.99":81.8,"4.100":0.909,"4.106":null,"4.110":68.3,"4.116":[40,64],"4.117":[59.7,80.3],"4.122":68.2,"4.123":0.894,"4.151":[87,57.2],"4.152":84.1,"4.154":34,"4.176":[22,38],"4.177":[64,76],"4.178":[6.7,97],"4.181":68.2,"4.184":15.9,"4.196":54,"4.197":[27,33],"4.214":86,"4.215":[41,47],"4.216":[80,120],"4.217":84.1,"4.218":70.3,"4.231":[53,67],"4.232":15.9,"4.237":84.1,"4.251":35,"4.252":166,"4.256":6};

test('Normalfördelningsuppgifterna har verkliga sammanhang och oförändrat facit',()=>{
  for(const [id,svar] of Object.entries(FACIT)){
    const t=get(id);assert.ok(t,id);
    assert.deepEqual(plain(t.rättSvar),svar,id);
    for(const h of [t.t,t.spelIntro,...(t.spelDelar||[]).flatMap(d=>[d.fraga,d.t])].filter(Boolean))
      assert.doesNotMatch(text(h),/En normalfördelning har|Normalfördelning:|En normalfördelad storhet|En variabel är normalfördelad|Ett stort material|En datamängd|En mätserie|En storhet är/,id);
  }
  assert.match(get('4.06').t,/blodtryck/);assert.match(get('4.26').spelIntro,/gösar/);assert.match(get('4.26').spelDelar[1].t,/gösar/);
  assert.match(get('4.95').spelDelar[2].t,/batterier/);assert.match(get('4.178').s,/skola B/);
  assert.equal(get('4.44').svarEnhet,'kattungar');
});

test('Delkorten bär själva sitt sammanhang',()=>{
  for(const id of ['4.07','4.13','4.26','4.45','4.57','4.66','4.72','4.87','4.95','4.116','4.117','4.151','4.215']){
    const t=get(id);assert.ok(t.spelIntro.length>80,id);
    assert.doesNotMatch(t.spelIntro,/^<p>Normalfördelning/,id);
  }
});

test('Uppgifter som saknade figur har fått en normalfördelningskurva',()=>{
  for(const id of ['4.07','4.19','4.37','4.39','4.69','4.232']){
    assert.match(get(id).t,/<svg[\s\S]*aria-label="Normalfördelningskurva/,id);
  }
  assert.match(get('4.07').spelIntro,/<svg/);
});

test('Nya uppgifter om att känna igen normalfördelat material',()=>{
  const ids=['4.475','4.476','4.477','4.478','4.479'];
  for(const id of ids){
    const t=get(id);assert.ok(t,id);assert.equal(t.omr,'normalfordelat_material');
    assert.deepEqual(plain(t.kurs),['2a','2b','2c']);assert.equal(t.spel,true);
    if(t.svarstyp==='alternativ')assert.equal(t.alternativ.filter(a=>a.ratt).length,1,id);
    if(id!=='4.476')assert.match(t.t,/<svg/,id);
  }
  // 4.477: andelen räknas ur histogrammets staplar.
  const aria=get('4.477').t.match(/aria-label="Histogram över längden hos 200 pojkar: ([^"]+)"/)[1];
  const staplar=[...aria.matchAll(/(\d+)–(\d+) cm (\d+)/g)].map(m=>[+m[1],+m[2],+m[3]]);
  const n=staplar.reduce((s,[, ,a])=>s+a,0);assert.equal(n,200);
  const mitt=staplar.filter(([a,b])=>a>=165&&b<=175).reduce((s,[, ,x])=>s+x,0);
  assert.equal(get('4.477').rättSvar,mitt/n*100);
  // 4.478: Sx ur klassmitterna stämmer med texten.
  const m=staplar.reduce((s,[a,b,x])=>s+x*(a+b)/2,0)/n;
  const sx=Math.sqrt(staplar.reduce((s,[a,b,x])=>s+x*((a+b)/2-m)**2,0)/(n-1));
  assert.equal(m,170);assert.match(get('4.478').t,new RegExp(`S_x\\\\approx${sx.toFixed(1).replace('.','\\{,\\}')}`));
  // 4.479: andelen negativa väntetider i en normalfördelning med textens μ och σ.
  const t9=get('4.479');assert.equal(t9.geogebra,true);
  const [mu,sig]=[...t9.t.matchAll(/\\(?:mu|sigma)=([\d{},]+)/g)].map(x=>Number(x[1].replace('{,}','.').replace(',','.')));
  const erf=x=>{const s=Math.sign(x);x=Math.abs(x);const t=1/(1+.3275911*x);return s*(1-((((1.061405429*t-1.453152027)*t+1.421413741)*t-.284496736)*t+.254829592)*t*Math.exp(-x*x));};
  const neg=50*(1+erf((0-mu)/(sig*Math.SQRT2)));
  const ratt=t9.alternativ.find(a=>a.ratt).txt;
  assert.match(ratt,new RegExp(`ungefär ${Math.round(neg)} % negativa`));
});

test('4.480: Natalies IQ 140 påverkar kvartilavståndet minst',()=>{
  const t=c.window.BANKMA2.find(x=>x.id==='4.480');
  assert.equal(t.omr,'standardavvikelse');assert.equal(t.traningsniva,1);assert.equal(t.niva,'E');
  assert.equal(t.alternativ.filter(a=>a.ratt).length,1);assert.equal(t.alternativ.find(a=>a.ratt).txt,'Kvartilavståndet');
  // Läs prickarna ur figuren: varje blå prick är en elev, x-läget ger IQ (85 vid x=40, 145 vid x=520).
  const iq=x=>Math.round(85+(x-40)/480*60);
  const klass=[...t.t.matchAll(/<circle cx="([\d.]+)" cy="[\d.]+" r="3\.7"/g)].map(m=>iq(+m[1])).sort((a,b)=>a-b);
  assert.equal(klass.length,24);assert.ok(Math.max(...klass)<=107&&Math.min(...klass)>=93);
  const med=v=>{const n=v.length;return n%2?v[(n-1)/2]:(v[n/2-1]+v[n/2])/2;};
  const kv=v=>{const n=v.length,h=Math.floor(n/2);return med(v.slice(h+n%2))-med(v.slice(0,h));};
  const sx=v=>{const m=v.reduce((a,b)=>a+b)/v.length;return Math.sqrt(v.reduce((a,x)=>a+(x-m)**2,0)/(v.length-1));};
  const vb=v=>Math.max(...v)-Math.min(...v);
  const efter=[...klass,140].sort((a,b)=>a-b);
  const okn=[kv(efter)-kv(klass),vb(efter)-vb(klass),sx(efter)-sx(klass)];
  assert.ok(okn[0]<okn[1]&&okn[0]<okn[2]&&okn[0]<=0.5,JSON.stringify(okn));
  assert.match(t.s,new RegExp(`från ${kv(klass)} till ${String(kv(efter)).replace('.',',')}`));
});
