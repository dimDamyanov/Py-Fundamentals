import re
data = input()
names = re.findall(r"\b[A-Z][a-z]+ [A-Z][a-z]+\b", data)
print(*names, sep=' ')