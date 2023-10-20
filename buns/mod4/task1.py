numbers = input().split()
uniq = set(numbers)
if len(uniq) == len(numbers):
    print("Все числа разные")
elif len(uniq) == 1:
    print("Все числа равны")
else:
    print("Есть равные и неравные числа")

