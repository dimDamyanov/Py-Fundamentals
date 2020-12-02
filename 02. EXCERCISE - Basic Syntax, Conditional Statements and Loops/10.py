quantity = int(input())
days_total = int(input())
spirit = 0
money_spent = 0
for day in range(1, (days_total + 1)):
    if day % 11 == 0:
        quantity += 2
    if day % 2 == 0:
        money_spent += (2 * quantity)
        spirit += 5
    if day % 3 == 0:
        money_spent += (8 * quantity)
        spirit += 13
    if day % 5 == 0:
        money_spent += (15 * quantity)
        spirit += 17
        if day % 3 == 0:
            spirit += 30
    if day % 10 == 0:
        spirit -= 20
        money_spent += 23
        if day == days_total:
            spirit -= 30

print(f'Total cost: {money_spent}\nTotal spirit: {spirit}')
