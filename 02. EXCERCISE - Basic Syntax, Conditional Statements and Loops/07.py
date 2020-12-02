n = int(input())
b = int(input())
for i in range(b, 0, -1):
    if i % n == 0:
        print(i)
        break
