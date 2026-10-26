'use strict';
/* Ma4 trig_ekv_formler: 1.201, 1.240, 1.290 och 1.704 var mallkloner (validatorn: EXACT_TEXT_DUPLICATE).
   2026-10-26 fick 1.240, 1.290 och 1.704 nya former av samma ekvation och alla fyra facit som 1.116. Svaren prövas i ekvationerna. */
const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('node:fs'),vm=require('node:vm'),path=require('node:path');
const c={window:{}};vm.runInNewContext(fs.readFileSync(path.join(__dirname,'..','uppgiftermato2.js'),'utf8'),c);
const B=JSON.parse(JSON.stringify(c.window.BANKMATO2)),get=id=>B.find(x=>x.id===id);
const S=v=>Math.sin(v*Math.PI/180),C=v=>Math.cos(v*Math.PI/180),nara=(a,b,id)=>assert.ok(Math.abs(a-b)<1e-9,id);
test('Fyra olika former med rubriker i varje steg och svarsrad',()=>{
  const former={'1.201':'2\\sin^2x+\\sin x-1=0','1.240':'2\\cos^2x+\\sin x=1','1.290':'\\cos x\\,(2\\cos x+1)=1','1.704':'2\\cos^2x=\\cos x+1'};
  for(const [id,ekv] of Object.entries(former)){const t=get(id);assert.ok(t.t.includes(ekv),id);assert.equal(t.omr,'trig_ekv_formler');
    const steg=[...t.s.matchAll(/<li>([\s\S]*?)<\/li>/g)];assert.ok(steg.length>=4,id);for(const m of steg)assert.match(m[1],/^<p class="facit-rubrik">/,id);
    assert.match(t.s,/class="facit-svar"/,id);assert.ok(t.ledtrad.length>40,id);}
});
test('Svaren uppfyller ekvationerna och inga lösningar saknas',()=>{
  const ekv={'1.201':x=>2*S(x)**2+S(x)-1,'1.240':x=>2*C(x)**2+S(x)-1,'1.290':x=>C(x)*(2*C(x)+1)-1,'1.704':x=>2*C(x)**2-C(x)-1};
  for(const [id,f] of Object.entries(ekv)){const svar=get(id).rättSvar.map(Number);for(const x of svar)nara(f(x),0,id);
    const max=id==='1.704'?360:359;const alla=[];for(let x=0;x<=max;x++)if(Math.abs(f(x))<1e-9)alla.push(x);assert.deepEqual(alla,svar,id);}
});
