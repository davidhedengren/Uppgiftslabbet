'use strict';
/* Felrapport 2026-10-23 10:33: stjärnkort utan formelsamlingsvärden, inga nästan-dubbletter, ingen "bolometrisk". */
const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('node:fs'),vm=require('node:vm'),path=require('node:path');
const c={window:{}};vm.runInNewContext(fs.readFileSync(path.join(__dirname,'..','uppgifter2.js'),'utf8'),c);
const B=JSON.parse(JSON.stringify(c.window.BANK2));const get=id=>{const t=B.find(x=>x.id===id);assert.ok(t,id);return t;};const v=id=>get(id).rättSvar;
const st=h=>(h||'').replace(/<svg[\s\S]*?<\/svg>/g,'').replace(/<[^>]+>/g,' ');
const nara=(a,b,rel=1e-6)=>Math.abs(a-b)<=Math.abs(b)*rel+1e-12;
const SIG=5.670374419e-8,PC=3.0856775814913673e16;
// Formelsamlingar skiljer sig något: svaren ska godtas med alla dessa kombinationer.
const ALT=[];for(const Ms of [4.74,4.83])for(const Ts of [5772,5778,5800])for(const Ls of [3.828e26,3.846e26,3.85e26])ALT.push({Ms,Ts,Ls});

test('Ingen "bolometrisk" någonstans i Fy2',()=>{assert.deepEqual(B.filter(t=>/bolometri/i.test(JSON.stringify(t))).map(t=>t.id),[]);});

test('Inga formelsamlingsvärden i stjärnkortens frågor',()=>{
  const re=/5\{?,\}?67|3\{?,\}?828|6\{?,\}?957|5\s?77[28]\s?K|5 800 K|4\{?,\}?74|1\{?,\}?932|2\{?,\}?898|Wiens konstant|\\sigma|σ|Bortse från absorption/;
  for(const t of B.filter(t=>t.kap===5))for(const x of [t,...(t.spelDelar||[])])assert.doesNotMatch(st(x.t),re,`${t.id}${x.etikett||''}`);
});

test('5.356–5.368 är nya stjärnor, inte dubbletter av 5.31–5.42',()=>{
  const namn=id=>st(get(id).t);
  for(const [id,ord] of [['5.356','Altair'],['5.357','Wolf 359'],['5.358','Canopus'],['5.360','Alkaid'],['5.361','Bellatrix'],['5.362','Aldebaran'],['5.365','Vega'],['5.366','Antares'],['5.367','Sirius'],['5.368','Hamal']])assert.match(namn(id),new RegExp(ord),id);
  for(const [a,b] of [['5.365','5.39'],['5.366','5.40'],['5.368','5.42'],['5.361','5.33'],['5.362','5.34'],['5.357','5.31'],['5.363','5.37']])assert.notEqual(namn(a).slice(0,60),namn(b).slice(0,60),a+' '+b);
});

test('Nya facit räknas om och toleranserna tål olika formelsamlingar',()=>{
  const inom=(id,i,x)=>{const t=get(id),r=Array.isArray(t.rättSvar)?t.rättSvar[i]:t.rättSvar,tol=Array.isArray(t.tolerans)?t.tolerans[i]:t.tolerans;return Math.abs(x-r)<=tol;};
  const kolla=(id,i,f)=>{const r=Array.isArray(v(id))?v(id)[i]:v(id);assert.ok(nara(r,f({Ms:4.74,Ts:5772,Ls:3.828e26}),1e-9),`${id}[${i}] facit`);for(const a of ALT)assert.ok(inom(id,i,f(a)),`${id}[${i}] med ${JSON.stringify(a)}`);};
  kolla('5.356',0,({Ms})=>10**(0.4*(Ms-2.2)));kolla('5.357',0,({Ms})=>Ms+7.5);kolla('5.358',0,({Ms})=>Ms-2.5*Math.log10(10700));
  const L360=4*Math.PI*2.37e9**2*SIG*15500**4;assert.ok(nara(v('5.360')[0],L360));kolla('5.360',1,({Ms,Ls})=>Ms-2.5*Math.log10(L360/Ls));
  kolla('5.361',0,({Ms})=>10**(0.4*(Ms+2.8)));kolla('5.361',1,({Ms,Ts})=>Math.sqrt(10**(0.4*(Ms+2.8)))*(Ts/22000)**2);
  kolla('5.362',0,({Ts})=>Ts*(440/44**2)**0.25);kolla('5.362',1,({Ms})=>Ms-2.5*Math.log10(440));
  assert.ok(nara(v('5.363')[0],9*0.8**4)&&nara(v('5.363')[1],2.5*Math.log10(9*0.8**4)));
  assert.deepEqual(v('5.364').slice(1),[10000,80]);
  kolla('5.365',0,({Ts})=>2.7**2*(9600/Ts)**4);kolla('5.365',1,({Ms,Ts})=>Ms-2.5*Math.log10(2.7**2*(9600/Ts)**4));
  const M366=1+5-5*Math.log10(1/0.0059);assert.ok(nara(v('5.366')[0],1/0.0059)&&nara(v('5.366')[1],M366));kolla('5.366',2,({Ms})=>10**(0.4*(Ms-M366)));kolla('5.366',3,({Ms,Ts})=>Math.sqrt(10**(0.4*(Ms-M366)))*(Ts/3600)**2);
  kolla('5.367',0,({Ms,Ts})=>{const L=1.711**2*(9940/Ts)**4,M=Ms-2.5*Math.log10(L);return 1/10**((-1.47-M+5)/5);});
  const d368=1/0.0496,M368=2+5-5*Math.log10(d368);assert.ok(nara(v('5.368')[0],M368)&&nara(v('5.368')[1],2.898e-3/650e-9));
  kolla('5.368',2,({Ms,Ls})=>10**(0.4*(Ms-M368))*Ls/(4*Math.PI*(d368*PC)**2));
  // äldre kort där solens värden togs bort ur texten
  kolla('5.31',0,({Ms,Ls})=>Ms-2.5*Math.log10(6.89e23/Ls));kolla('5.33',0,({Ms,Ts})=>Math.sqrt(10**(0.4*(Ms+3.55)))*(Ts/21000)**2);
  kolla('5.34',0,({Ms,Ts})=>Ts*(10**(0.4*(Ms+6.93))/203**2)**0.25);kolla('5.30',1,({Ms,Ls})=>10**(0.4*(Ms-0.58))*Ls);
});

test('Rapporterade kort',()=>{
  for(const id of ['5.314','5.324'])assert.match(get(id).t,/<svg[\s\S]*verkliga stjärnor/,id);
  assert.equal(get('5.323').traningsniva,3);assert.match(get('5.323').ledtrad,/R\^2/);
  const p=get('2.498');assert.doesNotMatch(p.t,/2\\pi\\sqrt/);assert.match(p.spelDelar[1].t,/pendeln vara för att få perioden 1,0 s på månen\? \(Svara i m\.\)/);
});

test('Enheten heter AU, inte AE, och kapitel 5 har inga självrättade kort',()=>{
  const k5=B.filter(t=>t.kap===5);
  assert.deepEqual(k5.filter(t=>/(?<![A-Za-zÅÄÖåäö0-9+\/=])AE(?![A-Za-zÅÄÖåäö0-9+\/=])/.test(JSON.stringify(t))).map(t=>t.id),[]);
  assert.equal(get('5.440').svarEnhet,'AU');assert.equal(get('5.5').svarEnhet,'AU');
  assert.deepEqual(k5.filter(t=>t.svarstyp==='manuell'||t.självrättning===false||(Array.isArray(t.självrättning)&&t.självrättning.includes(false))).map(t=>t.id),[]);
  assert.deepEqual(k5.filter(t=>t.traningsniva==null).map(t=>t.id),[]);
});
