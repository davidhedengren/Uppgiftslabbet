'use strict';
const{test}=require('node:test'),assert=require('node:assert/strict'),fs=require('node:fs'),vm=require('node:vm'),path=require('node:path');
const c={window:{}};for(const f of ['uppgifter.js','uppgifterma2.js','uppgiftermatf1.js'])vm.runInNewContext(fs.readFileSync(path.join(__dirname,'..',f),'utf8'),c);const q=(bank,id)=>c.window[bank].find(t=>t.id===id);
test('Rapporterad fysik och fem effektanalogier följer oberoende modeller',()=>{
 const models=[['5.564',[650*(9.82*1.75/2+1.75**2/(2*3)),650*9.82*1.75,3000*9.82*21/23]],['5.563',[1080*((95-65)/3.6)/7,1300*80/3.6]],['5.565',[850*15**2/2/(40*735.5),(850*15**2/2+850*9.82*3)/(40*735.5)]],['5.566',[1200*9.82*25*15/Math.hypot(100,15),(710*9.82*Math.sin(2*Math.PI/180)+500)*23,(950*9.82*Math.sin(5*Math.PI/180)+600)*30]],['5.567',[200+90*9.82*6*Math.sin(10*Math.PI/180),200/(30+90*9.82*Math.sin(10*Math.PI/180))]],['5.568',[Math.asin((45*735.5/(50/3.6)-300)/(1000*9.82))*180/Math.PI]]];
 for(const[id,vals]of models){const t=q('BANK',id);for(const[i,v]of vals.entries()){const stored=Array.isArray(t.rättSvar)?t.rättSvar[i]:t.rättSvar;assert.ok(Math.abs(v-stored)<1e-9*Math.max(1,Math.abs(v)),id);}}
 assert.equal(q('BANK','6.241').rättSvar,19640*.024/9.82);
 assert.ok(Math.abs(q('BANK','6.65').rättSvar[0]-(101300+998*9.82*3.5)/1000)<1e-10);
 assert.equal(q('BANK','6.553').rättSvar,2);
});
test('Funktionskort, logaritmsvar och mängdantal stämmer utan osynliga tidigare delar',()=>{
 const t=q('BANKMA2','2.378');assert.ok(Math.abs(3*1.4**t.rättSvar-20)<1e-12);assert.ok(Math.abs(t.rättSvar-5.64)<t.tolerans);assert.ok(Math.abs(t.rättSvar-5.65)>t.tolerans);
 const f=q('BANKMA2','2.137');assert.equal(f.spelDelar[1].svarFormat,'uttryck');assert.match(f.spelDelar[1].t,/\(x\+4\)\(x-3\)/);for(const x of [-4,3,0,2])assert.ok(Math.abs((x+4)*(x-3)-(x*x+x-12))<1e-12);
 const r=q('BANKMA2','2.731');for(const sign of [-1,1]){const x=Math.sqrt(3)+sign*Math.sqrt(2);assert.ok(Math.abs(x*x-2*Math.sqrt(3)*x+1)<1e-12);}assert.equal(r.svarsstruktur,'mängd');
 for(const[id,n]of [['1.565',3],['1.566',4],['1.567',5]]){const t=q('BANKMATF1',id);assert.equal(t.rättSvar,Array.from({length:1<<n},(_,mask)=>mask).length);assert.match(t.t,/tomma mängden/);assert.equal(t.traningsniva,2);}
});
