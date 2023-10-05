string = str(input())
nechet = ''
chet = ''
sum_n = 0
sum_c = 0

for i in range(0, len(string), 2):
    nechet += string[i]
for j in range(1, len(string), 2):
    chet += string[j]
    
nechet_ = int(nechet)
chet_ = int(chet)

while (nechet_ != 0):
    sum_n = sum_n + (nechet_ % 10)
    nechet_ = nechet_ // 10
while (chet_ != 0):
    sum_c = sum_c + (chet_ % 10)
    chet_ = chet_ // 10
if (sum_n + 3 * sum_c) % 10 == 0:
    print('yes')
else: print('no')

    
    
    
