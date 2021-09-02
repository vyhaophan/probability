# When I assign 2.71828 to the calculation, the answer didn't get through test case.
# So I have to import this exp package
from math import exp
def factorial(n):
    return 1 if n <= 1 else n * factorial(n - 1) 
lamb_da = float(input())
k = int(input())
result = lamb_da**k * exp(-lamb_da) / factorial(k)
print(round(result,3))