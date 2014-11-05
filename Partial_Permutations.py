####Partial Permutations
N = 95
n = 9
res = 1
for x in range(N,N-n,-1):
    res*=x
print res%1000000