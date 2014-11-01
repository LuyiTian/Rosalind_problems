####A Brief Introduction to Graph Theory

file_path = '/Users/luyi/Downloads/rosalind_grph (1).txt'

DNA_dict = {}
str_name = None
DNA = ''
for line in open(file_path):
    if line[0] == '>':
        if str_name:
            DNA_dict[str_name] = (DNA[:3],DNA[-3:])
            DNA = ''
        str_name = line.strip()[1:]
    else:
        DNA += line.strip()
DNA_dict[str_name] = (DNA[:3],DNA[-3:])
        

for key1 in DNA_dict.keys():
    for key2 in DNA_dict.keys():
        if DNA_dict[key1][1] == DNA_dict[key2][0] and key1 != key2:
            print key1,key2