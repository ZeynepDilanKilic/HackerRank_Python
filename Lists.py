if __name__ == '__main__':
    N = int(input())
    
mlist = []

for i in range(N):
    inp = input().split()
    if inp[0] == "insert":
        mlist.insert(int(inp[1]), int(inp[2]))
    elif inp[0] == "append":
        mlist.append(int(inp[1]))
    elif inp[0] == "remove":
        mlist.remove(int(inp[1]))
    elif inp[0] == "pop":
        mlist.pop()
    elif inp[0] == "sort":
        mlist.sort()
    elif inp[0] == "reverse":
        mlist.reverse()
    elif inp[0] == "print":
        print(mlist)    

