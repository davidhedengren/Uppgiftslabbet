#!/usr/bin/env node
'use strict';
/*
 * Renderar statistikfacit med GeoGebra-skärmbilder i mobilbredd med Kunskapsgymmets CSS.
 * Kontrollerar KaTeX-fel, bilder som inte laddas och för breda element.
 *
 *   KATEX=<katex/package> node tools/geogebra-statistik-facit-2026-11-05.browser.js \
 *     ../kunskapsgymmet <utmapp> [--bilder 4.338a,4.453] 4.328 4.329 ...
 */
const fs = require('fs');
const path = require('path');
const { pathToFileURL } = require('url');
const { chromium } = require('playwright');

const root = path.resolve(__dirname, '..');
const [cssFrom, ut, ...rest] = process.argv.slice(2);
let bilder = [];
const ids = [];
for (let k = 0; k < rest.length; k++) {
  if (rest[k] === '--bilder') bilder = rest[++k].split(',');
  else ids.push(rest[k]);
}
const bredd = +(process.env.BREDD || 390);
const kd = path.join(process.env.KATEX, 'dist');
const src = fs.readFileSync(path.join(root, 'uppgifterma2.js'), 'utf8');
const bank = JSON.parse(src.slice(src.indexOf('['), src.lastIndexOf(']') + 1));
const by = Object.fromEntries(bank.map((u) => [u.id, u]));
const html = fs.readFileSync(path.join(cssFrom, 'index.html'), 'utf8');
const css = [...html.matchAll(/<style[^>]*>([\s\S]*?)<\/style>/g)].map((m) => m[1]).join('\n');
let kcss = fs.readFileSync(path.join(kd, 'katex.min.css'), 'utf8');
kcss = kcss.replace(/url\((fonts\/[^)]+)\)/g, (_, f) => `url(data:font/woff2;base64,${fs.readFileSync(path.join(kd, f)).toString('base64')})`);
fs.mkdirSync(ut, { recursive: true });

(async () => {
  const b = await chromium.launch();
  const page = await b.newPage({ viewport: { width: bredd, height: 900 } });
  const sida = path.join(ut, '_render.html');
  fs.writeFileSync(sida, `<!doctype html><meta charset="utf-8"><base href="${pathToFileURL(root).href}/"><style>${css}\n${kcss}
html,body{height:auto!important;overflow:visible!important}body{display:block;padding:10px}
#review{height:auto!important;overflow:visible!important}.facit{display:block;width:100%;box-sizing:border-box}</style><main id="review"></main>`);
  await page.goto(pathToFileURL(sida).href);
  await page.addScriptTag({ path: path.join(kd, 'katex.min.js') });
  await page.addScriptTag({ path: path.join(kd, 'contrib', 'auto-render.min.js') });
  const fel = [];
  let antal = 0;
  for (const id of ids) {
    const u = by[id];
    const lista = [[id, u.s], ...(u.spelDelar || []).map((d) => [id + (d.etikett || ''), d.s])];
    for (const [namn, s] of lista) {
      await page.evaluate((s) => { const el = document.querySelector('#review'); el.innerHTML = `<div class="facit öppen">${s}</div>`; renderMathInElement(el, { throwOnError: false, strict: 'ignore' }); }, s);
      await page.waitForFunction(() => [...document.images].every((i) => i.complete), null, { timeout: 15000 });
      const r = await page.evaluate(() => ({
        kerr: document.querySelectorAll('.katex-error').length,
        broken: [...document.images].filter((i) => !i.naturalWidth).map((i) => i.getAttribute('src')),
        imgs: document.images.length,
        pageOverflow: document.documentElement.scrollWidth > innerWidth + 3,
        wide: [...document.querySelectorAll('.facit-matte,.facit-rubrik,.facit-svar,img')].filter((x) => x.getBoundingClientRect().right > innerWidth + 1 || x.scrollWidth > x.clientWidth + 3).map((x) => x.className || x.getAttribute('src')),
      }));
      antal++;
      if (r.kerr || r.broken.length || r.pageOverflow || r.wide.length || !r.imgs) fel.push({ facit: namn, ...r });
      if (bilder.includes(namn)) {
        await page.evaluate(() => scrollTo(0, 0));
        await page.screenshot({ path: path.join(ut, `facit-${namn}.png`), fullPage: true });
      }
    }
  }
  await b.close();
  console.log(JSON.stringify({ antal, fel }, null, 1));
  process.exit(fel.length ? 1 : 0);
})();
