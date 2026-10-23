"""Oberoende matematik och bankkontrakt för första repetitionsomgången.
Kör: python tools/np-repetition-2026-10-23.test.py (kräver sympy).
"""
import json, math, subprocess, unittest, runpy
from pathlib import Path
import sympy as s

ROOT=Path(__file__).resolve().parents[1]
COURSES={'ma1':8,'ma2':6,'mato1':5,'mato2':6}
x,n,t=s.symbols('x n t',real=True)

def load(course):
    text=(ROOT/f'uppgifter{course}.js').read_text()
    return json.loads(text[text.index('['):text.rindex(']')+1])
B={c:[q for q in load(c) if q['omr']=='np_repetition'] for c in COURSES}
def expr(value):return s.sympify(value,locals={'x':x,'n':n,'t':t,'i':s.I,'lg':lambda a:s.log(a,10)})

class Repetition(unittest.TestCase):
    def eq(self,course,num,expected):
        q=B[course][num-1]; actual=q['rättSvar']
        if isinstance(expected,list):
            self.assertEqual(len(actual),len(expected))
            for a,b in zip(actual,expected):
                if isinstance(b,float):self.assertAlmostEqual(float(a),b,places=8,msg=(course,q['id']))
                else:self.assertEqual(s.simplify(expr(a)-b),0,(course,q['id']))
        elif isinstance(expected,float):self.assertAlmostEqual(float(actual),expected,places=8,msg=(course,q['id']))
        else:self.assertEqual(s.simplify(expr(actual)-expected),0,(course,q['id']))
    def alt(self,c,num,index):self.assertEqual([i for i,a in enumerate(B[c][num-1]['alternativ']) if a['ratt']],[index])

    def test_ma1(self):
        self.eq('ma1',1,275*(1-s.Rational(12,100)))
        self.eq('ma1',2,24+3*6)
        self.eq('ma1',3,s.expand(4*(2*x-3)-3*(x+2)))
        self.eq('ma1',4,s.solve(2*x+35-185,x)[0])
        self.eq('ma1',5,2*3+1)
        self.eq('ma1',6,float(850*s.Rational(96,100)**3))
        self.eq('ma1',7,s.solve(s.Rational(8,10)*x-720,x)[0])
        self.eq('ma1',8,float(100*(1-s.Rational(92,100)**3)))
        self.eq('ma1',9,.1)
        self.alt('ma1',10,1)
        self.eq('ma1',11,11.25)
        self.eq('ma1',12,float(8*s.tan(25*s.pi/180)))
        self.eq('ma1',13,float(s.sqrt((4-2)**2+(-1+5)**2)))
        self.eq('ma1',14,8);self.assertLessEqual(95+18*8,240);self.assertGreater(95+18*9,240)
        self.eq('ma1',15,(935-620)//(7-4))
        self.eq('ma1',16,8);self.alt('ma1',17,3)
        self.eq('ma1',18,210-(2*210)//3);self.alt('ma1',19,2)
        self.eq('ma1',20,s.expand((n+2)**2-n**2))

    def test_ma2(self):
        self.eq('ma2',1,s.solve(x*x-49,x));self.eq('ma2',2,x*x-6*x+9)
        self.eq('ma2',3,s.solve(s.diff((x-2)**2-4,x),x)[0])
        y=s.Symbol('y');sol=s.solve([x+y-17,2*x+3*y-42],[x,y]);self.eq('ma2',4,[sol[x],sol[y]])
        self.eq('ma2',5,float(s.log(s.Rational(1,2))/s.log(s.Rational(92,100))))
        self.eq('ma2',6,s.log(14,10));self.eq('ma2',7,(180-50)//2)
        self.eq('ma2',8,3.6)
        values=[4,6,6,8];mean=sum(values)/len(values)
        self.eq('ma2',9,math.sqrt(sum((v-mean)**2 for v in values)/(len(values)-1)))
        self.eq('ma2',10,100*math.erf(1/math.sqrt(2)));self.eq('ma2',11,22-14)
        self.eq('ma2',12,s.solve(s.diff(x*(18-x),x),x)[0]);self.eq('ma2',13,s.solve(s.sqrt(x+6)-x,x)[0])
        self.eq('ma2',14,16);self.eq('ma2',15,[2*4-1,2*2-(-3)])
        self.eq('ma2',16,(s.Rational(32,16)*(x-2)*(x-8)).subs(x,5))
        xx=[1,2,3,4];yy=[3,6,7,10];xm=sum(xx)/4;ym=sum(yy)/4
        k=sum((a-xm)*(b-ym) for a,b in zip(xx,yy))/sum((a-xm)**2 for a in xx)
        self.eq('ma2',17,k*5+(ym-k*xm));self.alt('ma2',18,1)
        roots=s.solve((24-2*x)*(18-2*x)-280,x);self.eq('ma2',19,next(r for r in roots if 0<r<9))
        k=s.Symbol('k');self.eq('ma2',20,s.solve(s.discriminant(x*x-k*x+9,x),k))

    def test_mato1(self):
        self.eq('mato1',1,s.diff(4*x**3-5*x,x));self.eq('mato1',2,s.integrate(6*x*x-4*x,x))
        self.eq('mato1',3,(50-80)//(8-2));self.eq('mato1',4,(10-2)//(5-1))
        self.eq('mato1',5,s.cancel((x*x-25)/(x-5)));self.eq('mato1',6,4)
        self.assertGreater(s.diff(x**3-6*x*x+9,x,2).subs(x,4),0)
        self.eq('mato1',7,s.integrate(2*x+1,(x,0,3)))
        F=s.integrate(4*x+3,x);self.eq('mato1',8,F+10-F.subs(x,1))
        self.eq('mato1',9,float(s.diff(300*s.exp(-t/5),t).subs(t,5)))
        area=x*(60-2*x);at=s.solve(s.diff(area,x),x)[0];self.eq('mato1',10,area.subs(x,at))
        self.eq('mato1',11,7+s.integrate(6*x*x-4*x,(x,0,2)))
        self.eq('mato1',12,20+s.integrate(4+2*t-1,(t,0,5)))
        self.eq('mato1',13,float(s.integrate(s.Abs(x-1),(x,0,3))))
        self.eq('mato1',14,float(s.sqrt(6**2+8**2-2*6*8*s.cos(s.pi/3))))
        b=math.degrees(math.asin(.8));self.eq('mato1',15,sum(30+v<180 for v in [b,180-b]))
        self.eq('mato1',16,float(sum(3000*s.Rational(104,100)**j for j in range(3))))
        feasible=[(a,b) for a in range(11) for b in range(11) if a+b<=10 and 2*a+b<=14]
        self.eq('mato1',17,max(40*a+25*b for a,b in feasible))
        self.eq('mato1',18,-1.5);self.eq('mato1',19,4);self.assertEqual(s.Rational(4,2)*4**2/2,16)
        self.eq('mato1',20,8);self.assertEqual(s.diff(x**4-8*x*x,x).subs(x,2),0)

    def test_mato2(self):
        self.eq('mato2',1,s.diff(s.sin(3*x),x));self.eq('mato2',2,float(2*s.pi/2))
        self.eq('mato2',3,s.Abs(-3+4*s.I));self.eq('mato2',4,s.diff((x*x+1)*s.exp(x),x))
        self.eq('mato2',5,s.diff(x/(x+2),x));self.eq('mato2',6,s.diff(s.log(7-2*x),x))
        self.eq('mato2',7,[float(s.pi/6),float(5*s.pi/6)]);self.eq('mato2',8,.5)
        self.eq('mato2',9,s.pi*s.integrate(2*x,(x,0,3)))
        self.eq('mato2',10,float(1/s.integrate(x,(x,0,4))))
        self.eq('mato2',11,(5+s.I)/(1-2*s.I));self.eq('mato2',12,x**3-3*x*x+4)
        self.eq('mato2',13,3);self.eq('mato2',14,float(5+3*s.cos(s.pi/3)))
        self.eq('mato2',15,s.solve(s.diff(x*s.exp(-x),x),x)[0])
        self.eq('mato2',16,s.diff((2*x+1)**3,x,2).subs(x,1))
        self.eq('mato2',17,[2*s.sqrt(3)*s.I,-2*s.sqrt(3)*s.I]);self.eq('mato2',18,1)
        self.eq('mato2',19,s.integrate(x*s.cos(x)+s.sin(x),(x,0,s.pi/2)))
        self.eq('mato2',20,s.sqrt(5**2-3**2))

    def test_structure_and_existing_content(self):
        authored=runpy.run_path(str(ROOT/'tools/bygg-np-repetition-2026-10-23.py'))['BANKS']
        for c,kap in COURSES.items():
            self.assertEqual(B[c],authored[c],f'{c}: författarkälla och bank skiljer sig')
            allq=load(c);self.assertEqual(len({q['id'] for q in allq}),len(allq));self.assertEqual(len(B[c]),20)
            oldtxt=subprocess.check_output(['git','show',f'HEAD:uppgifter{c}.js'],cwd=ROOT,text=True)
            old=json.loads(oldtxt[oldtxt.index('['):oldtxt.rindex(']')+1]);self.assertEqual(allq[:len(old)],old)
            for q in B[c]:
                self.assertEqual(q['kap'],kap);self.assertEqual(q['repetition']['typ'],'egen')
                self.assertIn('facit-svar',q['s']);self.assertTrue(q['spel']);self.assertTrue(q['självrättning'])
                if q['geogebra']:self.assertTrue(q['miniräknare'])
                self.assertNotIn('spelDelar',q)  # Alla dessa kort är självständiga.
            other=ROOT.parent/'kunskapsgymmet'/f'uppgifter{c}.js';self.assertEqual(other.read_bytes(),(ROOT/other.name).read_bytes())
        self.assertEqual(B['ma1'][10]['kurs'],['1b']);self.assertEqual(B['ma1'][12]['kurs'],['1c'])
        self.assertEqual(B['ma2'][12]['kurs'],['2c']);self.assertTrue(B['ma2'][8]['geogebra'])
        self.assertEqual(B['mato1'][13]['kurs'],['1c']);self.assertEqual(B['mato1'][15]['kurs'],['1b'])

if __name__=='__main__':unittest.main(verbosity=2)
