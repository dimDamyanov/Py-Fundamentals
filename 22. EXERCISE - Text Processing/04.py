s = input()
encrypted = []
for c in s:
    encrypted.append(chr(ord(c)+3))
print(''.join(encrypted))