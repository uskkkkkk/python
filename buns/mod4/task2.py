def fastExp(a, n):
    if n == 1:
        return a
    if n == 0:
        return 1
    elif n % 2 != 0:
        return a * fastExp(a, n-1)
    elif n % 2 == 0:
        return fastExp(a*a, n/2)
a = float(input())
n = int(input())
print(fastExp(a, n))
    
