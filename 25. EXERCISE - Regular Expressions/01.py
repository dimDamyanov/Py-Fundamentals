import re

numbers = []
while True:
    data = input()
    if not data:
        break
    numbers.extend([e.group(0) for e in re.finditer('[0-9]+', data)])
print(*numbers, sep=' ')