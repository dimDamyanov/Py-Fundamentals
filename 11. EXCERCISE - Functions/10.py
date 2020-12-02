from sys import maxsize
data = list(map(int, input().split()))


def manipulate(command: str, arr: list):
    command = command.split()
    if command[0] == 'exchange':
        if int(command[1]) in range(len(arr)):
            arr[:] = arr[(int(command[1]) + 1):] + arr[:(int(command[1]) + 1)]
            return
        else:
            print('Invalid index')
            return
    elif command[0] == 'max':
        remainder = 1 if command[1] == 'odd' else 0
        max_ind = None
        max_num = -maxsize
        for ind, num in enumerate(arr):
            if num % 2 == remainder and num >= max_num:
                max_ind, max_num = ind, num
        if max_ind is None:
            print('No matches')
            return
        else:
            print(max_ind)
            return
    elif command[0] == 'min':
        remainder = 1 if command[1] == 'odd' else 0
        min_ind = None
        min_num = maxsize
        for ind, num in enumerate(arr):
            if num % 2 == remainder and num <= min_num:
                min_ind, min_num = ind, num
        if min_ind is None:
            print('No matches')
            return
        else:
            print(min_ind)
            return
    elif command[0] == 'first':
        if int(command[1]) <= len(arr):
            remainder = 1 if command[2] == 'odd' else 0
            res = []
            for num in arr:
                if num % 2 == remainder:
                    res.append(num)
                    if len(res) == int(command[1]):
                        break
            print(res)
            return
        else:
            print('Invalid count')
            return
    elif command[0] == 'last':
        if int(command[1]) <= len(arr):
            remainder = 1 if command[2] == 'odd' else 0
            res = []
            for num in arr[::-1]:
                if num % 2 == remainder:
                    res.append(num)
                    if len(res) == int(command[1]):
                        break
            print(res[::-1])
        else:
            print('Invalid count')
    else:
        return


line = input()
while line != 'end':
    manipulate(line, data)
    line = input()
print(data)