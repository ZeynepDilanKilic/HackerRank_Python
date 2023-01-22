from itertools import combinations_with_replacement

inp = input().split()
char_list = sorted(inp[0])
n = int(inp[1])

for char in combinations_with_replacement(char_list,n):
    print(''.join(char))