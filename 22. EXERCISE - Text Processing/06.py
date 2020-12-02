s = input()
r = []
for c in s:
    if not r or not c == r[len(r) - 1]:
        r.append(c)
print(''.join(r))