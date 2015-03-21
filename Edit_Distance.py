####Edit Distance
from numpy import zeros
s = 'Clarinet'
t = 'Cabinet'

M = zeros((len(s)+1,len(t)+1), dtype=int)
for i in range(1,len(s)+1):
    M[i][0]= i
for i in range(1,len(t)+1):
    M[0][i]= i
print M
# Compute each entry of M.
for i in xrange(1,len(s)+1):
    for j in xrange(1,len(t)+1):
        if s[i-1] == t[j-1]:
            M[i][j] = M[i-1][j-1]
        else:
            M[i][j] = min(M[i-1][j]+1,M[i][j-1]+1, M[i-1][j-1]+1)
print M
# Print and save the desired edit distance.
print M[len(s)][len(t)]
	