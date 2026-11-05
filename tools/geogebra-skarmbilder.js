#!/usr/bin/env node
'use strict';
/*
 * Skapar riktiga, markerade skärmbilder från GeoGebra Classic (svenska) för
 * statistikfacit: kalkylblad -> Envariabelanalys -> Σx -> statistikrader.
 *
 * GeoGebra körs lokalt från GeoGebra Math Apps-paketet (icke-kommersiell
 * licens, https://www.geogebra.org/license). Paketet ligger inte i repot.
 * Hämta det t.ex. ur npm-paketet node-geogebra:
 *   npm pack node-geogebra@1.3.2 && tar xzf node-geogebra-1.3.2.tgz
 *   export GGB_BUNDLE=$PWD/package/geogebra-math-apps-bundle/GeoGebra
 * Kontrollerad version: GeoGebra 5.4.916 (samma gränssnitt som
 * geogebra.org/classic 2026-11-05).
 *
 * Användning:
 *   node tools/geogebra-skarmbilder.js <spec.json> <utmapp> [jobb-slug ...]
 * Skriver PNG-filer och <utmapp>/geogebra-skarmbilder-logg.json med de värden
 * som GeoGebra faktiskt visade (används för att kontrollera facit).
 * Bilderna komprimeras efteråt med tools/geogebra-skarmbilder-komprimera.py.
 */
const fs = require('fs');
const path = require('path');
const http = require('http');
// Utan Playwright och lokalt GeoGebra-paket: GGB_WEBB=1 kör riktiga GeoGebra Classic från
// geogebra.org/classic?lang=sv via tools/geogebra-cdp-playwright.js (samma bilder och kontroller).
const WEBB = !!process.env.GGB_WEBB;
const { chromium } = WEBB ? require('./geogebra-cdp-playwright.js') : require('playwright');

const VIEW = { width: 1100, height: 660 };
const RED = '#d9480f';

function startServer(bundleDir) {
  const index = `<!doctype html><html><head><meta charset="utf-8"><title>GeoGebra</title>
<style>html,body{margin:0;padding:0;height:100%;overflow:hidden;background:#fff}
.snackbarComponent,.gwt-PopupPanel.snackbar,.matOpenKeyboardBtn{display:none!important}</style>
<script src="GeoGebra/deployggb.js"></script></head><body><div id="ggb"></div><script>
var params={appName:"classic",width:window.innerWidth,height:window.innerHeight,language:"sv",
showToolBar:true,showMenuBar:true,showAlgebraInput:true,allowStyleBar:true,useBrowserForJS:false,
showResetIcon:false,appletOnLoad:function(api){window.api=api;window.ggbReady=true;}};
var applet=new GGBApplet(params,true);applet.setHTML5Codebase("GeoGebra/HTML5/5.0/web3d/");
window.onload=function(){applet.inject("ggb");};</script></body></html>`;
  const types = { '.js': 'text/javascript', '.mjs': 'text/javascript', '.css': 'text/css', '.html': 'text/html',
    '.png': 'image/png', '.gif': 'image/gif', '.svg': 'image/svg+xml', '.woff': 'font/woff', '.woff2': 'font/woff2', '.json': 'application/json' };
  const root = path.dirname(path.resolve(bundleDir));
  const server = http.createServer((req, res) => {
    const url = decodeURIComponent(req.url.split('?')[0]);
    if (url === '/' || url === '/index.html') { res.writeHead(200, { 'Content-Type': 'text/html; charset=utf-8' }); return res.end(index); }
    const file = path.join(root, path.normalize(url).replace(/^([\\/])+/, ''));
    if (!file.startsWith(root) || !fs.existsSync(file) || fs.statSync(file).isDirectory()) { res.writeHead(404); return res.end(); }
    res.writeHead(200, { 'Content-Type': types[path.extname(file)] || 'application/octet-stream' });
    fs.createReadStream(file).pipe(res);
  });
  return new Promise((resolve) => server.listen(0, '127.0.0.1', () => resolve(server)));
}

async function newApp(browser, port, view = VIEW) {
  let page;
  if (WEBB) {
    page = await browser.newPage({ viewport: view, deviceScaleFactor: 2 });
    await page.goto('https://www.geogebra.org/classic?lang=sv');
    await page.waitForFunction(() => !!(window.ggbApplet && window.ggbApplet.evalCommand), null, { timeout: 120000 });
    // Kakbanner: välj det mest integritetsvänliga (bara nödvändiga kakor).
    for (const t of ['MORE OPTIONS', 'REJECT ALL']) {
      for (let k = 0; k < 12; k++) {
        const ok = await page.evaluate((t) => { const b = [...document.querySelectorAll('button')].find((x) => x.textContent.trim() === t); if (b) { b.click(); return true; } return false; }, t);
        if (ok) break; await page.waitForTimeout(500);
      }
    }
    await page.evaluate(() => { window.api = window.ggbApplet; const st = document.createElement('style');
      st.textContent = '.snackbarComponent,.gwt-PopupPanel.snackbar,.snackbar,.toolTipPanel{display:none!important}'; document.head.appendChild(st); });
  } else {
    const ctx = await browser.newContext({ viewport: view, deviceScaleFactor: 2, permissions: ['clipboard-read', 'clipboard-write'] });
    page = await ctx.newPage();
    page.on('close', () => ctx.close().catch(() => {}));
    await page.goto(`http://127.0.0.1:${port}/index.html`);
    await page.waitForFunction(() => window.ggbReady, null, { timeout: 120000 });
  }
  await page.waitForTimeout(1500);
  await page.click('.closeTabbedKeyboardButton').catch(() => {});
  await page.waitForTimeout(400);
  return page;
}

// Ritar markeringar ovanpå GeoGebra. items: {x,y,w,h, n?, label?, side?, mask?}
async function annotate(page, items) {
  await page.evaluate(({ items, RED }) => {
    // Dölj tipsrutor som ”Nybörjare? Kolla in vår Kalkylblad guide!”.
    for (const e of document.querySelectorAll('div')) { const r = e.getBoundingClientRect();
      if (r.height > 0 && r.height < 140 && /^Nybörjare\?/.test(e.textContent.trim()) && !e.querySelector('canvas')) e.style.visibility = 'hidden'; }
    let layer = document.getElementById('__ann');
    if (layer) layer.remove();
    layer = document.createElement('div');
    layer.id = '__ann';
    layer.style.cssText = 'position:fixed;left:0;top:0;width:100%;height:100%;pointer-events:none;z-index:2147483647;font-family:Arial,Helvetica,sans-serif';
    document.body.appendChild(layer);
    for (const it of items) {
      const pad = it.pad ?? 3;
      if (it.mask) {
        const m = document.createElement('div');
        m.style.cssText = `position:absolute;left:${it.x}px;top:${it.y}px;width:${it.w}px;height:${it.h}px;background:#e9ecef`;
        layer.appendChild(m);
        continue;
      }
      const b = document.createElement('div');
      b.style.cssText = `position:absolute;left:${it.x - pad}px;top:${it.y - pad}px;width:${it.w + 2 * pad}px;height:${it.h + 2 * pad}px;border:${it.bw || 3}px solid ${RED};border-radius:${it.round ? 999 : 7}px;box-sizing:border-box;box-shadow:0 0 0 2px #fff`;
      layer.appendChild(b);
      if (it.n || it.label) {
        const tag = document.createElement('div');
        const txt = (it.n ? `<b style="display:inline-block;min-width:20px;height:20px;line-height:20px;border-radius:10px;background:#fff;color:${RED};text-align:center;margin-right:${it.label ? 6 : 0}px">${it.n}</b>` : '') + (it.label || '');
        tag.innerHTML = txt;
        tag.style.cssText = `position:absolute;white-space:nowrap;background:${RED};color:#fff;font-size:${it.fs || 15}px;font-weight:bold;padding:3px 9px 3px 4px;border-radius:14px;box-shadow:0 1px 3px rgba(0,0,0,.35)`;
        layer.appendChild(tag);
        const tw = tag.offsetWidth, th = tag.offsetHeight;
        const side = it.side || 'right';
        let lx, ly;
        if (side === 'right') { lx = it.x + it.w + pad + 8; ly = it.y + it.h / 2 - th / 2; }
        else if (side === 'left') { lx = it.x - pad - 8 - tw; ly = it.y + it.h / 2 - th / 2; }
        else if (side === 'corner') { lx = it.x + it.w + pad - tw / 2; ly = it.y - pad - th / 2 + 4; }
        else if (side === 'inside') { lx = it.x + it.w - tw - 6; ly = it.y + it.h / 2 - th / 2; }
        else if (side === 'below') { lx = it.x + it.w / 2 - tw / 2; ly = it.y + it.h + pad + 7; }
        else { lx = it.x + it.w / 2 - tw / 2; ly = it.y - pad - 7 - th; }
        if (it.dx) lx += it.dx; if (it.dy) ly += it.dy;
        lx = Math.min(Math.max(2, lx), window.innerWidth - tw - 2);
        tag.style.left = `${lx}px`; tag.style.top = `${Math.max(2, ly)}px`;
      }
    }
  }, { items, RED });
  await page.waitForTimeout(150);
}
const clearAnn = (page) => page.evaluate(() => { const l = document.getElementById('__ann'); if (l) l.remove(); });

async function box(page, locator) {
  const b = await locator.boundingBox();
  if (!b) throw new Error('Hittade inte element för markering');
  return { x: b.x, y: b.y, w: b.width, h: b.height };
}

async function shoot(page, file, clip) {
  await page.screenshot({ path: file, clip: { x: clip.x, y: clip.y, width: clip.w, height: clip.h } });
  return file;
}

async function openMainMenuPerspektiv(page) {
  await page.locator('.rightButtonPanel button').last().click();
  await page.waitForTimeout(1000);
  await page.click('button.gwt-StackPanelItem:has-text("Perspektiv")');
  await page.waitForTimeout(1000);
}

async function chooseSpreadsheet(page) {
  await openMainMenuPerspektiv(page);
  await page.click('li.gwt-MenuItem[role=menuitem]:has-text("Kalkylblad")');
  await page.waitForTimeout(1800);
}

async function cellBox(page, col, row) {
  // geogebra.org ritar kalkylbladet på en canvas: kolumn A börjar vid x = 52, kolumnbredd 70,
  // rad 1 börjar vid y = 79 och radhöjden är 25 (uppmätt i vyn 1100 × 660).
  if (WEBB) return { x: 52 + 70 * (col.charCodeAt(0) - 65), y: 79 + 25 * (row - 1), w: 70, h: 25 };
  return page.evaluate(({ col, row }) => {
    const heads = [...document.querySelectorAll('td.SVheader')];
    const ch = heads.find((t) => t.textContent.trim() === col && t.getBoundingClientRect().y < 70);
    const rh = heads.find((t) => t.textContent.trim() === String(row) && t.getBoundingClientRect().x < 20);
    const a = ch.getBoundingClientRect(), b = rh.getBoundingClientRect();
    return { x: a.x, y: b.y, w: a.width, h: b.height };
  }, { col, row });
}

function fmtInput(v) { return String(v); }

async function typeColumn(page, values, col = 'A') {
  const c1 = await cellBox(page, col, 1);
  await page.mouse.click(c1.x + c1.w / 2, c1.y + c1.h / 2);
  await page.waitForTimeout(250);
  for (const v of values) {
    await page.keyboard.type(fmtInput(v), { delay: 30 });
    await page.waitForTimeout(80);
    await page.keyboard.press('Enter');
    await page.waitForTimeout(250);
  }
  await page.waitForTimeout(400);
  // Kontrollera att varje cell fick rätt värde (inmatningen kan tappa Enter under hög last).
  const got = await page.evaluate(({ col, n }) => Array.from({ length: n + 1 }, (_, k) => {
    const c = `${col}${k + 1}`; return api.exists(c) ? api.getValue(c) : null; }), { col, n: values.length });
  const bad = values.some((v, k) => got[k] === null || Math.abs(got[k] - v) > 1e-9) || got[values.length] !== null;
  if (bad) throw new Error(`Inmatningen blev fel: ${JSON.stringify(got)} i stället för ${JSON.stringify(values)}`);
  const cn = await cellBox(page, col, values.length);
  await page.mouse.move(c1.x + c1.w / 2, c1.y + c1.h / 2);
  await page.mouse.down();
  await page.mouse.move(cn.x + cn.w / 2, cn.y + cn.h / 2, { steps: 10 });
  await page.mouse.up();
  await page.waitForTimeout(500);
  return { x: c1.x, y: c1.y, w: c1.w, h: cn.y + cn.h - c1.y };
}

const barChartButton = (page) => page.locator('.toolbar_item').nth(1);

async function openOneVar(page) {
  await barChartButton(page).click();
  await page.waitForTimeout(900);
}
async function clickOneVar(page) {
  const b = await box(page, page.locator('li[mode="2020"]'));
  await page.mouse.move(b.x + 60, b.y + b.h / 2);
  await page.mouse.down(); await page.waitForTimeout(80); await page.mouse.up();
  await page.waitForSelector('select.gwt-ListBox', { timeout: 20000 });
  await page.waitForTimeout(1800);
}

const sigmaButton = (page) => page.locator('button.ToggleButton').first();

async function readStats(page) {
  return page.evaluate(() => {
    const out = {}; const rows = [];
    for (const tr of document.querySelectorAll('tr')) {
      const tds = [...tr.querySelectorAll('td')].filter((t) => t.offsetParent !== null);
      if (tds.length !== 2) continue;
      const k = tds[0].textContent.trim(), v = tds[1].textContent.trim();
      if (!/^(n|Medel|σ|s|Σx|Σx²|Min|Q1|Median|Q3|Max)$/.test(k)) continue;
      const a = tds[0].getBoundingClientRect(), b = tds[1].getBoundingClientRect();
      out[k] = v; rows.push({ k, v, x: a.x, y: a.y, w: b.x + b.width - a.x, h: a.height, vx: b.x, vw: b.width });
    }
    return { out, rows };
  });
}

// Hittar de högsta staplarna i stolpdiagrammet genom att läsa ritytans pixlar.
async function highestBars(page) {
  return page.evaluate(() => {
    const cands = [...document.querySelectorAll('canvas')].filter((c) => c.offsetParent !== null && c.clientWidth > 300);
    let best = [];
    for (const c of cands) {
      const ctx = c.getContext('2d');
      if (!ctx) continue;
      const W = c.width, H = c.height, k = W / c.clientWidth;
      const img = ctx.getImageData(0, 0, W, H).data;
      // Ljusgrön fyllning, eller mörkgrön kant när staplarna blir så smala att bara kanten ritas.
      const isFill = (i) => (Math.abs(img[i] - 179) < 14 && Math.abs(img[i + 1] - 212) < 14 && Math.abs(img[i + 2] - 179) < 14)
        || (img[i] < 60 && img[i + 1] > 70 && img[i + 1] < 160 && img[i + 2] < 60 && img[i + 3] > 200);
      const tops = new Array(W).fill(-1);
      for (let x = 0; x < W; x++) for (let y = 0; y < H; y++) if (isFill((y * W + x) * 4)) { tops[x] = y; break; }
      const runs = [];
      for (let x = 0; x < W; x++) {
        if (tops[x] < 0) continue;
        const r = runs[runs.length - 1];
        if (r && r.x1 === x - 1) { r.x1 = x; r.top = Math.min(r.top, tops[x]); } else runs.push({ x0: x, x1: x, top: tops[x] });
      }
      const good = runs.filter((r) => r.x1 - r.x0 >= 1);
      if (!good.length) continue;
      const minTop = Math.min(...good.map((r) => r.top));
      let bottom = 0;
      for (let y = H - 1; y >= 0 && !bottom; y--) for (const r of good) { const xm = Math.round((r.x0 + r.x1) / 2); if (isFill((y * W + xm) * 4)) { bottom = y; break; } }
      const rc = c.getBoundingClientRect();
      best = good.filter((r) => r.top - minTop <= 2).map((r) => ({ x: rc.x + r.x0 / k, y: rc.y + r.top / k, w: (r.x1 - r.x0 + 1) / k, h: (bottom - r.top + 1) / k }));
    }
    return best;
  });
}

async function sharedImages(browser, port, outDir) {
  const page = await newApp(browser, port);
  await openMainMenuPerspektiv(page);
  const menuBtn = await box(page, page.locator('.rightButtonPanel button').last());
  const persp = await box(page, page.locator('button.gwt-StackPanelItem:has-text("Perspektiv")'));
  const kalk = await box(page, page.locator('li.gwt-MenuItem[role=menuitem]:has-text("Kalkylblad")'));
  await annotate(page, [
    { ...menuBtn, n: 1, label: 'Meny', side: 'left', round: true },
    { ...persp, n: 2, side: 'inside', pad: 1 },
    { ...kalk, n: 3, side: 'inside', pad: 1 },
  ]);
  await shoot(page, path.join(outDir, 'geogebra-kalkylblad-perspektiv.png'), { x: 640, y: 0, w: 460, h: 400 });
  await clearAnn(page);
  await page.click('li.gwt-MenuItem[role=menuitem]:has-text("Kalkylblad")');
  await page.waitForTimeout(1800);
  await typeColumn(page, [4, 6, 8]);
  await openOneVar(page);
  const btn = await box(page, barChartButton(page));
  const item = await box(page, page.locator('li[mode="2020"]'));
  await annotate(page, [
    { ...btn, n: 1, side: 'corner', pad: 2 },
    { ...item, n: 2, side: 'inside', pad: 0 },
  ]);
  await shoot(page, path.join(outDir, 'geogebra-envariabelanalys-meny.png'), { x: 0, y: 0, w: 420, h: 230 });
  await page.close();
}

async function job(browser, port, outDir, j, log) {
  if (j.typ === 'normal') return normalJob(browser, port, outDir, j, log);
  const page = await newApp(browser, port);
  try { await jobSteps(page, outDir, j, log); } finally { await page.close(); }
}

// ---- Sannolikhetskalkylatorn (normalfördelning) ----
const NVIEW = { width: +(process.env.NVIEW_W || 520), height: +(process.env.NVIEW_H || 630) };
const MODE = { vanster: 'Öppet åt vänster', intervall: 'Intervall', hoger: 'Öppet åt höger' };
let urklippsLas = Promise.resolve();

async function openProbability(page) {
  await openMainMenuPerspektiv(page);
  await page.click('li.gwt-MenuItem[role=menuitem]:has-text("Sannolikhet")');
  await page.waitForSelector('.comboDistribution', { timeout: 20000 });
  await page.waitForTimeout(1500);
}

async function probFields(page) {
  return page.evaluate(() => [...document.querySelectorAll('.mathTextField')]
    .filter((f) => f.getAttribute('aria-hidden') !== 'true' && f.getBoundingClientRect().width > 0)
    .map((f) => { const r = f.getBoundingClientRect(); return { x: r.x, y: r.y, w: r.width, h: r.height }; }));
}

async function fillField(page, k, txt) {
  const f = (await probFields(page))[k];
  await page.mouse.click(f.x + f.w / 2, f.y + f.h / 2);
  await page.waitForTimeout(250);
  await page.keyboard.press('Control+A'); await page.keyboard.press('Backspace');
  await page.keyboard.type(String(txt), { delay: 30 });
  await page.keyboard.press('Enter');
  await page.waitForTimeout(900);
}

// Läser fältens innehåll via GeoGebras kopiering (fälten ritas i canvas). Ett lås hindrar
// att parallella sidor använder urklippet samtidigt.
async function readFields(page, index) {
  let res;
  const run = async () => {
    const out = [];
    const alla = await probFields(page);
    for (const f of index ? index.map((k) => alla[k]) : alla) {
      await page.mouse.click(f.x + f.w / 2, f.y + f.h / 2);
      await page.waitForTimeout(200);
      await page.evaluate(() => navigator.clipboard.writeText(''));
      await page.keyboard.press('Control+A'); await page.keyboard.press('Control+C');
      await page.waitForTimeout(250);
      out.push(await page.evaluate(() => navigator.clipboard.readText()));
      await page.keyboard.press('Escape');
    }
    res = out;
  };
  urklippsLas = urklippsLas.then(run, run);
  await urklippsLas;
  return res;
}

async function sharedProbability(browser, port, outDir) {
  const page = await newApp(browser, port, NVIEW);
  try {
    await openMainMenuPerspektiv(page);
    const menuBtn = await box(page, page.locator('.rightButtonPanel button').last());
    const persp = await box(page, page.locator('button.gwt-StackPanelItem:has-text("Perspektiv")'));
    const sann = await box(page, page.locator('li.gwt-MenuItem[role=menuitem]:has-text("Sannolikhet")'));
    await annotate(page, [
      { ...menuBtn, n: 1, label: 'Meny', side: 'left', round: true },
      { ...persp, n: 2, side: 'inside', pad: 1 },
      { ...sann, n: 3, side: 'inside', pad: 1 },
    ]);
    await shoot(page, path.join(outDir, 'geogebra-sannolikhet-perspektiv.png'), { x: NVIEW.width - 460, y: 0, w: 460, h: 420 });
  } finally { await page.close(); }
}

async function normalJob(browser, port, outDir, j, log) {
  const page = await newApp(browser, port, NVIEW);
  try {
    await openProbability(page);
    await page.evaluate(() => document.querySelectorAll('.snackbarComponent').forEach((e) => e.remove()));
    await fillField(page, 0, j.mu);
    await fillField(page, 1, j.sigma);
    await page.click(`button[title="${MODE[j.mode]}"]`);
    await page.waitForTimeout(900);
    const n = (await probFields(page)).length; // μ, σ, gräns(er), sannolikhet
    if (j.p !== undefined) await fillField(page, n - 1, j.p);
    else if (j.mode === 'intervall') { await fillField(page, 2, j.a); await fillField(page, 3, j.b); }
    else await fillField(page, 2, j.mode === 'hoger' ? j.a : j.b);
    await page.click('.closeTabbedKeyboardButton').catch(() => {});
    const vals = await readFields(page);
    // I läget Intervall är svaret en textetikett efter ") =" och inget fält.
    const etikett = await page.evaluate(() => {
      const ls = [...document.querySelectorAll('.gwt-Label')].filter((l) => l.offsetParent !== null);
      const k = ls.findIndex((l) => l.textContent.trim() === ') =');
      const l = k >= 0 ? ls[k + 1] : null;
      if (!l || !/^-?[0-9.]+$/.test(l.textContent.trim())) return null;
      const r = l.getBoundingClientRect();
      return { text: l.textContent.trim(), x: r.x, y: r.y + 8, w: r.width, h: r.height - 16 };
    });
    if (etikett) vals.push(etikett.text);
    // Avläsningen fokuserar varje fält, och GeoGebra räknar då om från det fält som lämnades sist.
    // Skriv därför in elevens indata igen så att bilden visar exakt det som eleven skriver.
    if (j.p !== undefined) await fillField(page, n - 1, j.p);
    else if (j.mode === 'intervall') { await fillField(page, 2, j.a); await fillField(page, 3, j.b); }
    else await fillField(page, 2, j.mode === 'hoger' ? j.a : j.b);
    {
      const efter = await readFields(page, j.p !== undefined ? [n - 1] : (j.mode === 'intervall' ? [2, 3] : [2]));
      const ska = j.p !== undefined ? [j.p] : (j.mode === 'intervall' ? [j.a, j.b] : [j.mode === 'hoger' ? j.a : j.b]);
      if (efter.some((x, k) => Math.abs(+x - +ska[k]) > 1e-9)) throw new Error(`${j.slug}: indata i bilden blev ${efter}, ska vara ${ska}`);
    }
    await page.evaluate(() => document.activeElement && document.activeElement.blur());
    await page.click('.closeTabbedKeyboardButton').catch(() => {});
    await page.waitForTimeout(600);
    const num = (x) => +String(x).replace('−', '-');
    if (num(vals[0]) !== +j.mu || num(vals[1]) !== +j.sigma) throw new Error(`${j.slug}: μ/σ blev ${vals}`);
    const svar = j.p !== undefined ? vals[2] : vals[vals.length - 1];
    const visat = (+svar).toFixed(4).replace(/\.?0+$/, '');
    log[j.slug] = { mu: j.mu, sigma: j.sigma, mode: j.mode, falt: vals, svar, visat };
    if (j.expect !== undefined && Math.abs(+svar - +j.expect) > 0.00005 + 1e-12) {
      throw new Error(`${j.slug}: GeoGebra visar ${vals}, förväntat ${j.expect}`);
    }
    const f = await probFields(page);
    const btn = await box(page, page.locator(`button[title="${MODE[j.mode]}"]`));
    const items = [
      { ...f[0], n: 1, side: 'corner', pad: 2 },
      { ...f[1], n: 2, side: 'corner', pad: 2 },
      { ...btn, n: 3, side: 'corner', pad: 2 },
    ];
    const grans = f.slice(2, f.length - 1);
    const sann = etikett ? { x: etikett.x, y: etikett.y, w: etikett.w, h: etikett.h } : f[f.length - 1];
    if (etikett) grans.push(f[f.length - 1]);
    if (j.p !== undefined) {
      items.push({ ...sann, n: 4, side: 'corner', pad: 2 });
      for (const g of grans) items.push({ ...g, n: 5, label: 'Svaret', side: 'above', dx: 115, pad: 2 });
    } else {
      for (const [k, g] of grans.entries()) items.push({ ...g, n: 4, side: 'corner', pad: 2, dx: k ? 0 : 0 });
      items.push({ ...sann, n: 5, label: 'Svaret', side: 'right', pad: 2 });
    }
    await annotate(page, items);
    await shoot(page, path.join(outDir, `geogebra-${j.slug}.png`), { x: 0, y: 85, w: NVIEW.width, h: NVIEW.height - 85 });
  } finally { await page.close(); }
}

async function jobSteps(page, outDir, j, log) {
  await chooseSpreadsheet(page);
  const values = j.values;
  let cells = await typeColumn(page, values);
  if (j.freq) {
    // Frekvenstabell: antal i kolumn B. När A och B markeras räknar GeoGebra B som frekvenser.
    const b = await typeColumn(page, j.freq, 'B');
    const a1 = await cellBox(page, 'A', 1);
    await page.mouse.move(a1.x + a1.w / 2, a1.y + a1.h / 2); await page.mouse.down();
    await page.mouse.move(b.x + b.w / 2, b.y + b.h - 4, { steps: 10 }); await page.mouse.up();
    await page.waitForTimeout(500);
    cells = { x: cells.x, y: cells.y, w: b.x + b.w - cells.x, h: cells.h };
  }
  const btn = await box(page, barChartButton(page));
  const last = values.length;
  await annotate(page, [
    { ...cells, n: 1, label: `${j.freq ? `A1–B${last}` : `A1–A${last}`} markerade`, side: 'right' },
    { ...btn, n: 2, label: 'Klicka här', side: 'right', pad: 2 },
  ]);
  const hData = Math.min(VIEW.height, cells.y + cells.h + 34);
  await shoot(page, path.join(outDir, `geogebra-${j.slug}-data.png`), { x: 0, y: 0, w: j.freq ? 420 : 330, h: hData });
  await clearAnn(page);

  await openOneVar(page);
  await clickOneVar(page);
  const sig = await box(page, sigmaButton(page));
  await annotate(page, [{ ...sig, label: 'Klicka på Σx', side: 'below', dx: -70, fs: 26, bw: 5, pad: 3 }]);
  await shoot(page, path.join(outDir, `geogebra-${j.slug}-analys.png`), { x: 200, y: 50, w: 900, h: 610 });
  await clearAnn(page);

  if (j.stolp) {
    const sel = page.locator('select.gwt-ListBox').first();
    await sel.selectOption({ label: 'Stolpdiagram' });
    await page.waitForTimeout(1500);
    const sb = await box(page, sel);
    let bars = await highestBars(page);
    for (let k = 0; k < 8 && !bars.length; k++) { await page.waitForTimeout(800); bars = await highestBars(page); }
    if (!bars.length) { await shoot(page, path.join(outDir, `DEBUG-${j.slug}-stolp.png`), { x: 0, y: 0, w: VIEW.width, h: VIEW.height }); throw new Error(`${j.slug}: hittade inga staplar i stolpdiagrammet`); }
    await annotate(page, [{ ...sb, label: 'Välj Stolpdiagram', side: 'right', dx: 66, pad: 2, fs: 22, bw: 5 },
      ...bars.map((r, i) => ({ ...r, pad: r.w < 8 ? 9 : 5, bw: r.w < 8 ? 3 : 6, fs: 26,
        label: i === 0 ? (bars.length > 1 ? 'Högsta staplarna' : 'Högst stapel') : '', side: 'above' }))]);
    await shoot(page, path.join(outDir, `geogebra-${j.slug}-stolp.png`), { x: 200, y: 50, w: 900, h: 610 });
    await clearAnn(page);
    await sel.selectOption({ label: 'Histogram' });
    await page.waitForTimeout(800);
  }

  await sigmaButton(page).click();
  await page.waitForFunction(() => [...document.querySelectorAll('td')].some((t) => t.textContent.trim() === 'Median' && t.offsetParent !== null), null, { timeout: 15000 });
  await page.waitForTimeout(1200);
  const { out, rows } = await readStats(page);
  const antal = j.freq ? j.freq.reduce((x, y) => x + y, 0) : values.length;
  const summa = values.reduce((x, y, k) => x + y * (j.freq ? j.freq[k] : 1), 0);
  if (+out.n !== antal || Math.abs(+out['Σx'] - summa) > 1e-6) throw new Error(`${j.slug}: GeoGebra visar n=${out.n}, Σx=${out['Σx']}`);
  log[j.slug] = { values, freq: j.freq, stats: out };
  if (j.expect) {
    for (const [k, v] of Object.entries(j.expect)) {
      if (String(out[k]) !== String(v)) throw new Error(`${j.slug}: GeoGebra visar ${k} = ${out[k]}, förväntat ${v}`);
    }
  }
  const top = rows[0], bottom = rows[rows.length - 1];
  const tableClip = { x: top.x - 8, y: top.y - 40, w: top.w + 16, h: bottom.y + bottom.h - top.y + 48 };
  for (const st of j.stats || []) {
    const items = [];
    for (const r of rows) {
      if (st.show && !st.show.includes(r.k)) items.push({ x: r.vx + 1, y: r.y + 1, w: r.vw - 2, h: r.h - 2, mask: true });
    }
    for (const r of rows) if ((st.frame || []).includes(r.k)) items.push({ x: r.x, y: r.y, w: r.w, h: r.h, pad: 1 });
    await annotate(page, items);
    await shoot(page, path.join(outDir, `geogebra-${j.slug}-${st.name}.png`), tableClip);
    await clearAnn(page);
  }
}

(async () => {
  const [specFile, outDir, ...only] = process.argv.slice(2);
  if (!specFile || !outDir || !(process.env.GGB_BUNDLE || WEBB)) {
    console.error('Användning: GGB_BUNDLE=<.../GeoGebra> node tools/geogebra-skarmbilder.js spec.json utmapp [slug ...]');
    process.exit(2);
  }
  const spec = JSON.parse(fs.readFileSync(specFile, 'utf8'));
  fs.mkdirSync(outDir, { recursive: true });
  const server = WEBB ? { close() {}, address: () => ({ port: 0 }) } : await startServer(process.env.GGB_BUNDLE);
  const port = server.address().port;
  const browser = await chromium.launch();
  const logFile = path.join(outDir, 'geogebra-skarmbilder-logg.json');
  const log = fs.existsSync(logFile) ? JSON.parse(fs.readFileSync(logFile, 'utf8')) : {};
  let fel = 0;
  try {
    if (!only.length || only.includes('shared')) await sharedImages(browser, port, outDir);
    if (only.includes('shared-normal') || (!only.length && spec.jobs.some((j) => j.typ === 'normal'))) await sharedProbability(browser, port, outDir);
    const ko = spec.jobs.filter((j) => !only.length || only.includes(j.slug));
    const parallellt = Math.max(1, +(process.env.GGB_PARALLELLT || 3));
    await Promise.all(Array.from({ length: parallellt }, async () => {
      while (ko.length) {
        const j = ko.shift();
        let klar = false;
        for (let forsok = 1; forsok <= 3 && !klar; forsok++) {
          try { await job(browser, port, outDir, j, log); klar = true; console.log('ok', j.slug, JSON.stringify(log[j.slug].stats || log[j.slug].falt)); }
          catch (e) { console.error(`försök ${forsok} misslyckades`, j.slug, e.message); }
        }
        if (!klar) { fel++; console.error('FEL', j.slug); }
      }
    }));
  } finally {
    fs.writeFileSync(logFile, JSON.stringify(log, null, 1));
    await browser.close();
    server.close();
  }
  process.exit(fel ? 1 : 0);
})();
