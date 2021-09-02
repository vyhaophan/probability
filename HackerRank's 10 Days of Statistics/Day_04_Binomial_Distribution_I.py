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

boy, girl = input().split()
boy = float(boy)
girl = float(girl)
p = boy / (boy+girl)
result = 0.0
for i in range(3,7):
    result += Binomial(i,6,p)
print(round(result,3))

