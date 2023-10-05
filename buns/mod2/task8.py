string = str(input())
i = string[-1]
s = ''
split_ = ','
counter = 0
for char in string:
    if char != split_:
        s = char + s
    else: break
    
for char in s[::-1]:
    if char == i:
        counter += 1
    else: break
print(counter)
