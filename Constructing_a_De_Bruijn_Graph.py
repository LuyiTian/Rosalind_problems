####Constructing a De Bruijn Graph

map_dict = {'A':'T','T':'A','G':'C','C':'G'}
def re_comp(string):
    string = string[::-1]
    res = ''
    for bp in string:
        res+=map_dict[bp]
    return res

file_path = '/Users/luyi/Downloads/rosalind_dbru.txt'
S = [line.strip() for line in open(file_path)]
S_rc = [re_comp(i) for i in S]
all_S = list(set(S+S_rc))
k = len(S[0])-1
for it in all_S:
    print '('+it[:k]+', '+it[1:k+1]+')'
