abc = str(input())
index1 = abc.find(' ')
index2 = abc.find(' ', index1 + 1)
a = int(abc[:index1])
b = int(abc[index1+1:index2])
c = int(abc[index2+1:])
if(a < b):
    if(b < c): print(b)
    elif(a > c): print(a)
    else: print(c)
elif(c < b): print(b)
elif(c > a): print(a)
else: print(c)