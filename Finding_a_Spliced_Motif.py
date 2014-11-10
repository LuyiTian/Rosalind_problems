####Finding a Spliced Motif

file_path = '/Users/luyi/Downloads/rosalind_sseq.txt'
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

string,motif = [i for i in read_fasta(file_path)]
motif = [i for i in motif]
RES = []
for ith,bp in enumerate(string):
    if bp == motif[0]:
        motif.pop(0)
        RES.append(ith+1)
    if len(motif) == 0:
        print 'finished'
        break
for i in RES:
    print i,