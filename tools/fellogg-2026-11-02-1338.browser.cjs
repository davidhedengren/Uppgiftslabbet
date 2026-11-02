'use strict';
const {chromium}=require('playwright'),path=require('node:path'),assert=require('node:assert/strict');
(async()=>{const b=await chromium.launch({executablePath:'/usr/bin/chromium',args:['--no-sandbox']});try{
 const p=await b.newPage({viewport:{width:1280,height:900}}),errors=[];p.on('pageerror',e=>errors.push(e.message));await p.route('https://*.supabase.co/**',r=>r.abort());await p.route('https://fonts.googleapis.com/**',r=>r.fulfill({body:''}));
 if(process.env.REVIEW_DEPS)await p.route(/^https:\/\/cdn\.jsdelivr\.net\/npm\/(katex|nerdamer)@/,r=>{const m=new URL(r.request().url()).pathname.match(/^\/npm\/(katex|nerdamer)@[^/]+\/(.+)$/);return r.fulfill({path:path.join(process.env.REVIEW_DEPS,m[1],m[2])})});
 await p.goto(process.env.REVIEW_URL||'http://127.0.0.1:8295');await p.waitForFunction(()=>typeof väljKurs==='function');await p.evaluate(()=>{document.body.classList.remove('password-locked');document.getElementById('passwordGate').hidden=true;});
 for(const [course,ids] of [['mato1',['3.132','3.731','3.500','3.486','2.85','2.90','2.95','2.100','2.105','2.110','2.115','2.120','3.359','3.365','3.369']]]){
  assert.equal(await p.evaluate(async course=>väljKurs(KURSER.find(k=>k.id===course),document.querySelector('[data-kurs="'+course+'"]')),course),true,course);
  for(const id of ids){const found=await p.evaluate(id=>{state.spår='1c';byggTräd();const q=variantBank().find(q=>q.id===id);if(!q)return false;state.omr=new Set([q.kap+':'+q.omr]);const pos=urval().findIndex(q=>q.id===id);rita(Math.floor(pos/UPPGIFTER_PER_SIDA));return pos>=0},id);assert.equal(found,true,id);
   const card=p.locator(`article.kort[data-id="${id}"]`);await card.scrollIntoViewIfNeeded();await card.locator('.facitknapp').click({timeout:5000});assert.equal(await card.locator('.katex-error').count(),0,id);
  }
 }
 assert.deepEqual(errors,[]);console.log('Rapporterade uppgifter och jämförelser visas utan KaTeX-fel i Uppgiftslabbet.');
 }finally{await b.close()}})().catch(e=>{console.error(e);process.exitCode=1});
