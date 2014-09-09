####Calculating Expected Offspring

INPUT = '''16545 18345 18556 17854 18406 18512'''
AA_AA, AA_Aa, AA_aa, Aa_Aa, Aa_aa, aa_aa = [float(i) for i in INPUT.split()]
RES = AA_AA+ AA_Aa+ AA_aa+ 0.75*Aa_Aa+ 0.5*Aa_aa
RES = RES*2
print RES