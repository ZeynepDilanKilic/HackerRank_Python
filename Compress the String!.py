from itertools import groupby

inp = input()

for i,j in groupby(map(int,list(inp))):
    print (tuple([len(list(j)),i]),end = " ")