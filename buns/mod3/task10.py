size = int(input())

matrix = [[0] * size for _ in range(size)]
for i in range(size):
    for j in range(size):
        matrix[i][j] = j + 1

for row in matrix:
    print(", ".join(str(num) for num in row))

for i in range(size):
    for j in range(i + 1, size):
        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

print()
for row in matrix:
    print(", ".join(str(num) for num in row))
