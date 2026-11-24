#!/usr/bin/env node
'use strict';
/*
 * Läsbar figurtext i mobil (agent/SVG_UTSEENDE_2026-11-24.md).
 *
 * Figurerna skalas ned till kortets bredd i mobil, cirka 320 px i Kunskapsgymmet. En figur ritad i 600 enheters
 * bredd med 11 enheters text visar då text på 6 px. Verktyget:
 *   1. mäter i Chromium den verkliga textstorleken (font-size × skala) för varje figur i en 320 px bred ruta,
 *   2. skalar alla font-size i figuren med k = MAL / median (högst KMAX) när medianen är under MAL,
 *   3. kör SVG-granskningens analys (tools/granska-svg.js) på figuren före och efter och behåller ändringen bara om
 *      inget fynd av typerna i SPARR blir fler. Annars provas ett mindre k, och sist lämnas figuren orörd.
 * Bara font-size ändras (attribut, style och <style>), aldrig koordinater, och bara inne i figurerna.
 *
 *   CHROME_PATH=... node tools/svg-textstorlek-2026-11-24.cjs [--bank uppgifter.js] [--skriv] [--plan plan.json] [--fran-plan]
 * AI-banken byggs av sina byggskript och förstoras inte här (körningen 2026-11-24 gällde de sju gemensamma bankerna).
 * Utan --skriv skrivs bara planen och en sammanfattning.
 */
const fs = require('fs');
const path = require('path');
const os = require('os');
const { chromium } = require('playwright');
const G = require('./granska-svg.js');

const ROOT = path.resolve(__dirname, '..');
const BANKER = ['uppgifter.js', 'uppgifter2.js', 'uppgifterma1.js', 'uppgifterma2.js', 'uppgiftermato1.js', 'uppgiftermato2.js',
  'uppgiftermatf1.js'];
const BRED = 320;      // figurens bredd i ett mobilkort
const MAL = 10.5;      // önskad median för texten, px
const KMIN = 1.12;     // mindre förstoring än så görs inte
const KMAX = 1.5;
const SPARR = ['TEXT_TEXT_COLLISION', 'TEXT_GEOMETRY_COLLISION', 'TEXT_PARTIALLY_OUTSIDE_VIEWBOX', 'TEXT_FULLY_OUTSIDE_VIEWBOX',
  'POINT_LABEL_COLLISION', 'MEASUREMENT_LABEL_CROSSES_GEOMETRY', 'DEGREE_LABEL_MISPLACED', 'EDGE_CLIPPING'];
const FALT = (q) => [q.t, q.spelIntro, q.s, q.ledtrad, ...(q.spelDelar || []).flatMap((d) => [d.t, d.fraga, d.s, d.ledtrad])];

const arg = (n, d) => { const i = process.argv.indexOf(n); return i >= 0 ? process.argv[i + 1] : d; };

function lasBank(fil) {
  const s = fs.readFileSync(path.join(ROOT, fil), 'utf8');
  return JSON.parse(s.slice(s.indexOf('['), s.lastIndexOf(']') + 1));
}

function figurer(bank) {
  const m = new Map();
  for (const q of bank) for (const v of FALT(q)) {
    if (typeof v !== 'string') continue;
    for (const svg of v.match(/<svg[\s\S]*?<\/svg>/g) || []) {
      if (!m.has(svg)) m.set(svg, []);
      if (!m.get(svg).includes(q.id)) m.get(svg).push(q.id);
    }
  }
  return m;
}

const avr = (x) => String(Math.round(x * 100) / 100);
function skala(svg, k) {
  // attribut: font-size="12" / font-size="12px"
  let ny = svg.replace(/(\sfont-size=)(["'])\s*([\d.]+)(px)?\s*\2/g, (_, a, q, v, px) => `${a}${q}${avr(parseFloat(v) * k)}${px || ''}${q}`);
  // style och <style>: font-size:12px / font-size: 12
  ny = ny.replace(/(font-size\s*:\s*)([\d.]+)(px)?(?=\s*[;"'}])/g, (_, a, v, px) => `${a}${avr(parseFloat(v) * k)}${px || ''}`);
  // font-kortform i style: font: 600 12px Arial
  ny = ny.replace(/(font\s*:\s*(?:[a-z0-9]+\s+)*?)([\d.]+)px/g, (_, a, v) => `${a}${avr(parseFloat(v) * k)}px`);
  return ny;
}

async function mat(svgs) {
  const br = await chromium.launch(process.env.CHROME_PATH ? { executablePath: process.env.CHROME_PATH } : {});
  const pg = await br.newPage({ viewport: { width: BRED + 40, height: 800 } });
  const ut = [];
  for (let i = 0; i < svgs.length; i += 120) {
    const del = svgs.slice(i, i + 120);
    await pg.setContent(`<!doctype html><meta charset="utf-8"><style>body{margin:0;font:17px Arial,sans-serif}
      .c{width:${BRED}px;margin:0 20px 30px;overflow:hidden}svg{max-width:100%;height:auto;display:block}</style>
      ${del.map((s, j) => `<div class="c" id="c${j}">${s}</div>`).join('')}`);
    ut.push(...await pg.evaluate((n) => {
      const r = [];
      for (let j = 0; j < n; j++) {
        const svg = document.querySelector('#c' + j + ' svg');
        const st = [];
        for (const t of svg ? svg.querySelectorAll('text') : []) {
          if (!t.textContent.trim()) continue;
          const m = t.getScreenCTM();
          st.push(parseFloat(getComputedStyle(t).fontSize) * (m ? Math.hypot(m.a, m.b) : 1));
        }
        st.sort((a, b) => a - b);
        r.push(st.length ? st[Math.floor(st.length / 2)] : null);
      }
      return r;
    }, del.length));
  }
  await br.close();
  return ut;
}

function antal(res) {
  const c = {};
  for (const f of res.findings || []) if (SPARR.includes(f.code)) c[f.code] = (c[f.code] || 0) + 1;
  return c;
}
const samre = (fore, efter) => SPARR.some((k) => (efter[k] || 0) > (fore[k] || 0));

async function main() {
  const banker = arg('--bank') ? [arg('--bank')] : BANKER;
  const planfil = arg('--plan', path.join(os.tmpdir(), 'svg-textstorlek-plan.json'));
  // --fran-plan: skriv en redan granskad plan utan att mäta om
  const plan = process.argv.includes('--fran-plan') ? JSON.parse(fs.readFileSync(planfil, 'utf8')) : {};
  for (const fil of process.argv.includes('--fran-plan') ? [] : banker) {
    const figs = figurer(lasBank(fil));
    const svgs = [...figs.keys()];
    const med = await mat(svgs);
    const kand = svgs.map((s, i) => ({ s, med: med[i] })).filter((x) => x.med && x.med < MAL / KMIN && /font-size/.test(x.s));
    const forsok = [];
    for (const x of kand) {
      const k = Math.min(KMAX, MAL / x.med);
      x.k = [k, 1 + (k - 1) / 2].filter((v) => v >= KMIN - 1e-9);
      x.ny = x.k.map((v) => skala(x.s, v));
    }
    const lista = [];
    for (const x of kand) { lista.push({ svg: x.s }); for (const n of x.ny) lista.push({ svg: n }); }
    const res = await G.analyzeSvgFigures(lista, { chromePath: G.resolveChromePath() });
    let p = 0, ok = 0, halv = 0, nej = 0, oforand = 0;
    plan[fil] = [];
    for (const x of kand) {
      const fore = antal(res[p++]);
      const efter = x.ny.map(() => antal(res[p++]));
      let val = -1;
      for (let i = 0; i < x.ny.length; i++) if (!samre(fore, efter[i])) { val = i; break; }
      if (x.ny.every((n) => n === x.s)) { oforand++; continue; }
      if (val < 0) { nej++; forsok.push({ ids: figs.get(x.s).slice(0, 3), med: +x.med.toFixed(1), fore, efter: efter[0] }); continue; }
      if (val === 0) ok++; else halv++;
      plan[fil].push({ gammal: x.s, ny: x.ny[val], k: +x.k[val].toFixed(2), med: +x.med.toFixed(1), ids: figs.get(x.s) });
    }
    console.log(`${fil}: figurer ${svgs.length}, för liten text ${kand.length}, förstoras ${ok} (+${halv} med halvt k), lämnas ${nej} (spärren), utan font-size-attribut ${oforand}`);
    plan[fil + '#lamnade'] = forsok;
  }
  if (!process.argv.includes('--fran-plan')) { fs.writeFileSync(planfil, JSON.stringify(plan)); console.log('plan:', planfil); }
  if (!process.argv.includes('--skriv')) return;
  for (const fil of banker) {
    const p = path.join(ROOT, fil);
    let src = fs.readFileSync(p, 'utf8');
    const fore = JSON.parse(src.slice(src.indexOf('['), src.lastIndexOf(']') + 1));
    let n = 0;
    for (const { gammal, ny } of plan[fil]) {
      const a = JSON.stringify(gammal).slice(1, -1), b = JSON.stringify(ny).slice(1, -1);
      const delar = src.split(a);
      if (delar.length < 2) throw new Error(`${fil}: figuren hittades inte som literal (${gammal.slice(0, 80)})`);
      n += delar.length - 1;
      src = delar.join(b);
    }
    const efter = JSON.parse(src.slice(src.indexOf('['), src.lastIndexOf(']') + 1));
    const utanFig = (q) => JSON.stringify(q).replace(/<svg[\s\S]*?<\/svg>/g, '');
    for (let i = 0; i < fore.length; i++) if (utanFig(fore[i]) !== utanFig(efter[i])) throw new Error(`${fil} ${fore[i].id}: ändring utanför figur`);
    fs.writeFileSync(p, src, 'utf8');
    console.log(`${fil}: ${plan[fil].length} figurer, ${n} förekomster skrivna`);
  }
}

main().catch((e) => { console.error(e); process.exit(1); });
