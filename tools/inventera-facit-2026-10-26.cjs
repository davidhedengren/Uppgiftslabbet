/* Sökindikatorer, inte automatiska kvalitetsomdömen. Ändrar inga uppgifter. */
const fs=require('fs'),vm=require('vm'),path=require('path');
const root=path.resolve(__dirname,'..');
const files={ma1:'uppgifterma1.js',ma2:'uppgifterma2.js',mato1:'uppgiftermato1.js',mato2:'uppgiftermato2.js',matf1:'uppgiftermatf1.js',fy1:'uppgifter.js',fy2:'uppgifter2.js'};
let summary=[],missing=[];
for(const [course,file]of Object.entries(files)){
 const c={window:{}};vm.runInNewContext(fs.readFileSync(path.join(root,file),'utf8'),c);const bank=Object.values(c.window).find(Array.isArray);
 const row={course,huvuduppgifter:bank.length,huvud_och_delar:0,utan_eget_facit:0,kort_facit_signal:0,utan_ledtrad:0,matte_utan_stegrubrik:0};
 for(const q of bank)for(const [i,a]of [q,...(q.spelDelar||[])].entries()){
  row.huvud_och_delar++;
  const s=(a.s||'').replace(/<svg[\s\S]*?<\/svg>/g,'').replace(/<[^>]*>/g,'').replace(/\s+/g,' ').trim();
  if(!s){row.utan_eget_facit++;missing.push({course,id:q.id,del:i?(a.etikett||i):null,omr:q.omr,spel:q.spel!==false&&a.spel!==false,status:'Behöver manuell kontroll'});}
  else if(s.length<150)row.kort_facit_signal++;
  if(!(a.ledtrad||q.ledtrad||'').trim())row.utan_ledtrad++;
  if(course.startsWith('ma')&&a.s&&!a.s.includes('facit-rubrik'))row.matte_utan_stegrubrik++;
 }
 summary.push(row);
}
const output={datum:'2026-10-26',avgransning:'Inventering av lagrade huvuduppgifter och delobjekt. Kort text och saknade rubriker är söksignaler, inte bevis på bristande facit. Delar utan eget facit ärver huvudfacitet i Kunskapsgymmet och kräver kontroll av svarsläckage. Detta är inte en manuell helbanksgranskning.',summary,kvar_utan_eget_facit:missing};
fs.writeFileSync(path.join(root,'agent/FACIT_INVENTERING_2026-10-26.json'),JSON.stringify(output,null,2)+'\n');console.table(summary);console.log('Kvarvarande delobjekt utan eget facit:',missing.length);
