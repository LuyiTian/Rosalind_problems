####Open Reading Frames

################
bases = ['U', 'C', 'A', 'G']
codons = [a+b+c for a in bases for b in bases for c in bases]
amino_acids = 'FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG'
codon_table = dict(zip(codons, amino_acids))

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
def DNA_to_RNA(in_string):
    '''Transcribing DNA into RNA'''
    return in_string.replace('T','U')
def RNA_to_protein(in_string,only = False):
    '''Translating RNA into Protein'''
    final_res = []
    if only:
        res = []
        for i in range(0,len(in_string),3):
            co = in_string[i:i+3]
            if len(co) != 3:continue
            if co == 'AUG':
                res.append('')
            if res:
                if codon_table[co] == '*':
                    final_res+=res
                    res = []
                else:
                    for res_i in range(len(res)):
                        res[res_i]+=codon_table[co]
        final_res = final_res[0]
        return final_res
    for ind in [0,1,2]:#three reading frames for each strand
        res = []
        for i in range(ind,len(in_string),3):
            co = in_string[i:i+3]
            if len(co) != 3:continue
            if co == 'AUG':
                res.append('')
            if res:
                if codon_table[co] == '*':
                    final_res+=res
                    res = []
                else:
                    for res_i in range(len(res)):
                        res[res_i]+=codon_table[co]
    return final_res
################
if __name__ == "__main__":
    file_path = '/Users/luyi/Downloads/rosalind_orf.txt'
    INPUT = ''
    for line in open(file_path):
        if line[0] == '>':continue
        INPUT+=line.strip()

    re_INPUT = com_strand(INPUT)

    RNA = DNA_to_RNA(INPUT)
    re_RNA = DNA_to_RNA(re_INPUT)
    RES = list(set(RNA_to_protein(RNA)+RNA_to_protein(re_RNA)))
    for it in RES:
        print it
