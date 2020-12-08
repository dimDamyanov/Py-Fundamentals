n = int(input())
dragons = {}

for i in range(n):
    d_type, name, damage, health, armor = input().split()
    try:
        damage = int(damage)
    except ValueError:
        damage = 45
    try:
        health = int(health)
    except ValueError:
        health = 250
    try:
        armor = int(armor)
    except ValueError:
        armor = 10
    if d_type in dragons:
        dragons[d_type][name] = [damage, health, armor]
    else:
        dragons[d_type] = {name: [damage, health, armor]}

for d_type, val in dragons.items():
    avg_damage = sum([e[0] for e in val.values()]) / len(val)
    avg_health = sum([e[1] for e in val.values()]) / len(val)
    avg_armor = sum([e[2] for e in val.values()]) / len(val)
    print(f'{d_type}::({avg_damage:.2f}/{avg_health:.2f}/{avg_armor:.2f})')
    val = dict(sorted(val.items(), key=lambda x: x[0]))
    for d in val:
        print(f'-{d} -> damage: {val[d][0]}, health: {val[d][1]}, armor: {val[d][2]}')