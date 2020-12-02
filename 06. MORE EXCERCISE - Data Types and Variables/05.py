n = int(input())
parentheses_count = 0
balanced = True
for i in range(n):
    line = input()
    if balanced:
        if line == '(':
            parentheses_count += 1
            if parentheses_count > 1:
                balanced = False
                continue
        elif line == ')':
            if parentheses_count == 0:
                balanced = False
            else:
                parentheses_count -= 1

if parentheses_count > 0:
    balanced = False

print('BALANCED') if balanced else print('UNBALANCED')
