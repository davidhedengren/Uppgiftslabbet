'use strict';
/* Riktiga skärmbilder av GeoGebra Classic (svenska) för statistikfacit.
   Användning: node tools/geogebra-statistik-bilder.js <spec.json> [utmapp]
   spec: [{namn:"4-453", varden:[38,39,40,41,42], frekvens:[3,4,5,2,1]?}, ...]
   För varje datamängd skapas <namn>-data.png (värdena markerade, verktygsknappen inramad) och
   <namn>-stat.png (statistikpanelen efter Σx, med Σx och raden s inramade). Den gemensamma
   bilden geogebra-envariabelanalys-meny.png skapas med {meny:true}. Panelens n, Medel, σ och s
   skrivs ut så att de kan jämföras med en oberoende beräkning.
   Se agent/MA2_STATISTIK_GEOGEBRA_SKARMBILDER_2026-11-05.md. */
const fs=require('node:fs'),path=require('node:path'),{execFileSync}=require('node:child_process');
const {starta,vila}=require('./geogebra-cdp.js');
const URL='https://www.geogebra.org/classic?lang=sv';
const knapp=t=>`(()=>{const k=[...document.querySelectorAll('button')].find(x=>x.textContent.trim()==='${t}'); if(k){k.click();return true;} return false;})()`;
const rekt=uttryck=>`(()=>{const e=${uttryck}; if(!e) return null; const r=e.getBoundingClientRect(); return [r.x,r.y,r.width,r.height];})()`;
const blad=t=>`[...document.querySelectorAll('*')].find(x=>x.children.length===0 && x.textContent.trim()===${JSON.stringify(t)} && x.getBoundingClientRect().width>0)`;

async function oppna(b){
  await b.ga(URL);
  for(let i=0;i<60;i++){ if(await b.evaluate('!!(window.ggbApplet&&ggbApplet.evalCommand)')) break; await vila(500); }
  for(let i=0;i<10;i++){ if(await b.evaluate(knapp('MORE OPTIONS'))) break; await vila(500); }
  for(let i=0;i<10;i++){ await vila(600); if(await b.evaluate(knapp('REJECT ALL'))) break; }
  await vila(1000);
  await b.evaluate(`ggbApplet.setPerspective('S'); true`); await vila(900);
  const kb=await b.evaluate(rekt(`document.querySelector('.closeTabbedKeyboardButton')`));
  if(kb){ await b.klick(kb[0]+kb[2]/2,kb[1]+kb[3]/2); await vila(400); }
  // Dölj verktygstips som annars hamnar i bilderna.
  await b.evaluate(`(()=>{const s=document.createElement('style');s.textContent='.snackbar,.toolTipPanel,.gwt-PopupPanel.snackbar{display:none!important}';document.head.appendChild(s);return true;})()`);
}
async function fyll(b,varden,frekvens){
  const kod=varden.map((v,i)=>`ggbApplet.evalCommand('A${i+1}=${v}');`).join('')
    +(frekvens||[]).map((v,i)=>`ggbApplet.evalCommand('B${i+1}=${v}');`).join('');
  await b.evaluate(kod+'true'); await vila(800);
  await b.hjul(300,300,-3000,-3000); await vila(400);
}
/* Kalkylbladet ritas på en canvas. Måtten är uppmätta i en skärmbild med bredden 720 px:
   kolumn A är 52–122 px, kolumn B 122–192 px, rad 1 har mitten 90,5 px och radhöjden är 25 px. */
async function celler(){ return {x:87, y1:90.5, dy:25, bredd:70}; }
async function panelVarden(b){
  return b.evaluate(`(()=>{const ut={};for(const k of ['n','Medel','σ','s']){const e=[...document.querySelectorAll('*')].find(x=>x.children.length===0&&x.textContent.trim()===k&&x.getBoundingClientRect().width>0); if(!e) continue; const r=e.getBoundingClientRect(); const v=[...document.querySelectorAll('*')].filter(x=>x.children.length===0&&x!==e).map(x=>[x,x.getBoundingClientRect()]).filter(([x,q])=>Math.abs(q.y-r.y)<4&&q.x>r.x+r.width-2&&q.width>0&&x.textContent.trim()!=='')[0]; ut[k]=v?v[0].textContent.trim():null;} return JSON.stringify(ut);})()`);
}
/* Ramar ritas med Python/PIL efteråt: [x,y,b,h] i CSS-pixlar, skalas med 2. */
function rama(fil,ramar,klipp){
  const py=path.join(__dirname,'geogebra-ramar.py');
  execFileSync('python',[py,fil,JSON.stringify(ramar),JSON.stringify(klipp)],{stdio:'inherit'});
}
async function datamangd(b,d,ut){
  await oppna(b);
  await fyll(b,d.varden,d.frekvens);
  const c=await celler(b);
  const n=d.varden.length, sista=c.y1+c.dy*(n-1), x2=d.frekvens?c.x+c.bredd:c.x;
  await b.klick(c.x,c.y1); await b.klick(x2,sista,8); await vila(500);
  const verktyg=[50,6,40,40];   // verktygsknappen med stapeldiagrammet
  const dataFil=path.join(ut,`geogebra-${d.namn}-data.png`);
  await b.bild(dataFil);
  const hojd=Math.min(b.hojd,sista+c.dy/2+12);
  rama(dataFil,[verktyg,[c.x-c.bredd/2,c.y1-c.dy/2,(d.frekvens?2:1)*c.bredd,c.dy*n]],[0,0,Math.min(b.bredd,x2+c.bredd/2+90),hojd]);
  // Verktyget → Envariabelanalys → Σx
  await b.klick(verktyg[0]+verktyg[2]/2,verktyg[1]+verktyg[3]/2); await vila(700);
  const post=await b.evaluate(rekt(blad('Envariabelanalys')));
  if(d.meny){ const f=path.join(ut,'geogebra-envariabelanalys-meny.png'); await b.bild(f); rama(f,[post],[0,0,post[0]+post[2]+30,post[1]+post[3]+90]); }
  await b.klick(post[0]+post[2]/2,post[1]+post[3]/2); await vila(1500);
  const sigma=await b.evaluate(rekt(`[...document.querySelectorAll('button')].find(x=>x.getAttribute('title')==='Visa statistik')`));
  await b.klick(sigma[0]+sigma[2]/2,sigma[1]+sigma[3]/2); await vila(1300);
  const varden=JSON.parse(await panelVarden(b));
  const sRad=await b.evaluate(rekt(blad('s'))), maxRad=await b.evaluate(rekt(blad('Max')));
  const statFil=path.join(ut,`geogebra-${d.namn}-stat.png`);
  await b.bild(statFil);
  const panelSlut=await b.evaluate(`(()=>{const e=${blad('Statistik')}; const p=e&&e.closest('div[class]'); let x=0; document.querySelectorAll('*').forEach(z=>{const r=z.getBoundingClientRect(); if(Math.abs(r.y-${sRad?sRad[1]:0})<4&&r.width>0&&r.x<700) x=Math.max(x,r.x+r.width);}); return x;})()`);
  rama(statFil,[sigma,[sRad[0]-2,sRad[1]-1,Math.max(120,panelSlut-sRad[0]+4),sRad[3]+2]],[0,0,b.bredd,Math.min(b.hojd,(maxRad?maxRad[1]+maxRad[3]:sRad[1]+200)+14)]);
  return {namn:d.namn,...varden};
}
async function main(){
  const spec=JSON.parse(fs.readFileSync(process.argv[2],'utf8'));
  const ut=process.argv[3]||path.join(__dirname,'..','bilder');
  const profil=path.join(require('node:os').tmpdir(),'gg-statistik-profil');
  const b=await starta({profil,bredd:720,hojd:600,skala:2});
  const resultat=[];
  try{ for(const d of spec){ resultat.push(await datamangd(b,d,ut)); console.log(JSON.stringify(resultat.at(-1))); } }
  finally{ await b.stang(); }
  return resultat;
}
if(require.main===module) main().catch(e=>{console.error(e);process.exit(1);});
module.exports={datamangd,oppna};
