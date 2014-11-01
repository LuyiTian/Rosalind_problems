####Finding a Protein Motif
''' http://rosalind.info/problems/mprt/questions/
Check at each and every position
I have seen that many people are expressing their anguish.
I came to know the exact issue why our code is working with the example but not with the actual sequences
Many of us might be using functions which read the sequence, they recognize a match and then continue from the position where the first match ends. Here is the catch.
The program should rather check for motif at each and every position.
Example, let us say the motif is from 3-6, the next match is checked from 7. So we will be missing motifs that might be there at positions 4, 5 and 6. so change the code such that it checks for motif at each and every position and you will get it right.
What our program reads: 201 276 351
What actual thing is: 201 276 278 351
'''
import urllib2
import re

file_path = '/Users/luyi/Downloads/rosalind_mprt (2).txt'
id_list = []
'''
N_gly_motif = re.compile(r"N[^P][ST][^P]")## solved, just use (?=N[^P]...)

for line in open(file_path):
    id_list.append(line.strip())
for uniprot_id in id_list:
    urlfile = urllib2.urlopen('http://www.uniprot.org/uniprot/{u_id}.fasta'.format(u_id = uniprot_id))
    Protein = ''
    for line in urlfile:
        if line[0] != '>':
            Protein+=line.strip()
    match = N_gly_motif.finditer(Protein)
    tmp = [m.start()+1 for m in match]## 1 based index instead of 0 based index
    if tmp:
        print uniprot_id 
        for it in tmp:
            print it,
        print '\n',
'''
##use brute force. a stupid way  :(
for line in open(file_path):
    id_list.append(line.strip())
for uniprot_id in id_list:
    urlfile = urllib2.urlopen('http://www.uniprot.org/uniprot/{u_id}.fasta'.format(u_id = uniprot_id))
    Protein = ''
    for line in urlfile:
        if line[0] != '>':
            Protein+=line.strip()
    tmp = []
    for ind, ch in enumerate(Protein):
        if ch == "N" and ind+3 < len(Protein):
            if Protein[ind+1] != "P":
                if Protein[ind+2] == "S" or Protein[ind+2] == "T":
                    if Protein[ind+3] != "P":
                        tmp.append(str(ind+1))
    if tmp:
        print uniprot_id
        print ' '.join(tmp)