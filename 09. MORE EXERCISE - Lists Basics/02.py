board = []
draw = True
for i in range(3):
    line = tuple(map(int, input().split()))
    board.append(line)

for row in board:
    if len(set(row)) == 1 and row[0] != 0:
        if row[0] == 1:
            print('First player won')
        else:
            print('Second player won')
        draw = False
columns = []

for i in range(len(board[0])):
    column = []
    for j in range(len(board)):
        column.append(board[j][i])
    columns.append(tuple(column))
for column in columns:
    if len(set(column)) == 1 and column[0] != 0:
        if column[0] == 1:
            print('First player won')
        else:
            print('Second player won')
        draw = False

diagonals = []
diagonal = []
for i in range(len(board)):
    diagonal.append(board[i][i])
diagonals.append(tuple(diagonal))
diagonal = []
for i in range(len(board)):
    diagonal.append(board[len(board) - (i + 1)][i])
diagonals.append(diagonal)

for diagonal in diagonals:
    if len(set(diagonal)) == 1 and diagonal[0] != 0:
        if diagonal[0] == 1:
            print('First player won')
        else:
            print('Second player won')
        draw = False

if draw:
    print('Draw!')