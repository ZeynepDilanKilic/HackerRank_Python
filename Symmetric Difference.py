M = int(input())
a_set = set(map(int, input().split()))
N = int(input())
b_set = set(map(int, input().split()))

a_diff = b_set.difference(a_set)
b_diff = a_set.difference(b_set)

output = b_diff.union(a_diff)

for i in sorted(list(output)):
    print(i)