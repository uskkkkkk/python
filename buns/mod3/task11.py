row = input().split()
game_matrix = []
game_matrix.append(row)

k = len(row)

for i in range(k-1):
    row = input().split()
    game_matrix.append(row)

def check_winner(board):
    k = len(board) 
    for i in range(k):
        if all((board[i][j] == board[i][0]) and (board[i][0] != "_") for j in range(1,k)):
            return board[i][0]
    for j in range(k):
        if all((board[i][j] == board[0][j]) and (board[0][j] != "_") for i in range(1,k)):
            return board[0][j]
    if all((board[i][i] == board[0][0]) and (board[0][0] != "_") for i in range(1,k)):
        return board[0][0]
    if all((board[i][k-i-1] == board[0][k-1]) and (board[0][k-1] != "_") for i in range(1,k)):
        return board[0][k-1]
    return "Ничья"

print(check_winner(game_matrix))
