pirate_ship = list(map(int, input().split('>')))
warship = list(map(int, input().split('>')))
max_h = int(input())
draw = True

line = input()
while line != 'Retire':
    data = line.split()
    if data[0] == 'Fire':
        if 0 <= int(data[1]) < len(warship):
            if warship[int(data[1])] <= int(data[2]):
                print('You won! The enemy ship has sunken.')
                draw = False
                break
            else:
                warship[int(data[1])] -= int(data[2])
    elif data[0] == 'Defend':
        if 0 <= int(data[1]) < len(pirate_ship) and 0 <= int(data[2]) < len(pirate_ship):
            for i in range(int(data[1]), int(data[2]) + 1):
                if pirate_ship[i] <= int(data[3]):
                    print('You lost! The pirate ship has sunken.')
                    draw = False
                    break
                else:
                    pirate_ship[i] -= int(data[3])
    elif data[0] == 'Repair':
        if 0 <= int(data[1]) < len(pirate_ship):
            if pirate_ship[int(data[1])] + int(data[2]) <= max_h:
                pirate_ship[int(data[1])] += int(data[2])
            else:
                pirate_ship[int(data[1])] = max_h
    elif data[0] == 'Status':
        rep = len([s for s in pirate_ship if s < 0.2 * max_h])
        print(f'{rep} sections need repair.')
    line = input()

if draw:
    print(f'Pirate ship status: {sum(pirate_ship)}')
    print(f'Warship status: {sum(warship)}')