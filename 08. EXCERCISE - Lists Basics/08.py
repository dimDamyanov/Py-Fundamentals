data = input().split('#')
water = int(input())
effort = 0
put_out = []
for entry in data:
    cell = entry.split(' = ')
    if cell[0] == 'High' and 81 <= int(cell[1]) <= 125:
        if water >= int(cell[1]):
            water -= int(cell[1])
            effort += (25 / 100) * int(cell[1])
            put_out.append(int(cell[1]))
        continue
    elif cell[0] == 'Medium' and 51 <= int(cell[1]) <= 80:
        if water >= int(cell[1]):
            water -= int(cell[1])
            effort += (25 / 100) * int(cell[1])
            put_out.append(int(cell[1]))
        continue
    elif cell[0] == 'Low' and 1 <= int(cell[1]) <= 50:
        if water >= int(cell[1]):
            water -= int(cell[1])
            effort += (25 / 100) * int(cell[1])
            put_out.append(int(cell[1]))
        continue
    else:
        continue
print('Cells:')
for e in put_out:
    print(f' - {e}')
print(f'Effort: {effort:.2f}\nTotal Fire: {sum(put_out)}')