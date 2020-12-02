import re
data = input()
numbers = [n.group(0) for n in re.finditer(r'(^|(?<=\s))-*\d+(\.\d+)*($|(?=\s))', data)]
print(*numbers, sep=' ')