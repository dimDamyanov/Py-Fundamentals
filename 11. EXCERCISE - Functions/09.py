n1 = int(input())
n2 = int(input())


def fact(a):
    return 1 if a == 1 else a * fact(a - 1)


print('%.2f' % (fact(n1) / fact(n2)))