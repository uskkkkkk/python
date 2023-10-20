def gcd_recursion (a, b):
    if a == 0 or b == 0: 
         return max(a, b)
    else:
        if a > b:
            return gcd_recursion(a - b, b)
        else:
            return gcd_recursion(a, b - a)
a = int(input())
b = int(input())
print(gcd_recursion (a, b))
