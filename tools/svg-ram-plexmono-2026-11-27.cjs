#!/usr/bin/env node
'use strict';
/*
 * Vidgar SVG-ramen (viewBox) där en text hamnar utanför bilden med typsnittet som Kunskapsgymmet
 * faktiskt laddar (IBM Plex Mono m.fl. från Google Fonts).
 *
 * Bakgrund (kvalitetsrapporten 2026-11-27): textförstoringen 2026-11-24 (commit 1a7e7b1) mättes med ett
 * smalare reservtypsnitt, eftersom granskningen inte laddade webbtypsnitten. Med IBM Plex Mono slutar t.ex.
 * ”R₂ = 1000 Ω” i Fy1 8.16 vid x ≈ 552 i en ram som slutar vid 532, så texten klipps av.
 *
 * För varje unik SVG i bankerna mäts alla synliga texter i figurens egna koordinater. Sticker en text ut mer än
 * 0,5 enheter vidgas viewBox åt det hållet (plus 4 enheters marginal), och width/height skalas i samma proportion,
 * så att ingenting flyttas eller förvrängs. Ingen annan del av figuren ändras.
 *
 *   node tools/svg-ram-plexmono-2026-11-27.cjs [--skriv] bank.js ...
 */
const fs = require('fs');
const path = require('path');
const { chromium } = require('playwright');

const skriv = process.argv.includes('--skriv');
const filer = process.argv.slice(2).filter((a) => !a.startsWith('--'));
const MARGINAL = 4;

function allaStrangar(v, ut) {
  if (typeof v === 'string') ut.push(v);
  else if (Array.isArray(v)) v.forEach((x) => allaStrangar(x, ut));
  else if (v && typeof v === 'object') Object.values(v).forEach((x) => allaStrangar(x, ut));
  return ut;
}

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1400, height: 900 } });
  await page.setContent(`<!doctype html><html><head><link rel="stylesheet"
    href="https://fonts.googleapis.com/css2?family=Instrument+Sans:wght@400;500;600;700&family=Atkinson+Hyperlegible:wght@400;700&family=IBM+Plex+Mono:wght@400;500;600&display=swap">
    </head><body style="margin:0"><div id="b" style="width:1200px"></div></body></html>`);
  const laddat = await page.evaluate(async () => {
    for (const w of [400, 500, 600, 700]) for (const f of ['IBM Plex Mono', 'Instrument Sans', 'Atkinson Hyperlegible']) {
      try { await document.fonts.load(`${w} 16px "${f}"`); } catch (_) {}
    }
    await document.fonts.ready;
    return document.fonts.check('600 16px "IBM Plex Mono"');
  });
  if (!laddat) throw new Error('IBM Plex Mono laddades inte');
  const sammanfattning = [];
  for (const fil of filer) {
    let src = fs.readFileSync(fil, 'utf8');
    const bank = JSON.parse(src.slice(src.indexOf('['), src.lastIndexOf(']') + 1));
    const svgTillId = new Map();
    for (const q of bank) {
      for (const s of allaStrangar(q, [])) {
        for (const m of s.match(/<svg[\s\S]*?<\/svg>/g) || []) {
          if (!svgTillId.has(m)) svgTillId.set(m, new Set());
          svgTillId.get(m).add(String(q.id));
        }
      }
    }
    const svgs = [...svgTillId.keys()].filter((s) => /<text/.test(s) && /viewBox=/.test(s));
    const resultat = await page.evaluate((svgs) => {
      const box = document.getElementById('b');
      const ut = [];
      for (const kod of svgs) {
        box.innerHTML = kod;
        const svg = box.querySelector('svg');
        if (!svg || !svg.viewBox || !svg.viewBox.baseVal || !svg.viewBox.baseVal.width) { ut.push(null); continue; }
        const vb = svg.viewBox.baseVal;
        const inv = svg.getScreenCTM().inverse();
        let x0 = vb.x, y0 = vb.y, x1 = vb.x + vb.width, y1 = vb.y + vb.height;
        const ute = [];
        for (const t of svg.querySelectorAll('text')) {
          const cs = getComputedStyle(t);
          if (cs.display === 'none' || cs.visibility === 'hidden' || !t.textContent.trim()) continue;
          const r = t.getBoundingClientRect();
          if (!r.width) continue;
          const hörn = [[r.left, r.top], [r.right, r.top], [r.left, r.bottom], [r.right, r.bottom]].map(([x, y]) => {
            const p = new DOMPoint(x, y).matrixTransform(inv); return [p.x, p.y];
          });
          const tx0 = Math.min(...hörn.map((p) => p[0])), tx1 = Math.max(...hörn.map((p) => p[0]));
          const ty0 = Math.min(...hörn.map((p) => p[1])), ty1 = Math.max(...hörn.map((p) => p[1]));
          if (tx0 < vb.x - 0.5 || tx1 > vb.x + vb.width + 0.5 || ty0 < vb.y - 0.5 || ty1 > vb.y + vb.height + 0.5) {
            ute.push(t.textContent.trim());
            x0 = Math.min(x0, tx0 - 4); x1 = Math.max(x1, tx1 + 4); y0 = Math.min(y0, ty0 - 4); y1 = Math.max(y1, ty1 + 4);
          }
        }
        ut.push(ute.length ? { ute, gl: [vb.x, vb.y, vb.width, vb.height], ny: [x0, y0, x1 - x0, y1 - y0] } : null);
      }
      box.innerHTML = '';
      return ut;
    }, svgs);
    let antal = 0;
    const tal = (v) => String(Math.round(v * 1000) / 1000);
    svgs.forEach((kod, i) => {
      const r = resultat[i];
      if (!r) return;
      const tagg = kod.match(/^<svg[^>]*>/)[0];
      const [, , gw, gh] = r.gl;
      const [nx, ny, nw, nh] = r.ny;
      let nytagg = tagg.replace(/viewBox="[^"]*"/, `viewBox="${tal(nx)} ${tal(ny)} ${tal(nw)} ${tal(nh)}"`);
      nytagg = nytagg.replace(/(\swidth=")([\d.]+)(")/, (m, a, w, b) => a + tal(Number(w) * nw / gw) + b);
      nytagg = nytagg.replace(/(\sheight=")([\d.]+)(")/, (m, a, h, b) => a + tal(Number(h) * nh / gh) + b);
      // Bakgrund som täckte den gamla ramen (rektanglar och kantlinjer över hela bredden eller höjden,
      // t.ex. land- och vattenbanden i 3.131) följer med till den nya ramen.
      const [gx, gy] = r.gl;
      const lika = (a, b) => Math.abs(Number(a) - b) < 0.01;
      let nykod = nytagg + kod.slice(tagg.length);
      nykod = nykod.replace(/<rect x="([-\d.]+)" y="([-\d.]+)" width="([\d.]+)" height="([\d.]+)"/g, (m, x, y, w, h) => {
        let [X, Y, W, H] = [x, y, w, h].map(Number);
        if (lika(X, gx) && lika(W, gw)) { X = nx; W = nw; }
        if (lika(Y, gy) && lika(H, gh)) { Y = ny; H = nh; }
        return `<rect x="${tal(X)}" y="${tal(Y)}" width="${tal(W)}" height="${tal(H)}"`;
      });
      nykod = nykod.replace(/<rect width="([\d.]+)" height="([\d.]+)"/g, (m, w, h) =>
        lika(gx, 0) && lika(gy, 0) && lika(w, gw) && lika(h, gh) ? `<rect x="${tal(nx)}" y="${tal(ny)}" width="${tal(nw)}" height="${tal(nh)}"` : m);
      nykod = nykod.replace(/<line x1="([-\d.]+)" y1="([-\d.]+)" x2="([-\d.]+)" y2="([-\d.]+)"/g, (m, a, b, c, d) => {
        let [x1, y1, x2, y2] = [a, b, c, d].map(Number);
        if (lika(y1, y2) && lika(Math.min(x1, x2), gx) && lika(Math.max(x1, x2), gx + gw)) {
          if (x1 < x2) { x1 = nx; x2 = nx + nw; } else { x2 = nx; x1 = nx + nw; }
        }
        if (lika(x1, x2) && lika(Math.min(y1, y2), gy) && lika(Math.max(y1, y2), gy + gh)) {
          if (y1 < y2) { y1 = ny; y2 = ny + nh; } else { y2 = ny; y1 = ny + nh; }
        }
        return `<line x1="${tal(x1)}" y1="${tal(y1)}" x2="${tal(x2)}" y2="${tal(y2)}"`;
      });
      const a = JSON.stringify(kod).slice(1, -1), b = JSON.stringify(nykod).slice(1, -1);
      const n = src.split(a).length - 1;
      if (!n) throw new Error('SVG hittades inte i filen: ' + [...svgTillId.get(kod)].join(','));
      src = src.split(a).join(b);
      antal += 1;
      sammanfattning.push(`${path.basename(fil)} ${[...svgTillId.get(kod)].join(',')}: ${r.ute.join(' | ')} · viewBox ${r.gl.map(tal).join(' ')} → ${r.ny.map(tal).join(' ')} (${n} ställen)`);
    });
    if (skriv && antal) fs.writeFileSync(fil, src);
    console.log(path.basename(fil), 'figurer att vidga:', antal);
  }
  console.log(sammanfattning.join('\n'));
  await browser.close();
})();
