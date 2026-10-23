#!/usr/bin/env python3
"""Inventera officiella arkivlänkar. Hämtar aldrig själva provuppgifterna.
Kör: python tools/inventera-nationella-prov.py /tmp/nationella/prim-ma1.html /tmp/nationella/umu-arkiv.html
HTML-kopiorna ska hämtas från de angivna arkivadresserna. Resultat på stdout.
"""
import sys,re,json,hashlib
from html.parser import HTMLParser
from urllib.parse import urljoin
from pathlib import Path
SOURCES=[('PRIM-gruppen, Stockholms universitet','https://www.su.se/enheter/prim-gruppen/nationella-prov/niva-1-kurs-1'),('Umeå universitet','https://www.umu.se/institutionen-for-tillampad-utbildningsvetenskap/np/np-2-4/tidigare-givna-prov/')]
class Archive(HTMLParser):
 def __init__(self):
  super().__init__();self.heading=None;self.heading_text=[];self.course=None;self.href=None;self.label=[];self.links=[]
 def handle_starttag(self,tag,attrs):
  if tag in ['h2','h3']:self.heading=tag;self.heading_text=[]
  if tag=='a':self.href=dict(attrs).get('href');self.label=[]
 def handle_data(self,d):
  if self.heading:self.heading_text.append(d)
  if self.href:self.label.append(d)
 def handle_endtag(self,tag):
  if tag==self.heading:
   title=' '.join(self.heading_text)
   match=re.search(r'(?:Kurs|matematik)\s+([123][abc]|4|A)\b',title,re.I)
   if match:self.course='Ma'+(match[1].upper() if match[1].lower()=='a' else match[1].lower())
   else:self.course=None
   self.heading=None
  if tag=='a' and self.href:
   if self.course and re.search(r'\.(?:pdf|zip)(?:$|\?)',self.href,re.I):self.links.append((self.course,re.sub(r'\s+',' ',' '.join(self.label)).strip(),self.href))
   self.href=None
records=[]
for source,filename in zip(SOURCES,sys.argv[1:]):
 publisher,archive_url=source;p=Archive();p.feed(Path(filename).read_text())
 for course,title,href in p.links:
  term=re.search(r'(VT|HT)\s*(\d{4}|\d{2})\b',title,re.I)
  if not term:raise ValueError('Okänt provdatum: '+title)
  year=int(term[2]);year+=2000 if year<100 else 0
  url=urljoin(archive_url,href)
  title_course=re.search(r'\bMa\s*([123][abc]|4)\b',title,re.I)
  notes=[]
  if title_course and 'Ma'+title_course[1].lower()!=course:notes.append('Länktextens kurs avviker från arkivavsnittet. Kontrollera filens innehåll före användning.')
  records.append({'id':hashlib.sha256((course+'|'+url).encode()).hexdigest()[:16],'originalCourse':course,'year':year,'term':term[1].upper(),'title':title,'url':url,'archiveUrl':archive_url,'publisher':publisher,'reviewStatus':'not_reviewed','republicationPermission':'not_verified','notes':notes})
assert len({r['id'] for r in records})==len(records)
print(json.dumps({'checkedOn':'2026-10-23','scope':'Länkar i två officiella arkiv; inte en fullständig inventering av alla historiska prov eller en uppgiftsvis Gy25-granskning.','documents':records},ensure_ascii=False,indent=2))
