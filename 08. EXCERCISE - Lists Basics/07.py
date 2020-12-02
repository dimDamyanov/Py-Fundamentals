gifts = list(input().split())
line = input()
while line != 'No Money':
    data = line.split()
    if data[0] == 'OutOfStock':
        gifts = [gift if data[1] != gift else None for gift in gifts]
    elif data[0] == 'Required':
        index = int(data[2])
        if index in range(0, len(gifts)):
            gifts[int(data[2])] = data[1]
    elif data[0] == 'JustInCase':
        gifts[len(gifts) - 1] = data[1]
    line = input()

for gift in gifts:
    if gift:
        print(gift, end=' ')