a = int(input())
b = int(input())
print(f'Before:\na = {a}\nb = {b}')
a += b
b = a - b
a -= b
print(f'After:\na = {a}\nb = {b}')
