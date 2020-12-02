l = list(map(int, input().split()))
n = int(input())
for i in range(n):
    l.remove(min(l))
print(l)
