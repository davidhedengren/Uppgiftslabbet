'use strict';
// Riktiga lokala GeoGebra-skärmbilder. Inga urklippsbehörigheter eller urklippsanrop.
// GGB_BUNDLE=/.../GeoGebra NODE_PATH=/.../node_modules node tools/ma2-medelvarden-skarmbilder-2026-11-06.cjs
const fs=require('node:fs'),path=require('node:path'),vm=require('node:vm'),assert=require('node:assert/strict'),{chromium}=require('playwright');
const root=path.join(__dirname,'..'),source=fs.readFileSync(path.join(__dirname,'geogebra-skarmbilder.js'),'utf8');
const ctx={require,process,console};
vm.runInNewContext(source.slice(0,source.lastIndexOf('(async () => {'))+';globalThis.helpers={startServer,fillField,probFields,annotate};',ctx);
const jobs=[
 ['4-257-mitt',5.95,.05,5.85,6.05,'Intervall',.9545],
 ['ma2-4-2148-lag',50,2,48,56,'Intervall',.84],
 ['ma2-4-2148-hog',54,2,48,56,'Intervall',.84],
 ['ma2-4-2149',210,10,190,220,'Intervall',.8186],
 ['ma2-4-2150',495,5,490,510,'Intervall',.84],
 ['ma2-4-2151',27,2,23,29,'Intervallkomplement',.1814]
];
(async()=>{assert.ok(process.env.GGB_BUNDLE,'Ange GGB_BUNDLE');const server=await ctx.helpers.startServer(process.env.GGB_BUNDLE);
 const b=await chromium.launch({executablePath:process.env.CHROMIUM||'/usr/bin/chromium',args:['--no-sandbox']});const log=[];
 try{for(const [slug,mu,sigma,lo,hi,mode,expected] of jobs){const p=await b.newPage({viewport:{width:760,height:760},deviceScaleFactor:1.5});
  try{await p.goto('http://127.0.0.1:'+server.address().port);await p.waitForFunction(()=>window.ggbReady,null,{timeout:90000});await p.evaluate(()=>api.setPerspective('6'));await p.waitForSelector('.mathTextField');await p.waitForTimeout(1500);
   await ctx.helpers.fillField(p,0,mu);await ctx.helpers.fillField(p,1,sigma);await p.locator(`button[title="${mode}"]`).click();await p.waitForTimeout(900);await ctx.helpers.fillField(p,2,lo);await ctx.helpers.fillField(p,3,hi);
   await p.locator('.closeTabbedKeyboardButton').click({timeout:500}).catch(()=>{});await p.evaluate(()=>document.activeElement?.blur());await p.waitForTimeout(500);
   const read=await p.evaluate(()=>{const xml=new DOMParser().parseFromString(api.getXML(),'application/xml'),d=xml.querySelector('probabilityCalculator distribution'),i=xml.querySelector('probabilityCalculator interval');
    const labels=[...document.querySelectorAll('.gwt-Label')].filter(e=>e.getBoundingClientRect().width>0),at=labels.findIndex(e=>e.textContent.trim()===') ='),e=labels.slice(at+1).filter(e=>/^\d+(?:\.\d+)?$/.test(e.textContent.trim())).at(-1),r=e?.getBoundingClientRect();
    return {version:api.getVersion(),parameters:d?.getAttribute('parameters'),low:i?.getAttribute('low'),high:i?.getAttribute('high'),mode:i?.getAttribute('mode'),value:e?.textContent.trim(),box:r?{x:r.x,y:r.y+8,w:r.width,h:r.height-16}:null};});
   assert.deepEqual(read.parameters.split(',').map(Number),[mu,sigma]);assert.equal(+read.low,lo);assert.equal(+read.high,hi);assert.ok(Math.abs(+read.value-expected)<.00006,JSON.stringify(read));
   const f=await ctx.helpers.probFields(p),btn=await p.locator(`button[title="${mode}"]`).boundingBox();
   await ctx.helpers.annotate(p,[{...f[0],n:1,side:'corner'},{...f[1],n:2,side:'corner'},{x:btn.x,y:btn.y,w:btn.width,h:btn.height,n:3,side:'corner'},...f.slice(2).map(v=>({...v,n:4,side:'corner'})),{...read.box,n:5,label:'Andelen',side:'below'}]);
   await p.screenshot({path:path.join(root,'bilder',`geogebra-${slug}.png`),clip:{x:0,y:85,width:760,height:675}});
   log.push({slug,mu,sigma,lo,hi,selected:mode,...read});console.log(slug,read.value);
  }finally{await p.close()}}
  fs.writeFileSync(path.join(root,'tools/ma2-medelvarden-geogebra-2026-11-06.json'),JSON.stringify(log,null,2)+'\n');
 }finally{await b.close();server.close()}
})().catch(e=>{console.error(e);process.exitCode=1});
