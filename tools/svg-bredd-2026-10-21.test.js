'use strict';
// Skydd för FP83: en inbäddad SVG utan bredd fyller hela uppgiftens bredd i Kunskapsgymmet (t.ex. fy1 8.383).
const {test}=require('node:test'),assert=require('node:assert/strict'),fs=require('fs'),path=require('path');
const BANKER=['uppgifter.js','uppgifter2.js','uppgifterma1.js','uppgifterma2.js','uppgiftermatf1.js','uppgiftermato1.js','uppgiftermato2.js'];
const harBredd=tag=>{
 const t=tag.replace(/\\"/g,'"');
 if(/\swidth\s*=/.test(t))return true;
 const st=t.match(/style\s*=\s*"([^"]*)"/);
 return !!(st&&/(^|;)\s*(max-)?width\s*:/.test(st[1]));
};
for(const bank of BANKER)test(bank+': varje figur har en bredd eller maxbredd',()=>{
 const src=fs.readFileSync(path.join(__dirname,'..',bank),'utf8');
 const utan=(src.match(/<svg\b[^>]*>/g)||[]).filter(t=>!harBredd(t));
 assert.equal(utan.length,0,utan.slice(0,3).join('\n'));
});
test('fy2 2.12 och 2.13: de höga fjäderfigurerna är 260 px breda',()=>{
 const src=fs.readFileSync(path.join(__dirname,'..','uppgifter2.js'),'utf8');
 assert.ok(src.includes('width=\\"260\\" height=\\"548\\"'));
 assert.ok(src.includes('width=\\"260\\" height=\\"606\\"'));
});
