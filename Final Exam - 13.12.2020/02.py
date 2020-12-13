import re

validate_pattern = r'(^|(?<=\s))(\$|%)(?P<tag>[A-Z][a-z]{2,})\2: (\[\d+\]\|){3}($|(?=\s))'

n = int(input())
for i in range(n):
    line = input()
    valid = re.match(validate_pattern, line)
    if valid:
        tag = valid.groupdict()['tag']
        nums = list(map(int, re.findall('\[(\d+)\]', line)))
        message = ''.join([chr(e) for e in nums])
        print(f'{tag}: {message}')
    else:
        print('Valid message not found!')