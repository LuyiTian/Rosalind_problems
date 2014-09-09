####Computing GC Content
most_id = ''
most_GC = 0.
file_path = '/Users/luyi/Downloads/rosalind_gc (1).txt'
the_id = None
for line in open(file_path):
    if line[0] == '>':
        if the_id:
            per = GC*100./the_len
            if per > most_GC:
                most_GC = per
                most_id = the_id
        the_id = line.strip()[1:]
        GC = 0
        the_len = 0
    else:
        the_len += len(line.strip())
        GC += line.strip().count('G')+line.strip().count('C')
per = GC*100./the_len
if per > most_GC:
    most_GC = per
    most_id = the_id
print most_id
print most_GC

