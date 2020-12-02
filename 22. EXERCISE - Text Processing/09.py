line = input()
result = ''
current = ''
for i in range(len(line)):
    if line[i].isdigit():
        if i < len(line) - 1 and line[i+1].isdigit():
            result += (current * (int(line[i]) * 10 + int(line[i+1]))).upper()
        else:
            result += (current * int(line[i])).upper()
        current = ''
    else:
        current += line[i]
print(f'Unique symbols used: {len(set(result))}')
print(result)