s = input().replace(' ', '')
count = {}
for c in s:
    if c in count:
        count[c] += 1
    else:
        count[c] = 1
for key, value in count.items():
    print(f'{key} -> {value}')