key = int(input())
n = int(input())
message = []
for i in range(n):
    c = input()
    message.append(chr(ord(c) + key))
print(*message, sep='')
