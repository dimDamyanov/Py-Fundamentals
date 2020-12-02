resource = {}
line = input()
while line != 'stop':
    quantity = int(input())
    if line in resource:
        resource[line] += quantity
    else:
        resource[line] = quantity
    line = input()

for key, value in resource.items():
    print(f'{key} -> {value}')
