string = str(input())
alphabet = 'abcdefghijklmnopqrstuvwxyz'
spl = ','
i = string[0]
n_ = ''
index_i = 0

for char in string[::-1]:
    if char != spl:
        n_ += char
    else: break
    
n = int(n_)

for j in range(len(alphabet)):
    if alphabet[j] == i:
        index_i = j
index_k = (index_i + n) % 26
k = alphabet[index_k]
print(k)
        
    
    
    

        
