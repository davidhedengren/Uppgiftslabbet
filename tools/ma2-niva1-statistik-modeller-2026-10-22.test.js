'use strict';
/* Påfyllnad 2026-10-22: 39 kort på träningsnivå 1 i Ma2 (4.500–4.530 och 2.900–2.907). */
const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('node:fs'),vm=require('node:vm'),path=require('node:path');
const c={window:{}};vm.runInNewContext(fs.readFileSync(path.join(__dirname,'..','uppgifterma2.js'),'utf8'),c);
const bank=c.window.BANKMA2;
const inom=(id,k,a,b)=>{const [kk,n]=id.split('.').map(Number);return kk===k&&n>=a&&n<=b;};
const nya=bank.filter(t=>inom(t.id,4,500,530)||inom(t.id,2,900,907));
const get=id=>nya.find(t=>t.id===id);
const Phi=x=>{const t=1/(1+.2316419*Math.abs(x)),d=.3989423*Math.exp(-x*x/2),p=d*t*(.3193815+t*(-.3565638+t*(1.781478+t*(-1.821256+t*1.330274))));return x>0?1-p:p;};
const andel=(mu,s,a,b)=>100*((b==null?1:Phi((b-mu)/s))-(a==null?0:Phi((a-mu)/s)));

test('39 nya kort på nivå 1 med figur eller tabell',()=>{
  assert.equal(nya.length,39);
  const per={};for(const t of nya){per[t.omr]=(per[t.omr]||0)+1;
    assert.equal(t.traningsniva,1,t.id);assert.equal(t.spel,true,t.id);
    assert.match(t.t,/<svg|<table/,t.id);
    if(t.svarstyp==='alternativ')assert.equal(t.alternativ.filter(a=>a.ratt).length,1,t.id);else assert.ok(Number.isFinite(t.rättSvar),t.id);}
  assert.deepEqual(per,{tabeller_diagram:12,kvartiler_percentiler:10,normalfordelning_digitala_verktyg:9,regressionsanalys_olika_modeller:8});
  for(const t of nya.filter(t=>t.omr==='normalfordelning_digitala_verktyg'))assert.equal(t.geogebra,true,t.id);
});

test('Normalfördelningsandelar räknas om ur texten',()=>{
  const fall={'4.522':[150,20,null,175],'4.523':[800,15,820,null],'4.524':[167,6,null,160],'4.525':[200,4,null,195],'4.526':[1000,8,990,1010],'4.527':[9,0.6,null,8.5],'4.530':[25,4,32,null]};
  const svar=[];
  for(const [id,[mu,s,a,b]] of Object.entries(fall)){const t=get(id);const v=andel(mu,s,a,b);
    assert.ok(Math.abs(t.rättSvar-Math.round(v*10)/10)<1e-9,`${id}: ${t.rättSvar} ≠ ${v}`);
    assert.match(t.t.replace(/<svg[\s\S]*?<\/svg>/g,''),new RegExp(String(mu).replace('.','\\{,\\}')));svar.push(t.rättSvar);}
  assert.equal(new Set(svar).size,svar.length);
});

test('Övriga facit räknas om',()=>{
  const fall={'4.501':50-20,'4.504':0.25*200,'4.506':11+14+9+16,'4.507':7+4+2,'4.508':18-12,'4.509':6100-4200,'4.511':0.5*40,
    '4.512':11,'4.513':(18+22)/2,'4.515':30-12,'4.517':3,'4.518':0.9*200,'4.519':50,'2.903':3.5*4+12,'2.904':(1-0.85)*100,'2.906':40};
  for(const [id,v] of Object.entries(fall))assert.ok(Math.abs(get(id).rättSvar-v)<1e-9,id);
});
