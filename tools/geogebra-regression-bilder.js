#!/usr/bin/env node
'use strict';
/*
 * Skärmbilder av Tvåvariabels regressionsanalys i GeoGebra Classic (svenska) för Ma2-facit.
 * Samma bildstil som tools/geogebra-skarmbilder.js (orange ramar och etiketter).
 * Körs mot geogebra.org/classic via tools/geogebra-cdp-playwright.js (ingen Playwright behövs).
 *
 *   node tools/geogebra-regression-bilder.js <spec.json> <utmapp> [slug ...]
 *
 * spec: {"jobs":[{"slug":"4-138","x":[1,2,3],"y":[7,10,12],"modell":"Linjär","r":true,"berakna":6}]}
 * Bilder per jobb: geogebra-<slug>-data.png (A och B markerade, knappen inringad),
 * geogebra-<slug>-regression.png (modell, ekvation, Σx och r inringade), förstorade utsnitt -ekvation.png
 * och -r.png samt vid "berakna"
 * geogebra-<slug>-berakna.png (Beräkna-fältet med x och y). Den gemensamma menybilden
 * geogebra-tvavariabel-meny.png skapas med slug "shared". Ekvation, r och beräknat y skrivs
 * till <utmapp>/geogebra-regression-logg.json för kontroll mot facit.
 * Logg: agent/MA2_REGRESSION_GEOGEBRA_BILDER_2026-11-05.md
 */
const fs = require('fs');
const path = require('path');
const { chromium } = require('./geogebra-cdp-playwright.js');

const VIEW = { width: 1100, height: 660 };
const RED = '#d9480f';

async function newApp(browser) {
  const page = await browser.newPage({ viewport: VIEW, deviceScaleFactor: 2 });
  await page.goto('https://www.geogebra.org/classic?lang=sv');
  await page.waitForFunction(() => !!(window.ggbApplet && window.ggbApplet.evalCommand), null, { timeout: 120000 });
  for (const t of ['MORE OPTIONS', 'REJECT ALL']) {
    for (let k = 0; k < 12; k++) {
      const ok = await page.evaluate((t) => { const b = [...document.querySelectorAll('button')].find((x) => x.textContent.trim() === t); if (b) { b.click(); return true; } return false; }, t);
      if (ok) break; await page.waitForTimeout(500);
    }
  }
  await page.evaluate(() => { window.api = window.ggbApplet; const st = document.createElement('style');
    st.textContent = '.snackbarComponent,.gwt-PopupPanel.snackbar,.snackbar,.toolTipPanel{display:none!important}'; document.head.appendChild(st); });
  await page.waitForTimeout(1200);
  await page.click('.closeTabbedKeyboardButton').catch(() => {});
  return page;
}

// Samma markeringar som tools/geogebra-skarmbilder.js. items: {x,y,w,h, n?, label?, side?}
async function annotate(page, items) {
  await page.evaluate(({ items, RED }) => {
    // Dölj tipsrutor nere till vänster (”Nybörjare?”, ”Flytta …”).
    for (const e of document.querySelectorAll('div')) { const r = e.getBoundingClientRect();
      if (r.height > 0 && r.height < 140 && r.y > 450 && r.x < 60 && /^(Nybörjare\?|Flytta)/.test(e.textContent.trim()) && !e.querySelector('canvas')) e.style.visibility = 'hidden'; }
    let layer = document.getElementById('__ann'); if (layer) layer.remove();
    layer = document.createElement('div'); layer.id = '__ann';
    layer.style.cssText = 'position:fixed;left:0;top:0;width:100%;height:100%;pointer-events:none;z-index:2147483647;font-family:Arial,Helvetica,sans-serif';
    document.body.appendChild(layer);
    for (const it of items) {
      const pad = it.pad ?? 3;
      const b = document.createElement('div');
      b.style.cssText = `position:absolute;left:${it.x - pad}px;top:${it.y - pad}px;width:${it.w + 2 * pad}px;height:${it.h + 2 * pad}px;border:${it.bw || 3}px solid ${RED};border-radius:7px;box-sizing:border-box;box-shadow:0 0 0 2px #fff`;
      layer.appendChild(b);
      if (it.n || it.label) {
        const tag = document.createElement('div');
        tag.innerHTML = (it.n ? `<b style="display:inline-block;min-width:20px;height:20px;line-height:20px;border-radius:10px;background:#fff;color:${RED};text-align:center;margin-right:${it.label ? 6 : 0}px">${it.n}</b>` : '') + (it.label || '');
        tag.style.cssText = `position:absolute;white-space:nowrap;background:${RED};color:#fff;font-size:${it.fs || 15}px;font-weight:bold;padding:3px 9px 3px 4px;border-radius:14px;box-shadow:0 1px 3px rgba(0,0,0,.35)`;
        layer.appendChild(tag);
        const tw = tag.offsetWidth, th = tag.offsetHeight, side = it.side || 'right';
        let lx, ly;
        if (side === 'right') { lx = it.x + it.w + pad + 8; ly = it.y + it.h / 2 - th / 2; }
        else if (side === 'left') { lx = it.x - pad - 8 - tw; ly = it.y + it.h / 2 - th / 2; }
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
const shoot = (page, file, c) => page.screenshot({ path: file, clip: { x: c.x, y: c.y, width: c.w, height: c.h } });
const box = async (page, sel, i = 0) => { const b = await page.locator(sel).nth(i).boundingBox(); return { x: b.x, y: b.y, w: b.width, h: b.height }; };

async function kalkylblad(page) {
  await page.locator('.rightButtonPanel button').last().click(); await page.waitForTimeout(1000);
  await page.click('button.gwt-StackPanelItem:has-text("Perspektiv")'); await page.waitForTimeout(1000);
  await page.click('li.gwt-MenuItem[role=menuitem]:has-text("Kalkylblad")'); await page.waitForTimeout(1800);
}
// Kalkylbladet ritas på en canvas: kolumn A börjar vid x = 52, bredd 70; rad 1 vid y = 79, höjd 25.
const cell = (col, row) => ({ x: 52 + 70 * (col.charCodeAt(0) - 65), y: 79 + 25 * (row - 1), w: 70, h: 25 });

async function skrivData(page, x, y) {
  await page.evaluate(({ x, y }) => { x.forEach((v, i) => api.evalCommand(`A${i + 1}=${v}`)); y.forEach((v, i) => api.evalCommand(`B${i + 1}=${v}`)); }, { x, y });
  await page.waitForTimeout(800);
  const got = await page.evaluate(({ n }) => Array.from({ length: n }, (_, k) => [api.getValue(`A${k + 1}`), api.getValue(`B${k + 1}`)]), { n: x.length });
  got.forEach(([a, b], k) => { if (Math.abs(a - x[k]) > 1e-9 || Math.abs(b - y[k]) > 1e-9) throw new Error(`fel inmatning rad ${k + 1}`); });
  const a1 = cell('A', 1), bn = cell('B', x.length);
  await page.mouse.move(a1.x + 35, a1.y + 12); await page.mouse.down();
  await page.mouse.move(bn.x + 35, bn.y + 12, { steps: 10 }); await page.mouse.up();
  await page.waitForTimeout(500);
  return { x: a1.x, y: a1.y, w: 140, h: 25 * x.length };
}

async function oppnaTvavariabel(page) {
  await page.locator('.toolbar_item').nth(1).click(); await page.waitForTimeout(900);
  const b = await page.locator('li[mode="2021"]').boundingBox();
  await page.mouse.move(b.x + 60, b.y + b.height / 2); await page.mouse.down(); await page.mouse.up();
  await page.waitForTimeout(2500);
}

async function shared(browser, ut) {
  const page = await newApp(browser);
  try {
    await kalkylblad(page);
    await skrivData(page, [1, 2, 3], [2, 4, 5]);
    await page.locator('.toolbar_item').nth(1).click(); await page.waitForTimeout(900);
    const btn = await box(page, '.toolbar_item', 1), item = await box(page, 'li[mode="2021"]');
    await annotate(page, [{ ...btn, n: 1, pad: 2, side: 'right', dx: -4, dy: -18 }, { ...item, n: 2, pad: 0, side: 'right' }]);
    await shoot(page, path.join(ut, 'geogebra-tvavariabel-meny.png'), { x: 0, y: 0, w: 470, h: 230 });
  } finally { await page.close(); }
}

async function job(browser, ut, j, logg) {
  const page = await newApp(browser);
  try {
    await kalkylblad(page);
    const cells = await skrivData(page, j.x, j.y);
    const btn = await box(page, '.toolbar_item', 1);
    await annotate(page, [{ ...cells, n: 1, label: `A1–B${j.x.length} markerade`, side: 'right' }, { ...btn, n: 2, label: 'Klicka här', side: 'right', pad: 2 }]);
    await shoot(page, path.join(ut, `geogebra-${j.slug}-data.png`), { x: 0, y: 0, w: 380, h: Math.min(VIEW.height, cells.y + cells.h + 34) });
    await clearAnn(page);

    await oppnaTvavariabel(page);
    // Listan Regressionsmodell är den som har valet Ingen (index ändras när Σx-panelen öppnas).
    const modellIndex = () => page.evaluate(() => [...document.querySelectorAll('select.gwt-ListBox')].filter((s) => s.offsetParent).findIndex((s) => [...s.options].some((o) => o.text === 'Ingen')));
    await page.locator('select.gwt-ListBox').nth(await modellIndex()).selectOption({ label: j.modell || 'Linjär' });
    await page.waitForTimeout(1200);
    if (j.grad) { await page.locator('select.gwt-ListBox').nth(2).selectOption({ label: String(j.grad) }); await page.waitForTimeout(1000); }
    await page.locator('button.ToggleButton').first().click();
    await page.waitForTimeout(1500);
    // Panelens värden och ekvationen (ekvationen ritas som bild; läs den med GeoGebra-kommandon).
    const vals = await page.evaluate(() => { const out = {}; for (const tr of document.querySelectorAll('tr')) { const td = [...tr.querySelectorAll('td')].filter((t) => t.offsetParent); if (td.length === 2) out[td[0].textContent.trim()] = td[1].textContent.trim(); } return out; });
    const selB = await box(page, 'select.gwt-ListBox', await modellIndex());
    const sigma = await box(page, 'button.ToggleButton', 0);
    const eq = { x: selB.x + selB.w + 6, y: selB.y - 19, w: j.ekvBredd || 240, h: 24 };
    const rRow = await page.evaluate(() => { const t = [...document.querySelectorAll('td')].find((x) => x.offsetParent && x.textContent.trim() === 'r'); if (!t) return null; const a = t.getBoundingClientRect(), b = t.nextElementSibling.getBoundingClientRect(); return { x: a.x, y: a.y, w: b.x + b.width - a.x, h: a.height }; });
    const items = [{ ...selB, n: 1, label: 'Regressionsmodell', side: 'below', pad: 2 }, { ...eq, n: 2, label: 'Modellens ekvation', side: 'right', pad: 3 }, { ...sigma, n: 3, label: 'Klicka på Σx', side: 'left', pad: 2 }];
    if (j.r && rRow) items.push({ ...rRow, n: 4, label: 'r', side: 'right', pad: 1, dx: 4 });
    await annotate(page, items);
    await shoot(page, path.join(ut, `geogebra-${j.slug}-regression.png`), { x: 200, y: 50, w: 900, h: 600 });
    // Förstorade utsnitt som går att läsa på mobil: modellen med ekvationen och statistikpanelen med r.
    await shoot(page, path.join(ut, `geogebra-${j.slug}-ekvation.png`),
      { x: selB.x - 8, y: selB.y - 48, w: Math.min(VIEW.width - selB.x + 8, eq.x + eq.w + 200 - selB.x), h: selB.h + 92 });
    if (j.r && rRow) await shoot(page, path.join(ut, `geogebra-${j.slug}-r.png`), { x: rRow.x - 6, y: Math.max(52, rRow.y - 150), w: rRow.w + 110, h: 230 });
    await clearAnn(page);
    // Kontroll: samma linjära modell med GeoGebras kommando AnpassaLinje (FitLine), oberoende av visningen.
    const fit = await page.evaluate(({ x, y }) => { api.evalCommand(`kontrollLinje=FitLine({${x.map((v, i) => `(${v},${y[i]})`).join(',')}})`); const v = api.getValueString('kontrollLinje'); api.deleteObject('kontrollLinje'); return v; }, { x: j.x, y: j.y });
    logg[j.slug] = { x: j.x, y: j.y, modell: j.modell || 'Linjär', panel: vals, anpassaLinje: fit };
    if (j.berakna !== undefined) {
      const inp = await page.evaluate(() => { const l = [...document.querySelectorAll('input')].filter((e) => e.offsetParent && e.getBoundingClientRect().y > 560); const e = l[0]; if (!e) return null; const r = e.getBoundingClientRect(); return { x: r.x, y: r.y, w: r.width, h: r.height }; });
      await page.mouse.click(inp.x + inp.w / 2, inp.y + inp.h / 2);
      await page.keyboard.type(String(j.berakna), { delay: 40 });
      await page.keyboard.press('Enter');
      await page.waitForTimeout(1200);
      const yv = await page.evaluate(() => [...document.querySelectorAll('input')].filter((e) => e.offsetParent && e.getBoundingClientRect().y > 560).map((e) => e.value));
      logg[j.slug].berakna = { x: j.berakna, falt: yv };
      const res = { x: inp.x - 70, y: inp.y - 4, w: inp.w + 260, h: inp.h + 8 };
      await annotate(page, [{ ...res, n: 5, label: `x = ${j.berakna}`, side: 'above', pad: 2 }]);
      await shoot(page, path.join(ut, `geogebra-${j.slug}-berakna.png`), { x: 200, y: 330, w: 640, h: 320 });
      await clearAnn(page);
    }
    console.log('ok', j.slug, JSON.stringify(logg[j.slug]));
  } finally { await page.close(); }
}

(async () => {
  const [specFile, ut, ...only] = process.argv.slice(2);
  const spec = JSON.parse(fs.readFileSync(specFile, 'utf8'));
  fs.mkdirSync(ut, { recursive: true });
  const loggFil = path.join(ut, 'geogebra-regression-logg.json');
  const logg = fs.existsSync(loggFil) ? JSON.parse(fs.readFileSync(loggFil, 'utf8')) : {};
  const browser = await chromium.launch();
  let fel = 0;
  try {
    if (!only.length || only.includes('shared')) await shared(browser, ut);
    for (const j of spec.jobs.filter((j) => !only.length || only.includes(j.slug))) {
      let klar = false;
      for (let f = 1; f <= 3 && !klar; f++) {
        try {
          // Ett jobb som hänger (t.ex. en sida som slutar svara) avbryts efter 4 minuter.
          await Promise.race([job(browser, ut, j, logg), new Promise((_, nej) => setTimeout(() => nej(new Error('tidsgräns')), 240000))]);
          klar = true;
        } catch (e) { console.error('försök', f, j.slug, e.message); }
      }
      if (!klar) { fel++; console.error('FEL', j.slug); }
    }
  } finally { fs.writeFileSync(loggFil, JSON.stringify(logg, null, 1)); await browser.close(); }
  process.exit(fel ? 1 : 0);
})();
