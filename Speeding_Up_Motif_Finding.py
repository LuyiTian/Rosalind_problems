####Speeding Up Motif Finding
file_path = '/Users/luyi/Downloads/rosalind_kmp.txt'
long_string = ''
for line in open(file_path):
    if line[0] == '>':
        continue
    else:
        long_string+=line.strip()
out_f = open('/Users/luyi/Downloads/rosalind_out','w')

arr_n = 0
for k in xrange(1,len(long_string)+1):
    FIND = False
    for x in range(min(k-1,arr_n+1),0,-1):
        if long_string[:x] == long_string[k-x:k]:
            out_f.write(str(x)+' ')
            arr_n = x
            FIND = True
            break
    if not FIND:
        out_f.write(str(0)+' ')
        arr_n = 0

