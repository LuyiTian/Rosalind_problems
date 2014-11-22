####Error Correction in Reads
map_dict = {'A':'T','T':'A','G':'C','C':'G'}
def re_comp(string):
    string = string[::-1]
    res = ''
    for bp in string:
        res+=map_dict[bp]
    return res

def one_mutation(raw,new):
    tmp = 0
    for a,b in zip(raw,new):
        if a != b: tmp+=1
    if tmp == 1:
        res = 1
    else:
        res = 0
        tmp = 0
        for a,b in zip(re_comp(raw),new):
            if a != b: tmp+=1
        if tmp == 1:
            res = -1
        else:
            res = 0
    return res

file_path = '/Users/luyi/Downloads/rosalind_corr.txt'
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

DNAs = [i for i in read_fasta(file_path)]
re_DNAs = [re_comp(i) for i in DNAs]

correct_list = []
err_list = []
for st in DNAs:
    if (DNAs.count(st)>1) or (re_DNAs.count(st)>=1 and (re_DNAs.index(st) != DNAs.index(st))):
        correct_list.append(st)
    else:
        err_list.append(st)
RES = []
for it in err_list:
    for st in correct_list:
        if one_mutation(st,it) == 1:
            RES.append(it+'->'+st)
        elif one_mutation(st,it) == -1:
            RES.append(it+'->'+re_comp(st))
RES = list(set(RES))
for it in RES:print it

