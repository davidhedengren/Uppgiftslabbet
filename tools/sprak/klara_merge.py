import io,re,json,sys
f=sys.argv[1]; s=io.open(f,encoding='utf-8',newline='').read()
m=re.search(r"<<<<<<< [^\n]*\n(.*?)=======\r?\n(.*?)>>>>>>> [^\n]*\n",s,re.S)
def parse(block):
    d={}
    mm=re.search(r"const KLARA=\{(.*)\};",block,re.S)
    for k,v in re.findall(r"'([^']+)':\[([^\]]*)\]",mm.group(1)):
        d.setdefault(k,[])
        for x in re.findall(r"'([^']+)'",v):
            if x not in d[k]: d[k].append(x)
    return d
a,b=parse(m.group(1)),parse(m.group(2))
for k,v in b.items():
    a.setdefault(k,[])
    for x in v:
        if x not in a[k]: a[k].append(x)
ny="const KLARA={ "+", ".join(f"'{k}':[{','.join(repr(x) for x in v)}]" for k,v in a.items())+" };\n"
s=s[:m.start()]+ny+s[m.end():]
io.open(f,'w',encoding='utf-8',newline='').write(s); print(ny[:300])
