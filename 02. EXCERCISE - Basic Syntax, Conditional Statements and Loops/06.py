from sys import maxsize


def happy_num(num):
    a = [0] * 10
    while num != 0:
        a[num % 10] += 1
        num //= 10
    for e in a:
        if e > 1:
            return False
    return True


year = int(input())
year += 1
while year < maxsize:
    if happy_num(year) == True:
        print(year)
        break
    else:
        year += 1
