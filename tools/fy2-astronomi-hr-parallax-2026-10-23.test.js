'use strict';
/* 2026-10-23: 47 kort om HR-diagram (med verkliga stjärnor), magnituder, parallax och stjärnors utveckling (5.400–5.446). */
const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('node:fs'),vm=require('node:vm'),path=require('node:path');
const c={window:{}};vm.runInNewContext(fs.readFileSync(path.join(__dirname,'..','uppgifter2.js'),'utf8'),c);
const nya=JSON.parse(JSON.stringify(c.window.BANK2.filter(t=>{const [k,n]=t.id.split('.').map(Number);return k===5&&n>=400&&n<=446;})));
const typ=s=>{const t=nya.filter(x=>x.typ===s);assert.equal(t.length,1,s);return t[0];};
const v=s=>typ(s).rättSvar,ratt=s=>typ(s).alternativ.find(a=>a.ratt).txt;
const utanSvg=h=>h.replace(/<svg[\s\S]*?<\/svg>/g,'').replace(/<table[\s\S]*?<\/table>/g,'');
const nara=(a,b,rel=1e-9)=>Math.abs(a-b)<=Math.abs(b)*rel+1e-12;

test('47 kort i fysikformat, inga formler eller konstanter i frågan',()=>{
  assert.equal(nya.length,47);const per={};
  for(const t of nya){per[t.omr]=(per[t.omr]||0)+1;
    assert.equal(t.miniräknare,true,t.id);assert.match(t.poang,/^\(\d\/\d\/\d\)$/,t.id);assert.ok(t.traningsniva>=1&&t.traningsniva<=3,t.id);
    assert.doesNotMatch(utanSvg(t.t),/5\s*\\?lg|10\^|2,898|5,67|4,74|3,26|206\s?265|\\sigma|\\lambda_\{?max/,t.id);
    if(t.svarstyp==='alternativ')assert.equal(t.alternativ.filter(a=>a.ratt).length,1,t.id);
    else assert.ok(/\(Svara [^)]*\.\)<\/p>$/.test(utanSvg(t.t))||[].concat(t.svarEnhet).some(Boolean),t.id);
    if(/HR-diagram/.test(t.t)&&/<svg/.test(t.t))assert.match(t.t,/verkliga stjärnor/,t.id);
  }
  assert.deepEqual(per,{farg_ljusstyrka:19,magnituder:12,avstandsmatning:11,stjarnornas_utveckling:5});
});

test('Facit räknas om',()=>{
  const r=(m,M)=>10**((m-M+5)/5);
  assert.equal(v('läsa absolut magnitud'),-5);assert.equal(v('läsa yttemperatur'),10000);assert.equal(v('läsa luminositet'),100);
  assert.equal(v('läsa luminositet under solens'),0.01);assert.equal(v('luminositetsförhållande ur diagram'),10000/100);
  assert.equal(v('stjärna på 10 parsecs avstånd'),3.2);assert.ok(nara(v('fem magnituder är faktor hundra'),10**(0.4*5)));assert.ok(nara(v('avståndsmodul tio'),r(10,0)));
  assert.ok(nara(v('absolut magnitud ur avstånd'),7+5-5*Math.log10(40)));assert.ok(nara(v('apparent magnitud ur avstånd'),-2-5+5*Math.log10(500)));
  assert.ok(nara(v('två och en halv magnitud'),10**(0.4*2.5)));assert.ok(nara(v('luminositet jämfört med solen'),10**(0.4*(4.74+0.26))));
  assert.deepEqual(v('avstånd med hjälp av HR-diagrammet'),[5,r(10,5)]);assert.ok(nara(v('avstånd till en röd jätte via HR-diagram'),r(7.5,0)));
  assert.ok(nara(v('avstånd ur parallax'),1/0.5));assert.ok(nara(v('parallax ur avstånd'),1/20));assert.ok(nara(v('parsec till ljusår'),2.4*3.2616));
  assert.ok(nara(v('parallax ur bildförskjutning'),1/(0.4/2)));assert.equal(v('ljusets gångtid från Sirius'),8.6);assert.equal(v('lika ljusstarka stjärnor på olika avstånd'),9);
  assert.ok(Math.abs(v('en parsec i astronomiska enheter')-206265)<1);assert.ok(nara(v('Gaia mäter i millibågsekunder'),1/0.0025));
  assert.ok(nara(v('temperatur ur strålningsmaximum'),2.898e-3/600e-9));assert.ok(nara(v('radie ur luminositet och temperatur'),Math.sqrt(1/0.5**4)));
  // Avläsningar ur diagrammen, med tolerans för avläsningen
  assert.ok(Math.abs(v('huvudseriestjärna ur bandet')-4.4)<0.01&&typ('huvudseriestjärna ur bandet').tolerans>=0.8);
  assert.ok(Math.abs(v('läsa av Rigels absoluta magnitud')-(-7.8))<0.01);assert.ok(Math.abs(v('läsa av Aldebarans temperatur')-3910)<=typ('läsa av Aldebarans temperatur').tolerans);
  assert.equal(ratt('varmaste stjärnan'),'A');assert.equal(ratt('hitta den vita dvärgen'),'D');assert.equal(ratt('störst radie'),'E');assert.equal(ratt('minst radie'),'D');
  assert.equal(ratt('spektralklass ur diagrammet'),'K');assert.equal(ratt('ljusast på himlen'),'Sirius');assert.equal(ratt('vit dvärg bland kända stjärnor'),'Sirius B');
  assert.equal(ratt('störst radie bland kända stjärnor'),'Betelgeuse');
});

test('Radier stämmer med Stefan–Boltzmann, även för de verkliga stjärnorna',()=>{
  const R=(T,M)=>Math.sqrt(10**(0.4*(4.74-M)))/(T/5800)**2,stor=o=>Object.entries(o).sort((a,b)=>b[1]-a[1]).map(x=>x[0]);
  const st={A:[20000,-5],B:[10000,1],C:[4000,0],D:[15000,12],E:[3500,-7],F:[3200,12]};
  const r=stor(Object.fromEntries(Object.entries(st).map(([k,[T,M]])=>[k,R(T,M)])));assert.equal(r[0],'E');assert.equal(r[r.length-1],'D');
  const k={Betelgeuse:[3500,-5.9],Rigel:[12100,-7.8],Aldebaran:[3910,-0.6],'Sirius A':[9940,1.4],'Sirius B':[25000,11.2],Solen:[5772,4.8],'Proxima Centauri':[3040,15.5]};
  const rk=stor(Object.fromEntries(Object.entries(k).map(([n,[T,M]])=>[n,R(T,M)])));assert.equal(rk[0],'Betelgeuse');assert.equal(rk[rk.length-1],'Sirius B');
});
