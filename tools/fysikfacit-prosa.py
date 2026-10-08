"""Replace explicit solution-step lists with paragraphs, preserving source bytes.
Only presentation changes: equations, figures, questions and grading are untouched.
Run on an explicitly selected JSON object, never on a heuristic candidate list.
"""
from html.parser import HTMLParser
import re

class StepLists(HTMLParser):
    def __init__(self, source):
        super().__init__(convert_charrefs=False)
        self.source=source;self.stack=[];self.edits=[]
        self.lines=[0]
        for m in re.finditer('\n',source):self.lines.append(m.end())
    def pos(self):
        row,col=self.getpos();return self.lines[row-1]+col
    def handle_starttag(self,tag,attrs):
        attrs=dict(attrs);old=self.get_starttag_text();at=self.pos()
        selected=tag=='ol' and 'facit-steglista' in attrs.get('class','').split()
        item=tag=='li' and bool(self.stack) and self.stack[-1][1]=='list'
        mode='list' if selected else 'item' if item else None
        if mode:self.edits.append((at,at+len(old),'<div class="facit-forklaring">' if selected else '<div class="facit-stycke">'))
        if tag not in {'area','base','br','col','embed','hr','img','input','link','meta','param','source','track','wbr'}:self.stack.append((tag,mode))
    def handle_startendtag(self,tag,attrs):pass
    def handle_endtag(self,tag):
        if not self.stack or self.stack[-1][0]!=tag:return
        _,mode=self.stack.pop()
        if mode:
            at=self.pos();end=self.source.index('>',at)+1;self.edits.append((at,end,'</div>'))

def plain_solution(source):
    parser=StepLists(source);parser.feed(source)
    result=source
    for start,end,new in reversed(parser.edits):result=result[:start]+new+result[end:]
    # Numeric facit-mark labels are generated step numbers; letters identify subquestions.
    result=re.sub(r'<span class="facit-mark">\d+</span>','',result)
    if not re.search(r'class=["\'][^"\']*\bfacit-stegvis\b',result):
        result='<div class="facit-v2 facit-stegvis">'+result+'</div>'
    return result

if __name__=='__main__':
    import sys,json
    path=sys.argv[1];bank=json.loads(open(path).read().removeprefix('window.BANK = ').removesuffix(';\n'))
    changed=0
    def visit(o):
        global changed
        if isinstance(o,dict):
            for k,v in o.items():
                if k=='s' and isinstance(v,str):
                    new=plain_solution(v);changed+=new!=v;o[k]=new
                elif isinstance(v,(list,dict)):visit(v)
        elif isinstance(o,list):
            for v in o:visit(v)
    visit(bank)
    open(path,'w').write('window.BANK = '+json.dumps(bank,ensure_ascii=False,indent=2)+';\n')
    print(f'{changed} solution fields reformatted; mathematical content retained.')
