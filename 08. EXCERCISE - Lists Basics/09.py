data = input().split('|')
budget = int(input())
bought_items = []


for entry in data:
    item = entry.split('->')
    if item[0] == 'Clothes' and float(item[1]) <= 50:
        if budget >= float(item[1]):
            budget -= float(item[1])
            bought_items.append(float(item[1]))
        continue
    elif item[0] == 'Shoes' and float(item[1]) <= 35:
        if budget >= float(item[1]):
            budget -= float(item[1])
            bought_items.append(float(item[1]))
        continue
    elif item[0] == 'Accessories' and float(item[1]) <= 20.50:
        if budget >= float(item[1]):
            budget -= float(item[1])
            bought_items.append(float(item[1]))
        continue
total = 0
for price in bought_items:
    total += 1.4 * price
    print(f'{(price * 1.4):.2f}', end=' ')
print(f'\nProfit: {(total - sum(bought_items)):.2f}')
if (total + budget) >= 150:
    print('Hello, France!')
else:
    print('Time to go.')