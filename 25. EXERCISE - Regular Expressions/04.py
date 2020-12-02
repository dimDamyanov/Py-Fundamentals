import re
data = input()
emails = [e.group(0) for e in re.finditer(r'(^|(?<=\s))[a-z0-9]+[._-]*[a-z0-9]+@[a-z-]+(\.[a-z-]+)+', data, re.IGNORECASE)]
print(*emails, sep='\n')
