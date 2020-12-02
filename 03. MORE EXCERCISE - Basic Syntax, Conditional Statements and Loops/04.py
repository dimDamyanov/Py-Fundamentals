n = 0
last = ''
for i in range(len(s)):
    last += s[i]
    if i > 1:
        test = ''
        for j in range(4, 0, -1):
            test += last[len(last) - j]
        if test == 'sand':
            n += 1
        test = ''
        for j in range(5, 0, -1):
            test += last[len(last) - j]
        if test == 'water':
            n += 1
        test = ''
        for j in range(4, 0, -1):
            test += last[len(last) - j]
        if test == 'fish':
            n += 1
        test = ''
        for j in range(3, 0, -1):
            test += last[len(last) - j]
        if test == 'sun':
            n += 1
print(n)
