n = input()
digits = list(map(int, str(n)))
digits.sort(reverse=True)
print(*digits, sep='')
