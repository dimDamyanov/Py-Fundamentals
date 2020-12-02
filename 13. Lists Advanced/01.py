n = int(input())
wagons = [0] * n
line = input()

while line != 'End':
    data = line.split()
    if data[0] == 'add':
        wagons[n-1] += int(data[1])
    elif data[0] == 'insert':
        wagons[int(data[1])] += int(data[2])
    elif data[0] == 'leave':
        if wagons[int(data[1])] > int(data[2]):
            wagons[int(data[1])] -= int(data[2])
        else:
            wagons[int(data[1])] = 0
    line = input()

print(wagons)