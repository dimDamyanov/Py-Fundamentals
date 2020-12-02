from math import ceil, sqrt


def prime(a: int):
    if a < 2:
        return False
    elif a == 2:
        return True
    else:
        for i in range(2, (ceil(sqrt(a)) + 1)):
            if a % i == 0:
                return False
        return True


n = int(input())
print(prime(n))
