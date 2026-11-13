'use strict';
// Felrapporter 2026-11-13 09:39 (Lars-Åke Andersson): ingen dopplereffekt i Fy2, inga separabla differentialekvationer
// och ingen allmän metod för att gå från rekursion till explicit formel i Ma5. Logg: agent/FELRAPPORTER_2026-11-13_0939.md.
const {test}=require('node:test'),a=require('node:assert/strict'),fs=require('node:fs'),vm=require('node:vm');
const las=(f,n)=>{const c={window:{}};vm.runInNewContext(fs.readFileSync(f,'utf8'),c);return c.window[n];};
const fy2=las('uppgifter2.js','BANK2'),ma5=las('uppgiftermatf1.js','BANKMATF1');
const q=(b,id)=>{const u=b.find(x=>x.id===id);a.ok(u,id);return u;};
const text=u=>JSON.stringify({...u,familjTidigare:undefined});
const r2=x=>Math.round(x*100)/100;

test('Fy2: ingen dopplereffekt i uppgifter, facit, ledtrådar eller delmoment',()=>{
 for(const u of fy2)a.doesNotMatch(text(u),/[Dd]oppler/,u.id);
 for(const u of fy2.filter(u=>u.omr==='ljud_horsel'))a.notEqual(u.familj,'Infraljud, ultraljud och dopplereffekt',u.id);
 const fam=fy2.filter(u=>u.familj==='Infraljud och ultraljud');a.equal(fam.length,9);
 for(const u of fam){a.ok(u.familjTidigare.includes('Infraljud, ultraljud och dopplereffekt'),u.id);a.ok(!u.familjTidigare.includes(u.familj),u.id);}
});

test('Fy2: omskrivna uppgifter räknas om',()=>{
 const c=2.998e8;
 const u43=q(fy2,'4.3');a.doesNotMatch(u43.t,/rör sig/);a.match(u43.s,/751/);a.equal(r2(c/8.4e9*100),3.57);a.match(u43.s,/3\{,\}6\\ \\mathrm\{cm\}/);
 const u112=q(fy2,'2.112');a.equal(u112.rättSvar,340*6.0e-3/2);a.equal(u112.svarEnhet,'m');a.doesNotMatch(u112.t,/y1="132"/);
 const u114=q(fy2,'2.114');a.match(u114.s,/360\\ \\mathrm m/);a.equal(1500*0.48/2,360);a.equal(1500/3.0e4,0.05);a.doesNotMatch(u114.t,/>v<\/text>/);
 const u115=q(fy2,'2.115');a.ok(Math.abs(u115.rättSvar-1540*65e-6/2*100)<1e-9);a.equal(u115.svarEnhet,'cm');a.equal(u115.manuellKomplettering,undefined);
 const u552=q(fy2,'5.52');const d=0.25*299792.458/70;a.ok(Math.abs(u552.rättSvar[1]-d*3.26156e-3)<0.005);
 a.ok(Math.abs(d*3.26e-3-u552.rättSvar[1])<=u552.tolerans[1],'1 pc = 3,26 ljusår godtas');
 a.equal(u552.spelDelar.length,3);a.equal(u552.spelDelar[2].alternativ.filter(x=>x.ratt).length,1);
 for(const p of u552.spelDelar)a.ok(p.t.startsWith('<p>En kvasar har rödförskjutningen'),'samma inledning '+p.etikett);
 a.doesNotMatch(q(fy2,'5.379').t,/dopplereffekt/);
});

test('Ma5 4.358: ingen separation, lösningsformen ges',()=>{
 const u=q(ma5,'4.358');a.doesNotMatch(u.t+u.s,/separ/i);a.equal(u.rättSvar,'4*e^(3*x^2/2)');a.equal(u.svarFormat,'uttryck');
 // y = 4e^(3x²/2): y(0) = 4 och y′ = 3xy (numerisk kontroll)
 const y=x=>4*Math.exp(1.5*x*x),h=1e-6;for(const x of [-1,0.3,1.2])a.ok(Math.abs((y(x+h)-y(x-h))/(2*h)-3*x*y(x))<1e-3*Math.max(1,y(x)));a.equal(y(0),4);
 for(const v of ma5)if(/separab/i.test(v.t))a.fail('separabel ekvation i '+v.id);
});

test('Ma5 rekursion: ingen allmän jämviktsmetod för explicit formel, svaren räknas om',()=>{
 for(const id of ['2.15','2.56','2.179','2.180','2.203','2.204','2.468']){const u=q(ma5,id);a.doesNotMatch(u.s,/[Jj]ämvikt|avvikelse/,id);a.doesNotMatch(u.t,/Bestäm en explicit formel för \\\(a_n\\\)\.<\/p>$/,id);}
 const rek=(x0,f,n)=>{let x=x0;for(let i=0;i<n;i++)x=f(x);return x;};
 const T=n=>rek(80,x=>0.75*x+5,n);a.ok(Math.abs(q(ma5,'2.179').rättSvar-T(10))<1e-9);a.equal(q(ma5,'2.179').tolerans,0);
 for(let n=0;n<6;n++){a.ok(Math.abs(T(n)-(20+60*0.75**n))<1e-9);a.ok(Math.abs(rek(35,x=>2/3*x+20/3,n)-(20+15*(2/3)**n))<1e-9);}
 a.equal(q(ma5,'2.468').rättSvar,20);a.ok(Math.abs(rek(35,x=>2/3*x+20/3,80)-20)<1e-9);
 const M=n=>rek(0,x=>0.8*x+10,n);let n=0;while(M(n)<=45)n++;a.equal(q(ma5,'2.203').rättSvar,n);
 for(let k=0;k<12;k++)a.ok(Math.abs(M(k)-50*(1-0.8**k))<1e-9);
 const u204=q(ma5,'2.204');a.deepEqual([...u204.rättSvar],[12,rek(20,x=>0.5*x+6,5)]);a.deepEqual([...u204.svarFormat],['numeriskt','numeriskt']);
 a.match(u204.spelDelar[1].t,/a_n=12\+8\\cdot0\{,\}5\^n/);
 // mönstret som frågan pekar på
 for(let k=1;k<6;k++){a.equal(rek(3,x=>2*x+1,k-1)+1,2**(k+1));a.equal(rek(5,x=>3*x-4,k-1)-2,3**k);}
 a.equal(q(ma5,'2.56').rättSvar,'2^(n+1)-1');a.equal(q(ma5,'2.180').rättSvar,'2+3^n');
 a.match(q(ma5,'2.56').t,/lägg till 1/);a.match(q(ma5,'2.180').t,/dra bort 2/);
 // 2.15: formeln ger startvärdet och uppfyller rekursionen
 const F=k=>120000/11+12000/11*0.78**k;a.ok(Math.abs(F(0)-12000)<1e-9);for(let k=0;k<5;k++)a.ok(Math.abs(0.78*F(k)+2400-F(k+1))<1e-9);
 a.match(q(ma5,'2.15').s,/11760/);a.match(q(ma5,'2.15').s,/10909/);
});
