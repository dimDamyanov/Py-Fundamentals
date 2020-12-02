products = {}
line = input()
while line != 'statistics':
    data = line.split(': ')
    if data[0] in products:
        products[data[0]] += int(data[1])
    else:
        products[data[0]] = int(data[1])
    line = input()

print('Products in stock:')
for key in products:
    print(f'- {key}: {products[key]}')
print(f'Total Products: {len(products)}\nTotal Quantity: {sum(products.values())}')