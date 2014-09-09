####Translating RNA into Protein
##the codon table is from: http://www.petercollingridge.co.uk/python-bioinformatics-tools/codon-table  by Peter Collingridge
bases = ['U', 'C', 'A', 'G']
codons = [a+b+c for a in bases for b in bases for c in bases]
amino_acids = 'FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG'
codon_table = dict(zip(codons, amino_acids))

SEQ = '''AUGAACUGGGAUGGGAGGGCAGAGUAUGGUGGCCGGUCGAGCUUUGCACUAACUCGGAUCAUGUUUUCGGUCCGCGUUGUUUUCUGGUUGGCAUUGCAGGCCCAAUCCUACUGUAUGCCACAUAAUAUUGUUCUCCGUGCUUUUUUGUUGUACACGUGCACGACUUAUUCCGAGGGCACAACGAAAGCUAUGCCAUGCUUACAAGGGGGAAUAUGGGGAGUUCAAUCUGAACCGAUUCCCCAAACAACUUGGUGUGUCGUCAGCCGAACUAGGCCCUCCUGCCGAUUGGCGUCCGAGAAUAUUGGUGAGGGUAUAGAAAUCCUACCUGAGGAUCCCUGUACUCCCAUAAAAUUAACCUAUGGCGCAGUCCCAUCAUGGAUGGACGAUCGGACGCCAGUUGUAUCUACCCAAAAAUAUACCAACCCUAACUUAACCAAAACGCGAAAAACUCGAAAGUUUCCUGUCGACUCGAUCUCUAUUACGUGGUGGUCGAGUCCCGUAGCGGGCGCUCUGCCUAAUUCCGGUUCAUUCUUAGAGAUACCAAUCUAUUACAGAUGGGAGACUAAGUACGUCACACAGCAAUCGCGCCUCCGAAGCUGGCGACCUGGACGUCUGAAGGAGGCGACCGGGCUCGCCGACCGUCGUACGGGGGGGAUUGGGGUCGUAAUCUGGAUGCACCACGACGCCGCUGUGGGUAAGUGGAUAUGUGUUUUCCUAAACUUGGAUGUAUCUCCGUACCAUAGGGGAAUCUCGUGGGGCCAGGUGUGUAUCAGAAGAACGGCAGCACCUCACCCGCCUCCGUCAUGUGACAUGCGACGAGUCGUCCGCGCUAGGAAUAGUCCUCCGUGGGCAGAGCAAUCACGCUAUCUGUCAGCUGUGAACAGGCGUUCGACUCAGGAUCAGAAGCAAGUACUCCUACGCUCAGCACUGACCCCUCGAUACAUUGCAAUCCCAGAGCCCUGUCUCCGCCCUGGUAUCAUGAUAAAUAUACAACGGCCGUUCUCAUCAACGUCUUUGCAGGUUAGUGCCUUACCUAAAGGCUUUGACGUUACUUUUAGCGGAUCAUACCCGACGCAGCGACUACACGGGCUUCCCACUAUCACAGAAACAAUCCGCCGUUGGCUCCGAGCUCGCGCCUAUCCUGCAUCAAAUGCCAUUUCCUCUCGGACAAGAUGCAGGAUCAUGAGUUUGAUACCCCAUAAGUCGUGGAGGCCGACAUCCUAUCCCCUCCUCUACACGUCUCCUCGCCCUAAAGAGCUUCGGCGGGCUCGGGUAAACCUUAAGUCCGUGUGUGCCUCAAUAAAACCGGUAGGUUGUUUUGCGUUCAGUACGAGUGUUGGUCACUGUAAAGAAGAUUUCGACUUGCGCCGUGGGCUUCUGGCAAAUACUACAUUCCUCCGUAAACCAGGCAGAUACUCUAUUGAACAGGCUACAACAUCCAAGUUAAGGAACAUCCCUUUUGUGCCAAUACGCAAAUCUAAUGUACUUGAUUCGGACUUAACUUCAAUAAUUCCAUUAGGUGAAGAAGAAGGUCGUAUGACGGACGGGCACUGCCGCGGGCUCUUAGGGAUAUCGUCCGGUACCAUUACUCUCAUAGUGAAUUUGUUAUUAAAGAGCUUUCCCUGGGUAGGUAUGGACCCGCGAAGGGUAGCGGGGAUCUACAGCUACUUCCUUGUCUGGAAAAUGGUUGGUCACGAAGUCCAUAUUGAGUAUGGGUCUAAGUUACAUUCGGUUAGGCCCUGUGACCACCCAGGGAAGUACUUGAACCGCCUGUCACAUCCUCAGAGCCCUAGCCCGGCCAAUACGAUAUCUAUGCCUCAAAGAAGUCUUGGUGUUUCCCAUCACUACUAUAUCUCGUGGACAGCCCGCCGCGGUCAGCAGCUGUUUCGGGUUAUGGGGAGACGAUCUCUCUGUUCCCUUAUGGAGCCCAUGGUGCUGGGUACUUGGACCAAUGGAUAUCCUUGCAGUAGCUUUAUUGCCCCGGCGGACGUCCCACGAACACACAUGCUGAAAGGAGUCUUUAGUCCUAGUCCCACAAAUAAUUUUCUUAUGGCCGCGAGUCCUAUUUGGCGGGACCAGAGCCUCUGCGGUGAAUCCCCCCGCGUUCGCGAACGUCAAAGUGAUGGUCUAAAGACAAGUGCAUUAGAUUCGGGAACACGGGGAGUGUCACCACGUGAGCUGAGGCGUAUAUCUACUCAGGGAGGGGACAAACAUGUGCCGAGCCUACGCUCGUGUAUCUCUGAGUUUGGCCCACUACCGUUAUACCGUCUGUGCCCGCUUAUGCAUUUUGUGACCGCCGUGAGUAUAAGCUCGUUAAGGAGGGGGAGUAUAGCAAAAGGAACCUUUCGACCGACGCCAACUGGGACGUACGGACGCUACAAGAGCAGUUCGCGAUCUACAAGCCCGUUAUUUGUGGAUAUUCGACUUCCACGUAGGACCUCGGAUCUCCGGCUUUUAUCUGAGAGAUGUGCCGUAGGUCGUAGACAUUGGUCGUGGGAAAUGCUUAUUAUACUCUUUGAAAAGGCAUUAAAGUCUCUUCAUCUCCGUAUUCGGGAUAUAUAUCUCCCGAACAGACCCAAUGCUUUUGCAUAUUUGGUGAGAGCAGAACGUAACUUAUCAGACCUUGGCUCUUGCCCGAUUAUUCGGAGUAACAGGACCCACUCAGCUUGCACCCGCUGCUUUUUCCAUCGUUGUCUCAGCUUCGCUUCACCUGUUGAUGAACAAGUAUUGUUCUAUGACGUAGGCGAAUGUGUGGGCGGGAUUGCCACAGUGUCUGAUAUAAGCAUUACCGAGGCAAGGUUCCCCAGUACACUCGAGAUUCCGGAGGCCGAGAGCACAAGUGCUUUAAAAUAUGCGAUGGCGCGUUUGGUAAUAGCUCAGUACUCUUAUUUUCUACUAGAGGACCCAUGGCAAUGCCGGGAGCUGUCUCCCUCCUGUUUUUAUACUGGCGCUACCUAUAAGCAGAUGGCAGUACACCCAGUAUGUCGAAGGUUACCCAAAGCAGAGAUACGUAGCCAACGUGAGGCCACUGGCUCAUCCGACGAGAGGGCAGCCCCGAAUCUUCAUGUGUGUCACAACCGUUCUCCAUCCCCACUCUGCCUCCUGUGGGCUACAACGGCCCUAUUCCUAUGGAAGGCUUCCUUGUCCAGUGCUACAGUGGUAGGCAAGGUCUCUCCUGGGAGAGAACGGAUGGGCAAUGGAAGUGAUAGGCUGACCGUCUAUAGGAUUAUGAUGCUCAUGGGCUUUGCCUGGGCGACAAGGAGACCACUAUUAUUACCUUGUGAGCCUCCCCUUUUUCCCUCUCAGGCGUGGAUGAGAAGCCGUUGUCUCAGUUCCGAUUGGCCCGUAAGACUUUAUCAACUAGGAUGGUUCCGGGCCAGCUUUAUGUUUCCAGCGAUCUCCUUGAAUGCCGCAACUUGCCUAGUCGAUCCCUCAGCUGGGUUAUACGGCACGCUGGGUUGUGGCGGAUCACGGUCGUUAAGUUUGCCAAGCCCAAUAAUGCCGCAGUCCAUCAAAUAUAGACGAGUACGUGGCAGACCUUACUGGUCCCUGGGGGUUUUAACCCCCGAACCGAAGCUCUGUAUCUGUCUCAACUCGCCAUUUGGCCUAUCCAAGCCUGCAGACUCCCAGGGCACUCAGACGGACCCACUUACCAAUACAGCUGACCUUACCGACAUUCAGGUGAGGAAUUGCCCAUUCGUCCAAUUCAAACUGACAUGCUCUCACCUAUGCAGGGGAGGUGAACAUGGGUGGGGAUGCAGAAUACCGGAUACAUGUCGUAUAGCGUGUACUUCUUGUGAAACAUCUUAUCCGGCUACGCUGUGUCGUAUUGUGCGACAGGCAAAGCUCCUGGCAAGUGUUCAAUUGAGAGAUGACGUUGGUUCACACAGUGGUGCCCGAUCCCCUUGCUCGACGCUUUCACUAGUGAUGGGCAUUUACGCGGGCACCGGUGCGAAUGCGGUUCAUGAUCCACUACUGCUCCGCGCUGCCCAUCAGAACUUUCGAGAUAGAGGCUCGGACCCGAUAUUUCGCAACGCGACCUUUGGAGUCCCCACAUGGCGAUAUCCAAUUAUAACUCUGAGGACUUCCGGACGAUUCUUGGGUGCACUAGCGGCACGACAAGGGAAUCCUGUCACGGUCACGUGGGCCAGUUCAGCCAAUUCAUCGAGACGGAUGGGUGUGGCGCCGUCUGCCCCUAUAGCGACCAACUACACGACUGCAACUGGAAAUCCAGAUGGGUAUCCUAGAGGUCGAUGCAUGUCAGAUCUCAAAUGCUCAAGGACACGAGAGAACGUAGGCUCGGCGCCCUGCUCGUUAGCGCUUAUCACACGAGGGUGGCCCAUAAUACAAAUUUUACAAGCCAGCCCGUGGCGAGGCCCGGAUGACACUCAGCAGCAGGAAGCCCCGCACAGCCCCUGUAAGAGGAACCCUCGAGAGGACCACUGCGUUCUGAGUGGUCAGCCGGGAAUAGGUAAGACUGAAAUGGGUAGAGGCAAAAUGCGACGCGCGUUUAAUUUGAGUCAACGGUAUUCUGGUAUCUUUUUCACCGCCUCGUCGAUUGUCAACUCAAAGCGGUACCCUGGGCAACCGUCUUCGAUUCUCAGUACCACGGAACUGGAAGCGAGACGGCGACUAUCACUGACCUUUCCAGUGUGUCUCAUAAGCACUAGAAUCGUGAUCAUCGUCCGUCAAGCCGCACGUUGGAUUCUGUGGAAAGUCAUACGUCUGGAUUCGGCUCUGGCCAGCACGCCCUCGUACAAGAUUCCACGAGCGUUACUUUACUAUAUUACAACCCCUCUCUUCGCGCAAGCACUUCUGUCAGCGACAUGGCGGAAGGAGACGCAUUGUCCUGUAGAUACGAGAGAUCCAGUAAUUCCUUUCUCGCAGCACUGGGCCACACUGGGGAAGUACUGGAGCAAGUACACACAAUUCACACGGUGCUACAGUACUCUCAUCCACAAAUUAAGAAUACAUUCGCCAGCAGGCGUGCCCUUUUGCGGAGCCGUGGCCGACGCUUACUAUUCGACCACUGCUCGUAUGCGACCCCGGUUCUCUGAUUCCCUACUUAACUCUGUCGAUACGCCUUUGCGCAAUCAGAUCAUACUUAGGUCAGCUACUUACUGGGUGUGUCUGCCCACGUUACCCGAUUACGGAGGACUGAUAGCAAAGAAAGGCACGUAUGAGAGGUUCGUAACCAUACCUGAAAGUGAUCCCAGGCUAGGCCUCUAUACUUAUGCCCGCAGCAAACACAGUUCUUACACCCAAAUGCGCGCUUUGAUAGAUUGCGGCAGGGAGUGUUGUCUCCAGCCUGUGGACCGUAACUGGCAAUACAAAUCCUAUAGCCACGGGCAGGUUACAGAAACGCUCCUCGUGGGUAGCAAGUGGGCAGAUGACUGGGACUCGCUGUUUUAUUUGAUUCAGGUGCGGCAAUUCGGCAAAGCGAAACAUAGCCACUCCCCUAGCUGUACAUAUCUCACUGUACAACAGGUUUCGGAGUGCACUGCGACCUCGUCCGCGUUGUAUAUAAUAUCAAUUGGGAGGCAUCCUCCUCAGUAUCGGAGGUUGUCUAAGGUGCUUCUAUUUCGUUAUGUUUCUGCCAACGCAGAGAGGAUAGUAAUCGGCAACCGCAUGGAUUUCGCUAAAGGGGCAAGGGGGGAGGGGCUAUACAAUCCUUCUAUCAAAGUCAUUAUGCAGGGCGAUGCUUUUUACAGUUCAGCCACGAAGUACUCCAUAUUAGCGAGGCGAGAUGCCUCUUCCCCGGUGCGCUUAAGGAUGGAGACGCAGGGGUAUGGCAACGGUAUGGGUCAAAUCCCUAUCGGAAGUAGGGCUCACGAUGUGGAGAUCUGGGAUCGCAAUGUAAUGACUAACGACGACUGCCAGGUAGGGAGUCUUGAGGACUUGCUCAUUGGUAUUGUAUACUCAAGCUCUCUCUUGACUGGUUCACCAACGUCUAUGGUACUACUUUGGGGGGACGACGGACGAGGCUACCUCUCGAACGUGGCAAGGGGCGUCCGCAGAUAUAUGGUGUGUGCGAAUGUUGGGCAGGUUAUCUUCCGCGCUACCGUUAGUCCCGCUCACUGGGUGCGGAAACCCUUACAAACAGGCGUCGAACAUCGUCUAGAGUCGCGAUAUUGGAUUGCCCGAUUAACCCCUAAACACGCAUUGACAAAUUGGGGCGAGACGGGUCACGGAACUAACCUCGGGACCGGCGAACAGUACAAAUUCCAGUUUCUAGACCCGUUCUGUGGCACGCCCAUCCAAUGUGGAUUCUACCGGCCAACCGGAAAACAUAAUCUCUCAUGGAACGUGGCCCCGGUAGUCUCCGGAAGAGUGAAUCGGCUGUUUCAGCACAAGGCGGGCACAUCCAGUUUUCAUAUGUCUCGAGAAACAGGGGGACCACUGUAUUAUCUCCGGUUUGAGGGGACUACCGUAGGGGGGUAUUUCGGUCGACCGACCAGAGGCAGUAGAAUCUUAUGCUCGUUGGCUCUUCAAACGAUUGAAGAGAAUGCCUUUUUACAUCUUGUGACUAAGCAGUUCCCAGCACAAACGACAAUGAGGCGCGGUCCAAUAGAGGUGACCGAAUAUAUUCGGUUACAGCCUGCCGCGCAUUUACCAGGGUGCAGAUACGGUACGUCGCACCGAUACGGACGACCCGCAUUUCUAGCCACCAGUCCACCUGUCCCAUUGCGGUCUAGUGUCAUGCUACUACGAGGUGCCUAUGCCGUACGCGAAAUUAAUCCGAGAGUCUCUCUAUACGAGCUGCAUAACCGAUCCGGAUCUGAUUCGUUGUGUGGCUUGUUCCUAAGCGUCCAUCAGACAUUCUCUAAUGCAAAGAUUAACUGCUCAAGCAAUGGCAUAGGAGACGCUCCUCCUUUCUUGCUAUGUUUCUUUAUACGCCAGGUCAAUUAUCCUCCGAAUCUGUGGUCUCGUCCCAAUAGACCGAGCGUAGACGUCAUGCUUACUAGUUCUGUGCGACCCUUAAUGGUCGUUCUAUCACAGGACCGUAGCGCCAUUCAGAUUAGCGAGUUAUUCAGUUUGAUCAAGCUAGCCAGCACGAACAUACAAAGCUCACACGACCCAGACCGCGGAAUAAGCGUGAUUACGCUGUAUAGUCUCGUGAGAGGAUAUAGGUUUCCGUUUCCAACCGCCAGCCCGUGGGACAUUAAUGGCGCACUUGCUUCGCCCAUGGUGAUGUGGGACAGGUUUACUUGUAGUCGUGGAUCCGGAUUGUCCAGCGAAGGCCGGCUCCCUAUGCCGCCCCACGCCAGCCGGUGCUCAUUCAUGACGUGCGAGCAAUUCGCAUAUGUCAAACCACCUAAUAUACGGUGGGUCAGGUUAGAGGUCGAUGUAUGUAUUGGUGCAGUAUCUAGAAAUACCGCUACAUAUCUCUCUUGUCACAACGAAUCGUUCAAGUGCCAUGUCCACACCUACUGUUGUUUCAUUAAGUUGAGCAGGUGCACCAAGGGGUUGAACGAGUGUUUUGCCCAAAAAGCCGCUUCGAGGUACUCGAAUGCCCAAUGGAUCCUCAGCAAACCUCCUUCAACACGUGCGUCCCCAGGAAUCUUACUAUAUUUCAUCGACACGACGCUUGUAUUUGUAUGCACCUUCCACGGGGACUUAGUACCCAAGCACUCUAGCAACUCGUGGCUAGAAACCAUCCGUAGUUCUCACCGGCGUAAUCGUUUAGGCGCAGCAUCACGCUCUCUGCCGUUGGUGUUAUGCCAAAACAAACCCAUGUACGGCAGGCCAAGCUGUCCAGAGUGUUUGAAUUUUACUGUUAGUUUGCCUUCCUGCUCCAGUACGACCUGCGGCAUUCUAUGGAAACUUGGCCUUCCGAAUCAGAGACCCAAUCGCACGGUGAGCUUAUACCCAACAUCUCAAAGUGGAUCUCAGCCUAACUCCGGGGGAUUUCGUCUUGAAUUUUCUCCCUUUAUCUUGUCCGUUCACAUACUGUUCUCUUACGUCGUUAUGACCCUUCCAAAGUCGGUAAGUACCAACACAGACGUGAAAUCCUGUUUUAUAUCGGUUCCUACUAAGCUUCAGAUAAAGCUCCCGUAUGUACCGAGUUUCCAAUCGCCGUCGUUAUUCUACGAUGUGGGCAAUCGGGUAUCGCCCGCACCGGGUGUUCAGACAGAGUACGUUACAAGUGCUGCCAUAAACAACUUAAGCGCUAGUGAGAGUCAGGGUACCGUAUUGUCGUCCAGAGUACAAUAUGGCGGGUCCCAGCGCCUCCUCUGUUGCUGUAGCGAUUCGACUUACUACAGACUCGCAGCGCUGCAAUCUCUGAUCUCACUCCUCACUAAUAGAAGGGGCCCGGGUUGGGAUGCACUACUUCCAGUUAGUACCCCUAUAUUAUUCCGCCUGCUGUGUAACGUUCCGAGUGGUGUAACCCUAUUAGCUCGUAAGGUGCCGACGAUCUAUGUACACACGAUACUAACAUCAGGCAGAUGUCAUCUACGCUCUGGCGACAUGUUAGUGGGUGCAUUUCGAGAAGAUUCGUCUUUCGUGUUAAUGGAUUACUACUCCGGUAUUCACUACGGCCUGCCCCAGGGGGAUAUGCGGUCAGCCCCGGAGCGACGAAAUGCUGGCGCGCAAUCACACCAAGAGAUCGUAGUCAUAGGUAAGCAAGAUGCAUACUGCCGUGGCCGUAGACUCCCUAGACGUCACAGCCAGGCUUUUUCGGCUCGGACCGUUGAGUACUUGACCCCAGUGUAG'''
RES = ''
for i in range(0,len(SEQ),3):
    co = SEQ[i:i+3]
    if codon_table[co] == '*':break
    RES+=codon_table[co]
print RES