####Introduction to Alternative Splicing
from math import factorial as f

def C(a,b):
    return (f(a)/f(a-b))/f(b)

m = 916
n = 1885

RES = 0
for k in range(m,n+1):
    RES+=C(n,k)
print RES%1000000