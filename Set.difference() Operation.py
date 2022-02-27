n1 = int(input())
s1 = set(input().split())

n2 = int(input())
s2 = set(input().split())

diff = s1.difference(s2)

print(len(diff))