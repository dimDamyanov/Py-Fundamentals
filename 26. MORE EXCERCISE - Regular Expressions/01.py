import re

participants = input().split(', ')
results = {}
line = input()
while line != 'end of race':
    name = ''.join(re.findall('[a-zA-Z]', line))
    distance = sum(map(int, re.findall('[0-9]', line)))
    if name in participants:
        if name in results:
            results[name] += distance
        else:
            results[name] = distance
    line = input()
results = sorted(results.items(), key=lambda x: x[1], reverse=True)
print(f'1st place: {results[0][0]}')
print(f'2nd place: {results[1][0]}')
print(f'3rd place: {results[2][0]}')