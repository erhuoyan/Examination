def GreatCommonDivisor(a,b):
    if a > b:
        a,b = b,a
    r = 1
    while r != 0:
        r = a % b
        a = b
        b = r
    return a
m = eval(input())
n = eval(input())
print(GreatCommonDivisor(m,n))