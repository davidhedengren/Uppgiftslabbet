// Read-only structural inventory. Flags guide manual review; never rewrite from these heuristics.
const fs=require('node:fs'),vm=require('node:vm'),path=require('node:path');
const root=path.resolve(__dirname,'..');
const files=['uppgifter.js','uppgifter2.js','uppgifterma1.js','uppgifterma2.js','uppgiftermato1.js','uppgiftermato2.js','uppgiftermatf1.js'];
const empty=()=>({facit:0,noSteps:0,noHeadings:0,noAnswer:0,thin:0});
const result=[];
for(const file of files){
 const ctx={window:{}};vm.runInNewContext(fs.readFileSync(path.join(root,file),'utf8'),ctx);
 const bank=Object.values(ctx.window).find(Array.isArray),areas={};
 const total={file,tasks:bank.length,...empty()};
 for(const q of bank){
  const area=areas[q.omr]??={area:q.omr,tasks:0,...empty()};area.tasks++;
  for(const part of [q,...q.spelDelar||[]]){
   const s=part.s||'',short=s.replace(/<svg[\s\S]*?<\/svg>/g,'').replace(/<[^>]*>/g,'').trim().length<150;
   for(const obj of [total,area]){
    obj.facit++;if(!/facit-steglista/.test(s))obj.noSteps++;if(!/facit-rubrik/.test(s))obj.noHeadings++;
    if(!/facit-svar/.test(s))obj.noAnswer++;if(short)obj.thin++;
   }
  }
 }
 result.push({...total,areas:Object.values(areas)});
}
process.stdout.write(JSON.stringify({notice:'Struktursökning, inte matematisk granskning. Kort text kan vara lämplig för enkla frågor. Ett klassnamn kan saknas trots fungerande förklaring.',banks:result},null,2)+'\n');
