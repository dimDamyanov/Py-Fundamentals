lost_fights = int(input())
price_helmet = float(input())
price_sword = float(input())
price_shield = float(input())
price_armor = float(input())
broken_shields = 0
total = 0

for i in range(1, (lost_fights + 1)):
    if i % 2 == 0:
        total += price_helmet
        if i % 3 == 0:
            broken_shields += 1
            total += price_shield
            if broken_shields % 2 == 0:
                total += price_armor
    if i % 3 == 0:
        total += price_sword

print(f'Gladiator expenses: {total:.2f} aureus')
