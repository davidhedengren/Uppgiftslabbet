#!/usr/bin/env node
'use strict';
/* Kör Kunskapsgymmets inbyggda självtester (window.KG_TEST_*) lokalt, utan Supabase.
   KG=../kunskapsgymmet DEPS=<katex/nerdamer-paket> node tools/kg-sjalvtester.cjs */
const fs = require('fs');
const path = require('path');
const { chromium } = require('playwright');
const KG = path.resolve(process.env.KG || path.join(__dirname, '..', '..', 'kunskapsgymmet'));
const DEPS = path.resolve(process.env.DEPS);
(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage();
  const sidfel = [];
  page.on('pageerror', (e) => sidfel.push(e.message));
  await page.route('**/*', (r) => {
    const u = new URL(r.request().url());
    const m = u.hostname === 'cdn.jsdelivr.net' && u.pathname.match(/^\/npm\/(katex|nerdamer)@[^/]+\/(.+)$/);
    if (m) return r.fulfill({ path: path.join(DEPS, m[1], 'package', m[2]) });
    if (u.hostname === 'kg.lokal') {
      const full = path.join(KG, u.pathname === '/' ? 'index.html' : decodeURIComponent(u.pathname.slice(1)));
      if (fs.existsSync(full)) return r.fulfill({ path: full, contentType: full.endsWith('.html') ? 'text/html' : 'text/javascript' });
      return r.fulfill({ status: 404, body: '' });
    }
    if (u.hostname.startsWith('fonts.')) return r.fulfill({ body: '' });
    return r.abort();
  });
  await page.goto('http://kg.lokal/');
  await page.waitForFunction(() => typeof formatRatt === 'function' && typeof nerdamer === 'function', null, { timeout: 60000 });
  const res = await page.evaluate(() => {
    const ut = {};
    for (const k of Object.keys(window).filter((k) => /^KG_TEST_/.test(k) && typeof window[k] === 'function')) {
      const orig = console.table;
      let tabell = null;
      console.table = (t) => { tabell = t; };
      try { ut[k] = { ok: window[k](), fel: (tabell || []).filter((r) => r.ok === false).map((r) => JSON.stringify(r).slice(0, 200)) }; }
      catch (e) { ut[k] = { ok: false, fel: ['kastade: ' + e.message] }; }
      console.table = orig;
    }
    return ut;
  });
  await browser.close();
  for (const [k, v] of Object.entries(res)) console.log(v.ok ? 'ok ' : 'FEL', k, v.fel.join(' | '));
  if (sidfel.length) console.log('sidfel', sidfel);
  process.exit(Object.values(res).every((v) => v.ok) ? 0 : 1);
})();
