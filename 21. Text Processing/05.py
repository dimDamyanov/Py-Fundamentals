s = input()
digits = []
letters = []
others = []
for c in s:
    if c.isdigit():
        digits.append(c)
    elif c.isalpha():
        letters.append(c)
    else:
        others.append(c)
print(f'{"".join(digits)}\n{"".join(letters)}\n{"".join(others)}')