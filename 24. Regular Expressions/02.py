import re
data = input()
phones = [e.group(0) for e in re.finditer(r'\+359([- ])2\1[0-9]{3}\1[0-9]{4}\b', data)]
print(*phones, sep=', ')