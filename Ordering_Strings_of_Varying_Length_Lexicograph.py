####Ordering Strings of Varying Length Lexicographically
from itertools import product
file_path = '/Users/luyi/Downloads/rosalind_lexv.txt'
f = open(file_path)
alph = f.readline().strip().split()
N = int(f.readline().strip())
f.close()
alph.insert(0,'*')
string = ''.join(alph)
for it in product(string,repeat = N):
    tmp = ''.join(it)
    if '*' not in tmp:
        print tmp
    else:
        for i in range(1,N):
            if tmp[i:N] == '*'*(N-i) and '*' not in tmp[:i]:
                print tmp.replace('*','')