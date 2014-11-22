####Matching Random Motifs

N = 91520
p = 0.422336
DNA = 'TAGAGGGCGA'

GC = p/2
AT = 0.5-GC
prob = {'A':AT, 'T':AT, 'G':GC, 'C':GC}
RES = 1

for bp in DNA:
    RES *= prob[bp]

P_not = (1-RES)**N
print 1-P_not