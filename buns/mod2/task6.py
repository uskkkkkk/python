domain = str(input())
point = '.'
domain_ = ''
for i in range(0, len(domain)):
    if domain[i] != point:
        domain_ = domain[i] + domain_
    else:
        print(domain_[::-1])
        domain_ = ''
print(domain_[::-1])
