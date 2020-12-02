courses = {}
line = input()
while line != 'end':
    data = line.split(' : ')
    if data[0] in courses:
        courses[data[0]].append(data[1])
    else:
        courses[data[0]] = [data[1]]
    line = input()
courses = sorted(courses.items(), key=lambda x: len(x[1]), reverse=True)
for i in range(len(courses)):
    _, names = courses[i]
    names.sort()

for c, names in courses:
    print(f'{c}: {len(names)}')
    for n in names:
        print(f'-- {n}')