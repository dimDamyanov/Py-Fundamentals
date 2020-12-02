n = int(input())
board = []


def findIsland(row: int, col: int, visited: list, island: list):
    global board
    h = len(board)
    l = len(board[0])
    if row < 0 or col < 0 or row >= h or col >= l or (row, col) in visited or board[row][col] == 0:
        return
    absolute_pos = (row, col)
    island.append(absolute_pos)
    visited.append((row, col))
    findIsland(row + 1, col, visited, island)
    findIsland(row - 1, col, visited, island)
    findIsland(row, col + 1, visited, island)
    findIsland(row, col - 1, visited, island)


def findDistinctIslands():
    global board
    rows = len(board)
    if rows == 0:
        return
    cols = len(board[0])
    visited = []
    islands = set()
    for i in range(rows):
        for j in range(cols):
            if board[i][j] == 1 and not (i, j) in visited:
                island = []
                findIsland(i, j, visited, island)
                islands.add(tuple(island))
    return len(islands)


for k in range(n):
    line = list(map(int, input().split()))
    board.append(line)

print(findDistinctIslands())
