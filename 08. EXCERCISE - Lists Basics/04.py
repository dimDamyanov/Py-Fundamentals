offers = list(map(int, input().split(', ')))
beggars = int(input())
sums = [0] * beggars
i = 0
while offers:
    sums[i] += offers.pop(0)
    i += 1
    if i == beggars:
        i = 0
print(sums)
