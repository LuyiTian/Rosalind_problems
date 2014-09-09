####Independent Alleles
from functools import reduce 
def factorial(X):
    return reduce(lambda x,y: x*y, range(1, int(X)+1))
def C_ab(a,b):
    return (float(factorial(a))/factorial(a-b))/factorial(b)
def the_func(N,n):
    '''
    tricks~~ the poplution is stable
    '''
    RES = 0
    _all = 2**N
    for i in range(n,_all):
        RES += C_ab(_all,i)*((0.25)**i)*((0.75)**(_all-i))
    return RES
print the_func(6, 15)