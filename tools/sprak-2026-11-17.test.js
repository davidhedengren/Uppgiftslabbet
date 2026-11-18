'use strict';
/* Språkgranskningen 2026-11-17 (agent/SPRAKGRANSKNING_2026-11-17.md). Uppgiftstexterna skrivs som lärarens egna
   prov och skrivs om för hand, område för område. Rättningsinstruktioner (tecken, positiv riktning, svarsform)
   ligger i fältet kgInstruktion, som bara Kunskapsgymmet visar. Enheten visas i Kunskapsgymmet via svarEnhet.
   Testet kontrollerar de områden som är klara, så att AI-mönstren inte kommer tillbaka. */
const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('node:fs'),vm=require('node:vm'),path=require('node:path');
function bank(file,key){const c={window:{}};vm.runInNewContext(fs.readFileSync(path.join(__dirname,'..',file),'utf8'),c);return c.window[key];}

const KLARA={ 'uppgifter2.js|BANK2':['cirkel','kast','fjadrar','svangningar','pendlar','vagrorelser','staende_vagor','ljud_horsel','ljudvagor','interferens','elektriska_falt','magnetism','orsted','laddade_partiklar','jordens_magnetfalt','induktion','induktion_ledare','vaxelstrom','vaxelstrom_spole_kondensator','kast_elfalt','spolar','em_vagor','vagrorelselara','temperaturstralning','straloptik','ljus_partikelstrom','de_broglie','atomstruktur','farg_ljusstyrka','exoplaneter','stjarnornas_utveckling','kosmologi','avstandsmatning','magnituder','tidsdilatation','langdkontraktion','relativistisk_energi'], 'uppgifter.js|BANK':['rorelsemangd','kollisioner','rorelseenergi','arbete','effekt','blandat_energi','tyngdkraft','aktivitet','em_stralning','fission','fusion','fyra_krafterna','karnreaktioner','medicinska_metoder','nuklider','sonderfall','standardmodellen','straldoser','stralning_materia','tryck','vatsketryck','arkimedes','gaslagen','varme','fasandring','enheter','medelhastighet','densitet','matnogg','vektorer','st_diagram','acceleration','vt_diagram','at_diagram','konstacc','kraftvektorer','newton1','newton2','newton3','normalkraft','gravitation','fjadrar','friktion','lutande_plan','moment','blandat_kraft','laddning','coulomb','strom','kretsar','multimeter','seriekoppling','parallellkoppling','kopplingar','falt','potential'], 'uppgifterma1.js|BANKMA1':['enhetsbyten','prefix','tiopotenser_prefix','proportionalitet_grunder','brakform','forhallanden','brakrakning','negativa_tal','tal_rakneordning','decimaltal_positionssystem','avrundning','overslag_grunder','andelar','algebraiska_uttryck','ekv_brak','ekv_flera_variabeltermer','ekv_parenteser','ekv_problemlosning','faktorisering','forenkla_uttryck','formler','intervall','linjara_ekvationer','linjara_olikheter','monster_samband','multiplicera_uttryck','funktionsbegreppet','definitionsmangd_vardemangd','representationer','grafisk_ekvationslosning','jamfora_modeller','linjara_funktioner','rata_linjens_ekvation','bestamma_linjar_funktion','exponentialfunktioner','potensfunktioner','potensregler','potensekvationer','procent','index','forandringsfaktor','upprepade_forandringar','genomsnittlig_forandring','ranta','amortering','omkrets_area','volym','kvadratrotter','pythagoras','sinus_cosinus_tangens','arcusfunktioner','strackor_vinklar','koordinatgeometri','vektorer','vektor_addition_subtraktion','vektor_absolutbelopp','vektor_skalar'] };

const FORBJUDET=[
 [/[Vv]älj ett alternativ/,'Välj ett alternativ'],[/[Mm]arkera det korrekta/,'Markera det korrekta alternativet'],
 [/\(Svara /,'(Svara …)'],[/[Ss]vara med (tre|två|en) (värdesiffr|decimal)/,'precisionskrav'],
 [/\b(?:[Ee]n|[Ee]tt|[Tt]vå|[Tt]re) (?:[a-zåäö]+ )?[a-zåäö]+ på [\d ,]+ ?(kg|g|ton)\b/,'"en kloss på 2 kg" (bestämd form som "lådan på 20 kg" pekar ut ett föremål och får stå)'],[/\b[Vv]ågrät|\b[Ll]odrät/,'vågrät/lodrät'],
 [/[Ff]rån vila/,'från vila'],[/[Pp]ositiva? riktning/,'positiv riktning'],[/[Mm]ed tecken|[Aa]nge tecken/,'med tecken'],
 [/andra krafters impuls|den korta stöten/,'stöt-förbehåll'],[/[Rr]äkna (bara )?på /,'Räkna på …'],[/[Ss]ammanlagd/,'sammanlagd'],
 [/[Bb]ortse från andra krafters/,'Bortse från andra krafters …'],[/[Ee]ndast .{0,40} verkar|[Bb]ara .{0,40} verkar/,'Endast … verkar'],
 [/utan tecken|\bentydigt\b/,'modellspråk'],[/[Mm]iniräknare får användas|[Bb]ehåll oavrundade|[Ff]ördjupning utanför/,'metatext'],
];
const synlig=h=>String(h||'').replace(/<svg[\s\S]*?<\/svg>/g,' ').replace(/<[^>]+>/g,' ').replace(/\s+/g,' ');

test('klara områden har uppgiftstexter utan AI-mönster',()=>{
 const fel=[];
 for(const [nyckel,omraden] of Object.entries(KLARA)){
  const [fil,glob]=nyckel.split('|');
  for(const u of bank(fil,glob).filter(u=>omraden.includes(u.omr))){
   const texter=[['t',u.t],['spelIntro',u.spelIntro],...(u.spelDelar||[]).flatMap((d,i)=>[[`del${i} t`,d.t],[`del${i} fraga`,d.fraga]])];
   for(const [falt,txt] of texter) for(const [rx,namn] of FORBJUDET) if(rx.test(synlig(txt))) fel.push(`${u.id} ${falt}: ${namn}`);
  }
 }
 assert.deepEqual(fel,[]);
});

test('kgInstruktion är kort och står inte i uppgiftstexten',()=>{
 for(const [nyckel,omraden] of Object.entries(KLARA)){
  const [fil,glob]=nyckel.split('|');
  for(const u of bank(fil,glob).filter(u=>omraden.includes(u.omr))){
   for(const x of [u,...(u.spelDelar||[])]) if(x.kgInstruktion){
    assert.equal(typeof x.kgInstruktion,'string',u.id);assert.ok(x.kgInstruktion.length<160,u.id);
    assert.ok(!String(x.t||'').includes(x.kgInstruktion),u.id);
    // Användarbeslut 2026-11-17: "svara med tecken" skrivs inte, eleverna förstår det själva.
    assert.doesNotMatch(x.kgInstruktion,/tecken/i,u.id);
   }
  }
 }
});

test('pilotexempel: Fy1 rörelsemängd skrivet som lärarens prov',()=>{
 const fy=bank('uppgifter.js','BANK'),q=id=>fy.find(u=>u.id===id);
 assert.match(q('5.277').t,/En boll med massan 0,20 kg rör sig med farten 8,0 m\/s\. Hur stor rörelsemängd har bollen\?/);
 // Negativt svar: tecknet krävs bara i Kunskapsgymmet.
 assert.equal(q('5.282').rättSvar,-8.1);assert.doesNotMatch(q('5.282').t,/positiv|tecken/);assert.equal(q('5.282').kgInstruktion,'Höger räknas som positiv riktning.');
 assert.equal(q('5.32').spelDelar[1].kgInstruktion,'Höger räknas som positiv riktning.');assert.ok(!q('5.32').spelDelar[0].kgInstruktion);
 // Formel ur frågan, svarsformen a·10⁻²¹ bara i Kunskapsgymmet och pappersfacit med hela svaret.
 assert.doesNotMatch(q('5.158').t,/p = mv/);
 assert.match(q('5.16').spelDelar[1].kgInstruktion,/a · 10⁻²¹/);assert.doesNotMatch(q('5.16').t,/talet a/);assert.match(q('5.16').s,/3,3 · 10⁻²¹ kg·m\/s/);
 // Lösningen hör inte hemma i frågan.
 assert.doesNotMatch(q('5.392').t,/Kraft · stopptid/);
});
