line = input()
index = 0
while index < len(line):
    if line[index] == '>':
        strength = int(line[index + 1])
        index += 1
        while strength:
            if index == len(line):
                break
            if line[index] == '>':
                strength += int(line[index+1])
                index += 1
            line = line[:index] + line[index + 1:]
            strength -= 1
    else:
        index += 1
print(line)