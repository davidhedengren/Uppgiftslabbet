#!/usr/bin/env node
'use strict';

const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');

const GILTIGA_NIVAER = new Set(['G', 'E', 'C', 'A']);
const GILTIGA_FORMAGOR = new Set(['begrepp', 'procedur', 'resonemang', 'modellering', 'problemlösning', 'problemlosning']);
const ALLVAR = ['ERROR', 'WARNING', 'INFO'];
const BANKKONFIG = {
  'uppgifter.js': { strukturfil: 'struktur.js', kapnamn: 'KAPNAMN', omr: 'OMR', spar: null, sparTaggar: [], kravKurs: false },
  'uppgifter2.js': { strukturfil: 'struktur2.js', kapnamn: 'KAPNAMN2', omr: 'OMR2', spar: null, sparTaggar: [], kravKurs: false },
  'uppgifterma1.js': { strukturfil: 'strukturma1.js', kapnamn: 'KAPNAMNMA1', omr: 'OMRMA1', spar: null, sparTaggar: ['1a', '1b', '1c'], kravKurs: true },
  'uppgifterma2.js': { strukturfil: 'strukturma2.js', kapnamn: 'KAPNAMNMA2', omr: 'OMRMA2', spar: 'SPARMA2', sparTaggar: ['2a', '2b', '2c'], kravKurs: true },
  'uppgiftermato1.js': { strukturfil: 'strukturmato1.js', kapnamn: 'KAPNAMNMATO1', omr: 'OMRMATO1', spar: 'SPARMATO1', sparTaggar: ['1b', '1c'], kravKurs: true },
  'uppgiftermato2.js': { strukturfil: 'strukturmato2.js', kapnamn: 'KAPNAMNMATO2', omr: 'OMRMATO2', spar: 'SPARMATO2', sparTaggar: ['2c'], kravKurs: true },
  'uppgiftermatf1.js': { strukturfil: 'strukturmatf1.js', kapnamn: 'KAPNAMNMATF1', omr: 'OMRMATF1', spar: null, sparTaggar: [], kravKurs: false },
};

const textFinns = (v) => typeof v === 'string' && v.trim().length > 0;
const arObjekt = (v) => v !== null && typeof v === 'object' && !Array.isArray(v);
const kortUppgift = (u, index) => ({ index: index + 1, id: textFinns(u?.id) ? u.id.trim() : '(saknas)' });
function laggTill(resultat, allvar, kod, kort, meddelande, extra = {}) { resultat.fynd.push({ allvar, kod, fil: resultat.fil, ...kort, meddelande, ...extra }); }

function lasJavascriptGlobaler(filsokvag) {
  const sandbox = { window: {} };
  vm.createContext(sandbox);
  new vm.Script(fs.readFileSync(filsokvag, 'utf8'), { filename: filsokvag }).runInContext(sandbox, { timeout: 30000 });
  return sandbox.window;
}
function lasBankfil(filsokvag) {
  const kandidater = Object.entries(lasJavascriptGlobaler(filsokvag)).filter(([namn, varde]) => /^BANK/i.test(namn) && Array.isArray(varde));
  if (kandidater.length !== 1) throw new Error(`Förväntade exakt en BANK-array men hittade ${kandidater.length}.`);
  return { globaltNamn: kandidater[0][0], bank: kandidater[0][1] };
}
function lasStruktur(projektrot, konfig) {
  const g = lasJavascriptGlobaler(path.join(projektrot, konfig.strukturfil));
  const kapnamn = g[konfig.kapnamn], omr = g[konfig.omr], spar = konfig.spar ? g[konfig.spar] : null;
  if (!arObjekt(kapnamn)) throw new Error(`Strukturglobalen ${konfig.kapnamn} saknas eller är inte ett objekt.`);
  if (!arObjekt(omr)) throw new Error(`Strukturglobalen ${konfig.omr} saknas eller är inte ett objekt.`);
  if (konfig.spar && !arObjekt(spar)) throw new Error(`Spårglobalen ${konfig.spar} saknas eller är inte ett objekt.`);
  return { kapnamn, omr, spar, sparTaggar: konfig.sparTaggar, kravKurs: konfig.kravKurs };
}

function extraheraBildreferenser(html) {
  if (!textFinns(html)) return [];
  const refs = [];
  for (const tagg of html.match(/<(?:img|image|source)\b[^>]*>/gi) || []) {
    for (const match of tagg.matchAll(/\b(?:src|href|xlink:href|srcset)\s*=\s*(["'])(.*?)\1/gi)) {
      refs.push(...(/\bsrcset\s*=/i.test(match[0]) ? match[2].split(',').map((x) => x.trim().split(/\s+/)[0]) : [match[2]]).filter(Boolean));
    }
  }
  return refs;
}
function lokalSokvag(ref, projektrot) {
  if (/^(?:https?:|data:|blob:|\/\/|#)/i.test(ref)) return null;
  let ren = ref.split(/[?#]/, 1)[0].replace(/&amp;/g, '&');
  try { ren = decodeURIComponent(ren); } catch (_) {}
  return path.resolve(projektrot, ren.replace(/^\/+/, ''));
}

function kontrolleraLatex(text) {
  const problem = [], stack = [];
  if (!textFinns(text)) return problem;
  for (let i = 0; i < text.length; i++) {
    if (text[i] !== '\\') continue;
    let j = i; while (text[j] === '\\') j++;
    const tecken = text[j], antal = j - i;
    if (antal % 2 === 1 && '()[]'.includes(tecken)) {
      const token = `\\${tecken}`;
      if (token === '\\(' || token === '\\[') stack.push(token);
      else { const vantad = token === '\\)' ? '\\(' : '\\['; if (stack.at(-1) !== vantad) problem.push(`oväntad avgränsare ${token}`); else stack.pop(); }
    }
    i = j - 1;
  }
  for (const token of stack) problem.push(`oavslutad avgränsare ${token}`);
  const begin = [...text.matchAll(/\\begin\{([^}]+)\}/g)].map((m) => m[1]);
  const end = [...text.matchAll(/\\end\{([^}]+)\}/g)].map((m) => m[1]);
  if (begin.join('\u0000') !== end.join('\u0000')) problem.push('obalanserad \\begin/\\end-miljö');
  return [...new Set(problem)];
}
function kontrolleraKlamrar(text) {
  let djup = 0;
  for (let i = 0; i < text.length; i++) { if (text[i] === '\\') { i++; continue; } if (text[i] === '{') djup++; if (text[i] === '}') djup--; if (djup < 0) return false; }
  return djup === 0;
}
function kontrolleraHtml(text) {
  const fynd = [];
  if (!textFinns(text)) return fynd;
  if (/<\s*(?:script|iframe|object|embed)\b|\bon[a-z]+\s*=|javascript\s*:/i.test(text)) fynd.push(['ERROR', 'DANGEROUS_HTML', 'aktivt eller farligt HTML-innehåll']);
  if (/<p\b[^>]*>(?:(?!<\/p>)[\s\S])*<(?:div|table|ol|ul|section|svg)\b/i.test(text)) fynd.push(['INFO', 'SUSPECT_HTML', 'blockelement ligger inuti <p> och är browser-tolererat men formellt misstänkt']);
  if (/<[^>]*$/.test(text)) fynd.push(['WARNING', 'SUSPECT_HTML', 'ett HTML-element verkar vara avhugget']);
  for (const tagg of ['div', 'span', 'ol', 'ul', 'table']) {
    const oppna = (text.match(new RegExp(`<${tagg}\\b`, 'gi')) || []).length, stangda = (text.match(new RegExp(`</${tagg}\\s*>`, 'gi')) || []).length;
    if (oppna !== stangda) fynd.push(['WARNING', 'SUSPECT_HTML', `obalanserat <${tagg}> (${oppna} öppna, ${stangda} stängda)`]);
  }
  return fynd;
}
function svgSegment(text) {
  const segment = [...text.matchAll(/<svg\b[\s\S]*?<\/svg\s*>/gi)].map((m) => m[0]);
  return { segment, oppna: (text.match(/<svg\b/gi) || []).length, stangda: (text.match(/<\/svg\s*>/gi) || []).length };
}
function kontrolleraSvg(svg) {
  const problem = [], info = [], rot = svg.match(/^<svg\b([^>]*)>/i);
  if (!rot) return { problem: ['SVG-roten kunde inte läsas'], viewBoxSaknas: false, info };
  const vb = rot[1].match(/\bviewBox\s*=\s*(["'])(.*?)\1/i);
  const viewBoxSaknas = !vb;
  if (vb) { const tal = vb[2].trim().split(/[\s,]+/).map(Number); if (tal.length !== 4 || tal.some((x) => !Number.isFinite(x)) || tal[2] <= 0 || tal[3] <= 0) problem.push('viewBox är ogiltig'); }
  const stack = [], ids = new Set(), dubblettIds = new Set();
  for (const match of svg.matchAll(/<!--[\s\S]*?-->|<\/?([A-Za-z_][\w:.-]*)\b[^>]*>/g)) {
    if (match[0].startsWith('<!--')) continue;
    const namn = match[1].toLowerCase(), stang = /^<\//.test(match[0]), sjalv = /\/\s*>$/.test(match[0]);
    if (!stang) { const id = match[0].match(/\bid\s*=\s*(["'])(.*?)\1/i)?.[2]; if (id) { if (ids.has(id)) dubblettIds.add(id); ids.add(id); } if (!sjalv) stack.push(namn); }
    else if (!stack.length || stack.pop() !== namn) { problem.push(`felaktigt stängningselement </${namn}>`); break; }
  }
  if (stack.length) problem.push(`oavslutat SVG-element <${stack.at(-1)}>`);
  for (const ref of svg.matchAll(/url\(\s*#([^)\s]+)\s*\)/g)) if (!ids.has(ref[1])) problem.push(`referens till saknat SVG-id #${ref[1]}`);
  if (dubblettIds.size) info.push(`duplicerade SVG-id:n: ${[...dubblettIds].join(', ')}`);
  if (!/\brole\s*=\s*(["'])img\1/i.test(rot[1]) && !/<title\b/i.test(svg) && !/\baria-label\s*=/i.test(rot[1])) info.push('SVG saknar role="img", aria-label och <title>');
  return { problem: [...new Set(problem)], viewBoxSaknas, info };
}

const giltigFamilj = (v) => textFinns(v) || (Array.isArray(v) && v.length > 0 && v.every(textFinns));
const giltigBoolestruktur = (v) => typeof v === 'boolean' || (Array.isArray(v) && v.length > 0 && v.every(giltigBoolestruktur));
function formMatchar(mask, svar) { return typeof mask === 'boolean' || (Array.isArray(mask) && Array.isArray(svar) && mask.length === svar.length && mask.every((del, i) => typeof del === 'boolean' || formMatchar(del, svar[i]))); }
const nagotSant = (v) => v === true || (Array.isArray(v) && v.some(nagotSant));
function toleransProblem(v) { if (v === undefined || v === null) return null; if (Array.isArray(v)) return v.map(toleransProblem).find(Boolean) || null; return typeof v !== 'number' || !Number.isFinite(v) || v < 0 ? 'tolerans måste vara ett icke-negativt ändligt tal, null eller en motsvarande array' : null; }
const harRattAlternativ = (u) => Array.isArray(u.alternativ) && u.alternativ.some((a) => a && (a.ratt === true || a.rätt === true || a.correct === true));

function renText(html, ersattTal = false) {
  let text = String(html || '').replace(/<svg\b[\s\S]*?<\/svg\s*>/gi, ' figur ').replace(/<[^>]+>/g, ' ').replace(/\\[()[\]]/g, ' ').replace(/\\[a-zA-Z]+/g, ' ').replace(/&[a-zA-Z#0-9]+;/g, ' ').toLocaleLowerCase('sv-SE');
  if (ersattTal) text = text.replace(/[-+]?\d+(?:[.,]\d+)?/g, '#');
  return text.replace(/[^a-zåäö0-9#]+/gi, ' ').trim().replace(/\s+/g, ' ');
}
function kontrolleraTextdubbletter(bank, resultat) {
  const exakt = new Map(), mallar = new Map();
  bank.forEach((u, index) => {
    if (!arObjekt(u)) return;
    const ren = renText(u.t); if (ren.length < 25) return;
    if (!exakt.has(ren)) exakt.set(ren, []); exakt.get(ren).push(kortUppgift(u, index));
    const mall = renText(u.t, true); if (!mallar.has(mall)) mallar.set(mall, []); mallar.get(mall).push({ ...kortUppgift(u, index), ren });
  });
  for (const poster of exakt.values()) if (poster.length > 1) laggTill(resultat, 'WARNING', 'EXACT_TEXT_DUPLICATE', poster[0], `Exakt normaliserad uppgiftstext delas av ${poster.map((x) => x.id).join(', ')}.`, { relateradeId: poster.map((x) => x.id) });
  for (const poster of mallar.values()) if (poster.length > 1 && new Set(poster.map((x) => x.ren)).size > 1) laggTill(resultat, 'INFO', 'VERY_SIMILAR_TEXT', poster[0], `Mycket lik textmall (främst tal skiljer) delas av ${poster.map((x) => x.id).join(', ')}.`, { relateradeId: poster.map((x) => x.id) });
}

function granskaBank(filnamn, bank, projektrot, struktur = null) {
  const resultat = { fil: filnamn, antalUppgifter: Array.isArray(bank) ? bank.length : 0, fynd: [] };
  if (!Array.isArray(bank)) { laggTill(resultat, 'ERROR', 'BANK_NOT_ARRAY', { id: '(bank)', index: 0 }, 'Banken är inte en array.'); return resultat; }
  const idPositioner = new Map();
  bank.forEach((u, index) => {
    const kort = kortUppgift(u, index);
    if (!arObjekt(u)) { laggTill(resultat, 'ERROR', 'TASK_NOT_OBJECT', kort, 'Bankelementet är inte ett objekt.'); return; }
    const id = textFinns(u.id) ? u.id.trim() : '';
    if (!id) laggTill(resultat, 'ERROR', 'MISSING_ID', kort, 'ID saknas eller är tomt.'); else { if (!idPositioner.has(id)) idPositioner.set(id, []); idPositioner.get(id).push(index + 1); }
    if (!textFinns(u.niva)) laggTill(resultat, 'ERROR', 'MISSING_LEVEL', kort, 'Nivå saknas eller är tom.'); else if (!GILTIGA_NIVAER.has(u.niva.trim())) laggTill(resultat, 'ERROR', 'INVALID_LEVEL', kort, `Ogiltig nivå: ${u.niva}.`);
    if (!textFinns(u.t)) laggTill(resultat, 'ERROR', 'MISSING_TASK_TEXT', kort, 'Uppgiftstexten t saknas eller är tom.');
    if (!textFinns(u.s)) laggTill(resultat, 'ERROR', 'MISSING_SOLUTION', kort, 'Facitfältet s saknas eller är tomt.');
    if (!textFinns(u.svarstyp)) laggTill(resultat, 'ERROR', 'MISSING_ANSWER_TYPE', kort, 'svarstyp saknas eller är tom.');
    if (!Object.prototype.hasOwnProperty.call(u, 'rättSvar')) laggTill(resultat, 'ERROR', 'MISSING_RIGHT_ANSWER_METADATA', kort, 'Fältet rättSvar saknas; använd null när uppgiften ska bedömas manuellt.');
    if (!Object.prototype.hasOwnProperty.call(u, 'tolerans')) laggTill(resultat, 'WARNING', 'MISSING_TOLERANCE_METADATA', kort, 'Fältet tolerans saknas; använd null när tolerans inte är relevant.');

    if (struktur) {
      const kap = String(u.kap ?? '');
      if (!kap || !textFinns(u.omr) || !struktur.omr?.[kap]?.[u.omr]) laggTill(resultat, 'ERROR', 'UNKNOWN_CHAPTER_AREA', kort, `Kapitel/område ${kap || '(saknas)'}/${u.omr || '(saknas)'} finns inte som exakt par i strukturfilen.`);
      if (struktur.kravKurs) {
        if (!Array.isArray(u.kurs) || !u.kurs.length) laggTill(resultat, 'ERROR', 'MISSING_COURSE_TAGS', kort, 'Kurs-/spårtaggar saknas.');
        else {
          for (const tagg of u.kurs) if (!struktur.sparTaggar.includes(tagg)) laggTill(resultat, 'ERROR', 'INVALID_COURSE_TAG', kort, `Okänd kurs-/spårtagg: ${tagg}.`);
          const tillatna = struktur.spar?.[kap]?.[u.omr];
          if (Array.isArray(tillatna)) for (const tagg of u.kurs) if (!tillatna.includes(tagg)) laggTill(resultat, 'WARNING', 'COURSE_TAG_OUTSIDE_STRUCTURE_TRACK', kort, `Taggen ${tagg} används av uppgiften men saknas för området i SPAR-strukturen.`);
        }
      } else if (u.kurs !== undefined) laggTill(resultat, 'WARNING', 'UNEXPECTED_COURSE_TAGS', kort, 'Banken använder normalt inte kurs-/spårtaggar men uppgiften har fältet kurs.');
    }

    if (!textFinns(u.poang)) laggTill(resultat, 'ERROR', 'MISSING_POINTS', kort, 'Poängmetadata saknas eller är tom.');
    else { const m = u.poang.trim().match(/^\(?(\d+)\/(\d+)\/(\d+)\)?$/); if (!m) laggTill(resultat, 'ERROR', 'INVALID_POINTS', kort, `Poängvärdet ${u.poang} följer inte formatet E/C/A.`); else { const d = m.slice(1).map(Number), summa = d.reduce((a,b)=>a+b,0); if (summa === 0 || summa > 20 || Math.max(...d) > 20) laggTill(resultat, 'WARNING', 'IMPLAUSIBLE_POINTS', kort, `Poängvärdet ${u.poang} är möjligt att läsa men verkar orimligt.`); } }
    if (!giltigFamilj(u.familj)) laggTill(resultat, 'ERROR', 'MISSING_FAMILY', kort, 'Familj saknas eller har ogiltigt format.');
    if (!Array.isArray(u.formaga) || !u.formaga.length || !u.formaga.every(textFinns)) laggTill(resultat, 'ERROR', 'MISSING_ABILITY', kort, 'formaga ska vara en icke-tom array med texter.'); else for (const f of u.formaga) if (!GILTIGA_FORMAGOR.has(f)) laggTill(resultat, 'WARNING', 'UNKNOWN_ABILITY', kort, `Okänd förmågetagg: ${f}.`);
    for (const falt of ['miniräknare','geogebra']) if (typeof u[falt] !== 'boolean') laggTill(resultat, 'ERROR', 'INVALID_AID_METADATA', kort, `${falt} ska vara true eller false.`, { falt });

    for (const falt of ['t','s','ledtrad','spelIntro']) if (typeof u[falt] === 'string') {
      for (const p of kontrolleraLatex(u[falt])) laggTill(resultat, 'ERROR', 'BROKEN_LATEX', kort, `${falt}: ${p}.`, { falt });
      if (!kontrolleraKlamrar(u[falt])) laggTill(resultat, 'WARNING', 'BROKEN_LATEX', kort, `${falt}: obalanserade klamrar kan tyda på trasig LaTeX.`, { falt });
      if (/\${1,2}[^$]+\${1,2}/.test(u[falt])) laggTill(resultat, 'WARNING', 'RAW_DOLLAR_LATEX', kort, `${falt}: rå dollar-LaTeX avviker från projektets delimiterformat.`, { falt });
      for (const [allvar,kod,msg] of kontrolleraHtml(u[falt])) laggTill(resultat, allvar, kod, kort, `${falt}: ${msg}.`, { falt });
      const svg = svgSegment(u[falt]);
      if (svg.oppna !== svg.stangda) laggTill(resultat, 'ERROR', 'BROKEN_SVG', kort, `${falt}: antalet öppnande och stängande SVG-taggar skiljer sig.`, { falt });
      for (const seg of svg.segment) { const k = kontrolleraSvg(seg); if (k.viewBoxSaknas) laggTill(resultat,'ERROR','SVG_VIEWBOX_MISSING',kort,`${falt}: SVG saknar viewBox.`,{falt}); for (const p of k.problem) laggTill(resultat,'ERROR','BROKEN_SVG',kort,`${falt}: ${p}.`,{falt}); for (const p of k.info) laggTill(resultat,'INFO','SVG_ACCESSIBILITY',kort,`${falt}: ${p}.`,{falt}); }
      for (const ref of extraheraBildreferenser(u[falt])) { const lokal=lokalSokvag(ref,projektrot); if (lokal&&!fs.existsSync(lokal)) laggTill(resultat,'ERROR','MISSING_IMAGE',kort,`${falt}: bildfilen ${ref} finns inte.`,{falt,bild:ref,sokvag:path.relative(projektrot,lokal)}); }
    }

    if (u.spelDelning === 'deluppgifter' && (!Array.isArray(u.spelDelar) || !u.spelDelar.length)) laggTill(resultat,'ERROR','SUBTASKS_MISSING',kort,'spelDelning anger deluppgifter men spelDelar saknas eller är tom.');
    if (Array.isArray(u.spelDelar)) {
      u.spelDelar.forEach((del,i)=>{ if (!arObjekt(del)||!Object.keys(del).length) laggTill(resultat,'ERROR','EMPTY_SUBTASK',kort,`Deluppgift ${i+1} är tom eller inte ett objekt.`,{delIndex:i+1}); if (arObjekt(del)&&!textFinns(del.t)&&!textFinns(del.fraga)) laggTill(resultat,'WARNING','SUBTASK_QUESTION_MISSING',kort,`Deluppgift ${i+1} saknar både t och fraga.`,{delIndex:i+1}); if (arObjekt(del)&&!textFinns(del.s)) laggTill(resultat,'WARNING','SUBTASK_SOLUTION_MISSING',kort,`Deluppgift ${i+1} saknar facitfältet s.`,{delIndex:i+1}); });
      if (Array.isArray(u.rättSvar)&&u.spelDelar.length!==u.rättSvar.length&&u.svarstyp!=='manuell') laggTill(resultat,'WARNING','SUBTASK_ANSWER_COUNT_MISMATCH',kort,`${u.spelDelar.length} spelDelar men ${u.rättSvar.length} svar på toppnivå.`);
    }
    if (Array.isArray(u.rättSvar)&&Array.isArray(u.svarEtiketter)&&u.rättSvar.length!==u.svarEtiketter.length) laggTill(resultat,'WARNING','ANSWER_METADATA_COUNT_MISMATCH',kort,`${u.rättSvar.length} svar men ${u.svarEtiketter.length} svarsetiketter.`);
    if (!giltigBoolestruktur(u.självrättning)) laggTill(resultat,'ERROR','INVALID_SELFCHECK_STRUCTURE',kort,'självrättning ska vara boolean eller en nästlad boolean-array.'); else if (Array.isArray(u.självrättning)&&!formMatchar(u.självrättning,u.rättSvar)) laggTill(resultat,'WARNING','SELFCHECK_SHAPE_MISMATCH',kort,'Strukturen i självrättning motsvarar inte strukturen i rättSvar.');
    const tolFel=toleransProblem(u.tolerans); if (tolFel) laggTill(resultat,'ERROR','INVALID_TOLERANCE',kort,tolFel);
    if (nagotSant(u.självrättning)) { const alt=['alternativ','val','flerval'].includes(u.svarstyp); if (alt&&Array.isArray(u.alternativ)&&!harRattAlternativ(u)) laggTill(resultat,'ERROR','ALTERNATIVE_WITHOUT_CORRECT',kort,'Självrättande alternativfråga saknar markerat rätt alternativ.'); else if ((u.rättSvar===null||u.rättSvar===undefined||u.rättSvar==='')&&!harRattAlternativ(u)) laggTill(resultat,'WARNING','SELFCHECK_WITHOUT_ANSWER',kort,'Självrättning är aktiv men användbart rättSvar eller markerat alternativ saknas.'); if (u.tolerans===undefined&&['numeriskt','tal'].includes(u.svarstyp)) laggTill(resultat,'WARNING','MISSING_TOLERANCE',kort,'Självrättande numerisk uppgift saknar toleransfält.'); }
  });
  for (const [id,pos] of idPositioner) if (pos.length>1) laggTill(resultat,'ERROR','DUPLICATE_ID',{id,index:pos[0]},`ID förekommer på positionerna ${pos.join(', ')}.`,{positioner:pos});
  kontrolleraTextdubbletter(bank,resultat);
  return resultat;
}

function granskaProjekt(projektrot) {
  const filer=fs.readdirSync(projektrot,{withFileTypes:true}).filter((p)=>p.isFile()&&/^uppgifter.*\.js$/i.test(p.name)).map((p)=>p.name).sort((a,b)=>a.localeCompare(b,'sv'));
  const resultat=[],lasfel=[],systemfynd=[];
  for (const fil of filer) try { const k=BANKKONFIG[fil]; if(!k) throw new Error('Bankfilen saknar strukturkonfiguration i kontrollscriptet.'); const struktur=lasStruktur(projektrot,k); const {globaltNamn,bank}=lasBankfil(path.join(projektrot,fil)); resultat.push({...granskaBank(fil,bank,projektrot,struktur),globaltNamn,strukturfil:k.strukturfil}); } catch(fel) { lasfel.push({fil,fel:fel.message}); systemfynd.push({allvar:'ERROR',kod:'LOAD_ERROR',fil,id:'(fil)',index:0,meddelande:fel.message}); }
  return {filer,resultat,lasfel,systemfynd};
}
function summeraFynd(g){const alla=[...g.systemfynd,...g.resultat.flatMap((r)=>r.fynd)];return Object.fromEntries(ALLVAR.map((a)=>[a,alla.filter((f)=>f.allvar===a).length]));}
const md=(v)=>String(v).replace(/\|/g,'\\|').replace(/\r?\n/g,' ');
function skapaMarkdown(g,projektrot){
  const totalt=g.resultat.reduce((s,r)=>s+r.antalUppgifter,0),summa=summera(g),alla=[...g.systemfynd,...g.resultat.flatMap((r)=>r.fynd)];
  const rader=['# Granskningslogg för Uppgiftslabbet','',`- Skapad: ${new Date().toISOString()}`,`- Projektrot: \`${projektrot}\``,`- Kontrollerade banker: ${g.filer.length}`,`- Kontrollerade uppgifter: ${totalt}`,`- **ERROR:** ${summa.ERROR}`,`- **WARNING:** ${summa.WARNING}`,`- **INFO:** ${summa.INFO}`,'','## Allvarsnivåer','','- **ERROR**: hög säkerhet; brutet format, saknad obligatorisk metadata eller referens som inte kan lösas.','- **WARNING**: sannolik avvikelse som behöver mänsklig bedömning.','- **INFO**: osäker kvalitets-, likhets- eller tillgänglighetsobservation; aldrig ett säkert fel.','','## Format som kontrollerna bygger på','','- Kärnfält i samtliga sju banker: `id`, `kap`, `omr`, `niva`, `poang`, `t`, `s`, `familj`, `formaga`, `miniräknare`, `geogebra` och självrättningsmetadata.','- Matematikbankernas spår lagras i arrayen `kurs`; fysikbankerna och Matematik fördjupning saknar normalt detta fält.','- Poäng godtas både som `1/0/0` och `(1/0/0)`.','- Nästlade arrayer tillåts i bland annat `rättSvar`, `självrättning`, `tolerans` och svarmetadata.','- Deluppgifter kan använda `t` eller `fraga`; osäkra antalsskillnader rapporteras som WARNING.','- Textlikhet är en heuristik: exakta normaliserade dubbletter är WARNING och talvarierade textmallar är INFO.','','## Sammanställning per bank','','| Bank | Struktur | Uppgifter | ERROR | WARNING | INFO |','|---|---|---:|---:|---:|---:|'];
  for(const r of g.resultat){const a=Object.fromEntries(ALLVAR.map((x)=>[x,r.fynd.filter((f)=>f.allvar===x).length]));rader.push(`| ${r.fil} | ${r.strukturfil} | ${r.antalUppgifter} | ${a.ERROR} | ${a.WARNING} | ${a.INFO} |`);}
  rader.push('','## Sammanställning per kontroll','','| Allvar | Kod | Antal |','|---|---|---:|');const per=new Map();for(const f of alla){const k=`${f.allvar}\0${f.kod}`;per.set(k,(per.get(k)||0)+1);}for(const[k,n]of[...per].sort()){const[a,c]=k.split('\0');rader.push(`| ${a} | \`${c}\` | ${n} |`);}if(!alla.length)rader.push('| – | Inga avvikelser | 0 |');
  for(const allvar of ALLVAR){rader.push('',`## ${allvar}`,'');const grupp=new Map();for(const f of alla.filter((x)=>x.allvar===allvar)){if(!grupp.has(f.kod))grupp.set(f.kod,[]);grupp.get(f.kod).push(f);}if(!grupp.size){rader.push('Inga fynd.');continue;}for(const[kod,fynd]of[...grupp].sort()){rader.push(`### ${kod} (${fynd.length})`,'');for(const f of fynd.slice(0,250))rader.push(`- \`${f.fil}\` · \`${md(f.id)}\` · position ${f.index}: ${md(f.meddelande)}`);if(fynd.length>250)rader.push(`- … ${fynd.length-250} ytterligare fynd utelämnade ur detaljlistan; totalsiffran ovan omfattar dem.`);rader.push('');}}
  rader.push('## Körning','','```text','node --test tools/granska-uppgifter.test.js','node tools/granska-uppgifter.js --output GRANSKNINGSLOGG.md','```','');return rader.join('\n');
}
function summera(g){return summeraFynd(g);}
function argumentEfter(flagga){const i=process.argv.indexOf(flagga);return i>=0?process.argv[i+1]:null;}
function main(){const rot=path.resolve(__dirname,'..'),g=granskaProjekt(rot),markdown=skapaMarkdown(g,rot),output=argumentEfter('--output');if(output){const mal=path.resolve(rot,output);fs.writeFileSync(mal,markdown,'utf8');console.log(`Granskningen sparades i ${path.relative(rot,mal)}.`);}else process.stdout.write(markdown);if(g.lasfel.length)process.exitCode=2;}
module.exports={granskaBank,granskaProjekt,skapaMarkdown,kontrolleraLatex,kontrolleraHtml,kontrolleraSvg};
if(require.main===module)main();
