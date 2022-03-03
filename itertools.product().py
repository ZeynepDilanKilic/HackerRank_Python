from itertools import product

A = list(map(int,input().split()))

B = list(map(int,input().split()))

dot =  list(product(A,B))

for i in dot:
    print(i, end = " ")