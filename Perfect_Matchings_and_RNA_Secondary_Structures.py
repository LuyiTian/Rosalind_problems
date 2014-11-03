####Perfect Matchings and RNA Secondary Structures
f = lambda x: x and x * f(x - 1) or 1
file_path = '/Users/luyi/Downloads/rosalind_pmch.txt'
RNA = ''
for line in open(file_path):
    if line[0] == '>':continue
    RNA+=line.strip()

AU = RNA.count('A')+RNA.count('U')
GC = len(RNA)-AU
print f(AU/2)*f(GC/2)