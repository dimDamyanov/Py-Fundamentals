key = list(map(int, input().split()))

line = input()
while line != 'find':
    i = 0
    j = 0
    res = []
    while i < len(line):
        if j == len(key):
            j = 0
        res.append(chr(ord(line[i])-key[j]))
        i += 1
        j += 1
    res = ''.join(res)
    treasure = res[res.find('&')+1:res.find('&', res.find('&')+1)]
    coords = res[res.find('<')+1:res.find('>')]
    print(f'Found {treasure} at {coords}')
    line = input()