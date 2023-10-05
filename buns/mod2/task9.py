string = str(input())
glas = 'аоуеёыияюэ'
soglas = 'бвгджзйклмнпрстфхцчщшъь'
count_glas = 0
count_soglas = 0
for char in string:
    if char in glas:
        count_glas += 1
    if char in soglas:
        count_soglas += 1
print(str(count_glas) + ' ' + str(count_soglas))
