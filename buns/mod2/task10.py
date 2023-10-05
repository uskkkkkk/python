string = str(input())
char = ''
i = 0
split_symb = ' '
while len(string) > i:
    if string[i] == split_symb:
        char = char + string[i - 1]
    i = i + 1
word = char + string[-1]
print(word)

