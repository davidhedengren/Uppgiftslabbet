'use strict';
const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('node:fs'),vm=require('node:vm'),path=require('node:path');
const las=(fil,nyckel)=>{const c={window:{}};vm.runInNewContext(fs.readFileSync(path.join(__dirname,'..',fil),'utf8'),c);return c.window[nyckel];};
const fy1=las('uppgifter.js','BANK'),fy2=las('uppgifter2.js','BANK2'),ma2=las('uppgifterma2.js','BANKMA2');
const hitta=(b,id)=>{const t=b.find(x=>x.id===id);assert.ok(t,id);return t;};
const del=(t,e)=>t.spelDelar.find(d=>d.etikett===e);
const utanSvg=h=>h.replace(/<svg[\s\S]*?<\/svg>/g,'');

test('fy2 3.161–3.172: ledaren syns i figuren och facit följer F = IL × B',()=>{
  const E={höger:[1,0,0],vänster:[-1,0,0],uppåt:[0,1,0],nedåt:[0,-1,0],ut:[0,0,1],in:[0,0,-1]};
  // Sedan 2026-10-24 är korten riktiga flervalskort som appen blandar; rätt alternativ jämförs i stället för bokstaven.
  const SV={'1,0,0':'höger','-1,0,0':'vänster','0,1,0':'uppåt','0,-1,0':'nedåt','0,0,-1':'in i pappret','0,0,1':'ut ur pappret'};
  for(let k=161;k<=172;k++){
    const t=hitta(fy2,`3.${k}`);
    assert.match(t.t,/stroke="#b87333"/,t.id);
    const m=t.t.match(/aria-label="Strömförande ledare med strömmen (\S+)(?: ur pappret| i pappret)? i ett magnetfält ([^\s"]+)/);
    assert.ok(m,t.id);const i=E[m[1]],b=E[m[2]];
    const f=[i[1]*b[2]-i[2]*b[1],i[2]*b[0]-i[0]*b[2],i[0]*b[1]-i[1]*b[0]].map(x=>x+0);
    assert.equal(SV[f.join(',')],t.alternativ.find(a=>a.ratt).txt,t.id);
  }
});

test('fy2 spolar och slingor: pilarna i figuren går åt samma håll som texten',()=>{
  const ids=[185,186,187,188,189,190,191,192,...Array.from({length:12},(_,i)=>209+i)].map(k=>`3.${k}`);
  for(const id of ids){
    const t=hitta(fy2,id),text=utanSvg(t.t);
    const medurs=/medurs/.test(text);assert.notEqual(medurs,/moturs/.test(text),id);
    const c=t.t.match(/<circle cx="(\d+)" cy="(\d+)" r="66"/);assert.ok(c,id);
    const [cx,cy]=[+c[1],+c[2]];
    const pilar=[...t.t.matchAll(/<polygon points="([^"]+)" fill="#b54b42"/g)].map(m=>m[1].split(' ').map(p=>p.split(',').map(Number)));
    assert.equal(pilar.length,4,id);
    for(const [tip,b1,b2] of pilar){
      const bas=[(b1[0]+b2[0])/2,(b1[1]+b2[1])/2],d=[tip[0]-bas[0],tip[1]-bas[1]],r=[bas[0]-cx,bas[1]-cy];
      assert.equal(r[0]*d[1]-r[1]*d[0]>0,medurs,id);   // y nedåt: positivt kryss är medurs på skärmen
    }
  }
});

test('fy2 6.12 godtar både c = 3,00·10^8 och c = 2,998·10^8 m/s',()=>{
  const t=hitta(fy2,'6.12');
  const L=c=>135*Math.sqrt(1-(2.90e8/c)**2);
  assert.ok(Math.abs(t.rättSvar-L(3.00e8))<1e-9);assert.ok(Math.abs(t.svarTabell[0][0]-L(299792458))<1e-9);
  assert.equal(t.tolerans,0.4);assert.match(t.s,/34\{,\}2/);
});

test('Nivåer enligt lärarens rapporter',()=>{
  assert.equal(hitta(fy2,'6.30').traningsniva,5);assert.equal(hitta(fy1,'5.396').traningsniva,5);
  const a=hitta(fy1,'5.123');assert.equal(del(a,'a').traningsniva,4);assert.equal(del(a,'b').traningsniva,5);
  assert.equal(del(hitta(fy1,'5.225'),'a').traningsniva,5);
});

test('fy1-texter: precision, frågor och självbärande delkort',()=>{
  assert.doesNotMatch(JSON.stringify(hitta(fy1,'5.95')),/Avrunda/);
  const p=hitta(fy1,'5.117');assert.match(p.t,/0,12 s\?/);assert.match(p.t,/0,020 s\?/);
  for(const e of 'ab')assert.match(del(p,e).t,/under inbromsningen/);
  const f=hitta(fy1,'5.97');assert.match(del(f,'a').t,/energi är lagrad/);assert.doesNotMatch(f.t,/från början/);
  const b=hitta(fy1,'5.382');assert.match(del(b,'b').t,/13 m\/s/);assert.match(del(b,'b').t,/650 N/);
  assert.equal((b.t.match(/18 m\/s/g)||[]).length,1);
  const g=hitta(fy1,'9.415');assert.match(del(g,'a').t,/protons genomsnittliga rörelseenergi/);assert.match(del(g,'a').t,/2,0·10⁷ K/);
});

test('ma2 4.117: delkorten förklarar gränserna',()=>{
  const t=hitta(ma2,'4.117');
  assert.match(del(t,'a').fraga,/10 % snabbaste/);assert.match(del(t,'b').fraga,/10 % långsammaste/);
  assert.deepEqual([...t.rättSvar],[59.7,80.3]);
});
