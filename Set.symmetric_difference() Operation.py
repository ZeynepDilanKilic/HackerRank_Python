n1 = int(input())
s1 = set(input().split())

n2 = int(input())
s2 = set(input().split())

symmetric_diff =  s1.symmetric_difference(s2)

print(len(symmetric_diff))