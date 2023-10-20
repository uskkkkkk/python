word = input()
a = set()
def is_palindrome_possible(word):
    for i in word:
        if i in a:
            a.remove(i)
        else: a.add(i)
    if len(a)>1:
        return False
    else: return True


def generate_palindrome(word):
    if is_palindrome_possible(word):
        letter_count = {}
        for letter in word:
            if letter in letter_count:
                letter_count[letter] += 1
            else:
                letter_count[letter] = 1
                    
        palindrome = []
        middle_char = ""
            
        for letter, count in letter_count.items():
            if count % 2 != 0:
                middle_char = letter * count
            else: palindrome.extend([letter] * (count // 2))
            
        return "".join(palindrome) + middle_char + "".join(palindrome[::-1])
    return "Нельзя составить палиндром"
print(generate_palindrome(word))    

