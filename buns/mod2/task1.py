string = str(input())
a_ = ''
b_ = ''
symb_comma = ','
symb_space = ' '
for char in string:
    if char != symb_comma:
        a_ += char
    else: break
for char in string[::-1]:
     if char != symb_space:
        b_ += char
     else: break
a = int(a_)
b = int(b_[::-1])
c = a % b
print(c)
