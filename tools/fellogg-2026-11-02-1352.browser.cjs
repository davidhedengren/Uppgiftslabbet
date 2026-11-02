'use strict';
const {chromium}=require('playwright'),path=require('node:path'),assert=require('node:assert/strict');
(async()=>{const b=await chromium.launch({executablePath:'/usr/bin/chromium',args:['--no-sandbox']});try{
 const p=await b.newPage(),errors=[];p.on('pageerror',e=>errors.push(e.message));await p.route('https://*.supabase.co/**',r=>r.abort());await p.route('https://fonts.googleapis.com/**',r=>r.fulfill({body:''}));
 if(process.env.REVIEW_DEPS)await p.route(/^https:\/\/cdn\.jsdelivr\.net\/npm\/(katex|nerdamer)@/,r=>{const m=new URL(r.request().url()).pathname.match(/^\/npm\/(katex|nerdamer)@[^/]+\/(.+)$/);return r.fulfill({path:path.join(process.env.REVIEW_DEPS,m[1],m[2])})});
 await p.goto(process.env.REVIEW_URL||'http://127.0.0.1:8295');await p.waitForFunction(()=>typeof väljKurs==='function');await p.evaluate(()=>{document.body.classList.remove('password-locked');document.getElementById('passwordGate').hidden=true;});
 assert.equal(await p.evaluate(()=>väljKurs(KURSER.find(k=>k.id==='ma1'),document.querySelector('[data-kurs="ma1"]'))),true);
 for(const width of [390,1280]){await p.setViewportSize({width,height:900});for(const id of ['0.77','0.80','0.86','0.89','0.92','0.98','0.322','0.879']){
 const found=await p.evaluate(id=>{state.spår='1a';byggTräd();const q=variantBank().find(q=>q.id===id);state.omr=new Set([q.kap+':'+q.omr]);const pos=urval().findIndex(q=>q.id===id);rita(Math.floor(pos/UPPGIFTER_PER_SIDA));return pos>=0},id);assert.equal(found,true,id);
 const card=p.locator(`article.kort[data-id="${id}"]`);await card.scrollIntoViewIfNeeded();if(id==='0.89')await card.locator('.katex').first().waitFor();const details=await card.evaluate(el=>({alts:el.querySelectorAll('.ul-alt').length,math:el.querySelectorAll('.katex').length,errors:el.querySelectorAll('.katex-error').length,text:el.textContent}));
 assert.equal(details.errors,0,id);if(id==='0.89'){assert.equal(details.alts,0);assert.ok(details.math>0,JSON.stringify(details));assert.match(details.text,/□/);if(width===1280)await card.screenshot({path:'/tmp/fellogg1352-089.png'});}else assert.equal(details.alts,id==='0.322'?3:4,id);
 await card.locator('.facitknapp').click();assert.equal(await card.locator('.katex-error').count(),0,id);
 }}assert.deepEqual(errors,[]);console.log('Alternativ, ruta och facit visas korrekt i Uppgiftslabbet på mobil och dator.');
 }finally{await b.close()}})().catch(e=>{console.error(e);process.exitCode=1});
