n = int(input())
shell = []
while n:
    if n - 2*(len(shell)+1) ** 2 <= 0:
        shell.append(n)
        n = 0
    else:
        shell.append(2*(len(shell)+1) ** 2)
        n -= 2*(len(shell)) ** 2

print(shell)