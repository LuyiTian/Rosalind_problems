####k-Mer Composition

bases = ['T', 'C', 'A', 'G']
the_set = [a+b+c+d for a in bases for b in bases for c in bases for d in bases]
the_set.sort()

file_path = '/Users/luyi/Downloads/rosalind_kmer.txt'
DNA = ''
for line in open(file_path):
    if line[0] == '>':continue
    DNA+=line.strip()
all_list = []
for i in range(len(DNA)-3):
    all_list.append(DNA[i:i+4])

for it in the_set:
    print all_list.count(it),