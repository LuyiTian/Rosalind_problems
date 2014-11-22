####Creating a Distance Matrix

file_path = '/Users/luyi/Downloads/rosalind_pdst.txt'
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

DNAs = [i for i in read_fasta(file_path)]

def cont_diff(sa,sb):
    tmp = 0
    for a,b in zip(sa,sb):
        if a != b:tmp+=1
    return float(tmp)/float(len(sa))

RES_dict = {}
for i in range(len(DNAs)):
    for j in range(i,len(DNAs)):
        RES_dict[(i,j)] = cont_diff(DNAs[i],DNAs[j])
        RES_dict[(j,i)] = cont_diff(DNAs[i],DNAs[j])

for row in range(len(DNAs)):
    string = ' '.join([str(RES_dict[row,col]) for col in range(len(DNAs))])
    print string

