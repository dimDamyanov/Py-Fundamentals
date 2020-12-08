dwarfs = {}
line = input()

while line != 'Once upon a time':
    name, color, phy = line.split(' <:> ')
    phy = int(phy)
    if color in dwarfs:
        if name in dwarfs[color]:
            if phy > dwarfs[color][name]:
                dwarfs[color][name] = phy
        else:
            dwarfs[color][name] = phy
    else:
        dwarfs[color] = {name: phy}
    line = input()

order = []
for color, d in dwarfs.items():
    n = len(d)
    for name, phy in d.items():
        order.append((name, color, phy, n))

order.sort(key=lambda x: (-x[2], -x[3]))
for dwarf in order:
    print(f'({dwarf[1]}) {dwarf[0]} <-> {dwarf[2]}')