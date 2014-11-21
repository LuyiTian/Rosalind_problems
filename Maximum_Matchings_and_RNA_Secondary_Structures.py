####Maximum Matchings and RNA Secondary Structures

f = lambda x: x and x * f(x - 1) or 1

def cout(smer,bger):

    return f(bger)/f(bger-smer)

file_path = '/Users/luyi/Downloads/rosalind_mmch.txt'
RNA = ''
for line in open(file_path):
    if line[0] == '>':continue
    RNA+=line.strip()
AU = cout(min(RNA.count('A'),RNA.count('U')),max(RNA.count('A'),RNA.count('U')))
GC = cout(min(RNA.count('G'),RNA.count('C')),max(RNA.count('G'),RNA.count('C')))
print AU*GC