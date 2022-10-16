import re;

N = int(input())
for _ in range(N):
    try:
        re.compile(input())
        output = True
    except re.error:
        output = False
    
    print(output)
