n = int(input())
nums = []
for i in range(n):
    num = int(input())
    nums.append(num)

command = input().casefold()
result_nums = []
for e in nums:
    if command == 'even':
        if e % 2 == 0:
            result_nums.append(e)
    elif command == 'odd':
        if e % 2 == 1:
            result_nums.append(e)
    elif command == 'negative':
        if e < 0:
            result_nums.append(e)
    elif command == 'positive':
        if e >= 0:
            result_nums.append(e)

print(result_nums)
