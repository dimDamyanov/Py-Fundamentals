string = input()
digits = [int(c) for c in string if c.isdigit()]
non_digits = [c for c in string if not c.isdigit()]

take = digits[::2]
skip = digits[1::2]
result = ''
for td, sd in zip(take, skip):
    if td >= len(non_digits):
        result += ''.join(non_digits)
    else:
        result += ''.join(non_digits[:td])
    non_digits = non_digits[td:]
    non_digits = non_digits[sd:]

print(result)