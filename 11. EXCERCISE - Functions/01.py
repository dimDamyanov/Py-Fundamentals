n1 = int(input())
n2 = int(input())
n3 = int(input())


def min_int(a, b, c):
    if a < b:
        return a if a < c else c
    else:
        return b if b < c else c


print(min_int(n1, n2, n3))