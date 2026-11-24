#!/usr/bin/env node
'use strict';
/*
 * Läsbar figurtext i mobil, steg 2: selektiv förstoring (agent/SVG_UTSEENDE_2026-11-24.md).
 *
 * Steg 1 (svg-textstorlek-2026-11-24.cjs) förstorade all text i en figur eller ingenting. 558 figurer stoppades av
 * spärren, oftast för att en eller ett par etiketter krockade. Här förstoras varje <text> för sig:
 *   1. I Chromium mäts varje <text> (dokumentordning): beräknad font-size i figurens enheter och px-skala i ett
 *      320 px brett mobilkort. Figurer med median under MAL px är kandidater.
 *   2. Texterna delas i grupper med samma ursprungliga storlek, färg och vikt (axeltal, punktetiketter, rubriker …).
 *      Alla får font-size = beräknad storlek × k (k = MAL / median, högst KMAX). Uttryckliga font-size på <tspan>
 *      inne i texten skalas med samma k.
 *   3. SVG-granskningens analys (tools/granska-svg.js) körs före och efter. För varje fyndtyp i SPARR som blivit fler
 *      får grupperna med texter i de nya fynden först halv förstoring och sedan ingen, så att en sorts etikett alltid
 *      har samma storlek. Text som hamnar utanför bilden får i
 *      stället en vidare viewBox (högst VIDGA av bredd/höjd). Detta upprepas högst VARV gånger.
 *   4. Figuren ändras bara om inget fynd i SPARR blivit fler och textens median ökat med minst VINST.
 * Koordinater ändras aldrig. Bara font-size, och i förekommande fall viewBox med width/height i samma proportion.
 *
 *   CHROME_PATH=... node tools/svg-textstorlek-selektiv-2026-11-24.cjs [--bank fil] [--plan plan.json] [--skriv] [--fran-plan]
 */
const fs = require('fs');
const path = require('path');
const os = require('os');
const { chromium } = require('playwright');
const G = require('./granska-svg.js');

const ROOT = path.resolve(__dirname, '..');
const BANKER = ['uppgifter.js', 'uppgifter2.js', 'uppgifterma1.js', 'uppgifterma2.js', 'uppgiftermato1.js', 'uppgiftermato2.js',
  'uppgiftermatf1.js'];
const BRED = 320, MAL = 10.5, KMAX = Number(process.env.KMAX || 1.5), VARV = 8, VINST = 1.08, VIDGA = Number(process.env.VIDGA || 0.12);
// Axeltal: rena tal, decimaltal, bråk och π-uttryck. När de förstoras flyttas de så att avståndet till axeln behålls.
const AXELTAL = /^\s*[−-]?(?:\d+(?:[,.]\d+)?|\d*\s*π(?:\s*\/\s*\d+)?|\d+\s*\/\s*\d+)\s*°?\s*$/;
const AXEL = process.argv.includes('--axel');
const SPARR = ['TEXT_TEXT_COLLISION', 'TEXT_GEOMETRY_COLLISION', 'TEXT_PARTIALLY_OUTSIDE_VIEWBOX', 'TEXT_FULLY_OUTSIDE_VIEWBOX',
  'POINT_LABEL_COLLISION', 'MEASUREMENT_LABEL_CROSSES_GEOMETRY', 'DEGREE_LABEL_MISPLACED', 'EDGE_CLIPPING'];
const UTANFOR = ['TEXT_PARTIALLY_OUTSIDE_VIEWBOX', 'EDGE_CLIPPING'];
// Ma2 3.14: testet ma2-kap3-overlapp-2026-10-27 är strängare än spärren (linje genom etikettens kärna).
// Ma1 2.05, 2.27 och Ma4 2.685: felrapporttester låser textkoordinater och viewBox.
const UNDANTAG = new Set(['uppgifterma2.js|3.14', 'uppgifterma1.js|2.05', 'uppgifterma1.js|2.27', 'uppgiftermato2.js|2.685']);
const FALT = (q) => [q.t, q.spelIntro, q.s, q.ledtrad, ...(q.spelDelar || []).flatMap((d) => [d.t, d.fraga, d.s, d.ledtrad])];
const arg = (n, d) => { const i = process.argv.indexOf(n); return i >= 0 ? process.argv[i + 1] : d; };
const avr = (x) => String(Math.round(x * 100) / 100);

function lasBank(fil) {
  const s = fs.readFileSync(path.join(ROOT, fil), 'utf8');
  return JSON.parse(s.slice(s.indexOf('['), s.lastIndexOf(']') + 1));
}
function figurer(fil) {
  const m = new Map();
  for (const q of lasBank(fil)) for (const v of FALT(q)) {
    if (typeof v !== 'string') continue;
    for (const svg of v.match(/<svg[\s\S]*?<\/svg>/g) || []) {
      if (!m.has(svg)) m.set(svg, []);
      if (!m.get(svg).includes(q.id)) m.get(svg).push(q.id);
    }
  }
  return m;
}

// <text …>…</text> i dokumentordning (samma ordning som querySelectorAll('text'))
function textSpann(svg) {
  const ut = [];
  const rx = /<text\b[^>]*>[\s\S]*?<\/text>/g;
  let m;
  while ((m = rx.exec(svg))) ut.push([m.index, m.index + m[0].length]);
  return ut;
}

function bygg(svg, matt, faktor, vb) {
  const sp = textSpann(svg);
  let ut = '', pos = 0;
  sp.forEach(([a, b], i) => {
    ut += svg.slice(pos, a);
    let bit = svg.slice(a, b);
    const k = faktor(i);
    if (k > 1.001) {
      const fsNy = avr(matt[i].enh * k);
      bit = bit.replace(/^<text\b[^>]*>/, (tag) => {
        let t = tag.replace(/\sfont-size=(["'])[^"']*\1/, '');
        t = t.replace(/(style=(["']))([^"']*)\2/, (_, a2, q, st) => {
          const ny = st.replace(/font-size\s*:\s*[^;]*;?\s*/g, '').trim();
          return ny ? `${a2}${ny}${q}` : '';
        }).replace(/\s+>$/, '>').replace(/\s{2,}/g, ' ');
        let ut2 = t.replace(/^<text\b/, `<text font-size="${fsNy}"`);
        // --axel: axeltal hålls centrerade mot sitt streck (start/end) eller växer bort från x-axeln (middle)
        const inne = bit.replace(/^<text\b[^>]*>/, '').replace(/<\/text>$/, '');
        if (AXEL && !/</.test(inne) && AXELTAL.test(inne.replace(/&minus;/g, '−'))) {
          const ym = ut2.match(/\sy=(["'])(-?[\d.]+)\1/);
          const anchor = (tag.match(/text-anchor=(["'])(\w+)\1/) || tag.match(/text-anchor\s*:\s*(\w+)/) || [])[2] || (tag.match(/text-anchor\s*:\s*(\w+)/) || [])[1] || 'start';
          if (ym && !/\s(?:dy|transform)=/.test(ut2)) {
            const d = matt[i].enh * (k - 1);
            const ny = parseFloat(ym[2]) + d * (anchor === 'middle' ? 0.72 : 0.34);
            ut2 = ut2.replace(ym[0], ` y=${ym[1]}${avr(ny)}${ym[1]}`);
          }
        }
        return ut2;
      });
      // tspan med egen absolut font-size skalas med samma faktor
      bit = bit.replace(/(<tspan\b[^>]*\sfont-size=)(["'])([\d.]+)(px)?\2/g, (_, a2, q, v, px) => `${a2}${q}${avr(parseFloat(v) * k)}${px || ''}${q}`);
    }
    ut += bit; pos = b;
  });
  ut += svg.slice(pos);
  if (vb) {
    ut = ut.replace(/^<svg\b[^>]*>/, (tag) => {
      let t = tag.replace(/\sviewBox=(["'])[^"']*\1/, ` viewBox="${vb.map(avr).join(' ')}"`);
      const w = tag.match(/\swidth=(["'])([\d.]+)\1/), h = tag.match(/\sheight=(["'])([\d.]+)\1/);
      if (w && h) t = t.replace(/\sheight=(["'])[\d.]+\1/, ` height="${avr(parseFloat(w[2]) * vb[3] / vb[2])}"`);
      return t;
    });
  }
  return ut;
}

async function mat(svgs) {
  const br = await chromium.launch(process.env.CHROME_PATH ? { executablePath: process.env.CHROME_PATH } : {});
  const pg = await br.newPage({ viewport: { width: BRED + 40, height: 800 } });
  const ut = [];
  for (let i = 0; i < svgs.length; i += 100) {
    const del = svgs.slice(i, i + 100);
    await pg.setContent(`<!doctype html><meta charset="utf-8"><style>body{margin:0;font:17px Arial,sans-serif}
      .c{width:${BRED}px;margin:0 20px 30px;overflow:hidden}svg{max-width:100%;height:auto;display:block}</style>
      ${del.map((s, j) => `<div class="c" id="c${j}">${s}</div>`).join('')}`);
    ut.push(...await pg.evaluate((n) => {
      const r = [];
      for (let j = 0; j < n; j++) {
        const svg = document.querySelector('#c' + j + ' svg');
        const t = [...(svg ? svg.querySelectorAll('text') : [])].map((e) => {
          const m = e.getScreenCTM();
          const enh = parseFloat(getComputedStyle(e).fontSize);
          const cs = getComputedStyle(e);
          return { enh, px: enh * (m ? Math.hypot(m.a, m.b) : 1), tom: !e.textContent.trim(), grupp: enh.toFixed(2) + '|' + cs.fill + '|' + cs.fontWeight };
        });
        const vb = svg && svg.viewBox && svg.viewBox.baseVal ? [svg.viewBox.baseVal.x, svg.viewBox.baseVal.y, svg.viewBox.baseVal.width, svg.viewBox.baseVal.height] : null;
        r.push({ t, vb });
      }
      return r;
    }, del.length));
  }
  await br.close();
  return ut;
}

const median = (a) => { const s = [...a].sort((x, y) => x - y); return s.length ? s[Math.floor(s.length / 2)] : null; };
function rakna(res) { const c = {}; for (const f of res.findings || []) if (SPARR.includes(f.code)) c[f.code] = (c[f.code] || 0) + 1; return c; }
// analysens elementindex → textordning
function textIndex(res) { const m = new Map(); let n = 0; for (const e of res.elements || []) if (e.tag === 'text') m.set(e.index, n++); return { m, n }; }
function nyckel(res, f, ti) { return f.code + '|' + (f.elements || []).filter((x) => ti.m.has(x)).map((x) => (res.elements[x] || {}).text).sort().join('/'); }

async function analysera(svgs) {
  return G.analyzeSvgFigures(svgs.map((svg) => ({ svg })), { chromePath: G.resolveChromePath() });
}

async function main() {
  const banker = arg('--bank') ? [arg('--bank')] : BANKER;
  const planfil = arg('--plan', path.join(os.tmpdir(), 'svg-textstorlek-selektiv.json'));
  const plan = process.argv.includes('--fran-plan') ? JSON.parse(fs.readFileSync(planfil, 'utf8')) : {};
  for (const fil of process.argv.includes('--fran-plan') ? [] : banker) {
    const figs = figurer(fil);
    const svgs = [...figs.keys()];
    const matt = await mat(svgs);
    let kand = svgs.map((s, i) => ({ s, m: matt[i] })).filter((x) => {
      const px = x.m.t.filter((t) => !t.tom).map((t) => t.px);
      x.med = median(px);
      return x.med && x.med < MAL / 1.12 && !figs.get(x.s).some((id) => UNDANTAG.has(fil + '|' + id));
    });
    const bas = await analysera(kand.map((x) => x.s));
    kand.forEach((x, i) => {
      x.bas = rakna(bas[i]);
      const ti = textIndex(bas[i]);
      x.basNycklar = new Set((bas[i].findings || []).filter((f) => SPARR.includes(f.code)).map((f) => nyckel(bas[i], f, ti)));
      x.k = Math.min(KMAX, MAL / x.med);
      // grupper: samma ursprungliga storlek, färg och vikt (t.ex. alla axeltal) får samma förstoring
      x.niva = new Map(x.m.t.map((t) => [t.grupp, 0]));   // 0 = k, 1 = halvt k, 2 = ingen
      x.f = (j) => { const n = x.niva.get(x.m.t[j].grupp); return x.m.t[j].tom || n >= 2 ? 1 : n === 1 ? 1 + (x.k - 1) / 2 : x.k; };
      x.aktiv = () => [...x.niva.values()].some((n) => n < 2);
      x.vb = null; x.klar = false; x.ok = false;
      x.fel = ti.n !== x.m.t.length || textSpann(x.s).length !== x.m.t.length;
    });
    kand = kand.filter((x) => !x.fel);
    for (let varv = 0; varv < VARV; varv++) {
      const aktiva = kand.filter((x) => !x.klar && x.aktiv());
      if (!aktiva.length) break;
      aktiva.forEach((x) => { x.ny = bygg(x.s, x.m.t, x.f, x.vb); });
      const res = await analysera(aktiva.map((x) => x.ny));
      aktiva.forEach((x, i) => {
        const r = res[i], c = rakna(r), ti = textIndex(r);
        const okade = SPARR.filter((k) => (c[k] || 0) > (x.bas[k] || 0));
        if (!okade.length) { x.klar = true; x.ok = true; return; }
        let atgard = false;
        // text utanför bilden: vidga viewBox en gång till alla texters ytterkant (+2 enheter)
        if (okade.some((k) => UTANFOR.includes(k)) && !x.vb && x.m.vb) {
          const tx = (r.elements || []).filter((e) => e.tag === 'text' && e.bbox && e.bbox.width > 0);
          const [vx, vy, vw, vh] = x.m.vb;
          let x0 = vx, y0 = vy, x1 = vx + vw, y1 = vy + vh;
          for (const e of tx) { x0 = Math.min(x0, e.bbox.x - 2); y0 = Math.min(y0, e.bbox.y - 2); x1 = Math.max(x1, e.bbox.x + e.bbox.width + 2); y1 = Math.max(y1, e.bbox.y + e.bbox.height + 2); }
          if ((x1 - x0) <= vw * (1 + VIDGA) && (y1 - y0) <= vh * (1 + VIDGA) && (x1 - x0 > vw || y1 - y0 > vh)) { x.vb = [x0, y0, x1 - x0, y1 - y0]; atgard = true; }
        }
        // grupper med texter i nya fynd: halvt k, sedan ingen förstoring
        const steg = new Set();
        for (const f of r.findings || []) {
          if (!okade.includes(f.code) || x.basNycklar.has(nyckel(r, f, ti))) continue;
          if (UTANFOR.includes(f.code) && atgard) continue;
          for (const e of f.elements || []) if (ti.m.has(e)) steg.add(x.m.t[ti.m.get(e)].grupp);
        }
        for (const g of steg) if (x.niva.get(g) < 2) { x.niva.set(g, x.niva.get(g) + 1); atgard = true; }
        if (!atgard) x.klar = true;
      });
    }
    plan[fil] = [];
    let ok = 0, svag = 0, nej = 0, vidgade = 0;
    for (const x of kand) {
      if (!x.ok) { nej++; continue; }
      const px = x.m.t.map((t, j) => t.px * x.f(j)).filter((v, j) => !x.m.t[j].tom);
      const nyMed = median(px) * (x.vb ? x.m.vb[2] / x.vb[2] : 1);
      if (nyMed < x.med * VINST) { svag++; continue; }
      ok++; if (x.vb) vidgade++;
      plan[fil].push({ gammal: x.s, ny: x.ny, ids: figs.get(x.s), med: +x.med.toFixed(1), nyMed: +nyMed.toFixed(1), k: +x.k.toFixed(2),
        andel: +(x.m.t.filter((t, j) => !t.tom && x.f(j) > 1.001).length / x.m.t.filter((t) => !t.tom).length).toFixed(2), vb: !!x.vb });
    }
    console.log(`${fil}: kandidater ${kand.length}, förstoras ${ok} (varav ${vidgade} med vidgad ram), för liten vinst ${svag}, lämnas ${nej}`);
  }
  if (!process.argv.includes('--fran-plan')) { fs.writeFileSync(planfil, JSON.stringify(plan)); console.log('plan:', planfil); }
  if (!process.argv.includes('--skriv')) return;
  for (const fil of banker) {
    const p = path.join(ROOT, fil);
    let src = fs.readFileSync(p, 'utf8');
    const fore = JSON.parse(src.slice(src.indexOf('['), src.lastIndexOf(']') + 1));
    let n = 0;
    for (const { gammal, ny } of plan[fil] || []) {
      const a = JSON.stringify(gammal).slice(1, -1), b = JSON.stringify(ny).slice(1, -1);
      const delar = src.split(a);
      if (delar.length < 2) throw new Error(`${fil}: figuren hittades inte (${gammal.slice(0, 80)})`);
      n += delar.length - 1; src = delar.join(b);
    }
    const efter = JSON.parse(src.slice(src.indexOf('['), src.lastIndexOf(']') + 1));
    const utanFig = (q) => JSON.stringify(q).replace(/<svg[\s\S]*?<\/svg>/g, '');
    for (let i = 0; i < fore.length; i++) if (utanFig(fore[i]) !== utanFig(efter[i])) throw new Error(`${fil} ${fore[i].id}: ändring utanför figur`);
    fs.writeFileSync(p, src, 'utf8');
    console.log(`${fil}: ${(plan[fil] || []).length} figurer, ${n} förekomster skrivna`);
  }
}
main().catch((e) => { console.error(e); process.exit(1); });
