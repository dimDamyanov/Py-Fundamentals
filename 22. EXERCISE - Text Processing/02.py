s = input().split()
s.sort(key=lambda x: -len(x))
sum_c = 0
for i in range(len(s[0])):
    if i < len(s[1]):
        sum_c += ord(s[0][i]) * ord(s[1][i])
    else:
        sum_c += ord(s[0][i])
print(sum_c)
