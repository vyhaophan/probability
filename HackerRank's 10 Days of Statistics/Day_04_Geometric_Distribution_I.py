def Factorial(x):
    if x <= 1:
        return 1
    return x * Factorial(x-1)
def Combination(n, r):
    return Factorial(n) / (Factorial(r)*Factorial(n-r))
def Exponential(a,n):
    if n <= 0 :
        return 1
    if n == 1:
        return a
    return a * Exponential(a,n-1)
def Binomial(x,n,p):
    q = 1-p
    com = Combination(n,x)
    return com * Exponential(p,x) * Exponential(q,n-x)
def GeometricDistribution(n,p):
    return ((1-p)**(n-1))*p

num, den = input().split()
n = int(input())
num = float(num)
den = float(den)
q = float(num/den)
p = 1 - q
result = GeometricDistribution(n,q)
print(round(result,3))