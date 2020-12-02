order = input()
n = int(input())


def calc_price(item, quantity):
    if item == 'coffee':
        return 1.5 * quantity
    elif item == 'water':
        return 1 * quantity
    elif item == 'coke':
        return 1.4 * quantity
    elif item == 'snacks':
        return 2 * quantity
    else:
        return


print(f'{calc_price(order, n):.2f}')