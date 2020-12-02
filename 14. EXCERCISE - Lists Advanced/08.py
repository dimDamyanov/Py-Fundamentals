targets = list(map(int, input().split()))
line = input()
while line != 'End':
    data = line.split()
    if data[0] == 'Shoot':
        if 0 <= int(data[1]) < len(targets):
            if int(data[2]) < targets[int(data[1])]:
                targets[int(data[1])] -= int(data[2])
            else:
                targets.pop(int(data[1]))
    elif data[0] == 'Add':
        if 0 <= int(data[1]) < len(targets):
            targets.insert(int(data[1]), int(data[2]))
        else:
            print('Invalid placement!')
    elif data[0] == 'Strike':
        if 0 <= int(data[1]) - int(data[2]) < len(targets) and 0 <= int(data[1]) + int(data[2]) < len(targets):
            [targets.pop(int(data[1]) - int(data[2])) for i in range(1+ 2 * int(data[2]))]
        else:
            print('Strike missed!')
    line = input()

print(*targets, sep='|')