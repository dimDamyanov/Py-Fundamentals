n = int(input())
for i in range(1, (n + 1)):
    result = sum(list(map(int, list(str(i)))))
    if result == 5 or result == 7 or result == 11:
        print(f'{i} -> True')
    else:
        print(f'{i} -> False')
