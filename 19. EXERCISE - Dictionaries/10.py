submissions = {}
banned = []
line = input()
while line != 'exam finished':
    data = line.split('-')
    username = data[0]
    if len(data) == 3:
        language = data[1]
        points = int(data[2])
        if language in submissions:
            submissions[language].append((username, points))
        else:
            submissions[language] = [(username, points)]
    else:
        banned.append(username)
    line = input()

results = {}
for l_sub in submissions.values():
    for sub in l_sub:
        user, p = sub
        if user not in banned:
            if user in results and results[user] < p:
                results[user] = p
            elif user not in results:
                results[user] = p

results = sorted(results.items(), key=lambda x: (-x[1], x[0]))
print('Results:')
for u, r in results:
    print(f'{u} | {r}')
print('Submissions:')
submissions = sorted(submissions.items(), key=lambda x: (-len(x[1]), x[0]))
for l, sub in submissions:
    print(f'{l} - {len(sub)}')
