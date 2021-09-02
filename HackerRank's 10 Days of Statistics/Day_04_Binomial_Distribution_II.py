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

rejection_pct, batch_size = input().split()
rejection_pct = float(float(rejection_pct)/100.)
batch_size = int(batch_size)
p = 1 - rejection_pct
result1 = 0.0
for i in range(8,11):
    result1 += Binomial(i,10,p)
print(round(result1,3))

result2 = 0.0
for i in range(1,9):
    result2 += Binomial(i,10,p)
print(round(result2,3))

