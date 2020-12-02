n = int(input())


def perfect_num(a):
    if int(str(a)[-1:]) % 2 == 1:
        return False
    div_sum = 1
    for i in range(2, (a >> 1) + 1):
        if a % i == 0:
            div_sum += i
    return True if div_sum == a else False


if perfect_num(n):
    print(f'We have a perfect number!')
else:
    print(f'It\'s not so perfect.')