####Enumerating_Gene_Orders
N = 6
from itertools import *
res = []
for i in permutations(range(1,N+1), N):
    res.append(i)
print len(res)
for i in res:
    for it in i:
        print it,
    print '\n',