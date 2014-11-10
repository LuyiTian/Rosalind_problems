####Transitions and Transversions

file_path = '/Users/luyi/Downloads/rosalind_tran.txt'
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

S1,S2 = [i for i in read_fasta(file_path)]

mutation_dict ={('A','G'):0,('G','A'):0,('A','C'):1,('C','A'):1,('A','T'):1,('T','A'):1\
                ,('C','T'):0,('T','C'):0,('C','G'):1,('G','C'):1,('G','T'):1,('T','G'):1\
                ,('A','A'):-1,('T','T'):-1,('G','G'):-1,('C','C'):-1}
transversions = float([mutation_dict[(a,b)] for a,b in zip(S1,S2)].count(1))
transitions = float([mutation_dict[(a,b)] for a,b in zip(S1,S2)].count(0))
print transitions/transversions