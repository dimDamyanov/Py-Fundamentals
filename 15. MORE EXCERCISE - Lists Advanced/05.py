def format_start():
    global maze
    for row in range(len(maze)):
        for col in range(len(maze[0])):
            if maze[row][col] == 'k':
                maze[row][col] = 1


def find_exits():
    global maze
    exits = []
    for row in range(len(maze)):
        for col in range(len(maze[row])):
            # if row == 0:
            #     if maze[row][col] == ' ' or maze[row][col] == 1:
            #         exits.append((row, col))
            if row == len(maze) - 1:
                if maze[len(maze) - 1][col] == ' ' or maze[len(maze) - 1][col] == 1:
                    exits.append((row, col))
            if col == 0:
                if maze[row][col] == ' ' or maze[row][col] == 1:
                    exits.append((row, col))
            if col == len(maze[row]) - 1:
                if maze[row][col] == ' ' or maze[row][col] == 1:
                    exits.append((row, col))
    return exits


def make_step(k):
    global maze
    dead_end = True
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == k:
                if i > 0 and maze[i - 1][j] == ' ':
                    maze[i - 1][j] = k + 1
                    dead_end = False
                if j > 0 and maze[i][j - 1] == ' ':
                    maze[i][j - 1] = k + 1
                    dead_end = False
                if i < (len(maze) - 1) and maze[i + 1][j] == ' ':
                    maze[i + 1][j] = k + 1
                    dead_end = False
                if j < (len(maze[0]) - 1) and maze[i][j + 1] == ' ':
                    maze[i][j + 1] = k + 1
                    dead_end = False
    return dead_end


n = int(input())
maze = []
finished = True
for l in range(n):
    line = list(input())
    maze.append(line)
format_start()
exits_points = find_exits()
if exits_points:
    m = 0
    while not [e for e in exits_points if maze[e[0]][e[1]] != ' ']:
        m += 1
        if make_step(m):
            finished = False
            break
    if finished:
        print(f'Kate got out in {"".join(map(str,set([maze[e[0]][e[1]] for e in exits_points if maze[e[0]][e[1]] != " "])))} moves')
        exit()
print('Kate cannot get out')