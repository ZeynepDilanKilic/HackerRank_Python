from collections import Counter

number_shoes = int(input())
shoe_sizes   = Counter(map(int,input().split()))

number_customers =int(input())  

earnings = 0

for customer in range(number_customers):
    size, p_i = map(int,input().split())
    if size in shoe_sizes and shoe_sizes[size] > 0:
        shoe_sizes[size] -= 1
        earnings += p_i
            
print(earnings)