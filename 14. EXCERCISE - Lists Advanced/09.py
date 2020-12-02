neighbourhood = list(map(int, input().split('@')))
position = 0
line = input()
while line != 'Love!':
    data = line.split()
    if (position + int(data[1])) >= len(neighbourhood):
        position = 0
    else:
        position += int(data[1])
    if neighbourhood[position] >= 2:
        neighbourhood[position] -= 2
        if neighbourhood[position] == 0:
            print(f'Place {position} has Valentine\'s day.')
    elif neighbourhood[position] == 0:
        print(f'Place {position} already had Valentine\'s day.')
    line = input()

print(f'Cupid\'s last position was {position}.')
if neighbourhood.count(0) == len(neighbourhood):
    print('Mission was successful.')
else:
    print(f'Cupid has failed {len(neighbourhood) - neighbourhood.count(0)} places.')