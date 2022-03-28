def average(array):
    # your code goes here
    arr =  set(array)
    sumA = 0
    s = len(arr)
    for i in arr:
        sumA += i
    return sumA/s

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)