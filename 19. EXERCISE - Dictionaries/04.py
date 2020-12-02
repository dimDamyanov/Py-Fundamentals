products = {}
line = input()
while line != 'buy':
    data = line.split()
    if data[0] in products:
        products[data[0]] = [products[data[0]][0]+int(data[2]), float(data[1])]
    else:
        products[data[0]] = [int(data[2]), float(data[1])]
    line = input()
for key, value in products.items():
    print(f'{key} -> {value[0]*value[1]:.2f}')