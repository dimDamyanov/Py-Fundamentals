num = int(input())


def tribonacci(n: int):
    t = [1]
    for i in range(n - 1):
        t_n = 0
        for j in range(3):
            if i-j >= 0:
                t_n += t[i-j]
        if t_n != 0:
            t.append(t_n)
    return t


print(*tribonacci(num))