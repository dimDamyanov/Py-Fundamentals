n1 = float(input())
n2 = float(input())
n3 = float(input())


def prod_sign(*args):
    negatives = 0
    for arg in args:
        if arg == 0:
            return 'zero'
        elif arg < 0:
            negatives += 1
    return 'positive' if negatives % 2 == 0 else 'negative'


print(prod_sign(n1, n2, n3))