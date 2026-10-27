'use strict';
/* 2026-10-23: äldre astronomikort i Fy2 kap 5 rättas automatiskt; 17 nya kort på högre nivå (5.447–5.463). */
const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('node:fs'),vm=require('node:vm'),path=require('node:path');
const c={window:{}};vm.runInNewContext(fs.readFileSync(path.join(__dirname,'..','uppgifter2.js'),'utf8'),c);
const B=JSON.parse(JSON.stringify(c.window.BANK2));
const O=['farg_ljusstyrka','magnituder','avstandsmatning','stjarnornas_utveckling'];const I=B.filter(t=>O.includes(t.omr));
const get=id=>{const t=B.find(x=>x.id===id);assert.ok(t,id);return t;};const v=id=>get(id).rättSvar;
const nara=(a,b,rel=1e-6)=>Math.abs(a-b)<=Math.abs(b)*rel+1e-12;
const LY=3.2616,PC=3.0856775814913673e16,ARC=206264.806;

test('Inga självrättade kort, alla har träningsnivå, inga standardformler i frågorna',()=>{
  const man=I.filter(t=>t.svarstyp==='manuell'||t.självrättning===false||(Array.isArray(t.självrättning)&&t.självrättning.includes(false)));
  assert.deepEqual(man.map(t=>t.id),[]);assert.deepEqual(I.filter(t=>t.traningsniva==null).map(t=>t.id),[]);
  for(const t of I)for(const x of [t,...(t.spelDelar||[])]){
    assert.doesNotMatch(x.t||'',/Absolut magnitud: \\\(M=m\+5|Wiens förskjutningslag:|Stefan–Boltzmanns lag för en stjärna|Wiens konstant är|Wiens lag: /,`${t.id}${x.etikett||''}`);
    assert.doesNotMatch(x.t||'',/<p>\s*<\/p>/,`${t.id}${x.etikett||''}`);
  }
  for(const id of ['5.8','5.315','6.51'])assert.doesNotMatch(get(id).s,/Skriv reaktionen|masskillnaden|Antalet kärnor/,id);
});

test('Delkort har egna rättningsfält och svarsinstruktion',()=>{
  for(const t of I.filter(t=>Array.isArray(t.spelDelar)&&t.svarstyp==='flera_delar')){
    assert.equal(t.rättSvar.length,t.spelDelar.length,t.id);
    t.spelDelar.forEach((d,i)=>{
      if(Array.isArray(d.alternativ)){assert.equal(d.alternativ.filter(a=>a.ratt).length,1,t.id+d.etikett);assert.equal(t.rättSvar[i],d.alternativ.find(a=>a.ratt).txt,t.id+d.etikett);}
      else if(['5.2','5.16','5.19','5.20','5.25','5.27','5.37','5.49','5.53','5.54','5.349','5.350','5.351','5.352'].includes(t.id))assert.ok(/\(Svara [^)]*\.\)/.test(d.t)||[].concat(t.svarEnhet)[i],t.id+d.etikett);
    });
  }
});

test('Omgjorda kort: facit räknas om',()=>{
  const d=a=>3474/(2*Math.tan(a/2*Math.PI/180));
  assert.ok(nara(v('5.17')[0],d(0.491))&&nara(v('5.17')[1],d(0.568)));
  assert.ok(nara(v('5.18')[0],6779/62e6*ARC)&&nara(v('5.18')[1],12104/45e6*ARC));assert.equal(v('5.18')[2],'Venus');
  assert.ok(nara(v('5.21')[0],11.4/LY)&&nara(v('5.21')[1],LY/11.4));
  assert.ok(nara(v('5.22')[0],LY/0.7685)&&nara(v('5.22')[1],LY/0.7685*0.0002/0.7685));
  assert.ok(Math.abs(v('5.23')-1/(1/0.54831+110e3*100*365.25*86400/PC))<1e-6);
  const r28=v('5.28');assert.ok(nara(r28[3],4+5-5*Math.log10(25))&&nara(r28[5],-1.5-5+5*Math.log10(20)));assert.deepEqual([r28[0],r28[2],r28[4],r28[6],r28[7]],[10,0.04,20,100,0.01]);
  assert.ok(nara(v('5.29')[0],10**(32.74/5)/ARC,1e-5));
  const M53=-2.81*Math.log10(30)-1.43,d53=10**((24-M53+5)/5)/1e6;assert.ok(nara(v('5.53')[0],M53)&&nara(v('5.53')[1],d53)&&nara(v('5.53')[2],70*d53));
  assert.ok(nara(v('5.54')[0][0],1.8**2*(12000/5772)**4)&&nara(v('5.54')[1][1],2.898e-3/3200*1e9));
  assert.ok(nara(v('5.16')[0],0.6/(2*Math.PI/180))&&nara(v('5.25')[0],10**(7.8/5)));
  assert.ok(nara(v('5.9'),1e4*3**-2.5));assert.equal(v('5.8'),0.25);assert.deepEqual(v('5.3'),[1,'lika']);
});

test('Nya kort: facit räknas om och toleransen tål M☉ = 4,83 och T☉ = 5 778 K',()=>{
  const nya=B.filter(t=>t.kap===5&&+t.id.split('.')[1]>=447&&+t.id.split('.')[1]<=463);assert.equal(nya.length,17);
  for(const t of nya){assert.ok(/\(Svara [^)]*\.\)<\/p>|<\/table><p>Vilken|Vilken ordning|störst luminositet\?<\/p>/.test(t.t.replace(/<svg[\s\S]*?<\/svg>/g,''))||[].concat(t.svarEnhet).some(Boolean),t.id);assert.ok(t.traningsniva>=1,t.id);}
  const kedja=(p,m,T,Msol=4.74,Tsol=5772)=>{const d=1/p,M=m+5-5*Math.log10(d),L=10**(0.4*(Msol-M)),R=Math.sqrt(L)*(Tsol/T)**2;return [d,M,L,R];};
  const inom=(t,i,x)=>Math.abs(x-t.rättSvar[i])<=t.tolerans[i];
  for(const [id,p,m,T] of [['5.447',0.0889,-0.05,4290]]){const t=get(id);kedja(p,m,T).forEach((x,i)=>assert.ok(nara(x,t.rättSvar[i]),id+i));
    const alt=kedja(p,m,T,4.83,5778);[2,3].forEach(i=>assert.ok(inom(t,i,alt[i]),`${id} del ${i} med 4,83`));}
  {const t=get('5.455'),k=kedja(0.25,9.0,12000);[1,2,3].forEach((i,j)=>assert.ok(nara(k[i],t.rättSvar[j]),'5.455'));const a=kedja(0.25,9.0,12000,4.83,5778);assert.ok(inom(t,1,a[2])&&inom(t,2,a[3]));}
  {const t=get('5.457'),T=2.898e-3/500e-9,k=kedja(0.1,4.0,T);assert.ok(nara(t.rättSvar[0],T));[1,2,3].forEach(i=>assert.ok(nara(k[i],t.rättSvar[i])));const a=kedja(0.1,4.0,T,4.83,5778);assert.ok(inom(t,2,a[2])&&inom(t,3,a[3]));}
  {const t=get('5.454'),T=2.898e-3/290e-9;assert.ok(nara(t.rättSvar[0],T)&&nara(t.rättSvar[1],100*(5772/T)**2));}
  assert.ok(nara(v('5.448'),4.74-7.5)&&Math.abs((4.83-7.5)-v('5.448'))<=get('5.448').tolerans);
  assert.equal(v('5.449'),10);assert.ok(nara(v('5.450'),10**(0.4*3.44)));assert.ok(nara(v('5.451'),-1.46+5-5*Math.log10(2.64)));
  assert.ok(nara(v('5.453'),10**2.5));assert.equal(v('5.456'),10);assert.ok(nara(v('5.458'),10*(5772/4500)**2));assert.equal(v('5.459'),9);
  assert.equal(v('5.460'),50);assert.ok(nara(v('5.461'),1361/1.52**2));assert.ok(nara(v('5.462')[0],4*Math.PI*(10*PC)**2*2e-9));
  assert.equal(get('5.452').alternativ.find(a=>a.ratt).txt,'B');assert.match(get('5.463').alternativ.find(a=>a.ratt).txt,/^Radar, parallax, cepheider/);
});
