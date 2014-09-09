####Mortal Fibonacci Rabbits
def mortal_fibs(n,k):
    res = {}
    for i in range(k+1):res[i] = 0
    res[0] = 1
    for i in range(n-1):
        m_0 = res[0]
        res[0] = sum([res[x] for x in range(1,k)])
        for j in range(k+1,1,-1):
            res[j] = res[j-1]
        res[1] = m_0
    return sum([res[x] for x in range(k)])
print mortal_fibs(80,19)