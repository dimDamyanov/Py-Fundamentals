import re

split_pattern = r'[, ]+'
health_pattern = r'[^0-9.+*/-]'
damage_pattern = r'[+-]?\d+\.?\d*'
div_mul_pattern = r'[*/]'
demons = {}
line = input()
data = re.split(split_pattern, line)
for d in data:
    health = sum(list(map(ord, re.findall(health_pattern, d))))
    damage = sum(list(map(float, [e.group() for e in re.finditer(damage_pattern, d)])))
    for c in re.findall(div_mul_pattern, d):
        if c == '*':
            damage *= 2
        else:
            damage /= 2
    demons[d] = (health, damage)
demons = sorted(demons.items(), key=lambda x: x[0])
for d, stats in demons:
    print(f'{d} - {stats[0]} health, {stats[1]:.2f} damage')