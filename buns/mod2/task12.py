number = str(input())
n = '123456789+'
b = '-)( '
number_ = ''
for char in number:
    if char in n:
        number_ += char
print(number_)
