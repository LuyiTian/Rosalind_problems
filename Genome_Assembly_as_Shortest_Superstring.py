###Genome Assembly as Shortest Superstring

file_path = '/Users/luyi/Downloads/rosalind_long (2).txt'
def read_fasta(file_path):
    string = ''
    for line in open(file_path):
        if line[0] == '>':
            if string:
                yield string
                string = ''
        else:
            string += line.strip()
    if string:
        yield string

all_string = [i for i in read_fasta(file_path)]
all_string.sort(key=lambda x:len(x), reverse=True)
for i in range(len(all_string[0])-1,1,-1):
    for a in all_string:
        for b in all_string:
            if b != a:
                if a[-i:] == b[:i]:
                    all_string.insert(0,a[:i]+b)
                    all_string.remove(a)
                    all_string.remove(b)
                elif a[:i] == b[-i:]:
                    all_string.insert(0,b[:i]+a)
                    all_string.remove(b)
                    all_string.remove(a)
            if len(all_string) == 1:
                print 'ANSWER:'
                print all_string[0]
                raise Exception
