
####Locating Restriction Sites

def com_strand(in_string):
    '''Complementing a Strand of DNA'''
    out_string = []
    for chr in in_string:
        if chr == "A":
            out_string.append("T")
        if chr == "T":
            out_string.append("A")
        if chr == "G":
            out_string.append("C")
        if chr == "C":
            out_string.append("G")
    out_string.reverse()
    out_string = ''.join(out_string)
    return out_string

file_path = '/Users/luyi/Downloads/rosalind_revp.txt'
DNA = ''
for line in open(file_path):
    if line[0] == '>':continue
    DNA+=line.strip()

res = []
all_len = range(4,13)
for i in range(len(DNA)-3):
    for j in all_len:
        if i+j > len(DNA):break
        if DNA[i:i+j] == com_strand(DNA[i:i+j]):
            res.append((i,j))
for i,j in res:
    print i+1,j
