nums = list(map(int, input().split(', ')))
indices = [ind for ind in range(len(nums)) if nums[ind] % 2 == 0]

print(indices)