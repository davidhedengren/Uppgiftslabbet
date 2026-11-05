'use strict';
/* Minimal ersättning för den del av Playwright som tools/geogebra-skarmbilder.js använder,
   byggd direkt på Chrome DevTools Protocol (Node 22+, inbyggd WebSocket och fetch).
   Används när Playwright och GeoGebra-paketet saknas: då körs riktiga GeoGebra Classic
   från geogebra.org/classic (svenska) i en dold Chrome. Se agent/MA2_STATISTIK_GEOGEBRA_SKARMBILDER_2026-11-05.md. */
const {spawn} = require('node:child_process');
const os = require('node:os'), path = require('node:path');
const CHROME = process.env.CHROME || 'C:/Program Files/Google/Chrome/Application/chrome.exe';
const vila = (ms) => new Promise((r) => setTimeout(r, ms));

async function anslut(wsUrl) {
  const ws = new WebSocket(wsUrl);
  await new Promise((ok, fel) => { ws.onopen = ok; ws.onerror = fel; });
  let nr = 0; const vantar = new Map();
  ws.onmessage = (e) => { const m = JSON.parse(e.data); if (m.id && vantar.has(m.id)) { const {ok, fel} = vantar.get(m.id); vantar.delete(m.id); m.error ? fel(new Error(JSON.stringify(m.error))) : ok(m.result); } };
  const send = (method, params = {}) => new Promise((ok, fel) => { const id = ++nr; vantar.set(id, {ok, fel}); ws.send(JSON.stringify({id, method, params})); });
  return {ws, send};
}

// Väljare: CSS, eventuellt med Playwrights :has-text("…") sist. Bara synliga element räknas.
function hittaUttryck(sel) {
  const m = sel.match(/^(.*?):has-text\("(.*)"\)$/);
  const css = m ? m[1] : sel, text = m ? m[2] : null;
  return `[...document.querySelectorAll(${JSON.stringify(css)})].filter(e=>{const r=e.getBoundingClientRect();return r.width>0&&r.height>0&&getComputedStyle(e).visibility!=='hidden'${text ? `&&e.textContent.includes(${JSON.stringify(text)})` : ''};})`;
}

function skapaSida(send, opts) {
  let musX = 0, musY = 0, nere = false;
  const evaluate = async (fn, arg) => {
    const expr = typeof fn === 'function' ? `(${fn.toString()})(${arg === undefined ? '' : JSON.stringify(arg)})` : fn;
    const r = await send('Runtime.evaluate', {expression: expr, awaitPromise: true, returnByValue: true});
    if (r.exceptionDetails) throw new Error(r.exceptionDetails.exception?.description || r.exceptionDetails.text);
    return r.result.value;
  };
  const mus = (type, extra = {}) => send('Input.dispatchMouseEvent', {type, x: musX, y: musY, button: 'left', clickCount: 1, buttons: nere ? 1 : 0, ...extra});
  const mouse = {
    async move(x, y, o = {}) { const steg = o.steps || 1, x0 = musX, y0 = musY; for (let i = 1; i <= steg; i++) { musX = x0 + (x - x0) * i / steg; musY = y0 + (y - y0) * i / steg; await mus('mouseMoved'); } },
    async down() { nere = true; await mus('mousePressed'); },
    async up() { nere = false; await mus('mouseReleased'); },
    async click(x, y) { await mouse.move(x, y); await mouse.down(); await mouse.up(); await vila(120); },
  };
  const keyboard = {
    async type(text, o = {}) { for (const ch of String(text)) { await send('Input.dispatchKeyEvent', {type: 'keyDown', key: ch, text: ch, unmodifiedText: ch}); await send('Input.dispatchKeyEvent', {type: 'keyUp', key: ch}); if (o.delay) await vila(o.delay); } },
    async press(key) {
      const K = {Enter: {key: 'Enter', code: 'Enter', windowsVirtualKeyCode: 13, text: '\r'}, Escape: {key: 'Escape', code: 'Escape', windowsVirtualKeyCode: 27}}[key];
      if (!K) throw new Error('Okänd tangent ' + key);
      await send('Input.dispatchKeyEvent', {type: 'keyDown', ...K}); await send('Input.dispatchKeyEvent', {type: 'keyUp', ...K, text: undefined});
    },
  };
  const waitForFunction = async (fn, arg, o = {}) => { const slut = Date.now() + (o.timeout || 30000); for (;;) { if (await evaluate(fn, arg)) return true; if (Date.now() > slut) throw new Error('Tidsgräns för waitForFunction'); await vila(200); } };
  const rektAv = async (sel, val) => evaluate(`(()=>{const l=${hittaUttryck(sel)};const e=${val === 'last' ? 'l[l.length-1]' : `l[${val}]`};if(!e)return null;e.scrollIntoViewIfNeeded&&e.scrollIntoViewIfNeeded();const r=e.getBoundingClientRect();return {x:r.x,y:r.y,width:r.width,height:r.height};})()`);
  const vanta = async (sel, val, timeout = 15000) => { const slut = Date.now() + timeout; for (;;) { const r = await rektAv(sel, val); if (r) return r; if (Date.now() > slut) throw new Error('Hittade inte ' + sel); await vila(200); } };
  const locator = (sel, val = 0) => ({
    first: () => locator(sel, 0), last: () => locator(sel, 'last'), nth: (i) => locator(sel, i),
    async boundingBox() { return vanta(sel, val); },
    async click() { const r = await vanta(sel, val); await mouse.click(r.x + r.width / 2, r.y + r.height / 2); },
    async selectOption({label}) {
      await vanta(sel, val);
      const ok = await evaluate(`(()=>{const l=${hittaUttryck(sel)};const s=${val === 'last' ? 'l[l.length-1]' : `l[${val}]`};const o=[...s.options].find(o=>o.text.trim()===${JSON.stringify(label)});if(!o)return false;s.value=o.value;s.selectedIndex=o.index;s.dispatchEvent(new Event('change',{bubbles:true}));return true;})()`);
      if (!ok) throw new Error('Saknar alternativet ' + label);
    },
  });
  return {
    evaluate, mouse, keyboard, waitForFunction, locator,
    waitForTimeout: vila,
    async goto(url) { await send('Page.navigate', {url}); await vila(1500); },
    async click(sel) { await locator(sel).click(); },
    async waitForSelector(sel, o = {}) { await vanta(sel, 0, o.timeout); },
    async screenshot({path: fil, clip}) {
      const r = await send('Page.captureScreenshot', {format: 'png', clip: {x: clip.x, y: clip.y, width: clip.width, height: clip.height, scale: 1}});
      require('node:fs').writeFileSync(fil, Buffer.from(r.data, 'base64'));
    },
    opts,
  };
}

const chromium = {
  async launch() {
    const port = Number(process.env.GG_PORT || 9370);
    const profil = path.join(os.tmpdir(), 'gg-pw-profil-' + port);
    const proc = spawn(CHROME, ['--headless=new', `--remote-debugging-port=${port}`, `--user-data-dir=${profil}`, '--lang=sv',
      '--no-first-run', '--no-default-browser-check', '--disable-extensions', '--disable-background-timer-throttling',
      '--disable-renderer-backgrounding', '--disable-backgrounding-occluded-windows', 'about:blank'], {stdio: 'ignore'});
    const bas = `http://127.0.0.1:${port}`;
    for (let i = 0; i < 240; i++) { try { await (await fetch(bas + '/json/version')).json(); break; } catch (_) { await vila(250); } }
    const sidor = [];
    return {
      async newPage({viewport, deviceScaleFactor}) {
        const t = await (await fetch(bas + '/json/new?about:blank', {method: 'PUT'})).json();
        const {ws, send} = await anslut(t.webSocketDebuggerUrl);
        await send('Page.enable'); await send('Runtime.enable');
        await send('Emulation.setDeviceMetricsOverride', {width: viewport.width, height: viewport.height, deviceScaleFactor, mobile: false});
        await send('Emulation.setFocusEmulationEnabled', {enabled: true}).catch(() => {});
        const sida = skapaSida(send, {viewport});
        sida.close = async () => { try { ws.close(); await fetch(bas + '/json/close/' + t.id); } catch (_) {} };
        sidor.push(sida);
        return sida;
      },
      async close() { for (const s of sidor) await s.close(); proc.kill(); await vila(300); },
    };
  },
};

module.exports = {chromium};
