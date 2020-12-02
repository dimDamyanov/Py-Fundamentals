items = input().split(', ')
line = input()

while line != 'Craft!':
    data = line.split(' - ')
    if data[0] == 'Collect':
        if data[1] not in items:
            items.append(data[1])
    elif data[0] == 'Drop':
        if data[1] in items:
            items.remove(data[1])
    elif data[0] == 'Combine Items':
        tokens = data[1].split(':')
        if tokens[0] in items:
            items.insert((items.index(tokens[0]) + 1), tokens[1])
    elif data[0] == 'Renew':
        if data[1] in items:
            items.remove(data[1])
            items.append(data[1])
    line = input()

print(*items, sep=', ')