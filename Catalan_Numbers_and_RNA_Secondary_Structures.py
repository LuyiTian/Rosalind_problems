####Catalan Numbers and RNA Secondary Structures
comp = {'A':'U', 'U':'A', 'C':'G', 'G':'C'}
def eq_GC(st):
    if (st.count('A')+st.count('U'))%2 == 0:return True
    else: return False
file_path = '/Users/luyi/Downloads/rosalind_cat (1).txt'
RNA = ''

for line in open(file_path):
    if line[0] == '>':continue
    RNA+=line.strip()


solved_dict = {}
def find_match(S,lo,up):
    if up-lo ==1:
        if S[up] == comp[S[lo]]:
            return 1
        else: return 0
    for bp in range(lo+1,up+1,2):
        #print 'bp:',bp
        if S[lo] == comp[S[bp]]:
            #print '  match'
            #print S[bp+1:up+1]
            if eq_GC(S[lo:bp+1]):
                if bp == up:
                    if solved_dict.has_key(S[lo+1:bp-1]):
                        solved_dict[S[lo:up+1]]+=solved_dict[S[lo+1:bp-1]]
                    else:
                        solved_dict[S[lo+1:bp-1]] = find_match(S,lo+1,up-1)
                        print solved_dict[S[lo+1:bp-1]]
                        solved_dict[S[lo:up+1]]+=solved_dict[S[lo+1:bp-1]]
                    #print '  RES',RES
                #print '    eq_gc',RES
                if solved_dict.has_key(S[lo:bp+1]):
                    if solved_dict.has_key(S[bp+1:up+1]):
                        pass
                    else:
                        solved_dict[S[bp+1:up+1]] = find_match(S,bp+1,up)
                else:
                    if solved_dict.has_key(S[bp+1:up+1]):
                        solved_dict[S[lo:bp+1]] = find_match(S,lo,bp)
                    else:
                        solved_dict[S[lo:bp+1]] = find_match(S,lo,bp)
                        solved_dict[S[bp+1:up+1]] = find_match(S,bp+1,up)
                solved_dict[S[lo:up+1]]+=solved_dict[S[lo:bp+1]]*solved_dict[S[bp+1:up+1]]
                #print '  RES',RES
    if solved_dict.has_key(S[lo:up+1]):
        return solved_dict[S[lo:up+1]]
    else:
        return 0
print find_match(RNA,0,len(RNA)-1)%1000000