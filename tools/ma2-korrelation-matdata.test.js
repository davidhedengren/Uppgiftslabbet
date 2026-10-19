'use strict';
const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('node:fs'),vm=require('node:vm'),path=require('node:path');
const root=path.join(__dirname,'..'),c={window:{}};
for(const file of ['uppgifterma2.js','strukturma2.js'])vm.runInNewContext(fs.readFileSync(path.join(root,file),'utf8'),c);
const NYA=[376,377,378,379,380,381,382,383];
const get=n=>c.window.BANKMA2.find(q=>q.id===`4.${n}`),plain=x=>JSON.parse(JSON.stringify(x));
const tal=s=>Number(String(s).replace('−','-').replace(',','.'));
/* Tabellens kolumner läses ur den visade tabellen, så att facit prövas mot det eleven ser. */
function kolumner(html){
  const rader=[...html.matchAll(/<tr>(.*?)<\/tr>/g)].map(m=>[...m[1].matchAll(/<td>(.*?)<\/td>/g)].map(x=>x[1])).filter(r=>r.length);
  return rader[0].map((_,i)=>rader.map(r=>r[i]));
}
function r(x,y){
  const n=x.length,mx=x.reduce((a,b)=>a+b,0)/n,my=y.reduce((a,b)=>a+b,0)/n;
  let sxy=0,sxx=0,syy=0;for(let i=0;i<n;i++){sxy+=(x[i]-mx)*(y[i]-my);sxx+=(x[i]-mx)**2;syy+=(y[i]-my)**2;}
  return sxy/Math.sqrt(sxx*syy);
}
const nara=(a,b,eps=1e-9)=>assert.ok(Math.abs(a-b)<eps,`${a} != ${b}`);
const tvaDec=v=>v.toFixed(2).replace('.','{,}');

test('Åtta nya korrelationsuppgifter har rätt kurs, område, verktyg och kontrakt',()=>{
  for(const n of NYA){
    const q=get(n);assert.ok(q,n);
    assert.equal(q.kap,4);assert.equal(q.omr,'korrelation_koefficient');assert.deepEqual(plain(q.kurs),['2b','2c']);
    assert.equal(q.familj,'Korrelation i mätdata med digitala verktyg');
    assert.equal(q.geogebra,true);assert.equal(q.miniräknare,true);assert.equal(q.spel,true);
    assert.ok(q.t&&q.s&&q.ledtrad);assert.ok(Array.isArray(q.rättSvar));
    if(q.spelDelar){
      const k=q.spelDelar.length;
      for(const f of ['rättSvar','tolerans','svarFormat','svarEnhet','svarEtiketter','självrättning','traningsniva','arbetsinsats'])assert.equal(q[f].length,k,`${n} ${f}`);
      q.spelDelar.forEach((d,i)=>{
        assert.equal(d.etikett,q.svarEtiketter[i]);assert.ok(d.fraga&&d.s&&d.ledtrad&&d.niva&&d.poang);
        if(d.alternativ){assert.equal(d.alternativ.filter(a=>a.ratt).length,1);assert.equal(q.rättSvar[i],d.alternativ.find(a=>a.ratt).txt);assert.equal(q.svarFormat[i],'text');}
        else{assert.equal(typeof q.rättSvar[i],'number');}
      });
    }
  }
  assert.equal(get(381).spelDelar,undefined);assert.equal(get(381).svarsstruktur,'ordnad');
  assert.ok(c.window.SPARMA2[4].korrelation_koefficient.includes('2b'));
});

test('Korrelationskoefficienterna stämmer med de visade tabellerna',()=>{
  const k376=kolumner(get(376).spelIntro).map(c=>c.map(tal));
  const [ah,ap,bh,bp]=k376;
  nara(get(376).rättSvar[0],r(ah,ap));nara(get(376).rättSvar[1],r(bh,bp));nara(get(376).rättSvar[2],r(ah.concat(bh),ap.concat(bp)));
  assert.ok(get(376).rättSvar[2]<0&&get(376).rättSvar[0]>0&&get(376).rättSvar[1]>0);
  const [v,s]=kolumner(get(377).spelIntro).map(c=>c.map(tal));
  nara(get(377).rättSvar[0],r(v,s));nara(get(377).rättSvar[1],r(v.map(x=>x*x),s));assert.ok(get(377).rättSvar[1]>get(377).rättSvar[0]);
  const [,L,S]=kolumner(get(378).spelIntro).map(c=>c.map(tal));
  nara(get(378).rättSvar[0],r(L,S));
  const utan=i=>i!==6;nara(get(378).rättSvar[2],r(L.filter((_,i)=>utan(i)),S.filter((_,i)=>utan(i))));
  assert.equal(L[6],177);assert.equal(S[6],157);
  const k379=kolumner(get(379).spelIntro);const T=k379[1].map(tal),E=k379[2].map(tal);
  nara(get(379).rättSvar[0],r(T,E));nara(get(379).rättSvar[1],r(T.slice(4,9),E.slice(4,9)));
  assert.deepEqual(k379[0].slice(4,9),['maj','jun','jul','aug','sep']);
  const [vx,vy,gx,gy]=kolumner(get(380).spelIntro).map(c=>c.map(tal));
  nara(get(380).rättSvar[0],r(vx,vy));nara(get(380).rättSvar[1],r(gx,gy));
  const [,cyk,lev]=kolumner(get(382).spelIntro).map(c=>c.map(tal));
  nara(get(382).rättSvar[0],r(cyk,lev));
  const [ta,tb]=kolumner(get(383).spelIntro).map(c=>c.map(tal));
  nara(get(383).rättSvar[0],r(ta,tb));nara(get(383).rättSvar[1],tb.reduce((a,b,i)=>a+b-ta[i],0)/ta.length,1e-9);
});

test('Inget tvådecimalsfacit ligger nära en avrundningsgräns och delkortens givna värden stämmer',()=>{
  for(const n of NYA){
    const q=get(n);if(!q.spelDelar)continue;
    q.rättSvar.forEach((v,i)=>{
      if(typeof v!=='number'||q.tolerans[i]!==0.005)return;
      const rest=Math.abs(v*100)%1;assert.ok(Math.abs(rest-0.5)>0.12,`${n} ${v}`);
      assert.ok(q.spelDelar[i].s.includes(tvaDec(v))||q.spelDelar[i].s.includes(v.toFixed(4).replace('.','{,}')),`${n}${q.svarEtiketter[i]} facit visar ${tvaDec(v)}`);
    });
    /* Resonemangskort som återger tidigare värden ska visa samma avrundning som facit. */
    const givna=q.spelDelar.filter(d=>d.alternativ).map(d=>d.fraga).join(' ');
    for(const m of givna.matchAll(/r\\approx(-?\d\{,\}\d\d)\b/g))
      assert.ok(q.rättSvar.some(v=>typeof v==='number'&&tvaDec(v)===m[1]),`${n}: givet r=${m[1]}`);
  }
});

test('Det suddade mätvärdet i 4.381 ger exakt heltalen 12–18',()=>{
  const x=[1,2,3,4,5,6],y=[4,7,7,10,12];
  const ok=[];for(let h=0;h<=40;h++)if(r(x,y.concat(h))>=0.95)ok.push(h);
  assert.deepEqual(ok,[12,13,14,15,16,17,18]);assert.deepEqual(plain(get(381).rättSvar),[12,18]);
  assert.deepEqual(plain(get(381).tolerans),[0,0]);
});

test('Facitfigurerna har punkter och ligger inom figurramen',()=>{
  for(const n of NYA){
    const q=get(n),svgs=[...q.s.matchAll(/<svg[^>]*viewBox="0 0 (\d+) (\d+)"[^>]*>(.*?)<\/svg>/g)];
    assert.ok(svgs.length>=1,`${n} saknar facitfigur`);
    for(const [,W,H,inner] of svgs){
      const punkter=[...inner.matchAll(/<circle cx="([\d.]+)" cy="([\d.]+)"/g)].concat([...inner.matchAll(/<rect x="([\d.]+)" y="([\d.]+)" width="11"/g)]);
      assert.ok(punkter.length>=1,n);
      for(const [,x,y] of punkter){assert.ok(+x>0&&+x<+W&&+y>0&&+y<+H,`${n}: (${x},${y})`);}
    }
  }
});
