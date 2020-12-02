data = list(map(int, input().split()))
n = int(input())
res = []
i = 0
ind = 0
while data:
    i += 1
    if i % n == 0:
        res.append(data.pop(ind))
    else:
        ind += 1
    if ind >= len(data):
        ind = 0
print(str(res).replace(' ', ''))