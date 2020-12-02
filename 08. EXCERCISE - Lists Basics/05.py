deck = input().split()
n = int(input())


def faro_shuffle(l: list):
    l_new = [l[0]]
    l1 = l[1:int(len(l) / 2)]
    l2 = l[int(len(l) / 2):-1]
    for j in range(len(l) - 2):
        if j % 2 == 0:
            l_new.append(l2[int(j / 2)])
        else:
            l_new.append(l1[int(j / 2)])
    l_new.append(l[len(l) - 1])
    return l_new


for i in range(n):
    deck = faro_shuffle(deck)

print(deck)
