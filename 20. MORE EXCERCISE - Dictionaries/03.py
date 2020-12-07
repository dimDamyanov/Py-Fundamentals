pool = {}

line = input()
while line != 'Season end':
    if ' -> ' in line:
        player, position, skill = line.split(' -> ')
        skill = int(skill)
        if player in pool:
            if (position in pool[player] and skill > pool[player][position]) or (position not in pool[player]):
                pool[player][position] = skill
        else:
            pool[player] = {position: skill}
    else:
        players = line.split(' vs ')
        if players[0] in pool and players[1] in pool:
            total_skill = [0, 0]
            common_pos = [pos for pos in pool[players[0]] if pos in pool[players[1]]]
            if common_pos:
                for pos in common_pos:
                    total_skill[0] += pool[players[0]][pos]
                    total_skill[1] += pool[players[1]][pos]
            if total_skill[0] > total_skill[1]:
                pool.pop(players[1])
            elif total_skill[0] < total_skill[1]:
                pool.pop(players[0])
    line = input()

for key in pool:
    pool[key] = dict((sorted(pool[key].items(), key=lambda x: (-x[1], x[0]))))
pool = sorted(pool.items(), key=lambda x: (-(sum(x[1].values())), x[0]))

for player, stats in pool:
    print(f'{player}: {sum(stats.values())} skill')
    for key in stats:
        print(f'- {key} <::> {stats[key]}')