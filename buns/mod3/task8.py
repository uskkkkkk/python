number_phone = input()
number = number_phone.replace('-', '').replace(')', '').replace('(', '').replace(' ', '')
print(number)
