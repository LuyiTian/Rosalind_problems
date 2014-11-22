####Finding a Shared Spliced Motif
from numpy import zeros
file_path = '/Users/luyi/Downloads/rosalind_lcsq (1).txt'
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

string_a,string_b = [i for i in read_fasta(file_path)]

def get_lst_mtf(dna1,dna2):
    ##dynamic programming
    M = zeros((len(dna1)+1,len(dna2)+1))
    for i in xrange(len(dna1)):
        for j in xrange(len(dna2)):
            if dna1[i] == dna2[j]:
                M[i+1][j+1] = M[i][j]+1
            else:
                M[i+1][j+1] = max(M[i+1][j],M[i][j+1])

    longest_sseq = ''
    i,j = len(dna1), len(dna2)
    while i*j != 0:
        if M[i][j] == M[i-1][j]:
            i -= 1
        elif M[i][j] == M[i][j-1]:
            j -= 1
        else:
            longest_sseq = dna1[i-1] + longest_sseq
            i -= 1
            j -= 1

    return longest_sseq
print get_lst_mtf(string_a,string_b)