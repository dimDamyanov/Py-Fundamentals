import re

data = input()
variable_dict = [e.groupdict() for e in re.finditer(r'(^|(?<=\s))_(?P<name>[A-Za-z]+)($|(?=\s))', data)]
variables = [v['name'] for v in variable_dict]
print(*variables, sep=',')