import numpy as np

n,m = input().split()

np.set_printoptions(legacy = '1.13')
arr = np.eye(int(n),int(m),k=0)

print(arr)