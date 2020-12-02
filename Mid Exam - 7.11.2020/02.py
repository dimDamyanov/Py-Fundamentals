chest = list(input().split('|'))

line = input()
while line != 'Yohoho!':
    data = line.split()
    if data[0] == 'Loot':
        for i in range(1, len(data)):
            if data[i] not in chest:
                chest.insert(0, data[i])
    elif data[0] == 'Drop':
        if 0 <= int(data[1]) < len(chest):
            chest.append(chest.pop(int(data[1])))
    elif data[0] == 'Steal':
        stolen = []
        if int(data[1]) > len(chest):
            stolen = chest
        else:
            stolen = chest[len(chest)-int(data[1]):]
        print(*stolen, sep=', ')
        chest = [e for e in chest if e not in stolen]
    line = input()

if chest:
    s = sum([len(e) for e in chest])
    print(f'Average treasure gain: {(s/len(chest)):.2f} pirate credits.')
else:
    print('Failed treasure hunt.')
