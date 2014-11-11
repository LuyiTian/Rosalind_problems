####Enumerating Oriented Gene Orderings
N = 3
from itertools import *
res = []
for i in permutations(range(1,N+1)+range(N+2,2*(N+1)), N):
    tmp = [it-N-1 for it in i]
    if len(list(set([abs(x) for x in tmp]))) == len(tmp):
        res.append(tmp)

print len(res)
for i in res:
    for it in i:
        print it,
    print '\n',