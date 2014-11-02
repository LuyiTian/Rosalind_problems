####RNA Splicing
from Open_Reading_Frames import DNA_to_RNA, RNA_to_protein

file_path = '/Users/luyi/Downloads/rosalind_splc.txt'
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

all_string = [i for i in read_fasta(file_path)]
for i in range(1,len(all_string)):
    all_string[0] = all_string[0].replace(all_string[i],'*')
all_string[0] = all_string[0].replace('*','')
the_RNA = DNA_to_RNA(all_string[0])
print RNA_to_protein(the_RNA,only=True)