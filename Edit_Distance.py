####Edit Distance
from numpy import zeros
t = 'writers'
s = 'vintner'

M = zeros((len(s)+1,len(t)+1), dtype=int)
for i in range(1,len(s)+1):
    M[i][0]= i
for i in range(1,len(t)+1):
    M[0][i]= i
print M
#initialize a matrix M


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

i = len(s)
j = len(t)
al_s = []
midd = []
al_t = []
while True:
    if i-1<0 and j-1<0:break
    dele = M[i][j-1]
    inse = M[i-1][j]
    mt = M[i-1][j-1]
    if dele<inse and dele<mt:
        al_s.append('*')
        midd.append(' ')
        al_t.append(t[j-1])
        j = j-1
    elif inse<dele and inse<mt:
        al_s.append(s[i-1])
        midd.append(' ')
        al_t.append('*')
        i = i-1
    elif mt == M[i][j]:
        al_s.append(s[i-1])
        midd.append('|')
        al_t.append(t[j-1])
        i = i-1
        j = j-1
    else:
        al_s.append(s[i-1])
        midd.append(' ')
        al_t.append(t[j-1])
        i = i-1
        j = j-1
print ''.join(al_s[::-1])
print ''.join(midd[::-1])
print ''.join(al_t[::-1])
