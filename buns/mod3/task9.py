with open('9задача.txt', 'r') as file:
    n = file.readline()
    
n = int(n)
x = 0
y = 0

while n > 0:
    if x == y and x >= 0:
        while x != -y - 1 and n > 0:
            n -= 1
            x -= 1

    if x == -y -1:
        while x != y and x < 0 and n > 0:
            n -= 1
            y -= 1
            
    if x == y and x < 0:
        while x != -y and n > 0:
            n -= 1
            x += 1

    if x == -y:
        while x != y and x > 0 and n > 0:
            n -= 1
            y += 1
        

with open('9задача.txt', 'w') as file:
    file.write(str(x) + ' ' + str(y))
