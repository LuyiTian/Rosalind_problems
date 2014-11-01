####Finding a Motif in DNA
INPUT = '''TTACTTGATTACTTGTTACTTGCGAGTCTCATTTACTTGGGTCTTTACTTGTTACTTGCTTACTTGGCTTACTTGATGTTACTTGTTACTTGAAGAAGGACTTACTTGTTACTTGTTGCTTACTTGCATTACTTGCTGTATTACTTGCAGCTTACTTGTCCAGTTTACTTGCTCTCAACTCTTACTTGCTTTGAATTACTTGCGTTACTTGATTACTTGTTACTTGTGTTACTTGCTTACTTGTTACTTGTTACTTGTGATCAATTACTTGGCTTACTTGTCTTACTTGCATTATTACTTGAAGTTTTACTTGCTTACTTGTGGGCTTCAATGGCGATGATTACTTGTTACTTGTTACTTGAGTATTTTTACTTGGATGGTTTCCTTACTTGTTACTTGACTAGTTACTTGGTTACTTGTAAGTTACTTGGTTACTTGTTACTTGTTACTTGCTTACTTGTGCCTGTGGGTTACTTGAGAACTTACTTGTGTTACTTGCCTTACTTGACGACACGAGTGTTACTTGTCTTACTTGTTACTTGCAGGCCTTGATTACTTGCAATTACTTGATTTACTTGCGTTACTTGCGTTACTTGGAGGTTACTTGGTTACTTGCGTGTAACCTTTACTTGATATTACTTGCATTACTTGGATTACTTGACGTTACTTGTTTACTTGTCTTACTTGTCGAGCTTTACTTGTTACTTGCTTACTTGTTACTTGTTACTTGATTACTTGAGTTACTTGTTTACTTGGTTACTTGTTTACTTGTTACTTGGCTGCTTACTTGCGG'''
motif = 'TTACTTGTT'
RES = []
for i in range(len(INPUT)):
    if INPUT[i:i+len(motif)] == motif:
        RES.append(i+1)
for it in RES:
    print it,