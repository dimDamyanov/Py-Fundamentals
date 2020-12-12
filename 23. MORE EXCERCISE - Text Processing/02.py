s_char = input()
e_char = input()
chars = input()
c_sum = 0

for c in chars:
    if s_char < c < e_char:
        c_sum += ord(c)

print(c_sum)