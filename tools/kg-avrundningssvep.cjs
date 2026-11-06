#!/usr/bin/env node
'use strict';
/*
 * Svep efter ett av felloggens vanligaste mönster: ett korrekt avrundat talsvar, eller samma tal med
 * enhet, underkänns av Kunskapsgymmets rättning. Kör den riktiga rättningen (delSvarRatt) lokalt för
 * varje kort med ett talsvar, i alla kurser, utan Supabase.
 *
 *   KG=../kunskapsgymmet DEPS=<mapp med katex/ och nerdamer/> node tools/kg-avrundningssvep.cjs [kurs ...] > ut.json
 *
 * Prov som ska godtas:
 *   - facit med svarets enhet efter ("320,3 g"),
 *   - facit avrundat till frågans antal decimaler eller värdesiffror,
 *   - facit med fler decimaler än frågan kräver (inte när frågan kräver exakt form).
 * Prov som ska underkännas: facit · 1,1 (för generös tolerans).
 * Utskriften är en lista med fynd. Den ersätter inte bedömningen av varje uppgift.
 */
const fs = require('fs');
const path = require('path');
const { chromium } = require('playwright');

const KG = path.resolve(process.env.KG || path.join(__dirname, '..', '..', 'kunskapsgymmet'));
const DEPS = path.resolve(process.env.DEPS);
const KURSER = process.argv.slice(2).length ? process.argv.slice(2) : ['fy1', 'fy2', 'ma1', 'ma2', 'mato1', 'mato2', 'matf1'];
const typer = { '.html': 'text/html', '.js': 'text/javascript', '.css': 'text/css', '.png': 'image/png', '.svg': 'image/svg+xml', '.json': 'application/json' };

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
      if (fs.existsSync(full)) return r.fulfill({ path: full, contentType: typer[path.extname(full)] || 'application/octet-stream' });
      return r.fulfill({ status: 404, body: '' });
    }
    if (u.hostname.startsWith('fonts.')) return r.fulfill({ body: '' });
    return r.abort();
  });
  await page.goto('http://kg.lokal/');
  await page.waitForFunction(() => typeof selectCourse === 'function' && typeof nerdamer === 'function', null, { timeout: 60000 });
  const alla = [];
  for (const kurs of KURSER) {
    const ok = await page.evaluate((k) => selectCourse(k, { record: false, render: false }), kurs);
    if (!ok) { console.error('kursen laddades inte', kurs); continue; }
    const res = await page.evaluate((kurs) => {
      const ORD = { en: 1, ett: 1, två: 2, tre: 3, fyra: 4, fem: 5, sex: 6, sju: 7 };
      const text = (c) => String(c.t || '').replace(/<svg[\s\S]*?<\/svg>/g, ' ').replace(/<[^>]+>/g, ' ').replace(/\s+/g, ' ');
      const komma = (s) => String(s).replace('.', ',');
      const ut = [];
      let antal = 0;
      for (const q of state.data.bank) {
        if (q.spel === false || q.självrättning === false) continue;
        const kort = q.spelDelning === 'deluppgifter' ? [q, ...expandGameTask(q).filter((x) => x !== q)] : [q];
        for (const c of kort) {
          const R = c.rättSvar;
          const fmt = Array.isArray(c.svarFormat) ? null : c.svarFormat;
          if (typeof R !== 'number' || !Number.isFinite(R) || Array.isArray(c.svarFormat)) continue;
          if (fmt && !/numer/i.test(fmt)) continue;
          if (c.alternativ || c.alt) continue;
          const tx = text(c);
          const exakt = /exakt|utan avrundning|bråkform|enklaste form|som ett bråk|grundpotensform|tiopotens|uttryck/i.test(tx);
          const enhet = typeof c.svarEnhet === 'string' && c.svarEnhet.trim() && !/^(st|stycken)$/i.test(c.svarEnhet.trim()) ? c.svarEnhet.trim() : null;
          const prov = (a) => { try { return delSvarRatt(a, R, c.svarEnhet, c.tolerans, c, 0, c.svarFormat) === true; } catch (e) { return 'kastade'; } };
          antal++;
          const godtas = [], avvisas = [];
          const ORD2 = { sex: 6, sju: 7 };
          const md0 = /avrundas till/i.test(tx) ? null : tx.match(/(?:svara|avrunda|ange|med|till)\b[^.?]{0,30}?\b(en|ett|två|tre|fyra|fem|sex|sju|[1-9])\s+decimal(?!tal)/i);
          const md = md0 && { 1: md0[1] }; if (md && ORD2[md[1].toLowerCase()]) md[1] = String(ORD2[md[1].toLowerCase()]);
          const mv = tx.match(/(en|två|tre|fyra|fem|[1-5])\s+värdesiffr/i);
          const heltal = /(avrunda|svara)[^.?]{0,40}(till\s+)?(närmaste\s+)?heltal|hela\s+(procent|kronor|grader|sekunder|meter|kvadratmeter|minuter|cm|mm)/i.test(tx);
          // Med svarVardesiffror rättas antalet värdesiffror: provet använder då facit avrundat till dem.
          const vsn = Array.isArray(c.svarVardesiffror) ? c.svarVardesiffror[0] : c.svarVardesiffror;
          const bas = vsn != null && R !== 0 ? komma(String(Number(R.toPrecision(vsn)))) : komma(R);
          if (enhet) godtas.push(['enhet', `${bas} ${enhet}`]);
          if (md) { const d = ORD[md[1].toLowerCase()] || +md[1]; godtas.push(['decimaler', komma(R.toFixed(d))]); if (enhet) godtas.push(['decimaler+enhet', `${komma(R.toFixed(d))} ${enhet}`]); }
          else if (mv && !(c.svarVardesiffror != null)) {
            const n = ORD[mv[1].toLowerCase()] || +mv[1]; const v = Number(R.toPrecision(n));
            if (Math.abs(v) >= 1e-3 && Math.abs(v) < 1e6) godtas.push(['värdesiffror', komma(String(v))]);
          } else if (heltal) godtas.push(['heltal', komma(String(Math.round(R)))]);
          if (!exakt && vsn == null && !Number.isInteger(R) && !md && !mv && !heltal) {
            // Utan angiven precision: tre värdesiffror när facit har fler.
            const v = Number(R.toPrecision(3));
            if (v !== R && Math.abs(R) >= 0.01) godtas.push(['tre värdesiffror (utan angiven precision)', komma(String(v))]);
          }
          if (Math.abs(R) > 1e-9) avvisas.push(['facit·1,1', komma(String(Number((R * 1.1).toPrecision(6))))]);
          const f = [];
          for (const [typ, a] of godtas) { const r = prov(a); if (r !== true) f.push({ typ, svar: a, utfall: r === 'kastade' ? 'kastade' : 'underkänt' }); }
          for (const [typ, a] of avvisas) { if (prov(a) === true) f.push({ typ, svar: a, utfall: 'godtas felaktigt' }); }
          if (f.length) ut.push({ kurs, id: c.id, R, tol: c.tolerans, enhet: c.svarEnhet || null, fmt: fmt || null, vs: c.svarVardesiffror ?? null, text: tx.slice(-260), fynd: f });
        }
      }
      return { antal, ut };
    }, kurs);
    console.error(kurs, 'kort med talsvar', res.antal, 'fynd', res.ut.length);
    alla.push(...res.ut);
  }
  await browser.close();
  process.stdout.write(JSON.stringify({ sidfel, fynd: alla }, null, 1));
})();
