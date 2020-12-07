contests = {}
users = {}

line = input()
while line != 'no more time':
    username, contest, points = line.split(' -> ')
    points = int(points)
    if contest in contests.keys():
        if (username in contests[contest].keys() and points > contests[contest][username]) or (username not in contests[contest].keys()):
            contests[contest][username] = points
    else:
        contests[contest] = {username: points}
    line = input()
for key in contests.keys():
    contests[key] = dict(sorted(contests[key].items(), key=lambda x: (-x[1], x[0])))

for key in contests:
    print(f'{key}: {len(contests[key])} participants')
    for ind, user in enumerate(contests[key].items()):
        print(f'{ind+1}. {user[0]} <::> {user[1]}')
        if user[0] in users:
            users[user[0]] += user[1]
        else:
            users[user[0]] = user[1]
users = sorted(users.items(), key=lambda x: (-x[1], x[0]))
print('Individual standings:')
for ind, user in enumerate(users):
    print(f'{ind+1}. {user[0]} -> {user[1]}')
