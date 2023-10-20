letters = {}
with open('5задание.txt', 'r') as file:
    for line in file:
        for char in line:
            if char.isalpha():
                if char in letters:
                    letters[char] += 1
                else:
                    letters[char] = 1

sorted_letters = sorted(letters.items(), key=lambda x: x[1])

with open('результат.txt', 'w') as result_file:
    for letter, count in sorted_letters:
        result_file.write(f'{letter}: {count}\n')
