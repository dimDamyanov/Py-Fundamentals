n = int(input())
board = []
destroyed = 0
for i in range(n):
    line = list(map(int, input().split()))
    board.append(line)
data = list(input().split())
for attack in data:
    row = int(attack.split('-')[0])
    col = int(attack.split('-')[1])
    if board[row][col] != 0:
        if board[row][col] == 1:
            destroyed += 1
        board[row][col] -= 1
print(destroyed)