import re

pattern = r'@(?P<name>[a-zA-Z]+)[^@!:>-]*:(?P<population>\d+)[^@!:>-]*!(?P<attack>[AD])![^@!:>-]*->(?P<soldiers>\d+)'

planets = {'A': [], 'D': []}
n = int(input())
for _ in range(n):
    line = input()
    s_count = len(re.findall('s', line, re.IGNORECASE))
    t_count = len(re.findall('t', line, re.IGNORECASE))
    a_count = len(re.findall('a', line, re.IGNORECASE))
    r_count = len(re.findall('r', line, re.IGNORECASE))
    count = s_count + t_count + a_count + r_count
    res = []
    for c in line:
        res.append(chr(ord(c)-count))
    message = ''.join(res)
    raw = re.search(pattern, message)
    if raw:
        data = raw.groupdict()
        planets[data['attack']].append(data['name'])
for key in planets:
    planets[key].sort()
print(f'Attacked planets: {len(planets["A"])}')
for p in planets["A"]:
    print(f'-> {p}')
print(f'Destroyed planets: {len(planets["D"])}')
for p in planets["D"]:
    print(f'-> {p}')
