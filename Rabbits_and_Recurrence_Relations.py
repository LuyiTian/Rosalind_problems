####Rabbits and Recurrence Relations
def fibs(n,k):
    res = [0,1]
    for i in xrange(n-1):
        res.append(k*(res[-2])+res[-1])
    return res[-1]
print fibs(30, 4)