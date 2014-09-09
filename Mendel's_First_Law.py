####Mendel's First Law
from functools import reduce 
INPUT = '''17 19 30'''
def factorial(X):
    return reduce(lambda x,y: x*y, range(1, int(X)+1))
def C_ab(a,b):
    return (float(factorial(a))/factorial(a-b))/factorial(b)
AA, Aa, aa = [float(x)for x in INPUT.split()]
_all = float(AA+Aa+aa)
Prob_aa = 0.25*C_ab(Aa,2)/C_ab(_all,2)+0.5*Aa*aa/C_ab(_all,2)+1.*C_ab(aa,2)/C_ab(_all,2)
print 1-Prob_aa