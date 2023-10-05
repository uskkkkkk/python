n = int(input())
n1 = n2 = n
binary = ''
octal = ''
hexadecimal = ''
hex_digits = "0123456789ABCDEF"
if n < 0:
    print("Неверный ввод")
else:
     while n > 0:
         binary = str(n % 2) + binary
         n = n// 2
     while n1 > 0:
         octal = str(n1 % 8) + octal
         n1 = n1 // 8
     while n2 > 0:
         hexadecimal = hex_digits[n2 % 16] + hexadecimal
         n2 = n2 // 16
print(binary, octal, hexadecimal)

