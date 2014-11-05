####Completing a Tree

file_path = '/Users/luyi/Downloads/rosalind_tree (2).txt'
f = open(file_path)
N = int(f.readline().strip())
edge_dict = {}
for line in f:
    a,b = [int(i) for i in line.strip().split()]
    edge_dict.setdefault(a,[]).append(b)
    edge_dict.setdefault(b,[]).append(a)
all_node = range(1,N+1)
clife_num = 0
old = 0
tmp_list = []
while all_node:
    if not tmp_list:
        tmp = all_node.pop(0)
        if edge_dict.has_key(tmp):
            tmp_list=[tmp]
        else:
            clife_num+=1
            continue
    for item in range(len(tmp_list)):
        for node in edge_dict[tmp_list[item]]:
            if node not in tmp_list:
                tmp_list.append(node)
    if len(tmp_list)>old:
        old = len(tmp_list)
    elif len(tmp_list) == old:
        clife_num+=1
        for it in tmp_list[1:]:
            all_node.remove(it)
        tmp_list = []
        old = 0
print clife_num-1
