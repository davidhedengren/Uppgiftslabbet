'use strict';
// Fy1-revision 2026-11-27 (tools/sprak/fy1_revision_2026-11-27.py): felrapporter 2026-11-27 09:54 (2.110, 2.84,
// 2.82, 2.55, 2.52, 3.72), rullgång → rullband, densiteter som eleverna slår upp även i Kunskapsgymmet, och
// deluppgiftskedjor där alla delkort börjar med samma inledning (omskr/fy1_kedjor_2026-11-27.py).
const {test}=require('node:test'),a=require('node:assert/strict'),fs=require('node:fs'),vm=require('node:vm');
const c={window:{}};vm.runInNewContext(fs.readFileSync('uppgifter.js','utf8'),c);
const bank=c.window.BANK||c.window.UPPGIFTER||Object.values(c.window).find(Array.isArray);
const q=id=>bank.find(u=>u.id===id),del=(id,e)=>q(id).spelDelar.find(d=>d.etikett===e);
const ren=h=>String(h||'').replace(/<svg[\s\S]*?<\/svg>/g,' ').replace(/<[^>]+>/g,' ').replace(/\s+/g,' ').trim();
const kgText=u=>[u.kgInstruktion,u.spelIntro,...(u.spelDelar||[]).flatMap(d=>[d.t,d.fraga,d.kgInstruktion])].map(ren).join(' | ');

test('felrapporterna',()=>{
 a.equal(ren(q('2.110').t),'Hur stor volym har 206 g havsvatten?');a.equal(q('2.110').kgInstruktion,'Havsvatten har densiteten 1,03 g/cm³.');
 a.doesNotMatch(ren(q('2.110').ledtrad),/deras sammanlagda/);
 for(const id of ['2.84','2.52'])a.doesNotMatch([q(id).spelIntro,...q(id).spelDelar.flatMap(d=>[d.t,d.fraga])].map(ren).join(' '),/densitet/i,id);
 a.doesNotMatch(ren(q('2.84').ledtrad)+ren(del('2.84','a').ledtrad),/2,70/);
 a.doesNotMatch(JSON.stringify(q('2.82')),/möblernas/);a.doesNotMatch(q('2.82').kgInstruktion||'',/Avrunda/);
 a.equal(del('2.55','b').fraga,'Ange densiteten i kg/m³.');a.match(del('2.55','b').t,/kg\/m³/);
 // 2.52 c: samma inledning som a och b, ändringen i frågan
 a.equal(del('2.52','c').t.split('<p>Hur stor')[0],del('2.52','a').t.split('<p>Bestäm volymen')[0]);
 a.match(del('2.52','c').fraga,/30 kg/);a.doesNotMatch(del('2.52','c').t,/massan 30 kg\.<\/p>/);
 a.doesNotMatch(ren(q('3.72').t),/1,62|9,82/);a.match(ren(q('3.72').t),/månen/);
 a.ok(Object.values(q('3.72').svarTabell).flat().length>=2);
});

test('rullgång heter rullband',()=>{
 a.doesNotMatch(fs.readFileSync('uppgifter.js','utf8'),/rullg[åa]ng/i);
 a.match(ren(q('3.234').t),/rullband/);a.match(ren(q('2.318').t),/rullband/);
});

test('densiteter: inte i frågetexterna, men i kgInstruktion för rättningen i Kunskapsgymmet',()=>{
 // Förtydligande 2026-11-27: ”i uppgiftslabbet ska det inte vara med några densiteter som finns i formelsamlingen,
 // men i kunskapsgymmet kan de stå … en egen del i koden”, alltså kgInstruktion (visas bara i Kunskapsgymmet).
 const tab=/(Vattnets|Kopparns|Järnets|Blyets|Guldets|Aluminiumets|Isens|Kvicksilvrets|Etanolens|Havsvattnets) densitet är (?!10[34]0 )\d|Densitet: (vatten|kvicksilver|havsvatten|is|järn|koppar)|(Koppar|Aluminium|Järn|Guld|Vatten|Bly|Stål|Zink) har densiteten \d/;
 const fragetext=u=>[u.spelIntro,...(u.spelDelar||[]).flatMap(d=>[d.t,d.fraga])].map(ren).join(' | ');
 for(const u of bank)a.doesNotMatch(fragetext(u),tab,u.id);
 a.equal(q('2.84').kgInstruktion,'Aluminiumets densitet är 2,70 g/cm³.');
 for(const e of ['a','b'])a.match(del('2.84',e).kgInstruktion,/2,70 g\/cm³/);
 for(const e of ['a','b','c'])a.match(del('2.52',e).kgInstruktion,/Blyets densitet är 11,3 g\/cm³/);
 a.match(q('2.110').kgInstruktion,/1,03 g\/cm³/);a.match(q('2.18').kgInstruktion,/zink 7,13 g\/cm³/);
 a.match(q('8.424').kgInstruktion,/Kopparns densitet är 8,96 g\/cm³/);a.match(q('8.424').kgInstruktion,/resistivitet/);
 a.match(q('2.82').kgInstruktion,/Luftens densitet är 1,20 kg\/m³/);a.doesNotMatch(ren(q('2.82').spelIntro),/densitet/);
 // Övriga tabellvärden (steget tabell): specifik värmekapacitet, smältvärme, ljudets fart, g på månen m.m.
 const tab2=/(Vattnets|Isens|Kopparns|Järnets|Aluminiumets) (specifika värmekapacitet|smältvärme|ångbildningsvärme) är \d|Ljudets fart (i (luft|vatten) )?är \d|Tyngdaccelerationen är [\d,]+ m\/s² på (månen|Mars)/;
 for(const u of bank)if(u.id!=='2.312')a.doesNotMatch(fragetext(u),tab2,u.id); // 2.312: ljudfarten 1304 m/s är uppgiftens egna data
 a.match(q('7.45').kgInstruktion,/smältvärme/);a.match(del('7.45','b').kgInstruktion,/smältvärme är 334 kJ\/kg/);
});

test('deluppgiftskedjor: alla delkort börjar med inledningen',()=>{
 const ids=['2.52','3.46','3.197','4.165','5.117','5.45','5.32','6.480','7.45','7.137'];
 for(const id of ids){const u=q(id);for(const d of u.spelDelar){a.ok(d.t.startsWith(u.spelIntro),id+d.etikett);a.equal(d.t,u.spelIntro+'<p>'+d.fraga+'</p>',id+d.etikett);}
  const fr=u.spelDelar.map(d=>d.fraga);a.equal(new Set(fr).size,fr.length,id+' två delar med samma fråga');}
 a.match(del('4.165','d').fraga,/0,20 m/);a.match(del('4.98','c').t,/drar rakt uppåt/);a.doesNotMatch(del('4.98','c').t,/<svg/); // egen text (EGEN_TEXT)
 a.match(del('3.46','c').fraga,/nedåt/);
 a.match(del('5.117','b').fraga,/0,020 s/);a.match(del('7.137','b').fraga,/8,2 kJ/);
});

test('grammatik i förbehåll',()=>{
 const s=fs.readFileSync('uppgifter.js','utf8');
 a.doesNotMatch(s,/Antag att en kropp med massan 65 kg effekten/);a.doesNotMatch(s,/röret vara högst/);
});
