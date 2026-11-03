'use strict';
const { test } = require('node:test'), assert = require('node:assert/strict'), fs = require('node:fs'), vm = require('node:vm');
const context = { window: {} }; vm.runInNewContext(fs.readFileSync('uppgifterma1.js', 'utf8'), context);
const question = id => context.window.BANKMA1.find(q => q.id === id);
const html = fs.readFileSync('index.html', 'utf8'), rendering = {};
for (const name of ['altVisas', 'uppgiftsText']) { const start = html.indexOf('function ' + name + '('); vm.runInNewContext(html.slice(start, html.indexOf('\n}', start) + 2), rendering); }
rendering.altBokstav = i => String.fromCharCode(65 + i);
function correlation(points) { const n = points.length, mx = points.reduce((s,p) => s+p[0],0)/n, my = points.reduce((s,p) => s+p[1],0)/n; let xy=0,xx=0,yy=0; for (const [x,y] of points) { xy+=(x-mx)*(y-my); xx+=(x-mx)**2; yy+=(y-my)**2; } return xy/Math.sqrt(xx*yy); }
test('Alternativen visas i lärarvyn och varje felsvar ger återkoppling', () => { for (const id of ['5.07','5.25','5.69']) { const q=question(id); assert.ok(rendering.altVisas(q),id); assert.equal((rendering.uppgiftsText(q).match(/class="ul-alt"/g)||[]).length,4,id); assert.equal(q.alternativ.filter(a=>a.ratt).length,1,id); assert.ok(q.alternativ.filter(a=>!a.ratt).every(a=>a.kommentar?.length>20),id); assert.equal(q.geogebra,false); assert.equal(q.miniräknare,true); } });
test('Punktdiagrammen i 5.07 har de samband facit beskriver', () => { const points=[...question('5.07').t.matchAll(/<circle cx="([\d.]+)" cy="([\d.]+)"/g)].map(m=>[Number(m[1]),-Number(m[2])]); assert.equal(points.length,16); const a=correlation(points.slice(0,8)), b=correlation(points.slice(8)); assert.ok(Math.abs(a-1)<1e-12); assert.ok(b>0 && b<1); assert.ok(a>b); });
test('Den textbaserade jämförelsen har ett entydigt svar och r = −0,93 tolkas negativt', () => { assert.match(question('5.69').t,/exakt på en fallande rät linje/); assert.match(question('5.69').t,/inte på en och samma räta linje/); assert.match(question('5.25').t,/-0\{,\}93/); assert.equal(question('5.25').alternativ.find(a=>a.ratt).txt,'Stark negativ korrelation'); });
