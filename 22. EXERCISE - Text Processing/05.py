s = input()
for ind, c in enumerate(s):
    if c == ':':
        print(s[ind:ind+2])