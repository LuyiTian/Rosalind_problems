####Consensus_and_Profile
file_path = '/Users/luyi/Downloads/rosalind_cons.txt'

def read_fasta(file_path):
    string_name = None
    for line in open(file_path):
        if line[0] == '>':
            if string_name:
                yield the_string
                the_string = ''
            else:
                string_name = line
                the_string = ''
        else:
            the_string+=line.strip()
    yield the_string

all_string = [res for res in read_fasta(file_path)]

A,T,C,G = [0]*len(all_string[0]),[0]*len(all_string[0]),\
[0]*len(all_string[0]),[0]*len(all_string[0])

for i in range(len(all_string[0])):
    tmp = [it[i] for it in all_string]
    A[i] = tmp.count('A')
    T[i] = tmp.count('T')
    G[i] = tmp.count('G')
    C[i] = tmp.count('C')
res_string = ''
for i in range(len(all_string[0])):
    tmp = (A[i],T[i],G[i],C[i])
    if A[i] == max(tmp):res_string+='A'
    elif T[i] == max(tmp):res_string+='T'
    elif G[i] == max(tmp):res_string+='G'
    else :res_string+='C'
print res_string
print 'A:', ' '.join([str(i) for i in A])
print 'C:', ' '.join([str(i) for i in C])
print 'G:', ' '.join([str(i) for i in G])
print 'T:', ' '.join([str(i) for i in T])





