####Finding a Shared Motif

#a super ugly brute-force method created by Luyi Tian
#assume a shared motif exists
#and with a lenth larger than four(almost always true)

import re
file_path = '/Users/luyi/Downloads/rosalind_lcsm (1).txt'
def read_fasta(file_path):
    string = ''
    for line in open(file_path):
        if line[0] == '>':
            if string:
                yield string
                string = ''
        else:
            string += line.strip()
    if string:
        yield string

final_RES = []
all_string = [i for i in read_fasta(file_path)]
for seg_len in range(3,15):#generally 15 is large enough!!(hope so)
    tmp_RES = []
    states = True
    for i in range(0,len(all_string[0]),seg_len):
        tmp = [m.start() for m in re.finditer(all_string[0][i:i+seg_len],all_string[1])]
        for i_1 in tmp:
            tmp_lo,tmp_hi = 0,0
            for p in range(1,seg_len):
                if i-p>0 and i_1-p>0:
                    if all_string[0][i-p:i+seg_len] == all_string[1][i_1-p:i_1+seg_len]:
                        tmp_lo = p
                if i+seg_len+p<len(all_string[0]) and i_1+seg_len+p<len(all_string[1]):
                    if all_string[0][i:i+seg_len+p] == all_string[1][i_1:i_1+seg_len+p]:
                        tmp_hi = p
        if tmp:
            tmp_RES.append([i-tmp_lo,i+seg_len+tmp_hi])
    tmp_RES.sort(key=lambda x:x[0])
    RES = [tmp_RES.pop(0)]
    i = 0
    while tmp_RES:
        if tmp_RES[0][0]<RES[-1][1]:
            RES[-1] = [RES[-1][0],tmp_RES[0][1]]
            tmp_RES.pop(0)
        else:
            RES.append(tmp_RES.pop(0))
    RES = [all_string[0][lo:hi] for lo,hi in RES]
    RES.sort(key=lambda x:len(x), reverse=True)
    for i in range(2,len(all_string)):
        if len(RES) == 0:
            states = False
            break
        for motif in RES:
            if motif not in all_string[i]:
                RES.remove(motif)
    if states:
        final_RES.append(RES[0])
final_RES.sort(key=lambda x:len(x), reverse=True)
print final_RES[0]