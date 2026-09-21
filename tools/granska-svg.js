#!/usr/bin/env node
'use strict';

const fs = require('node:fs');
const path = require('node:path');
const os = require('node:os');
const vm = require('node:vm');
const crypto = require('node:crypto');
const { spawnSync } = require('node:child_process');
const { pathToFileURL } = require('node:url');

const VERSION = '1.1.0';
const DEFAULT_CHROME = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe';
const BANKS = [
  ['uppgifter.js', 'BANK', 'Fysik - nivå 1'],
  ['uppgifter2.js', 'BANK2', 'Fysik - nivå 2'],
  ['uppgifterma1.js', 'BANKMA1', 'Matematik - nivå 1'],
  ['uppgifterma2.js', 'BANKMA2', 'Matematik - nivå 2'],
  ['uppgiftermatf1.js', 'BANKMATF1', 'Matematik fördjupning - nivå 1'],
  ['uppgiftermato1.js', 'BANKMATO1', 'Matematik fortsättning - nivå 1'],
  ['uppgiftermato2.js', 'BANKMATO2', 'Matematik fortsättning - nivå 2']
];

const CONFIG = Object.freeze({
  collisionPadding: 0.75,
  proximityPadding: 2.0,
  outsideTolerance: 0.25,
  angleEndpointToleranceRatio: 0.045,
  angleCenterSpreadRatio: 0.05,
  degreeLabelDistanceFactor: 2.35,
  batchSize: 55,
  maxBatchCharacters: 4500000
});

function escHtml(value) {
  return String(value).replace(/[&<>"']/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));
}

function round(n, places = 2) {
  return Number.isFinite(n) ? Number(n.toFixed(places)) : null;
}

function distance(a, b) {
  return Math.hypot(a.x - b.x, a.y - b.y);
}

function bboxDistance(a, b) {
  const dx = Math.max(a.x - (b.x + b.width), b.x - (a.x + a.width), 0);
  const dy = Math.max(a.y - (b.y + b.height), b.y - (a.y + a.height), 0);
  return Math.hypot(dx, dy);
}

function bboxIntersects(a, b, padding = 0) {
  return a.x <= b.x + b.width + padding && a.x + a.width >= b.x - padding &&
    a.y <= b.y + b.height + padding && a.y + a.height >= b.y - padding;
}

function pointInBbox(p, b, padding = 0) {
  return p.x >= b.x - padding && p.x <= b.x + b.width + padding && p.y >= b.y - padding && p.y <= b.y + b.height + padding;
}

function pointToBboxDistance(p, b) {
  const dx = Math.max(b.x - p.x, p.x - (b.x + b.width), 0);
  const dy = Math.max(b.y - p.y, p.y - (b.y + b.height), 0);
  return Math.hypot(dx, dy);
}

function pointToSegmentDistance(p, a, b) {
  const vx = b.x - a.x, vy = b.y - a.y;
  const length2 = vx * vx + vy * vy;
  if (!length2) return distance(p, a);
  const t = Math.max(0, Math.min(1, ((p.x - a.x) * vx + (p.y - a.y) * vy) / length2));
  return distance(p, { x: a.x + t * vx, y: a.y + t * vy });
}

function segmentIntersectsBbox(a, b, box, padding = 0) {
  const left = box.x - padding, right = box.x + box.width + padding;
  const top = box.y - padding, bottom = box.y + box.height + padding;
  let t0 = 0, t1 = 1;
  const dx = b.x - a.x, dy = b.y - a.y;
  for (const [p, q] of [[-dx, a.x - left], [dx, right - a.x], [-dy, a.y - top], [dy, bottom - a.y]]) {
    if (p === 0) {
      if (q < 0) return false;
    } else {
      const r = q / p;
      if (p < 0) t0 = Math.max(t0, r); else t1 = Math.min(t1, r);
      if (t0 > t1) return false;
    }
  }
  return true;
}

function segmentToBboxDistance(a, b, box) {
  if (segmentIntersectsBbox(a, b, box)) return 0;
  const corners = [
    { x: box.x, y: box.y }, { x: box.x + box.width, y: box.y },
    { x: box.x + box.width, y: box.y + box.height }, { x: box.x, y: box.y + box.height }
  ];
  return Math.min(pointToBboxDistance(a, box), pointToBboxDistance(b, box), ...corners.map((p) => pointToSegmentDistance(p, a, b)));
}

function bboxCenter(b) {
  return { x: b.x + b.width / 2, y: b.y + b.height / 2 };
}

function validBbox(b) {
  return b && [b.x, b.y, b.width, b.height].every(Number.isFinite);
}

function finding(severity, code, reason, elements = [], details = {}) {
  return { severity, code, reason, elements, ...details };
}

function parseViewBox(svg) {
  const match = svg.match(/\bviewBox\s*=\s*["']\s*([-+\d.eE]+)[ ,]+([-+\d.eE]+)[ ,]+([-+\d.eE]+)[ ,]+([-+\d.eE]+)/i);
  if (match) return { x: +match[1], y: +match[2], width: +match[3], height: +match[4] };
  const width = +(svg.match(/\bwidth\s*=\s*["']\s*([-+\d.eE]+)/i) || [0, 300])[1];
  const height = +(svg.match(/\bheight\s*=\s*["']\s*([-+\d.eE]+)/i) || [0, 150])[1];
  return { x: 0, y: 0, width, height };
}

function validSvgLength(raw) {
  return /^[-+]?(?:\d+(?:\.\d*)?|\.\d+)(?:e[-+]?\d+)?(?:%|em|ex|px|in|cm|mm|q|pt|pc)?$/i.test(raw);
}

const PATH_NUMBER = /[-+]?(?:\d+(?:\.\d*)?|\.\d+)(?:e[-+]?\d+)?/iy;

function validPathData(d) {
  let index = 0;
  const arity = { a: 7, c: 6, h: 1, l: 2, m: 2, q: 4, s: 4, t: 2, v: 1, z: 0 };

  const skipWhitespace = () => {
    while (index < d.length && /\s/.test(d[index])) index++;
  };
  const skipCommaWsp = () => {
    skipWhitespace();
    if (d[index] === ',') {
      index++;
      skipWhitespace();
      if (d[index] === ',') return false;
    }
    return true;
  };
  const readNumber = (firstAfterCommand = false) => {
    if (firstAfterCommand) skipWhitespace();
    else if (!skipCommaWsp()) return null;
    if (firstAfterCommand && d[index] === ',') return null;
    PATH_NUMBER.lastIndex = index;
    const match = PATH_NUMBER.exec(d);
    if (!match || match.index !== index) return null;
    index = PATH_NUMBER.lastIndex;
    return Number(match[0]);
  };
  const readArcFlag = () => {
    if (!skipCommaWsp()) return null;
    const flag = d[index];
    if (flag !== '0' && flag !== '1') return null;
    index++;
    return Number(flag);
  };
  const nextNonWhitespace = () => {
    let next = index;
    while (next < d.length && /\s/.test(d[next])) next++;
    return d[next] || '';
  };

  skipWhitespace();
  if (d[index] !== 'M' && d[index] !== 'm') return false;

  while (index < d.length) {
    skipWhitespace();
    const rawCommand = d[index];
    if (!/[AaCcHhLlMmQqSsTtVvZz]/.test(rawCommand || '')) return false;
    index++;
    const command = rawCommand.toLowerCase();
    const needed = arity[command];
    if (needed === 0) {
      if (nextNonWhitespace() && !/[AaCcHhLlMmQqSsTtVvZz]/.test(nextNonWhitespace())) return false;
      continue;
    }

    let groups = 0;
    while (index < d.length) {
      skipWhitespace();
      if (/[AaCcHhLlMmQqSsTtVvZz]/.test(d[index] || '')) break;
      const values = [];
      for (let parameter = 0; parameter < needed; parameter++) {
        const value = command === 'a' && (parameter === 3 || parameter === 4)
          ? readArcFlag()
          : readNumber(groups === 0 && parameter === 0);
        if (value === null) return false;
        values.push(value);
      }
      if (command === 'a' && (values[0] < 0 || values[1] < 0)) return false;
      groups++;
      const next = nextNonWhitespace();
      if (!next || /[AaCcHhLlMmQqSsTtVvZz]/.test(next)) break;
    }
    if (groups === 0) return false;
  }
  return true;
}

function invalidMarkupFindings(svg) {
  const out = [];
  const numericAttrs = /\b(cx|cy|r|rx|ry|x|y|x1|y1|x2|y2|width|height)\s*=\s*["']([^"']*)["']/gi;
  let match;
  while ((match = numericAttrs.exec(svg))) {
    const name = match[1].toLowerCase();
    const raw = match[2].trim();
    const n = parseFloat(raw);
    if (!raw || !validSvgLength(raw) || !Number.isFinite(n) || ((name === 'r' || name === 'rx' || name === 'ry') && n < 0) || ((name === 'width' || name === 'height') && n < 0)) {
      out.push(finding('ERROR', 'INVALID_GEOMETRY', `Ogiltigt geometrivärde ${name}="${raw}".`, [], { value: raw, attribute: name }));
    }
  }
  for (const p of svg.matchAll(/<path\b[^>]*\bd\s*=\s*["']([^"']*)["'][^>]*>/gi)) {
    const d = p[1].trim();
    if (!d || !validPathData(d)) {
      out.push(finding('ERROR', 'INVALID_GEOMETRY', 'Ogiltig eller uppenbart felaktig path-data.', [], { value: d.slice(0, 120) }));
    }
  }
  const vb = parseViewBox(svg);
  if (!(vb.width > 0 && vb.height > 0)) out.push(finding('ERROR', 'INVALID_GEOMETRY', 'viewBox måste ha positiv bredd och höjd.'));
  return out;
}

function makeBrowserHtml(figures) {
  const payload = JSON.stringify(figures.map((f, i) => ({ i, svg: f.svg }))).replace(/</g, '\\u003c');
  return `<!doctype html><meta charset="utf-8"><style>body{margin:0} .case{position:absolute;left:-10000px;top:0} svg{overflow:visible}</style><div id="cases"></div><pre id="result">pending</pre><script>
const input=${payload};
const NS='http://www.w3.org/2000/svg';
const ALLOWED_TAGS=new Set('svg g defs symbol use line path polyline polygon circle ellipse rect text tspan title desc clipPath mask marker pattern linearGradient radialGradient stop'.split(' '));
const DROP_SUBTREE=new Set(['script','foreignobject','iframe','object','embed','audio','video','canvas','style','a','image']);
const ALLOWED_ATTRS=new Set('id class viewBox preserveAspectRatio width height x y x1 y1 x2 y2 cx cy r rx ry d points transform text-anchor dominant-baseline font-size font-family font-weight fill fill-opacity fill-rule stroke stroke-width stroke-opacity stroke-linecap stroke-linejoin stroke-dasharray opacity display visibility vector-effect marker-start marker-mid marker-end clip-path mask patternUnits patternContentUnits gradientUnits gradientTransform offset stop-color stop-opacity href xlink:href'.toLowerCase().split(' '));
function safeUrlValue(name,value){const v=value.trim(),compact=v.replaceAll(' ','');if(name==='href'||name==='xlink:href')return v.startsWith('#');if(v.toLowerCase().includes('url('))return /^url\(#[A-Za-z_][A-Za-z0-9_:.-]*\)$/i.test(compact);return !/(?:javascript|data|file|https?):/i.test(v)}
function sanitizeSvg(markup){const refs=[];const doc=new DOMParser().parseFromString(markup,'image/svg+xml');if(doc.querySelector('parsererror')||!doc.documentElement||doc.documentElement.localName.toLowerCase()!=='svg')return{error:'SVG kunde inte parsas',svg:'',node:null,refs};function clean(el){const tag=el.localName.toLowerCase(),rawRef=el.getAttribute('href')||el.getAttribute('xlink:href');if(rawRef&&(!rawRef.startsWith('#')||tag==='image'))refs.push({tag,ref:rawRef,kind:'external'});if(DROP_SUBTREE.has(tag)||!ALLOWED_TAGS.has(tag)){el.remove();return}for(const attr of [...el.attributes]){const name=attr.name.toLowerCase(),value=attr.value;if(name.startsWith('on')||!ALLOWED_ATTRS.has(name)||!safeUrlValue(name,value)){if((name==='href'||name==='xlink:href')&&value&&!refs.some(r=>r.tag===tag&&r.ref===value))refs.push({tag,ref:value,kind:value.startsWith('#')?'internal':'external'});el.removeAttribute(attr.name)}}for(const child of [...el.children])clean(child)}clean(doc.documentElement);if(!doc.documentElement.isConnected)return{error:'SVG saknar tillåtet rotelement',svg:'',node:null,refs};for(const use of doc.querySelectorAll('use')){const ref=use.getAttribute('href')||use.getAttribute('xlink:href');if(ref&&ref.startsWith('#')&&!doc.getElementById(ref.slice(1)))refs.push({tag:'use',ref,kind:'unresolved'})}const text=new XMLSerializer().serializeToString(doc.documentElement);return{svg:text,node:doc.documentElement,refs}}
function finiteBox(b){return b&&[b.x,b.y,b.width,b.height].every(Number.isFinite)}
function rootPoint(svg,el,x,y){const p=svg.createSVGPoint();p.x=x;p.y=y;const m=el.getScreenCTM(),root=svg.getScreenCTM();if(!m||!root)return null;const viewport=p.matrixTransform(m),q=viewport.matrixTransform(root.inverse());return{x:q.x,y:q.y}}
function boxInRoot(svg,el){try{const b=el.getBBox();const pts=[[b.x,b.y],[b.x+b.width,b.y],[b.x+b.width,b.y+b.height],[b.x,b.y+b.height]].map(p=>rootPoint(svg,el,p[0],p[1])).filter(Boolean);if(!pts.length)return null;const xs=pts.map(p=>p.x),ys=pts.map(p=>p.y);return{x:Math.min(...xs),y:Math.min(...ys),width:Math.max(...xs)-Math.min(...xs),height:Math.max(...ys)-Math.min(...ys)}}catch(e){return null}}
function samples(svg,el,tag){const pts=[];try{if(tag==='line'){const x1=+el.getAttribute('x1')||0,y1=+el.getAttribute('y1')||0,x2=+el.getAttribute('x2')||0,y2=+el.getAttribute('y2')||0,count=Math.max(2,Math.min(80,Math.ceil(Math.hypot(x2-x1,y2-y1)/4)));for(let i=0;i<=count;i++)pts.push(rootPoint(svg,el,x1+(x2-x1)*i/count,y1+(y2-y1)*i/count))}else if(tag==='polyline'||tag==='polygon'){for(const p of el.points)pts.push(rootPoint(svg,el,p.x,p.y));if(tag==='polygon'&&pts.length)pts.push(pts[0])}else if(tag==='path'){const len=el.getTotalLength();const count=Math.max(8,Math.min(80,Math.ceil(len/4)));for(let i=0;i<=count;i++){const p=el.getPointAtLength(len*i/count);pts.push(rootPoint(svg,el,p.x,p.y))}}else if(tag==='circle'||tag==='ellipse'){const cx=+el.getAttribute('cx')||0,cy=+el.getAttribute('cy')||0,rx=tag==='circle'?(+el.getAttribute('r')||0):(+el.getAttribute('rx')||0),ry=tag==='circle'?rx:(+el.getAttribute('ry')||0);for(let i=0;i<24;i++){const a=2*Math.PI*i/24;pts.push(rootPoint(svg,el,cx+rx*Math.cos(a),cy+ry*Math.sin(a)))}}else if(tag==='rect'){const x=+el.getAttribute('x')||0,y=+el.getAttribute('y')||0,w=+el.getAttribute('width')||0,h=+el.getAttribute('height')||0;[[x,y],[x+w,y],[x+w,y+h],[x,y+h],[x,y]].forEach(p=>pts.push(rootPoint(svg,el,p[0],p[1])))}}catch(e){}return pts.filter(Boolean)}
function hiddenByTree(el,svg){for(let n=el;n&&n!==svg.parentElement;n=n.parentElement){const cs=getComputedStyle(n);if(cs.display==='none'||cs.visibility==='hidden'||Number(cs.opacity)===0)return true}return false}
function svgDomCopy(source){const copy=document.createElementNS(NS,source.localName);for(const attr of [...source.attributes])copy.setAttribute(attr.name,attr.value);for(const child of [...source.childNodes])copy.appendChild(child.nodeType===Node.ELEMENT_NODE?svgDomCopy(child):document.createTextNode(child.textContent||''));return copy}
function materializeUses(svg){const targets=new Map([...svg.querySelectorAll('[id]')].map(el=>[el.id,el]));function expandUse(use,stack){const ref=use.getAttribute('href')||use.getAttribute('xlink:href');if(!ref||!ref.startsWith('#'))return null;const id=ref.slice(1),target=targets.get(id);if(!target||stack.has(id))return null;const wrapper=document.createElementNS(NS,'g'),x=parseFloat(use.getAttribute('x'))||0,y=parseFloat(use.getAttribute('y'))||0,transform=use.getAttribute('transform')||'';for(const attr of [...use.attributes])if(!['href','xlink:href','x','y','width','height','transform'].includes(attr.name.toLowerCase()))wrapper.setAttribute(attr.name,attr.value);wrapper.setAttribute('transform',(transform+' translate('+x+' '+y+')').trim());wrapper.setAttribute('data-use-ref',ref);const next=new Set(stack);next.add(id);let clone;if(target.localName.toLowerCase()==='use'){clone=expandUse(target,next);if(!clone)return null}else if(target.localName.toLowerCase()==='symbol'){clone=document.createElementNS(NS,'svg');for(const name of ['viewBox','preserveAspectRatio'])if(target.hasAttribute(name))clone.setAttribute(name,target.getAttribute(name));clone.setAttribute('width',use.getAttribute('width')||target.getAttribute('width')||'100%');clone.setAttribute('height',use.getAttribute('height')||target.getAttribute('height')||'100%');clone.setAttribute('overflow','visible');for(const child of [...target.childNodes])clone.appendChild(child.cloneNode(true))}else clone=target.cloneNode(true);for(const nested of [...clone.querySelectorAll('use')]){const expanded=expandUse(nested,next);if(expanded)nested.replaceWith(expanded);else nested.remove()}wrapper.appendChild(clone);return wrapper}for(const use of [...svg.querySelectorAll('use')]){if(use.closest('defs,marker,clipPath,mask,pattern,symbol'))continue;const expanded=expandUse(use,new Set());if(expanded)use.replaceWith(expanded)}}
function one(item){const host=document.createElement('div');host.className='case';const sanitized=sanitizeSvg(item.svg);if(sanitized.error)return{i:item.i,error:sanitized.error,elements:[],sanitizedSvg:'',references:sanitized.refs};const svg=svgDomCopy(sanitized.node);host.appendChild(svg);document.getElementById('cases').appendChild(host);materializeUses(svg);const vr=svg.viewBox&&svg.viewBox.baseVal;const viewBox=vr&&vr.width?{x:vr.x,y:vr.y,width:vr.width,height:vr.height}:{x:0,y:0,width:svg.clientWidth||300,height:svg.clientHeight||150};const elements=[];let n=0;for(const el of svg.querySelectorAll('line,path,polyline,polygon,circle,ellipse,rect,text')){if(el.closest('defs,marker,clipPath,mask,pattern,symbol')||hiddenByTree(el,svg))continue;const cs=getComputedStyle(el);const tag=el.tagName.toLowerCase(),bbox=boxInRoot(svg,el),useRoot=el.closest('[data-use-ref]');const entry={index:n++,tag,bbox,ref:useRoot?useRoot.getAttribute('data-use-ref'):undefined,text:tag==='text'?(el.textContent||'').trim():'',d:tag==='path'?(el.getAttribute('d')||''):'',fill:cs.fill,fillOpacity:+cs.fillOpacity,stroke:cs.stroke,strokeWidth:parseFloat(cs.strokeWidth)||0,opacity:+cs.opacity,order:n,points:samples(svg,el,tag)};if(tag==='path'){try{entry.length=el.getTotalLength();if(!Number.isFinite(entry.length))entry.geometryError='Icke-finit pathlängd'}catch(e){entry.geometryError=String(e)}}elements.push(entry)}return{i:item.i,viewBox,elements,sanitizedSvg:sanitized.svg,references:sanitized.refs}}
const data=input.map(one);document.getElementById('result').textContent=JSON.stringify(data);
</script>`;
}

function parseDumpDom(text) {
  const match = text.match(/<pre id="result">([\s\S]*?)<\/pre>/i);
  if (!match) throw new Error('Chrome returnerade inget analysresultat.');
  const decoded = match[1].replace(/&quot;/g, '"').replace(/&#39;/g, "'").replace(/&lt;/g, '<').replace(/&gt;/g, '>').replace(/&amp;/g, '&');
  return JSON.parse(decoded);
}

function resolveChromePath(options = {}, env = process.env) {
  const chrome = options.chromePath || env.CHROME_PATH || DEFAULT_CHROME;
  if (!fs.existsSync(chrome)) throw new Error(`Chrome saknas: ${chrome}`);
  return chrome;
}

function validateBatchResults(results, expectedCount) {
  if (!Array.isArray(results) || results.length !== expectedCount) throw new Error(`Chrome returnerade fel antal analysresultat: ${Array.isArray(results) ? results.length : 'icke-array'} (förväntat ${expectedCount}).`);
  for (let i = 0; i < results.length; i++) if (!results[i] || results[i].i !== i) throw new Error(`Chrome-resultat har fel index vid position ${i}: ${results[i] && results[i].i}.`);
  return results;
}

function chromeAnalyzeBatch(figures, options) {
  const chrome = resolveChromePath(options);
  const scratchRoot = options.scratchRoot || process.env.TMPDIR || os.tmpdir();
  const dir = fs.mkdtempSync(path.join(scratchRoot, 'granska-svg-'));
  try {
    const htmlPath = path.join(dir, 'batch.html');
    fs.writeFileSync(htmlPath, makeBrowserHtml(figures), 'utf8');
    const url = pathToFileURL(htmlPath).href;
    const run = spawnSync(chrome, ['--headless=new', '--disable-gpu', '--no-first-run', '--no-default-browser-check', '--disable-extensions', '--allow-file-access-from-files', '--virtual-time-budget=2500', '--dump-dom', '--user-data-dir=' + path.join(dir, 'profile'), url], { encoding: 'utf8', maxBuffer: 120 * 1024 * 1024, timeout: options.chromeTimeout || 120000 });
    if (run.error) throw run.error;
    if (run.status !== 0) throw new Error(`Chrome misslyckades (${run.status}): ${(run.stderr || '').slice(-2000)}`);
    return validateBatchResults(parseDumpDom(run.stdout), figures.length);
  } finally {
    fs.rmSync(dir, { recursive: true, force: true });
  }
}

function isOpaqueBackgroundFor(text, geom, elements) {
  if (!text.bbox || !geom.bbox) return false;
  return elements.some((r) => r.tag === 'rect' && r.order < text.order && r.order > geom.order && r.bbox && r.fill !== 'none' && r.fill !== 'rgba(0, 0, 0, 0)' && r.fillOpacity > 0.75 && r.opacity > 0.75 &&
    r.bbox.x <= text.bbox.x + 1 && r.bbox.y <= text.bbox.y + 1 && r.bbox.x + r.bbox.width >= text.bbox.x + text.bbox.width - 1 && r.bbox.y + r.bbox.height >= text.bbox.y + text.bbox.height - 1);
}

function isLabelBackground(text, geom) {
  return geom.tag === 'rect' && geom.bbox && geom.fill !== 'none' && geom.fill !== 'rgba(0, 0, 0, 0)' && geom.fillOpacity > 0.75 && geom.opacity > 0.75 && geom.order < text.order &&
    geom.bbox.x <= text.bbox.x + 1 && geom.bbox.y <= text.bbox.y + 1 && geom.bbox.x + geom.bbox.width >= text.bbox.x + text.bbox.width - 1 && geom.bbox.y + geom.bbox.height >= text.bbox.y + text.bbox.height - 1;
}

function geometryTouchDistance(text, geom, padding = 0) {
  if (!validBbox(text.bbox) || !validBbox(geom.bbox) || !bboxIntersects(text.bbox, geom.bbox, padding)) return Infinity;
  const smallPointMarker = (geom.tag === 'circle' || geom.tag === 'ellipse') && Math.max(geom.bbox.width, geom.bbox.height) <= Math.max(14, text.bbox.height * 1.5);
  if (smallPointMarker && bboxIntersects(text.bbox, geom.bbox, padding)) return bboxDistance(text.bbox, geom.bbox);
  const points = geom.points || [];
  if (points.length < 2) return Infinity;
  let minDistance = Infinity;
  for (let i = 1; i < points.length; i++) minDistance = Math.min(minDistance, segmentToBboxDistance(points[i - 1], points[i], text.bbox));
  if ((geom.tag === 'circle' || geom.tag === 'ellipse') && points.length > 2) minDistance = Math.min(minDistance, segmentToBboxDistance(points.at(-1), points[0], text.bbox));
  return minDistance <= padding ? minDistance : Infinity;
}

function normalizedText(value) {
  return String(value).replace(/\s+/g, ' ').trim();
}

function nearIdenticalBbox(a, b, tolerance = 0.2) {
  return Math.abs(a.x - b.x) <= tolerance && Math.abs(a.y - b.y) <= tolerance &&
    Math.abs(a.width - b.width) <= tolerance && Math.abs(a.height - b.height) <= tolerance;
}

function uniqueCollisionTexts(texts) {
  const unique = [];
  for (const text of texts) {
    if (!unique.some((other) => normalizedText(other.text) === normalizedText(text.text) && nearIdenticalBbox(other.bbox, text.bbox))) unique.push(text);
  }
  return unique;
}

function lineOrientation(geom) {
  if (geom.tag !== 'line' || !geom.points || geom.points.length < 2) return null;
  const a = geom.points[0], b = geom.points.at(-1);
  if (Math.abs(a.x - b.x) <= 0.5) return 'vertical';
  if (Math.abs(a.y - b.y) <= 0.5) return 'horizontal';
  return null;
}

function gridLikeGeometry(geoms) {
  const vertical = geoms.filter((g) => lineOrientation(g) === 'vertical');
  const horizontal = geoms.filter((g) => lineOrientation(g) === 'horizontal');
  return { detected: vertical.length >= 3 && horizontal.length >= 3, members: new Set([...vertical, ...horizontal].map((g) => g.index)) };
}

function isPureNumericLabel(value) {
  return /^\s*[−+\-]?\d+(?:[.,]\d+)?\s*$/.test(value);
}

function isMeasurementLabel(value) {
  return /(?:^|[\s=:(])(?:\d+(?:[.,]\d+)?\s*)?(?:mm|cm|dm|km|m²|m³|m|kg|mg|g|ml|cl|dl|l|ms|sek|s|min|h|kr|%|°(?:c|f)?|grader)(?:\b|$)/i.test(value) || /\d\s*[×x]\s*\d/i.test(value);
}

function endpointNearRay(point, vertex, leg, tolerance) {
  if (!leg.points || leg.points.length < 2) return false;
  const ends = [leg.points[0], leg.points[leg.points.length - 1]];
  let far;
  if (distance(ends[0], vertex) <= tolerance) far = ends[1];
  else if (distance(ends[1], vertex) <= tolerance) far = ends[0];
  else return false;
  const vx = far.x - vertex.x, vy = far.y - vertex.y;
  const wx = point.x - vertex.x, wy = point.y - vertex.y;
  const cross = Math.abs(vx * wy - vy * wx) / Math.max(1, Math.hypot(vx, vy));
  const dot = vx * wx + vy * wy;
  return cross <= tolerance && dot >= -tolerance;
}

function findVertices(lines, tolerance) {
  const vertices = [];
  for (let i = 0; i < lines.length; i++) for (let j = i + 1; j < lines.length; j++) {
    const a = [lines[i].points[0], lines[i].points.at(-1)];
    const b = [lines[j].points[0], lines[j].points.at(-1)];
    for (const pa of a) for (const pb of b) {
      const d = distance(pa, pb);
      if (d <= tolerance) {
        const candidate = { x: (pa.x + pb.x) / 2, y: (pa.y + pb.y) / 2, d, legs: [lines[i], lines[j]] };
        if (!vertices.some((v) => distance(v, candidate) <= tolerance / 2 && v.legs.some((leg) => candidate.legs.includes(leg)))) vertices.push(candidate);
      }
    }
  }
  return vertices;
}

function bestVertexForArc(arc, vertices, tolerance, minDim) {
  const start = arc.points[0], end = arc.points.at(-1);
  let best = null;
  for (const vertex of vertices) {
    const r1 = distance(start, vertex), r2 = distance(end, vertex);
    if (Math.max(r1, r2) > minDim * 0.75) continue;
    const startMatches = vertex.legs.filter((leg) => endpointNearRay(start, vertex, leg, tolerance));
    const endMatches = vertex.legs.filter((leg) => endpointNearRay(end, vertex, leg, tolerance));
    const distinct = startMatches.some((a) => endMatches.some((b) => a !== b));
    const penalty = (!startMatches.length ? minDim : 0) + (!endMatches.length ? minDim : 0) + (!distinct ? minDim / 2 : 0);
    const score = Math.abs(r1 - r2) + penalty + Math.min(r1, r2) * 0.01;
    if (!best || score < best.score) best = { ...vertex, score };
  }
  return best;
}

function normalizedAngle(value) {
  const full = Math.PI * 2;
  return ((value % full) + full) % full;
}

function angularDistance(a, b) {
  const delta = Math.abs(normalizedAngle(a) - normalizedAngle(b));
  return Math.min(delta, Math.PI * 2 - delta);
}

function angleInsideMinorSector(angle, edgeA, edgeB, tolerance = 0.12) {
  const span = angularDistance(edgeA, edgeB);
  return angularDistance(edgeA, angle) + angularDistance(angle, edgeB) <= span + tolerance;
}

function analyzeGeometry(browser, svg) {
  const findings = invalidMarkupFindings(svg);
  for (const ref of browser.references || []) {
    const external = ref.kind === 'external';
    findings.push(finding(external ? 'WARNING' : 'INFO', external ? 'EXTERNAL_SVG_REFERENCE' : 'UNRESOLVED_SVG_REFERENCE', external ? `Extern ${ref.tag}-referens blockerades utan att hämtas.` : `Intern ${ref.tag}-referens kunde inte lösas.`, [], { element: ref.tag, ref: ref.ref }));
  }
  if (browser.error) {
    findings.push(finding('ERROR', 'INVALID_GEOMETRY', browser.error));
    return findings;
  }
  const vb = browser.viewBox;
  const diag = Math.hypot(vb.width, vb.height);
  const minDim = Math.min(vb.width, vb.height);
  const elements = browser.elements.filter((e) => validBbox(e.bbox) && !(e.tag === 'text' && (e.bbox.width <= 0 || e.bbox.height <= 0)));
  for (const e of browser.elements.filter((item) => item.geometryError)) findings.push(finding('ERROR', 'INVALID_GEOMETRY', `Webbläsaren kunde inte tolka ${e.tag}-geometrin.`, [e.index], { geometryError: e.geometryError, ref: e.ref }));
  const texts = elements.filter((e) => e.tag === 'text' && e.text);
  const collisionTexts = uniqueCollisionTexts(texts);
  const geoms = elements.filter((e) => e.tag !== 'text');
  const grid = gridLikeGeometry(geoms);

  for (const e of elements) {
    const b = e.bbox;
    const left = b.x, right = b.x + b.width, top = b.y, bottom = b.y + b.height;
    const vx1 = vb.x, vx2 = vb.x + vb.width, vy1 = vb.y, vy2 = vb.y + vb.height;
    const fully = right < vx1 - CONFIG.outsideTolerance || left > vx2 + CONFIG.outsideTolerance || bottom < vy1 - CONFIG.outsideTolerance || top > vy2 + CONFIG.outsideTolerance;
    const partial = !fully && (left < vx1 - CONFIG.outsideTolerance || right > vx2 + CONFIG.outsideTolerance || top < vy1 - CONFIG.outsideTolerance || bottom > vy2 + CONFIG.outsideTolerance);
    if (fully) findings.push(finding('ERROR', e.tag === 'text' ? 'TEXT_FULLY_OUTSIDE_VIEWBOX' : 'OBJECT_FULLY_OUTSIDE_VIEWBOX', `${e.tag} ligger helt utanför viewBox.`, [e.index], { coordinates: b }));
    else if (partial) {
      findings.push(finding('WARNING', e.tag === 'text' ? 'TEXT_PARTIALLY_OUTSIDE_VIEWBOX' : 'OBJECT_PARTIALLY_OUTSIDE_VIEWBOX', `${e.tag} ligger delvis utanför viewBox.`, [e.index], { coordinates: b }));
    } else {
      const edge = Math.min(left - vx1, vx2 - right, top - vy1, vy2 - bottom);
      if (edge >= -CONFIG.outsideTolerance && edge < Math.max(0.6, e.strokeWidth / 2)) findings.push(finding('INFO', 'EDGE_CLIPPING', `${e.tag} ligger mycket nära viewBox-kanten.`, [e.index], { distance: round(edge), coordinates: b }));
    }
  }

  for (let i = 0; i < collisionTexts.length; i++) for (let j = i + 1; j < collisionTexts.length; j++) {
    if (bboxIntersects(collisionTexts[i].bbox, collisionTexts[j].bbox, 0.25)) findings.push(finding('WARNING', 'TEXT_TEXT_COLLISION', `Texterna ”${collisionTexts[i].text}” och ”${collisionTexts[j].text}” överlappar.`, [collisionTexts[i].index, collisionTexts[j].index], { distance: round(bboxDistance(collisionTexts[i].bbox, collisionTexts[j].bbox)), coordinates: [collisionTexts[i].bbox, collisionTexts[j].bbox] }));
  }

  for (const text of collisionTexts) {
    const grouped = new Map();
    for (const geom of geoms) {
      if (!bboxIntersects(text.bbox, geom.bbox, CONFIG.proximityPadding)) continue;
      if (isLabelBackground(text, geom)) continue;
      if (isOpaqueBackgroundFor(text, geom, elements)) continue;
      const touchDistance = geometryTouchDistance(text, geom, CONFIG.collisionPadding);
      if (!Number.isFinite(touchDistance)) continue;
      if (grid.detected && isPureNumericLabel(text.text) && grid.members.has(geom.index)) continue;
      const pointLabel = (geom.tag === 'circle' || geom.tag === 'ellipse') && Math.max(geom.bbox.width, geom.bbox.height) <= Math.max(14, text.bbox.height * 1.5) && /^[A-Za-zÅÄÖåäö](?:\b|\()/u.test(text.text);
      const measurement = isMeasurementLabel(text.text);
      const code = pointLabel ? 'POINT_LABEL_COLLISION' : measurement ? 'MEASUREMENT_LABEL_CROSSES_GEOMETRY' : 'TEXT_GEOMETRY_COLLISION';
      if (!grouped.has(code)) grouped.set(code, []);
      grouped.get(code).push({ geom, distance: touchDistance });
    }
    for (const [code, hits] of grouped) {
      const pointLabel = code === 'POINT_LABEL_COLLISION';
      const measurement = code === 'MEASUREMENT_LABEL_CROSSES_GEOMETRY';
      const ids = hits.map((hit) => hit.geom.index);
      const reason = pointLabel ? `Punktetiketten ”${text.text}” kolliderar med punktmarkören.` : measurement ? `Mått-/längdetiketten ”${text.text}” korsar ${hits.length} geometridel${hits.length === 1 ? '' : 'ar'}.` : `Texten ”${text.text}” kolliderar med ${hits.length} geometridel${hits.length === 1 ? '' : 'ar'}.`;
      findings.push(finding('WARNING', code, reason, [text.index, ...ids], { count: hits.length, affectedElementIds: ids, distance: round(Math.min(...hits.map((hit) => hit.distance))), coordinates: [text.bbox, ...hits.map((hit) => hit.geom.bbox)] }));
    }
  }

  const degreeTexts = collisionTexts.filter((t) => /(?:°|grader)/i.test(t.text));
  const lineLikes = geoms.filter((e) => ['line', 'polyline'].includes(e.tag) && e.points && e.points.length >= 2);
  const vertexTolerance = Math.max(2, diag * 0.015);
  const vertices = findVertices(lineLikes, vertexTolerance);
  const arcPaths = geoms.filter((e) => e.tag === 'path' && /[Aa]\s*[-+\d.]/.test(e.d) && e.points.length >= 3 && (Math.hypot(e.bbox.width, e.bbox.height) < diag * 0.48 || degreeTexts.some((t) => bboxDistance(t.bbox, e.bbox) < minDim * 0.3)));
  const usedDegreeLabels = new Set();
  for (const arc of arcPaths) {
    const start = arc.points[0], end = arc.points.at(-1);
    const tol = Math.max(3, diag * CONFIG.angleEndpointToleranceRatio);
    const localVertex = bestVertexForArc(arc, vertices, tol, minDim);
    if (!localVertex) {
      findings.push(finding('INFO', 'ANGLE_ARC_REVIEW', 'Liten båge med vinkelutseende saknar tydligt identifierbara vinkelben.', [arc.index]));
      continue;
    }
    const r1 = distance(start, localVertex), r2 = distance(end, localVertex);
    const radius = (r1 + r2) / 2;
    const spread = Math.abs(r1 - r2);
    if (spread > Math.max(3, minDim * CONFIG.angleCenterSpreadRatio) || radius > minDim * 0.55) findings.push(finding('WARNING', 'ANGLE_ARC_OFF_CENTER', 'Vinkelbågens ändpunkter har orimligt olika avstånd till den avsedda spetsen.', [arc.index, ...localVertex.legs.map((x) => x.index)], { coordinates: { vertex: { x: round(localVertex.x), y: round(localVertex.y) }, start, end }, distances: { start: round(r1), end: round(r2), spread: round(spread) } }));
    const startMatches = localVertex.legs.filter((leg) => endpointNearRay(start, localVertex, leg, tol));
    const endMatches = localVertex.legs.filter((leg) => endpointNearRay(end, localVertex, leg, tol));
    const distinct = startMatches.some((a) => endMatches.some((b) => a !== b));
    const midpoint = arc.points[Math.floor(arc.points.length / 2)];
    const startAngle = Math.atan2(start.y - localVertex.y, start.x - localVertex.x);
    const endAngle = Math.atan2(end.y - localVertex.y, end.x - localVertex.x);
    const midpointAngle = Math.atan2(midpoint.y - localVertex.y, midpoint.x - localVertex.x);
    const wrongSector = distinct && !angleInsideMinorSector(midpointAngle, startAngle, endAngle);
    if (!startMatches.length || !endMatches.length || !distinct || wrongSector) findings.push(finding('WARNING', 'ANGLE_ARC_DIRECTION_MISMATCH', 'Vinkelbågens ändpunkter eller riktning stämmer inte med de identifierade vinkelbenen.', [arc.index, ...localVertex.legs.map((x) => x.index)], { coordinates: { vertex: { x: round(localVertex.x), y: round(localVertex.y) }, start, end, midpoint }, distances: { endpointTolerance: round(tol) }, angles: { start: round(startAngle), end: round(endAngle), midpoint: round(midpointAngle), wrongSector } }));
    const arcExtent = Math.max(arc.bbox.width, arc.bbox.height);
    const longWay = arc.length > Math.PI * Math.max(radius, 1) * 1.25;
    if (radius < minDim * 0.025 || radius > minDim * 0.38 || arcExtent < 3 || longWay) findings.push(finding('INFO', 'ANGLE_ARC_SUSPICIOUS', 'Vinkelbågen är ovanligt liten, stor eller går misstänkt långt runt.', [arc.index], { distances: { radius: round(radius), pathLength: round(arc.length), extent: round(arcExtent) } }));
    const bisectorVector = { x: Math.cos(startAngle) + Math.cos(endAngle), y: Math.sin(startAngle) + Math.sin(endAngle) };
    const bisectorAngle = Math.atan2(bisectorVector.y, bisectorVector.x);
    const candidates = degreeTexts.filter((item) => !usedDegreeLabels.has(item.index)).map((item) => {
      const center = bboxCenter(item.bbox);
      const labelDistance = distance(center, localVertex);
      const labelAngle = Math.atan2(center.y - localVertex.y, center.x - localVertex.x);
      const inside = angleInsideMinorSector(labelAngle, startAngle, endAngle, 0.18);
      return { item, center, distance: labelDistance, angle: labelAngle, inside, score: Math.abs(labelDistance - radius) + angularDistance(labelAngle, bisectorAngle) * Math.max(radius, 1) + (inside ? 0 : minDim) };
    }).sort((a, b) => a.score - b.score);
    const label = candidates[0];
    if (label) usedDegreeLabels.add(label.item.index);
    const radialMisplaced = label && (label.distance > Math.max(radius * CONFIG.degreeLabelDistanceFactor, minDim * 0.34) || label.distance < Math.max(3, radius * 0.25));
    if ((!label && degreeTexts.length) || (label && (!label.inside || radialMisplaced))) findings.push(finding('WARNING', 'DEGREE_LABEL_MISPLACED', label ? `Gradetiketten ”${label.item.text}” ligger orimligt i förhållande till bågens sektor/spets.` : 'Ingen lokal oanvänd gradetikett kunde paras entydigt med vinkelbågen.', label ? [label.item.index, arc.index] : [arc.index], { distance: label ? round(label.distance) : null, coordinates: { label: label ? label.item.bbox : null, vertex: { x: round(localVertex.x), y: round(localVertex.y) } }, angles: label ? { label: round(label.angle), bisector: round(bisectorAngle), insideSector: label.inside } : undefined }));
    const numericLabel = label && label.item.text.match(/^\s*(\d+(?:[.,]\d+)?)\s*(?:°|grader)\s*$/i);
    const actualDegrees = angularDistance(startAngle, endAngle) * 180 / Math.PI;
    const confidentPair = label && label.inside && !radialMisplaced && distinct && !wrongSector && startMatches.length && endMatches.length && spread <= Math.max(3, minDim * CONFIG.angleCenterSpreadRatio) && !longWay && actualDegrees > 1 && actualDegrees < 179;
    if (confidentPair && numericLabel) {
      const statedDegrees = Number(numericLabel[1].replace(',', '.'));
      const tolerance = Math.max(3, actualDegrees * 0.05);
      if (Math.abs(statedDegrees - actualDegrees) > tolerance) findings.push(finding('WARNING', 'ANGLE_LABEL_VALUE_MISMATCH', `Gradetiketten ”${label.item.text}” avviker från den lokala vinkeln ${round(actualDegrees, 1)}°.`, [label.item.index, arc.index, ...localVertex.legs.map((x) => x.index)], { angles: { statedDegrees: round(statedDegrees, 1), actualDegrees: round(actualDegrees, 1), toleranceDegrees: round(tolerance, 1) }, coordinates: { vertex: { x: round(localVertex.x), y: round(localVertex.y) }, label: label.item.bbox } }));
    }
  }

  const seen = new Set();
  return findings.filter((f) => {
    const key = `${f.code}|${(f.elements || []).join(',')}|${f.reason}`;
    if (seen.has(key)) return false;
    seen.add(key);
    return true;
  });
}

async function analyzeSvgFigures(figures, options = {}) {
  const opts = { ...CONFIG, ...options };
  const results = new Array(figures.length);
  let batch = [], chars = 0;
  const flush = () => {
    if (!batch.length) return;
    const browser = chromeAnalyzeBatch(batch.map((x) => x.figure), opts);
    for (let i = 0; i < batch.length; i++) {
      const original = batch[i];
      results[original.index] = { ...original.figure, sanitizedSvg: browser[i].sanitizedSvg || '<svg xmlns="http://www.w3.org/2000/svg"/>', references: browser[i].references || [], viewBox: browser[i].viewBox || parseViewBox(original.figure.svg), elements: browser[i].elements || [], findings: analyzeGeometry(browser[i], original.figure.svg) };
    }
    batch = []; chars = 0;
  };
  for (let i = 0; i < figures.length; i++) {
    const size = figures[i].svg.length;
    if (batch.length && (batch.length >= opts.batchSize || chars + size > opts.maxBatchCharacters)) flush();
    batch.push({ index: i, figure: figures[i] }); chars += size;
  }
  flush();
  return results;
}

function loadBank(repoRoot, file, variable) {
  const source = fs.readFileSync(path.join(repoRoot, file), 'utf8');
  const context = { window: {} };
  vm.createContext(context);
  vm.runInContext(source, context, { filename: file, timeout: 30000 });
  const tasks = context.window[variable];
  if (!Array.isArray(tasks)) throw new Error(`${file}: window.${variable} hittades inte.`);
  return tasks;
}

function collectSvgStrings(value, currentPath = '', out = []) {
  if (typeof value === 'string') {
    const regex = /<((?:[A-Za-z_][\w.-]*:)?)svg\b[\s\S]*?<\/\1svg\s*>/gi;
    let m, n = 0, r = 0;
    while ((m = regex.exec(value))) out.push({ kind: 'inline', svg: m[0], path: `${currentPath}[svg:${n++}]` });
    const addReference = (ref) => out.push({ kind: 'reference', ref, path: `${currentPath}[ref:${r++}]` });
    const attributeRef = /\b(?:src|href)\s*=\s*(?:(["'])([^"']+?\.svg(?:[?#][^"']*)?)\1|([^\s>]+?\.svg(?:[?#][^\s>]*)?))/gi;
    while ((m = attributeRef.exec(value))) addReference(m[2] || m[3]);
    const urlRef = /\burl\(\s*(?:(["'])([^"']+?\.svg(?:[?#][^"']*)?)\1|([^\s)'";]+?\.svg(?:[?#][^\s)'";]*)?))\s*\)/gi;
    while ((m = urlRef.exec(value))) addReference(m[2] || m[3]);
  } else if (Array.isArray(value)) {
    value.forEach((v, i) => collectSvgStrings(v, `${currentPath}[${i}]`, out));
  } else if (value && typeof value === 'object') {
    for (const [k, v] of Object.entries(value)) collectSvgStrings(v, currentPath ? `${currentPath}.${k}` : k, out);
  }
  return out;
}

function resolveSvgReference(repoRoot, ref) {
  const raw = String(ref).trim().replace(/&amp;/gi, '&');
  if (/^(?:[A-Za-z][A-Za-z\d+.-]*:|\/\/|[\\/])/.test(raw)) return { status: 'external' };
  let relative;
  try { relative = decodeURIComponent(raw.split(/[?#]/, 1)[0]); } catch { return { status: 'unresolved' }; }
  const absolute = path.resolve(repoRoot, relative);
  const within = path.relative(repoRoot, absolute);
  if (!relative || within.startsWith('..') || path.isAbsolute(within)) return { status: 'external' };
  if (!fs.existsSync(absolute) || !fs.statSync(absolute).isFile()) return { status: 'unresolved', resolvedPath: within.split(path.sep).join('/') };
  return { status: 'local', absolute, resolvedPath: within.split(path.sep).join('/') };
}

function sourceKeyFor(item) {
  return [item.bank, item.taskIndex, item.taskId, item.figureIndex, item.hash, ...(item.paths || [])].join('|');
}

function extractAll(repoRoot) {
  const figures = [], banks = [], references = [];
  for (const [file, variable, course] of BANKS) {
    const tasks = loadBank(repoRoot, file, variable);
    let raw = 0, containing = 0, unique = 0, referenceCount = 0, localReferences = 0, externalReferences = 0, unresolvedReferences = 0;
    for (const [taskIndex, task] of tasks.entries()) {
      const taskId = String(task.id ?? '(saknar id)');
      const taskHash = crypto.createHash('sha256').update(JSON.stringify(task)).digest('hex');
      const occurrences = collectSvgStrings(task);
      if (!occurrences.length) continue;
      containing++;
      raw += occurrences.length;
      const bySvg = new Map();
      for (const occ of occurrences) {
        if (occ.kind === 'reference') {
          referenceCount++;
          const resolution = resolveSvgReference(repoRoot, occ.ref);
          if (resolution.status === 'local') localReferences++; else if (resolution.status === 'external') externalReferences++; else unresolvedReferences++;
          const provenance = { bank: file, course, taskId, taskIndex, taskHash, path: occ.path, ref: occ.ref, status: resolution.status, resolvedPath: resolution.resolvedPath };
          references.push(provenance);
          if (resolution.status !== 'local') continue;
          const svg = fs.readFileSync(resolution.absolute, 'utf8');
          if (!bySvg.has(svg)) bySvg.set(svg, { paths: [], sourceKinds: new Set(), sourceRefs: [] });
          const entry = bySvg.get(svg);
          entry.paths.push(occ.path); entry.sourceKinds.add('local-file'); entry.sourceRefs.push({ ref: occ.ref, resolvedPath: resolution.resolvedPath, path: occ.path });
          continue;
        }
        if (!bySvg.has(occ.svg)) bySvg.set(occ.svg, { paths: [], sourceKinds: new Set(), sourceRefs: [] });
        const entry = bySvg.get(occ.svg);
        entry.paths.push(occ.path); entry.sourceKinds.add('inline');
      }
      unique += bySvg.size;
      let taskFigure = 0;
      for (const [svg, provenance] of bySvg) {
        const figureIndex = taskFigure++;
        const hash = crypto.createHash('sha256').update(svg).digest('hex');
        const figure = { bank: file, course, taskId, taskIndex, taskHash, figureIndex, paths: provenance.paths, sourceKind: provenance.sourceKinds.size === 1 ? [...provenance.sourceKinds][0] : 'mixed', sourceRefs: provenance.sourceRefs, hash, svg };
        figure.sourceKey = sourceKeyFor(figure);
        figures.push(figure);
      }
    }
    banks.push({ bank: file, course, tasks: tasks.length, tasksContainingSvg: containing, rawOccurrences: raw, figures: unique, references: referenceCount, localReferences, externalReferences, unresolvedReferences });
  }
  return { figures, banks, references };
}

function overlaySvg(result) {
  const vb = result.viewBox;
  const colors = { ERROR: '#dc2626', WARNING: '#f59e0b', INFO: '#2563eb' };
  const marks = [];
  for (const f of result.findings) {
    const color = colors[f.severity];
    for (const index of f.elements || []) {
      const e = result.elements.find((x) => x.index === index);
      if (e && e.bbox) marks.push(`<rect x="${e.bbox.x}" y="${e.bbox.y}" width="${Math.max(e.bbox.width, 1)}" height="${Math.max(e.bbox.height, 1)}" fill="none" stroke="${color}" stroke-width="${Math.max(vb.width, vb.height) / 250}" stroke-dasharray="4 3" vector-effect="non-scaling-stroke"/>`);
    }
    const coords = f.coordinates && f.coordinates.vertex;
    if (coords) marks.push(`<circle cx="${coords.x}" cy="${coords.y}" r="${Math.max(vb.width, vb.height) / 80}" fill="none" stroke="${color}" stroke-width="2" vector-effect="non-scaling-stroke"/>`);
  }
  return result.sanitizedSvg.replace(/<\/((?:[A-Za-z_][\w.-]*:)?)svg\s*>\s*$/i, (_, prefix) => `<g class="svg-review-overlay" pointer-events="none">${marks.join('')}</g></${prefix}svg>`);
}

function evidenceForFinding(result, item) {
  const byIndex = new Map((result.elements || []).map((element) => [element.index, element]));
  return (item.elements || []).map((index) => {
    const element = byIndex.get(index);
    if (!element) throw new Error(`Spårbarhetsfel: fynd ${item.code} hänvisar till element ${index} som saknas i ${result.sourceKey}.`);
    return {
      index,
      tag: element.tag,
      text: element.text || undefined,
      d: element.d || undefined,
      ref: element.ref || undefined,
      bbox: element.bbox,
      pointCount: Array.isArray(element.points) ? element.points.length : 0,
      firstPoint: Array.isArray(element.points) && element.points.length ? element.points[0] : undefined,
      lastPoint: Array.isArray(element.points) && element.points.length ? element.points[element.points.length - 1] : undefined
    };
  });
}

function verifyFindingTraceability(extraction, analyzed) {
  if (!extraction || !Array.isArray(extraction.figures)) throw new Error('Spårbarhetsfel: extraherade källfigurer saknas.');
  if (!Array.isArray(analyzed)) throw new Error('Spårbarhetsfel: analysresultat saknas.');
  if (extraction.figures.length !== analyzed.length) throw new Error(`Spårbarhetsfel: ${extraction.figures.length} källfigurer men ${analyzed.length} analysresultat.`);
  const sources = new Map();
  for (const source of extraction.figures) {
    const expectedKey = sourceKeyFor(source);
    const actualHash = crypto.createHash('sha256').update(source.svg).digest('hex');
    if (source.sourceKey !== expectedKey || source.hash !== actualHash) throw new Error(`Spårbarhetsfel i källproveniens: ${source.bank}:${source.taskId}.`);
    if (sources.has(source.sourceKey)) throw new Error(`Spårbarhetsfel: dubblerad källnyckel ${source.sourceKey}.`);
    sources.set(source.sourceKey, source);
  }
  const matched = new Set();
  let findings = 0, elementReferences = 0;
  const fields = ['bank', 'course', 'taskId', 'taskIndex', 'taskHash', 'figureIndex', 'hash', 'sourceKey', 'sourceKind'];
  for (const result of analyzed) {
    const source = sources.get(result.sourceKey);
    if (!source) throw new Error(`Spårbarhetsfel: analysresultatet saknar exakt källa (${result.sourceKey || 'ingen källnyckel'}).`);
    if (matched.has(result.sourceKey)) throw new Error(`Spårbarhetsfel: källan analyserades flera gånger (${result.sourceKey}).`);
    matched.add(result.sourceKey);
    for (const field of fields) if (result[field] !== source[field]) throw new Error(`Spårbarhetsfel: ${field} avviker för ${source.sourceKey}.`);
    if (JSON.stringify(result.paths) !== JSON.stringify(source.paths) || JSON.stringify(result.sourceRefs || []) !== JSON.stringify(source.sourceRefs || [])) throw new Error(`Spårbarhetsfel: sökväg eller källreferens avviker för ${source.sourceKey}.`);
    for (const item of result.findings || []) {
      const evidence = evidenceForFinding(result, item);
      findings++;
      elementReferences += evidence.length;
    }
  }
  if (matched.size !== sources.size) throw new Error('Spårbarhetsfel: minst en källfigur saknar analysresultat.');
  return { verified: true, figures: matched.size, findings, elementReferences };
}

function buildReport(repoRoot, extraction, analyzed, elapsedMs) {
  const traceability = verifyFindingTraceability(extraction, analyzed);
  const externalInventory = extraction.references || [];
  const byBank = new Map(extraction.banks.map((b) => [b.bank, { ...b, errors: 0, warnings: 0, infos: 0, flaggedFigures: 0 }]));
  const codeCounts = new Map();
  for (const r of analyzed) {
    if (r.findings.length) byBank.get(r.bank).flaggedFigures++;
    for (const f of r.findings) {
      const b = byBank.get(r.bank);
      if (f.severity === 'ERROR') b.errors++; else if (f.severity === 'WARNING') b.warnings++; else b.infos++;
      codeCounts.set(f.code, (codeCounts.get(f.code) || 0) + 1);
    }
  }
  const bankResults = [...byBank.values()];
  const topFindings = [...codeCounts].sort((a, b) => b[1] - a[1]).map(([code, count]) => ({ code, count }));
  const flagged = analyzed.filter((r) => r.findings.length);
  const representativeIds = [...new Set(flagged.slice(0, 30).map((r) => `${r.bank}:${r.taskId}`))].slice(0, 15);
  const json = {
    version: VERSION,
    generatedAt: new Date().toISOString(),
    findingsDeterministic: true,
    volatileMetadata: ['generatedAt', 'summary.runtimeMs'],
    engine: 'Local Google Chrome headless SVG DOM geometry; Node.js standard library only',
    config: CONFIG,
    summary: {
      tasks: bankResults.reduce((s, b) => s + b.tasks, 0),
      tasksContainingSvg: bankResults.reduce((s, b) => s + b.tasksContainingSvg, 0),
      rawOccurrences: bankResults.reduce((s, b) => s + b.rawOccurrences, 0),
      uniqueAnalyzedFigures: analyzed.length,
      flaggedFigures: flagged.length,
      errors: bankResults.reduce((s, b) => s + b.errors, 0),
      warnings: bankResults.reduce((s, b) => s + b.warnings, 0),
      infos: bankResults.reduce((s, b) => s + b.infos, 0),
      runtimeMs: elapsedMs
    },
    banks: bankResults,
    commonFindingTypes: topFindings,
    representativeIds,
    externalInventory,
    traceability,
    mappingNotes: [
      'Alla nästlade strängfält genomsöks, inklusive t, s, spelIntro och spelDelar[*].t/fraga/s.',
      'Exakt identiska SVG-kopior dedupliceras inom samma uppgift; samtliga förekomstsökvägar bevaras.',
      'Externa SVG-/bildreferenser kartläggs och blockeras utan nätverkshämtning; interna #use-referenser löses lokalt när målet finns.',
      'Uppgifts-ID är endast unika inom respektive bank. Varje fynd binds därför även till bankfil, uppgiftsindex, uppgiftshash, figursökväg och SVG-hash.'
    ],
    falsePositiveGuidance: [
      'WARNING och INFO är granskningssignaler, inte automatiska rättningsbeslut.',
      'Täta koordinatsystem, rutnät och avsiktligt närliggande etiketter kan ge kollisionsfynd.',
      'Vinkelheuristik körs bara på små A/a-bågar med närliggande vinkelben och/eller gradetikett.',
      'Överlagringar finns endast i rapportkopian och ändrar aldrig källfiguren.'
    ],
    findings: flagged.map((r) => ({ bank: r.bank, course: r.course, taskId: r.taskId, taskIndex: r.taskIndex, taskHash: r.taskHash, figureIndex: r.figureIndex, paths: r.paths, sourceKey: r.sourceKey, sourceKind: r.sourceKind, sourceRefs: r.sourceRefs, hash: r.hash, viewBox: r.viewBox, findings: r.findings.map((item) => ({ ...item, evidence: evidenceForFinding(r, item) })) }))
  };

  const cards = flagged.map((r, idx) => `<article class="card" data-bank="${escHtml(r.bank)}" data-severity="${escHtml([...new Set(r.findings.map((f) => f.severity))].join(' '))}"><header><h2>${escHtml(r.course)} · ${escHtml(r.bank)} · ID ${escHtml(r.taskId)} · bankindex ${r.taskIndex} · figur ${r.figureIndex + 1}</h2><code>${escHtml(r.sourceKey)} · ${escHtml(r.paths.join(', '))}</code></header><div class="figure">${overlaySvg(r)}</div><ol>${r.findings.map((f) => `<li class="${f.severity}"><strong>${escHtml(f.severity)} · ${escHtml(f.code)}</strong><div>${escHtml(f.reason)}</div><small>element: ${escHtml((f.elements || []).join(', ') || '—')} · detaljer: ${escHtml(JSON.stringify({ coordinates: f.coordinates, distances: f.distances, distance: f.distance, angles: f.angles, evidence: evidenceForFinding(r, f) }))}</small></li>`).join('')}</ol></article>`).join('\n');
  const inventoryHtml = externalInventory.length ? `<details class="inventory"><summary>SVG-referenser (${externalInventory.length})</summary><ul>${externalInventory.map((item) => `<li><strong>${escHtml(item.status)}</strong> · ${escHtml(item.bank)} · ID ${escHtml(item.taskId)} · <code>${escHtml(item.path)}</code> · ${escHtml(item.ref)}${item.resolvedPath ? ` → ${escHtml(item.resolvedPath)}` : ''}</li>`).join('')}</ul></details>` : '';
  const totals = json.summary;
  const html = `<!doctype html><html lang="sv"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width"><title>SVG-granskning</title><style>
:root{font-family:system-ui,sans-serif;color:#242126;background:#f5f4f6}body{margin:0}.top{position:sticky;top:0;z-index:2;background:#211d24;color:white;padding:18px 24px;box-shadow:0 2px 8px #0004}.top h1{margin:0 0 8px}.summary{display:flex;gap:16px;flex-wrap:wrap}.filters{margin-top:10px;display:flex;gap:8px;flex-wrap:wrap}button,select{padding:7px 10px;border-radius:7px;border:1px solid #aaa;background:white}main{max-width:1200px;margin:auto;padding:20px}.card,.inventory{background:white;border-radius:12px;padding:16px;margin:0 0 18px;box-shadow:0 1px 5px #0002}.card h2{font-size:18px;margin:0 0 4px}.figure{border:1px solid #ddd;overflow:auto;padding:10px;margin:12px 0;background:#fff}.figure svg{max-width:100%;height:auto}li{margin:8px 0;padding:8px;border-left:5px solid}.ERROR{border-color:#dc2626;background:#fef2f2}.WARNING{border-color:#f59e0b;background:#fffbeb}.INFO{border-color:#2563eb;background:#eff6ff}small{word-break:break-word;color:#555}.hidden{display:none}</style></head><body><section class="top"><h1>Deterministisk SVG-granskning</h1><div class="summary"><b>${totals.uniqueAnalyzedFigures} unika figurer</b><span>${totals.rawOccurrences} råa förekomster</span><span>${externalInventory.length} SVG-referenser</span><span>${totals.errors} ERROR</span><span>${totals.warnings} WARNING</span><span>${totals.infos} INFO</span><span>${(elapsedMs / 1000).toFixed(1)} s</span></div><div class="filters"><select id="bank"><option value="">Alla banker</option>${bankResults.map((b) => `<option>${escHtml(b.bank)}</option>`).join('')}</select><button data-sev="ERROR">ERROR</button><button data-sev="WARNING">WARNING</button><button data-sev="INFO">INFO</button><button data-sev="">Alla</button></div></section><main>${inventoryHtml}${cards || '<p>Inga fynd.</p>'}</main><script>let sev='';const bank=document.querySelector('#bank');function filter(){document.querySelectorAll('.card').forEach(c=>c.classList.toggle('hidden',(bank.value&&c.dataset.bank!==bank.value)||(sev&&!c.dataset.severity.includes(sev))))}bank.onchange=filter;document.querySelectorAll('button[data-sev]').forEach(b=>b.onclick=()=>{sev=b.dataset.sev;filter()});</script></body></html>`;
  fs.writeFileSync(path.join(repoRoot, 'SVG_GRANSKNING.json'), JSON.stringify(json, null, 2) + '\n', 'utf8');
  fs.writeFileSync(path.join(repoRoot, 'SVG_GRANSKNING.html'), html.replace(/[ \t]+(?=\r?\n|$)/g, ''), 'utf8');
  return { json, bankResults, topFindings, representativeIds };
}

async function main() {
  if (process.argv.includes('--chrome-preflight')) {
    console.log(resolveChromePath());
    return;
  }
  const started = Date.now();
  const repoRoot = path.resolve(__dirname, '..');
  const chromePath = resolveChromePath();
  const extraction = extractAll(repoRoot);
  const analyzed = await analyzeSvgFigures(extraction.figures, { chromePath });
  const elapsed = Date.now() - started;
  const report = buildReport(repoRoot, extraction, analyzed, elapsed);
  console.log(`SVG-granskning klar: ${analyzed.length} unika figurer (${report.json.summary.rawOccurrences} råa förekomster), ${report.json.summary.errors} ERROR, ${report.json.summary.warnings} WARNING, ${report.json.summary.infos} INFO, ${(elapsed / 1000).toFixed(1)} s.`);
  for (const b of report.bankResults) console.log(`${b.bank}: figurer=${b.figures}, råa=${b.rawOccurrences}, ERROR=${b.errors}, WARNING=${b.warnings}, INFO=${b.infos}`);
  console.log('Rapporter: SVG_GRANSKNING.html, SVG_GRANSKNING.json');
}

module.exports = { analyzeSvgFigures, collectSvgStrings, extractAll, overlaySvg, buildReport, resolveChromePath, validateBatchResults, verifyFindingTraceability, CONFIG, VERSION };

if (require.main === module) {
  main().catch((error) => {
    console.error(`SVG-granskning misslyckades: ${error.stack || error.message}`);
    process.exitCode = 1;
  });
}
