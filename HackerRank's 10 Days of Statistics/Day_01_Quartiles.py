# To make the code cleaner, I used the built-in median function
from statistics import median

n = int(input().strip())
arr = [int(x) for x in input().strip().split()]

n = len(arr)
arr = sorted(arr)

if n %2 == 0:        
    m1 = arr[n//2]
    m2 = arr[n//2 - 1]
    med = m1/2 + m2/2   
else:
    med = arr[n//2]

lower_half = arr[:n//2]
upper_half = arr[(n+1)//2:]

print(int(median(lower_half)))
print(int(med))
print(int(median(upper_half)))
    
