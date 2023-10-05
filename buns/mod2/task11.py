string = str(input())
boolean = False
new_string = ''
split_space = ' '
for char in string:
    if char != split_space:
        new_string += char
        
for i in range(0, len(new_string)):
    for k in range(1, len(new_string)):
        if new_string[i] == new_string[k]:
            boolean = True
        else:
            boolean = False
print(boolean)
