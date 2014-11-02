####Introduction to Random Strings
from math import log10

file_path = '/Users/luyi/Downloads/rosalind_prob.txt'
f = open(file_path)
the_string = f.readline().strip()
GCs = [float(i) for i in f.readline().strip().split()]
for the_GC in GCs:
    the_res = 0.
    for i in range(len(the_string)):
        if the_string[i] == 'A' or the_string[i] == 'T':
            the_res+=log10((1-the_GC)/2.)
        if the_string[i] == 'G' or the_string[i] == 'C':
            the_res+=log10(the_GC/2.)
    print the_res,
