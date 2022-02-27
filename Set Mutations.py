l = int(input())

s = set(map(int,input().split()))

operation_l =  int(input())

for i in range(operation_l):
    operation =  input().split()
    if operation[0] == "intersection_update":
        temp = set(map(int,input().split()))
        s.intersection_update(temp)
    elif operation[0] == "update":
        temp = set(map(int, input().split()))
        s.update(temp)
    elif operation [0] == "symmetric_difference_update":
        temp = set(map(int,input().split()))
        s.symmetric_difference_update(temp)
    elif operation[0] == "difference_update":
        temp = set(map(int,input().split()))
        s.difference_update(temp)
    else:
        assert False

print(sum(s))