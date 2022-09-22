from collections import OrderedDict

N = int(input())
orderedDict = OrderedDict();

for i in range(N):
    item = input().split()
    itemPrice = int(item[-1])
    itemName = " ".join(item[:-1])
    if(orderedDict.get(itemName)):
        orderedDict[itemName] += itemPrice
    else:
        orderedDict[itemName] =  itemPrice

for i in orderedDict.keys():
    print(i,orderedDict[i])