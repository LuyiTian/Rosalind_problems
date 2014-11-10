####Enumerating k-mers Lexicographically

from itertools import *
order = ['N', 'C', 'M', 'X', 'V']
N = 4

k_mers = [''.join(item) for item in product(order, repeat=N)]
for i in k_mers:print i