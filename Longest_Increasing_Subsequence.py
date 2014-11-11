####Longest Increasing Subsequence

file_path = '/Users/luyi/Downloads/rosalind_lgis (1).txt'
f = open(file_path)
N = int(f.readline().strip())
permutation = [int(i) for i in f.readline().strip().split()]
def get_decre(permutation,N):
    the_i = 0
    RES_list = []
    hi = 0
    for i,num in enumerate(permutation):
        if num>4*float(N)/5.:
            RES_list.append([num])
            the_i = i
            hi = num
            break

    for i in range(the_i+1,len(permutation)):
        max_len = 0
        tmp_l = []
        #if i%100 == 0 and i>the_i+1:
        #    print '_____',i,len(RES_list),hi
        if permutation[i]>hi:
            hi = permutation[i]
            RES_list.append([permutation[i]])
            continue
        for l in RES_list:
            if permutation[i]<l[-1]:
                l.append(permutation[i])
            elif permutation[i]<l[0]:
                for sub_i,nu in enumerate(l):
                    if permutation[i]>nu:
                        if len(l[:sub_i])>max_len:
                            tmp_l = l[:sub_i]
                            max_len = len(l[:sub_i])
                        break
        if tmp_l:
            RES_list.append(tmp_l+[permutation[i]])
    RES_list.sort(key=lambda x:len(x),reverse=True)
    return RES_list[0]
for it in get_decre(permutation[::-1],N)[::-1]:
    print it,
print '\n',
for it in get_decre(permutation,N):
    print it,



