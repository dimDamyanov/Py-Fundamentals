nums = list(map(int, input().split(', ')))
groups = []
while nums:
    group = [e for e in nums if e <= (len(groups)+1)*10]
    groups.append(group)
    nums = [e for e in nums if e not in group]

for index, group in enumerate(groups):
    print(f'Group of {(index + 1) * 10}\'s: {group}')