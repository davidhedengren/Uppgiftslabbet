#!/usr/bin/env node
'use strict';
/*
 * Kör Kunskapsgymmets riktiga rättning lokalt på uppgifter i en bank, utan konto och utan Supabase.
 * För varje uppgift och varje delkort (expandGameTask) körs den inbyggda facitkontrollen kvFacit,
 * och därefter elevsvar som ska godtas respektive underkännas.
 *
 *   KG=../kunskapsgymmet DEPS=<mapp med katex/package och nerdamer/package> \
 *   node tools/kg-sjalvrattning-kontroll.cjs <kurs> <bankfil> <varianter.json> [id ...]
 *
 * varianter.json: { "<kort-id>": { "ratt": ["..."], "fel": ["..."] } }, där kort-id är
 * uppgiftens id (1.1010) eller delkortets id (1.1010a). Gäller kort med ett svarsfält.
 */
const fs = require('fs');
const path = require('path');
const { chromium } = require('playwright');

const [kurs, bankfil, variantfil, ...ids] = process.argv.slice(2);
const KG = path.resolve(process.env.KG || path.join(__dirname, '..', '..', 'kunskapsgymmet'));
const DEPS = path.resolve(process.env.DEPS);
const varianter = variantfil && fs.existsSync(variantfil) ? JSON.parse(fs.readFileSync(variantfil, 'utf8')) : {};
const typer = { '.html': 'text/html', '.js': 'text/javascript', '.css': 'text/css', '.png': 'image/png', '.svg': 'image/svg+xml', '.json': 'application/json', '.woff2': 'font/woff2' };

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage();
  const fel = [];
  page.on('pageerror', (e) => fel.push('sidfel: ' + e.message));
  await page.route('**/*', (r) => {
    const u = new URL(r.request().url());
    if (u.hostname.endsWith('supabase.co')) return r.abort();
    if (u.hostname === 'fonts.googleapis.com' || u.hostname === 'fonts.gstatic.com') return r.fulfill({ body: '' });
    const m = u.hostname === 'cdn.jsdelivr.net' && u.pathname.match(/^\/npm\/(katex|nerdamer)@[^/]+\/(.+)$/);
    if (m) return r.fulfill({ path: path.join(DEPS, m[1], 'package', m[2]) });
    if (u.hostname === 'kg.lokal') {
      const fil = u.pathname === '/' ? 'index.html' : decodeURIComponent(u.pathname.slice(1));
      const full = path.basename(fil) === path.basename(bankfil) ? path.resolve(bankfil) : path.join(KG, fil);
      if (fs.existsSync(full)) return r.fulfill({ path: full, contentType: typer[path.extname(full)] || 'application/octet-stream' });
      return r.fulfill({ status: 404, body: '' });
    }
    return r.abort();
  });
  await page.goto('http://kg.lokal/');
  await page.waitForFunction(() => typeof selectCourse === 'function' && typeof nerdamer === 'function', null, { timeout: 60000 });
  const ok = await page.evaluate((k) => selectCourse(k, { record: false, render: false }), kurs);
  if (!ok) throw new Error('kursen laddades inte');
  const res = await page.evaluate(({ ids, varianter }) => {
    const ut = [];
    const bank = state.data.bank;
    const valda = ids.length ? ids.map((id) => bank.find((q) => q.id === id)) : bank;
    for (const q of valda) {
      if (!q) { ut.push({ id: '?', fel: ['uppgiften saknas'] }); continue; }
      const kort = [q, ...(q.spelDelning === 'deluppgifter' ? expandGameTask(q).filter((x) => x !== q) : [])];
      for (const c of kort) {
        const f = [];
        try { f.push(...kvFacit(c)); } catch (e) { f.push('kvFacit kastade: ' + e.message); }
        const v = varianter[c.id];
        if (v) {
          const prov = (anv) => delSvarRatt(anv, c.rättSvar, c.svarEnhet, c.tolerans, c, 0, c.svarFormat);
          for (const a of v.ratt || []) { let r; try { r = prov(a); } catch (e) { r = 'fel: ' + e.message; } if (r !== true) f.push(`godtas inte: "${a}"`); }
          for (const a of v.fel || []) { let r; try { r = prov(a); } catch (e) { r = false; } if (r === true) f.push(`godtas felaktigt: "${a}"`); }
        }
        ut.push({ id: c.id, fel: f });
      }
    }
    return ut;
  }, { ids, varianter });
  await browser.close();
  const medFel = res.filter((r) => r.fel.length);
  for (const r of medFel) console.log(r.id, '\n  ' + r.fel.join('\n  '));
  console.log(JSON.stringify({ kort: res.length, medFel: medFel.length, sidfel: fel }));
  process.exit(medFel.length || fel.length ? 1 : 0);
})();
