n1 = int(input())
n2 = int(input())
n3 = int(input())


def sum_numbers(a, b):
    return a + b


def subtract_numbers(a, b):
    return a - b


def add_and_subtract(a, b, c):
    return subtract_numbers((sum_numbers(a, b)), c)


print(add_and_subtract(n1, n2, n3))