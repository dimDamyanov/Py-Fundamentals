data = input().split()
bakery = {}
for i in range(0, len(data), 2):
    bakery[data[i]] = int(data[i+1])
print(bakery)