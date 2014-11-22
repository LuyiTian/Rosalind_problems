####Counting Subsets

f = lambda x: x and x * f(x - 1) or 1

def C(a,b):
    return (f(a)/f(a-b))/f(b)

N = 900
RES = 1#include empty set
for i in range(1,N+1):
    RES+=C(N,i)
print RES%1000000