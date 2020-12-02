companies = {}
line = input()
while line != 'End':
    data = line.split(' -> ')
    if data[0] in companies:
        if data[1] not in companies[data[0]]:
            companies[data[0]].append(data[1])
    else:
        companies[data[0]] = [data[1]]
    line = input()
companies = sorted(companies.items(), key=lambda x: x[0])
for c, es in companies:
    print(f'{c}')
    for e in es:
        print(f'-- {e}')