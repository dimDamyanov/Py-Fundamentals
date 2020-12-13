line = input()
guests = {}
disliked = 0
while line != 'Stop':
    tokens = line.split('-')
    if tokens[0] == 'Like':
        if tokens[1] not in guests:
            guests[tokens[1]] = [tokens[2]]
        elif tokens[2] not in guests[tokens[1]]:
            guests[tokens[1]].append(tokens[2])
    elif tokens[0] == 'Unlike':
        if tokens[1] in guests:
            if tokens[2] in guests[tokens[1]]:
                guests[tokens[1]].remove(tokens[2])
                disliked += 1
                print(f'{tokens[1]} doesn\'t like the {tokens[2]}.')
            else:
                print(f'{tokens[1]} doesn\'t have the {tokens[2]} in his/her collection.')
        else:
            print(f'{tokens[1]} is not at the party.')
    line = input()
guests = sorted(guests.items(), key=lambda x: (-len(x[1]), x[0]))
for g, meals in guests:
    print(f'{g}: {", ".join(meals)}')
print(f'Unliked meals: {disliked}')