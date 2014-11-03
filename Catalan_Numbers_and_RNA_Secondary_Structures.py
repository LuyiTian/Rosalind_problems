####Catalan Numbers and RNA Secondary Structures

#NOTE: main algo is from : https://github.com/jschendel/Rosalind/blob/master/033_CAT.py
#TODO: fix bugs of my original code
comp = {'A':'U', 'U':'A', 'C':'G', 'G':'C'}
def eq_GC(st):
    if (st.count('A')==st.count('U')) and (st.count('G')==st.count('C')):return True
    else: return False
file_path = '/Users/luyi/Downloads/rosalind_cat (2).txt'
RNA = ''

for line in open(file_path):
    if line[0] == '>':continue
    RNA+=line.strip()
def check_subinterval(subint):
    '''Checks if a given subinterval has the same number of matching nucleotides.'''
    N = [subint.count(nucleotide) for nucleotide in 'AUCG']
    return N[0] == N[1] and N[2] == N[3]  # Necessary for a noncrossing perfect bonding.


def noncrossing_perfect_bondings(rna):
    '''Returns the number of noncrossing perfect bondings for the given RNA sequence'''
    # Initialize dictionaries.
    bonding = {'A':'U', 'U':'A', 'C':'G', 'G':'C'}
    noncrossing_bondings = {}

    def count_noncrossing(rna):
        '''Recursively computes the number of noncrossing perfect bondings for a given RNA sequence'''
        if len(rna) <= 2:  # We only send valid rna matchings, so this return is ok.
            return 1
        elif rna in noncrossing_bondings:  # If we've already computed the value, return it!
            return noncrossing_bondings[rna]

        # Determine valid locations where the RNA can be split while maintaining necessary noncrossing conditions.
        splits = [i for i in xrange(1, len(rna), 2) if rna[0] == bonding[rna[i]] and check_subinterval(rna[1:i])]

        # Reduce the problem to noncrossing matchings over the subintervals.
        noncrossing_bondings[rna] = sum([count_noncrossing(rna[1:i])*count_noncrossing(rna[i+1:]) for i in splits]) 

        return noncrossing_bondings[rna]

    return count_noncrossing(rna)
print noncrossing_perfect_bondings(RNA)%1000000