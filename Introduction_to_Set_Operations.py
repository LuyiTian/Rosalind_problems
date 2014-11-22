####Introduction to Set Operations
file_path = '/Users/luyi/Downloads/rosalind_seto.txt'
with open (file_path) as f:
    S,A,B = f.readlines()
    S = set(range(1,int(S.strip())+1))
    A = set([int(i) for i in A.strip()[1:-1].split(', ')])
    B = set([int(i) for i in B.strip()[1:-1].split(', ')])
print '{'+', '.join([str(i) for i in list(A|B)])+'}'
print '{'+', '.join([str(i) for i in list(A&B)])+'}'
print '{'+', '.join([str(i) for i in list(A-B)])+'}'
print '{'+', '.join([str(i) for i in list(B-A)])+'}'
print '{'+', '.join([str(i) for i in list(S-A)])+'}'
print '{'+', '.join([str(i) for i in list(S-B)])+'}'