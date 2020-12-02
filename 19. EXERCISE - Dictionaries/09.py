force_book = {}
line = input()
while line != 'Lumpawaroo':
    if ' | ' in line:
        side, user = line.split(' | ')
        users = [e for l in force_book.values() for e in l]
        if user not in users:
            if side in force_book:
                force_book[side].append(user)
            else:
                force_book[side] = [user]
    if ' -> ' in line:
        user, side = line.split(' -> ')
        users = [e for l in force_book.values() for e in l]
        if user in users:
            for key, value in force_book.items():
                if user in value:
                    force_book[key].remove(user)
                    if len(force_book[key]) == 0:
                        force_book.pop(key)
                    if side in force_book:
                        force_book[side].append(user)
                    else:
                        force_book[side] = [user]
                    break
        else:
            if side in force_book:
                force_book[side].append(user)
            else:
                force_book[side] = [user]
        print(f'{user} joins the {side} side!')
    line = input()

force_book = sorted(force_book.items(), key=lambda x: (-len(x[1]), x[0]))
for side, users in force_book:
    print(f'Side: {side}, Members: {len(users)}')
    for user in sorted(users):
        print(f'! {user}')