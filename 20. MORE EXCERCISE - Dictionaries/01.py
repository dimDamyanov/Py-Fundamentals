contests = {}
candidates = {}
line = input()
while line != 'end of contests':
    contest, password = line.split(':')
    contests[contest] = password
    line = input()
line = input()
while line != 'end of submissions':
    contest, password, user, points = line.split('=>')
    points = int(points)
    if contest in contests and password == contests[contest]:
        if user in candidates:
            if (contest in candidates[user] and points > candidates[user][contest]) or contest not in candidates[user]:
                candidates[user][contest] = points
        else:
            candidates[user] = {contest: points}
    line = input()
best_c = sorted(candidates.items(), key=lambda x: -sum([p[1] for p in x[1].items()]))[0]
for key, value in candidates.items():
    candidates[key] = sorted(value.items(), key=lambda x: -x[1])
candidates = sorted(candidates.items(), key=lambda x: x[0])
print(f'Best candidate is {best_c[0]} with total {sum(p[1] for p in best_c[1].items())} points.')
print('Ranking:')
for candidate, submissions in candidates:
    print(candidate)
    for submission in submissions:
        print(f'#  {submission[0]} -> {submission[1]}')