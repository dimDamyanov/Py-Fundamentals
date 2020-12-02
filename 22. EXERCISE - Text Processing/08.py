lowers = {chr(i): i-96 for i in range(97, 123)}
uppers = {chr(i): i-64 for i in range(65, 91)}
data = input().split()
result = 0
for s in data:
    c_s = s[0]
    c_e = s[-1]
    n = int(s[1:-1])
    if c_s.isupper():
        n /= uppers[c_s]
    else:
        n *= lowers[c_s]
    if c_e.isupper():
        n -= uppers[c_e]
    else:
        n += lowers[c_e]
    result += n
print(f'{result:.2f}')