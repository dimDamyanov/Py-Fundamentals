import re
urls = []
while True:
    data = input()
    if not data:
        break
    urls.extend([e.group(0) for e in re.finditer(r'www.[A-Za-z0-9-]+(\.[a-z]+)+', data)])
print(*urls, sep='\n')