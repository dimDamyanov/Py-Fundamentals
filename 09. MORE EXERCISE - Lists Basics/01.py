data = list(map(int, input().split(', ')))
zeros = 0
res = []
for digit in data:
    if digit != 0:
        res.append(digit)
    else:
        zeros += 1
for i in range(zeros):
    res.append(0)
print(res)