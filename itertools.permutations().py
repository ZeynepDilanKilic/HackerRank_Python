from itertools import permutations

s,r = input().split()

perm = list(permutations(s,int(r)))
perm = sorted(perm,reverse=False)

for i in perm:
    print(*i,sep='')