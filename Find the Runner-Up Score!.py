if __name__ == '__main__':
    n = int(input())
    arr =list(map(int, input().split()))
    
maks1 = arr[0];
maks2 = 0;


for i in range(n):
    if(arr [i] > maks1):
        maks1 = arr[i]



while(True):
    try:
        arr.remove(maks1)
    except:
        break


for i in range(len(arr)):
    if(abs(arr[i]) > maks2):
        maks2 = arr[i]
        
print(maks2)