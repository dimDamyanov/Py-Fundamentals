budget = float(input())
flour_price = float(input())
cozonacs = 0
coloured_eggs = 0

egg_price = flour_price * (75 / 100)
milk_price = flour_price * (125 / 100) / 4
while True:
    if budget < (flour_price + egg_price + milk_price):
        break
    budget -= flour_price
    budget -= egg_price
    budget -= milk_price
    cozonacs += 1
    coloured_eggs += 3
    if cozonacs % 3 == 0:
        coloured_eggs -= (cozonacs - 2)

print(f'You made {cozonacs} cozonacs! Now you have {coloured_eggs} eggs and {budget:.2f}BGN left.')
