'use strict';
/* Ma2 kap 3, revision 2026-10-25 efter lärarens granskning:
   – ingen figur har texten ”Skiss. Mät inte i figuren.”;
   – de 30 korten med mallfigurer har skalenliga figurer som skiljer sig från varandra;
   – 13 kort i sats_bevis är omformulerade (färre nästan identiska kort);
   – 12 nya varianter av lärarens exempeluppgifter (3.2162–3.2173). */
const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('node:fs'),vm=require('node:vm'),path=require('node:path');
const src=fs.readFileSync(path.join(__dirname,'..','uppgifterma2.js'),'utf8');
const c={window:{}};vm.runInNewContext(src,c);
const B=JSON.parse(JSON.stringify(c.window.BANKMA2));const get=id=>{const t=B.find(x=>x.id===id);assert.ok(t,id);return t;};
const svgar=q=>[q.t,...(q.spelDelar||[]).flatMap(d=>Object.values(d).filter(v=>typeof v==='string'))].join('').match(/<svg[\s\S]*?<\/svg>/g)||[];
const MALL=['3.08','3.97','3.101','3.102','3.110','3.131','3.163','3.165','3.185','3.186','3.260','3.261','3.262','3.298','3.313','3.337','3.338','3.22','3.26','3.60','3.148',
  '3.35','3.48','3.77','3.81','3.285','3.297','3.311','3.150','3.153'];

test('Ingen figur har texten ”Skiss. Mät inte i figuren.”',()=>{
  assert.equal((src.match(/Mät inte i figuren/g)||[]).length,0);
});

test('Mallfigurerna är ersatta med egna figurer per kort',()=>{
  const sett=new Map();
  for(const id of MALL){const s=svgar(get(id));assert.equal(s.length,1,id);assert.match(s[0],/aria-label="[^"]{25,}"/,id);assert.doesNotMatch(s[0],/DE ∥ BC/,id);
    const nyckel=s[0].replace(/aria-label="[^"]*"/,'');assert.ok(!sett.has(nyckel),`${id} har samma figur som ${sett.get(nyckel)}`);sett.set(nyckel,id);}
  // 3.313 var en exakt dubblett av 3.298 och fick nya tal.
  assert.equal(get('3.313').rättSvar,16.5);assert.equal(get('3.298').rättSvar,12);
  assert.notEqual(get('3.313').t.replace(/<svg[\s\S]*<\/svg>/,''),get('3.298').t.replace(/<svg[\s\S]*<\/svg>/,''));
});

test('Omformulerade kort i sats och bevis',()=>{
  const ratt=id=>get(id).alternativ.filter(a=>a.ratt).map(a=>a.txt);
  assert.match(get('3.72').t,/n\^2\+n\+41/);assert.equal(ratt('3.72').length,1);
  assert.equal(get('3.348').svarstyp,'numeriskt');assert.equal(get('3.348').rättSvar,3);assert.equal(get('3.348').alternativ,undefined);
  assert.deepEqual(ratt('3.250'),['Noah']);assert.deepEqual(ratt('3.281'),['Nej']);assert.deepEqual(ratt('3.356'),['Sant']);assert.match(get('3.356').t,/x\^3=8/);
  assert.deepEqual(ratt('3.248'),['Sant']);assert.deepEqual(ratt('3.83'),['\\(\\Leftrightarrow\\)']);assert.deepEqual(ratt('3.249'),['Nej']);
  assert.match(get('3.300').t,/slutar på siffran 0/);assert.deepEqual(ratt('3.329'),['Nej']);assert.equal(get('3.329').rättSvar,'Nej');
  for(const id of ['3.106','3.104','3.40'])assert.match(get(id).t,/reellt tal/,id);
});

test('Tolv varianter av lärarens exempeluppgifter',()=>{
  const ids=Array.from({length:12},(_,i)=>`3.${2162+i}`);
  const forv={'3.2162':40,'3.2163':30,'3.2164':'3*sqrt(3)/2*s^2','3.2169':7.2,'3.2170':5,'3.2171':'10*sqrt(6)','3.2173':'2/3'};
  for(const id of ids){const k=get(id),[e,cc,a]=k.poang.split('/').map(Number);assert.equal(k.niva,a?'A':cc?'C':'E',id);
    assert.ok(k.niva==='E'?k.traningsniva<=2:k.niva==='C'?[3,4].includes(k.traningsniva):k.traningsniva>=4,id);
    if(id in forv)assert.equal(k.rättSvar,forv[id],id);else assert.equal(k.alternativ.filter(x=>x.ratt).length,1,id);
    if(id!=='3.2168')assert.equal(svgar(k).length,1,id);}
  assert.equal(get('3.2173').svarFormat,'bråk');
  // Vinkelbågarna i figurerna har de storlekar som etiketterna anger.
  const bagar=id=>(get(id).t.match(/<path d="M [^"]+"/g)||[]).map(p=>{const[,sx,sy,r,ex,ey]=p.match(/M ([\d.-]+) ([\d.-]+) A ([\d.]+) [\d.]+ 0 0 [01] ([\d.-]+) ([\d.-]+)/).map(Number);return 2*Math.asin(Math.min(1,Math.hypot(ex-sx,ey-sy)/(2*r)))*180/Math.PI;});
  for(const[id,v]of Object.entries({'3.2162':[115,40],'3.2163':[70,30],'3.2165':[75,25,100]})){const b=bagar(id);b.forEach((x,i)=>assert.ok(Math.abs(x-v[i])<1,`${id}: ${x} ≠ ${v[i]}`));}
});
