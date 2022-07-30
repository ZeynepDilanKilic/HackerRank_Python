inp = input().split()

count  = 0
contain = list(map(int,input().strip().split()))

A = set(map(int, input().strip().split()))
B = set(map(int, input().strip().split()))

for i in contain:
    if i in A:
        count = count + 1
    elif i in B:
        count =  count - 1
        
print(count)
