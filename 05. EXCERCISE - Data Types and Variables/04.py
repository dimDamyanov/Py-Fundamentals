n = int(input())
char_sum = 0
for i in range(n):
    c = input()
    char_sum += ord(c)

print(f'The sum equals: {char_sum}')