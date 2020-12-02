winning_symbols = '@#$^'


def is_jackpot(s):
    p1 = s[:10]
    p2 = s[10:]
    if p1 == p2 and p1[0] in winning_symbols and len(set(p1)) == 1:
        return True
    else:
        return False


def is_match(s):
    p1 = s[:10]
    p2 = s[10:]
    for ws in winning_symbols:
        for i in range(9, 5, -1):
            if ws * i in p1 and ws * i in p2:
                return ws, i
    return False


tickets = input().split(', ')
for t in tickets:
    ticket = t.strip()
    if not len(ticket) == 20:
        print('invalid ticket')
    else:
        if is_jackpot(ticket):
            print(f'ticket "{ticket}" - {10}{ticket[0]} Jackpot!')
            continue
        match = is_match(ticket)
        if match:
            print(f'ticket "{ticket}" - {match[1]}{match[0]}')
        else:
            print(f'ticket "{ticket}" - no match')