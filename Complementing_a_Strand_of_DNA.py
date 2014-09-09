####Complementing a Strand of DNA
INPUT =  '''
ATGCACGCTTTGCTGTGGCTAAATGGGCACCCCCATGCTGGTAAATCTACAAACGATTTATGTGCAGGTCTCACGCGTGAACGGGGGCGTGCGAAAGAGGCGTCTGGACAAGTAGATATGACGGTTACTTCGCGTTGAGACCCGTCGGGGCCTCCGAGGACAGCCATCCGCAGCCATTAGGGCCGCGGTGTGGTTAAGGAAACATGAAACGGTTATGCGATAGAGTAGCCCCTATGATAACTCAAGTAGAGCCGCGTAAGCGGTGGAAATAAGCTAGTACAGTGAAGTTGAGATCAAACGCGATAGTCGGGGGAGCAGTATGCTTGAATCTATGGCGACTCTTTAAAAATACCCAAAACGAATAGTGACTGGCTGTGCCCCGGACGTGGCATCTAAACCAGCTCTTTTGGTTAAATAGACCCTTATGGTTCGCCCTGGAACTGCGCCAGCCCGTGCGTATTGGTCAGTTTAACAGGAGTCCCAATAGATACAGGACTGTCTAACGATATCCCCCCTGGATTGAAACTACGTTAAAAGCGTTACAGAGCACTAACATATTATTTATCTGTGTATTATTTGCTCGCTGAATTGGCGGCTGAAGAGCTCCTAAACAACAAATGACGAAAGGTGGGGGGGTTCATCAGCCTTTGCTCACACATAGATGTGAATCGTCCTCCTACAACCGAGGACAATCAAGACTACACTGTAATTCCCGTTGCTATTTTTAGGGCTCACCCCTGCGACTAGCTAGGTGCAGCTACACGGCTTGGTAGACCTCTTTTCGTCACATACCAGGGGCGTATCTTTCGGTCAGAGCTA
'''
OUTPUT = []
for chr in INPUT:
    if chr == "A":
        OUTPUT.append("T")
    if chr == "T":
        OUTPUT.append("A")
    if chr == "G":
        OUTPUT.append("C")
    if chr == "C":
        OUTPUT.append("G")
OUTPUT.reverse()
OUTPUT = ''.join(OUTPUT)
print OUTPUT