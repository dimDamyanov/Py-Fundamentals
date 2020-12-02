data = input().split('|')
energy = 100
coins = 100
bankrupt = False

for entry in data:
    event = entry.split('-')
    if event[0] == 'rest':
        if energy + int(event[1]) >= 100:
            energy = 100
            print(f'You gained {100 - energy} energy.')
        else:
            energy += int(event[1])
            print(f'You gained {event[1]} energy.')
        print(f'Current energy: {energy}.')
    elif event[0] == 'order':
        if energy >= 30:
            coins += int(event[1])
            energy -= 30
            print(f'You earned {int(event[1])} coins.')
        else:
            print('You had to rest!')
            energy += 50
    else:
        if coins > int(event[1]):
            print(f'You bought {event[0]}.')
            coins -= int(event[1])
        else:
            print(f'Closed! Cannot afford {event[0]}.')
            bankrupt = True
            break

if not bankrupt:
    print(f'Day completed!\nCoins: {coins}\nEnergy: {energy}')