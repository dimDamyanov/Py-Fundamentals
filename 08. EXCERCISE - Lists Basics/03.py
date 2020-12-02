line = input().split()
cards = set(line)
players_a = 11
players_b = 11
terminated = False
for card in cards:
    team = card.split('-')[0].casefold()
    if team == 'a':
        players_a -= 1
    elif team == 'b':
        players_b -= 1

    if players_a == 6 or players_b == 6:
        terminated = True
        break

print(f'Team A - {players_a}; Team B - {players_b}')
if terminated:
    print('Game was terminated')