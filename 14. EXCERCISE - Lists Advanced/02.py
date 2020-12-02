nums = input().split()
biggest = sorted(nums, reverse=True)
print(*biggest, sep='')